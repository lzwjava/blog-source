---
audio: false
generated: true
lang: ja
layout: post
title: PHP用Piliストリーミングクラウドライブラリ
translated: true
type: note
---

### 主なポイント
- "pili-engineering/pili-sdk-php": "dev-master" を使用するには、Composer 経由でインストールし、Qiniu の認証情報を設定する必要があるようです。
- 調査によると、このパッケージは PHP 5.3.0 以上を必要とし、Qiniu に関連する Pili Streaming Cloud 用です。
- 証拠から、Hub オブジェクトを作成し、RTMP URL の生成などのストリーム操作を使用する傾向がありますが、正確な方法は異なる場合があります。

### インストール
まず、Composer がインストールされていることを確認してください。パッケージを `composer.json` ファイルに追加します：
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
次に、`composer install` または `composer update` を実行します。PHP スクリプトで以下をインクルードします：
```php
require 'vendor/autoload.php';
```

### セットアップと使用方法
Qiniu アカウントと Pili Hub が必要です。アクセスキー、シークレットキー、ハブ名を設定し、Hub オブジェクトを作成します：
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
ストリームを作成または取得します（例：`$stream = $hub->createStream('your_stream_key');`）。操作には `$stream->rtmpPublishUrl(60)` などのメソッドを使用します。

### 予期しない詳細
"dev-master" は開発バージョンであり、潜在的に不安定であることに注意してください。本番環境では 1.5.5 などのタグ付きバージョンが利用可能です。

---

### "pili-engineering/pili-sdk-php": "dev-master" 使用に関する包括的ガイド

このガイドでは、利用可能なドキュメントと例に基づき、"pili-engineering/pili-sdk-php" パッケージを "dev-master" バージョンで使用する方法について詳細に探求します。インストール、セットアップ、使用方法、および追加の考慮事項をカバーし、Pili Streaming Cloud サービスを扱う開発者の理解を深めます。

#### 背景とコンテキスト
"pili-engineering/pili-sdk-php" パッケージは、クラウドストレージおよび CDN プロバイダーである Qiniu に関連するサービス、Pili Streaming Cloud と対話するために設計された PHP 用サーバーサイドライブラリです。"dev-master" バージョンは最新の開発ブランチを指し、最近の機能を含む可能性がありますが、タグ付きリリースよりも不安定である可能性があります。このパッケージは PHP 5.3.0 以上を必要とし、2025年3月3日現在、多くの PHP 環境で利用可能です。

#### インストールプロセス
開始するには、PHP の依存関係マネージャーである Composer がインストールされている必要があります。インストールには、プロジェクトの `composer.json` ファイルにパッケージを追加し、Composer コマンドを実行してダウンロードすることが含まれます。具体的には：

- 以下を `composer.json` の "require" セクションに追加します：
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- ターミナルで `composer install` または `composer update` を実行して、パッケージとその依存関係を取得します。これにより、必要なファイルを含む `vendor` ディレクトリが作成されます。
- PHP スクリプトで、パッケージクラスにアクセスするためにオートローダーをインクルードします：
  ```php
  require 'vendor/autoload.php';
  ```

このプロセスにより、Composer のオートローディングを利用して、プロジェクトにパッケージが統合され、クラスへの簡単なアクセスが可能になります。

#### 前提条件とセットアップ
SDK を使用する前に、Qiniu アカウントが必要であり、Pili Hub を設定する必要があります。SDK は Pili Streaming Cloud サービスと対話するためです。これには、Qiniu からアクセスキーとシークレットキーを取得し、そのプラットフォーム内にハブを作成することが含まれます。ドキュメントによると、これらの認証情報は認証に不可欠です。

セットアップするには、PHP スクリプトで認証情報を定義します：
- アクセスキー：あなたの Qiniu アクセスキー。
- シークレットキー：あなたの Qiniu シークレットキー。
- ハブ名：使用前に存在する必要がある Pili Hub の名前。

セットアップの例は以下のようになります：
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Hub オブジェクトの作成と使用
SDK の核心は、ストリーム管理を容易にする Hub オブジェクトです。まず、Qiniu キーを使用して Credentials オブジェクトを作成します：
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
次に、これらの認証情報とハブ名を使用して Hub オブジェクトをインスタンス化します：
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
この Hub オブジェクトにより、ストリームの作成、取得、リスト表示など、さまざまなストリーム関連の操作を実行できます。

#### ストリームの操作
ストリームは Pili Streaming Cloud の中心であり、SDK は Hub オブジェクトを介してそれらを管理するメソッドを提供します。新しいストリームを作成するには：
```php
$streamKey = 'your_stream_key'; // ハブ内で一意である必要があります
$stream = $hub->createStream($streamKey);
```
既存のストリームを取得するには：
```php
$stream = $hub->getStream($streamKey);
```
ストリームオブジェクトは、その後、操作のためのさまざまなメソッドを提供します。利用可能なドキュメントに基づく詳細を以下の表に示します：

| **操作**               | **メソッド**                      | **説明**                                             |
|-------------------------|-----------------------------------|-----------------------------------------------------|
| ストリーム作成         | `$hub->createStream($key)`        | 指定されたキーで新しいストリームを作成します。      |
| ストリーム取得         | `$hub->getStream($key)`           | キーで既存のストリームを取得します。                |
| ストリーム一覧         | `$hub->listStreams($marker, $limit, $prefix)` | ページネーションオプションでストリームを一覧表示します。 |
| RTMP 公開 URL          | `$stream->rtmpPublishUrl($expire)`| 有効期限付きの RTMP 公開 URL を生成します。         |
| RTMP 再生 URL          | `$stream->rtmpPlayUrl()`          | ストリームの RTMP 再生 URL を生成します。           |
| HLS 再生 URL           | `$stream->hlsPlayUrl()`           | ストリーミング用の HLS 再生 URL を生成します。      |
| ストリーム無効化       | `$stream->disable()`              | ストリームを無効にします。                          |
| ストリーム有効化       | `$stream->enable()`               | ストリームを有効にします。                          |
| ストリームステータス取得 | `$stream->status()`              | ストリームの現在のステータスを取得します。          |

例えば、60秒の有効期限を持つ RTMP 公開 URL を生成するには：
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
この URL は、Pili Streaming Cloud にストリームを公開するために使用でき、有効期限により一時的なアクセスが保証されます。

#### 追加の考慮事項
- **バージョンの安定性**: "dev-master" バージョンは開発ブランチであり、潜在的に不安定です。本番環境では、Packagist [pili-engineering/pili-sdk-php versions](https://packagist.org/p/pili-engineering/pili-sdk-php) で利用可能な 1.5.5 などのタグ付きバージョンの使用を検討してください。履歴には、API の追加やメソッドの改良などの更新が示されており、バージョンは 2016 年にさかのぼります。
- **エラーハンドリング**: ドキュメントでは、ストリーム作成および取得の例で見られるように、潜在的な例外を処理するために try-catch ブロックの使用が示唆されています。
- **ドキュメントと例**: 具体的な例は広範に詳細化されていませんでしたが、GitHub リポジトリ [Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php) にはインストール手順と機能一覧が提供されており、他の言語の SDK（例：Python）との比較は、URL 生成などの類似の機能を示しています。

#### 比較考察
Python バージョンなどの他の Pili SDK と比較すると、同様のパターンが明らかになります：両方とも認証情報、ハブのセットアップ、およびストリーム操作を必要とします。ただし、PHP バージョンは Hub および Stream クラスを使用したオブジェクト指向アプローチを使用し、Python のより機能的なスタイルとは対照的です。これは、型安全性と IDE サポートを提供する PHP の典型的な開発慣行に沿っています。

#### 結論
"pili-engineering/pili-sdk-php": "dev-master" の使用には、Composer 経由でのインストール、Qiniu 認証情報の設定、Hub オブジェクトの作成、および `rtmpPublishUrl` などのメソッドを使用したストリームの管理が含まれます。環境が PHP 5.3.0+ の要件を満たしていることを確認し、本番使用における安定性を考慮してください。このガイドは包括的な出発点を提供し、詳細は公式ドキュメントおよびリポジトリで利用可能です。

### 主な引用文献
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php versions Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)