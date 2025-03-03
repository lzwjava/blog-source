---
audio: false
generated: true
lang: ja
layout: post
title: PHP用Piliストリーミングクラウドライブラリ
translated: true
---

### 主要ポイント
- "pili-engineering/pili-sdk-php": "dev-master"を使用するには、Composerを通じてインストールし、Qiniuの認証情報を設定する必要があるように見えます。
- このパッケージはPHP 5.3.0以上が必要で、Qiniuに関連するPili Streaming Cloud用です。
- Hubオブジェクトを作成し、RTMP URLの生成などのストリーム操作を行うことが推奨されていますが、具体的なメソッドは異なる場合があります。

### インストール
まず、Composerがインストールされていることを確認してください。`composer.json`ファイルに以下のようにパッケージを追加します：
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
次に、ターミナルで`composer install`または`composer update`を実行します。PHPスクリプトで以下のようにインクルードします：
```php
require 'vendor/autoload.php';
```

### 設定と使用方法
QiniuアカウントとPili Hubが必要です。アクセスキー、シークレットキー、Hub名を設定し、Hubオブジェクトを作成します：
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
ストリームを作成または取得し、例えば`$stream->rtmpPublishUrl(60)`のようなメソッドを使用します。

### 予期せぬ詳細
"dev-master"は開発バージョンであり、安定性が低い可能性があります。1.5.5などのタグ付きバージョンがプロダクション用に利用可能です。

---

### "pili-engineering/pili-sdk-php": "dev-master"の使用に関する包括的なガイド

このガイドは、利用可能なドキュメントと例に基づいて、"pili-engineering/pili-sdk-php"パッケージの"dev-master"バージョンを使用する方法について詳細に説明します。インストール、設定、使用、追加の考慮事項を含み、Pili Streaming Cloudサービスを利用する開発者にとっての包括的な理解を提供します。

#### 背景とコンテキスト
"pili-engineering/pili-sdk-php"パッケージは、PHP用のサーバーサイドライブラリで、Qiniu（クラウドストレージおよびCDNプロバイダー）に関連するPili Streaming Cloudと対話するために設計されています。"dev-master"バージョンは最新の開発ブランチを指し、新しい機能を含む可能性がありますが、タグ付きリリースよりも安定性が低いかもしれません。このパッケージはPHP 5.3.0以上が必要であり、2025年3月3日現在の多くのPHP環境で利用可能です。

#### インストール手順
まず、Composerがインストールされている必要があります。これはPHPの依存関係管理ツールです。インストールには、プロジェクトの`composer.json`ファイルにパッケージを追加し、Composerコマンドを実行してダウンロードする必要があります。具体的には：

- `composer.json`の"require"セクションに以下を追加します：
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- ターミナルで`composer install`または`composer update`を実行してパッケージとその依存関係を取得します。これにより、`vendor`ディレクトリが作成され、必要なファイルが含まれます。
- PHPスクリプトで、パッケージクラスにアクセスするためにオートローダーをインクルードします：
  ```php
  require 'vendor/autoload.php';
  ```

このプロセスにより、パッケージがプロジェクトに統合され、Composerのオートローディングを利用してクラスに簡単にアクセスできます。

#### 前提条件と設定
SDKを使用する前に、Qiniuアカウントが必要であり、Pili Hubを設定する必要があります。これは、SDKがPili Streaming Cloudサービスと対話するために必要な認証情報を取得するためです。ドキュメントには、これらの認証情報が認証に必要であることが示されています。

設定には、PHPスクリプトで認証情報を定義します：
- アクセスキー：Qiniuのアクセスキー。
- シークレットキー：Qiniuのシークレットキー。
- Hub名：Pili Hubの名前で、使用前に存在する必要があります。

設定の例は以下の通りです：
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Hubオブジェクトの作成と使用
SDKの核はHubオブジェクトであり、ストリーム管理を容易にします。まず、Qiniuキーを使用してCredentialsオブジェクトを作成します：
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
次に、これらの認証情報とHub名を使用してHubオブジェクトをインスタンス化します：
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
このHubオブジェクトを使用して、ストリームに関連するさまざまな操作を行うことができます。例えば、新しいストリームを作成するには：
```php
$streamKey = 'your_stream_key'; // ハブ内で一意である必要があります
$stream = $hub->createStream($streamKey);
```
既存のストリームを取得するには：
```php
$stream = $hub->getStream($streamKey);
```
ストリームオブジェクトは、以下の表に示すように、さまざまな操作を行うためのメソッドを提供します。これは、利用可能なドキュメントに基づいています：

| **操作**          | **メソッド**                     | **説明**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| ストリームの作成          | `$hub->createStream($key)`     | 指定されたキーで新しいストリームを作成します。             |
| ストリームの取得             | `$hub->getStream($key)`        | キーで既存のストリームを取得します。                 |
| ストリームのリスト表示           | `$hub->listStreams($marker, $limit, $prefix)` | ページネーションオプション付きでストリームをリスト表示します。               |
| RTMP発行URL       | `$stream->rtmpPublishUrl($expire)` | 有効期限付きのRTMP発行URLを生成します。  |
| RTMP再生URL          | `$stream->rtmpPlayUrl()`       | ストリームのRTMP再生URLを生成します。           |
| HLS再生URL           | `$stream->hlsPlayUrl()`        | ストリーミング用のHLS再生URLを生成します。             |
| ストリームの無効化         | `$stream->disable()`           | ストリームを無効にします。                                 |
| ストリームの有効化          | `$stream->enable()`            | ストリームを有効にします。                                  |
| ストリームのステータス取得      | `$stream->status()`            | ストリームの現在のステータスを取得します。          |

例えば、60秒の有効期限付きのRTMP発行URLを生成するには：
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
このURLは、Pili Streaming Cloudにストリームを発行するために使用でき、有効期限は一時的なアクセスを確保します。

#### 追加の考慮事項
- **バージョンの安定性**："dev-master"バージョンは開発ブランチであり、安定性が低いかもしれません。プロダクションでは、Packagistの[pili-engineering/pili-sdk-phpバージョン](https://packagist.org/p/pili-engineering/pili-sdk-php)で利用可能なタグ付きバージョン、例えば1.5.5を使用することを検討してください。履歴には、APIの追加やメソッドの精緻化などの更新が含まれており、バージョンは2016年から存在しています。
- **エラーハンドリング**：ドキュメントには、ストリームの作成や取得などの操作に対してtry-catchブロックを使用することが示されています。
- **ドキュメントと例**：具体的な例は詳細に説明されていませんが、GitHubリポジトリ[Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php)にはインストール手順と機能リストが含まれており、Pythonなど他の言語のSDKと比較すると、URL生成などの類似の機能が示されています。

#### 比較的な洞察
他のPili SDK（例えばPythonバージョン）と比較すると、類似のパターンが見られます：両方とも認証情報、Hubの設定、ストリーム操作が必要です。ただし、PHPバージョンはHubとStreamクラスを使用したオブジェクト指向アプローチを採用しており、Pythonのより機能的なスタイルとは対照的です。これはPHPの一般的な開発実践に合致し、型の安全性とIDEサポートを提供します。

#### 結論
"pili-engineering/pili-sdk-php": "dev-master"を使用するには、Composerを通じてインストールし、Qiniuの認証情報を設定し、Hubオブジェクトを作成し、`rtmpPublishUrl`などのメソッドを使用してストリームを管理します。PHP 5.3.0以上の環境が必要であることを確認し、プロダクション用には安定性を考慮してください。このガイドは、公式ドキュメントとリポジトリでさらに詳細を確認できる包括的なスタートポイントを提供します。

### 主要な引用
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-phpバージョン Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)