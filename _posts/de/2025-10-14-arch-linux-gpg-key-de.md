---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Arch Linux ISO-Verifizierungs-GPG-Schlüssel
translated: true
type: note
---

Sie haben diesen GPG-Schlüssel (den von Pierre Schmitz, mit dem Fingerabdruck `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C`) in Ihrem Schlüsselbund, da es der offizielle Signaturschlüssel ist, der von Arch Linux-Entwicklern verwendet wird, um ihre ISO-Abbilder kryptografisch zu signieren. Dies stellt sicher, dass der Download authentisch ist und nicht manipuliert wurde.

Als Sie einen bootfähigen USB-Stick für die Installation von Arch Linux auf macOS vorbereitet haben (wahrscheinlich gemäß der offiziellen Arch Wiki-Anleitung), umfasst der Standardprozess zwei Schritte für die Verifizierung:
1. Herunterladen der ISO und ihrer `.sig`-Datei.
2. Importieren des relevanten GPG-Schlüssels des Entwicklers (in diesem Fall Pierre Schmitz, da er einer der Hauptunterzeichner für aktuelle ISOs ist), um die Signatur mit einem Befehl wie `gpg --verify archlinux-YYYY.MM.DD-x86_64.iso.sig` zu überprüfen.

Sie haben wahrscheinlich so etwas wie `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` ausgeführt, um ihn abzurufen und zu importieren, wodurch er dauerhaft zu Ihrem lokalen GPG-Schlüsselbund hinzugefügt wurde. Deshalb wird er in `gpg --list-keys` angezeigt.

Es ist harmlos – GPG-Schlüssel sind nur öffentliche Daten für Verifizierungszwecke – und viele Arch-Benutzer haben am Ende einige davon, nachdem sie ISOs verifiziert haben. Wenn Sie ihn nicht mehr benötigen und entfernen möchten, führen Sie aus:
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
(Sie werden zur Bestätigung aufgefordert; es löscht nur den öffentlichen Schlüssel, nicht bereits verifizierte Signaturen.)

[Arch Linux ISO Download Seite](https://archlinux.org/download/)  
[Arch Wiki: Install Arch Linux on a Mac](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[Pierre Schmitz's GPG Keys](https://pierre-schmitz.com/gpg-keys/)