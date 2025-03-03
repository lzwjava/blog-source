---
audio: false
generated: true
lang: de
layout: post
title: Pili Streaming Cloud Bibliothek für PHP
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung von "pili-engineering/pili-sdk-php": "dev-master" eine Installation über Composer und die Einrichtung von Qiniu-Anmeldeinformationen erforderlich ist.
- Die Forschung deutet darauf hin, dass das Paket PHP 5.3.0 oder höher erfordert und für Pili Streaming Cloud, in Verbindung mit Qiniu, gedacht ist.
- Die Beweise sprechen dafür, ein Hub-Objekt zu erstellen und Stream-Operationen wie das Generieren von RTMP-URLs zu verwenden, aber die genauen Methoden können variieren.

### Installation
Stellen Sie zunächst sicher, dass Composer installiert ist. Fügen Sie das Paket Ihrer `composer.json`-Datei hinzu mit:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
Führen Sie dann `composer install` oder `composer update` aus. In Ihrem PHP-Skript fügen Sie hinzu:
```php
require 'vendor/autoload.php';
```

### Einrichtung und Verwendung
Sie benötigen ein Qiniu-Konto und ein Pili Hub. Legen Sie Ihren Zugriffsschlüssel, Geheimschlüssel und Hub-Namen fest, und erstellen Sie dann ein Hub-Objekt:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
Erstellen oder holen Sie sich einen Stream, z. B. `$stream = $hub->createStream('your_stream_key');`, und verwenden Sie Methoden wie `$stream->rtmpPublishUrl(60)` für Operationen.

### Unerwartetes Detail
Beachten Sie, dass "dev-master" eine Entwicklungsversion ist, die potenziell instabil ist, während getaggte Versionen wie 1.5.5 für die Produktion verfügbar sind.

---

### Umfassender Leitfaden zur Verwendung von "pili-engineering/pili-sdk-php": "dev-master"

Dieser Leitfaden bietet eine detaillierte Untersuchung, wie man das "pili-engineering/pili-sdk-php"-Paket mit der "dev-master"-Version verwendet, basierend auf der verfügbaren Dokumentation und Beispielen. Er deckt Installation, Einrichtung, Verwendung und zusätzliche Überlegungen ab und stellt sicher, dass Entwickler, die mit Pili Streaming Cloud-Diensten arbeiten, ein umfassendes Verständnis haben.

#### Hintergrund und Kontext
Das "pili-engineering/pili-sdk-php"-Paket ist eine serverseitige Bibliothek für PHP, die entwickelt wurde, um mit Pili Streaming Cloud zu interagieren, einem Dienst, der mit Qiniu, einem Cloud-Speicher- und CDN-Anbieter, verbunden ist. Die "dev-master"-Version bezieht sich auf den neuesten Entwicklungszweig, der möglicherweise neuere Funktionen enthält, aber weniger stabil als getaggte Veröffentlichungen sein könnte. Das Paket erfordert PHP 5.3.0 oder höher, was es für viele PHP-Umgebungen zugänglich macht, Stand März 3, 2025.

#### Installationsprozess
Um zu beginnen, müssen Sie Composer installiert haben, einen Abhängigkeitsmanager für PHP. Der Installationsprozess umfasst das Hinzufügen des Pakets zu Ihrer `composer.json`-Datei und das Ausführen eines Composer-Befehls, um es herunterzuladen. Speziell:

- Fügen Sie Folgendes zu Ihrer `composer.json` unter dem Abschnitt "require" hinzu:
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- Führen Sie `composer install` oder `composer update` in Ihrem Terminal aus, um das Paket und seine Abhängigkeiten zu holen. Dies erstellt ein `vendor`-Verzeichnis mit den erforderlichen Dateien.
- In Ihrem PHP-Skript schließen Sie den Autoloader ein, um auf die Paketklassen zuzugreifen:
  ```php
  require 'vendor/autoload.php';
  ```

Dieser Prozess stellt sicher, dass das Paket in Ihr Projekt integriert ist und Composer's Autoloading für einen einfachen Klassenzugriff genutzt wird.

#### Voraussetzungen und Einrichtung
Bevor Sie die SDK verwenden, benötigen Sie ein Qiniu-Konto und müssen einen Pili Hub einrichten, da die SDK mit Pili Streaming Cloud-Diensten interagiert. Dies umfasst das Erhalten eines Zugriffsschlüssels und eines Geheimschlüssels von Qiniu und das Erstellen eines Hubs innerhalb ihrer Plattform. Die Dokumentation deutet darauf hin, dass diese Anmeldeinformationen für die Authentifizierung unerlässlich sind.

Um die Einrichtung vorzunehmen, definieren Sie Ihre Anmeldeinformationen in Ihrem PHP-Skript:
- Zugriffsschlüssel: Ihr Qiniu-Zugriffsschlüssel.
- Geheimschlüssel: Ihr Qiniu-Geheimschlüssel.
- Hub-Name: Der Name Ihres Pili Hubs, der vor der Verwendung existieren muss.

Ein Beispiel für die Einrichtung sieht so aus:
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Erstellen und Verwenden des Hub-Objekts
Das Herzstück der SDK ist das Hub-Objekt, das die Streamverwaltung erleichtert. Erstellen Sie zunächst ein Credentials-Objekt mit Ihren Qiniu-Schlüsseln:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Erstellen Sie dann ein Hub-Objekt mit diesen Anmeldeinformationen und Ihrem Hub-Namen:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Dieses Hub-Objekt ermöglicht es Ihnen, verschiedene streambezogene Operationen durchzuführen, wie das Erstellen, Abrufen oder Auflisten von Streams.

#### Arbeiten mit Streams
Streams sind zentral für Pili Streaming Cloud, und die SDK bietet Methoden zur Verwaltung durch das Hub-Objekt. Um einen neuen Stream zu erstellen:
```php
$streamKey = 'your_stream_key'; // Muss innerhalb des Hubs eindeutig sein
$stream = $hub->createStream($streamKey);
```
Um einen bestehenden Stream abzurufen:
```php
$stream = $hub->getStream($streamKey);
```
Das Stream-Objekt bietet dann verschiedene Methoden für Operationen, die in der folgenden Tabelle basierend auf der verfügbaren Dokumentation detailliert sind:

| **Operation**          | **Methode**                     | **Beschreibung**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Stream erstellen        | `$hub->createStream($key)`     | Erstellt einen neuen Stream mit dem angegebenen Schlüssel.             |
| Stream abrufen          | `$hub->getStream($key)`        | Ruft einen bestehenden Stream nach Schlüssel ab.                 |
| Streams auflisten       | `$hub->listStreams($marker, $limit, $prefix)` | Listet Streams mit Paginierungsoptionen auf.               |
| RTMP Publish URL       | `$stream->rtmpPublishUrl($expire)` | Generiert eine RTMP Publish URL mit Ablaufzeit.  |
| RTMP Play URL          | `$stream->rtmpPlayUrl()`       | Generiert eine RTMP Play URL für den Stream.           |
| HLS Play URL           | `$stream->hlsPlayUrl()`        | Generiert eine HLS Play URL für das Streaming.             |
| Stream deaktivieren    | `$stream->disable()`           | Deaktiviert den Stream.                                 |
| Stream aktivieren      | `$stream->enable()`            | Aktiviert den Stream.                                  |
| Streamstatus abrufen   | `$stream->status()`            | Ruft den aktuellen Status des Streams ab.          |

Zum Beispiel, um eine RTMP Publish URL mit einer Ablaufzeit von 60 Sekunden zu generieren:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Diese URL kann zum Veröffentlichen von Streams an Pili Streaming Cloud verwendet werden, wobei die Ablaufzeit einen vorübergehenden Zugriff gewährleistet.

#### Zusätzliche Überlegungen
- **Versionsstabilität**: Die "dev-master"-Version ist der Entwicklungszweig, der potenziell instabil ist. Für die Produktion sollten Sie eine getaggte Version wie 1.5.5 in Betracht ziehen, die auf Packagist [pili-engineering/pili-sdk-php-Versionen](https://packagist.org/p/pili-engineering/pili-sdk-php) verfügbar ist. Die Geschichte zeigt Updates wie API-Hinzufügungen und Methodenverfeinerungen, mit Versionen, die bis ins Jahr 2016 zurückreichen.
- **Fehlerbehandlung**: Die Dokumentation schlägt die Verwendung von try-catch-Blöcken für Operationen vor, wie in den Beispielen für das Erstellen und Abrufen von Streams gezeigt, um potenzielle Ausnahmen zu behandeln.
- **Dokumentation und Beispiele**: Während spezifische Beispiele nicht ausführlich detailliert wurden, bietet das GitHub-Repository [Pili Streaming Cloud serverseitige Bibliothek für PHP](https://github.com/pili-engineering/pili-sdk-php) Installationsanweisungen und Funktionslisten, und Vergleiche mit anderen Sprach-SDKs (z. B. Python) deuten auf ähnliche Funktionalitäten hin, wie die URL-Generierung.

#### Vergleichende Erkenntnisse
Der Vergleich mit anderen Pili SDKs, wie der Python-Version, zeigt ähnliche Muster: Beide erfordern Anmeldeinformationen, Hub-Einrichtung und Stream-Operationen. Die PHP-Version verwendet jedoch einen objektorientierten Ansatz mit Hub- und Stream-Klassen, im Gegensatz zum funktionaleren Stil von Python. Dies entspricht den typischen PHP-Entwicklungsgewohnheiten und bietet Typsicherheit und IDE-Unterstützung.

#### Schlussfolgerung
Die Verwendung von "pili-engineering/pili-sdk-php": "dev-master" umfasst die Installation über Composer, die Einrichtung von Qiniu-Anmeldeinformationen, das Erstellen eines Hub-Objekts und das Verwalten von Streams mit Methoden wie `rtmpPublishUrl`. Stellen Sie sicher, dass Ihre Umgebung die Anforderungen von PHP 5.3.0+ erfüllt und berücksichtigen Sie die Stabilität für den Produktionsgebrauch. Dieser Leitfaden bietet einen umfassenden Ausgangspunkt, mit weiteren Details in der offiziellen Dokumentation und im Repository verfügbar.

### Wichtige Zitate
- [Pili Streaming Cloud serverseitige Bibliothek für PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php-Versionen Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)