---
audio: false
generated: true
image: false
lang: de
layout: post
title: Blockieren von Niedrigem und Höherem
translated: true
type: note
---

Sie sehen diesen Fehler:

```
Only block_low_and_above is supported for safetySetting.
```

Dies passiert, wenn Sie `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"` (oder einen anderen Wert) in `GenerateImagesConfig` für die **Imagen-4**-Modelle setzen – aber zum Zeitpunkt Ihrer Anfrage (August 2025) **erlaubt die API nur `"BLOCK_LOW_AND_ABOVE"`** für die Bildsicherheitsfilterung bei diesen Modellen ([Google Cloud][1]).

---

### ✅ So beheben Sie den Fehler im Code

Aktualisieren Sie einfach den `safety_filter_level` auf den unterstützten Wert:

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`: Nur dieser Wert wird für **Imagen 4** unterstützt. Andere Schwellenwerte wie `"BLOCK_MEDIUM_AND_ABOVE"` verursachen den 400 INVALID\_ARGUMENT Fehler ([Medium][2], [Google AI for Developers][3]).
* `number_of_images=1` ist explizit gesetzt, damit klar ist, dass Sie ein Bild pro Aufruf anfordern.

---

### 🧾 Andere optionale Parameter:

* `person_generation="ALLOW_ADULT"` ist die Standardeinstellung, aber es ist in Ordnung, explizit zu sein (blockiert Kinder; erlaubt Bilder mit Erwachsenen) ([Google Cloud][1]).
* `image_size="2K"` ist laut Ihrem Code gültig – stellen Sie nur sicher, dass Ihre SDK-Version dies unterstützt.

---

### TL;DR — Kurzanleitung

| Schritt | Was zu tun ist                                               |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | Ändern Sie safety\_filter\_level zu `"BLOCK_LOW_AND_ABOVE"`  |
| 🧾 2  | Behalten Sie `person_generation="ALLOW_ADULT"` (oder weglassen für Standard) |
| 🚫 3  | Verwenden Sie nicht `"BLOCK_MEDIUM_AND_ABOVE"` oder `"BLOCK_ONLY_HIGH"` |
| ⏱ 4   | Ändern Sie die Sicherheitseinstellung nicht erneut, bis Google weitere Stufen hinzufügt |

Lassen Sie mich wissen, wenn Sie einen anderen Fehler erhalten – ich helfe gerne!

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"