---
audio: false
generated: true
lang: hant
layout: post
title: Redis 客戶端 for PHP
translated: true
---

要在 PHP 中使用 `"predis/predis": "1.1"` 圖書館，你是指一個可以通過 Composer 安裝的 Redis 客戶端。以下是設置和在你的 PHP 專案中使用它的分步指南：

---

### 1. **安裝 Composer（如果尚未安裝）**
如果你還沒有安裝 Composer，請從 [getcomposer.org](https://getcomposer.org/) 下載並安裝它。它是 PHP 的依賴管理工具。

---

### 2. **設置你的專案**
如果你還沒有專案，請創建一個目錄：
```bash
mkdir my-redis-project
cd my-redis-project
```

---

### 3. **將 Predis 添加到你的專案**
運行以下 Composer 命令來安裝 Predis 1.1 版本：
```bash
composer require predis/predis:1.1
```
這將下載 Predis 1.1 版本並生成一個 `composer.json` 文件（以及一個包含圖書館的 `vendor` 目錄）。

或者，如果你已經有一個 `composer.json` 文件，你可以手動將以下行添加到其中：
```json
{
    "require": {
        "predis/predis": "1.1"
    }
}
```
然後運行：
```bash
composer install
```

---

### 4. **包含自動加載器**
在你的 PHP 腳本中，包含 Composer 自動加載器以加載 Predis：
```php
require 'vendor/autoload.php';
```

---

### 5. **基本使用範例**
以下是如何連接到 Redis 伺服器並使用 Predis 的簡單範例：

```php
<?php
require 'vendor/autoload.php';

use Predis\Client;

// 創建一個新的 Redis 客戶端實例
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1', // 替換為你的 Redis 伺服器主機
    'port'   => 6379,        // 默認 Redis 端口
]);

// 設置一個鍵值對
$redis->set('mykey', 'Hello, Redis!');

// 獲取值
$value = $redis->get('mykey');
echo $value; // 輸出：Hello, Redis!

// 列表範例
$redis->lpush('mylist', 'item1');
$redis->lpush('mylist', 'item2');
$list = $redis->lrange('mylist', 0, -1);
print_r($list); // 輸出：Array ( [0] => item2 [1] => item1 )
?>
```

---

### 6. **配置選項**
你可以通過將一個選項數組傳遞給 `Client` 构造函數來自定義連接。例如：
```php
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => 'redis.example.com',
    'port'   => 6379,
    'password' => 'yourpassword', // 如果需要身份驗證
    'database' => 0,              // 選擇特定的 Redis 資料庫
]);
```

---

### 7. **常見命令**
Predis 支持大多數 Redis 命令作為方法。以下是一些範例：
- **字符串**：`set`, `get`, `incr`, `decr`
- **列表**：`lpush`, `rpush`, `lpop`, `rpop`, `lrange`
- **集合**：`sadd`, `smembers`, `srem`
- **哈希**：`hset`, `hget`, `hgetall`

要獲取完整列表，請查看 [Predis 文檔](https://github.com/predis/predis) 或 Redis 命令參考。

---

### 8. **錯誤處理**
將你的 Redis 請求包裹在一個 try-catch 塊中以處理潛在的連接或運行時錯誤：
```php
try {
    $redis->set('test', 'value');
    echo $redis->get('test');
} catch (Exception $e) {
    echo "錯誤：" . $e->getMessage();
}
```

---

### 9. **先決條件**
- 確保你有一個正在運行的 Redis 伺服器（例如，本地通過 `redis-server` 或在遠程主機上）。
- PHP 5.3.0 或更高版本（Predis 1.1 兼容較舊的 PHP 版本，但請檢查你的環境）。

---

這就是了！你現在已經設置好在你的 PHP 專案中使用 Predis 1.1。如果你需要幫助進行特定的 Redis 操作或故障排除，請告訴我！