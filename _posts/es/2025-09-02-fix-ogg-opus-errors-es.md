---
audio: false
generated: true
image: false
lang: es
layout: post
title: Cómo solucionar fácilmente errores de decodificación de OGG Opus
translated: true
type: note
---

Respuesta corta: no establezcas `audio_channel_count` (ni `sample_rate_hertz`) en `ExplicitDecodingConfig` para tu archivo OGG/Opus. Eso es lo que está causando el error en v2 con:

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## Qué cambiar (código)

En tu rama `.ogg`, construye la configuración **sin** los canales/tasa de muestreo para que el servicio los infiera:

```python
if file_extension == "ogg":
    # Mantén solo el encoding; deja que STT infiera la tasa de muestreo/canales.
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

> Si **sabes con seguridad** que el archivo es Opus estéreo/48 kHz, puedes establecer `sample_rate_hertz=48000` y `audio_channel_count=2`. De lo contrario, omite ambos—no adivines.

---

## ¿Deberías preprocesar con ffmpeg?

No es necesario si el cambio anterior funciona. Pero si aún ves quejas de decodificación (streams mezclados, contenedor extraño, canales variables), transcodificar a un formato "simple" hace que la API por lotes sea muy feliz. Cualquiera de estas opciones es segura:

### Opción A: FLAC (sin pérdida, preferido)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### Opción B: WAV Linear16 (sin pérdida)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

Luego sube ese archivo al mismo bucket de GCS y ejecuta con **`auto_decoding_config`** (no se necesita decodificación explícita para FLAC/WAV):

```python
# para .flac o .wav
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

## Comprobaciones rápidas de sentido común

* Asegúrate de que tu etiqueta de idioma sea un BCP-47 válido. Para Mandarín puedes usar `"cmn-CN"` o `"cmn-Hans-CN"`.
* Mantén los nombres de archivo simples (ASCII) para evitar metadatos extraños en el contenedor.
* Si quieres confirmar los canales/tasa de muestreo antes de decidir, puedes inspeccionar con:

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**Conclusión:** Primero intenta eliminar `audio_channel_count` (y `sample_rate_hertz`). Si aún falla, transcodifica a FLAC/WAV y cambia a `auto_decoding_config`.