---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح أخطاء فك ترميز OGG Opus بسهولة
translated: true
type: note
---

إجابة مختصرة: لا تضبط `audio_channel_count` (أو `sample_rate_hertz`) في `ExplicitDecodingConfig` لملف OGG/Opus الخاص بك. هذا هو ما يتسبب في مشكلة v2 مع:

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## ما الذي يجب تغييره (الكود)

في فرع `.ogg` الخاص بك، أنشئ التكوين **بدون** قنوات/معدل حتى تستنتجها الخدمة:

```python
if file_extension == "ogg":
    # احتفظ فقط بالتشفير؛ دع STT تستنتج المعدل/القنوات.
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

> إذا كنت **تعتقد يقينًا** أن الملف بصيغة ستيريو/48 كيلوهرتز Opus، يمكنك ضبط `sample_rate_hertz=48000` و `audio_channel_count=2`. وإلا، احذف كليهما—لا تخمن.

---

## هل يجب عليك المعالجة المسبقة باستخدام ffmpeg؟

ليس عليك ذلك إذا نجح التغيير أعلاه. ولكن إذا ما زلت ترى شكاوى في فك التشفير (تيارات مختلطة، حاوية غريبة، قنوات متغيرة)، فإن إعادة التشفير إلى تنسيق "عادي" يجعل واجهة برمجة تطبيقات الدُفعات سعيدة جدًا. أي من الخيارين التاليين آمن:

### الخيار أ: FLAC (بدون فقدان، مُفضّل)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### الخيار ب: WAV بصيغة Linear16 (بدون فقدان)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

ثم حمّل ذلك الملف إلى دلو GCS نفسه وشغّله باستخدام **`auto_decoding_config`** (لا حاجة لفك التشفير الصريح لملفات FLAC/WAV):

```python
# لملفات .flac أو .wav
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

## فحوصات سريعة للتأكد من السلامة

* تأكد من أن وسم اللغة صالح وفقًا لـ BCP-47. للماندرين، يمكنك استخدام `"cmn-CN"` أو `"cmn-Hans-CN"`.
* حافظ على أسماء الملفات بسيطة (باستخدام أحرف ASCII) لتجنب بيانات وصفية غريبة للحاوية.
* إذا أردت التأكد من عدد القنوات/المعدل قبل اتخاذ القرار، يمكنك فحص الملف باستخدام:

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**خلاصة القول:** جرب أولاً إزالة `audio_channel_count` (و `sample_rate_hertz`). إذا استمر الفشل، فقم بإعادة تشفير الملف إلى FLAC/WAV وانتقل إلى استخدام `auto_decoding_config`.