---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Alipay SDK PHP-Integrationsleitfaden
translated: true
type: note
---

### Voraussetzungen
Um das Alipay SDK in PHP zu integrieren, benötigen Sie:
- Ein gültiges Alipay-Händlerkonto (Registrierung unter https://open.alipay.com).
- RSA-Schlüsselpaare: Erstellen Sie einen privaten Schlüssel für Ihren Server und laden Sie den öffentlichen Schlüssel bei Alipay hoch, um Transaktionen zu signieren.
- PHP 5.6+ (vorzugsweise 7.x für bessere Sicherheit), mit aktivierten Erweiterungen wie cURL und OpenSSL.
- Laden Sie das Alipay SDK von dessen offiziellem GitHub herunter (z.B. https://github.com/alipay/alipay-sdk-php) – beachten Sie, dass der bereitgestellte Code-Snippet für eine ältere Version (~2016) zu sein scheint; das neueste SDK verwendet neuere APIs wie Alipay Trade APIs. Wenn Sie das veraltete Mobile Security Pay verwenden, funktioniert es möglicherweise noch, ist jedoch veraltet.

### Einrichten des SDK
1. **Herunterladen und Einbinden**: Laden Sie das SDK-ZIP von Alipays Entwicklerportal oder GitHub herunter. Extrahieren Sie es in Ihr Projektverzeichnis (z.B. `vendor/alipay-sdk`).
2. **Dateien einbinden**: Binden Sie in Ihrem PHP-Skript die Haupt-SDK-Datei ein, z.B.:
   ```php
   require_once 'pfad/zu/alipay-sdk/AopClient.php'; // Für modernes SDK
   ```
   Für die Legacy-Version in Ihrem Snippet benötigen Sie möglicherweise benutzerdefinierte Includes wie `AopSdk.php`.

3. **Schlüssel und Konto konfigurieren**:
   - Generieren Sie RSA-Schlüssel (2048-Bit) mit OpenSSL-Befehlen oder Online-Tools. Beispiel:
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - Füllen Sie das `$config`-Array wie in Ihrem Snippet gezeigt aus:
     - `partner`: Ihre Alipay-Partner-ID (16 Stellen, beginnend mit 2088).
     - `private_key`: Ihr PEM-kodierter privater Schlüssel (roh, ohne Header wie -----BEGIN PRIVATE KEY-----).
     - `alipay_public_key`: Der öffentliche Schlüssel von Alipay (kopieren Sie ihn von Ihrer Alipay-Konsole).
     - Andere Felder: Verwenden Sie HTTPS für `transport`, und legen Sie `cacert.pem` (von der Alipay-Dokumentation herunterladen) im Skriptverzeichnis für die SSL-Verifizierung ab.

### Initialisieren des SDK
Erstellen Sie eine AopClient-Instanz und übergeben Sie die Konfiguration:
```php
use Orvibo\AopSdk\AopClient; // Namespace für Ihre SDK-Version anpassen

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // Produktions-URL
$aopClient->appId = 'your_app_id'; // Neueres SDK verwendet appId statt partner
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // Modernes SDK bevorzugt RSA2
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

Für Legacy Mobile Pay wie in Ihrem Snippet würden Sie ältere Klassen wie `AlipaySign` verwenden.

### Eine Zahlungsanfrage stellen
1. **Anforderungsparameter erstellen**:
   ```php
   $request = new AlipayTradeAppPayRequest(); // Oder ähnlich für Ihre SDK-Version
   $request->setBizContent("{" .
       "\"body\":\"Testtransaktion\"," .
       "\"subject\":\"Testbetreff\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // Ihre Benachrichtigungs-URL
   ```

2. **Anfrage ausführen**:
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // Dieser signierte String wird im Alipay SDK Ihrer App verwendet
   ```

3. **In Ihrer mobilen App (bei Integration in eine App)**: Übergeben Sie die Antwort an das native Alipay SDK Ihrer App (z.B. Android/iOS), um die Zahlung abzuschließen.

### Umgang mit Benachrichtigungen und Antworten
- **Asynchrone Benachrichtigungen**: Richten Sie ein Callback-PHP-Skript unter der `notify_url` ein, um die Benachrichtigungen von Alipay zu verifizieren.
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // Signatur verifizieren
  // Zahlungsstatus verarbeiten (z.B. Datenbank aktualisieren)
  ```
- **Synchrone Rückgabe**: Nach der Zahlung leitet Alipay zu Ihrer `return_url` weiter (falls gesetzt).

### Testen und Bereitstellung
- Verwenden Sie Alipays Sandbox-Umgebung zum Testen: https://openhome.alipay.com/platform/devEnv.htm.
- Häufige Probleme: Stellen Sie sicher, dass die Schlüssel korrekt formatiert sind (keine zusätzlichen Zeilen). Verwenden Sie RSA2 für bessere Sicherheit.
- Sicherheitstipps: Speichern Sie Schlüssel sicher (nicht in der Versionskontrolle). Verifizieren Sie immer Signaturen, um Manipulationen zu verhindern.

Wenn dies für das alte SDK gilt, ziehen Sie ein Upgrade auf Alipays neuestes PHP SDK in Betracht (z.B. via Composer: `composer require alipay/openapisdk`) für bessere Funktionen und Sicherheit. Detaillierte Dokumentation finden Sie unter https://docs.open.alipay.com/. Wenn Sie auf Fehler stoßen, teilen Sie Ihren Code und Ihre Logs zur Fehlerbehebung mit.