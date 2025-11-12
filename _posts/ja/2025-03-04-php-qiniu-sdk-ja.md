---
audio: false
generated: true
lang: ja
layout: post
title: 七牛PHP SDK
translated: true
type: note
---

PHPで`"qiniu/php-sdk": "^7.0"`を使用するには、Qiniu PHP SDKをプロジェクトに統合する必要があります。このSDKを使用すると、ファイルのアップロード、バケットの管理など、Qiniu Cloud Storageサービスと連携できます。以下に、始めるためのステップバイステップガイドを示します：

---

### 1. Qiniu PHP SDKのインストール
SDKをインストールする推奨方法は、PHPの依存関係管理ツールであるComposerを使用することです。システムにComposerがインストールされていることを確認してください。

#### 手順：
- ターミナルを開き、プロジェクトディレクトリに移動します。
- 以下のコマンドを実行して、Qiniu PHP SDK（バージョン7.x）をプロジェクトに追加します：
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- ComposerはSDKとその依存関係を`vendor/`ディレクトリにダウンロードし、オートロードファイルを生成します。

Composerがインストールされていない場合は、[getcomposer.org](https://getcomposer.org/)からダウンロードできます。

---

### 2. プロジェクトのセットアップ
インストール後、SDKクラスを使用するために、PHPスクリプトにオートローダーを含める必要があります。

#### 例：
プロジェクトディレクトリにPHPファイル（例：`index.php`）を作成し、先頭に以下の行を追加します：
```php
require_once 'vendor/autoload.php';
```

これにより、必要なときにSDKクラスが自動的にロードされます。

---

### 3. 認証の設定
Qiniu SDKを使用するには、Qiniuアカウントのダッシュボードから取得できるQiniuの`AccessKey`と`SecretKey`が必要です。

#### 例：
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

`'YOUR_ACCESS_KEY'`と`'YOUR_SECRET_KEY'`を実際の認証情報に置き換えてください。

---

### 4. 基本的な使用法：ファイルのアップロード
Qiniu SDKで最も一般的なタスクの1つは、ファイルをバケットにアップロードすることです。以下は、ローカルファイルをアップロードする方法の例です。

#### 例：
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Qiniuバケット名に置き換えてください
$filePath = '/path/to/your/file.txt'; // アップロードするファイルへのパス
$key = 'file.txt'; // Qiniuストレージでのファイル名（元のファイル名を使用する場合はnullにできます）

$token = $auth->uploadToken($bucket); // アップロードトークンを生成
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

- `$bucket`: Qiniuバケットの名前。
- `$filePath`: アップロードするファイルのローカルパス。
- `$key`: Qiniuに保存されるファイルキー（名前）。`null`に設定すると、Qiniuはファイルのハッシュに基づいてキーを生成します。
- `$token`: 認証情報とバケット名を使用して生成されたアップロードトークン。
- `putFile`メソッドは配列を返します：`$ret`（成功情報）と`$error`（エラー情報、存在する場合）。

---

### 5. 追加機能
Qiniu PHP SDKは、他にも多くの機能を提供します：
- **バケットの管理**: `Qiniu\Storage\BucketManager`を使用して、ファイルのリスト表示、削除、またはバケット設定の管理を行います。
- **ファイル操作**: バケット内のファイルのコピー、移動、削除。
- **画像処理**: サイズ変更またはフォーマットされた画像のURLを生成。

#### 例：バケット内のファイルのリスト表示
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Error: " . $error->message();
} else {
    echo "Files in bucket:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. エラーハンドリング
SDK操作後は常に`$error`変数を確認してください。操作が失敗した場合、`$error`には何が問題だったかの詳細が含まれます。

#### 例：
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. 要件
- PHPバージョン：SDKバージョン`^7.0`は、PHP 5.3.3以上（後のリリースではPHP 8.xまで）をサポートします。
- 拡張機能：SDKで必要とされる`cURL`および`xml` PHP拡張機能が有効になっていることを確認してください。

以下のコマンドでPHPバージョンと拡張機能を確認できます：
```bash
php -v
php -m
```

---

### 8. 次のステップ
- **ドキュメント**: 詳細については、[公式Qiniu PHP SDKドキュメント](https://developer.qiniu.com/kodo/sdk/php)または[GitHubリポジトリ](https://github.com/qiniu/php-sdk)を参照してください。
- **例**: その他のユースケースについては、GitHubリポジトリの`examples/`ディレクトリを確認してください。
- **サポート**: 問題が発生した場合は、Qiniuサポート（<support@qiniu.com>）にチケットを送信するか、コミュニティフォーラムで質問してください。

---

### 完全なサンプルコード
以下は、ファイルをアップロードするための完全なスクリプトです：
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
    echo "Upload failed: " . $error->message();
} else {
    echo "Upload successful! File hash: " . $ret['hash'];
}
```

プレースホルダーの値（`YOUR_ACCESS_KEY`、`YOUR_SECRET_KEY`、`YOUR_BUCKET_NAME`、`/path/to/your/file.txt`）を実際のデータに置き換えれば、準備完了です！

特定の機能についてヘルプが必要な場合はお知らせください！