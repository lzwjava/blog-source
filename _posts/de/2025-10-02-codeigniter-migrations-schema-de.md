---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Migrationen Datenbankschemaverwaltung
translated: true
type: note
---

### Was sind CodeIgniter Migrations?

CodeIgniter (CI) Migrations sind eine Funktion, die hilft, Datenbank-Schemaänderungen auf eine versionskontrollierte Weise zu verwalten, ähnlich wie Tools wie Flyway oder Liquibase. Sie ermöglichen es Ihnen, PHP-Skripte zu schreiben, die Datenbankänderungen definieren (z.B. das Erstellen von Tabellen, Hinzufügen von Spalten oder Ändern von Daten), und diese dann der Reihe nach auszuführen, um Ihr Schema über verschiedene Umgebungen hinweg aktuell zu halten. Dies verhindert manuelle SQL-Fehler und unterstützt Rollbacks.

Migrations funktionieren, indem sie:
- Migrationsdateien in einem Verzeichnis speichern (Standard: `application/migrations/`).
- "Versionen" in einer Datenbanktabelle verfolgen, um zu wissen, welche Migrationen bereits angewendet wurden.
- Skripte vorwärts (up) oder rückwärts (down) ausführen, je nach Bedarf.

Die von Ihnen geteilte Konfigurationsdatei (`migration.php`) steuert das Verhalten von Migrationen. Sie verwendet PHP-Arrays, um Optionen festzulegen. Im Folgenden werde ich die wichtigsten Einstellungen mit Beispielen erläutern.

### Wichtige Konfigurationseinstellungen

| Einstellung | Wert in Ihrem Code | Erklärung | Funktionsweise |
|-------------|---------------------|-----------|----------------|
| `migration_enabled` | `FALSE` | Aktiviert oder deaktiviert Migrationen global. Wenn `FALSE`, können keine Migrationen ausgeführt werden (aus Sicherheitsgründen, da sie die DB ändern). | CI prüft dies, bevor ein Migrationsbefehl ausgeführt wird. Setzen Sie es während der Entwicklung auf `TRUE` und dann in der Produktion wieder auf `FALSE`. Beispiel: Wenn aktiviert, Ausführung via `$this->migration->current()` in einem Controller. |
| `migration_type` | `'timestamp'` | Dateinamensstil: `'sequential'` (z.B. `001_add_blog.php`) oder `'timestamp'` (z.B. `20121031104401_add_blog.php`). Timestamp wird für eine bessere Versionskontrolle empfohlen. | Dateien werden in chronologischer Reihenfolge geladen. Timestamp verwendet das Format `YYYYMMDDHHIISS` (z.B. `20121031104401` für 31. Okt. 2012, 10:44:01). |
| `migration_table` | `'migrations'` | Name der DB-Tabelle, die die angewendeten Migrationen verfolgt. Erforderlich. | CI erstellt diese Tabelle, falls sie nicht existiert. Sie speichert die neueste Migrationsversion. Das Löschen oder Aktualisieren dieser Tabelle setzt den Migrationsverlauf zurück. |
| `migration_auto_latest` | `FALSE` | Wenn `TRUE` und `migration_enabled` ist `TRUE`, werden Migrationen automatisch auf die neueste Version ausgeführt, wenn die Migrationsbibliothek geladen wird (z.B. beim Seitenaufruf). | Nützlich für Dev-Umgebungen, um Schemata automatisch zu synchronisieren. Setzen Sie es auf `FALSE`, um Migrationen manuell für mehr Kontrolle auszuführen (sicherer in der Prod). |
| `migration_version` | `0` | Die Zielversion/Nummer, auf die migriert werden soll. Auf den Dateinamen-Präfix setzen (z.B. `20121031104401`). `0` bedeutet, dass keine Migrationen angewendet wurden. | Das Ausführen von `$this->migration->version(20121031104401)` migriert bis zu diesem Punkt. Wird für gezielte Rollbacks verwendet – negative Zahlen führen ein Downgrade durch. |
| `migration_path` | `APPPATH.'migrations/'` | Verzeichnis, in dem die Migrationsdateien gespeichert sind. `APPPATH` ist eine CI-Konstante, die auf `application/` zeigt. | CI durchsucht diesen Ordner nach PHP-Dateien, die der Namenskonvention entsprechen. Muss vom Webserver beschreibbar sein. Benutzerdefinierte Pfade wie `BASEPATH.'custom/migrations/'` sind möglich. |

### Wie man Migrationen verwendet (Schritt für Schritt)

1. **Migrationen aktivieren**: Setzen Sie vorübergehend `$config['migration_enabled'] = TRUE;` in der Konfigurationsdatei.

2. **Eine Migrationsdatei erstellen**: Fügen Sie eine PHP-Datei in `application/migrations/` mit einem Namen wie `20121031104401_add_blog.php` hinzu. Verwenden Sie darin die Migration-Klasse von CI:
   ```php
   defined('BASEPATH') OR exit('No direct script access allowed');

   class Migration_Add_blog extends CI_Migration {
       public function up() {
           $this->dbforge->add_field('id');
           $this->dbforge->create_table('blogs');
       }

       public function down() {
           $this->dbforge->drop_table('blogs');
       }
   }
   ```
   - `up()` wendet Änderungen an (z.B. Tabelle erstellen).
   - `down()` macht sie rückgängig (z.B. Tabelle löschen).

3. **Migrationen ausführen**:
   - Bibliothek laden: `$this->load->library('migration');`
   - Auf die neueste Version: `$this->migration->current();`
   - Auf eine bestimmte Version: `$this->migration->version('20121031104401');`
   - Über die Kommandozeile (falls CLI aktiviert): `php index.php migrate current`

4. **Gängige Befehle**:
   - `$this->migration->latest()`: Alias für `current()`.
   - `$this->migration->find_migratables()`: Listet verfügbare Dateien auf.
   Fehler werden in den CI-Logdateien protokolliert oder werfen Exceptions.

5. **Beste Praktiken**:
   - Halten Sie Migrationen idempotent (sicher zum erneuten Ausführen).
   - Testen Sie zuerst in der Dev-Umgebung; vermeiden Sie die Aktivierung von Auto-Migrate in der Produktion, um versehentliche Schemaänderungen zu verhindern.
   - Verwenden Sie Transaktionen, falls Ihre DB sie für atomare Änderungen unterstützt.
   - Deaktivieren Sie sie nach der Verwendung: Setzen Sie sie aus Sicherheitsgründen wieder auf `FALSE`.

Wenn Sie auf Probleme stoßen (z.B. Berechtigungen für den Pfad), überprüfen Sie die Logs von CI oder die Dokumentation unter [codeigniter.com/user_guide/libraries/migration.html](https://codeigniter.com/user_guide/libraries/migration.html). Geben Sie Ihre CI-Version für maßgeschneiderte Ratschläge an!