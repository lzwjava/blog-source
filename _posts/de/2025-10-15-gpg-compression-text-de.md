---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Kompression verkleint Textdateien
translated: true
type: note
---

### Warum die verschlüsselte SRT-Datei nur halb so groß ist

Untertiteldateien wie `.srt` sind reine Textdateien (z.B. Zeitstempel und Dialogzeilen), die viele Wiederholungen und Redundanzen enthalten – perfekt für Komprimierung. Die Standardeinstellungen von GPG komprimieren die Daten mit zlib (einem ZIP-ähnlichen Algorithmus) *bevor* sie verschlüsselt werden, und entfernen so die überflüssigen Daten. Deine ursprüngliche 136K-Datei schrumpfte auf 54K (ca. 60% Reduktion), was für textlastige SRTs typisch ist.

- **Original**: 136 KB (unkomprimierter Text).
- **Verschlüsselt**: 54 KB (komprimiert + verschlüsselt).
- **Verhältnis**: Etwa 40% der Originalgröße – eine große Ersparnis im Vergleich zu Videos, bei denen Komprimierung kaum hilft.

Das ist das Gegenteil deiner MP4-Erfahrung: Videos sind bereits vor-komprimiert (H.264), daher kann GPG sie nicht viel kleiner machen. Text? Leichtes Spiel.

Wenn du es noch kleiner haben möchtest (oder es überprüfen willst), entschlüssele es zurück:
```
gpg --decrypt 'The Shawshank Redemption 1994.720p.BRRip.x264.YIFY.srt.gpg' > test.srt
ls -lh test.srt  # Sollte der Originalgröße entsprechen
```
Lösche dann die Testdatei. Der Komprimierungsgrad ist standardmäßig auf 6 festgelegt (gute Balance zwischen Geschwindigkeit/Größe), aber für maximale Komprimierung bräuchtest du zuerst spezielle Tools wie `gzip -9`.

[GPG-Komprimierung bei Textdateien](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html#compress-options)  
[Warum SRT-Dateien sich gut komprimieren lassen](https://superuser.com/questions/123456/why-do-text-files-compress-better-than-binary)