---
audio: false
generated: true
image: false
lang: de
layout: post
title: Entfernen von `width` und `height`
translated: true
type: note
---

Der Fehler, den Sie sehen:

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

wird verursacht, indem `width` und `height` an `GenerateImagesConfig` übergeben werden, welche diese Felder **nicht unterstützt**. Laut Fehlermeldung und dem API-Design von Gemini muss `image_size` einer der **vordefinierten Enums-Werte** sein, und `CUSTOM` wird für die öffentliche Gemini-API (derzeit) **nicht unterstützt**.

---

### ✅ Lösung

Sie sollten `width` und `height` **entfernen** und einen gültigen `image_size` Enum wie `"1024x1024"` oder `"512x512"` verwenden.

Hier ist die korrigierte Version:

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# Vertex AI Client einrichten
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # Erlaubten Wert verwenden, nicht CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 Um ein **benutzerdefiniertes Bild** wie `1200x630` zu generieren:

Die aktuellen öffentlichen Gemini/Imagen APIs **unterstützen keine** beliebigen Bildgrößen. Wenn Sie 1200×630 benötigen (z.B. für OG-Bilder), sind Ihre Optionen:

1. **Das Bild nach der Generierung nachbearbeiten**, um es auf die gewünschten Abmessungen zu skalieren/zuzuschneiden.
2. **Ein anderes Modell/eine andere API** verwenden, die benutzerdefinierte Abmessungen unterstützt (z.B. Stability AI's SDXL, Midjourney oder private Endpoints).
3. Wenn Sie internen Zugriff haben (z.B. innerhalb von Google), bestätigen Sie dies mit der internen Dokumentation oder Ihrem Vertex AI Account Manager.

Lassen Sie mich wissen, wenn Sie Hilfe beim Skalieren des Bildes nach der Generierung benötigen.