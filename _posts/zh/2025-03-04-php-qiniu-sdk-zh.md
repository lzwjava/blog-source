---
audio: false
generated: true
lang: zh
layout: post
title: 七牛 PHP SDK
translated: true
---

要在 PHP 中使用 `"qiniu/php-sdk": "^7.0"`，你需要将 Qiniu PHP SDK 集成到你的项目中。这个 SDK 允许你与 Qiniu 云存储服务进行交互，例如上传文件、管理存储桶等。以下是一个逐步指南，帮助你开始：

---

### 1. 安装 Qiniu PHP SDK
推荐的安装方式是通过 Composer，这是一个 PHP 的依赖管理工具。确保你的系统上已经安装了 Composer。

#### 步骤：
- 打开终端并导航到你的项目目录。
- 运行以下命令将 Qiniu PHP SDK（版本 7.x）添加到你的项目中：
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer 会将 SDK 和其依赖项下载到 `vendor/` 目录，并生成一个自动加载文件。

如果你没有安装 Composer，可以从 [getcomposer.org](https://getcomposer.org/) 下载。

---

### 2. 设置你的项目
安装完成后，你需要在 PHP 脚本中包含自动加载器，以使用 SDK 类。

#### 示例：
在项目目录中创建一个 PHP 文件（例如 `index.php`），并在顶部添加以下行：
```php
require_once 'vendor/autoload.php';
```

这样可以确保在需要时自动加载 SDK 类。

---

### 3. 配置认证
使用 Qiniu SDK 需要你的 Qiniu `AccessKey` 和 `SecretKey`，你可以从 Qiniu 账户仪表板获取。

#### 示例：
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

用你的实际凭证替换 `'YOUR_ACCESS_KEY'` 和 `'YOUR_SECRET_KEY'`。

---

### 4. 基本用法：上传文件
使用 Qiniu SDK 的最常见任务之一是将文件上传到存储桶。以下是如何上传本地文件的示例。

#### 示例：
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // 替换为你的 Qiniu 存储桶名称
$filePath = '/path/to/your/file.txt'; // 要上传的文件路径
$key = 'file.txt'; // Qiniu 存储中的文件名称（可以设置为 null 以使用原始文件名）

$token = $auth->uploadToken($bucket); // 生成上传令牌
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "上传失败: " . $error->message();
} else {
    echo "上传成功！文件哈希: " . $ret['hash'];
}
```

- `$bucket`：你的 Qiniu 存储桶名称。
- `$filePath`：要上传的本地文件路径。
- `$key`：文件在 Qiniu 中存储的键（名称）。如果设置为 `null`，Qiniu 会根据文件的哈希生成一个键。
- `$token`：使用你的凭证和存储桶名称生成的上传令牌。
- `putFile` 方法返回一个数组：`$ret`（成功信息）和 `$error`（如果有错误信息）。

---

### 5. 附加功能
Qiniu PHP SDK 提供了许多其他功能，例如：
- **管理存储桶**：使用 `Qiniu\Storage\BucketManager` 列出文件、删除文件或管理存储桶设置。
- **文件操作**：在存储桶中复制、移动或删除文件。
- **图像处理**：生成缩放或格式化图像的 URL。

#### 示例：列出存储桶中的文件
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "错误: " . $error->message();
} else {
    echo "存储桶中的文件:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. 错误处理
在 SDK 操作后始终检查 `$error` 变量。如果操作失败，`$error` 将包含有关发生了什么的详细信息。

#### 示例：
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. 要求
- PHP 版本：SDK 版本 `^7.0` 支持 PHP 5.3.3 及更高版本（在后续发布中支持到 PHP 8.x）。
- 扩展：确保启用了 `cURL` 和 `xml` PHP 扩展，因为它们是 SDK 所需的。

你可以使用以下命令检查你的 PHP 版本和扩展：
```bash
php -v
php -m
```

---

### 8. 下一步
- **文档**：更多详细信息，请参考 [官方 Qiniu PHP SDK 文档](https://developer.qiniu.com/kodo/sdk/php) 或 [GitHub 仓库](https://github.com/qiniu/php-sdk)。
- **示例**：在 GitHub 仓库中检查 `examples/` 目录以获取更多用例。
- **支持**：如果遇到问题，请向 Qiniu 支持提交票据（<support@qiniu.com>）或在他们的社区论坛中提问。

---

### 完整示例代码
以下是一个完整的脚本来上传文件：
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
    echo "上传失败: " . $error->message();
} else {
    echo "上传成功！文件哈希: " . $ret['hash'];
}
```

用你的实际数据替换占位符值（`YOUR_ACCESS_KEY`、`YOUR_SECRET_KEY`、`YOUR_BUCKET_NAME`、`/path/to/your/file.txt`），你就可以开始了！

如果你需要帮助使用特定功能，请告诉我！