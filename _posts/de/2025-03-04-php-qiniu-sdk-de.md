---
audio: false
generated: true
lang: de
layout: post
title: Qiniu PHP SDK
translated: true
type: note
---

Um das `"qiniu/php-sdk": "^7.0"` in PHP zu verwenden, müssen Sie das Qiniu PHP SDK in Ihr Projekt integrieren. Dieses SDK ermöglicht Ihnen die Interaktion mit Qiniu Cloud Storage Services, wie zum Beispiel das Hochladen von Dateien, das Verwalten von Buckets und mehr. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung für den Einstieg:

---

### 1. Installieren des Qiniu PHP SDK
Der empfohlene Weg zur Installation des SDKs ist über Composer, einen Dependency Manager für PHP. Stellen Sie sicher, dass Composer auf Ihrem System installiert ist.

#### Schritte:
- Öffnen Sie Ihr Terminal und navigieren Sie zu Ihrem Projektverzeichnis.
- Führen Sie den folgenden Befehl aus, um das Qiniu PHP SDK (Version 7.x) zu Ihrem Projekt hinzuzufügen:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer lädt das SDK und seine Abhängigkeiten in das `vendor/` Verzeichnis herunter und erzeugt eine Autoload-Datei.

Falls Sie Composer nicht installiert haben, können Sie es von [getcomposer.org](https://getcomposer.org/) herunterladen.

---

### 2. Richten Sie Ihr Projekt ein
Nach der Installation müssen Sie den Autoloader in Ihr PHP-Skript einbinden, um die SDK-Klassen verwenden zu können.

#### Beispiel:
Erstellen Sie eine PHP-Datei (z.B. `index.php`) in Ihrem Projektverzeichnis und fügen Sie die folgende Zeile am Anfang hinzu:
```php
require_once 'vendor/autoload.php';
```

Dies stellt sicher, dass die SDK-Klassen automatisch geladen werden, wenn sie benötigt werden.

---

### 3. Konfigurieren Sie die Authentifizierung
Um das Qiniu SDK zu verwenden, benötigen Sie Ihren Qiniu `AccessKey` und `SecretKey`, die Sie aus Ihrem Qiniu Account Dashboard beziehen können.

#### Beispiel:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Ersetzen Sie `'YOUR_ACCESS_KEY'` und `'YOUR_SECRET_KEY'` durch Ihre tatsächlichen Zugangsdaten.

---

### 4. Grundlegende Verwendung: Hochladen einer Datei
Eine der häufigsten Aufgaben mit dem Qiniu SDK ist das Hochladen von Dateien in einen Bucket. Hier ist ein Beispiel, wie Sie eine lokale Datei hochladen können.

#### Beispiel:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Ersetzen Sie dies durch Ihren Qiniu Bucket-Namen
$filePath = '/path/to/your/file.txt'; // Pfad zur Datei, die Sie hochladen möchten
$key = 'file.txt'; // Der Name der Datei im Qiniu Storage (kann null sein, um den ursprünglichen Dateinamen zu verwenden)

$token = $auth->uploadToken($bucket); // Erzeugen eines Upload-Tokens
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload fehlgeschlagen: " . $error->message();
} else {
    echo "Upload erfolgreich! Datei-Hash: " . $ret['hash'];
}
```

- `$bucket`: Der Name Ihres Qiniu Buckets.
- `$filePath`: Der lokale Pfad zur Datei, die Sie hochladen möchten.
- `$key`: Der Dateischlüssel (Name), unter dem sie in Qiniu gespeichert wird. Wenn `null`, generiert Qiniu einen Schlüssel basierend auf dem Hash der Datei.
- `$token`: Ein Upload-Token, generiert mit Ihren Zugangsdaten und dem Bucket-Namen.
- Die `putFile` Methode gibt ein Array zurück: `$ret` (Erfolgsinformationen) und `$error` (Fehlerinformationen, falls vorhanden).

---

### 5. Zusätzliche Funktionen
Das Qiniu PHP SDK bietet viele weitere Funktionalitäten, wie zum Beispiel:
- **Verwalten von Buckets**: Verwenden Sie `Qiniu\Storage\BucketManager`, um Dateien aufzulisten, zu löschen oder Bucket-Einstellungen zu verwalten.
- **Dateioperationen**: Kopieren, Verschieben oder Löschen von Dateien in Ihrem Bucket.
- **Bildverarbeitung**: Generieren von URLs für skalierte oder formatierte Bilder.

#### Beispiel: Auflisten von Dateien in einem Bucket
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Fehler: " . $error->message();
} else {
    echo "Dateien im Bucket:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. Fehlerbehandlung
Überprüfen Sie immer die `$error` Variable nach SDK-Operationen. Wenn eine Operation fehlschlägt, enthält `$error` Details darüber, was schiefgelaufen ist.

#### Beispiel:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. Voraussetzungen
- PHP-Version: Die SDK-Version `^7.0` unterstützt PHP 5.3.3 und höher (bis zu PHP 8.x in späteren Releases).
- Erweiterungen: Stellen Sie sicher, dass die PHP-Erweiterungen `cURL` und `xml` aktiviert sind, da sie vom SDK benötigt werden.

Sie können Ihre PHP-Version und Erweiterungen überprüfen mit:
```bash
php -v
php -m
```

---

### 8. Wo Sie weitermachen können
- **Dokumentation**: Weitere Details finden Sie in der [offiziellen Qiniu PHP SDK Dokumentation](https://developer.qiniu.com/kodo/sdk/php) oder im [GitHub Repository](https://github.com/qiniu/php-sdk).
- **Beispiele**: Schauen Sie sich das `examples/` Verzeichnis im GitHub-Repo für weitere Anwendungsfälle an.
- **Support**: Wenn Sie auf Probleme stoßen, reichen Sie ein Ticket beim Qiniu Support ein (<support@qiniu.com>) oder fragen Sie in ihren Community-Foren.

---

### Vollständiger Beispielcode
Hier ist ein vollständiges Skript zum Hochladen einer Datei:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/path/to/your/file.txt';
$key = 'file.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload fehlgeschlagen: " . $error->message();
} else {
    echo "Upload erfolgreich! File hash: " . $ret['hash'];
}
```

Ersetzen Sie die Platzhalterwerte (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/path/to/your/file.txt`) durch Ihre tatsächlichen Daten, und schon kann es losgehen!

Lassen Sie mich wissen, wenn Sie Hilfe zu einer bestimmten Funktion benötigen!