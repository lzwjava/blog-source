---
audio: false
generated: true
lang: de
layout: post
title: PHP-Werkzeug zur Erstellung von QR-Codes
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie "endroid/qr-code" Version 2.2.2 über Composer installieren und sicherstellen müssen, dass die GD-Erweiterung aktiviert ist.
- Recherchen deuten darauf hin, dass Sie QR-Codes mit der Builder-Klasse generieren können, indem Sie Parameter wie Daten, Größe und Writer festlegen und dann das Ergebnis speichern oder ausgeben.
- Die Beweislage tendiert dazu, dass die Bibliothek PNG, SVG und andere Formate unterstützt, mit Optionen für Logos und Beschriftungen, aber überprüfen Sie dies für Version 2.2.2.

### Installation
Installieren Sie zunächst die Bibliothek mit Composer über den Befehl:
```
composer require endroid/qr-code:2.2.2
```
Stellen Sie sicher, dass Ihre PHP-Installation die GD-Erweiterung aktiviert hat, da diese für die Bildgenerierung erforderlich ist.

### Verwendungsbeispiel
Hier ist ein grundlegendes Beispiel mit der Builder-Klasse, das wahrscheinlich mit Version 2.2.2 kompatibel ist:
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
Die Bibliothek unterstützt verschiedene Writer (z.B. PNG, SVG) und ermöglicht Anpassungen wie das Hinzufügen von Logos oder Beschriftungen. Da es sich bei Version 2.2.2 jedoch um eine ältere Version handelt, sind einige Funktionen in der aktuellen Dokumentation (wie erweiterte Logo-Optionen) möglicherweise nicht verfügbar. Überprüfen Sie daher die Dokumentation für diese spezifische Version auf [GitHub](https://github.com/endroid/qr-code).

---

### Umfragehinweis: Detaillierte Anleitung zur Verwendung von "endroid/qr-code" Version 2.2.2

Dieser Hinweis bietet eine umfassende Anleitung zur Verwendung der "endroid/qr-code"-Bibliothek, Version 2.2.2, zur Generierung von QR-Codes in PHP-Anwendungen. Er erweitert die direkte Antwort, indem alle relevanten Details aus der Recherche einbezogen werden, um ein gründliches Verständnis für Entwickler, insbesondere für diejenigen, die mit der Bibliothek neu sind, zu gewährleisten. Der Inhalt ist so strukturiert, dass er einen professionellen Artikel nachahmt, mit Tabellen zur Klarheit und inline URLs für weitere Referenzen.

#### Einführung
Die "endroid/qr-code"-Bibliothek ist ein PHP-Tool zur Generierung von QR-Codes, das häufig für Anwendungen wie Produktverfolgung, Dokumentenmanagement und Marketing verwendet wird. Version 2.2.2, wie in der Anfrage angegeben, ist eine ältere Version, und obwohl die Bibliothek auf [Packagist](https://packagist.org/packages/endroid/qr-code) als eingestellt vermerkt ist, bleibt sie für die grundlegende QR-Code-Generierung funktionsfähig. Diese Anleitung beschreibt die Installation und Verwendung mit Schwerpunkt auf der Kompatibilität mit Version 2.2.2 unter Anerkennung potenzieller Unterschiede zu neueren Versionen.

#### Installationsprozess
Um zu beginnen, müssen Sie die Bibliothek über Composer, den PHP-Paketmanager, installieren. Der Befehl lautet:
```
composer require endroid/qr-code:2.2.2
```
Dies stellt sicher, dass Sie genau Version 2.2.2 erhalten. Eine kritische Voraussetzung ist die GD-Erweiterung für PHP, die aktiviert und konfiguriert sein muss, da sie für die Bildgenerierung unerlässlich ist. Ohne sie kann die Bibliothek keine visuellen QR-Codes erzeugen.

| Schritt               | Details                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Installationsbefehl   | `composer require endroid/qr-code:2.2.2`                                |
| PHP-Anforderung       | Sicherstellen, dass die GD-Erweiterung aktiviert ist (zur Bestätigung `phpinfo()` prüfen) |

Recherchen zeigen, dass die GitHub-Repository der Bibliothek ([GitHub](https://github.com/endroid/qr-code)) und [Packagist](https://packagist.org/packages/endroid/qr-code)-Seiten diese Installationsmethode bestätigen, wobei keine spezifische Dokumentation für Version 2.2.2 gefunden wurde, was auf die Abhängigkeit von allgemeinen Verwendungsmustern hindeutet.

#### Verwendungsdetails
Die Bibliothek bietet zwei primäre Methoden zur QR-Code-Generierung: Verwendung der Builder-Klasse oder direkt mit der QrCode-Klasse. Angesichts des Fokus der Anfrage auf die Verwendung wird der Builder-Ansatz aufgrund seiner Einfachheit empfohlen, obwohl beide hier der Vollständigkeit halber detailliert beschrieben werden.

##### Verwendung der Builder-Klasse
Die Builder-Klasse bietet eine fließende Schnittstelle zur Konfiguration von QR-Codes. Basierend auf Beispielen aus der aktuellen Dokumentation sieht eine grundlegende Implementierung so aus:
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
Dieser Code erstellt einen QR-Code für die URL im PNG-Format, mit ISO-8859-1-Kodierung für eine bessere Scanner-Kompatibilität und hoher Fehlerkorrektur. Sie können ihn auch als Data-URI ausgeben:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Dies ist nützlich für die Einbettung in HTML, z.B. `<img src="<?php echo $qrCodeDataUri; ?>">`.

Aufgrund des Alters von Version 2.2.2 könnten einige Klassen wie `ErrorCorrectionLevelHigh` jedoch anders benannt sein (z.B. `ErrorCorrectionLevel::HIGH` in älteren Versionen). Recherchen in Stack Overflow-Beiträgen ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) deuten darauf hin, dass ältere Versionen Methoden wie `setErrorCorrection('high')` verwendeten, daher sollte die API für 2.2.2 überprüft werden.

##### Direkte Verwendung der QrCode-Klasse
Für mehr Kontrolle können Sie die QrCode-Klasse direkt verwenden, wie in Beispielen zu sehen:
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
Diese Methode ist ausführlicher, ermöglicht jedoch Feinabstimmungen, wie das Festlegen von Vorder- und Hintergrundfarben, was für Version 2.2.2 relevant sein könnte. Überprüfen Sie auch hier die Verfügbarkeit der Methoden.

#### Konfigurationsoptionen
Die Bibliothek unterstützt verschiedene Writer für verschiedene Ausgabeformate, wie in der folgenden Tabelle detailliert, basierend auf der aktuellen Dokumentation, mit einem Hinweis zur Überprüfung für Version 2.2.2:

| Writer-Klasse         | Format   | Hinweise                                                              |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Komprimierungsstufe konfigurierbar, Standard -1                      |
| SvgWriter             | SVG      | Geeignet für Vektorgrafiken, keine Komprimierungsoptionen           |
| WebPWriter            | WebP     | Qualität 0-100, Standard 80, gut für Webnutzung                     |
| PdfWriter             | PDF      | Einheit in mm, Standard, gut für Druck                              |

Kodierungsoptionen umfassen UTF-8 (Standard) und ISO-8859-1, wobei letzteres für die Barcode-Scanner-Kompatibilität empfohlen wird. Runde Blockgrößen-Modi (margin, enlarge, shrink, none) können die Lesbarkeit verbessern, aber ihre Verfügbarkeit in 2.2.2 muss bestätigt werden.

#### Erweiterte Funktionen und Überlegungen
Für erweiterte Verwendungen, wie das Einbetten von Logos, unterstützt die Builder-Klasse Methoden wie `logoPath()` und `logoResizeToWidth()`, wie in einem Medium-Artikel ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)) zu sehen. Diese könnten jedoch nachträgliche Ergänzungen nach 2.2.2 sein, daher sollte die Kompatibilität getestet werden. Die Validierung generierter QR-Codes ist möglich, beeinträchtigt jedoch die Leistung und ist standardmäßig deaktiviert, ein Detail von [GitHub](https://github.com/endroid/qr-code).

Angesichts des Vermerks "eingestellt" auf [Packagist](https://packagist.org/packages/endroid/qr-code) sind potenzielle Sicherheits- oder Wartungsbedenken zu beachten, obwohl die Bibliothek für die grundlegende Nutzung weiterhin brauchbar bleibt. Für Symfony-Benutzer gibt es ein Bundle ([GitHub](https://github.com/endroid/qr-code-bundle)), das jedoch außerhalb der allgemeinen PHP-Nutzung liegt.

#### Versionsspezifische Hinweise
Recherchen zeigten keine direkte Dokumentation für Version 2.2.2, wobei GitHub-Tags diese nicht auflisten, was darauf hindeutet, dass es sich um eine ältere Version oder einen Tippfehler handeln könnte. Die aktuelle Repository zeigt Versionen bis 6.0.0, und [Packagist](https://packagist.org/packages/endroid/qr-code) listet sie als eingestellt und empfiehlt endroid/qr-code, was verwirrend ist, da es sich um dasselbe Paket handelt. Dies deutet auf potenzielle Umbenennungs- oder Versionsprobleme hin, daher sollten Benutzer Abhängigkeiten sperren und Upgrades testen.

#### Schlussfolgerung
Die Verwendung von "endroid/qr-code" Version 2.2.2 umfasst die Installation über Composer, Sicherstellung der GD-Erweiterung und Generierung von QR-Codes mit der Builder- oder QrCode-Klasse. Während die Beispiele auf der aktuellen Dokumentation basieren, sollten API-Unterschiede für 2.2.2 überprüft werden, insbesondere für erweiterte Funktionen. Für weitere Details konsultieren Sie die GitHub-Seite der Bibliothek und verwandte Stack Overflow-Diskussionen.

#### Wichtige Zitate
- [QR Code Generator GitHub Repository](https://github.com/endroid/qr-code)
- [endroid/qr-code Packagist-Seite](https://packagist.org/packages/endroid/qr-code)
- [Medium-Artikel über das Erstellen von QR-Codes mit eingebetteten Bildern](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Endroid QR Code Stack Overflow-Diskussion](https://stackoverflow.com/questions/40777377/endroid-qr-code)