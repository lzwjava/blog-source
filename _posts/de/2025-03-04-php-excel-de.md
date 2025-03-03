---
audio: false
generated: true
lang: de
layout: post
title: PHPExcel-Bibliothek
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung von "phpoffice/phpexcel": "^1.8" eine Installation über Composer und die Verwendung von PHP-Code zum Lesen und Schreiben von Excel-Dateien erforderlich ist.
- Die Forschung legt nahe, dass die Bibliothek veraltet ist, daher sollten neue Projekte PhpSpreadsheet in Betracht ziehen.
- Die Beweise deuten darauf hin, dass PHP-Erweiterungen wie mbstring, XML und XMLWriter erforderlich sind.

### Installation
Um loszulegen, fügen Sie `"phpoffice/phpexcel": "^1.8"` zu Ihrer `composer.json`-Datei hinzu und führen Sie `composer install` aus. Dies lädt die Bibliothek herunter, die für die Arbeit mit Excel-Dateien in PHP unerlässlich ist.

### Grundlegende Verwendung
Zum Schreiben in eine Excel-Datei:
- Inkludieren Sie die Bibliothek mit `require 'vendor/autoload.php';`.
- Erstellen Sie ein neues PHPExcel-Objekt: `$objPHPExcel = new PHPExcel();`.
- Legen Sie Zellwerte fest, z. B. `$sheet->setCellValue('A1', 'value');`.
- Speichern Sie die Datei mit einem Writer, wie `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` gefolgt von `$writer->save('filename.xlsx');`.

Zum Lesen aus einer Excel-Datei:
- Laden Sie die Datei mit `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');`.
- Greifen Sie auf Zellwerte zu, z. B. `$cellValue = $sheet->getCell('A1')->getValue();`.

### Unerwartetes Detail
Ein unerwarteter Aspekt ist, dass PHPExcel verschiedene Dateiformate wie .xls und .xlsx unterstützt und Dateitypen beim Lesen automatisch erkennen kann, was die Verwendung vereinfacht.

---

### Umfragehinweis: Umfassender Leitfaden zur Verwendung von "phpoffice/phpexcel": "^1.8"

Dieser Hinweis bietet eine detaillierte Untersuchung der Verwendung der PHPExcel-Bibliothek, insbesondere Version 1.8 oder höher, wie durch die Composer-Abhängigkeit "phpoffice/phpexcel": "^1.8" angegeben. Angesichts ihres Veraltungsstatus hebt dieser Leitfaden Überlegungen für moderne Alternativen hervor und stellt sicher, dass sowohl Anfänger als auch fortgeschrittene Benutzer ein umfassendes Verständnis haben. Der Inhalt ist so strukturiert, dass er Installation, Verwendung, Abhängigkeiten und zusätzlichen Kontext abdeckt, sodass alle relevanten Details aus der Forschung enthalten sind.

#### Hintergrund und Kontext
PHPExcel ist eine PHP-Bibliothek, die zum Lesen und Schreiben von Tabellenkalkulationsdateien, insbesondere Excel-Formaten wie .xls und .xlsx, entwickelt wurde. Die Versionsangabe "^1.8" gibt einen semantischen Versionsbereich an, was bedeutet, dass jede Version von 1.8 bis, aber nicht einschließlich, 2.0, was, angesichts der Geschichte der Bibliothek, auf Version 1.8.1 als die neueste, veröffentlicht im Jahr 2015, hinweist. Forschung zeigt jedoch, dass PHPExcel offiziell im Jahr 2017 veraltet und im Jahr 2019 archiviert wurde, mit der Empfehlung, auf seinen Nachfolger, PhpSpreadsheet, zu migrieren, aufgrund von fehlender Wartung und potenziellen Sicherheitsproblemen. Dieser Kontext ist für Benutzer wichtig, da er Vorsicht für neue Projekte nahelegt, obwohl der Leitfaden sich auf die Verwendung der angegebenen Version konzentriert, wie vom Benutzer angefordert.

Die Funktionalität der Bibliothek umfasst das Erstellen, Lesen und Manipulieren von Excel-Dateien und unterstützt Formate über Excel hinaus, wie CSV und HTML. Sie war Teil des PHPOffice-Projekts, das sich seitdem auf PhpSpreadsheet konzentriert, das verbesserte Funktionen und PHP-Standards-Konformität bietet. Angesichts des aktuellen Datums, 3. März 2025, und des Archivstatus der Bibliothek sollten Benutzer sich ihrer Einschränkungen bewusst sein, insbesondere bei neueren PHP-Versionen und Sicherheitsupdates.

#### Installationsprozess
Um "phpoffice/phpexcel": "^1.8" zu installieren, nutzt der Prozess Composer, den PHP-Abhängigkeitsmanager. Die Schritte sind wie folgt:
- Fügen Sie die Abhängigkeit zu Ihrer `composer.json`-Datei unter dem Abschnitt "require" hinzu: `"phpoffice/phpexcel": "^1.8"`.
- Führen Sie den Befehl `composer install` in Ihrem Projektverzeichnis aus. Dieser Befehl lädt die Bibliothek herunter und aktualisiert das `vendor`-Verzeichnis mit den erforderlichen Dateien.

Die Klammer (^) in Composer folgt der semantischen Versionskontrolle, die sicherstellt, dass Versionen 1.8, 1.8.1 oder alle Patch-Updates installiert werden, aber keine Versionen, die die Kompatibilität brechen (d. h. nicht 2.0 oder höher). Angesichts der letzten Veröffentlichung der Bibliothek, 1.8.1 im Jahr 2015, löst dies normalerweise Version 1.8.1 auf.

Forschung bestätigt, dass die Packagist-Seite für phpoffice/phpexcel sie als aufgegeben auflistet und stattdessen phpoffice/phpspreadsheet empfiehlt, aber sie bleibt für die Installation verfügbar, was mit der Anfrage des Benutzers übereinstimmt.

#### Grundlegende Verwendung: Schreiben in Excel
Nach der Installation umfasst die Verwendung von PHPExcel das Inkludieren der Autoload-Datei für das Klassenladen und dann die Nutzung seiner Klassen zur Manipulation von Tabellenkalkulationen. Hier ist eine detaillierte Aufschlüsselung:

- **Inkludieren der Autoload-Datei:** Beginnen Sie Ihr PHP-Skript mit `require 'vendor/autoload.php';`. Diese Zeile stellt sicher, dass alle Composer-installierten Bibliotheken, einschließlich PHPExcel, automatisch geladen werden, indem PSR-0-Autoloading gemäß der Struktur der Bibliothek aus dem Jahr 2015 genutzt wird.

- **Erstellen eines neuen PHPExcel-Objekts:** Initialisieren Sie eine neue Tabellenkalkulation mit `$objPHPExcel = new PHPExcel();`. Dieses Objekt stellt die gesamte Arbeitsmappe dar, die mehrere Blätter und Eigenschaften ermöglicht.

- **Arbeiten mit Blättern:** Greifen Sie auf das aktive Blatt zu, indem Sie `$sheet = $objPHPExcel->getSheet(0);` für das erste Blatt verwenden, oder erstellen Sie ein neues mit `$sheet = $objPHPExcel->createSheet();`. Blätter sind nullbasiert, sodass `getSheet(0)` das erste Blatt anvisiert.

- **Festlegen von Zellwerten:** Füllen Sie Zellen mit der Methode `setCellValue`, z. B. `$sheet->setCellValue('A1', 'Hello');`. Diese Methode nimmt eine Zellenreferenz (wie 'A1') und den einzufügenden Wert entgegen, der Text, Zahlen oder Formeln sein kann.

- **Speichern der Datei:** Um zu speichern, erstellen Sie einen Writer für das gewünschte Format. Für Excel 2007 und höher (.xlsx) verwenden Sie `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Dann speichern Sie mit `$writer->save('filename.xlsx');`. Andere Formate umfassen 'Excel5' für .xls (Excel 95) oder 'CSV' für kommagetrennte Werte.

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
- **Laden der Datei:** Verwenden Sie `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');`, um eine vorhandene Excel-Datei zu laden. Die IOFactory kann den Dateityp automatisch erkennen, aber Sie können einen Reader angeben, z. B. `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` für einen expliziten Typ.

- **Zugreifen auf Blätter und Zellen:** Nach dem Laden greifen Sie auf Blätter wie zuvor zu, z. B. `$sheet = $objPHPExcel->getSheet(0);`. Rufen Sie Zellwerte mit `$cellValue = $sheet->getCell('A1')->getValue();` ab, was den Inhalt der angegebenen Zelle zurückgibt.

Ein Beispiel zum Lesen:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Gibt "Hello" aus
```
Dies liest den Wert aus A1 und zeigt grundlegendes Abrufen.

#### Abhängigkeiten und Anforderungen
PHPExcel hat spezifische PHP-Anforderungen und Erweiterungen, die für den Betrieb erforderlich sind:
- **PHP-Version:** Erfordert PHP 5.2 oder 7.0 oder höher, wie aus den Packagist-Metadaten hervorgeht. Angesichts des aktuellen Datums, 3. März 2025, sollten die meisten modernen PHP-Installationen dies erfüllen, aber ältere Setups könnten Updates benötigen.
- **Erweiterungen:** Die Bibliothek hängt von `ext-mbstring`, `ext-XML` und `ext-XMLWriter` ab, die in Ihrer PHP-Konfiguration aktiviert sein müssen. Diese Erweiterungen handhaben die Zeichenkodierung, XML-Analyse und XML-Schreibung, die für Excel-Dateioperationen jeweils unerlässlich sind.

Benutzer sollten diese Erweiterungen mit `phpinfo()` oder durch Überprüfen der `php.ini`-Datei aktivieren, um sicherzustellen, dass keine Kompatibilitätsprobleme auftreten.

#### Zusätzliche Funktionen und Formate
Über das grundlegende Lesen/Schreiben hinaus unterstützt PHPExcel verschiedene Dateiformate, was ein unerwartetes Detail für Benutzer ist, die nur mit Excel vertraut sind. Die Bibliothek kann:
- Excel 2007 (.xlsx) über 'Excel2007' Writer/Reader.
- Excel 95 (.xls) über 'Excel5'.
- CSV-Dateien über 'CSV'.
- HTML über 'HTML'.

Beim Speichern geben Sie den Writer-Typ an; beim Lesen erkennt die IOFactory oft automatisch, aber explizite Reader können für Zuverlässigkeit verwendet werden. Zum Beispiel, um als .xls zu speichern:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
Diese Flexibilität ist für Legacy-Systeme oder spezifische Formatanforderungen nützlich, Benutzer sollten jedoch potenzielle formatbezogene Einschränkungen beachten, insbesondere bei älteren Excel-Versionen.

#### Veraltung und Migrationshinweise
Ein kritischer Punkt ist die Veraltung von PHPExcel. Forschung zeigt, dass es im Jahr 2019 archiviert wurde, mit der letzten Aktualisierung im Jahr 2015, und nicht mehr gewartet wird. Dies wirft Bedenken hinsichtlich Sicherheitslücken und Kompatibilität mit PHP-Versionen über 7.0 auf, insbesondere mit modernen Standards wie PHP 8.x. Sowohl das GitHub-Repository als auch die Packagist-Seite empfehlen die Migration zu PhpSpreadsheet, das Namespaces, PSR-Konformität und aktive Entwicklung bietet.

Für Benutzer bedeutet dies:
- Für bestehende Projekte, die PHPExcel 1.8 verwenden, setzen Sie mit Vorsicht fort, stellen Sie sicher, dass Sicherheits- und Kompatibilitätstests durchgeführt werden.
- Für neue Projekte, sollten Sie PhpSpreadsheet stark in Betracht ziehen, mit verfügbaren Migrationswerkzeugen, wie in der PhpSpreadsheet-Dokumentation ([Migration von PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)) angegeben.

Dieser Rat ist besonders relevant angesichts des aktuellen Datums, um sicherzustellen, dass Benutzer mit modernen, unterstützten Bibliotheken übereinstimmen.

#### Dokumentation und weiteres Lernen
Für eine tiefere Untersuchung ist die offizielle Dokumentation für PHPExcel in ihrem GitHub-Repository unter dem Dokumentationsordner verfügbar, obwohl der Zugriff möglicherweise das Herunterladen von Dateien wie der Entwicklerdokumentation DOC erfordert. Online-Tutorials wie das auf SitePoint ([Generate Excel Files and Charts with PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) bieten praktische Beispiele, die Diagramme und Formatierungen abdecken, die über die grundlegende Verwendung hinausgehen. Stack Overflow-Threads bieten ebenfalls Community-Einblicke, obwohl Vorsicht bei veralteten Antworten geboten ist, angesichts des Status der Bibliothek.

#### Vergleichstabelle: PHPExcel vs. PhpSpreadsheet
Um die Entscheidungsfindung zu unterstützen, hier eine Vergleichstabelle, die die wichtigsten Unterschiede hervorhebt, basierend auf der Forschung:

| Merkmal                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Letzte Aktualisierung    | 2015                              | Aktiv (Stand 2025)               |
| Namespaces               | Nein, Stammnamespace               | Ja, PSR-4-konform               |
| Wartungsstatus           | Veraltet, archiviert 2019         | Aktiv gewartet                   |
| PHP-Version-Unterstützung| Bis 7.0                           | PHP 7.4+                        |
| Dateiformat-Unterstützung| Excel, CSV, HTML, etc.            | Erweitert, einschließlich ODS, PDF|
| Leistung                 | Mäßig, speicherintensiv           | Optimiert, skalierbar             |

Diese Tabelle unterstreicht die Verschiebung zu PhpSpreadsheet für moderne Anforderungen, obwohl PHPExcel für Legacy-Zwecke weiterhin funktionsfähig bleibt.

#### Schlussfolgerung
Die Verwendung von "phpoffice/phpexcel": "^1.8" umfasst die Installation über Composer, die Nutzung seiner Klassen für Excel-Operationen und die Sicherstellung der erforderlichen PHP-Erweiterungen. Obwohl funktionsfähig, erfordert seine Veraltung Vorsicht, mit PhpSpreadsheet für zukünftige Projekte empfohlen. Dieser Leitfaden bietet einen umfassenden Ausgangspunkt mit Beispielen, Abhängigkeiten und zusätzlichen Ressourcen, die Benutzer weiter erkunden können.