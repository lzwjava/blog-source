---
audio: false
generated: false
lang: de
layout: post
title: Versuche llama.cpp
translated: true
---

## llama.cpp

Beim Versuch, `llama.cpp` mit einem Modell zu starten, könnten Sie einen Fehler wie diesen erhalten:

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: Laden des Modells von models/7B/Phi-3-mini-4k-instruct-q4.gguf
Fehler beim Laden des Modells: unbekannte (Magie, Version) Kombination: 46554747, 00000003; handelt es sich wirklich um eine GGML-Datei?
llama_load_model_from_file: Fehler beim Laden des Modells
llama_init_from_gpt_params: Fehler: Fehler beim Laden des Modells 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: Fehler: Modell konnte nicht geladen werden
```

Dieser Fehler tritt auf, weil Sie das `main`-Programm ausführen. Das Ausführen der `llama-cli` oder `llama-server`-Programme, die sich unter `build/bin` befinden, sollte das Problem beheben.

Das `main`-Programm wurde am 8. August 2023 erstellt, was bedeutet, dass es nicht die aktuelle Version ist.

Eine weitere Lösung besteht darin, `llama.cpp` mit Homebrew zu installieren:

```bash
brew install llama.cpp
```

Dadurch wird sichergestellt, dass Sie eine kompatible Version der Bibliothek haben.

## Modell bereitstellen

```bash
/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
```

Die Parameter `--ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1` sind wichtig. Sie verbessern die Geschwindigkeit.

## LLM Farm

Es ist eine großartige iOS-App. In den Einstellungen gibt es etwa 20 Modelle. Beim Importieren eines GGUF-Modells, das von Hugging Face heruntergeladen wurde, kann es zu einem Absturz kommen.

## Vorteile

Das Selbsthosting dieser LLM-Modelle ermöglicht es Ihnen, sie lokal ohne Netzwerkzugriff auszuführen. Zum Beispiel, wenn große Dateien heruntergeladen werden, die das Netzwerk überlasten, kann das Ausführen eines lokalen Modells vorteilhaft sein.

## Ressourcen

*   [Hugging Face GGML Modelle](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)