---
audio: false
generated: true
lang: hant
layout: post
title: 七牛 PHP SDK
translated: true
---

在 PHP 中使用 `"qiniu/php-sdk": "^7.0"`，您需要將 Qiniu PHP SDK 整合到您的項目中。這個 SDK 允許您與 Qiniu 雲存儲服務進行互動，例如上傳文件、管理存儲桶等。以下是一個逐步指南，幫助您開始：

---

### 1. 安裝 Qiniu PHP SDK
推薦的安裝方式是通過 Composer，一個 PHP 的依賴管理工具。請確保您的系統已經安裝了 Composer。

#### 步驟：
- 打開您的終端並導航到您的項目目錄。
- 運行以下命令將 Qiniu PHP SDK（版本 7.x）添加到您的項目中：
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer 會將 SDK 和其依賴項下載到 `vendor/` 目錄並生成一個自動加載文件。

如果您還沒有安裝 Composer，可以從 [getcomposer.org](https://getcomposer.org/) 下載。

---

### 2. 設置您的項目
安裝後，您需要在 PHP 腳本中包含自動加載器以使用 SDK 類。

#### 範例：
在項目目錄中創建一個 PHP 文件（例如 `index.php`），並在頂部添加以下行：
```php
require_once 'vendor/autoload.php';
```

這樣可以確保在需要時自動加載 SDK 類。

---

### 3. 配置驗證
要使用 Qiniu SDK，您需要您的 Qiniu `AccessKey` 和 `SecretKey`，這些可以從您的 Qiniu 帳戶儀表板獲取。

#### 範例：
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

用您的實際憑證替換 `'YOUR_ACCESS_KEY'` 和 `'YOUR_SECRET_KEY'`。

---

### 4. 基本使用：上傳文件
使用 Qiniu SDK 的最常見任務之一是將文件上傳到存儲桶。以下是如何上傳本地文件的範例。

#### 範例：
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // 用您的 Qiniu 存儲桶名稱替換
$filePath = '/path/to/your/file.txt'; // 您要上傳的文件的本地路徑
$key = 'file.txt'; // Qiniu 存儲中的文件名（可以設置為 null 以使用原始文件名）

$token = $auth->uploadToken($bucket); // 生成上傳令牌
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "上傳失敗: " . $error->message();
} else {
    echo "上傳成功！文件哈希: " . $ret['hash'];
}
```

- `$bucket`：您的 Qiniu 存儲桶的名稱。
- `$filePath`：您要上傳的本地文件的路徑。
- `$key`：文件在 Qiniu 中的存儲鍵（名稱）。如果設置為 `null`，Qiniu 將根據文件的哈希生成鍵。
- `$token`：使用您的憑證和存儲桶名稱生成的上傳令牌。
- `putFile` 方法返回一個數組：`$ret`（成功信息）和 `$error`（如果有錯誤的錯誤信息）。

---

### 5. 額外功能
Qiniu PHP SDK 提供了許多其他功能，例如：
- **管理存儲桶**：使用 `Qiniu\Storage\BucketManager` 列出文件、刪除文件或管理存儲桶設置。
- **文件操作**：在您的存儲桶中複製、移動或刪除文件。
- **圖像處理**：生成縮放或格式化圖像的 URL。

#### 範例：列出存儲桶中的文件
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "錯誤: " . $error->message();
} else {
    echo "存儲桶中的文件:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. 錯誤處理
在 SDK 操作後，始終檢查 `$error` 變量。如果操作失敗，`$error` 將包含有關發生什麼的詳細信息。

#### 範例：
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. 要求
- PHP 版本：SDK 版本 `^7.0` 支持 PHP 5.3.3 及以上（在後來的版本中支持 PHP 8.x）。
- 扩展：請確保啟用了 `cURL` 和 `xml` PHP 扩展，因為 SDK 需要它們。

您可以使用以下命令檢查 PHP 版本和扩展：
```bash
php -v
php -m
```

---

### 8. 下一步
- **文檔**：有關更多詳細信息，請參考 [官方 Qiniu PHP SDK 文檔](https://developer.qiniu.com/kodo/sdk/php) 或 [GitHub 存儲庫](https://github.com/qiniu/php-sdk)。
- **範例**：檢查 GitHub 存儲庫中的 `examples/` 目錄以獲取更多用例。
- **支持**：如果遇到問題，請向 Qiniu 支持提交票據（<support@qiniu.com>）或在其社區論壇中提問。

---

### 完整範例代碼
以下是上傳文件的完整腳本：
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
    echo "上傳失敗: " . $error->message();
} else {
    echo "上傳成功！文件哈希: " . $ret['hash'];
}
```

用您的實際數據替換占位符值（`YOUR_ACCESS_KEY`、`YOUR_SECRET_KEY`、`YOUR_BUCKET_NAME`、`/path/to/your/file.txt`），您就可以開始了！

如果您需要幫助使用特定功能，請告訴我！