---
audio: false
lang: de
layout: post
title: Llama.cpp ausprobieren
translated: true
---

## llama.cpp

Beim Versuch, `llama.cpp` mit einem Modell auszuführen, könnten Sie auf einen Fehler wie diesen stoßen:

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: loading model from models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: unknown (magic, version) combination: 46554747, 00000003; is this really a GGML file?
llama_load_model_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: unable to load model
```

Dieser Fehler tritt auf, weil Sie das `main`-Programm ausführen. Das Ausführen der Programme `llama-cli` oder `llama-server`, die sich unter `build/bin` befinden, sollte das Problem lösen.

Das `main`-Programm wurde am 8. August 2023 erstellt, was bedeutet, dass es sich nicht um die aktuelle Version handelt.

Eine weitere Lösung besteht darin, `llama.cpp` mit Homebrew zu installieren:

```bash
brew install llama.cpp
```

Dies stellt sicher, dass Sie eine kompatible Version der Bibliothek haben.

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 hours ago
mistral:7b             f974a74358d6    4.1 GB    15 hours ago
```

```bash
ollama remove model
```

Es ist ein großartiges Tool. Es gibt einige Fehler in Ollamac. Zum Beispiel aktualisieren sich mehrere Textfelder in der App, wenn eine Antwort von der lokalen API empfangen wird.

## LLM Farm

Es ist eine großartige iOS-App. In den Einstellungen gibt es etwa 20 Modelle. Beim Importieren eines GGUF-Modells, das von Hugging Face heruntergeladen wurde, kann es zu einem Absturz kommen.

## Vorteile

Das Selbst-Hosting dieser LLM-Modelle ermöglicht es Ihnen, sie lokal ohne Netzwerkzugang auszuführen. Zum Beispiel kann das Ausführen eines lokalen Modells beim Herunterladen großer Dateien, die das Netzwerk verstopfen, von Vorteil sein.

## Ressourcen

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)