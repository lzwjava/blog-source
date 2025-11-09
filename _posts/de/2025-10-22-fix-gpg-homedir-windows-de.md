---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Korrigieren von GPG-Heimatverzeichnispfaden unter Windows
translated: true
type: note
---

Ja, du hast recht. In Git Bash unter Windows (das in einer MSYS2/Cygwin-ähnlichen Umgebung läuft), führt die Verwendung von Backslashes (`\`) im `--homedir`-Pfad für `gpg` dazu, dass die Shell das Argument aufgrund der Funktionsweise von Escapes und Pfadkonvertierungen falsch interpretiert. Dies verfälscht den Pfad (z. B. könnte `C:\Users\me\.gnupg` zu etwas Ungültigem wie `C:Usersme.gnupg` aufgelöst werden oder während der automatischen Konvertierung in das Windows-Format weiter beschädigt werden), was das Verzeichnis nicht auffindbar macht. Infolgedessen kann GPG die Schlüsseldateien nicht finden, was zu einem "no secret key"-Fehler (oder ähnlichem, wie "No such file or directory" für `pubring.kbx`) führt.

### Schnelle Lösung
- Verwende Schrägstriche (`/`) mit dem MSYS2-stiligen Laufwerkpräfix: `gpg --homedir /c/Users/me/.gnupg ...`
- Dies wird von MSYS2 automatisch in den korrekten Windows-Pfad (z. B. `C:\Users\me\.gnupg`) konvertiert, wenn es an das native GPG-Binary übergeben wird.
- Vermeide Laufwerksbuchstaben wie `c:/` ohne das führende `/` – diese werden als relative Pfade behandelt, die Ihr aktuelles Arbeitsverzeichnis voranstellen und denselben Suchfehler verursachen.

Für Umgebungsvariablen wie `GNUPGHOME` gilt dieselbe Regel: setze sie mit `/` (z. B. `export GNUPGHOME=/c/Users/me/.gnupg`).

[MSYS2 Filesystem Paths](https://www.msys2.org/docs/filesystem-paths/)  
[GNUPGHOME in MSYS2 Discussion](https://lists.gnupg.org/pipermail/gnupg-users/2025-February/067536.html)  
[GPG --homedir Bug on Windows/MSYS2](https://www.reddit.com/r/GnuPG/comments/1cl4dw8/bug_windows_homedir_with_drive_letter_treated_as/)