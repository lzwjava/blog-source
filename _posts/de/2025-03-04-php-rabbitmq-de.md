---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von RabbitMQ in PHP
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie "php-amqplib/php-amqplib" Version 2.6.* über Composer installieren und die grundlegenden Schritte zum Senden und Empfangen von Nachrichten mit RabbitMQ befolgen müssen.
- Der Prozess umfasst das Aufbauen einer Verbindung, das Deklarieren einer Warteschlange und die Verwendung von Methoden wie `basic_publish` zum Senden und `basic_consume` mit einer Schleife zum Empfangen, was sich leicht von neueren Versionen unterscheiden kann.
- Recherchen deuten darauf hin, dass für Version 2.6.* der Empfangsprozess eine manuelle Schleife mit `wait()` erfordert, anders als bei neueren Versionen, die möglicherweise eine `consume()`-Methode verwenden.

---

### Installation und Einrichtung
Um mit "php-amqplib/php-amqplib" Version 2.6.* zu beginnen, installieren Sie es zunächst mit Composer, indem Sie folgenden Befehl ausführen:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Stellen Sie sicher, dass RabbitMQ auf Ihrem System installiert ist und läuft, typischerweise erreichbar unter `localhost:5672` mit Standardanmeldedaten (`guest/guest`). Passen Sie diese Einstellungen an, wenn Ihr Setup abweicht.

### Nachrichten senden
Um eine Nachricht zu senden, binden Sie die notwendigen PHP-Dateien ein und erstellen Sie eine Verbindung:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

Deklarieren Sie eine Warteschlange und veröffentlichen Sie Ihre Nachricht:

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

Schließen Sie abschließend die Verbindung:

```php
$channel->close();
$connection->close();
```

### Nachrichten empfangen
Richten Sie für den Empfang ähnlich ein, definieren Sie jedoch einen Callback für die Nachrichtenbehandlung:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Received ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

Beachten Sie, dass für Version 2.6.* die Schleife mit `wait()` notwendig ist, um weiterhin Nachrichten zu empfangen. Dies ist ein unerwartetes Detail im Vergleich zu neueren Versionen, die möglicherweise eine einfachere `consume()`-Methode verwenden.

---

### Umfragehinweis: Detaillierte Verwendung von "php-amqplib/php-amqplib" Version 2.6.*

Dieser Abschnitt bietet einen umfassenden Leitfaden zur Verwendung der Bibliothek "php-amqplib/php-amqplib", speziell Version 2.6.*, für die Interaktion mit RabbitMQ, einem beliebten Message-Queue-System. Die Informationen stammen aus offizieller Dokumentation, Tutorials und versionsspezifischen Details, um Entwicklern ein gründliches Verständnis zu ermöglichen.

#### Hintergrund und Kontext
"php-amqplib/php-amqplib" ist eine PHP-Bibliothek für die Kommunikation mit RabbitMQ, die das AMQP 0.9.1 Protokoll implementiert. Version 2.6.* ist eine ältere Version, und obwohl sich die Bibliothek bis März 2025 zur Version 3.x.x weiterentwickelt hat, ist das Verständnis ihrer Verwendung in dieser spezifischen Version für Legacy-Systeme oder spezifische Projektanforderungen entscheidend. Die Bibliothek wird von Mitwirkenden, darunter Ramūnas Dronga und Luke Bakken, gepflegt, mit bedeutender Beteiligung von VMware-Ingenieuren, die an RabbitMQ arbeiten ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

RabbitMQ-Tutorials, wie z.B. auf der offiziellen RabbitMQ-Website, bieten Beispiele, die allgemein anwendbar sind, aber möglicherweise neuere Versionen widerspiegeln. Für Version 2.6.* sind Anpassungen notwendig, insbesondere im Empfangsprozess, wie unten detailliert beschrieben.

#### Installationsprozess
Beginnen Sie, indem Sie die Bibliothek mit Composer, dem PHP-Abhängigkeitsmanager, installieren. Führen Sie den folgenden Befehl in Ihrem Projektverzeichnis aus:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Dieser Befehl stellt sicher, dass die Bibliothek heruntergeladen und für die Verwendung konfiguriert wird, wobei Composer die Abhängigkeiten verwaltet. Stellen Sie sicher, dass RabbitMQ installiert ist und läuft, typischerweise erreichbar unter `localhost:5672` mit Standardanmeldedaten (`guest/guest`). Für die Produktion passen Sie Host, Port und Anmeldedaten nach Bedarf an und konsultieren Sie [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) für Setups mit Managed Brokern.

#### Nachrichten senden: Schritt für Schritt
Das Senden von Nachrichten umfasst das Herstellen einer Verbindung und das Veröffentlichen in einer Warteschlange. Hier ist der Prozess:

1. **Erforderliche Dateien einbinden:**
   Verwenden Sie den Composer-Autoloader, um die Bibliothek einzubinden:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **Verbindung und Kanal erstellen:**
   Initialisieren Sie eine Verbindung zu RabbitMQ und öffnen Sie einen Kanal:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   Die Parameter sind Host, Port, Benutzername und Passwort, mit den gezeigten Standardwerten. Für SSL oder andere Konfigurationen siehe [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Warteschlange deklarieren und veröffentlichen:**
   Deklarieren Sie eine Warteschlange, um sicherzustellen, dass sie existiert, und veröffentlichen Sie dann eine Nachricht:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   Hier erstellt `queue_declare` eine Warteschlange namens 'hello' mit Standardeinstellungen (nicht dauerhaft, nicht exklusiv, automatisches Löschen). `basic_publish` sendet die Nachricht an die Warteschlange.

4. **Verbindung schließen:**
   Schließen Sie nach dem Senden den Kanal und die Verbindung, um Ressourcen freizugeben:

   ```php
   $channel->close();
   $connection->close();
   ```

Dieser Prozess ist standardmäßig über Versionen hinweg gleich, ohne signifikante Änderungen im Changelog für Version 2.6.* im Vergleich zu späteren Versionen.

#### Nachrichten empfangen: Versionsspezifische Details
Das Empfangen von Nachrichten in Version 2.6.* erfordert besondere Aufmerksamkeit, da sich der Empfangsmechanismus von neueren Versionen unterscheidet. Hier ist der detaillierte Prozess:

1. **Erforderliche Dateien einbinden:**
   Ähnlich wie beim Senden, binden Sie den Autoloader und die notwendigen Klassen ein:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **Verbindung und Kanal erstellen:**
   Stellen Sie die Verbindung und den Kanal wie zuvor her:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **Warteschlange deklarieren:**
   Stellen Sie sicher, dass die Warteschlange existiert, entsprechend der Deklaration des Senders:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **Callback definieren:**
   Erstellen Sie eine Callback-Funktion zum Behandeln empfangener Nachrichten:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   Diese Funktion wird für jede Nachricht aufgerufen und gibt in diesem Beispiel den Textkörper aus.

5. **Nachrichten empfangen:**
   Verwenden Sie für Version 2.6.* `basic_consume`, um den Callback zu registrieren, und starten Sie dann eine Schleife, um weiterhin Nachrichten zu empfangen:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   Die `basic_consume`-Methode nimmt Parameter für Warteschlangenname, Consumer-Tag, no-local, no-ack, exklusiv, no-wait und Callback entgegen. Die Schleife mit `wait()` hält den Consumer am Laufen und prüft auf Nachrichten. Dies ist ein wichtiges Detail, da neuere Versionen (z.B. 3.2) möglicherweise eine `consume()`-Methode verwenden, die in 2.6.* basierend auf einer Überprüfung der API-Dokumentation nicht verfügbar war.

6. **Verbindung schließen:**
   Schließen Sie nach dem Empfang die Ressourcen:

   ```php
   $channel->close();
   $connection->close();
   ```

Ein unerwartetes Detail ist die Notwendigkeit der manuellen Schleife in Version 2.6.*, die für den Produktionseinsatz zusätzliche Fehlerbehandlung erfordern kann, wie das Abfangen von Ausnahmen für Verbindungsprobleme.

#### Versionsspezifische Überlegungen
Version 2.6.* gehört zu den älteren Versionen, und obwohl der Changelog sie nicht explizit auflistet, zeigen Versionen um 2.5 bis 2.7 Verbesserungen wie Heartbeat-Unterstützung und PHP 5.3-Kompatibilität. Für große Nachrichten unterstützt Version 2.6.* `setBodySizeLimit` auf dem Kanal, um Speicherlimits zu handhaben und Nachrichten bei Bedarf abzuschneiden, mit Details in [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

Im Vergleich zu Version 3.2 umfassen die Änderungen PHP 8-Unterstützung und neue Methoden wie `consume()`, aber die Kernfunktionalität für das Senden und grundlegende Empfangen bleibt ähnlich. Benutzer sollten auf Kompatibilität testen, insbesondere mit PHP-Versionen, da 2.6.* wahrscheinlich PHP 5.3 bis 7.x unterstützt, gemäß Changelog-Einträgen.

#### Fehlerbehebung und Best Practices
- Wenn das Senden fehlschlägt, überprüfen Sie die RabbitMQ-Protokolle auf Ressourcenalarme, wie z.B. Festplattenspeicher unter 50 MB, und passen Sie die Einstellungen über [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items) an.
- Stellen Sie für den Empfang sicher, dass der Consumer kontinuierlich läuft; verwenden Sie Tools wie Supervisor für das Daemonisieren in der Produktion.
- Listen Sie Warteschlangen mit `rabbitmqctl list_queues` unter Linux oder `rabbitmqctl.bat list_queues` unter Windows als privilegierter Benutzer auf, gemäß [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html).

#### Tabelle: Versionsvergleich für wichtige Methoden

| Methode             | Verhalten in Version 2.6.*                          | Verhalten in Version 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Standard, veröffentlicht in Warteschlange                    | Unverändert, gleiche Verwendung                        |
| `basic_consume`    | Erfordert Schleife mit `wait()` für den Empfang       | Ähnlich, aber `consume()`-Methode verfügbar     |
| `setBodySizeLimit` | Unterstützt für große Nachrichten, schneidet bei Einstellung ab                | Unterstützt, gleiche Funktionalität                |
| PHP-Kompatibilität  | Wahrscheinlich 5.3 bis 7.x                               | Unterstützt PHP 7.x und 8.x                     |

Diese Tabelle hebt den kritischen Unterschied beim Empfang hervor, der für Benutzer von Version 2.6.* entscheidend ist.

#### Fazit
Die Verwendung von "php-amqplib/php-amqplib" Version 2.6.* umfasst eine standardmäßige Composer-Installation, das Senden von Nachrichten über `basic_publish` und das Empfangen über `basic_consume` mit einer manuellen Schleife. Während sie neueren Versionen ähnelt, erfordert der Empfangsprozess zusätzliche Aufmerksamkeit, was es für Entwickler wesentlich macht, für Legacy-Systeme zu testen und anzupassen. Weitere Details finden Sie in den offiziellen RabbitMQ-Tutorials und dem GitHub-Repository.

---

### Wichtige Zitate
- [GitHub - php-amqplib/php-amqplib The most widely used PHP client for RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ tutorial - "Hello World!" PHP example](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation Get started with CloudAMQP and PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Formerly videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG file](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items and settings](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI reference and usage](https://www.rabbitmq.com/cli.html)