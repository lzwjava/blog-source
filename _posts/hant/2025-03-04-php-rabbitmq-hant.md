---
audio: false
generated: true
lang: hant
layout: post
title: 在 PHP 中使用 RabbitMQ
translated: true
type: note
---

### 重點摘要
- 若要使用 "php-amqplib/php-amqplib" 2.6.* 版本，似乎需要透過 Composer 安裝，並遵循使用 RabbitMQ 發送和接收訊息的基本步驟。
- 流程包括建立連線、宣告佇列，以及使用 `basic_publish` 方法發送訊息，並使用帶有迴圈的 `basic_consume` 來接收訊息，這與較新版本可能略有不同。
- 研究顯示，對於 2.6.* 版本，消費過程需要手動使用帶有 `wait()` 的迴圈，這與可能使用更簡便的 `consume()` 方法的較新版本不同。

---

### 安裝與設定
要開始使用 "php-amqplib/php-amqplib" 2.6.* 版本，首先使用 Composer 安裝，執行以下指令：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

請確保 RabbitMQ 已安裝並在您的系統上運行，通常可透過 `localhost:5672` 存取，並使用預設憑證 (`guest/guest`)。如果您的設定不同，請調整這些設定。

### 發送訊息
要發送訊息，請包含必要的 PHP 檔案並建立連線：

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

宣告一個佇列並發布您的訊息：

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

最後，關閉連線：

```php
$channel->close();
$connection->close();
```

### 接收訊息
對於接收訊息，設定方式類似，但需定義一個回呼函數來處理訊息：

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

請注意，對於 2.6.* 版本，您需要帶有 `wait()` 的迴圈來持續消費訊息，這是一個與可能使用更簡便 `consume()` 方法的較新版本相比，出乎意料的細節。

---

### 調查備註："php-amqplib/php-amqplib" 2.6.* 版本的詳細用法

本節提供關於使用 "php-amqplib/php-amqplib" 函式庫（特別是 2.6.* 版本）與 RabbitMQ（一個流行的訊息佇列系統）互動的全面指南。這些資訊來自官方文件、教學以及版本特定細節，確保開發人員能透徹理解。

#### 背景與情境
"php-amqplib/php-amqplib" 是一個用於與 RabbitMQ 通訊的 PHP 函式庫，實作了 AMQP 0.9.1 通訊協定。2.6.* 版本是一個較舊的發布版本，儘管截至 2025 年 3 月，該函式庫已發展到 3.x.x 版本，但了解此特定版本的用法對於遺留系統或特定專案需求至關重要。該函式庫由包括 Ramūnas Dronga 和 Luke Bakken 在內的貢獻者維護，並有 VMware 工程師在 RabbitMQ 上的重要參與 ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))。

RabbitMQ 教學，例如官方 RabbitMQ 網站上的那些，提供的範例通常適用，但可能反映較新版本。對於 2.6.* 版本，需要進行調整，特別是在消費過程中，如下所述。

#### 安裝流程
首先，使用 PHP 相依性管理工具 Composer 安裝該函式庫。在您的專案目錄中執行以下指令：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

此指令確保函式庫被下載並設定以供使用，Composer 會管理相依性。請確保 RabbitMQ 已安裝並運行，通常可透過 `localhost:5672` 存取，並使用預設憑證 (`guest/guest`)。對於生產環境，請根據需要調整主機、端口和憑證，並參考 [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) 以了解託管代理設定的相關資訊。

#### 發送訊息：逐步說明
發送訊息涉及建立連線並發布到佇列。流程如下：

1. **包含必要檔案：**
   使用 Composer 自動載入器來包含函式庫：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **建立連線和通道：**
   初始化與 RabbitMQ 的連線並開啟一個通道：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   參數為主機、端口、使用者名稱和密碼，預設值如所示。對於 SSL 或其他設定，請參考 [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php)。

3. **宣告佇列並發布：**
   宣告一個佇列以確保其存在，然後發布訊息：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   這裡，`queue_declare` 建立一個名為 'hello' 的佇列，並使用預設設定（非持久、非獨佔、自動刪除）。`basic_publish` 將訊息發送到佇列。

4. **關閉連線：**
   發送後，關閉通道和連線以釋放資源：

   ```php
   $channel->close();
   $connection->close();
   ```

此流程在各版本中是標準的，變更日誌中未提及 2.6.* 版本與後續版本相比有重大變更。

#### 接收訊息：版本特定細節
在 2.6.* 版本中接收訊息需要特別注意，因為消費機制與較新版本不同。詳細流程如下：

1. **包含必要檔案：**
   與發送類似，包含自動載入器和必要的類別：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **建立連線和通道：**
   如前所述建立連線和通道：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **宣告佇列：**
   確保佇列存在，並與發送方的宣告匹配：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **定義回呼函數：**
   建立一個回呼函數來處理接收到的訊息：

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   此函數將針對每條訊息被呼叫，在此範例中列印訊息主體。

5. **消費訊息：**
   對於 2.6.* 版本，使用 `basic_consume` 註冊回呼函數，然後進入一個迴圈以持續消費：

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` 方法接受佇列名稱、消費者標籤、no-local、no-ack、獨佔、no-wait 和回呼等參數。帶有 `wait()` 的迴圈保持消費者運行，檢查訊息。這是一個重要的細節，因為根據 API 文件審查，較新版本（例如 3.2）可能使用 `consume()` 方法，而該方法在 2.6.* 版本中不可用。

6. **關閉連線：**
   消費後，關閉資源：

   ```php
   $channel->close();
   $connection->close();
   ```

一個出乎意料的細節是 2.6.* 版本需要手動迴圈，這在生產使用中可能需要額外的錯誤處理，例如捕獲連線問題的異常。

#### 版本特定注意事項
2.6.* 版本是舊發布版本的一部分，雖然變更日誌沒有明確列出，但 2.5 到 2.7 左右的版本顯示了諸如心跳支援和 PHP 5.3 相容性等增強功能。對於大型訊息，2.6.* 版本支援在通道上使用 `setBodySizeLimit` 來處理記憶體限制，並在需要時截斷訊息，詳細資訊請參閱 [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)。

與 3.2 版本相比，變更包括 PHP 8 支援和新的方法如 `consume()`，但發送和基本消費的核心功能保持相似。使用者應測試相容性，特別是與 PHP 版本，因為根據變更日誌條目，2.6.* 版本可能支援 PHP 5.3 到 7.x。

#### 疑難排解與最佳實踐
- 如果發送失敗，請檢查 RabbitMQ 日誌以了解資源警報，例如磁碟空間低於 50 MB，並透過 [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items) 調整設定。
- 對於消費，請確保消費者持續運行；在生產環境中使用像 Supervisor 這樣的工具進行守護程序化。
- 在 Linux 上使用 `rabbitmqctl list_queues` 或在 Windows 上使用 `rabbitmqctl.bat list_queues`（作為特權使用者）列出佇列，根據 [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html)。

#### 表格：關鍵方法的版本比較

| 方法                 | 2.6.* 版本行為                               | 3.2 版本行為                               |
|----------------------|---------------------------------------------|-------------------------------------------|
| `basic_publish`      | 標準，發布到佇列                            | 未變更，用法相同                          |
| `basic_consume`      | 需要帶有 `wait()` 的迴圈進行消費            | 類似，但提供 `consume()` 方法             |
| `setBodySizeLimit`   | 支援大型訊息，設定時截斷                    | 支援，功能相同                            |
| PHP 相容性           | 可能為 5.3 到 7.x                           | 支援 PHP 7.x 和 8.x                       |

此表格突出了消費方面的關鍵差異，這對於 2.6.* 版本使用者至關重要。

#### 結論
使用 "php-amqplib/php-amqplib" 2.6.* 版本涉及標準的 Composer 安裝，透過 `basic_publish` 發送訊息，並透過帶有手動迴圈的 `basic_consume` 接收訊息。雖然與較新版本相似，但消費過程需要額外注意，這使得開發人員必須為遺留系統進行測試和調整。更多詳細資訊，請參閱官方 RabbitMQ 教學和 GitHub 儲存庫。

---

### 主要引用文獻
- [GitHub - php-amqplib/php-amqplib The most widely used PHP client for RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ tutorial - "Hello World!" PHP example](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation Get started with CloudAMQP and PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Formerly videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG file](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items and settings](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI reference and usage](https://www.rabbitmq.com/cli.html)