---
audio: false
generated: true
image: false
lang: de
layout: post
title: Fixes offizielles Imagen Python-Snippet
translated: true
type: note
---

Du hast im Grunde die korrekte Logik implementiert, aber die **get‑unstuck**-Anweisungen sind leicht daneben. Hier ist eine bereinigte Version, die vom offiziellen Beispiel in der Dokumentation adaptiert wurde:

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← Setze deinen API-Schlüssel oder verwende die Umgebungsvariable GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # optional für 2K-Auflösung; erfordert neueres fast-preview library
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # Konvertiere rohe Bytes in ein PIL-Bild
    pil.save(f"output-image-{i+1}.png")
    print(f"Saved image {i+1}, {len(raw):,} bytes")
```

Während Google's Python-Ausschnitt auch `image_size="2K"` für sein 4‑Preview-Modell verwendete, sei dir bewusst, dass:

* Du `google-genai` v1.28 oder neuer ausführen musst, um `image_size` für Imagen 4-Modelle zu unterstützen;
* Andernfalls lasse dieses Feld weg (der Standard ist 1.024×1.024 bei einer festen quadratischen Pixelauflösung) ([GitHub][1]).

---

### 🚩 Häufige Fallstricke & Lösungen

1. **Fehlende PIL-Installation**
   Wenn du `google-genai` installiert, aber `Pillow` nicht hinzugefügt hast, können `.image.save()`-Aufrufe stillschweigend fehlschlagen (oder einen `AttributeError` verursachen). Stelle sicher:

   ```bash
   pip install pillow
   ```

2. **Kein API-Schlüssel oder falscher Dienst ausgewählt**
   Wenn du `genai.Client()` ohne API-Schlüssel und ohne Cloud-Berechtigungen aufrufst, schlägt der Client zur Laufzeit mit einem Authentifizierungsfehler fehl (z.B. `"401 UNAUTHENTICATED"`). Übergib entweder `api_key="…"` oder setze `GOOGLE_API_KEY` in deiner Shell, für die Gemini Developer API ([GitHub][1]).

3. **Bibliotheksversions-Konflikt**
   Ältere Versionen der Bibliothek oder das veraltete `google.generativeai`-Modul exportieren `generate_images()` nicht und verwenden möglicherweise immer noch die *veraltete* Generative-AI-Schnittstelle. Stelle immer sicher:

   ```bash
   pip install --upgrade google-genai
   ```

   Das Problem "kann die Ausgabebilder nicht öffnen" in älteren Repositories (`deprecated-generative-ai-python`) resultierte aus diesem Konflikt und warf normalerweise `UnidentifiedImageError` oder `FileNotFoundError` nach dem Schreiben von beschädigten Bytes ([GitHub][1]).

4. **UnidentifiedImageError beim Öffnen mit PIL**
   Wenn du siehst:

   ```
   PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
   ```

   bedeutet das normalerweise, dass der Antwort-Puffer beschädigt oder unvollständig ist. Überprüfe doppelt, ob:

   * Dein Prompt nicht gefiltert wurde (z.B. durch RAI-Blocking);
   * Du die Bytes nicht base64-decodierst (das SDK liefert bereits rohe PNG/JPEG-Daten zurück);
   * Dein Datei-Download nicht vorzeitig abgebrochen wurde.

---

### ✅ Warum dieser Fix funktioniert

* Das offizielle Snippet in Google's Dokumentation vom 2025‑08‑01 verwendet genau:

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  bevor es über `result.image.save(...)` gespeichert wird ([Google Cloud][2]).

* Aber andere Anleitungen, die Imagen 3-Modelle verwenden, geben nur `number_of_images`, `aspect_ratio` und Sicherheitseinstellungen an – ohne `image_size` – weil Imagen 3 es nicht unterstützt ([GitHub][1]).

Wenn du dem obigen Ablauf folgst, solltest du weitermachen können. Wenn du auf eine spezifische Fehlermeldung stößt (wie HTTP 403, fehlender JSON-Schlüssel in der Antwort, etc.), kannst du diese gerne hier einfügen, und ich helfe dir, den nächsten Schritt zur Fehlerbehebung zu gehen.

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"