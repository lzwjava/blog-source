---
audio: false
generated: true
image: false
lang: hi
layout: post
title: गूगल स्पीच एपीआई के लिए एएसी एम4ए ठीक करें
translated: true
type: note
---

हाँ—आपकी फ़ाइल **एम4ए कंटेनर में एएसी** (iPhone Voice Memos) है। Google Speech-to-Text v2 बैच अक्सर एएसी/एम4ए को ऑटो-डिकोड करने में विफल हो जाता है और यही त्रुटि देता है। पहले एक समर्थित कोडेक/कंटेनर में कनवर्ट करें—फिर या तो `AutoDetectDecodingConfig()` रखें या (बेहतर) डिकोडिंग को स्पष्ट रूप से निर्दिष्ट करें।

यहाँ सबसे तेज़ रास्ता है।

## विकल्प A — `ffmpeg` के साथ वन-लाइनर फिक्स (सुझाया गया: Ogg/Opus)

छोटी फाइलें, बेहतरीन सटीकता, आधिकारिक तौर पर समर्थित।

```bash
# 48 kHz, मोनो, OGG में Opus
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -c:a libopus -b:a 48k ~/Downloads/haifeng_and_zhiwei.ogg
```

फिर नई फ़ाइल पर अपनी स्क्रिप्ट चलाएँ:

```bash
python scripts/agent/speech_to_text_agent.py --input_file ~/Downloads/haifeng_and_zhiwei.ogg
```

## विकल्प B — लॉसलेस FLAC (भी समर्थित)

WAV से छोटा; लॉसलेस।

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 48000 -sample_fmt s16 -c:a flac ~/Downloads/haifeng_and_zhiwei.flac
```

## विकल्प C — Linear16 WAV (सबसे बड़ी फ़ाइल)

```bash
ffmpeg -i ~/Downloads/haifeng_and_zhiwei.m4a -vn -ac 1 -ar 16000 -sample_fmt s16 -c:a pcm_s16le ~/Downloads/haifeng_and_zhiwei.wav
```

---

## कोड ट्वीक्स (ताकि आपको यह समस्या दोबारा न हो)

1.  **अधिक एक्सटेंशन की अनुमति दें** और उसी तरह सफ़िक्स से भाषा चुनें।
2.  **स्वचालित रूप से ट्रांसकोड करें** एक समर्थित फॉर्मेट में (मैं Ogg/Opus का उपयोग करता हूँ)।
3.  **API को स्पष्ट रूप से बताएँ कि आप क्या भेज रहे हैं** (स्पष्ट डिकोडिंग)।

इसे अपनी स्क्रिप्ट में डालें (न्यूनतम, केंद्रित परिवर्तन):

```python
import subprocess
import tempfile
from pathlib import Path
from google.cloud.speech_v2.types import cloud_speech

SUPPORTED_EXTS = {".ogg", ".flac", ".wav", ".mp3"}  # mp3 भी समर्थित है

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

    # स्पष्ट डिकोडिंग को प्राथमिकता दें — "असमर्थित एन्कोडिंग" के आश्चर्य से बचाता है
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
        decoding_cfg = cloud_speech.AutoDetectDecodingConfig()  # फॉलबैक

    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding_cfg,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
        # वैकल्पिक: वक्ता पहचान, विराम चिह्न, आदि।
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

    # सफ़िक्स द्वारा भाषा तय करें
    language_code = "cmn-CN" if src.name.endswith("-zh" + src.suffix) else "en-US"

    # समर्थित एन्कोडिंग/कंटेनर सुनिश्चित करें
    if src.suffix.lower() not in SUPPORTED_EXTS:
        print(f"Transcoding {src.name} to Ogg/Opus...")
        input_file = _transcode_to_ogg_opus(str(src))
        src = Path(input_file)

    # आपके लोकल .txt के लिए आउटपुट गेटिंग (आप इसे यथावत रख सकते हैं या स्टेम से जोड़ सकते हैं)
    output_filename = os.path.join(output_dir, f"{src.stem}.txt")
    if os.path.exists(output_filename):
        print(f"Skipping {src.name}: {output_filename} already exists.")
        return

    print(f"Processing: {src.name}")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("test2x")
        # फोल्डर "audio-files/" रखें, नए एक्सटेंशन के साथ रियल फाइलनेम रखें
        blob = bucket.blob(f"audio-files/{src.name}")
        if not blob.exists():
            blob.upload_from_filename(str(src))
            print(f"Uploaded {src.name} to GCS.")
        else:
            print(f"{src.name} already exists in GCS.")

        gcs_audio_uri = f"gs://test2x/audio-files/{src.name}"
        gcs_output_uri = f"gs://test2x/transcripts/{src.stem}"

        # एक्सटेंशन के आधार पर डिकोडिंग चुनें
        ext = src.suffix.lower()
        if ext == ".ogg":
            decoding = "ogg_opus"
        elif ext == ".flac":
            decoding = "flac"
        elif ext == ".wav":
            decoding = "linear16"
        else:
            decoding = None  # ऑटोडिटेक्ट पर फॉल बैक करें

        run_batch_recognize(
            audio_gcs_uri=gcs_audio_uri,
            output_gcs_folder=gcs_output_uri,
            language_code=language_code,
            decoding=decoding,
        )

        print(f"File {src.name} processed.\n")

        # ट्रांसक्रिप्शन JSONs डाउनलोड करें
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

### यह क्यों काम करता है

* iOS Voice Memos → **AAC/M4A**. Batch STT v2 इसे विश्वसनीय रूप से ऑटोडिटेक्ट/डिकोड नहीं करता है।
* **OGG/Opus** (या **FLAC/WAV**) में ट्रांसकोड करके और **API को कोडेक बताकर**, आप "असमर्थित एन्कोडिंग" त्रुटि से पूरी तरह बच जाते हैं।

### व्यावहारिक सुझाव

* आपके **1h21m मोनो वॉइस मेमो** जैसी लंबी रिकॉर्डिंग के लिए, **OGG/Opus 48k** गुणवत्ता बनाए रखते हुए आकार और GCS इग्रेस को कम करता है।
* मोनो (`-ac 1`) रखें। स्टीरियो केवल पहचान में मदद किए बिना लागत दोगुनी कर देता है।
* अगर बातचीत मैंडरिन है, तो आपका `"cmn-CN"` कोड ठीक है; जैसा आप पहले से करते हैं, `"-zh.m4a"` नेमिंग कन्वेंशन का उपयोग करें।
* अगर आपको वक्ता परिवर्तन चाहिए, बाद में वक्ता पहचान सक्षम करें; पहले डिकोड पाथ ठीक करें।

अगर आप चाहें, तो मैं वैकल्पिक **स्वचालित लोकल → GCS अपलोड + पुनः नामकरण** भी जोड़ सकता हूँ ताकि आपका `m4a` इनपुट स्वीकार किया जाए लेकिन हमेशा आंतरिक रूप से `.ogg` के रूप में प्रोसेस हो।