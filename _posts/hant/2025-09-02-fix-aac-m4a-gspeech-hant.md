---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復用於Google Speech API的AAC M4A檔案
translated: true
type: note
---

是的——你的檔案是 **AAC 編碼格式封裝在 M4A 容器中**（iPhone 語音備忘錄）。Google Speech-to-Text v2 批次辨識經常無法自動解碼 AAC/M4A 並傳回該確切錯誤。請先轉換為支援的編解碼器/容器格式——然後可以保留 `AutoDetectDecodingConfig()` 或（更好）明確指定解碼設定。

這是最快的解決路徑。

## 選項 A — 使用 `ffmpeg` 的一行指令修復（推薦：Ogg/Opus）

檔案小，準確度高，官方支援。

```bash
# 48 kHz，單聲道，Ogg 容器中的 Opus 編碼
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

然後對新檔案執行你的腳本：

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## 選項 B — 無損 FLAC 格式（同樣支援）

比 WAV 小；無損格式。

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## 選項 C — Linear16 WAV 格式（檔案最大）

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## 程式碼調整（避免再次遇到此問題）

1.  **允許更多副檔名**並以相同方式根據副檔名選擇語言。
2.  **自動轉碼**為支援的格式（我使用 Ogg/Opus）。
3.  **明確告知 API 你傳送的內容**（明確解碼設定）。

將以下內容加入你的腳本（最小化、重點調整）：

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 也受支援

def _transcode_to_ogg_opus(src_path: str) -> str:
    src = Path(src_path)
    dst = src.with_suffix(".ogg")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(src),
        "-vn",
        "-ac", "1",
        "-ar", "48000",
        "-c:a", "libopus",
        "-b:a", "48k",
        str(dst),
    ]
    subprocess.run(cmd, check=True)
    return str(dst)

def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US", decoding="ogg_opus"):
    client = SpeechClient()

    # 優先使用明確解碼設定 — 避免「不支援的編碼」意外
    if decoding == "ogg_opus":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            ogg_opus=cloud_speech.OggOpusDecodingConfig()
        )
    elif decoding == "flac":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            flac=cloud_speech.FlacDecodingConfig()
        )
    elif decoding == "linear16":
        decoding_cfg = cloud_speech.ExplicitDecodingConfig(
            linear16=cloud_speech.Linear16DecodingConfig()
        )
    else:
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # 後備方案

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # 可選：說話者分離、標點符號等
        # speech_adaptation=...
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
    print("Waiting for operation to complete...")
    response = client.batch_recognize(request=request).result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)

def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    src = Path(input_file)
    if not src.exists():
        print(f"Error: {src} does not exist.")
        return

    # 根據副檔名決定語言
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # 確保編碼/容器受支援
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # 輸出閘道，用於你的本地 .txt 檔案（你可以保持原樣或根據 stem 設定）
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # 保留 "audio-files/" 資料夾，保留真實檔案名及新副檔名
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # 根據副檔名選擇解碼方式
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # 後備為自動偵測

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # 下載轉錄結果 JSON 檔案
        blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{src.stem}")
        for b in blobs:
            if b.name.endswith(".json"):
                local_output_path = os.path.join(output_dir, os.path.basename(b.name))
                b.download_to_filename(local_output_path)
                print(f"Downloaded {b.name} to {local_output_path}")

    except Exception as e:
        print(f"Failed to process {src.name}: {e}")

    print(f"Processing complete for {src.name}.")
```

### 為何這能解決問題

*   iOS 語音備忘錄 → **AAC/M4A**。Batch STT v2 無法可靠地自動偵測/解碼此格式。
*   透過轉碼為 **OGG/Opus**（或 **FLAC/WAV**）並**告知 API 使用的編解碼器**，你可以完全避免「不支援的編碼」錯誤。

### 實用提示

*   對於像你 **1 小時 21 分鐘的單聲道語音備忘錄**這樣的長錄音，**OGG/Opus 48k** 能在保持質量的同時縮小檔案大小和 GCS 出口流量。
*   保持單聲道 (`-ac 1`)。立體聲只會使成本加倍而無助於辨識。
*   如果對話是普通話，你的 `"cmn-CN"` 語言代碼是正確的；請按照你現有的做法使用 `"-zh.m4a"` 命名約定。
*   如果你需要說話者轉換，稍後啟用說話者分離；先修復解碼路徑。

如果你需要，我還可以加入可選的**自動本機 → GCS 上傳 + 重新命名**功能，這樣你的 `m4a` 輸入會被接受，但在後台始終以內部 `.ogg` 格式處理。