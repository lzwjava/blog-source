---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Alipay SDK PHP統合ガイド
translated: true
type: note
---

### 前提条件
PHPでAlipay SDKを統合するには、以下が必要です：
- 有効なAlipayマーチャントアカウント（https://open.alipay.com で登録）
- RSAキーペア：サーバー用の秘密鍵を生成し、公開鍵をAlipayにアップロードして取引に署名
- PHP 5.6以上（セキュリティ向上のため7.x推奨）、cURLやOpenSSLなどの拡張機能が有効
- Alipay公式GitHub（例：https://github.com/alipay/alipay-sdk-php）からAlipay SDKをダウンロード。提供されたコードスニペットは古いバージョン（2016年頃）用です。最新SDKはAlipay Trade APIなど新しいAPIを使用します。レガシーモバイルセキュリティペイを使用している場合は動作する可能性がありますが、非推奨です。

### SDKのセットアップ
1. **ダウンロードとインクルード**：AlipayのデベロッパーポータルまたはGitHubからSDK ZIPをダウンロード。プロジェクトディレクトリ（例：`vendor/alipay-sdk`）に展開します。
2. **ファイルのインクルード**：PHPスクリプトでメインSDKファイルをインクルード、例：
   ```php
   require_once 'path/to/alipay-sdk/AopClient.php'; // 最新SDK用
   ```
   スニペットのレガシーバージョンの場合は、`AopSdk.php`のようなカスタムインクルードが必要な場合があります。

3. **キーとアカウントの設定**：
   - OpenSSLコマンドまたはオンラインツールを使用してRSAキー（2048ビット）を生成。例：
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - スニペットに示されているように`$config`配列を入力：
     - `partner`：AlipayパートナーID（2088で始まる16桁）
     - `private_key`：PEMエンコードされた秘密鍵（-----BEGIN PRIVATE KEY-----などのヘッダーなし）
     - `alipay_public_key`：Alipayの公開鍵（Alipayコンソールからコピー）
     - その他のフィールド：`transport`にHTTPSを使用し、SSL検証用に`cacert.pem`（Alipayドキュメントからダウンロード）をスクリプトディレクトリに配置

### SDKの初期化
AopClientインスタンスを作成し、設定を渡します：
```php
use Orvibo\AopSdk\AopClient; // SDKバージョンに合わせて名前空間を調整

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // 本番URL
$aopClient->appId = 'your_app_id'; // 新しいSDKはpartnerの代わりにappIdを使用
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // 最新SDKはRSA2を推奨
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

スニペットのレガシーモバイルペイの場合は、`AlipaySign`などの古いクラスを使用します。

### 支払いリクエストの実行
1. **リクエストパラメータの構築**：
   ```php
   $request = new AlipayTradeAppPayRequest(); // またはSDKバージョンに応じた類似クラス
   $request->setBizContent("{" .
       "\"body\":\"テスト取引\"," .
       "\"subject\":\"テスト件名\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // 通知URL
   ```

2. **リクエストの実行**：
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // この署名済み文字列はアプリのAlipay SDKで使用
   ```

3. **モバイルアプリでの処理（アプリ連携の場合）**：レスポンスをアプリのネイティブAlipay SDK（Android/iOS）に渡して支払いを完了

### 通知とレスポンスの処理
- **非同期通知**：`notify_url`にコールバックPHPスクリプトを設定してAlipayの通知を検証
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // 署名を検証
  // 支払いステータスを処理（例：データベースを更新）
  ```
- **同期リターン**：支払い後、Alipayは`return_url`（設定されている場合）にリダイレクト

### テストとデプロイメント
- テストにはAlipayのサンドボックス環境を使用：https://openhome.alipay.com/platform/devEnv.htm
- 一般的な問題：キーが正しくフォーマットされていることを確認（余分な行なし）。セキュリティ向上のためRSA2を使用
- セキュリティのヒント：キーは安全に保管（バージョン管理システムに含めない）。改ざん防止のため常に署名を検証

これが古いSDK用の場合は、機能とセキュリティ向上のためAlipayの最新PHP SDK（例：Composerで`composer require alipay/openapisdk`）へのアップグレードを検討してください。詳細なドキュメントは https://docs.open.alipay.com/ を参照。エラーが発生した場合は、コードとログを共有してトラブルシューティングを行ってください。