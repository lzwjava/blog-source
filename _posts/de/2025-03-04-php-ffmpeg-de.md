---
audio: false
generated: true
lang: de
layout: post
title: Mit ffmpeg in PHP arbeiten
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung der Version ~0.5 von "php-ffmpeg/php-ffmpeg" zunächst FFMpeg auf Ihrem System installiert werden muss und dann Composer verwendet wird, um die PHP-Bibliothek zu installieren.
- Die Forschung deutet darauf hin, dass die Autoload-Datei eingeschlossen und eine Instanz von `FFMpeg\FFMpeg` für die Medienmanipulation erstellt werden sollte, mit der Möglichkeit, Binärpfade anzugeben, falls erforderlich.
- Die Beweise sprechen dafür, Methoden wie `open()`, `save()` und `frame()` für grundlegende Operationen zu verwenden, aber überprüfen Sie die GitHub-Dokumentation auf vollständige Details aufgrund potenzieller versionsspezifischer Unterschiede.

---

### Installation
Stellen Sie zunächst sicher, dass FFMpeg auf Ihrem System installiert ist:
- Auf Ubuntu verwenden Sie `sudo apt-get install ffmpeg`.
- Auf macOS verwenden Sie `brew install ffmpeg`.
- Auf Windows laden Sie von [dieser Website](https://www.gyan.dev/ffmpeg/builds/) herunter und befolgen Sie die Anweisungen.

Installieren Sie anschließend die php-FFMpeg-Bibliothek über Composer mit:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### Einrichtung und Verwendung
Schließen Sie die Autoload-Datei in Ihrem PHP-Skript ein:
```php
require_once 'vendor/autoload.php';
```

Erstellen Sie eine Instanz von `FFMpeg\FFMpeg`, optional mit Angabe der Pfade, falls die FFMpeg-Binärdateien nicht im System-Pfad sind:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/path/to/FFMpeg',
    'ffprobe' => '/path/to/FFprobe'
));
```

Öffnen Sie eine Mediendatei und führen Sie Operationen durch, wie z.B.:
- Transcodieren: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- Extrahieren eines Frames: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- Schneiden: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

Für weitere Details verweisen Sie auf die Dokumentation der Bibliothek auf [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### Umfragehinweis: Umfassender Leitfaden zur Verwendung von php-FFMpeg/php-FFMpeg Version ~0.5

Dieser Hinweis bietet eine eingehende Untersuchung der Verwendung der "php-FFMpeg/php-FFMpeg"-Bibliothek, insbesondere Version etwa 0.5, basierend auf verfügbaren Informationen. Er erweitert die direkte Antwort, indem er alle relevanten Details aus der Forschung einbezieht und so ein umfassendes Verständnis für Benutzer sicherstellt, die diese PHP-Bibliothek zur Medienmanipulation implementieren möchten.

#### Hintergrund und Kontext
Die "php-FFMpeg/php-FFMpeg"-Bibliothek ist ein PHP-Wrapper für die FFMpeg-Binärdatei, der eine objektorientierte Manipulation von Video- und Audiodateien ermöglicht. Sie unterstützt Aufgaben wie Transcodieren, Frame-Extraktion, Schneiden und mehr, was sie wertvoll für Entwickler macht, die an medienbezogenen Anwendungen arbeiten. Die Versionsangabe "~0.5" bedeutet jede Version größer oder gleich 0.5 und kleiner als 1.0, was auf Kompatibilität mit älteren PHP-Versionen hinweist, die wahrscheinlich im 0.x-Zweig des Repositorys zu finden sind.

Angesichts des aktuellen Datums, 3. März 2025, und der Entwicklung der Bibliothek könnte die Version 0.5 Teil der Legacy-Unterstützung sein, während der Hauptzweig nun PHP 8.0 oder höher erfordert. Dieser Hinweis geht davon aus, dass der Benutzer innerhalb der Einschränkungen dieser Version arbeitet, und erkennt potenzielle Unterschiede in der Funktionalität im Vergleich zu neueren Veröffentlichungen an.

#### Installationsprozess
Zunächst muss FFMpeg auf dem System installiert werden, da die Bibliothek auf deren Binärdateien für Operationen angewiesen ist. Die Installationsmethoden variieren je nach Betriebssystem:
- **Ubuntu**: Verwenden Sie den Befehl `sudo apt-get install ffmpeg`, um über den Paketmanager zu installieren.
- **macOS**: Nutzen Sie Homebrew mit `brew install ffmpeg` für eine einfache Installation.
- **Windows**: Laden Sie die FFMpeg-Binärdateien von [dieser Website](https://www.gyan.dev/ffmpeg/builds/) herunter und befolgen Sie die bereitgestellten Anweisungen, um sicherzustellen, dass die Ausführbaren im System-Pfad zugänglich sind oder manuell angegeben werden.

Nach der Installation von FFMpeg wird die php-FFMpeg-Bibliothek über Composer, den PHP-Paketmanager, installiert. Der Befehl `composer require php-FFMpeg/php-FFMpeg:~0.5` stellt sicher, dass die richtige Version abgerufen wird. Dieser Prozess erstellt ein `vendor`-Verzeichnis im Projekt, das die Bibliothek und deren Abhängigkeiten enthält, wobei Composer das Autoloading verwaltet, um eine nahtlose Integration zu gewährleisten.

#### Einrichtung und Initialisierung
Nach der Installation schließen Sie die Autoload-Datei in Ihrem PHP-Skript ein, um den Zugriff auf die Klassen der Bibliothek zu ermöglichen:
```php
require_once 'vendor/autoload.php';
```

Erstellen Sie eine Instanz von `FFMpeg\FFMpeg`, um mit der Bibliothek zu beginnen. Die Erstellungsmethode ermöglicht die Konfiguration, insbesondere wenn FFMpeg-Binärdateien nicht im System-Pfad sind:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/path/to/your/own/FFMpeg',
    'ffprobe' => '/path/to/your/own/FFprobe'
));
```
Diese Konfiguration unterstützt das Festlegen von Timeouts, Thread-Zahlen und expliziten Binärpfaden, was die Flexibilität für verschiedene Systemeinstellungen erhöht. Die Standardkonfiguration sucht nach Binärdateien im Pfad, aber eine manuelle Angabe stellt die Kompatibilität sicher, insbesondere in benutzerdefinierten Umgebungen.

#### Kernverwendung und Operationen
Die Bibliothek bietet eine flüssige, objektorientierte Schnittstelle zur Medienmanipulation. Beginnen Sie mit dem Öffnen einer Mediendatei:
```php
$video = $ff->open('input.mp4');
```
Dies unterstützt lokale Dateisystempfade, HTTP-Ressourcen und andere von FFMpeg unterstützte Protokolle, wobei eine Liste der unterstützten Typen über den Befehl `ffmpeg -protocols` verfügbar ist.

##### Transcodieren
Das Transcodieren beinhaltet das Konvertieren von Medien in verschiedene Formate. Verwenden Sie die `save`-Methode mit einer Formatinstanz:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
Das `X264`-Format ist nur ein Beispiel; die Bibliothek unterstützt verschiedene Video- und Audioformate, die über `FFMpeg\Format\FormatInterface` implementiert werden können, mit spezifischen Schnittstellen wie `VideoInterface` und `AudioInterface` für die jeweiligen Medientypen.

##### Frame-Extraktion
Die Extraktion von Frames ist nützlich für Thumbnails oder Analysen. Der folgende Code extrahiert einen Frame bei 5 Sekunden:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
Die `TimeCode`-Klasse, Teil von `FFMpeg\Coordinate`, stellt eine präzise Zeitmessung sicher, mit Optionen für Genauigkeit bei der Bildextraktion.

##### Schneiden
Um einen Teil des Videos zu schneiden, geben Sie Start- und Endzeiten an:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
Dies erstellt ein neues Video-Segment, das die ursprüngliche Qualität und das Format beibehält, mit der Möglichkeit, zusätzliche Filter anzuwenden, falls erforderlich.

#### Fortgeschrittene Funktionen und Überlegungen
Die Bibliothek unterstützt zusätzliche Funktionen, wie in der Dokumentation beschrieben:
- **Audio-Manipulation**: Ähnlich wie bei Video kann Audio mit `FFMpeg\Media\Audio::save` transcodiert werden, wobei Filter angewendet, Metadaten hinzugefügt und resampled wird.
- **GIF-Erstellung**: Animierte GIFs können mit `FFMpeg\Media\Gif::save` gespeichert werden, mit optionalen Dauerparametern.
- **Verkettung**: Kombinieren Sie mehrere Mediendateien mit `FFMpeg\Media\Concatenate::saveFromSameCodecs` für gleiche Codecs oder `saveFromDifferentCodecs` für verschiedene Codecs, mit Ressourcen für weiteres Lesen unter [diesem Link](https://trac.ffmpeg.org/wiki/Concatenate), [diesem Link](https://ffmpeg.org/ffmpeg-formats.html#concat-1) und [diesem Link](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **Erweiterte Medienverarbeitung**: Unterstützt mehrere Eingänge/Ausgänge mit `-filter_complex`, nützlich für komplexe Filterung und Zuordnung, mit eingebauter Filterunterstützung.
- **Metadaten-Extraktion**: Verwenden Sie `FFMpeg\FFProbe::create` für Metadaten, validieren Sie Dateien mit `FFMpeg\FFProbe::isValid` (verfügbar seit v0.10.0, wobei Version 0.5 dies möglicherweise nicht enthält).

Koordinaten wie `FFMpeg\Coordinate\AspectRatio`, `Dimension`, `FrameRate`, `Point` (dynamisch seit v0.10.0) und `TimeCode` bieten eine präzise Kontrolle über die Medieneigenschaften, wobei einige Funktionen wie dynamische Punkte möglicherweise in Version 0.5 nicht verfügbar sind.

#### Versionsspezifische Hinweise
Angesichts der Angabe "~0.5" stimmt die Bibliothek wahrscheinlich mit dem 0.x-Zweig überein, der ältere PHP-Versionen unterstützt. Das GitHub-Repository deutet auf PHP 8.0 oder höher für den Hauptzweig hin, mit 0.x für Legacy-Unterstützung. Genauere Details zur Version 0.5 wurden jedoch nicht explizit in den Veröffentlichungen gefunden, was darauf hinweist, dass sie möglicherweise Teil der Commit-Historie oder Branch-Commits ist. Benutzer sollten die Kompatibilität überprüfen, da neuere Funktionen wie bestimmte Koordinatentypen (z.B. dynamische Punkte) möglicherweise Versionen jenseits von 0.5 erfordern.

#### Dokumentation und weiteres Lesen
Während die Read-the-Docs-Seite ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) leer erschien, enthält das GitHub-Repository ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) umfassende Dokumentation innerhalb der README-Datei, die API-Verwendung, Formate und Beispiele abdeckt. Dies ist die Hauptressource für Version 0.5, da keine spezifische Online-Dokumentation für diese Legacy-Version gefunden wurde.

#### Tabelle: Zusammenfassung der wichtigsten Operationen und Methoden

| Operation               | Methodenbeispiel                                      | Beschreibung                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Mediendatei öffnen       | `$ff->open('input.mp4')`                           | Lädt eine Mediendatei zur Manipulation             |
| Video transcodieren      | `$video->save('output.mp4', new X264())`           | Konvertiert in das angegebene Format                    |
| Frame extrahieren       | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | Extrahiert Frame zur angegebenen Zeit, speichert als Bild |
| Video schneiden         | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | Erstellt Clip zwischen Zeiten, speichert als neue Datei   |
| Instanz konfigurieren   | `FFMpeg::create(array('binary' => '/path/to/FFMpeg'))` | Setzt benutzerdefinierte Binärpfade und Optionen            |

Diese Tabelle fasst die Kernfunktionalität zusammen und hilft Benutzern bei der schnellen Referenz bei der Implementierung der Bibliothek.

#### Unerwartetes Detail: Auswirkungen der Legacy-Version
Ein unerwarteter Aspekt ist die potenzielle Einschränkung der Version 0.5, da sie im 0.x-Zweig für ältere PHP-Unterstützung platziert ist. Dies könnte den Zugriff auf moderne Funktionen wie dynamische Koordinatenpunkte, die in v0.10.0 eingeführt wurden, einschränken, und erfordert von Benutzern, Branch-Commits auf genaue Fähigkeiten zu überprüfen, was eine zusätzliche Komplexität hinzufügt, die in neueren Versionen nicht sofort ersichtlich ist.

#### Schlussfolgerung
Die Verwendung von "php-FFMpeg/php-FFMpeg" Version ~0.5 umfasst die Installation von FFMpeg, die Einrichtung über Composer und die Nutzung einer objektorientierten API für Medienaufgaben. Während grundlegende Operationen wie Transcodieren und Frame-Extraktion einfach sind, können versionsspezifische Unterschiede die Notwendigkeit erfordern, die 0.x-Zweig-Dokumentation auf [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) zu konsultieren. Dieser umfassende Ansatz stellt sicher, dass Benutzer die Bibliothek effektiv nutzen können, und erkennt sowohl ihre Macht als auch potenzielle Legacy-Einschränkungen an.

---

### Wichtige Zitate
- [FFMpeg PHP Objektorientierte Bibliothek Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Dokumentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Dokumentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download und Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Verkettung Wiki-Seite](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formate Dokumentationsseite](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Befehlszeilen-Tool Dokumentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)