---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verwendung von Vorwärtsschrägstrichen für GPG-Heimatverzeichnisse
translated: true
type: note
---

### Pfadtrennzeichen für GPGs `--homedir` in Git Bash (Windows)

Verwenden Sie in Git Bash unter Windows **immer Schrägstriche (`/`)** für den `--homedir`-Pfad. Git Bash ist eine Unix-ähnliche Umgebung (basierend auf MSYS2) und erwartet daher POSIX-artige Pfade mit `/` als Trennzeichen. Backslashes (`\`) werden höchstwahrscheinlich Fehler verursachen, da GPG in diesem Kontext sie nicht nativ ohne Escaping verarbeitet, und es ist unnötiger Aufwand.

#### Warum `/`?
- Git Bash bildet Windows-Laufwerke auf eine Unix-ähnliche Struktur ab: `C:\Users\IhrName` wird zu `/c/Users/IhrName`.
- GPG (mitgeliefert mit Git für Windows) folgt der gleichen Konvention. Die Verwendung von `\` kann zu Pfadauflösungsfehlern führen oder doppeltes Escaping (z.B. `\\`) erfordern, was fehleranfällig ist.
- Offizielle Beispiele und Community-Setups (z.B. für Git-Signing) verwenden durchgängig `/` in Git Bash.

#### Beispiel zur Verwendung
```
gpg --homedir /c/Users/IhrName/.gnupg --list-secret-keys
```
- Dies verweist auf Ihr standardmäßiges GPG-Verzeichnis auf dem C:-Laufwerk.
- Für ein benutzerdefiniertes Verzeichnis: `gpg --homedir /d/MyCustomGpgDir --full-generate-key` (D:-Laufwerk).

#### Schnelltest
In Git Bash:
1. Führen Sie `pwd` aus – die Ausgabe wird etwa `/c/Users/IhrName` lauten (alles mit `/`).
2. Versuchen Sie `gpg --homedir /c/Users/IhrName/.gnupg --version` (funktioniert).
3. Vergleichen Sie mit `\`: `gpg --homedir C:\Users\IhrName\.gnupg --version` (schlägt fehl oder gibt eine Warnung aus).

Wenn Sie Windows CMD/PowerShell verwenden, akzeptieren diese sowohl `/` als auch `\`, aber bleiben Sie in Git Bash der Konsistenz halber bei `/`. Für mehr Informationen siehe [GnuPG Handbuch zu Konfigurationsoptionen](https://www.gnupg.org/documentation/manuals/gnupg/Configuration-Options.html).