---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG ASCII Armor erklärt
translated: true
type: note
---

In GPG (GNU Privacy Guard) bezieht sich "Armor" auf ASCII-Armor, ein Format, das binäre OpenPGP-Daten (wie verschlüsselte Dateien, Signaturen oder Schlüssel) in eine menschenlesbare, textbasierte Darstellung kodiert. Dies ist nützlich, um Daten über textbasierte Kanäle, wie E-Mail, ohne Beschädigung zu übertragen – ähnlich wie uuencode oder base64 funktionieren, jedoch mit zusätzlichen Headern (z.B. "-----BEGIN PGP MESSAGE-----") und Prüfsummen für die Integrität.

Sie können es mit der Option `--armor` (oder `-a`) während Befehlen wie Verschlüsselung (`gpg -a -e file.txt`) oder Schlüsselexport (`gpg --armor --export keyid`) aktivieren, wodurch das Ergebnis in diesem Armored-Textformat anstelle von rohen Binärdaten ausgegeben wird.

## Referenzen
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)