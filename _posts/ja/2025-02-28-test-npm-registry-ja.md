---
audio: false
generated: true
lang: ja
layout: post
title: 生NPMレジストリのテスト 生HTTPリクエストを使用して
translated: true
type: note
---

NPMレジストリを`curl`やInsomniaなどの生のHTTPリクエストでテストする場合、NPMクライアントに依存せずに、接続性、認証、パッケージデータ提供機能を確認できます。レジストリがユーザー名とパスワードを要求するため、リクエストで手動で認証を処理する必要があります。以下は、トークンベースまたは基本認証をサポートするNPM互換レジストリ（Verdaccio、Nexus、カスタム実装など）を想定した、生のHTTPリクエストを使用したレジストリテストの完全ガイドです。

---

## 生のHTTPリクエストでレジストリをテストする手順

### 1. 認証とトークンの取得（必要な場合）

ほとんどのNPMレジストリはトークンベース認証を使用しており、さらなるリクエストを行う前にログインしてトークンを取得する必要があります。一部のレジストリは基本認証を直接サポートしている場合もあります。`curl`を使用した認証方法は以下の通りです：

#### `curl`を使用したログイン
レジストリの認証エンドポイントにPUTリクエストを送信してトークンを取得します：

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **置換項目**:
  - `<username>`: レジストリのユーザー名
  - `<password>`: レジストリのパスワード
  - `<registry-url>`: レジストリの完全なURL（例: `https://my-registry.example.com`）
- **期待されるレスポンス**: 成功すると、トークンを含むJSONレスポンスが返されます：
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **トークンの保存**: 後続のリクエストで使用するため、`your-auth-token`の値をコピーします。

**注意**: レジストリが異なる認証エンドポイントや方法（基本認証やカスタムAPIなど）を使用する場合は、そのドキュメントを確認してください。基本認証を直接サポートする場合、このステップをスキップし、後続のリクエストで`-u "<username>:<password>"`を含めることができます。

---

### 2. レジストリへのping送信

レジストリのルートURLまたはpingエンドポイントにGETリクエストを送信して、基本的な接続性をテストします。

#### `curl`を使用したping送信
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **置換項目**:
  - `your-auth-token`: ステップ1で取得したトークン
  - `<registry-url>`: レジストリURL
- **期待されるレスポンス**: 成功したレスポンス（HTTP 200）は、レジストリのホームページまたは簡単なステータスメッセージ（CouchDBベースのレジストリの場合`{"db_name":"registry"}`など）を返す場合があります。
- **代替方法**: 一部のレジストリは`/-/ping`エンドポイントを提供しています：
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**基本認証を使用する場合**: トークンを使用せず、基本認証をサポートするレジストリの場合：
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. パッケージメタデータの取得

特定のパッケージの詳細をリクエストして、レジストリがパッケージメタデータを提供できることを確認します。

#### `curl`を使用したメタデータ取得
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **置換項目**:
  - `<package-name>`: レジストリ上に存在することがわかっているパッケージ（例：公開レジストリをプロキシする場合は`lodash`、プライベートパッケージの場合は`my-org-utils`など）
- **期待されるレスポンス**: バージョン、依存関係、tarball URLを含むパッケージのメタデータを持つJSONオブジェクト。例：
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<registry-url>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**基本認証を使用する場合**：
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **成功**: メタデータを含む200 OKレスポンスは、レジストリがパッケージデータを正しく提供していることを確認します。

---

### 4. パッケージtarballのダウンロード（オプション）

レジストリが実際のパッケージファイルを配信できることを確認するために、パッケージtarballをダウンロードします。

#### `curl`を使用したtarballダウンロード
1. ステップ3のメタデータから、特定のバージョンの`tarball` URLを見つけます（例：`<registry-url>/lodash/-/lodash-4.17.21.tgz`）。
2. ダウンロードします：
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **置換項目**: `<tarball-url>`をメタデータからのURLに置き換えます。
- **`-O`フラグ**: 元のファイル名でファイルを保存します（例：`lodash-4.17.21.tgz`）。
- **基本認証を使用する場合**：
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **成功**: ファイルが正常にダウンロードされ、内容を確認するために展開できます（例：`tar -xzf <filename>`）。

---

## Insomniaでのテスト

GUIツールのInsomniaを好む場合は、以下の手順に従ってください：

### 1. 認証の設定
- Insomniaで新しいリクエストを作成します。
- **Auth**タブに移動します：
  - **Bearer Token**: ステップ1でトークンを取得した場合、「Bearer Token」を選択し、`your-auth-token`を貼り付けます。
  - **Basic Auth**: レジストリが基本認証を使用する場合、「Basic Auth」を選択し、`<username>`と`<password>`を入力します。

### 2. レジストリへのping送信
- **メソッド**: GET
- **URL**: `<registry-url>`または`<registry-url>/-/ping`
- **Send**をクリックします。
- **期待されるレスポンス**: シンプルなレスポンス本文を含む200 OKステータス。

### 3. パッケージメタデータの取得
- **メソッド**: GET
- **URL**: `<registry-url>/<package-name>`
- Authタブで認証が設定されていることを確認します。
- **Send**をクリックします。
- **期待されるレスポンス**: JSON形式のパッケージメタデータを含む200 OKステータス。

### 4. tarballのダウンロード
- **メソッド**: GET
- **URL**: メタデータからのtarball URL（例：`<registry-url>/<package-name>/-/<package-name>-<version>.tgz`）
- **Send and Download**をクリックして、ファイルをローカルに保存します。
- **成功**: ファイルがダウンロードされ、レジストリがパッケージを提供していることを確認します。

---

## トラブルシューティング

- **401 Unauthorized**:
  - トークンまたは資格情報を確認してください。
  - `Authorization`ヘッダーまたは基本認証が正しくフォーマットされていることを確認してください。
- **404 Not Found**:
  - パッケージがレジストリに存在することを確認してください。
  - 公開パッケージ（例：`lodash`）をテストする場合、レジストリが公開NPMレジストリをプロキシしていることを確認してください。
- **接続エラー**:
  - `<registry-url>`を再確認してください（必要に応じて`https://`を含める）。
  - HTTPSレジストリで`curl`を使用してSSLエラーが発生する場合、テスト目的でのみ証明書チェックをバイパスするために`-k`を追加してください。
- **カスタムレジストリの動作**:
  - これらの手順が失敗する場合、特定のエンドポイントや認証方法についてレジストリのドキュメントを参照してください。

---

## 結論

`curl`またはInsomniaでこれらの手順に従うことで、生のHTTPリクエストを使用してNPMレジストリの接続性、認証、パッケージ提供機能をテストできます。まず認証（必要な場合）を行い、次にレジストリにpingを送信し、既知のパッケージのメタデータを取得し、オプションでtarballをダウンロードします。このアプローチにより、レジストリがHTTPレベルで完全に動作していることを確認できます。