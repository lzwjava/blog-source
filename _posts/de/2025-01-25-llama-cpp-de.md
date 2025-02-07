---
audio: false
lang: de
layout: post
title: llama.cpp ausprobieren
translated: true
---

## llama.cpp

Beim Versuch, `llama.cpp` mit einem Modell auszuführen, kann folgender Fehler auftreten:

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

Dieser Fehler tritt auf, weil Sie das `main`-Programm ausführen. Die Ausführung der Programme `llama-cli` oder `llama-server` unter `build/bin` sollte das Problem beheben.

Das `main`-Programm wurde am 8. August 2023 erstellt, d. h. es ist nicht der aktuelle Build.

Eine andere Lösung ist die Installation von `llama.cpp` mit Homebrew:

```bash
brew install llama.cpp
```

Dies stellt sicher, dass Sie eine kompatible Version der Bibliothek haben.

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    vor 14 Stunden
mistral:7b             f974a74358d6    4.1 GB    vor 15 Stunden
```

```bash
ollama remove model
```

Es ist ein großartiges Werkzeug. Es gibt einige Fehler in Ollamac. Beispielsweise werden bei Empfang einer Antwort von der lokalen API mehrere Textfelder in der App aktualisiert.

Unter Linux läuft Ollama jedoch als Systemdienst. Hier ist die Serviceconfigurationsdatei:

`/etc/systemd/system/ollama.service`:

```bash
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/home/lzw/.local/bin:/home/lzw/bin:/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"

[Install]
WantedBy=default.target
```

Verwenden Sie die folgenden Befehle, um den Ollama-Dienst zu steuern:

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

Es ist eine großartige iOS-App. In den Einstellungen gibt es etwa 20 Modelle. Beim eigenständigen Importieren von GGUF-Modellen, die von Hugging Face heruntergeladen werden, kann es zu einem Absturz kommen.

## Vorteile

Das Self-Hosting dieser LLM-Modelle ermöglicht es Ihnen, sie lokal auszuführen, ohne Netzwerkzugriff zu benötigen. Beispielsweise kann die Ausführung eines lokalen Modells von Vorteil sein, wenn große Dateien heruntergeladen werden, die das Netzwerk belasten.

## Ressourcen

*   [Hugging Face GGML Modelle](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
