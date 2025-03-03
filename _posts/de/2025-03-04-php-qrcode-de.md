---
audio: false
generated: true
lang: de
layout: post
title: PHP-Tool zur Erstellung von QR-Codes
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung von "endroid/qr-code" Version 2.2.2 eine Installation über Composer erforderlich ist und sichergestellt werden muss, dass die GD-Erweiterung aktiviert ist.
- Die Forschung deutet darauf hin, dass QR-Codes mit der Builder-Klasse erstellt werden können, indem Parameter wie Daten, Größe und Writer festgelegt und das Ergebnis gespeichert oder ausgegeben wird.
- Die Beweise deuten darauf hin, dass die Bibliothek PNG, SVG und andere Formate unterstützt, mit Optionen für Logos und Beschriftungen, aber dies sollte für Version 2.2.2 überprüft werden.

### Installation
Zuerst installieren Sie die Bibliothek mit Composer mit dem Befehl:
```
composer require endroid/qr-code:2.2.2
```
Stellen Sie sicher, dass Ihre PHP-Konfiguration die GD-Erweiterung aktiviert hat, da diese für die Bildgenerierung erforderlich ist.

### Beispiel für die Verwendung
Hier ist ein einfaches Beispiel mit der Builder-Klasse, das wahrscheinlich mit Version 2.2.2 kompatibel ist:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Dies erstellt einen QR-Code für eine URL und speichert ihn als PNG-Datei. Sie können ihn auch als Data-URI für die Webanzeige ausgeben.

### Zusätzliche Hinweise
Die Bibliothek unterstützt verschiedene Writer (z. B. PNG, SVG) und ermöglicht Anpassungen wie das Hinzufügen von Logos oder Beschriftungen. Da Version 2.2.2 jedoch älter ist, könnten einige Funktionen in der aktuellen Dokumentation (wie erweiterte Logo-Optionen) nicht verfügbar sein. Überprüfen Sie daher die Dokumentation für diese spezifische Version auf [GitHub](https://github.com/endroid/qr-code).

---

### Umfragehinweis: Detaillierte Anleitung zur Verwendung von "endroid/qr-code" Version 2.2.2

Dieser Hinweis bietet eine umfassende Anleitung zur Verwendung der "endroid/qr-code"-Bibliothek, Version 2.2.2, zur Erstellung von QR-Codes in PHP-Anwendungen. Er erweitert die direkte Antwort, indem alle relevanten Details aus der Forschung einbezogen werden, um Entwicklern, insbesondere denen, die neu in der Bibliothek sind, ein umfassendes Verständnis zu vermitteln. Der Inhalt ist so strukturiert, dass er einem professionellen Artikel ähnelt, mit Tabellen für Klarheit und Inline-URLs für weitere Referenzen.

#### Einführung
Die "endroid/qr-code"-Bibliothek ist ein PHP-Tool zur Erstellung von QR-Codes, das weit verbreitet für Anwendungen wie Produktverfolgung, Dokumentenmanagement und Marketing verwendet wird. Version 2.2.2, die in der Abfrage angegeben ist, ist eine ältere Version, und obwohl die Bibliothek auf [Packagist](https://packagist.org/packages/endroid/qr-code) als aufgegeben gekennzeichnet ist, bleibt sie für die grundlegende QR-Code-Erstellung funktionsfähig. Diese Anleitung beschreibt die Installation und Verwendung, mit einem Fokus auf die Sicherstellung der Kompatibilität mit Version 2.2.2 und der Berücksichtigung möglicher Unterschiede zu neueren Versionen.

#### Installationsprozess
Zunächst müssen Sie die Bibliothek über Composer, den PHP-Paketmanager, installieren. Der Befehl lautet:
```
composer require endroid/qr-code:2.2.2
```
Dies stellt sicher, dass Sie genau Version 2.2.2 erhalten. Eine kritische Anforderung ist die GD-Erweiterung für PHP, die aktiviert und konfiguriert sein muss, da sie für die Bildgenerierung unerlässlich ist. Ohne diese kann die Bibliothek keine visuellen QR-Codes erstellen.

| Schritt                  | Details                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Installationsbefehl    | `composer require endroid/qr-code:2.2.2`                                |
| PHP-Anforderung       | Stellen Sie sicher, dass die GD-Erweiterung aktiviert ist (überprüfen Sie `phpinfo()` zur Bestätigung)     |

Die Forschung zeigt, dass die GitHub-Repository ([GitHub](https://github.com/endroid/qr-code)) und die [Packagist](https://packagist.org/packages/endroid/qr-code)-Seiten diese Installationsmethode bestätigen, wobei keine spezifische Dokumentation für Version 2.2.2 gefunden wurde, was auf die Abhängigkeit von allgemeinen Nutzungsmustern hinweist.

#### Nutzungsdetails
Die Bibliothek bietet zwei Hauptmethoden zur QR-Code-Erstellung: die Verwendung der Builder-Klasse oder direkt mit der QrCode-Klasse. Da sich die Abfrage auf die Nutzung konzentriert, wird der Builder-Ansatz aufgrund seiner Einfachheit empfohlen, obwohl beide hier zur Vollständigkeit beschrieben werden.

##### Verwendung der Builder-Klasse
Die Builder-Klasse bietet eine flüssige Schnittstelle zur Konfiguration von QR-Codes. Basierend auf Beispielen aus der aktuellen Dokumentation ist eine grundlegende Implementierung:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Dieser Code erstellt einen QR-Code für die URL im PNG-Format mit ISO-8859-1-Kodierung für eine bessere Scannerkompatibilität und eine hohe Fehlerkorrektur. Sie können ihn auch als Data-URI ausgeben:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Dies ist nützlich zum Einbetten in HTML, z. B. `<img src="<?php echo $qrCodeDataUri; ?>">`.

Da Version 2.2.2 jedoch älter ist, könnten einige Klassen wie `ErrorCorrectionLevelHigh` anders benannt sein (z. B. `ErrorCorrectionLevel::HIGH` in älteren Versionen). Forschung aus Stack Overflow-Posts ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) deutet darauf hin, dass ältere Versionen Methoden wie `setErrorCorrection('high')` verwendet haben, daher überprüfen Sie die API für 2.2.2.

##### Direkte Verwendung der QrCode-Klasse
Für mehr Kontrolle können Sie die QrCode-Klasse verwenden, wie in Beispielen zu sehen:
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
Diese Methode ist ausführlicher, ermöglicht jedoch eine feinere Abstimmung, wie das Festlegen von Vorder- und Hintergrundfarben, was für Version 2.2.2 relevant sein könnte. Überprüfen Sie auch hier die Dokumentation auf die Verfügbarkeit der Methoden.

#### Konfigurationsoptionen
Die Bibliothek unterstützt verschiedene Writer für unterschiedliche Ausgabeformate, wie in der folgenden Tabelle basierend auf der aktuellen Dokumentation, mit einem Hinweis zur Überprüfung für Version 2.2.2:

| Writer-Klasse          | Format   | Hinweise                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Komprimierungsstufe konfigurierbar, Standard -1                           |
| SvgWriter             | SVG      | Geeignet für Vektorgrafiken, keine Komprimierungsoptionen                 |
| WebPWriter            | WebP     | Qualität 0-100, Standard 80, gut für Webnutzung                          |
| PdfWriter             | PDF      | Einheit in mm, Standard, gut für Druck                                 |

Kodierungsoptionen umfassen UTF-8 (Standard) und ISO-8859-1, wobei Letzteres für die Kompatibilität mit Barcode-Scannern empfohlen wird. Runde Blockgrößenmodi (Rand, vergrößern, verkleinern, keine) können die Lesbarkeit verbessern, aber ihre Verfügbarkeit in 2.2.2 muss bestätigt werden.

#### Fortgeschrittene Funktionen und Überlegungen
Für fortgeschrittene Anwendungen, wie das Einbetten von Logos, unterstützt die Builder-Klasse Methoden wie `logoPath()` und `logoResizeToWidth()`, wie in einem Medium-Artikel ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)) zu sehen. Diese könnten jedoch Ergänzungen nach 2.2.2 sein, daher testen Sie die Kompatibilität. Die Validierung erzeugter QR-Codes ist möglich, beeinträchtigt jedoch die Leistung und ist standardmäßig deaktiviert, ein Detail von [GitHub](https://github.com/endroid/qr-code).

Angesichts der Hinweise auf die Aufgabe der Bibliothek auf [Packagist](https://packagist.org/packages/endroid/qr-code) ist es wert, potenzielle Sicherheits- oder Wartungsprobleme zu beachten, obwohl sie für die grundlegende Nutzung weiterhin funktionsfähig ist. Für Symfony-Nutzer gibt es ein Bundle ([GitHub](https://github.com/endroid/qr-code-bundle)), das jedoch außerhalb der allgemeinen PHP-Nutzung liegt.

#### Versionsspezifische Hinweise
Die Forschung zeigte keine direkte Dokumentation für Version 2.2.2, wobei die GitHub-Tags diese Version nicht auflisten, was auf eine ältere Version oder einen Tippfehler hinweist. Das aktuelle Repository zeigt Versionen bis 6.0.0, und [Packagist](https://packagist.org/packages/endroid/qr-code) listet es als aufgegeben auf, empfiehlt jedoch endroid/qr-code, was verwirrend ist, da es sich um dasselbe Paket handelt. Dies deutet auf mögliche Umbenennungen oder Versionsprobleme hin, daher sollten Benutzer Abhängigkeiten sperren und Upgrades testen.

#### Schlussfolgerung
Die Verwendung von "endroid/qr-code" Version 2.2.2 umfasst die Installation über Composer, die Sicherstellung der GD-Erweiterung und die Erstellung von QR-Codes mit der Builder- oder QrCode-Klasse. Während die Beispiele auf der aktuellen Dokumentation basieren, überprüfen Sie die API-Unterschiede für 2.2.2, insbesondere für fortgeschrittene Funktionen. Für weitere Details konsultieren Sie die GitHub-Seite der Bibliothek und verwandte Stack Overflow-Diskussionen.

#### Wichtige Zitate
- [QR-Code-Generator GitHub-Repository](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist-Seite](https://packagist.org/packages/endroid/qr-code)
- [Medium-Artikel zur Erstellung von QR-Codes mit eingebetteten Bildern](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR-Code Stack Overflow-Diskussion](https://stackoverflow.com/questions/40777377/endroid-qr-code)