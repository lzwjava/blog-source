---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von ffmpeg in PHP
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie zur Verwendung von "php-ffmpeg/php-ffmpeg" Version ~0.5 zuerst FFMpeg auf Ihrem System installieren müssen und dann Composer verwenden, um die PHP-Bibliothek zu installieren.
- Recherchen deuten darauf hin, dass die Autoload-Datei eingebunden und eine Instanz von `FFMpeg\FFMpeg` für die Medienbearbeitung erstellt werden muss, wobei Optionen zur Angabe von Binärpfaden bei Bedarf verfügbar sind.
- Die Hinweise sprechen dafür, Methoden wie `open()`, `save()` und `frame()` für grundlegende Operationen zu verwenden, aber überprüfen Sie die GitHub-Dokumentation für vollständige Details aufgrund potenzieller versionsspezifischer Unterschiede.

---

### Installation
Stellen Sie zunächst sicher, dass FFMpeg auf Ihrem System installiert ist:
- Unter Ubuntu verwenden Sie `sudo apt-get install ffmpeg`.
- Unter macOS verwenden Sie `brew install ffmpeg`.
- Unter Windows laden Sie es von [dieser Website](https://www.gyan.dev/ffmpeg/builds/) herunter und folgen den Anweisungen.

Installieren Sie anschließend die php-FFMpeg-Bibliothek via Composer mit:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### Einrichtung und Verwendung
Binden Sie die Autoload-Datei in Ihr PHP-Skript ein:
```php
require_once 'vendor/autoload.php';
```

Erstellen Sie eine Instanz von `FFMpeg\FFMpeg`, optional mit Pfadangaben, falls sich die FFMpeg-Binärdateien nicht im System-PATH befinden:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/pfad/zur/FFMpeg',
    'ffprobe' => '/pfad/zur/FFprobe'
));
```

Öffnen Sie eine Mediendatei und führen Sie Operationen durch, wie zum Beispiel:
- Transkodieren: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- Einzelbild extrahieren: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- Ausschneiden: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

Weitere Details finden Sie in der Dokumentation der Bibliothek auf [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von php-FFMpeg/php-FFMpeg Version ~0.5

Dieser Hinweis bietet eine eingehende Untersuchung der Verwendung der "php-FFMpeg/php-FFMpeg"-Bibliothek, speziell Version ungefähr 0.5, basierend auf verfügbaren Informationen. Er erweitert die direkte Antwort, indem alle relevanten Details aus der Recherche einbezogen werden, um ein gründliches Verständnis für Benutzer zu gewährleisten, die diese PHP-Bibliothek zur Medienbearbeitung implementieren möchten.

#### Hintergrund und Kontext
Die "php-FFMpeg/php-FFMpeg"-Bibliothek ist ein PHP-Wrapper für die FFMpeg-Binärdatei, der eine objektorientierte Bearbeitung von Video- und Audiodateien ermöglicht. Sie unterstützt Aufgaben wie Transkodieren, Einzelbild-Extraktion, Zuschneiden und mehr, was sie wertvoll für Entwickler macht, die an medienbezogenen Anwendungen arbeiten. Die Versionsangabe "~0.5" zeigt jede Version größer oder gleich 0.5 und kleiner als 1.0 an, was auf Kompatibilität mit älteren PHP-Versionen hindeutet, die sich wahrscheinlich im 0.x-Zweig des Repositorys befindet.

Angesichts des aktuellen Datums, dem 3. März 2025, und der Entwicklung der Bibliothek, könnte Version 0.5 Teil der Legacy-Unterstützung sein, wobei der Hauptzweig nun PHP 8.0 oder höher erfordert. Dieser Hinweis geht davon aus, dass der Benutzer innerhalb der Einschränkungen dieser Version arbeitet, und erkennt potenzielle Funktionsunterschiede im Vergleich zu neueren Versionen an.

#### Installationsprozess
Um zu beginnen, muss FFMpeg auf dem System installiert sein, da die Bibliothek für Operationen auf dessen Binärdateien angewiesen ist. Die Installationsmethoden variieren je nach Betriebssystem:
- **Ubuntu**: Verwenden Sie den Befehl `sudo apt-get install ffmpeg`, um über den Paketmanager zu installieren.
- **macOS**: Nutzen Sie Homebrew mit `brew install ffmpeg` für eine unkomplizierte Installation.
- **Windows**: Laden Sie die FFMpeg-Binärdateien von [dieser Website](https://www.gyan.dev/ffmpeg/builds/) herunter und folgen Sie den bereitgestellten Anweisungen, wobei Sie sicherstellen, dass die ausführbaren Dateien im System-PATH zugänglich oder manuell angegeben sind.

Nach der FFMpeg-Installation wird die php-FFMpeg-Bibliothek über Composer, den PHP-Paketmanager, installiert. Der Befehl `composer require php-FFMpeg/php-FFMpeg:~0.5` stellt sicher, dass die korrekte Version bezogen wird. Dieser Prozess erstellt ein `vendor`-Verzeichnis im Projekt, das die Bibliothek und ihre Abhängigkeiten beherbergt, wobei Composer das Autoloading für nahtlose Integration verwaltet.

#### Einrichtung und Initialisierung
Nach der Installation binden Sie die Autoload-Datei in Ihr PHP-Skript ein, um Zugriff auf die Klassen der Bibliothek zu ermöglichen:
```php
require_once 'vendor/autoload.php';
```

Erstellen Sie eine Instanz von `FFMpeg\FFMpeg`, um mit der Verwendung der Bibliothek zu beginnen. Die Erstellungsmethode erlaubt Konfiguration, was besonders wichtig ist, wenn sich FFMpeg-Binärdateien nicht im System-PATH befinden:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/pfad/zu/Ihrer/eigenen/FFMpeg',
    'ffprobe' => '/pfad/zu/Ihrer/eigenen/FFprobe'
));
```
Diese Konfiguration unterstützt das Setzen von Timeouts, Thread-Anzahlen und expliziten Binärpfaden, was die Flexibilität für verschiedene Systemkonfigurationen erhöht. Das Standard-Setup sucht nach Binärdateien im PATH, aber manuelle Angabe gewährleistet Kompatibilität, besonders in benutzerdefinierten Umgebungen.

#### Kernverwendung und Operationen
Die Bibliothek bietet eine flüssige, objektorientierte Schnittstelle für die Medienbearbeitung. Beginnen Sie, indem Sie eine Mediendatei öffnen:
```php
$video = $ff->open('input.mp4');
```
Dies unterstützt lokale Dateisystempfade, HTTP-Ressourcen und andere von FFMpeg unterstützte Protokolle, wobei eine Liste unterstützter Typen über den Befehl `ffmpeg -protocols` verfügbar ist.

##### Transkodieren
Transkodieren beinhaltet die Konvertierung von Medien in verschiedene Formate. Verwenden Sie die `save`-Methode mit einer Formatinstanz:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
Das `X264`-Format ist ein Beispiel; die Bibliothek unterstützt verschiedene Video- und Audioformate, implementierbar über `FFMpeg\Format\FormatInterface`, mit spezifischen Interfaces wie `VideoInterface` und `AudioInterface` für jeweilige Medientypen.

##### Einzelbild-Extraktion
Das Extrahieren von Einzelbildern ist nützlich für Thumbnails oder Analysen. Der folgende Code extrahiert ein Einzelbild bei 5 Sekunden:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
Die `TimeCode`-Klasse, Teil von `FFMpeg\Coordinate`, gewährleistet präzises Timing, mit Optionen für Genauigkeit bei der Bildextraktion.

##### Zuschneiden
Um einen Teil des Videos auszuschneiden, geben Sie Start- und Endzeiten an:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
Dies erzeugt ein neues Videosegment, das die ursprüngliche Qualität und das Format beibehält, mit der Möglichkeit, bei Bedarf zusätzliche Filter anzuwenden.

#### Erweiterte Funktionen und Überlegungen
Die Bibliothek unterstützt zusätzliche Funktionen, wie in der Dokumentation beschrieben:
- **Audiobearbeitung**: Ähnlich wie Video kann Audio mit `FFMpeg\Media\Audio::save` transkodiert werden, wobei Filter angewendet, Metadaten hinzugefügt und resampelt werden kann.
- **GIF-Erstellung**: Animierte GIFs können mit `FFMpeg\Media\Gif::save` gespeichert werden, mit optionalen Dauerparametern.
- **Verkettung**: Kombinieren Sie mehrere Mediendateien mit `FFMpeg\Media\Concatenate::saveFromSameCodecs` für gleiche Codecs oder `saveFromDifferentCodecs` für verschiedene Codecs, mit Ressourcen zum Weiterlesen unter [diesem Link](https://trac.ffmpeg.org/wiki/Concatenate), [diesem Link](https://ffmpeg.org/ffmpeg-formats.html#concat-1) und [diesem Link](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **Erweiterte Medienbehandlung**: Unterstützt mehrere Ein-/Ausgaben mit `-filter_complex`, nützlich für komplexe Filterung und Mapping, mit eingebauter Filterunterstützung.
- **Metadatenextraktion**: Verwenden Sie `FFMpeg\FFProbe::create` für Metadaten, validieren Sie Dateien mit `FFMpeg\FFProbe::isValid` (verfügbar seit v0.10.0, beachten Sie, dass Version 0.5 dies möglicherweise nicht hat).

Koordinaten, wie `FFMpeg\Coordinate\AspectRatio`, `Dimension`, `FrameRate`, `Point` (dynamisch seit v0.10.0) und `TimeCode`, bieten präzise Kontrolle über Medieneigenschaften, obwohl einige Funktionen wie dynamische Punkte in Version 0.5 möglicherweise nicht verfügbar sind.

#### Versionsspezifische Hinweise
Angesichts der "~0.5"-Spezifikation stimmt die Bibliothek wahrscheinlich mit dem 0.x-Zweig überein und unterstützt ältere PHP-Versionen. Das GitHub-Repository zeigt PHP 8.0 oder höher für den Hauptzweig an, mit 0.x für Legacy-Unterstützung. Allerdings wurden explizite Details zu Version 0.5 nicht in Releases gefunden, was darauf hindeutet, dass sie Teil des Commit-Verlaufs oder von Branch-Comits sein könnte. Benutzer sollten die Kompatibilität überprüfen, da neuere Funktionen wie bestimmte Koordinatentypen (z.B. dynamische Punkte) Versionen über 0.5 erfordern könnten.

#### Dokumentation und Weiterführendes
Während die Read the Docs-Seite ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) leer erschien, enthält das GitHub-Repository ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) umfassende Dokumentation innerhalb der README, die API-Nutzung, Formate und Beispiele abdeckt. Dies ist die primäre Ressource für Version 0.5, angesichts des Mangels an spezifischer Online-Dokumentation für diese Legacy-Version.

#### Tabelle: Zusammenfassung der wichtigsten Operationen und Methoden

| Operation               | Methodenbeispiel                                      | Beschreibung                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Mediendatei öffnen      | `$ff->open('input.mp4')`                           | Lädt eine Mediendatei zur Bearbeitung           |
| Video transkodieren     | `$video->save('output.mp4', new X264())`           | Konvertiert in das angegebene Format            |
| Einzelbild extrahieren  | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | Extrahiert Einzelbild zur angegebenen Zeit, speichert als Bild |
| Video zuschneiden       | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | Erstellt Ausschnitt zwischen Zeiten, speichert als neue Datei |
| Instanz konfigurieren   | `FFMpeg::create(array('binary' => '/pfad/zur/FFMpeg'))` | Setzt benutzerdefinierte Binärpfade und Optionen |

Diese Tabelle fasst die Kernfunktionalität zusammen und hilft Benutzern beim schnellen Nachschlagen während der Implementierung der Bibliothek.

#### Unerwartetes Detail: Implikationen der Legacy-Version
Ein unerwarteter Aspekt ist die potenzielle Einschränkung von Version 0.5, angesichts ihrer Platzierung im 0.x-Zweig für ältere PHP-Unterstützung. Dies könnte den Zugriff auf moderne Funktionen einschränken, wie z.B. dynamische Koordinatenpunkte, die in v0.10.0 eingeführt wurden, was Benutzer zwingt, Branch-Comits auf genaue Fähigkeiten zu überprüfen, was eine Ebene der Komplexität hinzufügt, die in neueren Versionen nicht unmittelbar ersichtlich ist.

#### Schlussfolgerung
Die Verwendung von "php-FFMpeg/php-FFMpeg" Version ~0.5 beinhaltet die Installation von FFMpeg, die Einrichtung via Composer und die Nutzung einer objektorientierten API für Medienaufgaben. Während grundlegende Operationen wie Transkodieren und Einzelbild-Extraktion unkompliziert sind, können versionsspezifische Unterschiede die Konsultation der Dokumentation des 0.x-Zweiges auf [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg) erforderlich machen. Dieser umfassende Ansatz stellt sicher, dass Benutzer die Bibliothek effektiv nutzen können, wobei sowohl ihre Leistungsfähigkeit als auch potenzielle Legacy-Einschränkungen anerkannt werden.

---

### Wichtige Zitate
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)