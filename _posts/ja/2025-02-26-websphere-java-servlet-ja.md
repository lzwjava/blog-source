---
audio: false
generated: false
lang: ja
layout: post
title: Java Servlet アプリケーションの WebSphere Liberty Profile
translated: true
---

WebSphere Liberty Profile (WLP) 上で非常に簡単な Java Servlet アプリケーションを実行するための完全なガイドです。この例では、"Hello World!" を返す基本的な Servlet を作成し、`dropins` ディレクトリを使用して WLP にデプロイします。`servlet-4.0` フェーチャが有効になっている WLP が既に設定されていることを前提としています。このガイドでは Maven を使用せず、必要なすべてのコードとデプロイ手順を提供します。

---

### ステップバイステップガイド

#### 1. Servlet アプリケーションの構造を作成
Servlet アプリケーションのディレクトリ構造を手動で作成します。任意のフォルダ名を使用できますが、この例では `SimpleServletApp` と呼びます。

- **ディレクトリ構造:**
  ```
  SimpleServletApp/
  ├── src/
  │   └── com/
  │       └── example/
  │           └── HelloServlet.java
  └── webapp/
      └── WEB-INF/
          └── web.xml
  ```

#### 2. Servlet コードを記述
`SimpleServletApp/src/com/example/` に `HelloServlet.java` ファイルを作成し、以下の内容を記述します：

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **説明:** この Servlet は、HTTP GET リクエストに対して "Hello World!" をプレーンテキストで応答します。最大の互換性とシンプルさのために、アノテーションを使用せずにシンプルな `doGet` メソッドを使用しています。

#### 3. `web.xml` デプロイメント記述子を作成
`SimpleServletApp/webapp/WEB-INF/` に `web.xml` ファイルを作成し、以下の内容を記述します：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **説明:** `web.xml` ファイルは、`HelloServlet` クラスを `/hello` URL パターンにマッピングします。アノテーションを使用しないため、これは必要です。

#### 4. Servlet をコンパイル
`javac` を使用して `HelloServlet.java` ファイルを `.class` ファイルにコンパイルします。コンパイル時に `javax.servlet-api` ライブラリがクラスパスに含まれている必要があります。これは WLP によって提供されますが、コンパイル中に利用可能である必要があります。

- **手順:**
  1. WLP インストールにある Servlet API JAR を特定します。例えば、WLP が `/opt/ibm/wlp` にインストールされている場合、JAR は通常以下にあります：
     ```
     /opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar
     ```
     正確なファイル名は WLP のバージョンによって異なる場合があります。
  2. `SimpleServletApp` ディレクトリから以下のコマンドを実行します：
     ```bash
     javac -cp "/opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar" src/com/example/HelloServlet.java
     ```
  3. これにより、`SimpleServletApp/src/com/example/` に `HelloServlet.class` が作成されます。

#### 5. アプリケーションを WAR ファイルにパッケージ
コンパイルされたファイルを整理し、手動で WAR ファイルを作成します。

- **コンパイルされたクラスを移動:**
  `WEB-INF/classes` ディレクトリを作成し、コンパイルされたクラスファイルを移動します：
  ```bash
  mkdir -p webapp/WEB-INF/classes/com/example
  mv src/com/example/HelloServlet.class webapp/WEB-INF/classes/com/example/
  ```

- **WAR ファイルを作成:**
  `SimpleServletApp` ディレクトリから `jar` コマンドを使用して `webapp` フォルダを WAR ファイルにパッケージします：
  ```bash
  cd webapp
  jar -cvf ../myapp.war .
  cd ..
  ```
  これにより、`SimpleServletApp` ディレクトリに `myapp.war` が作成されます。

#### 6. WLP に WAR ファイルをデプロイ
`dropins` ディレクトリを使用して WAR ファイルを WLP にデプロイします。

- **`dropins` ディレクトリを特定:**
  WLP サーバーの `dropins` ディレクトリを特定します。WLP が `/opt/ibm/wlp` にインストールされ、サーバー名が `myServer` の場合、パスは以下の通りです：
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **WAR ファイルをコピー:**
  WAR ファイルを `dropins` ディレクトリに移動します：
  ```bash
  cp myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **サーバーを起動（実行中でない場合）:**
  WLP が実行されていない場合は、以下のコマンドを実行して起動します：
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  既に実行中の場合、WAR ファイルを自動的に検出しデプロイします。

- **デプロイを確認:**
  サーバーのログまたはコンソールに以下のようなメッセージが表示されることを確認します：
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ログは `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` にあります。

#### 7. アプリケーションにアクセス
ブラウザでデプロイされた Servlet をテストします。

- **ブラウザを開く:**
  以下の URL にアクセスします：
  ```
  http://localhost:9080/myapp/hello
  ```
  - `9080` は WLP のデフォルトの HTTP ポートです。
  - `/myapp` は WAR ファイル名からのコンテキストルートです。
  - `/hello` は `web.xml` で定義された URL パターンです。

- **期待される結果:**
  プレーンテキストとして以下が表示されるはずです：
  ```
  Hello World!
  ```

---

### 注意点
- **JSP は含まれていません:** JSP ファイルが含まれているかどうかの質問があったが、この *非常に簡単な* アプリケーションは基本的な Servlet だけに焦点を当てています。必要に応じて JSP を追加できます。
- **コンテキストルート:** コンテキストルート (`/myapp`) は WAR ファイル名から来ます。`myapp.war` をリネームして変更できます（例: `app.war` は `/app`）。
- **ポート番号:** WLP はデフォルトで HTTP に `9080` を使用します。異なる場合は `server.xml` を確認してください。
- **Java バージョン:** WLP と互換性のある Java バージョンを使用してください（例: Java 8 または 11）。
- **トラブルシューティング:** 正しく動作しない場合は、`/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` を確認し、WAR ファイルが `dropins` にあり、サーバーが実行中であることを確認してください。

---

### 要約
このガイドでは、以下の手順を示します：
1. 簡単な Servlet (`HelloServlet.java`) と `web.xml` を作成します。
2. Maven を使用せずに `javac` で Servlet をコンパイルします。
3. 手動で WAR ファイル (`myapp.war`) にパッケージします。
4. WLP の `dropins` ディレクトリにデプロイします。
5. `http://localhost:9080/myapp/hello` で "Hello World!" にアクセスします。

これにより、ビルドツールのような Maven を使用せずに、WebSphere Liberty Profile 上で実行される非常にシンプルな Servlet アプリケーションが提供されます。