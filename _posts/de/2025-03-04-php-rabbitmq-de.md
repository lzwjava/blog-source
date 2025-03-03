---
audio: false
generated: true
lang: de
layout: post
title: RabbitMQ in PHP verwenden
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung von "php-amqplib/php-amqplib" Version 2.6.* eine Installation über Composer erforderlich ist und grundlegende Schritte zum Senden und Empfangen von Nachrichten mit RabbitMQ befolgt werden müssen.
- Der Prozess umfasst das Einrichten einer Verbindung, das Deklarieren einer Warteschlange und die Verwendung von Methoden wie `basic_publish` zum Senden und `basic_consume` mit einer Schleife zum Empfangen, was sich leicht von neueren Versionen unterscheiden kann.
- Forschungen deuten darauf hin, dass für Version 2.6.* der Empfangsprozess eine manuelle Schleife mit `wait()` erfordert, im Gegensatz zu neueren Versionen, die möglicherweise eine `consume()`-Methode verwenden.

---

### Installation und Einrichtung
Um mit "php-amqplib/php-amqplib" Version 2.6.* zu beginnen, installieren Sie es zunächst mit Composer, indem Sie ausführen:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Stellen Sie sicher, dass RabbitMQ auf Ihrem System installiert und läuft, normalerweise unter `localhost:5672` mit den Standardanmeldeinformationen (`guest/guest`). Passen Sie diese Einstellungen an, wenn Ihre Konfiguration abweicht.

### Nachrichten senden
Um eine Nachricht zu senden, schließen Sie die erforderlichen PHP-Dateien ein und erstellen Sie eine Verbindung:

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

Schließen Sie schließlich die Verbindung:

```php
$channel->close();
$connection->close();
```

### Nachrichten empfangen
Zum Empfangen richten Sie ähnlich ein, aber definieren Sie einen Rückruf für die Nachrichtenverarbeitung:

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

Beachten Sie, dass für Version 2.6.* die Schleife mit `wait()` erforderlich ist, um weiter zu empfangen, was ein unerwartetes Detail im Vergleich zu neueren Versionen ist, die möglicherweise eine einfachere `consume()`-Methode verwenden.

---

### Umfragehinweis: Detaillierte Verwendung von "php-amqplib/php-amqplib" Version 2.6.*

Dieser Abschnitt bietet eine umfassende Anleitung zur Verwendung der "php-amqplib/php-amqplib"-Bibliothek, speziell Version 2.6.*, zur Interaktion mit RabbitMQ, einem beliebten Message-Queue-System. Die Informationen stammen aus der offiziellen Dokumentation, Tutorials und versionsspezifischen Details, um Entwicklern ein gründliches Verständnis zu vermitteln.

#### Hintergrund und Kontext
"php-amqplib/php-amqplib" ist eine PHP-Bibliothek zur Kommunikation mit RabbitMQ, die das AMQP 0.9.1-Protokoll implementiert. Version 2.6.* ist eine ältere Veröffentlichung, und obwohl die Bibliothek bis März 2025 auf Version 3.x.x aktualisiert wurde, ist das Verständnis ihrer Verwendung in dieser spezifischen Version für Legacy-Systeme oder spezifische Projektanforderungen entscheidend. Die Bibliothek wird von Beiträgern einschließlich Ramūnas Dronga und Luke Bakken gepflegt, mit erheblicher Beteiligung von VMware-Ingenieuren, die an RabbitMQ arbeiten ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

RabbitMQ-Tutorials, wie die auf der offiziellen RabbitMQ-Website, bieten Beispiele, die im Allgemeinen anwendbar sind, aber möglicherweise neuere Versionen widerspiegeln. Für Version 2.6.* sind Anpassungen erforderlich, insbesondere im Empfangsprozess, wie unten detailliert.

#### Installationsprozess
Um zu beginnen, installieren Sie die Bibliothek mit Composer, dem PHP-Abhängigkeitsmanager. Führen Sie den folgenden Befehl in Ihrem Projektverzeichnis aus:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Dieser Befehl stellt sicher, dass die Bibliothek heruntergeladen und für die Verwendung konfiguriert wird, wobei Composer die Abhängigkeiten verwaltet. Stellen Sie sicher, dass RabbitMQ installiert und läuft, normalerweise unter `localhost:5672` mit den Standardanmeldeinformationen (`guest/guest`). Für die Produktion passen Sie Host, Port und Anmeldeinformationen nach Bedarf an und konsultieren Sie die [CloudAMQP PHP-Dokumentation](https://www.cloudamqp.com/docs/php.html) für verwaltete Broker-Einstellungen.

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

   Die Parameter sind Host, Port, Benutzername und Kennwort, mit den Standardwerten wie gezeigt. Für SSL oder andere Konfigurationen verweisen Sie auf das [RabbitMQ PHP-Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Warteschlange deklarieren und veröffentlichen:**
   Deklarieren Sie eine Warteschlange, um sicherzustellen, dass sie existiert, und veröffentlichen Sie dann eine Nachricht:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   Hier erstellt `queue_declare` eine Warteschlange mit dem Namen 'hello' mit Standard-Einstellungen (nicht dauerhaft, nicht exklusiv, automatisch löschen). `basic_publish` sendet die Nachricht an die Warteschlange.

4. **Verbindung schließen:**
   Nach dem Senden schließen Sie den Kanal und die Verbindung, um Ressourcen freizugeben:

   ```php
   $channel->close();
   $connection->close();
   ```

Dieser Prozess ist über Versionen hinweg standardmäßig, mit keinen wesentlichen Änderungen im Changelog für Version 2.6.* im Vergleich zu späteren Veröffentlichungen.

#### Nachrichten empfangen: Versionsspezifische Details
Das Empfangen von Nachrichten in Version 2.6.* erfordert sorgfältige Aufmerksamkeit, da der Empfangsmechanismus sich von neueren Versionen unterscheidet. Hier ist der detaillierte Prozess:

1. **Erforderliche Dateien einbinden:**
   Ähnlich wie beim Senden, binden Sie den Autoloader und die erforderlichen Klassen ein:

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
   Stellen Sie sicher, dass die Warteschlange existiert, passend zur Deklaration des Senders:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **Rückruf definieren:**
   Erstellen Sie eine Rückruf-Funktion zur Verarbeitung empfangener Nachrichten:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   Diese Funktion wird für jede Nachricht aufgerufen, die den Körper in diesem Beispiel druckt.

5. **Nachrichten konsumieren:**
   Für Version 2.6.* verwenden Sie `basic_consume`, um den Rückruf zu registrieren, und gehen Sie dann in eine Schleife, um weiter zu konsumieren:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   Die `basic_consume`-Methode nimmt Parameter für den Warteschlangennamen, den Verbrauchertag, no-local, no-ack, exklusiv, no-wait und Rückruf. Die Schleife mit `wait()` hält den Verbraucher am Laufen, Nachrichten überprüft. Dies ist ein wichtiges Detail, da neuere Versionen (z. B. 3.2) möglicherweise eine `consume()`-Methode verwenden, die in 2.6.* nicht verfügbar war, basierend auf der API-Dokumentationsüberprüfung.

6. **Verbindung schließen:**
   Nach dem Konsumieren schließen Sie die Ressourcen:

   ```php
   $channel->close();
   $connection->close();
   ```

Ein unerwartetes Detail ist die Notwendigkeit der manuellen Schleife in Version 2.6.*, die möglicherweise zusätzliche Fehlerbehandlungen für die Produktion erfordert, wie das Abfangen von Ausnahmen für Verbindungsprobleme.

#### Versionsspezifische Überlegungen
Version 2.6.* ist Teil der älteren Veröffentlichungen, und obwohl der Changelog dies nicht explizit auflistet, zeigen Versionen um 2.5 bis 2.7 Verbesserungen wie Heartbeat-Unterstützung und PHP 5.3-Kompatibilität. Für große Nachrichten unterstützt Version 2.6.* `setBodySizeLimit` auf dem Kanal, um Speichergrenzen zu behandeln, Nachrichten bei Bedarf zu kürzen, mit Details in [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

Im Vergleich zu Version 3.2 umfassen Änderungen die Unterstützung von PHP 8 und neue Methoden wie `consume()`, aber die Kernfunktionalität zum Senden und grundlegenden Konsumieren bleibt ähnlich. Benutzer sollten auf Kompatibilität testen, insbesondere mit PHP-Versionen, da 2.6.* wahrscheinlich PHP 5.3 bis 7.x unterstützt, basierend auf Changelog-Einträgen.

#### Fehlerbehebung und Best Practices
- Wenn das Senden fehlschlägt, überprüfen Sie die RabbitMQ-Protokolle auf Ressourcenalarme, wie z. B. weniger als 50 MB Festplattenspeicher, und passen Sie die Einstellungen gemäß der [RabbitMQ-Konfigurationsanleitung](https://www.rabbitmq.com/configure.html#config-items) an.
- Für das Konsumieren stellen Sie sicher, dass der Verbraucher kontinuierlich läuft; verwenden Sie Tools wie Supervisor zum Daemonisieren in der Produktion.
- Listen Sie Warteschlangen mit `rabbitmqctl list_queues` auf Linux oder `rabbitmqctl.bat list_queues` auf Windows als privilegierter Benutzer auf, gemäß den [RabbitMQ-Befehlszeilen-Tools](https://www.rabbitmq.com/cli.html).

#### Tabelle: Versionsvergleich für Schlüsselmethoden

| Methode             | Verhalten der Version 2.6.*                          | Verhalten der Version 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Standard, veröffentlicht in der Warteschlange                    | Unverändert, gleiche Verwendung                        |
| `basic_consume`    | Erfordert Schleife mit `wait()` zum Konsumieren       | Ähnlich, aber `consume()`-Methode verfügbar     |
| `setBodySizeLimit` | Unterstützt für große Nachrichten, kürzt bei Einstellung | Unterstützt, gleiche Funktionalität                |
| PHP-Kompatibilität | Wahrscheinlich 5.3 bis 7.x                               | Unterstützt PHP 7.x und 8.x                     |

Diese Tabelle hebt den wesentlichen Unterschied im Konsumieren hervor, der für Benutzer von Version 2.6.* entscheidend ist.

#### Schlussfolgerung
Die Verwendung von "php-amqplib/php-amqplib" Version 2.6.* umfasst eine Standard-Installation über Composer, mit dem Senden von Nachrichten über `basic_publish` und dem Empfangen über `basic_consume` mit einer manuellen Schleife. Während es ähnlich wie neuere Versionen ist, erfordert der Empfangsprozess zusätzliche Aufmerksamkeit, was es für Entwickler unerlässlich macht, für Legacy-Systeme zu testen und anzupassen. Für weitere Details konsultieren Sie die offiziellen RabbitMQ-Tutorials und das GitHub-Repository.

---

### Wichtige Zitate
- [GitHub - php-amqplib/php-amqplib Der am häufigsten verwendete PHP-Client für RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ-Tutorial - "Hello World!" PHP-Beispiel](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP-Dokumentation Starten Sie mit CloudAMQP und PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Früher videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG-Datei](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ-Konfigurationsanleitung Konfigurationselemente und -einstellungen](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ-Befehlszeilen-Tools CLI-Referenz und -Verwendung](https://www.rabbitmq.com/cli.html)