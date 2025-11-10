---
audio: false
generated: true
image: false
lang: de
layout: post
title: Bild mit KI-Prompt transformieren
translated: true
type: note
---

Stand August 2025 haben sich OpenAIs DALL-E-Modelle, insbesondere die neueren "GPT Image"-Modelle (wie `gpt-image-1`), weiterentwickelt und unterstützen nun anspruchsvollere Bildmanipulation, einschließlich "Image-to-Image"-Transformationen. Während DALL-E 2 einen spezifischen "Variations"-Endpunkt dafür hatte, integrieren die neueren Modelle diese Funktionalität durch eine Kombination aus Bildeingaben und detaillierten Textprompts.

So würden Sie eine "Image-to-Image"-Aufgabe wie das Anwenden eines Ghibli-Stils über die OpenAI API angehen:

### Das Grundprinzip: Bildbearbeitung mit einem Text-Prompt

Im Gegensatz zu einem einfachen Text-zu-Bild-Prompt beinhaltet Image-to-Image mit der OpenAI API die Bereitstellung sowohl eines Bildes als auch eines Text-Prompts, der die gewünschten Änderungen beschreibt. Der Schlüssel liegt darin, dem Modell Anweisungen zu geben, wie es das Bild in einem neuen Stil "neu interpretieren" soll.

### Schritt-für-Schritt-Anwendung der API

Der Prozess umfasst typischerweise einige wichtige Schritte:

1.  **Bereiten Sie Ihr Bild vor:** Das Bild, das Sie transformieren möchten, muss in einem unterstützten Format (z.B. PNG, JPEG) vorliegen und die Größenanforderungen erfüllen (oft ist ein quadratisches Seitenverhältnis am besten). Sie müssen dieses Bild für den API-Aufruf bereitstellen.

2.  **Formulieren Sie einen aussagekräftigen Prompt:** Dies ist der wichtigste Teil. Sie sagen nicht einfach "mach das im Ghibli-Stil". Sie müssen die *Elemente* des Ghibli-Stils beschreiben, die das Modell anwenden soll. Ein guter Prompt dient als Leitfaden für die KI und weist sie an, wie das Bild neu gerendert werden soll.

      * **Schlechter Prompt:** "Ghibli-Stil"
      * **Besserer Prompt:** "Eine magische Waldszene im Stil von Studio Ghibli. Verwende weiche Aquarelltexturen, eine lebendige aber sanfte Farbpalette mit Golden-Hour-Beleuchtung und verleihe ihr eine verspielte, traumhafte Atmosphäre."
      * **Noch besserer Prompt:** "Verwandele dieses Porträt in eine Studio-Ghibli-Figur, behalte ihre wesentlichen Merkmale bei, aber gestalte sie mit der unverwechselbaren Ghibli-Ästhetik: leicht vereinfachte Gesichtszüge, ausdrucksstarke Augen und eine weiche Farbpalette. Verwende handgemalte Texturen und ein nostalgisches Gefühl."

3.  **Führen Sie den API-Aufruf durch:** Sie verwenden die OpenAI API für Bildbearbeitung. Der Endpunkt dafür ist typischerweise Teil der Bildgenerierungs-API, aber mit spezifischen Parametern für die Bildeingabe. Sie übergeben Ihr Bild (oft als Base64-kodierter String oder eine Datei-ID, wenn Sie es auf den OpenAI-Server hochgeladen haben) und Ihren detaillierten Prompt.

      * **Endpunkt:** Der spezifische Endpunkt könnte `/v1/images/edits` für DALL-E 2 sein, aber für neuere Modelle wie GPT Image könnte er in einen einzigen, leistungsstärkeren `/v1/chat/completions`-Endpunkt integriert sein, der multimodale Eingaben (sowohl Text als auch Bilder) verarbeitet. Die Dokumentation wird den korrekten Endpunkt und die Struktur Ihrer Anfrage vorgeben.

      * **Parameter:**

          * `model`: Gibt das zu verwendende Modell an, z.B. `dall-e-2` oder ein neueres Modell wie `gpt-image-1`.
          * `image`: Die vorbereiteten Bilddaten.
          * `prompt`: Die Textbeschreibung des anzuwendenden Ghibli-Stils.
          * `n`: Die Anzahl der zu generierenden Bilder (oft auf 1 für neuere Modelle begrenzt).
          * `size`: Die gewünschte Ausgabegröße (z.B. "1024x1024").

4.  **Verarbeiten Sie die Antwort:** Die API gibt ein JSON-Objekt zurück, das eine URL zum neu generierten Bild enthält. Sie können dieses Bild dann herunterladen und speichern.

### Beispielcode (Konzeptionell Python)

Auch wenn der genaue Code sich mit API-Updates ändern kann, hier ein konzeptionelles Beispiel unter Verwendung der `openai` Python-Bibliothek:

```python
import openai
import base64
from io import BytesIO
from PIL import Image

# Richten Sie Ihren OpenAI API-Schlüssel ein
# Sie sollten dies aus Ihren Umgebungsvariablen beziehen, nicht hartkodieren
openai.api_key = os.getenv("OPENAI_API_KEY")

# Funktion zum Kodieren des Bildes in base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Pfad zu dem Bild, das Sie transformieren möchten
image_path = "your_photo.png"
base64_image = encode_image(image_path)

# Ihr detaillierter Ghibli-Stil-Prompt
prompt_text = "Transformiere dieses Bild in einen Studio-Ghibli-Animationsstil. Wende weiche Aquarelltexturen, eine lebendige aber sanfte Farbpalette mit Golden-Hour-Beleuchtung und eine verspielte, traumhafte Atmosphäre an. Behalte die ursprüngliche Komposition des Bildes bei."

try:
    response = openai.images.generate(
        model="gpt-image-1", # oder "dall-e-2" für den Variations-Endpunkt
        prompt=prompt_text,
        image_base64=base64_image, # Dieser Parameter kann je nach API-Version variieren
        size="1024x1024",
        n=1,
    )

    image_url = response.data[0].url
    print(f"Generiertes Ghibli-Stil-Bild: {image_url}")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

```

**Wichtige Hinweise:**

  * **API-Updates:** Die OpenAI API entwickelt sich ständig weiter. Konsultieren Sie immer die offizielle OpenAI API-Dokumentation für die aktuellsten Endpunkte, Parameter und Codebeispiele.
  * **Modellauswahl:** Das neuere `gpt-image-1`-Modell ist im Allgemeinen überlegen, wenn es darum geht, komplexe, nuancenreiche Anweisungen zu befolgen, und kann sowohl für Bildanalyse als auch -generierung verwendet werden, was ein mächtiges Werkzeug für Image-to-Image-Aufgaben ist.
  * **Prompt-Engineering:** Die Qualität Ihrer Ausgabe hängt stark von Ihrem Prompt ab. Experimentieren Sie mit verschiedenen beschreibenden Begriffen und stilistischen Elementen, um genau den gewünschten Ghibli-artigen Look zu erreichen.