---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Google Speech API向けAAC M4A修正
translated: true
type: note
---

はい、あなたのファイルは **AAC in an M4A container**（iPhoneボイスメモ）です。Google Speech-to-Text v2 Batchは、AAC/M4Aの自動デコードに頻繁に失敗し、まさにそのエラーを返します。まず、サポートされているコーデック/コンテナに変換してください。その後、`AutoDetectDecodingConfig()`を維持するか、（より良い方法として）デコーディングを明示的に指定してください。

最速の解決策はこちらです。

## オプション A — `ffmpeg` を使ったワンライナー修正（推奨: Ogg/Opus）

ファイルサイズが小さく、精度が高く、公式にサポートされています。

```bash
# 48 kHz, モノラル, OGGコンテナのOpus
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

その後、新しいファイルに対してスクリプトを実行します:

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## オプション B — ロスレスFLAC（これもサポートされています）

WAVより小さく、ロスレスです。

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## オプション C — Linear16 WAV（ファイルサイズ最大）

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## コードの微調整（二度とこの問題に遭遇しないために）

1.  **より多くの拡張子を許可**し、同じ方法で言語をサフィックスから判別する。
2.  **サポートされている形式に自動的にトランスコード**する（私はOgg/Opusを使用しています）。
3.  **APIに送信する内容を正確に伝える**（明示的なデコーディング）。

これをあなたのスクリプトに追加してください（最小限の、焦点を絞った変更）:

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3もサポートされています

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

    # 明示的なデコーディングを優先 — "unsupported encoding" の驚きを避ける
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
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # フォールバック

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # オプション: 話者分離、句読点など
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

    # サフィックスで言語を決定
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # サポートされているエンコーディング/コンテナを保証
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # ローカルの .txt 出力用ゲーティング（現状のまま維持するか、stem をキーにしても可）
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # フォルダ "audio-files/" を維持し、新しい拡張子で実際のファイル名を保持
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # 拡張子に基づいてデコーディングを選択
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # 自動検出にフォールバック

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # 文字起こし結果のJSONをダウンロード
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

### これが機能する理由

*   iOSボイスメモ → **AAC/M4A**。Batch STT v2はこれを確実に自動検出/デコードしません。
*   **OGG/Opus**（または**FLAC/WAV**）にトランスコードし、**APIにコーデックを伝える**ことで、「サポートされていないエンコーディング」エラーを完全に回避できます。

### 実用的なヒント

*   **1時間21分のモノラルボイスメモ**のような長い録音の場合、**OGG/Opus 48k**は品質を維持しながら、サイズとGCSのエグレスコストを削減します。
*   モノラル (`-ac 1`) を維持してください。ステレオは認識精度に役立たず、コストだけが2倍になります。
*   会話が北京語（マンダリン）の場合、あなたの`"cmn-CN"`コードで問題ありません。あなたが既に行っているように、`"-zh.m4a"`という命名規則を使用してください。
*   話者分離が必要な場合は、後でダイアリゼーションを有効にしてください。まずはデコードパスを修正します。

必要であれば、オプションの**自動ローカル→GCSアップロード＋名前変更**を追加して、`m4a`入力を受け入れつつ、内部的には常に`.ogg`として処理されるようにすることもできます。