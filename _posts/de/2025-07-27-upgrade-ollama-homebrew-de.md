---
audio: false
generated: true
image: false
lang: de
layout: post
title: Aktualisierung von Ollama mit Homebrew
translated: true
type: note
---

Um Ollama auf die neueste Version (aktuell v0.10.0, Stand Juli 2025) mit Homebrew auf macOS zu aktualisieren, folge diesen Schritten:

1. Aktualisiere die Formeln von Homebrew, um sicherzustellen, dass die neuesten verfügbaren Versionen bekannt sind:
   ```
   brew update
   ```

2. Aktualisiere speziell Ollama:
   ```
   brew upgrade ollama
   ```

3. Überprüfe die Aktualisierung, indem du die Version prüfst:
   ```
   ollama --version
   ```

Wenn du Ollama als Hintergrunddienst ausführst, starte ihn nach der Aktualisierung neu:
```
brew services restart ollama
```

Alternativ, wenn du es manuell ausführst, stoppe alle bestehenden Prozesse und starte es erneut mit deinem bevorzugten Befehl (z.B. aus den "caveats" in deiner Installationsausgabe):
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

Über diesen Standardprozess hinaus sind keine besonderen Upgrade-Anweisungen erforderlich.

[Ollama Releases](https://github.com/ollama/ollama/releases)