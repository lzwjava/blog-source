---
audio: false
generated: true
lang: ja
layout: post
title: Google Cloud Transcription
translated: true
---

最近、Google CloudのSpeech-to-Text APIを試してみました。以下は、その文字起こしを行うために使用したPython関数です。

```python
import os
import argparse
from google.cloud import storage

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Google Cloud Speech-to-Text Batch APIを使用して音声ファイルを文字起こしします。

    Args:
        audio_gcs_uri: 音声ファイルのGCS URI。
        output_gcs_folder: 文字起こし結果を保存するフォルダのGCS URI。
        language_code: 文字起こしの言語コード（例: "en-US", "cmn-CN"）。
    """
    client = SpeechClient()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config={},
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
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
    operation = client.batch_recognize(request=request)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
    print(response)


def process_audio_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    all_audio_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
    total_files = len(all_audio_files)
    print(f"処理する音声ファイルの総数: {total_files}")

    if total_files == 0:
        print(f"'{input_dir}' ディレクトリに音声ファイルが見つかりません。")
        return

    files_processed = 0

    for filename in all_audio_files:
        audio_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(output_filename):
            print(f"{filename} をスキップ: {output_filename} は既に存在します。")
            continue
        print(f"\n処理中 {files_processed + 1}/{total_files}: {filename}")
        try:
            # ファイル名のサフィックスに基づいて言語を決定
            if filename.endswith('-zh.mp3') or filename.endswith('-zh.wav') or filename.endswith('-zh.m4a'):
                language_code = "cmn-CN"
            else:
                language_code = "en-US"

            # GCS URIを構築
            gcs_audio_uri = f"gs://test2x/audio-files/{filename}"  # バケットとフォルダを置き換えてください
            gcs_output_uri = f"gs://test2x/transcripts/{os.path.splitext(filename)[0]}" # バケットとフォルダを置き換えてください
            
            # ファイルが存在しない場合はGCSにアップロード
            # この部分は実装されていません。ファイルをGCSにアップロードするコードを追加する必要があります
            # 例えば、google-cloud-storageライブラリを使用して

            storage_client = storage.Client()
            bucket = storage_client.bucket("test2x")
            blob = bucket.blob(f"audio-files/{filename}")
            if not blob.exists():
                blob.upload_from_filename(audio_file_path)
                print(f"{filename} をGCSにアップロードしました。")
            else:
                print(f"{filename} は既にGCSに存在します。")


            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code
            )
            files_processed += 1
            print(f"ファイル {files_processed}/{total_files} を処理しました。\n")

            # 文字起こし結果をダウンロード
            output_gcs_uri_json = f"{gcs_output_uri}/{os.path.splitext(filename)[0]}_transcript_*.json"
            
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{os.path.splitext(filename)[0]}")
            
            for blob in blobs:
                if blob.name.endswith(".json"):
                    local_output_path = os.path.join(output_dir, os.path.basename(blob.name))
                    blob.download_to_filename(local_output_path)
                    print(f"{blob.name} を {local_output_path} にダウンロードしました。")


        except Exception as e:
            print(f"{filename} の処理に失敗しました: {e}")
            continue

    print(f"処理が完了しました！ {files_processed}/{total_files} ファイルを処理しました。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="音声ファイルを処理して文字起こしを生成します。")
    parser.add_argument('--input_dir', type=str, default="assets/audios", help="音声ファイルの入力ディレクトリ。")

    args = parser.parse_args()

    process_audio_files(
        input_dir=args.input_dir,
        output_dir=OUTPUT_DIRECTORY,
    )

```

結果。簡潔にするために一部の値を削除したJSON出力のサンプルを示します。完全なJSONにはより詳細な情報が含まれます。

```json
{
    "results": [
        {
            "alternatives": [
                {
                    "transcript": "Here's To The Crazy Ones The Misfits the Rebels the troublemakers the round pegs in the square holes the ones who see things differently they're not fond of rules and they have no respect for the status quo",
                    "confidence": 0.95684826,
                    "words": [
                        {
                            "startOffset": "1s",
                            "endOffset": "4.200s",
                            "word": "Here's",
                            "confidence": 0.8265989
                        },
                        {
                            "startOffset": "4.200s",
                            "endOffset": "4.400s",
                            "word": "To",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.400s",
                            "word": "The",
                            "confidence": 0.9994259
                        },
                        {
                            "startOffset": "4.400s",
                            "endOffset": "4.900s",
                            "word": "Crazy",
                            "confidence": 0.9975712
                        },
                        {
                            "startOffset": "4.900s",
                            "endOffset": "5.100s",
                            "word": "Ones",
                            "confidence": 0.9904002
                        },
                        {
                            "startOffset": "5.100s",
                            "endOffset": "6.700s",
                            "word": "The",
                            "confidence": 0.9994307
                        },
                        {
                            "startOffset": "6.700s",
                            "endOffset": "7.200s",
                            "word": "Misfits",
                            "confidence": 0.9352707
                        },
                        {
                            "startOffset": "7.200s",
                            "endOffset": "8.400s",
                            "word": "the",
                            "confidence": 0.99881697
                        },
                        {
                            "startOffset": "8.400s",
                            "endOffset": "8.800s",
                            "word": "Rebels",
                            "confidence": 0.9900544
                        },
                        {
                            "startOffset": "8.800s",
                            "endOffset": "10.300s",
                            "word": "the",
                            "confidence": 0.99904335
                        }                        
                    ]
                }
            ],
            "resultEndOffset": "23.780s",
            "languageCode": "en-us"
        }
    ]
}
```