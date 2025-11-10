---
audio: false
generated: true
lang: de
layout: post
title: Fehlende libpq-fe.h für psycopg2
translated: true
type: note
---

Beim Versuch, das Python-Paket `psycopg2` zu installieren, sind Sie auf einen Fehler gestoßen, der darauf hinweist, dass das Wheel nicht erfolgreich gebaut werden konnte. Der entscheidende Teil der Fehlermeldung lautet:

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

Dieser Fehler tritt auf, weil die Datei `libpq-fe.h`, eine Header-Datei aus der PostgreSQL-Client-Bibliothek, auf Ihrem System fehlt. Das Paket `psycopg2` benötigt diese Datei, um aus dem Quellcode zu bauen, da es die Schnittstelle bereitstellt, um Python mit PostgreSQL-Datenbanken zu verbinden. Im Folgenden werde ich erklären, warum dies passiert, und eine schrittweise Lösung zur Behebung des Problems bereitstellen.

---

### Warum dieser Fehler auftritt
Das Paket `psycopg2` ist ein PostgreSQL-Adapter für Python. Wenn Sie es mit `pip` installieren, versucht es, seine C-Erweiterungen zu kompilieren. Diese Erweiterungen hängen von der PostgreSQL-Client-Bibliothek ab, insbesondere von den Entwicklungs-Headern wie `libpq-fe.h`. Die Fehlermeldung bestätigt dies:

```
It appears you are missing some prerequisite to build the package from source.
```

Ihrem System, das anscheinend eine Debian-basierte Linux-Distribution ist (basierend auf der Verwendung von `x86_64-linux-gnu-gcc`), fehlen die notwendigen PostgreSQL-Entwicklungsdateien. Ohne diese schlägt die Kompilierung fehl, was den Bau des Wheels für `psycopg2` verhindert.

Die Fehlermeldung schlägt auch zwei Optionen vor:
1.  Installieren Sie das vorgebaute Binärpaket `psycopg2-binary` über PyPI.
2.  Installieren Sie die fehlenden Voraussetzungen und bauen Sie `psycopg2` aus dem Quellcode.

Da Ihr Projekt `psycopg2` (nicht `psycopg2-binary`) in der Requirements-Datei spezifiziert und das Bauen aus dem Quellcode für Kompatibilität oder Anpassung notwendig sein könnte, konzentrieren wir uns auf die Reparatur des Build-Prozesses. Ich werde die Binäroption jedoch später der Vollständigkeit halber erwähnen.

---

### So beheben Sie den Fehler
Um das Problem zu lösen, müssen Sie das PostgreSQL-Client-Entwicklungspaket installieren, das `libpq-fe.h` und andere notwendige Dateien bereitstellt. So gehen Sie vor:

#### Schritt 1: Identifizieren Sie Ihr System
Ihre Build-Ausgabe enthält `x86_64-linux-gnu-gcc`, was darauf hindeutet, dass Sie wahrscheinlich ein Debian-basiertes System wie Ubuntu verwenden. Die Lösung ist darauf zugeschnitten, aber ich werde später Alternativen für andere Distributionen erwähnen.

#### Schritt 2: Installieren Sie das PostgreSQL-Entwicklungspaket
Auf Debian-basierten Systemen (z.B. Ubuntu) enthält das Paket `libpq-dev` die Header der PostgreSQL-Client-Bibliothek, einschließlich `libpq-fe.h`. Installieren Sie es mit dem folgenden Befehl:

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

-   **`sudo apt-get update`**: Stellt sicher, dass Ihre Paketliste aktuell ist.
-   **`sudo apt-get install libpq-dev`**: Installiert die Entwicklungsdateien für die PostgreSQL-Client-Bibliothek.

Dieses Paket platziert `libpq-fe.h` an einem Standardort (typischerweise `/usr/include/postgresql`), den der Build-Prozess durchsucht (wie in Ihrem Include-Pfad zu sehen: `-I/usr/include/postgresql`).

#### Schritt 3: Wiederholen Sie die Installation
Sobald `libpq-dev` installiert ist, versuchen Sie erneut, Ihre Requirements zu installieren:

```bash
pip install -r scripts/requirements/requirements.local.txt
```

Dies sollte nun erfolgreich sein, da die fehlende Datei `libpq-fe.h` verfügbar ist und `psycopg2` so sein Wheel bauen kann.

---

### Überprüfung der Reparatur
Wenn die Installation immer noch fehlschlägt, überprüfen Sie, ob die PostgreSQL-Header korrekt installiert sind:
-   Führen Sie `pg_config --includedir` aus, um zu sehen, wo die Header sich befinden (z.B. `/usr/include/postgresql`).
-   Stellen Sie sicher, dass dies mit dem Include-Pfad im Build-Befehl (`-I/usr/include/postgresql`) übereinstimmt.

Ihre Build-Ausgabe zeigt `-DPG_VERSION_NUM=140018`, was darauf hindeutet, dass PostgreSQL 14 als Ziel verwendet wird. Das Paket `libpq-dev` ist versionsunabhängig und sollte mit den PostgreSQL-14-Headern funktionieren.

---

### Alternative: Verwenden Sie das Binärpaket
Wenn Sie `psycopg2` nicht aus dem Quellcode bauen müssen (z.B. für spezifische Optimierungen oder Kompatibilität), können Sie stattdessen das vorgebaute `psycopg2-binary` installieren:

```bash
pip install psycopg2-binary
```

Um dies in Ihrem Projekt zu verwenden, aktualisieren Sie `scripts/requirements/requirements.local.txt`, um `psycopg2` durch `psycopg2-binary` zu ersetzen. Beachten Sie jedoch, dass `psycopg2-binary` Einschränkungen haben kann (z.B. potenzielle Kompatibilitätsprobleme mit bestimmten PostgreSQL-Versionen), daher ist das Bauen aus dem Quellcode vorzuziehen, wenn Ihr Projekt es erfordert.

---

### Für andere Distributionen
Wenn Sie kein Debian-basiertes System verwenden, installieren Sie das entsprechende Paket:
-   **Red Hat/CentOS/Fedora**: `sudo yum install postgresql-devel` oder `sudo dnf install postgresql-devel`
-   **Arch Linux**: `sudo pacman -S postgresql-libs`
-   **macOS (mit Homebrew)**: `brew install libpq`

Wiederholen Sie anschließend den `pip install`-Befehl.

---

### Zusammenfassung
Der Fehler tritt auf, weil `libpq-fe.h` fehlt, das Teil der PostgreSQL-Client-Entwicklungsdateien ist. Für Ihr Debian-basiertes System sollte die Installation von `libpq-dev` mit `sudo apt-get install libpq-dev` das Problem beheben. Führen Sie danach Ihren `pip install`-Befehl erneut aus, und `psycopg2` sollte erfolgreich gebaut werden. Wenn Sie eine schnellere Lösung bevorzugen und keine Quellcode-Kompilierung benötigen, verwenden Sie stattdessen `psycopg2-binary`.