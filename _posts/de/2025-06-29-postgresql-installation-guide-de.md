---
audio: false
generated: true
lang: de
layout: post
title: Behebung von psycopg2 durch Installation von PostgreSQL
translated: true
type: note
---

Der Fehler, den du erhältst, zeigt an, dass das `psycopg2`-Paket die PostgreSQL-`pg_config`-Ausführbare Datei benötigt, um aus dem Quellcode zu bauen, diese aber auf deinem System nicht gefunden wird. Das bedeutet, dass du PostgreSQL auf deinem macOS-System installieren musst, um die notwendigen Abhängigkeiten bereitzustellen. Nachfolgend findest du die Schritte zur Installation von PostgreSQL auf macOS und zur Behebung des Problems.

### Schritte zur Installation von PostgreSQL auf macOS

#### 1. **Installation von PostgreSQL mit Homebrew (Empfohlen)**
Homebrew ist der einfachste Weg, um PostgreSQL auf macOS zu installieren und zu verwalten.

1. **Homebrew installieren (falls noch nicht geschehen)**:
   - Öffne das Terminal und führe aus:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Folge den Anweisungen auf dem Bildschirm, um die Homebrew-Installation abzuschließen.

2. **PostgreSQL installieren**:
   - Führe im Terminal aus:
     ```bash
     brew install postgresql
     ```
   - Dieser Befehl installiert PostgreSQL und seine Abhängigkeiten, einschließlich der für `psycopg2` benötigten `pg_config`-Ausführbaren Datei.

3. **PostgreSQL starten**:
   - Um den PostgreSQL-Dienst zu starten, führe aus:
     ```bash
     brew services start postgresql
     ```
   - Alternativ, um ihn manuell für eine einzelne Sitzung zu starten:
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **Installation überprüfen**:
   - Prüfe, ob PostgreSQL installiert und aktiv ist:
     ```bash
     psql --version
     ```
   - Du solltest die PostgreSQL-Version sehen (z.B. `psql (PostgreSQL) 17.0`).
   - Du kannst dich auch in die PostgreSQL-Shell einloggen, um es zu bestätigen:
     ```bash
     psql -U $(whoami)
     ```

#### 2. **`psycopg2` nach der PostgreSQL-Installation installieren**
Sobald PostgreSQL installiert ist, versuche, `psycopg2` erneut zu installieren. Die `pg_config`-Ausführbare Datei sollte jetzt in deinem PATH verfügbar sein.

1. **`psycopg2` installieren**:
   - Führe aus:
     ```bash
     pip install psycopg2
     ```
   - Wenn du eine Requirements-Datei verwendest, führe aus:
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **Alternative: `psycopg2-binary` installieren (Einfachere Option)**:
   - Wenn du das Bauen von `psycopg2` aus dem Quellcode (was PostgreSQL-Abhängigkeiten erfordert) vermeiden möchtest, kannst du das vorkompilierte `psycopg2-binary`-Paket installieren:
     ```bash
     pip install psycopg2-binary
     ```
   - Hinweis: `psycopg2-binary` wird für Produktionsumgebungen aufgrund potenzieller Kompatibilitätsprobleme nicht empfohlen, ist aber für Entwicklung oder Tests in Ordnung.

#### 3. **Optional: `pg_config` zum PATH hinzufügen (falls nötig)**
Wenn die `pg_config`-Ausführbare Datei nach der Installation von PostgreSQL immer noch nicht gefunden wird, musst du sie möglicherweise manuell zu deinem PATH hinzufügen.

1. `pg_config` lokalisieren:
   - Homebrew installiert PostgreSQL typischerweise in `/opt/homebrew/bin` (für Apple Silicon) oder `/usr/local/bin` (für Intel Macs).
   - Überprüfe den Speicherort:
     ```bash
     find /opt/homebrew -name pg_config
     ```
     oder
     ```bash
     find /usr/local -name pg_config
     ```

2. Zum PATH hinzufügen:
   - Wenn `pg_config` gefunden wurde (z.B. in `/opt/homebrew/bin`), füge es zu deinem PATH hinzu, indem du deine Shell-Konfigurationsdatei bearbeitest (z.B. `~/.zshrc` oder `~/.bash_profile`):
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - Wende die Änderungen an:
     ```bash
     source ~/.zshrc
     ```

3. `pg_config` überprüfen:
   - Führe aus:
     ```bash
     pg_config --version
     ```
   - Wenn eine Version zurückgegeben wird, ist der PATH korrekt gesetzt.

#### 4. **Fehlerbehebung**
- **Fehler besteht fort**: Wenn `pip install psycopg2` weiterhin fehlschlägt, stelle sicher, dass du die notwendigen Build-Tools hast:
  - Installiere die Xcode Command Line Tools:
    ```bash
    xcode-select --install
    ```
  - Installiere `libpq` (PostgreSQL-Client-Bibliothek) explizit, falls nötig:
    ```bash
    brew install libpq
    ```

- **Python-Version-Kompatibilität**: Stelle sicher, dass deine Python-Version (in deinem Fall 3.13) mit `psycopg2` kompatibel ist. Wenn Probleme bestehen bleiben, ziehe die Verwendung einer virtuellen Umgebung mit einer etwas älteren Python-Version in Betracht (z.B. 3.11 oder 3.12):
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **Homebrew überprüfen**: Stelle sicher, dass Homebrew auf dem neuesten Stand ist:
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **Alternative Installationsmethoden (Optional)**
Wenn du Homebrew nicht verwenden möchtest, kannst du PostgreSQL auch installieren über:
- **Postgres.app**:
  - Lade es von [postgresapp.com](https://postgresapp.com/) herunter.
  - Folge den Setup-Anweisungen, um PostgreSQL zu installieren und zu starten.
  - Füge das `bin`-Verzeichnis (z.B. `/Applications/Postgres.app/Contents/Versions/latest/bin`) wie oben beschrieben zu deinem PATH hinzu.
- **Offizielles PostgreSQL-Installationsprogramm**:
  - Lade das macOS-Installationsprogramm von [postgresql.org](https://www.postgresql.org/download/macosx/) herunter.
  - Folge dem Installations-Assistenten.

#### 6. **Projekt erneut versuchen**
Nach der Installation von PostgreSQL und `psycopg2` (oder `psycopg2-binary`), versuche erneut, dein Projekt auszuführen oder die Requirements neu zu installieren:
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### Zusätzliche Hinweise
- **Warum der Fehler auftrat**: Das `psycopg2`-Paket benötigt die PostgreSQL-Entwicklungsbibliotheken (insbesondere `libpq`), um aus dem Quellcode zu bauen. Die Installation von PostgreSQL über Homebrew stellt diese Bibliotheken bereit.
- **Produktionsüberlegungen**: Verwende für die Produktion `psycopg2` (nicht `psycopg2-binary`) und stelle sicher, dass deine PostgreSQL-Version mit der Zielumgebung übereinstimmt.
- **Dokumentation**: Weitere Details findest du im `psycopg2`-Installationsleitfaden unter [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html).

Wenn du auf weitere Probleme stößt, teile bitte die spezifische Fehlermeldung mit, und ich kann bei der weiteren Fehlerbehebung helfen!