---
audio: false
generated: true
lang: de
layout: post
title: 'Metas Smart Glasses: Funktionen und APIs'
translated: true
type: note
---

Lassen Sie uns die Smart-Glasses-Angebote von Meta aufschlüsseln, einschließlich Ray-Ban und Oakley, ihre Nutzerbasis und was ihre APIs Entwicklern bieten.

**Was sind Meta VR Glass, Ray-Ban und Oakley Smart Glasses?**

Es ist wichtig, die Terminologie hier zu klären. „Meta VR Glass“ ist kein spezifischer Produktname, den Meta allgemein verwendet. Stattdessen ist das primäre VR/MR-Angebot von Meta die **Meta Quest**-Reihe von Headsets (z. B. Meta Quest 3).

Wenn Leute allgemein von „Meta-Brillen“ in einer brilleähnlichen Formfaktor sprechen, meinen sie typischerweise:

*   **Ray-Ban Meta Smart Glasses:** Dies sind verbraucherorientierte Smart Glasses, die in Partnerschaft mit EssilorLuxottica (dem Unternehmen hinter Ray-Ban) entwickelt wurden. Sie sind so gestaltet, dass sie wie konventionelle Ray-Ban-Sonnenbrillen aussehen, und konzentrieren sich auf Funktionen wie:
    *   Freihand-Foto- und Videoaufnahme (mit einer sichtbaren LED-Anzeige für den Datenschutz).
    *   Open-Ear-Lautsprecher für Audio (Musik, Podcasts, Anrufe).
    *   Integrierte Mikrofone für Anrufe und Sprachbefehle (einschließlich „Hey Meta“ für Meta AI).
    *   Livestreaming-Fähigkeiten zu Facebook und Instagram.
    *   Integration mit Meta AI für verschiedene Aufgaben (z. B. Informationen erhalten, Nachrichten senden, Umgebung für Barrierefreiheit beschreiben).
    *   Kein integriertes Display oder AR-Head-Mounted-Display (es handelt sich um „Smart Glasses“, nicht im typischen Sinne um AR-Brillen).

*   **Oakley Meta Glasses (z. B. Oakley Meta HSTN):** Dies ist eine neuere Reihe von „Performance AI Glasses“, die in Zusammenarbeit mit Oakley, ebenfalls Teil von EssilorLuxottica, entwickelt wurden. Sie teilen viele der Funktionen der Ray-Ban Meta Brillen, sind aber speziell für Sportler und Leistung konzipiert. Wichtige Aspekte sind:
    *   Auffälliges, sportliches Design, typisch für Oakley.
    *   Verbesserte Haltbarkeit und Wasserdichtheit (IPX4).
    *   Längere Akkulaufzeit.
    *   Höhere Auflösung der Kamera (3K-Video).
    *   Integration mit Meta AI, mit Funktionen, die auf Sportler zugeschnitten sind (z. B. Fragen zu Windbedingungen für Golf).

**Wie viele Nutzer gibt es?**

Stand Februar 2025 haben die **Ray-Ban Meta Smart Glasses** seit ihrem Launch im September 2023 über **2 Millionen Einheiten** verkauft. EssilorLuxottica plant, die jährliche Produktionskapazität bis Ende 2026 auf 10 Millionen Einheiten zu erhöhen, was auf eine starke Nachfrage und Metas Zuversicht in die Zukunft des Produkts hindeutet.

Die **Oakley Meta Glasses** sind eine neuere Produktlinie, deren Vorbestellungen im Juli 2025 starten. Daher sind spezifische Nutzerzahlen für die Oakley Meta Brillen noch nicht verfügbar, aber sie streben eine bedeutende Marktpräsenz an.

**Was bietet ihre API für Entwickler?**

Es ist wichtig, zwischen APIs für VR/MR-Headsets (wie Meta Quest) und Smart Glasses (wie Ray-Ban Meta und Oakley Meta) zu unterscheiden.

**Für Meta Quest (VR/MR-Headsets):**

Meta bietet eine robuste Entwicklerplattform für sein Meta Horizon OS (ehemals Quest OS) und stellt verschiedene APIs und SDKs zur Erstellung immersiver VR- und Mixed-Reality-Erlebnisse bereit. Wichtige Bereiche für Entwickler sind:

*   **OpenXR:** Ein Standard zur Erstellung hochperformanter XR-Erlebnisse, der es Entwicklern ermöglicht, plattformübergreifende VR/MR-Apps zu bauen.
*   **Meta Horizon Worlds:** Tools zum Erstellen und Gestalten von Erlebnissen innerhalb von Metas sozialer VR-Plattform.
*   **Android Apps:** Entwickler können bestehende Android-Apps mit Meta Horizon OS kompatibel machen und dessen einzigartige räumliche Funktionen nutzen.
*   **Webentwicklung:** 2D-Web-Apps entwerfen und bereitstellen, die die Multitasking-Fähigkeiten von Quest nutzen.
*   **Meta Spatial SDK:** Entwickelt für Mixed Reality, ermöglicht es Entwicklern, 2D-Apps mit innovativen räumlichen Elementen zu transformieren.
*   **Passthrough Camera API:** Ermöglicht Entwicklern, virtuelle und reale Welten nahtlos zu verschmelzen und Mixed-Reality-Anwendungen zu erstellen.
*   **Interaction APIs:** Für Hand-Tracking, Controller-Eingabe, Fortbewegung und mehr.
*   **Voice Command & Text-to-Speech (TTS) APIs:** Zur Integration von Sprachsteuerung und gesprochener Ausgabe in Anwendungen.
*   **Scene Understanding APIs:** Um auf Daten über die physische Umgebung des Nutzers zuzugreifen und diese zu nutzen (z. B. Szenen-Mesh, Anker).
*   **Social Features APIs:** Für Bestenlisten, Herausforderungen, Benutzerbenachrichtigungen usw.

**Für Ray-Ban Meta und Oakley Meta Smart Glasses:**

Derzeit gibt es kein öffentlich veröffentlichtes, umfassendes, offizielles SDK oder eine API speziell für Drittanwendungsentwickler, um benutzerdefinierte Anwendungen zu erstellen, die *direkt auf* den Ray-Ban Meta oder Oakley Meta Smart Glasses laufen.

Allerdings haben Entwickler auf kreative Weise Wege gefunden, mit diesen Geräten zu interagieren:

*   **Meta AI Integration:** Der primäre Weg, auf dem Entwickler mit diesen Brillen interagieren können, ist deren Integration mit **Meta AI**. Das bedeutet, Entwickler können potenziell die Fähigkeiten von Meta AI für verschiedene Aufgaben nutzen, indem sie bestehende APIs für Large Language Models (LLMs) und andere AI-Dienste verwenden. Beispielsweise haben einige community-gesteuerte Projekte „hackige“ Integrationen demonstriert, die Messenger als Brücke nutzen, um Befehle an die Brille zu senden oder Daten von ihr zu empfangen und diese dann mit Diensten wie ChatGPT oder Google Gemini über deren jeweilige APIs zu verarbeiten. Dies stützt sich auf die eingebaute Fähigkeit der Brillen, mit Meta AI zu interagieren und Nachrichten zu senden/zu empfangen.
*   **Content Sharing:** Die Brillen fungieren in erster Linie als Aufnahme- und Sharing-Gerät. Entwickler können mit der **Meta View App** (der Begleit-App für die Brillen) interagieren, indem sie Möglichkeiten bieten, mit der Brille aufgenommenen Content auf ihren Plattformen zu teilen, ähnlich wie Content zu Instagram, Facebook, WhatsApp usw. geteilt wird.
*   **Barrierefreiheits-Funktionen:** Die eingebaute Meta AI bietet Barrierefreiheits-Funktionen wie das Beschreiben der Umgebung oder das Vorlesen von Text. Obwohl es sich nicht um eine direkte API für Entwickler handelt, um neue Apps *auf* den Brillen zu bauen, unterstreicht es das Potenzial für KI-gestützte Assistenz, die letztendlich durch offenere Entwicklungstools zugänglich gemacht werden könnte.

Während Meta seine langfristige Vision für eine offenere Entwicklung an zukünftigen Smart Glasses (potenziell mit Head-up-Displays, wie das gerühmte „Orion“-Projekt) dargelegt hat, ist der Entwicklerzugang für die aktuellen Ray-Ban Meta und Oakley Meta Smart Glasses primär indirekt, indem ihre Integration mit Meta AI und Content-Sharing-Funktionalitäten genutzt wird. Die Community erkundet aktiv Workarounds und inoffizielle Integrationen in Abwesenheit eines dedizierten öffentlichen SDKs für On-Device-App-Entwicklung.