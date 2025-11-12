---
audio: false
generated: true
lang: ja
layout: post
title: PHPでのRabbitMQの使用
translated: true
type: note
---

### 主なポイント
- 「php-amqplib/php-amqplib」バージョン2.6.*を使用するには、Composer経由でインストールし、RabbitMQでのメッセージ送受信の基本的な手順に従う必要があるようです。
- プロセスには、接続の設定、キューの宣言、送信には `basic_publish` を、受信には `basic_consume` とループを使用する方法が含まれ、これは新しいバージョンとは若干異なる可能性があります。
- 調査によると、バージョン2.6.*では、消費プロセスには `consume()` メソッドを使用する可能性のある新しいバージョンとは異なり、`wait()` を使用した手動ループが必要です。

---

### インストールとセットアップ
「php-amqplib/php-amqplib」バージョン2.6.*を始めるには、まずComposerを使用してインストールします。以下のコマンドを実行してください：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

RabbitMQがシステムにインストールされ、実行されていることを確認してください。通常、デフォルトの認証情報（`guest/guest`）で `localhost:5672` でアクセスできます。設定が異なる場合はこれらの設定を調整してください。

### メッセージの送信
メッセージを送信するには、必要なPHPファイルをインクルードし、接続を作成します：

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
受信の場合も同様に設定しますが、メッセージ処理用のコールバックを定義します：

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

バージョン2.6.*では、消費を継続するために `wait()` を含むループが必要であることに注意してください。これは、より単純な `consume()` メソッドを使用する可能性のある新しいバージョンと比較して予期しない詳細です。

---

### 調査ノート: 「php-amqplib/php-amqplib」バージョン2.6.*の詳細な使用方法

このセクションでは、人気のあるメッセージキューシステムであるRabbitMQと対話するための「php-amqplib/php-amqplib」ライブラリ、特にバージョン2.6.*の使用に関する包括的なガイドを提供します。この情報は、公式ドキュメント、チュートリアル、およびバージョン固有の詳細に基づいており、開発者にとって徹底した理解を保証します。

#### 背景とコンテキスト
「php-amqplib/php-amqplib」は、RabbitMQと通信するためのPHPライブラリで、AMQP 0.9.1プロトコルを実装しています。バージョン2.6.*は古いリリースですが、2025年3月時点でライブラリはバージョン3.x.xに進化しています。この特定のバージョンでの使用方法を理解することは、レガシーシステムや特定のプロジェクト要件にとって重要です。このライブラリは、Ramūnas DrongaやLuke Bakkenを含む貢献者によって維持されており、RabbitMQに取り組むVMwareエンジニアの重要な関与があります ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib))。

RabbitMQチュートリアル（公式RabbitMQウェブサイトのものなど）は、一般的に適用可能な例を提供しますが、新しいバージョンを反映している可能性があります。バージョン2.6.*では、特に以下で詳述する消費プロセスにおいて調整が必要です。

#### インストールプロセス
始めるには、PHPの依存関係マネージャーであるComposerを使用してライブラリをインストールします。プロジェクトディレクトリで次のコマンドを実行してください：

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

このコマンドは、ライブラリがダウンロードされ、使用できるように設定され、Composerが依存関係を管理することを保証します。RabbitMQがインストールされ、実行されていることを確認してください。通常、デフォルトの認証情報（`guest/guest`）で `localhost:5672` でアクセスできます。本番環境では、ホスト、ポート、認証情報を必要に応じて調整し、管理ブローカー設定については [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) を参照してください。

#### メッセージの送信: ステップバイステップ
メッセージの送信には、接続の確立とキューへの公開が含まれます。プロセスは以下の通りです：

1. **必要なファイルをインクルード:**
   Composerオートローダーを使用してライブラリをインクルードします：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **接続とチャネルを作成:**
   RabbitMQへの接続を初期化し、チャネルを開きます：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   パラメータはホスト、ポート、ユーザー名、パスワードで、デフォルトは示されている通りです。SSLやその他の設定については、[RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php) を参照してください。

3. **キューを宣言し、公開:**
   キューが存在することを確認するために宣言し、メッセージを公開します：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   ここで、`queue_declare` はデフォルト設定（非永続、非排他、自動削除）で「hello」という名前のキューを作成します。`basic_publish` はメッセージをキューに送信します。

4. **接続を閉じる:**
   送信後、リソースを解放するためにチャネルと接続を閉じます：

   ```php
   $channel->close();
   $connection->close();
   ```

このプロセスはバージョン間で標準的であり、バージョン2.6.*の変更ログでは後のリリースと比較して重要な変更は記載されていません。

#### メッセージの受信: バージョン固有の詳細
バージョン2.6.*でのメッセージ受信は注意深い注意を必要とします。なぜなら、消費メカニズムが新しいバージョンとは異なるからです。詳細なプロセスは以下の通りです：

1. **必要なファイルをインクルード:**
   送信と同様に、オートローダーと必要なクラスをインクルードします：

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **接続とチャネルを作成:**
   以前と同様に接続とチャネルを確立します：

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **キューを宣言:**
   キューが存在することを確認し、送信側の宣言と一致させます：

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **コールバックを定義:**
   受信したメッセージを処理するコールバック関数を作成します：

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   この関数は各メッセージに対して呼び出され、この例では本文を出力します。

5. **メッセージを消費:**
   バージョン2.6.*では、`basic_consume` を使用してコールバックを登録し、消費を継続するためにループに入ります：

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   `basic_consume` メソッドは、キュー名、コンシューマータグ、no-local、no-ack、排他、no-wait、およびコールバックのパラメータを取ります。`wait()` を含むループはコンシューマーを実行し続け、メッセージをチェックします。これは重要な詳細です。なぜなら、新しいバージョン（例：3.2）では `consume()` メソッドを使用する可能性がありますが、APIドキュメントのレビューに基づくと、2.6.*では利用できなかったためです。

6. **接続を閉じる:**
   消費後、リソースを閉じます：

   ```php
   $channel->close();
   $connection->close();
   ```

予期しない詳細は、バージョン2.6.*での手動ループの必要性であり、本番使用では接続問題に対する例外のキャッチなどの追加のエラーハンドリングが必要になる可能性があります。

#### バージョン固有の考慮事項
バージョン2.6.*は古いリリースの一部であり、変更ログに明示的に記載されていませんが、2.5から2.7周辺のバージョンでは、ハートビートサポートやPHP 5.3互換性などの拡張が示されています。大きなメッセージの場合、バージョン2.6.*は、必要に応じてメッセージを切り詰める、チャネル上の `setBodySizeLimit` をサポートしてメモリ制限を処理します。詳細は [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib) にあります。

バージョン3.2と比較すると、変更にはPHP 8サポートや `consume()` のような新しいメソッドが含まれますが、送信と基本的な消費のコア機能は同様のままです。ユーザーは互換性、特にPHPバージョンに関してテストする必要があります。変更ログのエントリによると、2.6.*はおそらくPHP 5.3から7.xをサポートします。

#### トラブルシューティングとベストプラクティス
- 送信が失敗した場合、ディスク容量が50 MBを下回るなどのリソースアラームについてRabbitMQログを確認し、[RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items) 経由で設定を調整してください。
- 消費については、コンシューマーが継続的に実行されることを確認してください。本番環境でのデーモン化にはSupervisorなどのツールを使用します。
- Linuxでは `rabbitmqctl list_queues`、Windowsでは特権ユーザーとして `rabbitmqctl.bat list_queues` を使用してキューをリストします。[RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html) に従ってください。

#### 表: 主要メソッドのバージョン比較

| メソッド             | バージョン2.6.*の動作                          | バージョン3.2の動作                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | 標準的、キューに公開                             | 変更なし、同じ使用方法                         |
| `basic_consume`    | 消費のために `wait()` を含むループが必要            | 同様だが、`consume()` メソッドが利用可能        |
| `setBodySizeLimit` | 大きなメッセージをサポート、設定すると切り詰める     | サポート、同じ機能性                           |
| PHP互換性          | おそらく5.3から7.x                              | PHP 7.x および 8.x をサポート                  |

この表は、バージョン2.6.*ユーザーにとって重要な消費における主要な違いを強調しています。

#### 結論
「php-amqplib/php-amqplib」バージョン2.6.*の使用には、標準的なComposerインストールが含まれ、`basic_publish` 経由でのメッセージ送信と、手動ループを含む `basic_consume` 経由での受信が行われます。新しいバージョンと同様ですが、消費プロセスには追加の注意が必要であり、開発者がレガシーシステム向けにテストおよび調整することが不可欠です。詳細については、公式のRabbitMQチュートリアルとGitHubリポジトリを参照してください。

---

### 主要な引用文献
- [GitHub - php-amqplib/php-amqplib The most widely used PHP client for RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [RabbitMQ tutorial - "Hello World!" PHP example](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [CloudAMQP PHP Documentation Get started with CloudAMQP and PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Formerly videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib CHANGELOG file](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [RabbitMQ Configuration Guide Config items and settings](https://www.rabbitmq.com/configure.html#config-items)
- [RabbitMQ Command Line Tools CLI reference and usage](https://www.rabbitmq.com/cli.html)