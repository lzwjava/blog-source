---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: GitHub Copilot認証フロー
translated: true
type: note
---

良い質問です — GitHub Copilotの認証フローは、基本的には標準的な **OAuth2 デバイスコードグラント** ですが、Copilotサービス自体のためにGitHub固有のトークンが追加されています。ステップバイステップで説明します：

---

### 1. **デバイスフロー (`/login/device/code`)**

* 初回ログイン時、Copilotクライアント（例：VS Code拡張機能、JetBrainsプラグイン、CLI）はGitHubのOAuthエンドポイントを呼び出します：

  ```
  POST https://github.com/login/device/code
  ```
* **client_id** (GitHub Copilot専用のもの) を送信します。
* GitHubからの応答：

  * `device_code` (ポーリングに使用される内部コード)、
  * `user_code` (ブラウザで表示され入力するコード)、
  * `verification_uri` (コードを入力するためのURL)、
  * `interval` (クライアントがポーリングする間隔)。

---

### 2. **アクセストークンのポーリング**

* Copilotクライアントは次にポーリングします：

  ```
  POST https://github.com/login/oauth/access_token
  ```
* `device_code` と `client_id` を含めます。
* ブラウザで承認が完了すると、GitHubは以下を返します：

  * `access_token` (Copilot利用のためにスコープされた**GitHub OAuthトークン**)、
  * `token_type=bearer`、
  * `expires_in` (有効期限)。

この `access_token` は**通常のGitHub OAuth2トークン**です。

---

### 3. **`copilot_internal` トークンへの交換**

* Copilotクライアントは、GitHub OAuthトークンを直接Copilot APIの呼び出しに使用できません。
* 代わりに、Copilotサービスと交換します：

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* 応答は以下の通り：

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* この **`copilot_internal` v2トークン** が、Copilotクライアントが **Copilot推論サービス** (例: `https://copilot-proxy.githubusercontent.com`) と通信するために使用するものです。

---

### 4. **`copilot_internal` トークンの使用**

* 後続のすべての補完やチャットリクエストは、以下で認証されます：

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* このトークンは有効期間が短く（通常約1時間）、あなたのGitHubアカウントとCopilotサブスクリプションステータスに紐づいています。
* クライアントは、GitHub OAuthアクセストークンを再交換することで定期的にこれを更新します。

---

✅ **まとめ:**

* `/login/device/code` → ブラウザで認証するためのコードを取得。
* `/login/oauth/access_token` → GitHub OAuthトークンを取得。
* `/copilot_internal/v2/token` → それを短命のCopilotトークンと交換。これが補完に使用される*実際の*資格情報。

---

**実際のリクエスト/レスポンス例**（ヘッダーとサンプルJSONを含む）も示して、ペイロードが実際にどのように見えるか確認してみませんか？