---
audio: false
generated: true
lang: de
layout: post
title: PortAudio und PyAudio
translated: true
type: note
---

Der Fehler tritt auf, weil **pyaudio** die PortAudio-Entwicklungsheader zum Kompilieren benötigt, die auf Ihrem System fehlen. So beheben Sie das Problem:

### Schritt-für-Schritt-Lösung:

1. **Installieren Sie die PortAudio-Entwicklungsheader** (erforderlich für pyaudio):
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **Installieren Sie Python-Entwicklungswerkzeuge** (falls noch nicht installiert):
```bash
sudo apt install python3-dev
```

3. **Wiederholen Sie die Installation**:
```bash
pip install -r requirements.local.txt
```

### Falls Sie immer noch pycrypto-Probleme haben:
Das pycrypto-Paket ist veraltet und kann Kompatibilitätsprobleme verursachen. Ersetzen Sie es durch **pycryptodome**, indem Sie Ihre `requirements.local.txt` ändern:

1. Öffnen Sie die Requirements-Datei:
```bash
nano requirements.local.txt
```

2. Ersetzen Sie `pycrypto` mit:
```
pycryptodome
```

3. Speichern Sie und führen Sie die Installation erneut aus:
```bash
pip install -r requirements.local.txt
```

### Warum das funktioniert:
- `portaudio19-dev` stellt die fehlenden PortAudio-Header bereit, die zum Kompilieren von pyaudio benötigt werden
- `python3-dev` enthält die notwendigen Python-Entwicklungsheader
- `pycryptodome` ist ein gewarteter Drop-in-Ersatz für das veraltete pycrypto

### Alternative für pycrypto (falls Sie es unbedingt behalten müssen):
Wenn Sie speziell pycrypto benötigen, installieren Sie zuerst die Build-Abhängigkeiten:
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
Beachten Sie jedoch, dass pycrypto Kompatibilitätsprobleme mit neueren Python-Versionen hat.

Nach diesen Schritten sollten alle Pakete korrekt installiert werden. Die DEPRECATION-Warnungen bezüglich Legacy-Builds sind informativer Natur und verhindern die Installation nicht - sie weisen darauf hin, dass die Pakete in Zukunft auf PEP 517-Builds migriert werden müssen.