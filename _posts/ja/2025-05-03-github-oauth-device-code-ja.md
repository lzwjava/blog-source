---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: GitHub OAuth デバイスコードフロー
translated: true
type: note
---

### 概要

このJavaScriptコードは、GitHubでの認証とアクセストークンの取得のためにOAuth 2.0デバイス認証グラントフロー（デバイスコードグラントとも呼ばれる）を実装しています。このフローは、ユーザーが認証を承認するためにWebブラウザと直接対話できないヘッドレスアプリケーション（CLIツールや組み込みシステムなど）で一般的に使用されます。

この特定のケースでは、GitHub Copilotプラグイン（NeovimやVim用など）からのリクエストを模倣しているように見え、GitHubの認証システムとの統合やアクセスを可能にするためにCopilotクライアントを偽装するヘッダーを使用しています。目標は、ユーザー認証を必要とするGitHub APIコール（`scope: "read:user"` で示されるようにユーザー情報の読み取りなど）に使用できるアクセストークンを生成することです。

このコードはNode.jsスクリプトとして実行され、HTTPリクエストに `fetch` を、環境変数に `process` を使用します。Node.jsが `fetch` を利用可能であることを前提としています（新しいバージョンまたはポリフィル経由）。成功すると、ユーザーがリクエストを承認するか、タイムアウトするまでGitHubのサーバーをポーリングします。

**重要な注意点:**
- このコードでは、環境変数 `MY_COPILOT_CLIENT_ID` の設定が必要です。これはGitHub Copilot用に登録されたGitHub OAuth AppのクライアントIDである可能性があります。
- エラー処理は最小限です。例えば、fetchが失敗した場合、ログを出力して継続するか終了します。
- セキュリティ的には、アクセストークンの保存やログ出力は危険です（APIアクセス権限を付与します）。このコードは完全なトークンオブジェクトをコンソールに直接出力しており、実際の使用ではプライバシー/セキュリティ上の問題となる可能性があります。アクセストークンは安全に扱う必要があります（例えば、暗号化して保存し、ローテーションする）。
- このフローにはユーザーの操作が含まれます：ユーザーはURLにアクセスし、GitHubのサイトでコードを入力して承認する必要があります。
- これはGitHubの公式ドキュメントのコードではありません。GitHub Copilotの動作からリバースエンジニアリングされたように見えます。APIはGitHubの利用規約に従って責任を持って使用してください。

### ステップバイステップの詳細

#### 1. 環境チェック
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- 環境変数から `MY_COPILOT_CLIENT_ID` を取得します（例：シェルで `export MY_COPILOT_CLIENT_ID=your_client_id` で設定）。
- 設定されていない場合、エラーをログ出力しスクリプトを終了します（プロセスコード1は失敗を示します）。
- このクライアントIDは登録済みのGitHub OAuth Appからのものです（OAuthフローに必要）。

#### 2. 共通ヘッダーの設定
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- HTTPリクエスト用のキーと値のペアを持つ `Headers` オブジェクトを作成します。
- これらのヘッダーは、リクエストをGitHub Copilot Vimプラグイン（Neovim 0.6.1用バージョン1.16.0）からのもののように見せます。これはユーザーエージェントを偽装し、CopilotのAPIコールを模倣するためであり、GitHubがリクエストを受け入れるために必要または有用である可能性があります。
- `"accept": "application/json"`: JSONレスポンスを期待します。
- `"content-type": "application/json"`: リクエストボディでJSONを送信します。
- `"accept-encoding"`: 帯域幅を節約するためにgzip/deflate圧縮を許可します。

#### 3. `getDeviceCode()` 関数
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **目的**: GitHubにデバイスコードをリクエストして、デバイスコードフローを開始します。
- 以下を含むJSONペイロードを構築します：
  - `client_id`: OAuthクライアントID（アプリの認証用）。
  - `scope`: `"read:user"` — トークンの権限を基本的なユーザープロファイル情報の読み取りに制限します（例：GitHub API経由でのユーザー名、メールアドレス）。これは最小限のスコープです。
- `https://github.com/login/device/code`（GitHubのOAuthデバイスコードエンドポイント）へのPOSTリクエストを行います。
- JSONレスポンスを解析します（期待されるフィールド：`device_code`、`user_code`、`verification_uri`、`expires_in` — コードには表示されていませんが、このフローの標準です）。
- エラー時（例：ネットワーク問題）、ログ出力しますが継続します（`undefined` を返す可能性があります）。
- GitHubからの解析されたJSONデータオブジェクトを返します。

#### 4. `getAccessToken(deviceCode: string)` 関数
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **目的**: ユーザーが承認した後、デバイスコードをアクセストークンと交換するためにGitHubをポーリングします。
- 前のステップからの `device_code` を受け取ります。
- 以下を含むJSONを構築します：
  - `client_id`: 前回と同じ。
  - `device_code`: このデバイス/認証試行を識別する一意のコード。
  - `grant_type`: これがデバイスコードグラントであることを指定します（標準的なOAuth2 URN）。
- `https://github.com/login/oauth/access_token` へのPOSTリクエストを行います。
- 解析されたJSONレスポンスを返します。これは以下のようになります：
  - 成功時： `{ access_token: "...", token_type: "bearer", scope: "read:user" }`。
  - 保留/エラー時： `{ error: "...", error_description: "..." }`（例："authorization_pending" または "slow_down"）。
- エラー（例：fetch失敗）はログ出力されますが明示的に処理されないため、呼び出し元は戻り値をチェックする必要があります。

#### 5. メイン実行（即時実行 async 関数）
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **全体の流れ**: 完全なOAuth 2.0デバイスコードグラントを調整します。
- `getDeviceCode()` を呼び出し、レスポンスを変数に分割代入します（成功しこれらのプロパティを持つことを想定）。
- ユーザーへの指示をログ出力します：
  - `user_code`: 短い英数字のコード（例："ABCD-EFGH"）。
  - `verification_uri`: 通常は `https://github.com/login/device`。ユーザーがここで認証します。
  - `expires_in`: コードの有効期限までの秒数（例：900秒は15分）。
- ユーザーはURLにアクセスし、GitHubにサインインし、ユーザーコードを入力してアプリを承認する必要があります。
- トークンを取得するために無限ループでポーリングします：
  - 試行間で5秒待機します（ポーリング間隔。GitHubは頻度が高すぎるリクエストに対してslow_downを推奨しています）。
  - `getAccessToken(device_code)` を呼び出します。
  - レスポンスに `error` がある場合：ログ出力します（例："authorization_pending" の場合は待機を継続）。
  - `access_token` がある場合：完全なトークンオブジェクト（インデント付きでフォーマット）をログ出力し、ループを抜けます。
- **エッジケース/問題点**:
  - `getDeviceCode()` が失敗した場合、分割代入でエラーが発生する可能性があります（コードはこれをチェックしていません）。
  - ループのタイムアウトがありません — アクセストークンが受信されるかスクリプトがクラッシュするまで無限にポーリングします。
  - アクセストークンをコンソールに出力すると露出します。本番環境では安全に保存する必要があります（例：ファイルやデータベースへ）。

### エンドツーエンドの仕組み
1. **ステップ1: デバイスコードのリクエスト** → スクリプトがGitHubから一時コードを取得。
2. **ステップ2: ユーザー承認** → ユーザーがGitHubにアクセスし、コードを入力して権限を付与。
3. **ステップ3: トークンのポーリング** → スクリプトがトークンが発行されるまでGitHubに問い合わせ続ける。
4. **結果**: 指定されたスコープ（例：GitHub API経由でのユーザーデータ読み取り）用のアクセストークン。

これはGitHub CLIのようなツールの動作を模倣したもので、Copilot用に適応されています。GitHubの公式OAuthドキュメントについては、https://docs.github.com/ja/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow を参照してください。類似のものを構築する場合は、OAuth標準とGitHubのポリシーに準拠していることを確認してください。変更や実行について質問がある場合は、お知らせください！