---
audio: false
generated: true
lang: ja
layout: post
title: RabbitMQをPHPで使用する
translated: true
---

### 主要ポイント
- "php-amqplib/php-amqplib" バージョン 2.6.* を使用するには、Composer を使用してインストールし、RabbitMQ でメッセージの送受信のための基本的な手順を実行する必要があると考えられます。
- このプロセスには、接続の設定、キューの宣言、および `basic_publish` メソッドを使用した送信と `basic_consume` メソッドを使用した受信のループが含まれます。これは、より新しいバージョンとは少し異なる場合があります。
- 研究によると、バージョン 2.6.* の受信プロセスには、新しいバージョンが `consume()` メソッドを使用するのに対して、手動ループで `wait()` を使用する必要があるとされています。

---

### インストールと設定
"php-amqplib/php-amqplib" バージョン 2.6.* を使用するには、まず Composer を使用してインストールします。以下のコマンドを実行してください：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

システムに RabbitMQ がインストールされ、実行されていることを確認してください。通常、デフォルトの資格情報 (`guest/guest`) で `localhost:5672` にアクセスできます。設定が異なる場合は、これらの設定を調整してください。

### メッセージの送信
メッセージを送信するには、必要な PHP ファイルをインクルードし、接続を作成します：

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

キューを宣言し、メッセージを公開します：

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

最後に、接続を閉じます：

```php
$channel->close();
$connection->close();
```

### メッセージの受信
受信するには、同様に設定し、メッセージ処理のためのコールバックを定義します：

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

バージョン 2.6.* の場合、`wait()` を使用したループが必要で、これは新しいバージョンがより簡単な `consume()` メソッドを使用するのに対して意外な詳細です。

---

### アンケートノート: "php-amqplib/php-amqplib" バージョン 2.6.* の詳細な使用法

このセクションでは、RabbitMQ、人気のあるメッセージキューシステムと対話するために "php-amqplib/php-amqplib" ライブラリ、特にバージョン 2.6.* を使用するための包括的なガイドを提供します。この情報は、公式のドキュメント、チュートリアル、バージョン固有の詳細から得られ、開発者にとって徹底的な理解を提供します。

#### 背景とコンテキスト
"php-amqplib/php-amqplib" は、AMQP 0.9.1 プロトコルを実装して RabbitMQ と通信するための PHP ライブラリです。バージョン 2.6.* は古いリリースであり、ライブラリは 2025 年 3 月までにバージョン 3.x.x に進化しましたが、この特定のバージョンの使用を理解することは、レガシーシステムや特定のプロジェクト要件にとって重要です。このライブラリは、Ramūnas Dronga と Luke Bakken を含む貢献者によって維持されており、VMware エンジニアが RabbitMQ に関与しています ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))。

RabbitMQ のチュートリアル、特に公式の RabbitMQ ウェブサイトのものは、一般的に適用可能ですが、バージョン 2.6.* に対して調整が必要です。以下に詳細を示します。

#### インストールプロセス
まず、Composer、PHP の依存関係管理ツールを使用してライブラリをインストールします。プロジェクトディレクトリで以下のコマンドを実行します：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

このコマンドにより、ライブラリがダウンロードされ、使用のために設定され、Composer が依存関係を管理します。RabbitMQ がインストールされ、実行されていることを確認してください。通常、デフォルトの資格情報 (`guest/guest`) で `localhost:5672` にアクセスできます。プロダクション環境では、ホスト、ポート、資格情報を必要に応じて調整し、[CloudAMQP PHP ドキュメント](https://www.cloudamqp.com/docs/php.html) を参考にしてマネージドブローカーの設定を行ってください。

#### メッセージの送信: ステップバイステップ
メッセージの送信には、接続を確立し、キューに公開することが含まれます。以下がそのプロセスです：

1. **必要なファイルのインクルード:**
   Composer のオートローダーを使用してライブラリをインクルードします：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **接続とチャネルの作成:**
   RabbitMQ に接続し、チャネルを開きます：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   パラメータはホスト、ポート、ユーザー名、パスワードで、デフォルト値が示されています。SSL などの他の設定については、[RabbitMQ PHP チュートリアル](https://www.rabbitmq.com/tutorials/tutorial-one-php) をご覧ください。

3. **キューの宣言と公開:**
   キューが存在することを確認し、メッセージを公開します：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   ここで、`queue_declare` はデフォルト設定（非耐久性、非排他性、自動削除）で 'hello' という名前のキューを作成します。`basic_publish` はメッセージをキューに送信します。

4. **接続の閉じ:**
   送信後、リソースを解放するためにチャネルと接続を閉じます：

   ```php
   $channel->close();
   $connection->close();
   ```

このプロセスはバージョン間で標準的であり、バージョン 2.6.* の変更履歴に比べて後続のリリースでは重要な変更が見られません。

#### メッセージの受信: バージョン固有の詳細
バージョン 2.6.* でメッセージを受信するには、消費メカニズムに注意が必要です。以下が詳細なプロセスです：

1. **必要なファイルのインクルード:**
   送信と同様に、オートローダーと必要なクラスをインクルードします：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **接続とチャネルの作成:**
   以前と同様に接続とチャネルを確立します：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **キューの宣言:**
   送信側の宣言と一致するようにキューが存在することを確認します：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **コールバックの定義:**
   受信メッセージを処理するためのコールバック関数を作成します：

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   この関数は各メッセージに対して呼び出され、この例ではボディを表示します。

5. **メッセージの消費:**
   バージョン 2.6.* の場合、`basic_consume` を使用してコールバックを登録し、消費を続けるためのループに入ります：

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` メソッドには、キュー名、消費者タグ、no-local、no-ack、排他、no-wait、コールバックのパラメータがあります。ループと `wait()` は消費者を実行し続け、メッセージをチェックします。これは重要な詳細であり、バージョン 3.2 などの新しいバージョンでは `consume()` メソッドを使用する可能性がありますが、バージョン 2.6.* では API ドキュメントのレビューに基づいて利用できませんでした。

6. **接続の閉じ:**
   消費後、リソースを閉じます：

   ```php
   $channel->close();
   $connection->close();
   ```

バージョン 2.6.* では、手動ループが必要であり、これはプロダクション用に追加のエラーハンドリングが必要な場合があります。例えば、接続問題のための例外をキャッチします。

#### バージョン固有の考慮事項
バージョン 2.6.* は古いリリースであり、バージョン 2.5 から 2.7 までの変更履歴には、ハートビートサポートや PHP 5.3 の互換性などの向上が含まれています。バージョン 2.6.* では、大きなメッセージに対する `setBodySizeLimit` を使用してメモリ制限を処理し、必要に応じてメッセージを切り捨てることができます。詳細については、[GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib) をご覧ください。

バージョン 3.2 と比較すると、変更点には PHP 8 のサポートや新しいメソッド `consume()` が含まれますが、送信と基本的な消費のコア機能は似ています。ユーザーは、特に PHP バージョンとの互換性をテストする必要があります。バージョン 2.6.* は、変更履歴のエントリに基づいて PHP 5.3 から 7.x をサポートしている可能性があります。

#### トラブルシューティングとベストプラクティス
- メッセージの送信に失敗した場合、リソースアラーム（ディスクスペースが 50 MB 未満など）を確認し、[RabbitMQ 設定ガイド](https://www.rabbitmq.com/configure.html#config-items) に従って設定を調整してください。
- 消費する場合、消費者が継続的に実行されることを確認し、プロダクション環境では Supervisor を使用してデーモン化してください。
- Linux では `rabbitmqctl list_queues`、Windows では `rabbitmqctl.bat list_queues` を使用してキューをリストアップし、特権ユーザーとして実行してください。詳細については、[RabbitMQ コマンドラインツール](https://www.rabbitmq.com/cli.html) をご覧ください。

#### 表: 主要メソッドのバージョン比較

| メソッド             | バージョン 2.6.* の動作                          | バージョン 3.2 の動作                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | 標準的で、キューに公開                          | 変更なし、同じ使用方法                        |
| `basic_consume`    | 消費のために `wait()` を使用したループが必要       | 似ていますが、`consume()` メソッドが利用可能     |
| `setBodySizeLimit` | 大きなメッセージに対応、設定に応じて切り捨て       | 同じ機能をサポート                          |
| PHP 互換性          | おそらく 5.3 から 7.x                               | PHP 7.x と 8.x をサポート                     |

この表は、消費プロセスの主要な違いを強調しており、バージョン 2.6.* のユーザーにとって重要です。

#### 結論
"php-amqplib/php-amqplib" バージョン 2.6.* を使用するには、標準的な Composer インストールが必要であり、送信は `basic_publish` を使用し、受信は `basic_consume` を使用して手動ループを使用します。新しいバージョンと似ていますが、消費プロセスには追加の注意が必要であり、レガシーシステムに対して開発者がテストし、調整することが重要です。さらに詳しい情報については、公式の RabbitMQ チュートリアルと GitHub リポジトリを参照してください。

---

### 主要な引用
- [GitHub - php-amqplib/php-amqplib RabbitMQ 用の最も広く使用される PHP クライアント](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ チュートリアル - "Hello World!" PHP 例](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP ドキュメント CloudAMQP と PHP を使用して開始](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist 以前は videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG ファイル](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ 設定ガイド 設定項目と設定](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ コマンドラインツール CLI 参照と使用法](https://www.rabbitmq.com/cli.html)