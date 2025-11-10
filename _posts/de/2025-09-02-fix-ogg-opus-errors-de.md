---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von OGG-Opus-Decodierungsfehlern
translated: true
type: note
---

Kurze Antwort: Setze `audio_channel_count` (oder `sample_rate_hertz`) in `ExplicitDecodingConfig` für deine OGG/Opus-Dateien nicht. Das ist der Auslöser für den Fehler in v2:

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## Was zu ändern ist (Code)

In deinem `.ogg`-Branch, baue die Konfiguration **ohne** Kanäle/Rate, damit der Service sie ableitet:

```python
if file_extension == "ogg":
    # Nur die Kodierung beibehalten; Rate/Kanäle von STT ableiten lassen.
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

> Wenn du **sicher weißt**, dass die Datei Stereo/48 kHz Opus ist, kannst du `sample_rate_hertz=48000` und `audio_channel_count=2` setzen. Ansonsten, lasse beide weg – rate nicht.

---

## Solltest du mit ffmpeg vorverarbeiten?

Das ist nicht nötig, wenn die obige Änderung funktioniert. Aber wenn du weiterhin Dekodierfehler siehst (gemischte Streams, seltsamer Container, variable Kanäle), dann macht das Transkodieren in ein "einfaches" Format die Batch-API sehr glücklich. Eine der folgenden Optionen ist sicher:

### Option A: FLAC (verlustfrei, bevorzugt)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### Option B: Linear16 WAV (verlustfrei)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

Lade dann diese Datei in den gleichen GCS-Bucket hoch und verwende **`auto_decoding_config`** (für FLAC/WAV ist keine explizite Dekodierung nötig):

```python
# für .flac oder .wav
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

## Schnelle Plausibilitätsprüfungen

* Stelle sicher, dass dein Sprach-Tag ein gültiger BCP-47-Code ist. Für Mandarin kannst du `"cmn-CN"` oder `"cmn-Hans-CN"` verwenden.
* Halte Dateinamen einfach (ASCII), um seltsame Container-Metadaten zu vermeiden.
* Wenn du Kanäle/Rate vor der Entscheidung bestätigen möchtest, kannst du sie inspizieren mit:

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**Fazit:** Versuche zuerst, `audio_channel_count` (und `sample_rate_hertz`) zu entfernen. Wenn es weiterhin fehlschlägt, transkodiere nach FLAC/WAV und wechsle zu `auto_decoding_config`.