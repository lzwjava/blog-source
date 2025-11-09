---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Zed unter Ubuntu 24.04 installieren
translated: true
type: note
---

Für Ubuntu 24.04 LTS ist die unkomplizierteste und offizielle Installationsmethode für Zed (den hochperformanten Code-Editor) über das bereitgestellte Shell-Skript. Dieses funktioniert nativ auf den meisten Linux-Distributionen, einschließlich Debian-basierten wie Ubuntu. Es kümmert sich automatisch um Abhängigkeiten und stellt sicher, dass Sie die neueste stabile Version erhalten.

### Empfohlene Installation: Offizielles Skript
Führen Sie dies in Ihrem Terminal aus:
```
curl -f https://zed.dev/install.sh | sh
```
- Dies installiert Zed in `~/.local/bin/zed` (fügen Sie es ggf. zu Ihrem PATH hinzu: `export PATH="$HOME/.local/bin:$PATH"` in `~/.bashrc` oder ähnlich).
- Voraussetzungen: Ihr System (glibc 2.39 auf Kernel 6.14) erfüllt die Anforderungen (x86_64 glibc >= 2.31).
- Starten Sie Zed nach der Installation mit `zed` oder über das GNOME-App-Menü.
- Für den Preview-Kanal (Nightly Builds): `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`.

Wenn Sie ein gesandboxtes, universelles Paket bevorzugen (keine nativen Abhängigkeiten), verwenden Sie die Flathub-Option aus Ihrer Liste (`dev.zed.Zed`) via Flatpak:
1. Installieren Sie Flatpak, falls nicht vorhanden: `sudo apt update && sudo apt install flatpak`.
2. Fügen Sie das Flathub-Repository hinzu: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3. Installation: `flatpak install flathub dev.zed.Zed`.
4. Ausführung: `flatpak run dev.zed.Zed`.

Das Skript ist im Allgemeinen schneller und besser in eine Desktop-Umgebung wie GNOME integriert, aber Flatpak ist ideal, wenn Sie Isolierung wünschen oder es bereits für andere Apps verwenden. Vermeiden Sie die anderen Optionen in Ihrer Liste, da diese für nicht-Debian-Distributionen gedacht sind und auf Ubuntu nicht ohne zusätzliche Einrichtung funktionieren.

### Referenzen
- [Zed Linux Installation Docs](https://zed.dev/docs/linux)
- [Zed on Linux Announcement](https://zed.dev/linux)
- [Repology Zed Packages](https://repology.org/project/zed-editor/versions)