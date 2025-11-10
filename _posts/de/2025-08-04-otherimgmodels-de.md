---
audio: false
generated: true
image: false
lang: de
layout: post
title: Andere Bildmodelle auf Vertex AI
translated: true
type: note
---

Während Imagen die Flaggschiff-Familie von Bildgenerierungsmodellen von Google auf Vertex AI ist, stehen andere Optionen zur Verfügung, insbesondere wenn Sie nach unterschiedlichen Fähigkeiten oder Open-Source-Alternativen suchen.

Hier ist eine Übersicht über andere bildbezogene Modelle, die Sie auf Vertex AI verwenden können:

### Gemini-Modelle (für multimodale Anwendungsfälle)
Die Gemini-Modellfamilie ist multimodal, was bedeutet, dass sie verschiedene Datentypen verarbeiten und verstehen kann, einschließlich Text, Bilder, Video und Audio. Während sie primär für ihre textbasierten Ausgaben bekannt sind, verfügen einige Gemini-Modelle über spezifische Funktionen für bildbezogene Aufgaben. Zum Beispiel können einige Gemini-Modelle:
* **Bilder aus einer Textaufforderung generieren**.
* **Bilder mittels Konversationsanweisungen bearbeiten**.
* **Visuelles Frage-Antworten (VQA)** durchführen, bei dem Sie eine Frage zu einem Bild stellen und eine textbasierte Antwort erhalten.
* **Beschreibungen für ein gegebenes Bild generieren** (Bildbeschriftung).

Dies ist eine gute Option, wenn Sie eine Anwendung entwickeln, die sowohl Text als auch Bilder auf konversationelle oder integrierte Weise verarbeiten muss, anstatt nur ein Bild aus einer einfachen Aufforderung zu generieren.

### Open-Source-Modelle aus dem Model Garden
Der **Model Garden** von Vertex AI ist ein zentraler Hub, in dem Sie eine Vielzahl von Modellen entdecken, testen, anpassen und bereitstellen können, einschließlich sowohl proprietärer Modelle von Google als auch einer kuratierten Auswahl von Open-Source-Modellen. Hier finden Sie Alternativen zu Imagen, wie zum Beispiel:

* **Llama 3-Vision**: Eine Familie multimodaler Modelle, die für visuelle Erkennung, Bildschlussfolgerung und Bildbeschriftung optimiert sind.
* **Flux**: Ein Rectified Flow Transformer-Modell, das hochwertige Bilder aus Textbeschreibungen generiert.
* **Instant ID**: Ein identitätserhaltendes Text-zu-Bild-Generierungsmodell. Dies ist nützlich, um neue Bilder einer bestimmten Person oder eines Subjekts zu generieren, während deren wesentliche Identitätsmerkmale erhalten bleiben.

Diese Open-Source-Modelle bieten oft unterschiedliche Lizenzbedingungen, Leistungsmerkmale und Anpassungsmöglichkeiten, was Ihnen mehr Flexibilität für spezifische Anwendungsfälle gibt.

### Andere vision-bezogene Modelle
Neben der Bildgenerierung bietet Vertex AI vortrainierte Modelle für eine Vielzahl von Vision-Aufgaben, die nützlich sein könnten:

* **Multimodale Embeddings**: Erzeugt Vektordarstellungen von Bildern, die Sie für Aufgaben wie Bildersuche (ähnliche Bilder finden), Klassifizierung oder Clustering verwenden können.
* **Vertex AI AutoML Image**: Ermöglicht es Ihnen, Ihre eigenen benutzerdefinierten Machine-Learning-Modelle für Bildklassifizierung, Objekterkennung und Bildsegmentierung zu trainieren, ohne Code schreiben zu müssen.
* **Video-Modelle (Veo)**: Obwohl kein Bildmodell, ermöglicht Veo die Generierung hochwertiger Videos aus Text- oder Bildaufforderungen. Es ist ein leistungsstarkes Werkzeug für die Medienerstellung, das über Standbilder hinausgeht.