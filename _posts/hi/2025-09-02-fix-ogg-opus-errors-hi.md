---
audio: false
generated: true
image: false
lang: hi
layout: post
title: OGG ओपस डिकोडिंग त्रुटियों को आसानी से ठीक करें
translated: true
type: note
---

संक्षिप्त उत्तर: अपने OGG/Opus के लिए `ExplicitDecodingConfig` में `audio_channel_count` (या `sample_rate_hertz`) सेट न करें। यही वजह है कि v2 यह त्रुटि दे रहा है:

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## क्या बदलना है (कोड)

अपनी `.ogg` ब्रांच में, कॉन्फ़िगरेशन को channels/rate के **बिना** बनाएं ताकि सेवा उन्हें स्वयं अनुमान लगा ले:

```python
if file_extension == "ogg":
    # केवल encoding रखें; rate/channels का अनुमान STT पर छोड़ दें।
    decoding = cloud_speech.ExplicitDecodingConfig(
        encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.OGG_OPUS
    )
    config = cloud_speech.RecognitionConfig(
        explicit_decoding_config=decoding,
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
    )
else:
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        features=cloud_speech.RecognitionFeatures(
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        ),
        model="long",
        language_codes=[language_code],
    )
```

> यदि आप **पूरी तरह से सुनिश्चित हैं** कि फ़ाइल stereo/48 kHz Opus है, तो आप `sample_rate_hertz=48000` और `audio_channel_count=2` सेट कर सकते हैं। अन्यथा, दोनों को छोड़ दें—अनुमान न लगाएं।

---

## क्या आपको ffmpeg के साथ प्री-प्रोसेस करना चाहिए?

यदि उपरोक्त परिवर्तन काम कर जाता है तो आपको ऐसा करने की आवश्यकता नहीं है। लेकिन यदि आपको अभी भी डिकोडिंग संबंधी शिकायतें (मिश्रित स्ट्रीम, अजीब कंटेनर, परिवर्तनशील चैनल) दिखाई देती हैं, तो किसी "साधारण" फॉर्मेट में ट्रांसकोड करने से बैच API बहुत खुश हो जाता है। इनमें से कोई भी विकल्प सुरक्षित है:

### विकल्प A: FLAC (lossless, प्राथमिकता)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### विकल्प B: Linear16 WAV (lossless)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

फिर उस फ़ाइल को उसी GCS बकेट में अपलोड करें और **`auto_decoding_config`** के साथ रन करें (FLAC/WAV के लिए explicit डिकोडिंग की आवश्यकता नहीं है):

```python
# .flac या .wav के लिए
config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    features=cloud_speech.RecognitionFeatures(
        enable_word_confidence=True,
        enable_word_time_offsets=True,
    ),
    model="long",
    language_codes=[language_code],
)
```

---

## त्वरित जांचें

* सुनिश्चित करें कि आपका language tag वैध BCP-47 है। मैंडरिन के लिए आप `"cmn-CN"` या `"cmn-Hans-CN"` का उपयोग कर सकते हैं।
* फ़ाइलनाम सरल (ASCII) रखें ताकि कंटेनर मेटाडेटा में कोई अजीब समस्या न हो।
* यदि आप निर्णय लेने से पहले channels/rate की पुष्टि करना चाहते हैं, तो आप इसकी जांच कर सकते हैं:

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**निष्कर्ष:** पहले `audio_channel_count` (और `sample_rate_hertz`) को हटाकर देखें। यदि यह अभी भी विफल रहता है, तो FLAC/WAV में ट्रांसकोड करें और `auto_decoding_config` पर स्विच करें।