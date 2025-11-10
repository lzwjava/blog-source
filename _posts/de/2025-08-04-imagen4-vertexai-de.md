---
audio: false
generated: true
image: false
lang: de
layout: post
title: Vertex AIs Imagen 4 Modelle
translated: true
type: note
---

Basierend auf dem von Ihnen bereitgestellten Code-Snippet verwenden Sie `genai.Client`, um mit einem Modell für die Bildgenerierung auf Vertex AI zu interagieren. Das von Ihnen angegebene Modell ist `"imagen-4.0-generate-preview-06-06"`.

Hier ist eine Aufschlüsselung dessen, was neu ist und was dieses Modell darstellt:

### Die neuesten Bildgenerierungsmodelle auf Vertex AI

Das von Ihnen verwendete Modell, `imagen-4.0-generate-preview-06-06`, ist Teil der neuesten **Imagen 4** Modellfamilie auf Vertex AI. Zu dieser Modellfamilie gehören auch:

*   **`imagen-4.0-generate-preview-06-06`**: Dies ist das Standard-Imagen-4-Modell, das ein Gleichgewicht zwischen Geschwindigkeit und Qualität bietet.
*   **`imagen-4.0-ultra-generate-preview-06-06`**: Diese "Ultra"-Version ist für höhere Qualität konzipiert, ist jedoch langsamer und teurer.
*   **`imagen-4.0-fast-generate-preview-06-06`**: Diese "Fast"-Variante priorisiert Geschwindigkeit und geringere Latenz gegenüber der bestmöglichen Qualität.

Diese Imagen-4-Modelle sind ein bedeutendes Update, das auf früheren Versionen wie Imagen 3 und Imagen 2 aufbaut. Die wichtigsten Funktionen und Updates von Imagen 4 umfassen:

*   **Verbesserte Bildqualität**: Die neuen Modelle sind darauf ausgelegt, Bilder mit höherer Qualität zu generieren als ihre Vorgänger.
*   **Unterstützung für mehr Seitenverhältnisse**: Imagen 4 unterstützt mehrere Seitenverhältnisse, darunter `1:1`, `3:4`, `4:3`, `9:16` und `16:9`, was Ihnen mehr Kontrolle über das Ergebnis gibt.
*   **Mehrsprachige Prompts**: Während Englisch die Hauptsprache ist, unterstützen diese Modelle auch Textprompts in mehreren anderen Sprachen, darunter Chinesisch (vereinfacht und traditionell), Hindi, Japanisch, Koreanisch, Portugiesisch und Spanisch (in der Vorschau).
*   **Sicherheitsfunktionen**: Die Modelle enthalten benutzerkonfigurierbare Sicherheitseinstellungen und integrieren digitale Wasserzeichen (SynthID), um KI-generierte Inhalte zu kennzeichnen.

Die Parameter `person_generation` und `safety_filter_level` in Ihrem Code-Snippet sind weiterhin relevant und ermöglichen es Ihnen, das Verhalten des Modells für Responsible AI zu konfigurieren, wie Sie es mit `person_generation="ALLOW_ADULT"` und `safety_filter_level="BLOCK_LOW_AND_ABOVE"` getan haben.

### Über die Bildgenerierung hinaus

Zusätzlich zu den aktualisierten Imagen-Modellen hat Google Cloud kürzlich auch andere neue generative KI-Modelle auf Vertex AI eingeführt, darunter:

*   **Veo 3 und Veo 3 Fast**: Dies sind die neuesten Videogenerierungsmodelle, mit denen Sie hochwertige Videos aus Text- oder Bildprompts erstellen können. Veo 3 ist für hochwertige, professionelle Videos mit Funktionen wie nativer Audioausgabe und Lippen-Sync konzipiert, während Veo 3 Fast für Geschwindigkeit optimiert ist.
*   **Gemini 2.5 Modelle**: Dies sind die neuesten Versionen der Gemini-Modellfamilie, darunter Gemini 2.5 Pro, Gemini 2.5 Flash und Gemini 2.5 Flash-Lite, die fortschrittliches Reasoning, Multi-Modalität und verbesserte Leistung für verschiedene Aufgaben bieten.