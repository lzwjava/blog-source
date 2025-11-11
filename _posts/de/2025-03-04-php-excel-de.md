---
audio: false
generated: true
lang: de
layout: post
title: PHPExcel Bibliothek
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass man "phpoffice/phpexcel": "^1.8" über Composer installieren und PHP-Code verwenden muss, um Excel-Dateien zu lesen und zu schreiben.
- Recherchen deuten darauf hin, dass die Bibliothek veraltet ist, daher sollte man für neue Projekte die Verwendung von PhpSpreadsheet in Betracht ziehen.
- Die Hinweise sprechen dafür, dass PHP-Erweiterungen wie mbstring, XML und XMLWriter erforderlich sind.

### Installation
Um zu beginnen, fügen Sie `"phpoffice/phpexcel": "^1.8"` zu Ihrer `composer.json`-Datei hinzu und führen Sie `composer install` aus. Dies lädt die Bibliothek herunter, die für die Arbeit mit Excel-Dateien in PHP unerlässlich ist.

### Grundlegende Verwendung
Um in eine Excel-Datei zu schreiben:
- Binden Sie die Bibliothek mit `require 'vendor/autoload.php';` ein.
- Erstellen Sie ein neues PHPExcel-Objekt: `$objPHPExcel = new PHPExcel();`.
- Setzen Sie Zellenwerte, z.B. `$sheet->setCellValue('A1', 'value');`.
- Speichern Sie die Datei mit einem Writer, z.B. `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` gefolgt von `$writer->save('filename.xlsx');`.

Um aus einer Excel-Datei zu lesen:
- Laden Sie die Datei mit `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');`.
- Greifen Sie auf Zellenwerte zu, z.B. `$cellValue = $sheet->getCell('A1')->getValue();`.

### Unerwartetes Detail
Ein unerwarteter Aspekt ist, dass PHPExcel verschiedene Dateiformate wie .xls und .xlsx unterstützt und beim Lesen Dateitypen automatisch erkennen kann, was die Verwendung vereinfacht.

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von "phpoffice/phpexcel": "^1.8"

Diese Notiz bietet eine detaillierte Erkundung der Verwendung der PHPExcel-Bibliothek, speziell Version 1.8 oder höher, wie durch die Composer-Abhängigkeit "phpoffice/phpexcel": "^1.8" angegeben. Angesichts ihres Veraltungsstatus hebt dieser Leitfaden auch Überlegungen zu modernen Alternativen hervor und stellt ein gründliches Verständnis sowohl für Anfänger als auch für fortgeschrittene Benutzer sicher. Der Inhalt ist so strukturiert, dass er Installation, Verwendung, Abhängigkeiten und zusätzlichen Kontext abdeckt, um sicherzustellen, dass alle relevanten Details aus der Recherche enthalten sind.

#### Hintergrund und Kontext
PHPExcel ist eine PHP-Bibliothek, die zum Lesen und Schreiben von Tabellenkalkulationsdateien, insbesondere Excel-Formaten wie .xls und .xlsx, entwickelt wurde. Die Versionsangabe "^1.8" zeigt einen semantischen Versionsbereich an, was bedeutet, dass jede Version von 1.8 bis zu, aber nicht einschließlich, 2.0 verwendet wird. Angesichts der Geschichte der Bibliothek weist dies auf Version 1.8.1 als die letzte, 2015 veröffentlichte Version hin. Recherchen zeigen jedoch, dass PHPExcel 2017 offiziell als veraltet markiert und 2019 archiviert wurde, mit der Empfehlung, aufgrund fehlender Wartung und möglicher Sicherheitsprobleme zu seinem Nachfolger PhpSpreadsheet zu migrieren. Dieser Kontext ist für Benutzer entscheidend, da er zur Vorsicht bei neuen Projekten rät, obwohl sich der Leitfaden auf die Verwendung der angeforderten Version konzentriert.

Die Funktionalität der Bibliothek umfasst das Erstellen, Lesen und Bearbeiten von Excel-Dateien und unterstützt Formate über Excel hinaus, wie z.B. CSV und HTML. Sie war Teil des PHPOffice-Projekts, das seinen Fokus seitdem auf PhpSpreadsheet verlagert hat, das verbesserte Funktionen und PHP-Standardkonformität bietet. Angesichts des aktuellen Datums, dem 3. März 2025, und des Archivierungsstatus der Bibliothek sollten Benutzer sich ihrer Einschränkungen bewusst sein, insbesondere bei neueren PHP-Versionen und Sicherheitsupdates.

#### Installationsprozess
Um "phpoffice/phpexcel": "^1.8" zu installieren, nutzt der Prozess Composer, den PHP-Abhängigkeitsmanager. Die Schritte sind wie folgt:
- Fügen Sie die Abhängigkeit Ihrer `composer.json`-Datei im Abschnitt "require" hinzu: `"phpoffice/phpexcel": "^1.8"`.
- Führen Sie den Befehl `composer install` in Ihrem Projektverzeichnis aus. Dieser Befehl lädt die Bibliothek herunter und aktualisiert das `vendor`-Verzeichnis mit den notwendigen Dateien.

Die Caret (^)-Notation in Composer folgt dem semantischen Versioning und stellt sicher, dass Versionen 1.8, 1.8.1 oder alle Patch-Updates installiert werden, aber keine Versionen, die die Kompatibilität brechen würden (d.h. nicht 2.0 oder höher). Da die letzte Veröffentlichung der Bibliothek 2015 Version 1.8.1 war, wird dies typischerweise auf Version 1.8.1 aufgelöst.

Recherchen bestätigen, dass die Packagist-Seite für phpoffice/phpexcel sie als aufgegeben auflistet und stattdessen phpoffice/phpspreadsheet vorschlägt, aber sie bleibt für die Installation verfügbar, was der Benutzeranfrage entspricht.

#### Grundlegende Verwendung: Schreiben in Excel
Nach der Installation beinhaltet die Verwendung von PHPExcel das Einbinden der Autoload-Datei zum Laden von Klassen und dann die Nutzung ihrer Klassen zur Tabellenbearbeitung. Hier ist eine detaillierte Aufschlüsselung:

- **Autoload-Datei einbinden:** Beginnen Sie Ihr PHP-Skript mit `require 'vendor/autoload.php';`. Diese Zeile stellt sicher, dass alle von Composer installierten Bibliotheken, einschließlich PHPExcel, automatisch geladen werden, unter Nutzung von PSR-0-Autoloading gemäß der Struktur der Bibliothek von 2015.

- **Neues PHPExcel-Objekt erstellen:** Initialisieren Sie eine neue Tabelle mit `$objPHPExcel = new PHPExcel();`. Dieses Objekt repräsentiert die gesamte Arbeitsmappe und ermöglicht mehrere Blätter und Eigenschaften.

- **Mit Blättern arbeiten:** Greifen Sie auf das aktive Blatt mit `$sheet = $objPHPExcel->getSheet(0);` für das erste Blatt zu oder erstellen Sie ein neues mit `$sheet = $objPHPExcel->createSheet();`. Blätter sind nullbasiert indiziert, also zielt `getSheet(0)` auf das erste Blatt.

- **Zellenwerte setzen:** Füllen Sie Zellen mit der Methode `setCellValue`, z.B. `$sheet->setCellValue('A1', 'Hello');`. Diese Methode nimmt eine Zellreferenz (wie 'A1') und den einzufügenden Wert, der Text, Zahlen oder Formeln sein kann.

- **Datei speichern:** Um zu speichern, erstellen Sie einen Writer für das gewünschte Format. Für Excel 2007 und höher (.xlsx) verwenden Sie `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Dann speichern Sie mit `$writer->save('filename.xlsx');`. Andere Formate sind 'Excel5' für .xls (Excel 95) oder 'CSV' für kommagetrennte Werte.

Ein Beispielskript zum Schreiben könnte so aussehen:
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
Dies erstellt eine einfache Excel-Datei mit "Hello" in A1 und "World" in B1.

#### Grundlegende Verwendung: Lesen aus Excel
Das Lesen aus einer Excel-Datei folgt einem ähnlichen Muster, beginnt aber mit dem Laden der Datei:
- **Datei laden:** Verwenden Sie `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` um eine vorhandene Excel-Datei zu laden. Die IOFactory kann den Dateityp automatisch erkennen, aber Sie können einen Reader explizit angeben, z.B. `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` für expliziten Typ.

- **Auf Blätter und Zellen zugreifen:** Nach dem Laden greifen Sie wie zuvor auf Blätter zu, z.B. `$sheet = $objPHPExcel->getSheet(0);`. Rufen Sie Zellenwerte mit `$cellValue = $sheet->getCell('A1')->getValue();` ab, was den Inhalt der angegebenen Zelle zurückgibt.

Ein Beispiel zum Lesen:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Gibt "Hello" aus
```
Dies liest den Wert aus A1 und demonstriert die grundlegende Abfrage.

#### Abhängigkeiten und Anforderungen
PHPExcel hat spezifische PHP-Anforderungen und Erweiterungen, die für den Betrieb benötigt werden:
- **PHP-Version:** Erfordert PHP 5.2 oder 7.0 oder höher, gemäß den Packagist-Metadaten. Angesichts des aktuellen Datums, dem 3. März 2025, sollten die meisten modernen PHP-Installationen dies erfüllen, aber ältere Setups benötigen möglicherweise Updates.
- **Erweiterungen:** Die Bibliothek hängt von `ext-mbstring`, `ext-XML` und `ext-XMLWriter` ab, die in Ihrer PHP-Konfiguration aktiviert sein müssen. Diese Erweiterungen handhaben Zeichenkodierung, XML-Parsing bzw. XML-Schreiben und sind für Excel-Dateioperationen unerlässlich.

Benutzer sollten überprüfen, ob diese Erweiterungen mit `phpinfo()` aktiv sind oder die `php.ini`-Datei prüfen, um sicherzustellen, dass keine Kompatibilitätsprobleme auftreten.

#### Zusätzliche Funktionen und Formate
Über grundlegendes Lesen/Schreiben hinaus unterstützt PHPExcel verschiedene Dateiformate, was ein unerwartetes Detail für Benutzer ist, die nur mit Excel vertraut sind. Die Bibliothek kann handhaben:
- Excel 2007 (.xlsx) über 'Excel2007' Writer/Reader.
- Excel 95 (.xls) über 'Excel5'.
- CSV-Dateien über 'CSV'.
- HTML über 'HTML'.

Beim Speichern geben Sie den Writer-Typ an; beim Lesen erkennt IOFactory oft automatisch, aber explizite Reader können für Zuverlässigkeit verwendet werden. Zum Beispiel, um als .xls zu speichern:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
Diese Flexibilität ist nützlich für Legacy-Systeme oder spezifische Formatbedürfnisse, obwohl Benutzer potenzielle formatspezifische Einschränkungen beachten sollten, besonders bei älteren Excel-Versionen.

#### Veraltung und Migrationsempfehlung
Ein kritischer Punkt ist die Veraltung von PHPExcel. Recherchen zeigen, dass es 2019 archiviert wurde, das letzte Update 2015 war und es nicht mehr gewartet wird. Dies wirft Bedenken bezüglich Sicherheitslücken und Kompatibilität mit PHP-Versionen über 7.0 hinaus auf, insbesondere mit modernen Standards wie PHP 8.x. Das GitHub-Repository und die Packagist-Seite empfehlen beide die Migration zu PhpSpreadsheet, das Namespaces, PSR-Konformität und aktive Entwicklung bietet.

Für Benutzer bedeutet dies:
- Für bestehende Projekte, die PHPExcel 1.8 verwenden, fahren Sie mit Vorsicht fort und stellen Sie Tests auf Sicherheit und Kompatibilität sicher.
- Für neue Projekte ziehen Sie stark PhpSpreadsheet in Betracht, mit verfügbaren Migrationswerkzeugen, wie in der PhpSpreadsheet-Dokumentation ([Migration from PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)) vermerkt.

Diese Empfehlung ist besonders angesichts des aktuellen Datums relevant, um sicherzustellen, dass Benutzer sich an moderne, unterstützte Bibliotheken halten.

#### Dokumentation und Weiteres Lernen
Für tiefergehende Erkundungen ist die offizielle Dokumentation für PHPExcel in ihrem GitHub-Repository unter dem Documentation-Ordner verfügbar, obwohl der Zugriff das Herunterladen von Dateien wie der Entwicklerdokumentation DOC erfordern kann. Online bieten Tutorials wie das auf SitePoint ([Generate Excel Files and Charts with PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) praktische Beispiele, die über die grundlegende Verwendung hinausgehen und Diagramme und Formatierung abdecken. Stack-Overflow-Diskussionen bieten ebenfalls Community-Einblicke, obwohl bei veralteten Antworten aufgrund des Status der Bibliothek Vorsicht geboten ist.

#### Vergleichstabelle: PHPExcel vs. PhpSpreadsheet
Um die Entscheidungsfindung zu unterstützen, hier eine Vergleichstabelle, die auf Recherchen basierende Hauptunterschiede hervorhebt:

| Merkmal                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Letztes Update           | 2015                              | Aktiv (Stand 2025)              |
| Namespaces               | Nein, Root-Namespace              | Ja, PSR-4 konform               |
| Wartungsstatus           | Veraltet, archiviert 2019         | Aktiv gewartet                  |
| PHP-Version-Unterstützung| Bis 7.0                           | PHP 7.4+                        |
| Dateiformat-Unterstützung| Excel, CSV, HTML, etc.            | Erweitert, inkl. ODS, PDF       |
| Leistung                 | Mäßig, speicherintensiv           | Optimiert, skalierbar           |

Diese Tabelle unterstreicht den Wechsel zu PhpSpreadsheet für moderne Anforderungen, obwohl PHPExcel für Legacy-Zwecke funktional bleibt.

#### Fazit
Die Verwendung von "phpoffice/phpexcel": "^1.8" beinhaltet die Installation über Composer, die Nutzung seiner Klassen für Excel-Operationen und das Sicherstellen der erforderlichen PHP-Erweiterungen. Obwohl funktional, erfordert ihre Veraltung Vorsicht, wobei PhpSpreadsheet für zukünftige Projekte empfohlen wird. Dieser Leitfaden bietet einen umfassenden Ausgangspunkt mit Beispielen, Abhängigkeiten und zusätzlichen Ressourcen für Benutzer zur weiteren Erkundung.

### Wichtige Zitate
- [Packagist phpoffice/phpexcel Seite mit Installationsdetails](https://packagist.org/packages/phpoffice/phpexcel)
- [SitePoint Tutorial zum Generieren von Excel-Dateien mit PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [PHPExcel GitHub Repository Archivierungsstatus](https://github.com/PHPOffice/PHPExcel)
- [PhpSpreadsheet Migrationsleitfaden von PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)