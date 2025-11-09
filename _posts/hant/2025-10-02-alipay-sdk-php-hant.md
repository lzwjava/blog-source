---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Alipay SDK PHP 整合指南
translated: true
type: note
---

### 前置準備
要整合 Alipay SDK 至 PHP 環境，您需要：
- 有效的 Alipay 商戶帳戶（請至 https://open.alipay.com 註冊）
- RSA 金鑰對：為您的伺服器生成私鑰，並將公鑰上傳至 Alipay 用於交易簽署
- PHP 5.6+（建議使用 7.x 版本以獲得更好的安全性），並啟用 cURL 及 OpenSSL 等擴充功能
- 從官方 GitHub（例如 https://github.com/alipay/alipay-sdk-php）下載 Alipay SDK – 請注意提供的程式碼片段似乎是舊版本（約 2016 年）；最新 SDK 使用較新的 API，如 Alipay Trade APIs。若您使用舊版行動安全支付，可能仍可運作但已不建議使用

### 設定 SDK
1. **下載與引入**：從 Alipay 開發者入口網站或 GitHub 下載 SDK ZIP 壓縮檔，解壓縮至專案目錄（例如 `vendor/alipay-sdk`）
2. **引入檔案**：在 PHP 程式中引入主要 SDK 檔案，例如：
   ```php
   require_once 'path/to/alipay-sdk/AopClient.php'; // 適用於現代版 SDK
   ```
   若使用您程式碼片段中的舊版本，可能需要自訂引入方式，例如 `AopSdk.php`

3. **設定金鑰與帳戶**：
   - 使用 OpenSSL 指令或線上工具生成 RSA 金鑰（2048 位元）。範例：
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - 填入程式碼片段中的 `$config` 陣列：
     - `partner`：您的 Alipay 合作夥伴 ID（16 位數字，以 2088 開頭）
     - `private_key`：您的 PEM 編碼私鑰（原始格式，不含 -----BEGIN PRIVATE KEY----- 等標頭）
     - `alipay_public_key`：Alipay 的公鑰（從您的 Alipay 控制台複製）
     - 其他欄位：使用 HTTPS 作為 `transport`，並將 `cacert.pem`（從 Alipay 文件下載）置於程式目錄中以進行 SSL 驗證

### 初始化 SDK
建立 AopClient 實例並傳入設定：
```php
use Orvibo\AopSdk\AopClient; // 請根據您的 SDK 版本調整命名空間

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // 正式環境 URL
$aopClient->appId = 'your_app_id'; // 新版 SDK 使用 appId 取代 partner
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // 現代版 SDK 建議使用 RSA2
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

若使用舊版行動支付（如您的程式碼片段），則需使用較舊的類別，例如 `AlipaySign`

### 發起支付請求
1. **建立請求參數**：
   ```php
   $request = new AlipayTradeAppPayRequest(); // 或根據您的 SDK 版本使用類似類別
   $request->setBizContent("{" .
       "\"body\":\"測試交易\"," .
       "\"subject\":\"測試標題\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // 您的通知 URL
   ```

2. **執行請求**：
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // 此簽名字串將用於您應用程式中的 Alipay SDK
   ```

3. **在行動應用程式中（若與應用程式整合）**：將回應傳遞至您應用程式的原生 Alipay SDK（例如 Android/iOS）以完成支付

### 處理通知與回應
- **非同步通知**：在 `notify_url` 設定回呼 PHP 程式以驗證 Alipay 的通知
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // 驗證簽章
  // 處理支付狀態（例如更新資料庫）
  ```
- **同步返回**：支付完成後，Alipay 將重新導向至您設定的 `return_url`

### 測試與部署
- 使用 Alipay 沙箱環境進行測試：https://openhome.alipay.com/platform/devEnv.htm
- 常見問題：確保金鑰格式正確（無多餘行號）。建議使用 RSA2 以提升安全性
- 安全提示：安全儲存金鑰（勿置於版本控制系統中）。務必驗證簽章以防篡改

若您使用的是舊版 SDK，建議升級至 Alipay 最新 PHP SDK（例如透過 Composer：`composer require alipay/openapisdk`）以獲得更好的功能與安全性。詳細文件請參閱 https://docs.open.alipay.com/。若遇到錯誤，請分享您的程式碼與日誌以便進行疑難排解