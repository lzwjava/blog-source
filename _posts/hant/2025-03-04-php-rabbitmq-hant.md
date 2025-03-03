---
audio: false
generated: true
lang: hant
layout: post
title: 使用 RabbitMQ 於 PHP
translated: true
---

### 關鍵要點
- 使用 "php-amqplib/php-amqplib" 版本 2.6.* 似乎需要通過 Composer 安裝，並遵循基本步驟來發送和接收 RabbitMQ 的消息。
- 過程涉及設置連接、聲明隊列，並使用 `basic_publish` 方法發送和 `basic_consume` 方法接收，這些方法可能與較新版本有所不同。
- 研究表明，對於版本 2.6.*，消費過程需要手動循環使用 `wait()`，而較新版本可能使用 `consume()` 方法。

---

### 安裝和設置
要開始使用 "php-amqplib/php-amqplib" 版本 2.6.*，首先使用 Composer 安裝它，運行以下命令：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

確保 RabbitMQ 已安裝並在您的系統上運行，通常可以在 `localhost:5672` 訪問，使用默認憑證 (`guest/guest`)。如果您的設置不同，請調整這些設置。

### 發送消息
要發送消息，包含必要的 PHP 文件並創建連接：

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

聲明一個隊列並發布您的消息：

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

最後，關閉連接：

```php
$channel->close();
$connection->close();
```

### 接收消息
接收消息時，設置與發送相似，但定義一個回調函數來處理消息：

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

請注意，對於版本 2.6.*，您需要使用 `wait()` 循環來保持消費，這是與較新版本相比的意外細節，因為較新版本可能使用更簡單的 `consume()` 方法。

---

### 調查筆記：詳細使用 "php-amqplib/php-amqplib" 版本 2.6.*

本節提供了使用 "php-amqplib/php-amqplib" 庫的全面指南，特別是版本 2.6.*，以與 RabbitMQ 這個流行的消息隊列系統進行交互。這些信息來自官方文檔、教程和版本特定的細節，確保開發人員能夠全面理解。

#### 背景和上下文
"php-amqplib/php-amqplib" 是一個用於與 RabbitMQ 通信的 PHP 庫，實現了 AMQP 0.9.1 協議。版本 2.6.* 是一個較舊的版本，儘管該庫已經在 2025 年 3 月發布了 3.x.x 版本，但了解其在這個特定版本中的使用對於遺留系統或特定項目需求至關重要。該庫由包括 Ramūnas Dronga 和 Luke Bakken 在內的貢獻者維護，並且 VMware 工程師在 RabbitMQ 上有顯著的參與 ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))。

RabbitMQ 教程，例如官方 RabbitMQ 網站上的教程，提供了通常適用的示例，但可能反映了較新的版本。對於版本 2.6.*，需要進行調整，特別是在消費過程中，如下所述。

#### 安裝過程
首先，使用 Composer 安裝庫，這是 PHP 依賴管理器。在項目目錄中運行以下命令：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

這個命令確保庫被下載並配置以供使用，Composer 管理依賴。確保 RabbitMQ 已安裝並運行，通常可以在 `localhost:5672` 訪問，使用默認憑證 (`guest/guest`)。對於生產環境，根據需要調整主機、端口和憑證，並參考 [CloudAMQP PHP 文檔](https://www.cloudamqp.com/docs/php.html) 以了解受管理的代理設置。

#### 發送消息：逐步指南
發送消息涉及建立連接並發布到隊列。以下是過程：

1. **包含必要的文件：**
   使用 Composer 自動加載器包含庫：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **創建連接和通道：**
   初始化與 RabbitMQ 的連接並打開一個通道：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   參數是主機、端口、用戶名和密碼，如上所示。對於 SSL 或其他配置，請參考 [RabbitMQ PHP 教程](https://www.rabbitmq.com/tutorials/tutorial-one-php)。

3. **聲明隊列並發布：**
   聲明一個隊列以確保其存在，然後發布一條消息：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   這裡，`queue_declare` 創建一個名為 'hello' 的隊列，使用默認設置（非持久化、非獨佔、自動刪除）。`basic_publish` 將消息發送到隊列。

4. **關閉連接：**
   發送後，關閉通道和連接以釋放資源：

   ```php
   $channel->close();
   $connection->close();
   ```

這個過程在各個版本中是標準的，變更日誌中沒有記錄對於版本 2.6.* 相比於後來的版本的顯著變化。

#### 接收消息：版本特定細節
在版本 2.6.* 中接收消息需要仔細注意，因為消費機制與較新版本不同。以下是詳細過程：

1. **包含必要的文件：**
   與發送相同，包含自動加載器和必要的類：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **創建連接和通道：**
   如上所述建立連接和通道：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **聲明隊列：**
   確保隊列存在，與發送者的聲明匹配：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **定義回調：**
   創建一個回調函數來處理接收到的消息：

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   這個函數將對每條消息調用，在這個例子中打印消息體。

5. **消費消息：**
   對於版本 2.6.*，使用 `basic_consume` 註冊回調，然後進入循環以保持消費：

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` 方法接受隊列名稱、消費者標籤、no-local、no-ack、獨佔、no-wait 和回調作為參數。循環與 `wait()` 保持消費者運行，檢查消息。這是一個重要細節，因為較新版本（例如 3.2）可能使用 `consume()` 方法，根據 API 文檔檢查，這在 2.6.* 中不可用。

6. **關閉連接：**
   消費後，關閉資源：

   ```php
   $channel->close();
   $connection->close();
   ```

意外的細節是版本 2.6.* 需要手動循環，這可能需要在生產中進行額外的錯誤處理，例如捕捉連接問題的異常。

#### 版本特定考量
版本 2.6.* 是較舊的版本，儘管變更日誌中沒有明確列出它，但 2.5 到 2.7 之間的版本顯示了心跳支持和 PHP 5.3 兼容性等增強。對於大消息，版本 2.6.* 支持通道上的 `setBodySizeLimit` 來處理內存限制，如果設置則截斷消息，詳細信息請參考 [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)。

與版本 3.2 相比，變更包括 PHP 8 支持和新方法如 `consume()`，但發送和基本消費的核心功能保持相似。用戶應該測試兼容性，特別是與 PHP 版本，因為 2.6.* 可能支持 PHP 5.3 到 7.x，根據變更日誌條目。

#### 錯誤排除和最佳實踐
- 如果發送失敗，請檢查 RabbitMQ 日誌以獲取資源警報，例如磁盤空間低於 50 MB，並根據 [RabbitMQ 配置指南](https://www.rabbitmq.com/configure.html#config-items) 调整設置。
- 對於消費，請確保消費者持續運行；在生產中使用工具如 Supervisor 來守護進程。
- 使用 `rabbitmqctl list_queues` 在 Linux 上或 `rabbitmqctl.bat list_queues` 在 Windows 上作為特權用戶列出隊列，參考 [RabbitMQ 命令行工具](https://www.rabbitmq.com/cli.html)。

#### 表：關鍵方法的版本比較

| 方法             | 版本 2.6.* 行為                          | 版本 3.2 行為                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | 標準，發布到隊列                    | 未變更，相同使用                        |
| `basic_consume`    | 需要使用 `wait()` 循環進行消費       | 相似，但 `consume()` 方法可用     |
| `setBodySizeLimit` | 支持大消息，如果設置則截斷 | 支持，相同功能                |
| PHP 兼容性  | 可能 5.3 到 7.x                               | 支持 PHP 7.x 和 8.x                     |

這個表格突出了消費過程中的關鍵差異，這對於 2.6.* 用戶至關重要。

#### 結論
使用 "php-amqplib/php-amqplib" 版本 2.6.* 涉及標準的 Composer 安裝，通過 `basic_publish` 發送消息，並通過 `basic_consume` 使用手動循環接收消息。儘管與較新版本相似，但消費過程需要額外注意，這使得開發人員必須測試並調整遺留系統。有關更多詳細信息，請參考官方 RabbitMQ 教程和 GitHub 存儲庫。

---

### 關鍵引用
- [GitHub - php-amqplib/php-amqplib 最廣泛使用的 PHP 客戶端](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ 教程 - "Hello World!" PHP 示例](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP 文檔 使用 CloudAMQP 和 PHP 開始](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist 以前是 videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG 文件](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ 配置指南 配置項和設置](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ 命令行工具 CLI 參考和使用](https://www.rabbitmq.com/cli.html)