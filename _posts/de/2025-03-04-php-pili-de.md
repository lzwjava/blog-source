---
audio: false
generated: true
lang: de
layout: post
title: Pili Streaming Cloud Bibliothek für PHP
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass für die Verwendung von "pili-engineering/pili-sdk-php": "dev-master" eine Installation via Composer und die Einrichtung von Qiniu-Zugangsdaten erforderlich sind.
- Recherchen deuten darauf hin, dass das Paket PHP 5.3.0 oder höher benötigt und für Pili Streaming Cloud im Zusammenhang mit Qiniu bestimmt ist.
- Die Hinweise deuten darauf hin, dass ein Hub-Objekt erstellt und Stream-Operationen wie die Generierung von RTMP-URLs verwendet werden, aber die genauen Methoden können variieren.

### Installation
Stellen Sie zunächst sicher, dass Composer installiert ist. Fügen Sie das Paket Ihrer `composer.json`-Datei hinzu mit:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
Führen Sie dann `composer install` oder `composer update` aus. Binden Sie in Ihrem PHP-Skript Folgendes ein:
```php
require 'vendor/autoload.php';
```

### Einrichtung und Verwendung
Sie benötigen ein Qiniu-Konto und einen Pili Hub. Legen Sie Ihren Access Key, Secret Key und Hub-Namen fest und erstellen Sie dann ein Hub-Objekt:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('Ihr_Access_Key', 'Ihr_Secret_Key');
$hub = new Hub($credentials, 'Ihr_Hub_Name');
```
Erstellen oder holen Sie einen Stream, z.B. `$stream = $hub->createStream('Ihr_Stream_Key');`, und verwenden Sie Methoden wie `$stream->rtmpPublishUrl(60)` für Operationen.

### Unerwartetes Detail
Beachten Sie, dass "dev-master" eine Entwicklungsversion ist, die potenziell instabil sein kann, während getaggte Versionen wie 1.5.5 für den Produktiveinsatz verfügbar sind.

---

### Umfassende Anleitung zur Verwendung von "pili-engineering/pili-sdk-php": "dev-master"

Diese Anleitung bietet eine detaillierte Erkundung der Verwendung des Pakets "pili-engineering/pili-sdk-php" mit der Version "dev-master", basierend auf verfügbarer Dokumentation und Beispielen. Sie behandelt Installation, Einrichtung, Verwendung und zusätzliche Überlegungen, um ein gründliches Verständnis für Entwickler zu gewährleisten, die mit Pili Streaming Cloud Services arbeiten.

#### Hintergrund und Kontext
Das Paket "pili-engineering/pili-sdk-php" ist eine serverseitige Bibliothek für PHP, die für die Interaktion mit Pili Streaming Cloud entwickelt wurde, einem Service, der mit Qiniu, einem Cloud-Speicher- und CDN-Anbieter, verbunden ist. Die Version "dev-master" bezieht sich auf den neuesten Entwicklungszweig, der möglicherweise aktuelle Funktionen enthält, aber weniger stabil sein könnte als getaggte Releases. Das Paket erfordert PHP 5.3.0 oder höher, was es für viele PHP-Umgebungen ab dem 3. März 2025 zugänglich macht.

#### Installationsprozess
Um zu beginnen, muss Composer installiert sein, ein Abhängigkeitsmanager für PHP. Die Installation umfasst das Hinzufügen des Pakets zur `composer.json`-Datei Ihres Projekts und das Ausführen eines Composer-Befehls, um es herunterzuladen. Konkret:

- Fügen Sie Folgendes Ihrer `composer.json` unter dem Abschnitt "require" hinzu:
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- Führen Sie `composer install` oder `composer update` in Ihrem Terminal aus, um das Paket und seine Abhängigkeiten abzurufen. Dies erstellt ein `vendor`-Verzeichnis mit den notwendigen Dateien.
- Binden Sie in Ihrem PHP-Skript den Autoloader ein, um auf die Paketklassen zuzugreifen:
  ```php
  require 'vendor/autoload.php';
  ```

Dieser Prozess stellt sicher, dass das Paket in Ihr Projekt integriert ist und Composer's Autoloading für einfachen Klassen-Zugriff nutzt.

#### Voraussetzungen und Einrichtung
Bevor Sie das SDK verwenden, benötigen Sie ein Qiniu-Konto und müssen einen Pili Hub einrichten, da das SDK mit Pili Streaming Cloud Services interagiert. Dazu müssen Sie einen Access Key und einen Secret Key von Qiniu beschaffen und einen Hub auf deren Plattform erstellen. Die Dokumentation legt nahe, dass diese Zugangsdaten für die Authentifizierung wesentlich sind.

Zur Einrichtung definieren Sie Ihre Zugangsdaten in Ihrem PHP-Skript:
- Access Key: Ihr Qiniu Access Key.
- Secret Key: Ihr Qiniu Secret Key.
- Hub-Name: Der Name Ihres Pili Hubs, der bereits existieren muss.

Eine Beispiel-Einrichtung sieht so aus:
```php
$accessKey = 'Ihr_Access_Key';
$secretKey = 'Ihr_Secret_Key';
$hubName = 'Ihr_Hub_Name';
```

#### Erstellen und Verwenden des Hub-Objekts
Der Kern des SDK ist das Hub-Objekt, das die Stream-Verwaltung erleichtert. Erstellen Sie zunächst ein Credentials-Objekt mit Ihren Qiniu-Keys:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Instanziieren Sie dann ein Hub-Objekt mit diesen Zugangsdaten und Ihrem Hub-Namen:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Dieses Hub-Objekt ermöglicht es Ihnen, verschiedene stream-bezogene Operationen durchzuführen, wie das Erstellen, Abrufen oder Auflisten von Streams.

#### Arbeiten mit Streams
Streams sind zentral für Pili Streaming Cloud, und das SDK bietet Methoden, um sie über das Hub-Objekt zu verwalten. Um einen neuen Stream zu erstellen:
```php
$streamKey = 'Ihr_Stream_Key'; // Muss innerhalb des Hubs eindeutig sein
$stream = $hub->createStream($streamKey);
```
Um einen bestehenden Stream abzurufen:
```php
$stream = $hub->getStream($streamKey);
```
Das Stream-Objekt bietet dann verschiedene Methoden für Operationen, detailliert in der folgenden Tabelle basierend auf der verfügbaren Dokumentation:

| **Operation**          | **Methode**                     | **Beschreibung**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Stream erstellen       | `$hub->createStream($key)`     | Erstellt einen neuen Stream mit dem angegebenen Schlüssel. |
| Stream abrufen         | `$hub->getStream($key)`        | Ruft einen bestehenden Stream anhand des Schlüssels ab. |
| Streams auflisten      | `$hub->listStreams($marker, $limit, $prefix)` | Listet Streams mit Paginierungsoptionen auf.         |
| RTMP Publish URL       | `$stream->rtmpPublishUrl($expire)` | Erzeugt eine RTMP Publish URL mit Ablaufzeit.        |
| RTMP Play URL          | `$stream->rtmpPlayUrl()`       | Erzeugt eine RTMP Play URL für den Stream.           |
| HLS Play URL           | `$stream->hlsPlayUrl()`        | Erzeugt eine HLS Play URL für das Streaming.         |
| Stream deaktivieren    | `$stream->disable()`           | Deaktiviert den Stream.                              |
| Stream aktivieren      | `$stream->enable()`            | Aktiviert den Stream.                                |
| Stream-Status abrufen  | `$stream->status()`            | Ruft den aktuellen Status des Streams ab.            |

Um beispielsweise eine RTMP Publish URL mit einer Ablaufzeit von 60 Sekunden zu generieren:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Diese URL kann zum Publizieren von Streams an Pili Streaming Cloud verwendet werden, wobei die Ablaufzeit temporären Zugang gewährleistet.

#### Zusätzliche Überlegungen
- **Versionsstabilität**: Die Version "dev-master" ist der Entwicklungszweig und potenziell instabil. Für den Produktiveinsatz sollten Sie eine getaggte Version in Betracht ziehen, wie z.B. 1.5.5, verfügbar auf Packagist [pili-engineering/pili-sdk-php Versionen](https://packagist.org/p/pili-engineering/pili-sdk-php). Die Historie zeigt Updates wie API-Ergänzungen und Methodenverfeinerungen, mit Versionen bis zurück zu 2016.
- **Fehlerbehandlung**: Die Dokumentation schlägt die Verwendung von Try-Catch-Blöcken für Operationen vor, wie in Beispielen für Stream-Erstellung und -Abruf zu sehen, um potenzielle Ausnahmen zu behandeln.
- **Dokumentation und Beispiele**: Während spezifische Beispiele nicht umfassend detailliert waren, bietet das GitHub-Repository [Pili Streaming Cloud serverseitige Bibliothek für PHP](https://github.com/pili-engineering/pili-sdk-php) Installationsanweisungen und Funktionslisten, und Vergleiche mit anderen Sprach-SDKs (z.B. Python) deuten auf ähnliche Funktionalität hin, wie z.B. URL-Generierung.

#### Vergleichende Einblicke
Ein Vergleich mit anderen Pili SDKs, wie der Python-Version, zeigt ähnliche Muster: Beide benötigen Zugangsdaten, Hub-Einrichtung und Stream-Operationen. Die PHP-Version verwendet jedoch einen objektorientierten Ansatz mit Hub- und Stream-Klassen, im Gegensatz zum funktionaleren Stil von Python. Dies entspricht den typischen PHP-Entwicklungspraktiken und bietet Typsicherheit und IDE-Unterstützung.

#### Fazit
Die Verwendung von "pili-engineering/pili-sdk-php": "dev-master" umfasst die Installation via Composer, die Einrichtung von Qiniu-Zugangsdaten, die Erstellung eines Hub-Objekts und die Verwaltung von Streams mit Methoden wie `rtmpPublishUrl`. Stellen Sie sicher, dass Ihre Umgebung die PHP 5.3.0+-Anforderungen erfüllt, und berücksichtigen Sie die Stabilität für den Produktiveinsatz. Diese Anleitung bietet einen umfassenden Ausgangspunkt, mit weiteren Details in der offiziellen Dokumentation und im Repository.

### Wichtige Zitate
- [Pili Streaming Cloud serverseitige Bibliothek für PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php Versionen Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)