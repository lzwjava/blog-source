---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Standard-Texteditoren in RHEL Minimal
translated: true
type: note
---

In Red Hat Enterprise Linux (RHEL), insbesondere bei einer Minimal-Installation (dem Standard für Server und schlanke Setups), ist der einzige standardmäßig verfügbare Text-Editor **vi**, bereitgestellt durch das Paket `vim-minimal`. Dies bietet Ihnen eine grundlegende, kompatible Implementierung des klassischen `vi`-Befehls zum Bearbeiten von Dateien im Terminal.

- Das vollständige **`vim`** (die erweiterte Version mit mehr Funktionen, Syntax-Hervorhebung usw.) ist nicht standardmäßig installiert. Sie können es mit `sudo dnf install vim-enhanced` hinzufügen.
- **Nano** und **Emacs** sind in der Minimal-Installation nicht enthalten. Sie sind in den Repositories verfügbar, erfordern aber eine explizite Installation:
  - Für Nano: `sudo dnf install nano`
  - Für Emacs: `sudo dnf install emacs`

Dies hält die Minimal-Installation schlank (etwa 200-300 Pakete insgesamt), um Sicherheit und Leistung zu priorisieren. Wenn Sie eine vollständige Desktop- oder Server-Installation (nicht minimal) durchführen, könnten je nach gewählter Umgebung mehr Tools mitinstalliert werden.

[Erste Schritte mit Nano (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[Warum sind in RHEL standardmäßig zwei vim installiert?](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[RHEL 9 Paketmanifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)