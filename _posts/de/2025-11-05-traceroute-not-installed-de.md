---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Traceroute nicht standardmäßig installiert
translated: true
type: note
---

Traceroute ist auf Linux definitiv verfügbar – es ist ein Standard-Netzwerkdiagnosetool, das den Route verfolgt, die Pakete zu einem Ziel nehmen. Es ist jedoch in vielen modernen Distributionen (wie Ubuntu, Fedora oder Debian-Minimal-Installationen) oft **nicht standardmäßig installiert**, um Basis-Systeme schlank zu halten. Deshalb erscheint es nicht in Ihrer Tab-Vervollständigung für "trac".

### Schnelle Lösung
Installieren Sie es über Ihren Paketmanager:
- **Debian/Ubuntu**: `sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS**: `sudo dnf install traceroute` (oder `sudo yum install traceroute` auf älteren Versionen)
- **Arch**: `sudo pacman -S traceroute`

Sobald es installiert ist, sollte die Eingabe von `trac` + Tab nun `traceroute` in der Liste enthalten. Sie können es dann z.B. mit `traceroute example.com` ausführen, um es zu testen.

Wenn Sie sich in einer containerisierten oder sehr minimalistischen Umgebung befinden (z.B. Alpine Linux), wird möglicherweise `tr` als Alias verwendet oder ein anderes Paket benötigt – teilen Sie mir Ihre Distribution für genauere Angaben mit!