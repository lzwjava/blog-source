---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 加速長音頻轉錄處理
translated: true
type: note
---

### 為什麼30分鐘或1小時音訊的處理時間這麼長？

Google Cloud Speech-to-Text Batch API (v2) 專為非同步長時間運作設計，特別是使用 `"long"` 模型處理較長音訊檔案（每個檔案最長約1小時）。以下是它可能感覺「太長」的原因：

- **處理時間隨音訊長度增加**：轉錄並非即時完成。30分鐘的音訊檔案可能需要5-20分鐘；1小時的檔案則可能需要10-40分鐘或更久。這包括：
  - 佇列等待時間（如果你的專案/區域處於忙碌狀態）。
  - 實際轉錄時間（AI模型推論，對長音訊來說是計算密集型任務）。
  - 後處理（例如：字詞時間戳記、信心分數）。
- **批次處理特性**：與即時串流不同，批次工作在 Google 伺服器後台運行。你的腳本呼叫 `operation.result()` 會阻塞並等待，但實際工作是非同步進行的。
- **其他因素**：
  - 音訊格式/品質：OGG/Opus 或 M4A/AAC 需要解碼，若取樣率/聲道不匹配會增加額外負擔。
  - 模型選擇：`"long"` 模型針對會議/播客優化，但比 `"default"` 或 `"short"` 等短模型慢。
  - 網路/配額：上傳至 GCS、API 呼叫及下載結果都會增加延遲。免費層級配額或高需求可能延遲工作。
  - 無內建平行處理：腳本會依序一次處理一個檔案。

如果你的音訊持續超過30分鐘，目前的設定並不適合快速周轉——它更適合離線/批量處理。

### 如何修正：減少處理時間

要更快處理長音訊，關鍵在於**將檔案分割成較小的區塊**（例如：每個5-15分鐘）。這樣可以：
- 平行處理（同時執行多個批次工作）。
- 使用更快的模型（例如：每個區塊使用 `"short"` 或 `"default"` 模型）。
- 每個工作的等待時間更短（例如：每個區塊1-5分鐘，而非整個檔案30+分鐘）。

#### 步驟1：分割音訊檔案
使用 **FFmpeg**（免費命令列工具）無需重新編碼即可分割檔案（快速且無損）。如果需要請安裝 FFmpeg（例如：macOS 上 `brew install ffmpeg`，Linux 上 `apt install ffmpeg`）。

在你的腳本中加入分割輸入檔案的函式。以下是整合分割功能的更新腳本：

```python
import os
import argparse
import subprocess
import tempfile
from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import sys
import time  # For polling

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api  # noqa: F401

MAX_AUDIO_LENGTH_SECS = 20 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"
CHUNK_DURATION_SECS = 600  # 每個區塊10分鐘；可根據需要調整（例如：900為15分鐘）


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    使用 FFmpeg 將音訊檔案分割成較小的區塊。
    
    Args:
        input_file: 輸入音訊的路徑。
        chunk_duration_secs: 每個區塊的持續時間（秒）。
    
    Returns:
        區塊檔案路徑列表。
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # 為區塊建立暫存目錄
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # FFmpeg 命令（無需重新編碼以提升速度）
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # 輸出格式
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # 無需重新編碼直接複製串流
        "-map", "0",  # 映射所有串流
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # 輸出模式
        "-y"  # 覆寫
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # 尋找生成的區塊
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # 按名稱排序（例如：chunk_001, chunk_002）
        print(f"已將 {filename} 分割成 {len(chunk_files)} 個區塊。")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"使用 FFmpeg 分割 {filename} 時出錯：{e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    使用 Google Cloud Speech-to-Text Batch API 轉錄音訊檔案。
    更新為在音訊可能較短時（例如分割後）使用較短的模型。
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # 對於區塊，使用 "short" 或 "default" 模型以提升速度（如果 <15 分鐘）
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # 根據區塊大小調整

    if file_extension == "ogg":
        decoding = cloud_speech.ExplicitDecodingConfig(
            encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=48000,
            audio_channel_count=1
        )
        config = cloud_speech.RecognitionConfig(
            explicit_decoding_config=decoding,
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )
    else:
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )

    output_config = cloud_speech.RecognitionOutputConfig(
        gcs_output_config=cloud_speech.GcsOutputConfig(uri=output_gcs_folder),
    )

    files = [cloud_speech.BatchRecognizeFileMetadata(uri=audio_gcs_uri)]

    request = cloud_speech.BatchRecognizeRequest(
        recognizer="projects/graphite-ally-445108-k3/locations/global/recognizers/_",
        config=config,
        files=files,
        recognition_output_config=output_config,
    )

    print(f"開始為 {filename} 進行批次辨識...")
    operation = client.batch_recognize(request=request)
    
    # 輪詢進度（詳情見下文）
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # 每個區塊的較短逾時
    print(f"完成 {filename} 的轉錄。回應：{response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    輪詢長時間運作的操作並顯示進度。
    """
    while not operation.done():
        # 取得操作元資料（如果可用；Speech API 提供基本狀態）
        try:
            metadata = operation.metadata
            print(f"{filename} 的進度：狀態={getattr(metadata, 'state', 'Unknown')}, "
                  f"已處理={getattr(metadata, 'progress_bytes', 'N/A')} 位元組")
        except Exception:
            print(f"等待 {filename}...（每30秒檢查一次）")
        
        time.sleep(30)  # 每30秒輪詢一次
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"錯誤：{filename} 不是支援的音訊檔案（.m4a 或 .ogg）。")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"跳過 {filename}：{output_filename} 已存在。")
        return

    print(f"處理中：{filename}")

    # 判斷語言
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # 如果檔案較長則進行分割（啟發式：>15 分鐘，但你可以使用 ffprobe 探查持續時間）
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # 粗略檢查：>100MB 可能較長
        print(f"檔案較大；正在分割成 {CHUNK_DURATION_SECS//60} 分鐘的區塊。")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("分割失敗；以單一檔案處理。")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # 用於後續合併

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # 建構 GCS 路徑
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # 如果需要則上傳區塊
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"已上傳區塊 {chunk_filename} 至 GCS。")
        else:
            print(f"區塊 {chunk_filename} 已在 GCS 中。")

        # 轉錄
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # 下載並收集轉錄稿
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # 解析 JSON 以提取文字（簡化；使用 json 模組進行完整解析）
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"已下載並解析 {b.name}")

            all_transcripts.append(chunk_transcript)

            # 清理暫存區塊（如果已分割）
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"處理區塊 {chunk_filename} 失敗：{e}")

    # 將所有轉錄稿合併為一個檔案
    combined_text = "\n\n--- 區塊邊界 ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"合併後的轉錄稿已儲存至 {output_filename}")

    # 清理暫存目錄（如果進行了分割）
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"完成 {filename} 的處理。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="處理單一語音備忘錄（.m4a/.ogg）檔案以產生轉錄稿。"
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="語音備忘錄檔案的輸入路徑。",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="轉錄稿的輸出目錄。",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="區塊持續時間（秒）（用於分割長檔案）。",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # 允許覆寫
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### 主要變更與優勢：
- **分割**：使用 FFmpeg 建立不重疊的區塊（例如：每個10分鐘）。對於1小時的檔案，約為6個工作，可透過修改使用執行緒/多處理（例如：透過 `concurrent.futures`）來平行執行。
- **更快模型**：對 <15 分鐘的區塊切換至 `"short"` 模型——處理速度快2-3倍。
- **合併轉錄稿**：解析 JSON 輸出並將其合併為單一 `.txt` 檔案，包含邊界以便閱讀。
- **清理**：移除暫存區塊及舊的 GCS blob（如果需要，可在迴圈中加入 `blob.delete()`）。
- **使用方式**：與之前一樣執行，例如：`python script.py --input_file long_audio.m4a --chunk_secs 600`。若不分割，使用較大的 `--chunk_secs`（例如：3600）。

#### 其他優化：
- **平行處理**：如果你有許多區塊/檔案，使用 Python 的 `ThreadPoolExecutor` 同時提交 `run_batch_recognize` 工作（限制在5-10個以避免觸及配額）。
- **探查音訊持續時間**：使用 `ffprobe`（FFmpeg）動態決定是否需要分割：`ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`。
- **切換至串流 API**：對於互動式使用，使用同步 `recognize`（限制約每檔案1分鐘）或串流用於即時，但這不適合批次長檔案。
- **成本/配額**：檢查你的 Google Cloud 配額（Speech-to-Text 允許約每分鐘1000個請求）。長時間工作會消耗更多點數（標準模型約每分鐘 $0.036）。
- **先測試較短的**：從 `--chunk_secs 300`（5分鐘）開始以查看加速效果。

### 顯示進度：輪詢操作

更新後的 `poll_operation_with_progress()` 函式取代了阻塞的 `operation.result()`。它：
- 每30秒檢查一次。
- 從 `operation.metadata` 列印狀態（例如：狀態如 "RUNNING" 或 "DONE"，以及已處理的位元組（如果可用）——Speech API 的元資料是基本的，但總比沒有好）。
- 如果失敗則引發錯誤。

對於更詳細的進度（例如：完成百分比），Speech API 不提供細粒度指標，但你可以：
- 透過 Google Cloud Console 監控（你專案的 Operations 頁面）。
- 使用 `gcloud` CLI：`gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`。
- 完成後，JSON 結果透過時間戳記間接包含每個語句的進度。

如果進行分割，你會看到來自多個區塊的交錯進度，使其感覺較少「卡住」。

如果這未能解決你的問題（例如：特定錯誤），請分享日誌/輸出以進行進一步調整！