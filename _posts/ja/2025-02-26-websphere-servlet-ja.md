---
audio: true
generated: true
lang: ja
layout: post
title: Servlet バージョンの WebSphere Liberty プロファイル
translated: true
---

### エラーの理解

`console.log` からのエラーメッセージは、`spring-web-6.2.3.jar` 内の `web-fragment.xml` ファイルに関連する `DDParser ParseException` を示しています。具体的には、デプロイメント記述子がバージョン "50"（これは Servlet 5.0 に対応）を指定しているが、WebSphere Liberty Profile (WLP) サーバーは現在バージョン "40"（Servlet 4.0）でプロビジョニングされているため、この不一致が発生しています。この不一致は以下の理由で発生します：

- **Servlet 5.0** は Jakarta EE 9 の一部であり、新しいバージョンの Spring Boot（例：Spring Boot 3.x、`spring-web-6.2.3.jar` を含む）で必要です。
- **Servlet 4.0** は Java EE 8 の一部であり、WLP は `javaee-8.0` フェーチャーで構成されているため、Servlet 5.0 をサポートしていません。

これを修正するには、WLP でサポートされる Servlet バージョンをアプリケーションで必要なバージョンに合わせる必要があります。推奨されるソリューションは、Servlet 5.0 をサポートするために `jakartaee-9.1` フェーチャーを有効にすることです。

---

### ソリューション：WLP を Servlet 5.0 をサポートするように更新

WLP を `jakartaee-9.1` フェーチャーを使用して更新することで問題を修正する方法は以下の通りです：

#### 1. **`server.xml` ファイルの場所を特定**
- `server.xml` 構成ファイルは、WLP で有効にされているフェーチャーを定義します。
- これは通常、サーバーディレクトリにあります。例：`/opt/ibm/wlp/usr/servers/myServer/server.xml`、`myServer` はサーバーの名前です。

#### 2. **`server.xml` ファイルの編集**
- テキストエディタで `server.xml` ファイルを開きます。
- サーバーで有効にされているフェーチャーをリストする `<featureManager>` セクションを探します。以下のように表示されるかもしれません：
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- `javaee-8.0` フェーチャーを `jakartaee-9.1` に置き換えて Servlet 5.0 サポートを有効にします：
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- ファイルを保存します。

#### 3. **WLP 開発モードでの変更の適用（適用可能な場合）**
- **開発モード**で WLP を実行している場合（例：`wlp/bin/server run` コマンドまたは IDE 統合を使用）は、以下のように変更を適用します：
  - **手動再起動:**
    - サーバーを停止します：
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - サーバーを再起動します：
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **開発モードのホットリロード:**
    - WLP が開発モードで実行されている場合（例：`server run` または IDE を介して）は、`server.xml` の変更を自動的に検出するかもしれません。しかし、新しいフェーチャーが読み込まれることを確認するために再起動が推奨されます。

#### 4. **修正の確認**
- サーバーを再起動した後、アプリケーションを再デプロイします（例：WAR ファイルを `dropins` ディレクトリにコピーするか、デプロイメント方法を使用）。
- サーバーログを確認して、成功したデプロイメントを確認します。以下のようなメッセージを探します：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Application myapp started in X.XXX seconds.
  ```
- アプリケーションにアクセスして（例：`http://localhost:9080/myapp/`）エラーなしで動作していることを確認します。

---

### 代替ソリューション：Spring Boot のダウングレード

WLP を `jakartaee-9.1` に更新することができない場合（例：他のアプリケーションとの互換性の制約）は、Servlet 4.0 に対応する Spring Boot のバージョンにダウングレードすることができます：

#### 1. **Spring Boot 2.7.x に切り替え**
- Spring Boot 2.7.x は Servlet 4.0（および Servlet 3.1 などの以前のバージョン）をサポートします。
- `pom.xml` を更新して Spring Boot 2.7.x を使用します：
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- 最新の 2.7.x バージョンを使用 -->
      <relativePath/>
  </parent>
  ```

#### 2. **再構築と再デプロイ**
- アプリケーションを再構築します：
  ```bash
  mvn clean package
  ```
- 生成された WAR ファイルを WLP に再デプロイし、エラーなしで起動することを確認します。

---

### まとめ
- **エラーの原因**：アプリケーション（`spring-web-6.2.3.jar`）は Servlet 5.0 を必要としますが、WLP は Servlet 4.0 に構成されています。
- **推奨される修正**：WLP を `jakartaee-9.1` フェーチャーを使用するように更新し、`server.xml` を編集してサーバーを再起動します。
- **代替修正**：Spring Boot 2.7.x にダウングレードして WLP の Servlet 4.0 サポートに合わせます。

推奨されるソリューション（WLP の更新）により、アプリケーションは Spring Boot 3.x と Jakarta EE 9 の最新機能を使用できます。上記の手順に従って問題を解決し、アプリケーションを成功裏にデプロイしてください。