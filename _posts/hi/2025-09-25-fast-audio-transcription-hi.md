---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: लंबे ऑडियो ट्रांसक्रिप्शन प्रसंस्करण में तेजी
translated: true
type: note
---

### 30 मिनट या 1 घंटे की ऑडियो के लिए प्रोसेसिंग इतनी लंबी क्यों होती है?

Google Cloud Speech-to-Text Batch API (v2) को एसिंक्रोनस, लंबे समय तक चलने वाले ऑपरेशन्स के लिए डिज़ाइन किया गया है, खासकर `"long"` मॉडल के साथ, जो एक्सटेंडेड ऑडियो फ़ाइलों (प्रति फ़ाइल ~1 घंटे तक) को हैंडल करता है। यहाँ बताया गया है कि यह "बहुत लंबा" क्यों लग सकता है:

- **प्रोसेसिंग समय ऑडियो की लंबाई के साथ स्केल करता है**: ट्रांसक्रिप्शन तत्काल नहीं है। 30 मिनट की ऑडियो फ़ाइल के लिए, इसमें 5-20 मिनट लग सकते हैं; 1 घंटे के लिए, 10-40 मिनट या अधिक। इसमें शामिल है:
  - कतारबद्ध होने का समय (यदि आपका प्रोजेक्ट/रिजन व्यस्त है)।
  - वास्तविक ट्रांसक्रिप्शन (AI मॉडल इनफेरेंस, जो लंबी ऑडियो के लिए कंप्यूट-इंटेंसिव है)।
  - पोस्ट-प्रोसेसिंग (जैसे, वर्ड टाइमिंग, कॉन्फिडेंस स्कोर)।
- **बैच प्रकृति**: रियल-टाइम स्ट्रीमिंग के विपरीत, बैच जॉब बैकग्राउंड में Google के सर्वर पर चलती हैं। आपकी स्क्रिप्ट `operation.result()` को कॉल करती है, जो ब्लॉक करती है और इंतजार करती है, लेकिन असली काम एसिंक्रोनस तरीके से होता है।
- **अन्य कारक**:
  - ऑडियो फॉर्मेट/गुणवत्ता: OGG/Opus या M4A/AAC को डिकोडिंग की आवश्यकता होती है, जो ओवरहेड जोड़ती है यदि सैंपल रेट/चैनल मिसमैच होते हैं।
  - मॉडल चुनाव: `"long"` मीटिंग्स/पॉडकास्ट के लिए ऑप्टिमाइज़्ड है लेकिन `"default"` या `"short"` जैसे छोटे मॉडल की तुलना में धीमा है।
  - नेटवर्क/कोटा: GCS पर अपलोड करना, API कॉल, और रिजल्ट डाउनलोड करना लेटेंसी जोड़ते हैं। फ्री टियर कोटा या उच्च मांग जॉब्स को विलंबित कर सकती है।
  - कोई बिल्ट-इन पैरेललिज़्म नहीं: स्क्रिप्ट एक समय में एक फ़ाइल को क्रमिक रूप से प्रोसेस करती है।

यदि आपकी ऑडियो लगातार 30+ मिनट की है, तो वर्तमान सेटअप त्वरित टर्नअराउंड के लिए आदर्श नहीं है—यह ऑफलाइन/बल्क प्रोसेसिंग के लिए बेहतर है।

### इसे कैसे ठीक करें: प्रोसेसिंग समय कम करें

लंबी ऑडियो को तेजी से हैंडल करने के लिए, मुख्य बिंदु है **फ़ाइल को छोटे-छोटे हिस्सों (chunks) में विभाजित करना** (जैसे, प्रत्येक 5-15 मिनट)। यह अनुमति देता है:
- समानांतर प्रोसेसिंग (एक साथ कई बैच जॉब चलाना)।
- तेज मॉडल का उपयोग (जैसे, प्रति चंक `"short"` या `"default"`)।
- प्रति जॉब कम इंतजार का समय (जैसे, पूरी फ़ाइल के लिए 30+ मिनट के बजाय प्रति चंक 1-5 मिनट)।

#### चरण 1: ऑडियो फ़ाइल को विभाजित करें
फ़ाइलों को बिना री-एन्कोडिंग के (तेज और लॉसलेस) विभाजित करने के लिए **FFmpeg** (मुफ्त, कमांड-लाइन टूल) का उपयोग करें। यदि आवश्यक हो तो FFmpeg इंस्टॉल करें (जैसे, macOS पर `brew install ffmpeg`, Linux पर `apt install ffmpeg`)।

अपनी स्क्रिप्ट में इनपुट फ़ाइल को विभाजित करने के लिए एक फ़ंक्शन जोड़ें। यहाँ विभाजन को एकीकृत करके आपकी स्क्रिप्ट का एक अद्यतन संस्करण दिया गया है:

```python
import os
import argparse
import subprocess
import tempfile
from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import sys
import time  # पोलिंग के लिए

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api  # noqa: F401

MAX_AUDIO_LENGTH_SECS = 20 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"
CHUNK_DURATION_SECS = 600  # प्रति चंक 10 मिनट; आवश्यकतानुसार समायोजित करें (जैसे, 15 मिनट के लिए 900)


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    FFmpeg का उपयोग करके ऑडियो फ़ाइल को छोटे हिस्सों (chunks) में विभाजित करें।
    
    Args:
        input_file: इनपुट ऑडियो का पथ।
        chunk_duration_secs: प्रत्येक चंक की अवधि सेकंड में।
    
    Returns:
        चंक फ़ाइल पथों की सूची।
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # चंक्स के लिए अस्थायी डायरेक्टरी बनाएँ
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # FFmpeg कमांड (गति के लिए कोई री-एन्कोडिंग नहीं)
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # आउटपुट फॉर्मेट
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # बिना री-एन्कोडिंग के स्ट्रीम्स को कॉपी करें
        "-map", "0",  # सभी स्ट्रीम्स को मैप करें
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # आउटपुट पैटर्न
        "-y"  # ओवरराइट करें
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # जेनरेट किए गए चंक्स ढूंढें
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # नाम के आधार पर क्रमबद्ध करें (जैसे, chunk_001, chunk_002)
        print(f"{filename} को {len(chunk_files)} चंक्स में विभाजित किया।")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"{filename} को विभाजित करने में FFmpeg त्रुटि: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Google Cloud Speech-to-Text Batch API का उपयोग करके एक ऑडियो फ़ाइल का ट्रांसक्रिप्शन करता है।
    यदि ऑडियो संभावित रूप से छोटी है (जैसे, विभाजन के बाद) तो छोटे मॉडल का उपयोग करने के लिए अद्यतन किया गया।
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # चंक्स के लिए, गति के लिए "short" या "default" मॉडल का उपयोग करें (यदि <15 मिनट)
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # चंक आकार के आधार पर समायोजित करें

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

    print(f"{filename} के लिए बैच रिकग्नाइज़ शुरू कर रहा हूँ...")
    operation = client.batch_recognize(request=request)
    
    # प्रगति के लिए पोल करें (विवरण के लिए नीचे देखें)
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # प्रति चंक कम टाइमआउट
    print(f"{filename} के लिए ट्रांसक्रिप्शन पूरा हुआ। प्रतिक्रिया: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    लंबे समय तक चलने वाले ऑपरेशन को पोल करें और प्रगति दिखाएं।
    """
    while not operation.done():
        # ऑपरेशन मेटाडेटा प्राप्त करें (यदि उपलब्ध हो; Speech API बेसिक स्टेटस प्रदान करती है)
        try:
            metadata = operation.metadata
            print(f"{filename} के लिए प्रगति: State={getattr(metadata, 'state', 'Unknown')}, "
                  f"Processed={getattr(metadata, 'progress_bytes', 'N/A')} bytes")
        except Exception:
            print(f"{filename} का इंतज़ार कर रहा हूँ... (हर 30s में जाँच)")
        
        time.sleep(30)  # हर 30 सेकंड में पोल करें
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"त्रुटि: {filename} एक समर्थित ऑडियो फ़ाइल (.m4a या .ogg) नहीं है।")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"{filename} को छोड़ रहा हूँ: {output_filename} पहले से मौजूद है।")
        return

    print(f"प्रोसेसिंग: {filename}")

    # भाषा निर्धारित करें
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # यदि फ़ाइल लंबी है तो उसे चंक्स में विभाजित करें (अनुमान: >15 मिनट, लेकिन आप ffprobe से अवधि जांच सकते हैं)
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # मोटा अनुमान: >100MB संभवतः लंबी
        print(f"फ़ाइल बड़ी है; इसे {CHUNK_DURATION_SECS//60}-मिनट के चंक्स में विभाजित कर रहा हूँ।")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("विभाजन विफल; सिंगल फ़ाइल के रूप में प्रोसेस कर रहा हूँ।")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # बाद में संयोजित करने के लिए

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # GCS पथ बनाएँ
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # यदि आवश्यक हो तो चंक अपलोड करें
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"चंक {chunk_filename} को GCS पर अपलोड किया।")
        else:
            print(f"चंक {chunk_filename} पहले से ही GCS में मौजूद है।")

        # ट्रांसक्राइब करें
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # ट्रांसक्रिप्ट डाउनलोड करें और एकत्र करें
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # JSON को पार्स करके टेक्स्ट निकालें (सरलीकृत; पूर्ण पार्सिंग के लिए json मॉड्यूल का उपयोग करें)
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"{b.name} डाउनलोड और पार्स किया गया")

            all_transcripts.append(chunk_transcript)

            # यदि विभाजन हुआ है तो अस्थायी चंक साफ़ करें
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"चंक {chunk_filename} को प्रोसेस करने में विफल: {e}")

    # सभी ट्रांसक्रिप्ट्स को एक फ़ाइल में संयोजित करें
    combined_text = "\n\n--- Chunk Boundary ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"संयोजित ट्रांसक्रिप्ट {output_filename} में सहेजी गई।")

    # यदि विभाजन हुआ है तो अस्थायी डायरेक्टरी साफ़ करें
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"{filename} के लिए प्रोसेसिंग पूर्ण।")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ट्रांसक्रिप्शन जनरेट करने के लिए एक सिंगल वॉइस मेमो (.m4a/.ogg) फ़ाइल प्रोसेस करें।"
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="वॉइस मेमो फ़ाइल के लिए इनपुट पथ।",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="ट्रांसक्रिप्शन के लिए आउटपुट डायरेक्टरी।",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="सेकंड में चंक अवधि (लंबी फ़ाइलों को विभाजित करने के लिए)।",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # ओवरराइड की अनुमति दें
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### मुख्य परिवर्तन और लाभ:
- **विभाजन**: गैर-ओवरलैपिंग चंक्स (जैसे, प्रत्येक 10-मिनट) बनाने के लिए FFmpeg का उपयोग करता है। 1 घंटे की फ़ाइल के लिए, यह ~6 जॉब्स हैं, जिन्हें यदि आप थ्रेडिंग/मल्टीप्रोसेसिंग (जैसे, `concurrent.futures` के माध्यम से) का उपयोग करने के लिए संशोधित करते हैं तो समानांतर रूप से चलाया जा सकता है।
- **तेज मॉडल**: चंक्स <15 मिनट के लिए `"short"` पर स्विच करता है—2-3x तेजी से प्रोसेस करता है।
- **ट्रांसक्रिप्ट्स को संयोजित करना**: JSON आउटपुट को पार्स करता है और उन्हें आसान पठन के लिए सीमाओं के साथ एक सिंगल `.txt` फ़ाइल में मर्ज करता है।
- **सफाई**: यदि आवश्यक हो तो अस्थायी चंक्स और पुराने GCS ब्लॉब्स को हटाता है (लूप में `blob.delete()` जोड़ें)।
- **उपयोग**: पहले की तरह चलाएं, जैसे, `python script.py --input_file long_audio.m4a --chunk_secs 600`। बिना विभाजन के, एक बड़ा `--chunk_secs` (जैसे, 3600) का उपयोग करें।

#### अन्य ऑप्टिमाइज़ेशन:
- **समानांतर प्रोसेसिंग**: यदि आपके पास कई चंक्स/फ़ाइलें हैं, तो `run_batch_recognize` जॉब्स को समवर्ती रूप से सबमिट करने के लिए Python के `ThreadPoolExecutor` का उपयोग करें (कोटा हिट से बचने के लिए 5-10 तक सीमित करें)।
- **ऑडियो अवधि जांचें**: यह गतिशील रूप से तय करने के लिए कि क्या विभाजन आवश्यक है, `ffprobe` (FFmpeg) का उपयोग करें: `ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`।
- **स्ट्रीमिंग API पर स्विच करें**: इंटरैक्टिव उपयोग के लिए, सिंक्रोनस `recognize` (सीमा ~1 मिनट/फ़ाइल) या लाइव के लिए स्ट्रीमिंग का उपयोग करें, लेकिन यह बैच लंबी फ़ाइलों के लिए आदर्श नहीं है।
- **लागत/कोटा**: अपना Google Cloud कोटा जांचें (Speech-to-Text ~1000 अनुरोध/मिनट की अनुमति देता है)। लंबी जॉब्स अधिक क्रेडिट (~$0.036/मिनट स्टैंडर्ड मॉडल के लिए) खपत करती हैं।
- **पहले छोटे के साथ परीक्षण करें**: स्पीडअप देखने के लिए `--chunk_secs 300` (5 मिनट) से शुरू करें।

### प्रगति दिखाना: ऑपरेशन को पोल करना

अद्यतन किया गया `poll_operation_with_progress()` फ़ंक्शन ब्लॉकिंग `operation.result()` को प्रतिस्थापित करता है। यह:
- हर 30 सेकंड में जाँच करता है।
- `operation.metadata` से स्टेटस प्रिंट करता है (जैसे, "RUNNING" या "DONE" जैसी स्टेट, और बाइट्स प्रोसेस्ड यदि उपलब्ध हो—Speech API मेटाडेटा बेसिक है, लेकिन यह कुछ नहीं से बेहतर है)।
- यदि यह विफल होता है तो एक एरर उठाता है।

अधिक विस्तृत प्रगति (जैसे, % पूर्ण) के लिए, Speech API विस्तृत मेट्रिक्स प्रदान नहीं करती है, लेकिन आप यह कर सकते हैं:
- Google Cloud कंसोल के माध्यम से मॉनिटर करें (आपके प्रोजेक्ट के लिए ऑपरेशन्स पेज)।
- `gcloud` CLI का उपयोग करें: `gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`।
- पूर्ण होने के बाद, JSON रिजल्ट्स अप्रत्यक्ष रूप से टाइमस्टैम्प्स के माध्यम से प्रति-उच्चारण प्रगति शामिल करते हैं।

यदि विभाजन हो रहा है, तो आप कई चंक्स से इंटरलीव्ड प्रगति देखेंगे, जिससे यह कम "अटका हुआ" महसूस होगा।

यदि यह आपकी समस्या का समाधान नहीं करता है (जैसे, विशिष्ट त्रुटियाँ), तो अधिक ट्वीक्स के लिए लॉग/आउटपुट साझा करें