---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: 長い音声文字起こし処理の高速化
translated: true
type: note
---

### 30分や1時間の音声処理が長い理由

Google Cloud Speech-to-Text Batch API（v2）は、特に長時間の音声ファイル（ファイルあたり最大約1時間）を処理する`"long"`モデルを使用した、非同期の長時間実行操作向けに設計されています。これが「長すぎる」と感じられる理由は以下の通りです：

- **処理時間は音声の長さに比例**：文字起こしは瞬時には行われません。30分の音声ファイルの場合、5〜20分かかる可能性があります。1時間の音声の場合、10〜40分以上かかることもあります。これには以下が含まれます：
  - キューイング時間（プロジェクト/リージョンが混雑している場合）
  - 実際の文字起こし（長時間音声に対するAIモデル推論は計算集約的）
  - 後処理（単語のタイミング、信頼度スコアなど）
- **バッチ処理の性質**：リアルタイムストリーミングとは異なり、バッチジョブはGoogleのサーバーでバックグラウンド実行されます。スクリプトは`operation.result()`を呼び出してブロック待機しますが、実際の処理は非同期で行われます。
- **その他の要因**：
  - 音声形式/品質：OGG/OpusやM4A/AACはデコードが必要で、サンプルレート/チャンネルが一致しない場合にオーバーヘッドが生じます
  - モデル選択：`"long"`は会議/ポッドキャスト向けに最適化されていますが、`"default"`や`"short"`などの短いモデルより低速です
  - ネットワーク/クォータ：GCSへのアップロード、API呼び出し、結果のダウンロードによりレイテンシが追加されます。無料枠のクォータや高需要によりジョブが遅延する可能性があります
  - 組み込みの並列処理なし：スクリプトはファイルを1つずつ順次処理します

音声が常に30分以上の場合、現在の設定は迅速な処理には理想的ではありません。オフライン/一括処理向けです。

### 解決方法：処理時間の短縮

長時間音声をより高速に処理するには、**ファイルを小さなチャンクに分割する**（例：各5〜15分）ことが重要です。これにより以下が可能になります：
- 並列処理（複数のバッチジョブを同時実行）
- 高速なモデルの使用（チャンクごとに`"short"`や`"default"`など）
- ジョブあたりの待機時間の短縮（ファイル全体で30分以上ではなく、チャンクごとに1〜5分）

#### ステップ1：音声ファイルの分割
**FFmpeg**（無料のコマンドラインツール）を使用して、エンコードなしでファイルを分割します（高速でロスレス）。必要に応じてFFmpegをインストールしてください（例：macOSでは`brew install ffmpeg`、Linuxでは`apt install ffmpeg`）。

入力ファイルを分割する関数をスクリプトに追加します。以下は分割機能を統合した更新版スクリプトです：

```python
import os
import argparse
import subprocess
import tempfile
from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import sys
import time  # ポーリング用

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api  # noqa: F401

MAX_AUDIO_LENGTH_SECS = 20 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"
CHUNK_DURATION_SECS = 600  # チャンクあたり10分; 必要に応じて調整（例：15分の場合は900）


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    FFmpegを使用して音声ファイルを小さなチャンクに分割します。
    
    Args:
        input_file: 入力音声ファイルのパス
        chunk_duration_secs: 各チャンクの秒単位の長さ
    
    Returns:
        チャンクファイルパスのリスト
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # チャンク用の一時ディレクトリを作成
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # FFmpegコマンド（速度のため再エンコードなし）
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # 出力形式
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # 再エンコードせずにストリームをコピー
        "-map", "0",  # すべてのストリームをマップ
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # 出力パターン
        "-y"  # 上書き
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # 生成されたチャンクを検索
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # 名前でソート（例：chunk_001、chunk_002）
        print(f"{filename}を{len(chunk_files)}個のチャンクに分割しました。")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"{filename}の分割中にFFmpegエラーが発生しました: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Google Cloud Speech-to-Text Batch APIを使用して音声ファイルを文字起こしします。
    分割後など音声が短い可能性がある場合に高速なモデルを使用するように更新。
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # チャンクの場合、速度のために"short"または"default"モデルを使用（15分未満の場合）
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # チャンクサイズに基づいて調整

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

    print(f"{filename}のバッチ認識を開始しています...")
    operation = client.batch_recognize(request=request)
    
    # 進捗状況のポーリング（詳細は以下を参照）
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # チャンクごとに短いタイムアウト
    print(f"{filename}の文字起こしが完了しました。応答: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    長時間実行操作をポーリングして進捗状況を表示します。
    """
    while not operation.done():
        # 操作メタデータを取得（利用可能な場合; Speech APIは基本的なステータスを提供）
        try:
            metadata = operation.metadata
            print(f"{filename}の進捗: State={getattr(metadata, 'state', 'Unknown')}, "
                  f"Processed={getattr(metadata, 'progress_bytes', 'N/A')} bytes")
        except Exception:
            print(f"{filename}を待機中...（30秒ごとに確認）")
        
        time.sleep(30)  # 30秒ごとにポーリング
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"エラー: {filename}はサポートされていない音声ファイルです（.m4aまたは.oggである必要があります）。")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"{filename}をスキップします: {output_filename}は既に存在します。")
        return

    print(f"処理中: {filename}")

    # 言語を決定
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # ファイルが長い場合にチャンクに分割（ヒューリスティック: >15分、ただしffprobeで長さを調査可能）
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # 大まかなチェック: >100MBは長い可能性が高い
        print(f"ファイルが大きいため、{CHUNK_DURATION_SECS//60}分のチャンクに分割します。")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("分割に失敗しました。単一ファイルとして処理します。")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # 後で結合するため

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # GCSパスを構築
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # 必要に応じてチャンクをアップロード
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"チャンク{chunk_filename}をGCSにアップロードしました。")
        else:
            print(f"チャンク{chunk_filename}は既にGCSに存在します。")

        # 文字起こし
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # トランスクリプトをダウンロードして収集
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # JSONを解析してテキストを抽出（簡略化; 完全な解析にはjsonモジュールを使用）
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"{b.name}をダウンロードして解析しました")

            all_transcripts.append(chunk_transcript)

            # 分割された場合は一時チャンクをクリーンアップ
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"チャンク{chunk_filename}の処理に失敗しました: {e}")

    # すべてのトランスクリプトを1つのファイルに結合
    combined_text = "\n\n--- チャンク境界 ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"結合されたトランスクリプトを{output_filename}に保存しました")

    # 分割が発生した場合は一時ディレクトリをクリーンアップ
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"{filename}の処理が完了しました。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="単一のVoice Memo（.m4a/.ogg）ファイルを処理して文字起こしを生成します。"
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Voice Memoファイルの入力パス。",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="文字起こしの出力ディレクトリ。",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="秒単位のチャンク長（長いファイルを分割する場合）。",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # オーバーライドを許可
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### 主な変更点と利点：
- **分割**：FFmpegを使用して重複しないチャンクを作成（例：各10分）。1時間のファイルの場合、約6つのジョブになり、スレッド/マルチプロセッシングを使用するように変更すれば並列実行可能（例：`concurrent.futures`経由）
- **高速なモデル**：15分未満のチャンクに`"short"`に切り替え - 2〜3倍高速に処理
- **トランスクリプトの結合**：JSON出力を解析し、読みやすいように境界を設けて単一の`.txt`ファイルにマージ
- **クリーンアップ**：必要に応じて一時チャンクと古いGCS blobを削除（ループ内に`blob.delete()`を追加可能）
- **使用方法**：以前と同様に実行、例：`python script.py --input_file long_audio.m4a --chunk_secs 600`。分割しない場合は、大きな`--chunk_secs`を使用（例：3600）

#### その他の最適化：
- **並列処理**：多くのチャンク/ファイルがある場合、Pythonの`ThreadPoolExecutor`を使用して`run_batch_recognize`ジョブを同時に送信（クォータ制限を避けるために5〜10に制限）
- **音声長の調査**：`ffprobe`（FFmpeg）を使用して分割が必要かどうかを動的に決定：`ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`
- **Streaming APIへの切り替え**：対話型使用の場合、同期`recognize`を使用（制限：ファイルあたり約1分）またはライブ用にストリーミングを使用しますが、バッチ長ファイルには理想的ではありません
- **コスト/クォータ**：Google Cloudクォータを確認（Speech-to-Textは約1000リクエスト/分を許可）。長時間ジョブはより多くのクレジットを消費（標準モデルで約$0.036/分）
- **まず短いものでテスト**：速度向上を確認するために`--chunk_secs 300`（5分）から開始

### 進捗状況の表示：操作のポーリング

更新された`poll_operation_with_progress()`関数は、ブロッキング`operation.result()`を置き換えます。これにより：
- 30秒ごとにチェック
- `operation.metadata`からのステータスを表示（例："RUNNING"や"DONE"などの状態、および利用可能な場合は処理済みバイト数 - Speech APIメタデータは基本的ですが、何もないよりはましです）
- 失敗した場合はエラーを発生

より詳細な進捗状況（例：完了率）については、Speech APIは細かいメトリクスを提供しませんが、以下を行うことができます：
- Google Cloud Consoleで監視（プロジェクトのOperationsページ）
- `gcloud` CLIを使用：`gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`
- 完了後、JSON結果にはタイムスタンプを介して間接的に発話ごとの進捗状況が含まれます

分割している場合、複数のチャンクからの進捗状況が交互に表示され、「行き詰まり」感が少なくなります。

これで問題が解決しない場合（例：特定のエラー）、さらなる調整のためにログ/出力を共有してください！