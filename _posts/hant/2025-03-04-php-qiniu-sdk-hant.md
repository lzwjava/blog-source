---
audio: false
generated: true
lang: hant
layout: post
title: 七牛雲 PHP SDK
translated: true
type: note
---

要在 PHP 中使用 `"qiniu/php-sdk": "^7.0"`，您需要將七牛 PHP SDK 整合到您的專案中。此 SDK 讓您能與七牛雲端儲存服務互動，例如上傳檔案、管理儲存空間等。以下是入門指南：

---

### 1. 安裝七牛 PHP SDK
建議透過 PHP 的相依性管理工具 Composer 來安裝 SDK。請確保系統已安裝 Composer。

#### 步驟：
- 開啟終端機並導航至您的專案目錄。
- 執行以下指令，將七牛 PHP SDK（版本 7.x）加入您的專案：
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer 會將 SDK 及其相依套件下載至 `vendor/` 目錄，並產生自動載入檔案。

若尚未安裝 Composer，可從 [getcomposer.org](https://getcomposer.org/) 下載。

---

### 2. 設定專案
安裝完成後，您需要在 PHP 腳本中包含自動載入器，以便使用 SDK 類別。

#### 範例：
在專案目錄中建立 PHP 檔案（例如 `index.php`），並在頂部加入以下行：
```php
require_once 'vendor/autoload.php';
```

這確保 SDK 類別在需要時能自動載入。

---

### 3. 設定認證
使用七牛 SDK 需要您的七牛 `AccessKey` 和 `SecretKey`，這些可從七牛帳戶儀表板取得。

#### 範例：
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

將 `'YOUR_ACCESS_KEY'` 和 `'YOUR_SECRET_KEY'` 替換為您的實際憑證。

---

### 4. 基本用法：上傳檔案
使用七牛 SDK 最常見的任務之一是上傳檔案至儲存空間。以下是上傳本地檔案的範例。

#### 範例：
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // 替換為您的七牛儲存空間名稱
$filePath = '/path/to/your/file.txt'; // 要上傳的檔案路徑
$key = 'file.txt'; // 在七牛儲存中的檔案名稱（可設為 null 使用原始檔名）

$token = $auth->uploadToken($bucket); // 產生上傳 token
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "上傳失敗：" . $error->message();
} else {
    echo "上傳成功！檔案雜湊值：" . $ret['hash'];
}
```

- `$bucket`：您的七牛儲存空間名稱。
- `$filePath`：要上傳的檔案本地路徑。
- `$key`：在七牛儲存中的檔案鍵（名稱）。若設為 `null`，七牛將基於檔案雜湊值產生鍵名。
- `$token`：使用您的憑證和儲存空間名稱產生的上傳 token。
- `putFile` 方法回傳陣列：`$ret`（成功資訊）和 `$error`（錯誤資訊，如有）。

---

### 5. 其他功能
七牛 PHP SDK 提供許多其他功能，例如：
- **管理儲存空間**：使用 `Qiniu\Storage\BucketManager` 來列出檔案、刪除檔案或管理儲存空間設定。
- **檔案操作**：在儲存空間中複製、移動或刪除檔案。
- **圖片處理**：產生調整大小或格式化圖片的 URL。

#### 範例：列出儲存空間中的檔案
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "錯誤：" . $error->message();
} else {
    echo "儲存空間中的檔案：\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. 錯誤處理
執行 SDK 操作後，請務必檢查 `$error` 變數。若操作失敗，`$error` 將包含錯誤詳情。

#### 範例：
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. 需求
- PHP 版本：SDK 版本 `^7.0` 支援 PHP 5.3.3 及以上（後續版本支援至 PHP 8.x）。
- 擴充功能：確保啟用 `cURL` 和 `xml` PHP 擴充功能，因 SDK 需要這些功能。

您可透過以下指令檢查 PHP 版本和擴充功能：
```bash
php -v
php -m
```

---

### 8. 後續步驟
- **文件**：更多詳情請參閱[七牛 PHP SDK 官方文件](https://developer.qiniu.com/kodo/sdk/php)或 [GitHub 儲存庫](https://github.com/qiniu/php-sdk)。
- **範例**：查看 GitHub 儲存庫中的 `examples/` 目錄以獲取更多使用案例。
- **支援**：若遇到問題，請提交工單至七牛支援（<support@qiniu.com>）或在社群論壇提問。

---

### 完整範例程式碼
以下是上傳檔案的完整腳本：
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
    echo "上傳失敗：" . $error->message();
} else {
    echo "上傳成功！檔案雜湊值：" . $ret['hash'];
}
```

將佔位符值（`YOUR_ACCESS_KEY`、`YOUR_SECRET_KEY`、`YOUR_BUCKET_NAME`、`/path/to/your/file.txt`）替換為您的實際資料，即可開始使用！

如需特定功能的協助，請告知！