---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von Emacs auf RHEL
translated: true
type: note
---

### Emacs auf Red Hat Enterprise Linux installieren

Red Hat Enterprise Linux (RHEL) verwendet primär den DNF-Paketmanager zur Installation von Software. Emacs ist in den Standard-Repositorys verfügbar, sodass die Installation unkompliziert ist. Nachfolgend sind die Schritte für moderne Versionen (RHEL 8 und später) aufgeführt. Für ältere Versionen (z.B. RHEL 7) ersetzen Sie `dnf` durch `yum`.

#### Voraussetzungen
- Stellen Sie sicher, dass Sie über Root-Rechte verfügen (verwenden Sie `sudo`).
- Ihr System sollte bei Red Hat Subscription Management registriert sein, wenn Sie die offiziellen RHEL-Repositorys verwenden.

#### Installationsschritte
1. **Aktualisieren Sie Ihren Paket-Cache** (empfohlen, um die neueste verfügbare Version zu erhalten):  
   ```
   sudo dnf update
   ```

2. **Installieren Sie Emacs**:  
   ```
   sudo dnf install emacs
   ```  
   Dadurch wird die neueste stabile Version installiert, die in den Repositorys verfügbar ist (z.B. Emacs 28.x oder 29.x, abhängig von Ihrer RHEL-Version).

3. **Überprüfen Sie die Installation**:  
   Führen Sie den folgenden Befehl aus, um die Version zu prüfen:  
   ```
   emacs --version
   ```  
   Sie sollten eine Ausgabe wie `GNU Emacs 28.2` (oder ähnlich) sehen.

#### Hinweise
- Wenn Sie eine ältere RHEL-Version mit YUM verwenden (z.B. RHEL 7), lautet der Befehl `sudo yum install emacs`.
- Für die allerneueste Emacs-Version (z.B. 29+) müssen Sie möglicherweise aus dem Quellcode kompilieren oder Drittanbieter-Repositorys wie EPEL verwenden, da die Basis-Repositorys möglicherweise hinterherhinken.
- Um Emacs zu starten, geben Sie einfach `emacs` in das Terminal ein.

[GNU Emacs FAQ: Installing Emacs](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[Red Hat Documentation: Managing Software with DNF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)