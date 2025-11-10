---
audio: false
generated: true
image: false
lang: de
layout: post
title: Ändern des Open-WebUI-Ports
translated: true
type: note
---

Um den Port zu ändern, wenn Sie Open WebUI mit dem Befehl `open-webui serve` ausführen (typischerweise nach der Installation via pip), verwenden Sie das Flag `--port` gefolgt von der gewünschten Port-Nummer. Der Standardport ist 8080.

### Schritte:
1. Stellen Sie sicher, dass Open WebUI installiert ist:  
   ```
   pip install open-webui
   ```

2. Führen Sie den Server auf einem anderen Port aus (z. B. 3000):  
   ```
   open-webui serve --port 3000
   ```

   - Dadurch wird die WebUI unter `http://localhost:3000` erreichbar sein (oder der IP-Adresse Ihres Servers mit dem neuen Port).
   - Hinweis: Die Umgebungsvariable `PORT` wird beim Verwenden des `serve`-Befehls ignoriert; Sie müssen stattdessen das `--port` Flag verwenden.

Falls Sie Docker anstelle einer direkten Installation verwenden:
- Setzen Sie die Umgebungsvariable `PORT`, z. B. `docker run -e PORT=3000 ...`.
- Mappen Sie den Port extern mit `-p <host_port>:3000` (passen Sie dies bei Bedarf an).

Detaillierte Installations- und Konfigurationsanleitungen finden Sie in der offiziellen Dokumentation.

[Environment Variable Configuration | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Quick Start | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)