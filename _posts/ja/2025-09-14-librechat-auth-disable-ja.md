---
audio: false
date: 2025-09-14
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: LibreChat認証回避の無効化
translated: true
type: note
---

短い答え：LibreChatで認証を完全にオフにすることはできませんが、「ログインを繰り返し求められる」問題を止め、「ログイン不要」に近い状態にすることは可能です。実際に機能する方法（とその理由）を以下に示します：

### 1) 認証を完全には無効化できない

これはメンテナーによって確認されています：登録は無効化できますが、認証システム自体をオフにすることはできません（[GitHub][1]）

### 2) ログアウトされ続ける理由

**HTTP**（例：LAN IP）でインスタンスにアクセスすると、本番環境ではCookieに`secure`マークが付けられるため、ブラウザがCookieを保持せず、ログイン画面に戻されます。**HTTPS**（自己署名証明書でも可）を使用するか、APIをセキュアCookieを無効にする開発モードで実行してください（[GitHub][1]）

### 3) 2つの確実な修正方法

#### オプションA — 適切/安全（推奨）

* LibreChatをHTTPSの背後に配置（nginx/caddy/traefik；LAN上では自己署名証明書でも可）
* 次に、`.env`でセッション期間を延長：

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24時間
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30日
  ```
* env変更後、コンテナを再起動
  これにより数日/数週間ログイン状態が維持され、Cookieの消失が修正されます（[GitHub][2]）

#### オプションB — 「プライベートLAN上で、ログアウトを止めたいだけ」

* `docker-compose.override.yml`を作成し、APIを開発モードで実行（セキュアCookieを無効化）：

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* `docker compose up -d`で適用
  これは安全性が低い（Cookieが`secure`ではない）ですが、プレーンHTTP経由での強制再ログインを止めます（[librechat.ai][3]）

### 4) オプションの利便性向上設定

* **新規サインアップを無効化**して実質的にシングルユーザー化：

  ```
  ALLOW_REGISTRATION=false
  ```

  （必要に応じて`npm run create-user`でユーザーを追加可能）（[librechat.ai][4]）
* 最もシンプルなログイン経路を希望する場合は、`.env`の他の認証トグル（メール/ソーシャルログインフラグ）を保持（[librechat.ai][5]）

### 5) あなたのケース向けクイックチェックリスト（v0.8.0-rc3）

1. 決定：HTTPSプロキシ（最良）**または**開発モード（LAN向け簡易修正）
2. `.env`でより長い`SESSION_EXPIRY`と`REFRESH_TOKEN_EXPIRY`を設定
3. env変更を有効にするためスタックを再起動
4. （オプション）「シングルユーザー」感覚にするため登録をオフ

希望であれば、現在の`docker-compose.yml`と`.env`（シークレットなし）を貼り付けてください。あなたの設定に追加/変更すべき箇所を正確にマークします。

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"