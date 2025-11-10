---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leichte lokale LLM-Webclient-Optionen
translated: true
type: note
---

Wenn Sie nach leichtgewichtigen, Open-Source-Webclients suchen, um LLMs lokal auszuführen – mit weniger Abhängigkeiten als Open WebUI – hier sind einige gute Alternativen:

**1. Lobe Chat**
- Leichtgewichtig und erweiterbar, unterstützt Lobe Chat sowohl lokale als auch remote LLMs. Es bietet ein Plugin-System und eine saubere Benutzeroberfläche und kann über Docker oder direkt auf Ihrem Rechner ausgeführt werden. Es ist bekannt für seine einfache Einrichtung und gute Performance mit Ollama und anderen Backends.

**2. LM Studio**
- LM Studio ist eine Desktop-App, die GGUF-Modelle (wie Mistral, Phi 3 und Gemma) unterstützt und eine einfache, benutzerfreundliche Oberfläche bietet. Es ist ideal für schnelle lokale Inferenz und erfordert keine komplexe Einrichtung oder viele Abhängigkeiten.

**3. text-generation-webui (Oobabooga)**
- Eine funktionsreiche, auf Gradio basierende Web-Oberfläche, die mehrere Backends unterstützt (transformers, GPTQ, AWQ, EXL2, llama.cpp). Es ist hochgradig anpassbar und weit verbreitet, allerdings etwas aufwändiger einzurichten als LM Studio.

**4. AnythingLLM**
- Ein vielseitiger, selbst gehosteter Chat-Client, der gut für sowohl lokale als auch cloud-basierte Modelle funktioniert. Es ist für den allgemeinen Gebrauch konzipiert und als Desktop-App verfügbar, was es flexibel und relativ leichtgewichtig macht.

**5. Jan**
- Jan ist eine plattformübergreifende, offline-fähige Chat-Oberfläche mit Drag-and-Drop-Anpassung und vorgefertigten Vorlagen. Es ist für Performance optimiert und unterstützt mehrere LLM-APIs, was es zu einer guten Wahl für datenschutzbewusste Nutzer macht.

**6. Ollama UI**
- Speziell für Ollama entwickelt, ist diese Oberfläche minimal und einfach zu deployen, was sie zu einer guten Wahl macht, wenn Sie Ollama bereits für das Modell-Serving verwenden.

**7. Open-LLM-WebUI**
- Eine einfache, open-source Web-Oberfläche zum lokalen Ausführen von kompakten LLMs. Sie ist auf Benutzerfreundlichkeit und minimalen Einrichtungsaufwand ausgelegt, was sie zu einer guten Alternative für diejenigen macht, die etwas Unkompliziertes suchen.

**Zusammenfassungstabelle:**

| Client                | Hauptmerkmale                         | Einrichtungsaufwand | Am besten geeignet für      |
|-----------------------|---------------------------------------|---------------------|-----------------------------|
| Lobe Chat             | Plugins, Docker-Unterstützung, saubere Oberfläche | Niedrig       | Allgemeine Nutzung, Ollama  |
| LM Studio             | Desktop-App, GGUF-Unterstützung, einfache Oberfläche | Sehr Niedrig  | Schnelle lokale Inferenz    |
| text-generation-webui | Multi-Backend, hochgradig anpassbar   | Mittel              | Fortgeschrittene Nutzer     |
| AnythingLLM           | Desktop-App, flexibel, allgemeine Nutzung | Niedrig        | Lokal/Cloud-Hybrid          |
| Jan                   | Offline, Drag-and-Drop, Vorlagen      | Niedrig             | Datenschutz, Anpassung      |
| Ollama UI             | Minimal, auf Ollama fokussiert        | Sehr Niedrig        | Ollama-Nutzer               |
| Open-LLM-WebUI        | Einfach, leichtgewichtig              | Niedrig             | Kompakte LLMs               |

Wenn Sie die absolut leichtgewichtigste Option wollen, sind **LM Studio** oder **Ollama UI** ein guter Ausgangspunkt. Für mehr Funktionen und Flexibilität sind **Lobe Chat** oder **text-generation-webui** gute Wahlmöglichkeiten.

Möchten Sie weitere Details zur Einrichtung oder zu spezifischen Anwendungsfällen für einen dieser Clients?