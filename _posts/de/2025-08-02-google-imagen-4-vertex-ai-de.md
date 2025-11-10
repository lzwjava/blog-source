---
audio: false
generated: true
image: false
lang: de
layout: post
title: Google Imagen 4 Vorschau-Leitfaden
translated: true
type: note
---

Um Google Imagen 4 Preview 0606 zu verwenden, müssen Sie es über Googles Vertex AI-Plattform aufrufen, da es sich um ein Generative AI Preview-Angebot für die Text-zu-Bild-Generierung handelt. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung basierend auf verfügbaren Informationen:

### So verwenden Sie Google Imagen 4 Preview 0606

1.  **Auf Vertex AI zugreifen**:
    *   **Plattform**: Imagen 4 Preview 0606 ist auf Google Clouds Vertex AI verfügbar. Sie benötigen einen Google Cloud Account, um zu beginnen.
    *   **Registrierung**: Wenn Sie noch kein Konto haben, registrieren Sie sich unter [cloud.google.com](https://cloud.google.com) und richten Sie ein Projekt ein. Stellen Sie sicher, dass die Abrechnung aktiviert ist, da es sich um ein Preview-Angebot mit potenziellen Kosten handelt (Preisdetails finden Sie im Imagen-Bereich der Vertex AI-Preiseseite).[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)
    *   **Zu Vertex AI navigieren**: Sobald Sie eingeloggt sind, gehen Sie zum Vertex AI-Bereich in der Google Cloud Console und suchen Sie die Generative AI Tools.

2.  **Umgebung einrichten**:
    *   **Authentifizierung**: Authentifizieren Sie Ihr Konto mit Google Cloud-Anmeldedaten. Sie können ein Zugriffstoken mit dem folgenden Befehl generieren:
        ```bash
        gcloud auth print-access-token
        ```
    *   **Projekt und Standort**: Legen Sie Ihre Google Cloud Projekt-ID und den Standort fest (z.B. `us-central1`). Beispiel:
        ```bash
        export GOOGLE_CLOUD_PROJECT=your-project-id
        export GOOGLE_CLOUD_LOCATION=us-central1
        ```

3.  **Das Imagen 4-Modell verwenden**:
    *   **API-Zugriff**: Auf Imagen 4 Preview 0606 kann über die Vertex AI API zugegriffen werden. Verwenden Sie den Model Endpoint `imagen-4.0-generate-preview-06-06`. Sie können programmgesteuert mit Tools wie cURL oder dem Google Gen AI SDK für Python damit interagieren.
    *   **Beispiel cURL-Request**:
        ```bash
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
        -d '{"instances": [{"prompt": "A cat reading a book"}], "parameters": {"sampleCount": 1}}'
        ```
        Dies gibt ein base64-kodiertes Bild zurück.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
    *   **Python SDK-Beispiel**:
        ```python
        from google import genai
        from google.genai.types import GenerateImagesConfig
        client = genai.Client()
        image = client.models.generate_images(
            model="imagen-4.0-generate-preview-06-06",
            prompt="A dog reading a newspaper",
            config=GenerateImagesConfig(image_size="2K")
        )
        image.generated_images[0].image.save("output-image.png")
        print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
        ```
        Dies generiert ein Bild und speichert es als PNG-Datei.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

4.  **Effektive Prompts erstellen**:
    *   **Prompt-Struktur**: Für die besten Ergebnisse verwenden Sie detaillierte und spezifische Prompts. Fügen Sie das Subjekt, die Umgebung, den künstlerischen Stil (z.B. fotorealistisch, abstrakt), die Stimmung und kompositorische Elemente (z.B. Kamerawinkel) hinzu. Beispiel: "Eine lebendige grafische Illustration einer futuristischen Stadt bei Sonnenuntergang, Cyberpunk-Stil, mit Neonlichtern und einer dramatischen Froschperspektive."
    *   **Tipps**:
        *   Seien Sie präzise: Vage Prompts können zu unvorhersehbaren Ergebnissen führen.
        *   Vermeiden Sie unsinnige Eingaben (z.B. zufällige Emojis), da sie inkonsistente Ausgaben erzeugen können.
        *   Geben Sie bei Bedarf Text an, da Imagen 4 ein verbessertes Typografie-Rendering hat.[](https://deepmind.google/models/imagen/)[](https://replicate.com/blog/google-imagen-4)
    *   **Negative Prompts**: Sie können einen negativen Prompt verwenden, um unerwünschte Elemente auszuschließen (z.B. "no text", wenn Sie keinen Text im Bild möchten).[](https://docs.aimlapi.com/api-references/image-models/google/imagen-4-preview)

5.  **Varianten erkunden**:
    *   Imagen 4 Preview 0606 hat Varianten wie **Fast** (bis zu 10x schneller, optimiert für Massengenerierung) und **Ultra** (höhere Übereinstimmung mit Prompts für den professionellen Einsatz). Prüfen Sie, ob diese in Ihrer Vertex AI-Oberfläche verfügbar sind, und wählen Sie basierend auf Ihren Anforderungen (z.B. Fast für schnelles Prototyping, Ultra für hochwertige Ausgaben).[](https://fal.ai/models/fal-ai/imagen4/preview)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

6.  **Ausgabe und Sicherheitsfunktionen überprüfen**:
    *   **Ausgabeformate**: Bilder werden in Standardformaten wie PNG oder JPEG mit einer Auflösung von bis zu 2K generiert.[](https://fal.ai/models/fal-ai/imagen4/preview)
    *   **SynthID-Wasserzeichen**: Alle Bilder enthalten ein unsichtbares digitales Wasserzeichen, um sie als KI-generiert zu identifizieren und so Transparenz zu gewährleisten.[](https://deepmind.google/models/imagen/)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
    *   **Inhaltsbeschränkungen**: Imagen 4 verwendet Filterung, um schädliche Inhalte zu minimieren, aber es könnte bei komplexen Kompositionen, kleinen Gesichtern oder zentrierten Bildern Schwierigkeiten haben. Lesen Sie Googles Nutzungsrichtlinien für Inhaltsbeschränkungen.[](https://deepmind.google/models/imagen/)[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

7.  **Alternative Plattformen**:
    *   Imagen 4 ist auch auf Drittanbieter-Plattformen wie Replicate, fal.ai oder AI/ML API verfügbar, die möglicherweise einfachere Schnittstellen oder Sandbox-Umgebungen zum Testen bieten. Zum Beispiel:
        *   **Replicate**: Führen Sie Imagen 4 mit einem Prompt wie "A serene mountain landscape at sunset, hyperrealistic style." aus. Prüfen Sie die Dokumentation von Replicate für API-Schlüssel und Nutzung.[](https://replicate.com/blog/google-imagen-4)[](https://replicate.com/google/imagen-4-fast)
        *   **fal.ai**: Verwenden Sie deren API mit einem Request wie:
            ```javascript
            const result = await fal.subscribe("fal-ai/imagen4/preview", {
                input: { prompt: "A serene mountain landscape at sunset, hyperrealistic style" }
            });
            console.log(result.images[0].url);
            ```
            Die Preise variieren (z.B. $0,05/Bild für Standard, $0,04 für Fast, $0,06 für Ultra).[](https://fal.ai/models/fal-ai/imagen4/preview)
    *   **Gemini App oder Google Workspace**: Imagen 4 ist in die Gemini App, Google Slides, Docs und Vids integriert, um Bilder direkt in Workflows zu generieren. In Google Docs können Sie beispielsweise Bilder zur Dokumentillustration generieren.[](https://www.stablediffusion.blog/imagen4)

8.  **Testen und Iterieren**:
    *   Experimentieren Sie mit Prompts in einer Sandbox-Umgebung (z.B. Google AI Studio für begrenztes kostenloses Testen), bevor Sie sie in die Produktion integrieren.[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
    *   Überwachen Sie die API-Nutzung und Kosten über das Dashboard der Plattform, da Preview-Angebote möglicherweise eingeschränkten Support oder sich ändernde Funktionen haben.[](https://fal.ai/models/fal-ai/imagen4/preview)

### Zusätzliche Hinweise
*   **Preise**: Prüfen Sie die Vertex AI-Preiseseite für Imagen 4-Kosten (z.B. $0,04/Bild für Standard, $0,06/Bild für Ultra).[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)[](https://fal.ai/models/fal-ai/imagen4/preview)
*   **Einschränkungen**: Imagen 4 könnte bei vagen Prompts, kleinen Gesichtern oder perfekt zentrierten Kompositionen Schwierigkeiten haben. Verwenden Sie klare, strukturierte Prompts für die besten Ergebnisse.[](https://deepmind.google/models/imagen/)
*   **Verfügbarkeit**: Als Preview-Angebot können sich Funktionen und Support ändern. Prüfen Sie die Launch Stage-Beschreibungen von Google Cloud auf Updates.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

Für detaillierte Dokumentation besuchen Sie die [Vertex AI Imagen Seite](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) oder den [Google Developers Blog](https://developers.googleblog.com). Für API-Zugriff siehe [x.ai/api](https://x.ai/api) für allgemeine AI API-Anleitung, obwohl spezifische Imagen 4-Details auf Google Cloud zu finden sind.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)

Wenn Sie Hilfe mit einer bestimmten Plattform oder einem Anwendungsfall benötigen, lassen Sie es mich wissen!