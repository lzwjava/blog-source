---
audio: true
lang: de
layout: post
title: Versuche llama.cpp
translated: true
---

## llama.cpp

Wenn Sie versuchen, `llama.cpp` mit einem Modell auszuführen, könnten Sie auf einen Fehler wie diesen stoßen:

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

Dieser Fehler tritt auf, weil ich das `main`-Programm ausführe. Das Ausführen der Programme `llama-cli` oder `llama-server`, die sich unter `build/bin` befinden, sollte das Problem beheben.

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

Es ist ein großartiges Werkzeug. Es gibt einige Fehler in Ollamac. Zum Beispiel, wenn es eine Antwort von der lokalen API erhält, aktualisieren sich mehrere Textfelder in der App.

## LLM Farm

Es ist eine großartige iOS-App. In den Einstellungen gibt es etwa 20 Modelle. Wenn wir ein GGUF-Modell selbst importieren, das von Hugging Face heruntergeladen wurde, kann dies zu einem Absturz führen.

## Vorteile

Das Selbsthosten dieser LLM-Modelle ermöglicht es Ihnen, sie lokal auszuführen, ohne auf Netzwerkzugriff angewiesen zu sein. Zum Beispiel kann es von Vorteil sein, ein lokales Modell auszuführen, wenn große Dateien heruntergeladen werden, die das Netzwerk belasten.

## Ressourcen

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)