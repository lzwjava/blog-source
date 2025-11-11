---
audio: false
generated: true
lang: hant
layout: post
title: PHP Redis 客戶端
translated: true
type: note
---

要在 PHP 中使用 `"predis/predis": "1.1"` 函式庫，這是一個可透過 Composer 安裝的 Redis 客戶端。以下是在 PHP 專案中設定與使用的逐步指南：

---

### 1. **安裝 Composer（若尚未安裝）**
如果尚未安裝 Composer，請從 [getcomposer.org](https://getcomposer.org/) 下載並安裝。這是 PHP 的相依性管理工具。

---

### 2. **設定專案**
如果還沒有專案，請建立專案目錄：
```bash
mkdir my-redis-project
cd my-redis-project
```

---

### 3. **將 Predis 加入專案**
執行以下 Composer 指令來安裝 Predis 1.1 版：
```bash
composer require predis/predis:1.1
```
這將下載 Predis 1.1 版並生成 `composer.json` 檔案（以及包含函式庫的 `vendor` 目錄）。

若已有 `composer.json` 檔案，可手動加入這行：
```json
{
    "require": {
        "predis/predis": "1.1"
    }
}
```
然後執行：
```bash
composer install
```

---

### 4. **引入自動載入器**
在 PHP 腳本中引入 Composer 的自動載入器來載入 Predis：
```php
require 'vendor/autoload.php';
```

---

### 5. **基礎使用範例**
以下是連接 Redis 伺服器並使用 Predis 的簡單範例：

```php
<?php
require 'vendor/autoload.php';

use Predis\Client;

// 建立新的 Redis 客戶端實例
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1', // 請替換為你的 Redis 伺服器主機
    'port'   => 6379,        // 預設 Redis 端口
]);

// 設定鍵值對
$redis->set('mykey', 'Hello, Redis!');

// 取得數值
$value = $redis->get('mykey');
echo $value; // 輸出：Hello, Redis!

// 清單操作範例
$redis->lpush('mylist', 'item1');
$redis->lpush('mylist', 'item2');
$list = $redis->lrange('mylist', 0, -1);
print_r($list); // 輸出：Array ( [0] => item2 [1] => item1 )
?>
```

---

### 6. **設定選項**
可透過傳遞選項陣列給 `Client` 建構函式來自訂連線設定：
```php
$redis = new Client([
    'scheme' => 'tcp',
    'host'   => 'redis.example.com',
    'port'   => 6379,
    'password' => 'yourpassword', // 如需身份驗證
    'database' => 0,              // 選擇特定 Redis 資料庫
]);
```

---

### 7. **常用指令**
Predis 直接支援多數 Redis 指令。以下是一些範例：
- **字串**：`set`, `get`, `incr`, `decr`
- **清單**：`lpush`, `rpush`, `lpop`, `rpop`, `lrange`
- **集合**：`sadd`, `smembers`, `srem`
- **雜湊**：`hset`, `hget`, `hgetall`

完整指令清單請查閱 [Predis 文件](https://github.com/predis/predis) 或 Redis 指令參考。

---

### 8. **錯誤處理**
使用 try-catch 區塊包裝 Redis 操作以處理可能的連線或執行錯誤：
```php
try {
    $redis->set('test', 'value');
    echo $redis->get('test');
} catch (Exception $e) {
    echo "錯誤：" . $e->getMessage();
}
```

---

### 9. **必要條件**
- 確保 Redis 伺服器正在運行（例如本機透過 `redis-server` 或遠端主機）
- PHP 5.3.0 或更高版本（Predis 1.1 相容舊版 PHP，但請確認環境符合）

---

完成！你現在已經可以在 PHP 專案中使用 Predis 1.1 了。如需特定 Redis 操作或疑難排解協助，請隨時告知！