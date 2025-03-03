---
audio: false
generated: true
lang: de
layout: post
title: Qiniu PHP SDK
translated: true
---

Um die `"qiniu/php-sdk": "^7.0"` in PHP zu verwenden, müssen Sie die Qiniu PHP SDK in Ihr Projekt integrieren. Diese SDK ermöglicht es Ihnen, mit den Qiniu Cloud Storage-Diensten zu interagieren, wie z.B. das Hochladen von Dateien, das Verwalten von Buckets und mehr. Hier ist eine Schritt-für-Schritt-Anleitung, um Ihnen den Einstieg zu erleichtern:

---

### 1. Installieren Sie die Qiniu PHP SDK
Die empfohlene Methode zur Installation der SDK ist über Composer, einen Abhängigkeitsmanager für PHP. Stellen Sie sicher, dass Composer auf Ihrem System installiert ist.

#### Schritte:
- Öffnen Sie Ihr Terminal und navigieren Sie zu Ihrem Projektverzeichnis.
- Führen Sie den folgenden Befehl aus, um die Qiniu PHP SDK (Version 7.x) zu Ihrem Projekt hinzuzufügen:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer lädt die SDK und deren Abhängigkeiten in das `vendor/` Verzeichnis herunter und erstellt eine Autoload-Datei.

Falls Sie Composer nicht installiert haben, können Sie es von [getcomposer.org](https://getcomposer.org/) herunterladen.

---

### 2. Richten Sie Ihr Projekt ein
Nach der Installation müssen Sie den Autoloader in Ihrem PHP-Skript einbinden, um die SDK-Klassen zu verwenden.

#### Beispiel:
Erstellen Sie eine PHP-Datei (z.B. `index.php`) in Ihrem Projektverzeichnis und fügen Sie die folgende Zeile an den Anfang hinzu:
```php
require_once 'vendor/autoload.php';
```

Dadurch wird sichergestellt, dass die SDK-Klassen automatisch geladen werden, wenn sie benötigt werden.

---

### 3. Konfigurieren Sie die Authentifizierung
Um die Qiniu SDK zu verwenden, benötigen Sie Ihren Qiniu `AccessKey` und `SecretKey`, die Sie von Ihrem Qiniu-Konto-Dashboard erhalten können.

#### Beispiel:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Ersetzen Sie `'YOUR_ACCESS_KEY'` und `'YOUR_SECRET_KEY'` durch Ihre tatsächlichen Anmeldeinformationen.

---

### 4. Grundlegende Nutzung: Datei hochladen
Eine der häufigsten Aufgaben mit der Qiniu SDK ist das Hochladen von Dateien in einen Bucket. Hier ist ein Beispiel, wie Sie eine lokale Datei hochladen können.

#### Beispiel:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Ersetzen Sie durch den Namen Ihres Qiniu Buckets
$filePath = '/pfad/zu/ihrer/datei.txt'; // Pfad zur Datei, die Sie hochladen möchten
$key = 'datei.txt'; // Der Name der Datei in der Qiniu-Speicherung (kann null sein, um den ursprünglichen Dateinamen zu verwenden)

$token = $auth->uploadToken($bucket); // Generieren Sie ein Upload-Token
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
- `$key`: Der Dateischlüssel (Name), unter dem sie in Qiniu gespeichert wird. Wenn auf `null` gesetzt, generiert Qiniu einen Schlüssel basierend auf dem Dateihash.
- `$token`: Ein Upload-Token, das mit Ihren Anmeldeinformationen und dem Bucketnamen generiert wird.
- Die `putFile`-Methode gibt ein Array zurück: `$ret` (Erfolgsinformationen) und `$error` (Fehlerinformationen, falls vorhanden).

---

### 5. Zusätzliche Funktionen
Die Qiniu PHP SDK bietet viele weitere Funktionen, wie z.B.:
- **Verwalten von Buckets**: Verwenden Sie `Qiniu\Storage\BucketManager`, um Dateien zu listen, zu löschen oder Bucket-Einstellungen zu verwalten.
- **Dateioperationen**: Kopieren, Verschieben oder Löschen von Dateien in Ihrem Bucket.
- **Bildverarbeitung**: Generieren Sie URLs für skalierte oder formatierte Bilder.

#### Beispiel: Dateien in einem Bucket auflisten
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
Überprüfen Sie immer die Variable `$error` nach SDK-Vorgängen. Wenn ein Vorgang fehlschlägt, enthält `$error` Details darüber, was schiefgelaufen ist.

#### Beispiel:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. Anforderungen
- PHP-Version: Die SDK-Version `^7.0` unterstützt PHP 5.3.3 und höher (bis PHP 8.x in späteren Versionen).
- Erweiterungen: Stellen Sie sicher, dass die PHP-Erweiterungen `cURL` und `xml` aktiviert sind, da sie von der SDK benötigt werden.

Sie können Ihre PHP-Version und Erweiterungen mit überprüfen:
```bash
php -v
php -m
```

---

### 8. Was als Nächstes?
- **Dokumentation**: Für weitere Details besuchen Sie die [offizielle Qiniu PHP SDK-Dokumentation](https://developer.qiniu.com/kodo/sdk/php) oder das [GitHub-Repository](https://github.com/qiniu/php-sdk).
- **Beispiele**: Überprüfen Sie das Verzeichnis `examples/` im GitHub-Repo für weitere Anwendungsfälle.
- **Support**: Wenn Sie Probleme haben, senden Sie ein Ticket an den Qiniu-Support (<support@qiniu.com>) oder fragen Sie in deren Community-Foren nach.

---

### Vollständiges Beispielskript
Hier ist ein vollständiges Skript zum Hochladen einer Datei:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/pfad/zu/ihrer/datei.txt';
$key = 'datei.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload fehlgeschlagen: " . $error->message();
} else {
    echo "Upload erfolgreich! Datei-Hash: " . $ret['hash'];
}
```

Ersetzen Sie die Platzhalterwerte (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/pfad/zu/ihrer/datei.txt`) durch Ihre tatsächlichen Daten, und Sie sind startklar!

Lassen Sie mich wissen, wenn Sie Hilfe bei einer bestimmten Funktion benötigen!