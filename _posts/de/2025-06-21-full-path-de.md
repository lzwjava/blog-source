---
audio: false
generated: true
lang: de
layout: post
title: Ermitteln des vollständigen Dateipfads in Ubuntu
translated: true
type: note
---

In Ubuntu können Sie den vollständigen Pfad einer Datei mit den Befehlen `realpath` oder `readlink -f` abrufen. Für Ihr Beispiel mit `geckodriver` können Sie Folgendes ausführen:

```bash
realpath ./geckodriver
```

oder

```bash
readlink -f ./geckodriver
```

Beide geben den vollständigen Pfad aus, z. B.:

```
/home/lzw/bin/geckodriver
```

Der Befehl `realpath` ist unkompliziert und wird häufig für diesen Zweck verwendet. Falls `realpath` nicht installiert ist, können Sie es mit folgendem Befehl installieren:

```bash
sudo apt install realpath
```

Alternativ ist `readlink -f` normalerweise standardmäßig als Teil von coreutils verfügbar.