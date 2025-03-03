---
audio: false
generated: true
lang: ja
layout: post
title: Qiniu PHP SDK
translated: true
---

PHPで`"qiniu/php-sdk": "^7.0"`を使用するには、プロジェクトにQiniu PHP SDKを統合する必要があります。このSDKを使用すると、Qiniuクラウドストレージサービス（ファイルのアップロード、バケットの管理など）とやり取りできます。以下は、始めるためのステップバイステップのガイドです。

---

### 1. Qiniu PHP SDKのインストール
SDKをインストールする推奨方法は、PHPの依存関係管理ツールであるComposerを使用することです。システムにComposerがインストールされていることを確認してください。

#### ステップ:
- ターミナルを開き、プロジェクトディレクトリに移動します。
- 次のコマンドを実行して、Qiniu PHP SDK（バージョン7.x）をプロジェクトに追加します：
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- ComposerはSDKとその依存関係を`vendor/`ディレクトリにダウンロードし、自動読み込みファイルを生成します。

Composerがインストールされていない場合は、[getcomposer.org](https://getcomposer.org/)からダウンロードできます。

---

### 2. プロジェクトの設定
インストール後、PHPスクリプトでSDKクラスを使用するために、自動読み込みを含める必要があります。

#### 例:
プロジェクトディレクトリにPHPファイル（例：`index.php`）を作成し、次の行を先頭に追加します：
```php
require_once 'vendor/autoload.php';
```

これにより、必要なときにSDKクラスが自動的に読み込まれます。

---

### 3. 認証の設定
Qiniu SDKを使用するには、Qiniuアカウントダッシュボードから取得した`AccessKey`と`SecretKey`が必要です。

#### 例:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

`'YOUR_ACCESS_KEY'`と`'YOUR_SECRET_KEY'`を実際の資格情報に置き換えてください。

---

### 4. 基本的な使用方法：ファイルのアップロード
Qiniu SDKを使用して行う最も一般的なタスクの一つは、ファイルをバケットにアップロードすることです。以下は、ローカルファイルをアップロードする方法の例です。

#### 例:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Qiniuバケット名に置き換えてください
$filePath = '/path/to/your/file.txt'; // アップロードしたいファイルのパス
$key = 'file.txt'; // Qiniuストレージ内でのファイル名（nullに設定すると、元のファイル名を使用）

$token = $auth->uploadToken($bucket); // アップロードトークンを生成
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "アップロードに失敗しました: " . $error->message();
} else {
    echo "アップロードに成功しました！ファイルハッシュ: " . $ret['hash'];
}
```

- `$bucket`：Qiniuバケットの名前。
- `$filePath`：アップロードしたいローカルファイルのパス。
- `$key`：Qiniuで保存されるファイルキー（名前）。nullに設定すると、Qiniuはファイルのハッシュに基づいてキーを生成します。
- `$token`：資格情報とバケット名を使用して生成されたアップロードトークン。
- `putFile`メソッドは配列を返します：`$ret`（成功情報）と`$error`（エラー情報、存在する場合）。

---

### 5. 追加機能
Qiniu PHP SDKには、以下のような他の機能も提供されています：
- **バケットの管理**：`Qiniu\Storage\BucketManager`を使用して、ファイルのリスト表示、削除、バケット設定の管理を行います。
- **ファイル操作**：バケット内のファイルをコピー、移動、または削除します。
- **画像処理**：リサイズされたまたはフォーマットされた画像のURLを生成します。

#### 例：バケット内のファイルのリスト表示
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "エラー: " . $error->message();
} else {
    echo "バケット内のファイル:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. エラーハンドリング
SDK操作の後、`$error`変数を常に確認してください。操作が失敗した場合、`$error`には何が間違ったかの詳細が含まれます。

#### 例:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. 要件
- PHPバージョン：SDKバージョン`^7.0`はPHP 5.3.3以降（後続のリリースではPHP 8.xまで）をサポートします。
- 拡張機能：SDKは`cURL`および`xml` PHP拡張機能が必要です。

PHPバージョンと拡張機能を確認するには、以下を実行します：
```bash
php -v
php -m
```

---

### 8. 次に進む場所
- **ドキュメント**：詳細については、[公式Qiniu PHP SDKドキュメント](https://developer.qiniu.com/kodo/sdk/php)または[GitHubリポジトリ](https://github.com/qiniu/php-sdk)を参照してください。
- **例**：GitHubリポジトリの`examples/`ディレクトリに、他の使用例を確認できます。
- **サポート**：問題が発生した場合は、Qiniuサポートにチケットを提出するか、コミュニティフォーラムで質問してください（<support@qiniu.com>）。

---

### 完全な例コード
ファイルをアップロードする完全なスクリプトは以下の通りです：
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
    echo "アップロードに失敗しました: " . $error->message();
} else {
    echo "アップロードに成功しました！ファイルハッシュ: " . $ret['hash'];
}
```

プレースホルダー値（`YOUR_ACCESS_KEY`、`YOUR_SECRET_KEY`、`YOUR_BUCKET_NAME`、`/path/to/your/file.txt`）を実際のデータに置き換えると、完了です！

特定の機能でお手伝いが必要な場合は、お知らせください！