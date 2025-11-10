---
audio: false
generated: true
image: false
lang: de
layout: post
title: Google Gen AI Bildkonfiguration
translated: true
type: note
---

Hier ist eine kurze Übersicht: Der `image_size`-Parameter wird im Google Gen AI (Gemini/Imagen) Python SDK nicht unterstützt. Stattdessen wählen Sie zwischen Modellvarianten (die jeweils implizite Standardauflösungen haben), steuern das **Seitenverhältnis** und wenden – wenn Sie höhere Pixelzahlen benötigen – eine **Hochskalierung** an. Sie können auch die **Komprimierung** und das **Ausgabeformat** anpassen, plus die üblichen Einstellungen für "Anzahl der Bilder", "Negativ-Prompt", "Sicherheit" und "Personen".

## Modellvarianten

Sie wählen einen Modellnamen – jede Variante hat ihre eigene Standardauflösung und Leistungscharakteristik:

* **imagen-3.0**-Familie:

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* **imagen-4.0 (Vorschau)**-Familie:

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **Legacy**: `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## Standardauflösung

Standardmäßig ist eine quadratische ("1:1") Ausgabe dieser Modelle **1024 × 1024 Pixel**. Wenn Sie eine kleinere Datei benötigen, können Sie lokal herunterskalieren; wenn Sie eine höhere Auflösung benötigen, siehe **Hochskalierung** unten. ([raymondcamden.com][2])

## Seitenverhältnisse

Anstatt absolute Abmessungen anzugeben, verwenden Sie das Feld `aspect_ratio` in Ihrer `GenerateImagesConfig`. Unterstützte Werte:

* `1:1` (Quadrat)
* `3:4` (höher, Social-Media-Hochformat)
* `4:3` (klassische Fotografie/Fernsehen)
* `16:9` (Breitbild-Landschaften)
* `9:16` (hoch/Hochformat, z.B. für Handy-Hintergründe) ([Google Cloud][1], [Google AI for Developers][3])

Dieselbe Liste finden Sie in Community-Tutorials dokumentiert:

* DataCamp weist genau auf diese fünf Verhältnisse für Imagen 3 hin ([DataCamp][4])
* CodeSignals Guide zählt sie ebenfalls für Gemini/Imagen auf ([CodeSignal][5])

## Hochskalierung

Wenn Sie echte "2K"- oder "4K"-Ausgaben benötigen, rufen Sie den **Hochskalierungs**-Modus auf:

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` verdoppelt jede Dimension (z.B. 1024 → 2048, grob 2K)
* `"x4"` vervierfacht (z.B. 1024 → 4096, grob 4K) ([Google Cloud][1])

## Komprimierung & Formate

* **JPEG-Qualität**: Verwenden Sie `compression_quality` (0–100, Standard 75), um Dateigröße gegen Detailreichtum abzuwägen ([Google Cloud][1])
* **MIME-Typen**: Über `output_options.mime_type` können Sie wählen zwischen
  `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/bmp`, `image/tiff` oder `image/vnd.microsoft.icon` ([Google Cloud][6])

## Zusätzliche Konfigurationsoptionen

Alles andere befindet sich in `GenerateImagesConfig`:

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # Wie viele Bilder generiert werden sollen
    seed=1234,                    # Für deterministische Ausgaben
    enhance_prompt=True,          # LLM-basierte Prompt-Umformulierung
    negative_prompt="exclude dogs",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

Diese erlauben es Ihnen, Zufälligkeit, Prompt-Verbesserung, Sicherheitsschwellen und ob das Model Personen darstellen darf, zu steuern. ([Google Cloud][1])

## Empfehlung

Entfernen Sie Ihre Zeile `image_size="2K"` – es gibt kein solches Flag. Gehen Sie stattdessen so vor:

1.  **Wählen Sie das richtige Modell** für Geschwindigkeit vs. Qualität.
2.  Verwenden Sie **`aspect_ratio`** für die Bildkomposition.
3.  Wenn Sie wirklich höhere Pixelzahlen benötigen, generieren Sie mit der Basisauflösung und wenden Sie dann die eingebaute **Hochskalierung** ("x2" oder "x4") an.
4.  Passen Sie **compression\_quality** an oder skalieren Sie lokal herunter für kleinere Dateien.

Mit diesen Stellschrauben können Sie quadratische oder cinematische Formate, kleine oder hochauflösende Ausgaben erreichen, ohne einen nicht unterstützten `image_size`-Parameter.

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"