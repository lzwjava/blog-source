---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger Facilement les Erreurs de Décodage OGG Opus
translated: true
type: note
---

Réponse courte : ne définissez pas `audio_channel_count` (ni `sample_rate_hertz`) dans `ExplicitDecodingConfig` pour votre OGG/Opus. C'est ce qui fait échouer v2 avec :

```
explicit_decoding_config.audio_channel_count: audio_channel_count is out of range
```

## Ce qu'il faut changer (code)

Dans votre branche `.ogg`, construisez la configuration **sans** les canaux/le taux d'échantillonnage pour que le service les déduise :

```python
if file_extension == "ogg":
    # Conservez uniquement l'encodage ; laissez STT déduire le taux d'échantillonnage/les canaux.
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

> Si vous **savez avec certitude** que le fichier est de l'Opus stéréo/48 kHz, vous pouvez définir `sample_rate_hertz=48000` et `audio_channel_count=2`. Sinon, omettez les deux — ne devinez pas.

---

## Devriez-vous prétraiter avec ffmpeg ?

Vous n'êtes pas obligé si le changement ci-dessus fonctionne. Mais si vous voyez toujours des erreurs de décodage (flux mixés, conteneur étrange, canaux variables), le transcodage vers un format "simple" rend l'API Batch très heureuse. L'une ou l'autre de ces options est sûre :

### Option A : FLAC (sans perte, préféré)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a flac haifeng_and_zhiwei.flac
```

### Option B : WAV Linear16 (sans perte)

```bash
ffmpeg -y -i haifeng_and_zhiwei.ogg -ac 1 -ar 16000 -c:a pcm_s16le haifeng_and_zhiwei.wav
```

Ensuite, téléchargez ce fichier vers le même bucket GCS et exécutez avec **`auto_decoding_config`** (aucun décodage explicite nécessaire pour FLAC/WAV) :

```python
# pour .flac ou .wav
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

## Vérifications rapides

* Assurez-vous que votre étiquette de langue est un BCP-47 valide. Pour le mandarin, vous pouvez utiliser `"cmn-CN"` ou `"cmn-Hans-CN"`.
* Gardez les noms de fichiers simples (ASCII) pour éviter des métadonnées de conteneur étranges.
* Si vous voulez confirmer les canaux/le taux d'échantillonnage avant de décider, vous pouvez inspecter avec :

  ```bash
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 haifeng_and_zhiwei.ogg
  ```

**Conclusion :** Essayez d'abord de supprimer `audio_channel_count` (et `sample_rate_hertz`). Si cela échoue toujours, transcodez en FLAC/WAV et passez à `auto_decoding_config`.