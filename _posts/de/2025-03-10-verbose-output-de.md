---
audio: false
generated: true
lang: de
layout: post
title: Die Kunst des Krieges
translated: true
type: note
---

Hier sind weitere Beispiele zur Aktivierung der ausführlichen Ausgabe in verschiedenen Tools und Systemen, die das Thema der Bereitstellung detaillierter Rückmeldungen oder Protokollierung erweitern:

- **PowerShell**: Um die ausführliche Ausgabe zu aktivieren, verwenden Sie den `-Verbose`-Parameter mit Cmdlets, die ihn unterstützen. Zum Beispiel:
  ```powershell
  Get-Process -Verbose
  ```
  Alternativ können Sie die Variable `$VerbosePreference` global setzen:
  ```powershell
  $VerbosePreference = "Continue"
  ```

- **CMake**: Um eine ausführliche Ausgabe während des Build-Prozesses zu erhalten, verwenden Sie das Flag `--verbose` oder setzen `VERBOSE=1`:
  ```bash
  cmake --build . --verbose
  ```
  Oder:
  ```bash
  make VERBOSE=1
  ```

- **Make**: Um die ausführliche Ausgabe zu aktivieren und alle ausgeführten Befehle zu sehen, verwenden Sie das Flag `-d` für Debugging oder vermeiden Sie die Stillschaltung der Ausgabe mit `@`:
  ```bash
  make -d
  ```
  Oder bearbeiten Sie die Makefile, um die `@`-Präfixe vor Befehlen zu entfernen.

- **GCC (GNU Compiler Collection)**: Für eine ausführliche Kompilierungsausgabe verwenden Sie das Flag `-v`:
  ```bash
  gcc -v -o output source.c
  ```

- **GDB (GNU Debugger)**: Um die Ausführlichkeit zu erhöhen, verwenden Sie den Befehl `set verbose on` innerhalb von GDB:
  ```gdb
  (gdb) set verbose on
  (gdb) run
  ```

- **Ruby**: Führen Sie Ruby-Skripte mit dem ausführlichen Modus unter Verwendung der Flags `-v` oder `--verbose` aus:
  ```bash
  ruby -v script.rb
  ```
  Für zusätzliche Warnungen verwenden Sie `-w`:
  ```bash
  ruby -w script.rb
  ```

- **Perl**: Aktivieren Sie die ausführliche Ausgabe mit dem Flag `-v` oder verwenden Sie das `diagnostics`-Pragma für detaillierte Fehlermeldungen:
  ```bash
  perl -v script.pl
  ```
  Oder im Skript:
  ```perl
  use diagnostics;
  ```

- **PHP**: Führen Sie PHP-Skripte mit ausführlicher Fehlerberichterstattung aus, indem Sie `error_reporting` und `display_errors` in der `php.ini` setzen:
  ```ini
  error_reporting = E_ALL
  display_errors = On
  ```
  Oder über die Kommandozeile:
  ```bash
  php -d error_reporting=E_ALL script.php
  ```

- **R**: Um die ausführliche Ausgabe in R-Skripten zu aktivieren, verwenden Sie das Argument `verbose=TRUE` in Funktionen, die es unterstützen (z.B. `install.packages`):
  ```R
  install.packages("dplyr", verbose=TRUE)
  ```

- **Go (Golang)**: Für eine ausführliche Ausgabe während der Kompilierung oder von Tests verwenden Sie das Flag `-v`:
  ```bash
  go build -v
  go test -v
  ```

- **Rust (Cargo)**: Aktivieren Sie die ausführliche Ausgabe mit Cargo unter Verwendung der Flags `-v` oder `-vv`:
  ```bash
  cargo build -v
  cargo run -vv
  ```

- **Jenkins**: Um die ausführliche Protokollierung für eine Pipeline zu aktivieren, fügen Sie die `verbose`-Option im Skript hinzu oder konfigurieren Sie die Konsolenausgabe in den Job-Einstellungen. Zum Beispiel in einer Jenkinsfile:
  ```groovy
  sh 'some_command --verbose'
  ```
  Alternativ können Sie die Systemeigenschaft `-Dhudson.model.TaskListener.verbose=true` beim Starten von Jenkins setzen.

- **Vagrant**: Erhalten Sie eine ausführliche Ausgabe mit dem `--debug`-Flag:
  ```bash
  vagrant up --debug
  ```

- **Puppet**: Führen Sie Puppet mit erhöhter Ausführlichkeit unter Verwendung der Flags `--verbose` oder `--debug` aus:
  ```bash
  puppet apply site.pp --verbose
  puppet apply site.pp --debug
  ```

- **Chef**: Aktivieren Sie die ausführliche Ausgabe mit dem `-l`-Flag (Log-Level):
  ```bash
  chef-client -l debug
  ```

- **SaltStack**: Erhöhen Sie die Ausführlichkeit mit dem `-l`-Flag (z.B. `debug` oder `trace`):
  ```bash
  salt '*' test.ping -l debug
  ```

- **PostgreSQL (psql)**: Um eine ausführliche Ausgabe von `psql` zu erhalten, verwenden Sie das Flag `-e`, um Abfragen auszugeben, oder `\set VERBOSITY verbose` für detaillierte Fehlermeldungen:
  ```bash
  psql -e -f script.sql
  ```
  Oder in `psql`:
  ```sql
  \set VERBOSITY verbose
  ```

- **MySQL**: Führen Sie den MySQL-Client mit ausführlicher Ausgabe unter Verwendung von `--verbose` aus:
  ```bash
  mysql --verbose < script.sql
  ```

- **SQLite**: Verwenden Sie den Befehl `.explain` für ausführliche Abfrageausführungspläne:
  ```sqlite
  sqlite3 database.db
  sqlite> .explain
  sqlite> SELECT * FROM table;
  ```

- **MongoDB**: Aktivieren Sie die ausführliche Protokollierung, indem Sie `mongod` mit dem `-v`-Flag starten (bis zu `-vvvvv` für mehr Details):
  ```bash
  mongod -v
  ```

- **Elasticsearch**: Starten Sie Elasticsearch mit ausführlicher Protokollierung, indem Sie die Datei `log4j2.properties` anpassen:
  ```properties
  logger.action.level = debug
  ```
  Oder übergeben Sie `--verbose` beim Start:
  ```bash
  elasticsearch --verbose
  ```

- **NGINX**: Testen Sie die Konfiguration mit ausführlicher Ausgabe unter Verwendung von `-T`:
  ```bash
  nginx -T
  ```
  Für Laufzeit-Ausführlichkeit erhöhen Sie die `error_log`-Stufe in der `nginx.conf`:
  ```nginx
  error_log /var/log/nginx/error.log debug;
  ```

- **Apache HTTP Server**: Aktivieren Sie die ausführliche Protokollierung, indem Sie die Direktive `LogLevel` in `httpd.conf` oder `apache2.conf` setzen:
  ```apache
  LogLevel debug
  ```

- **OpenSSL**: Erhalten Sie eine ausführliche Ausgabe mit Befehlen wie `s_client`:
  ```bash
  openssl s_client -connect example.com:443 -debug
  ```

- **JUnit (Java Testing)**: Führen Sie JUnit-Tests mit ausführlicher Ausgabe aus, indem Sie den Test-Runner konfigurieren (z.B. Maven Surefire Plugin):
  ```xml
  <configuration>
      <argLine>-verbose</argLine>
  </configuration>
  ```

Diese Beispiele decken eine breite Palette von Tools aus Programmiersprachen, Build-Systemen, Datenbanken, Servern und DevOps-Dienstprogrammen ab. Lassen Sie mich wissen, wenn Sie spezifischere Beispiele oder Details für ein bestimmtes Tool wünschen!