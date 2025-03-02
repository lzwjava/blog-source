---
audio: false
generated: true
lang: ja
layout: post
title: Java Servlet アプリケーションの Maven
translated: true
---

ここには、WebSphere Liberty Profile (WLP) 上で Maven を使用してビルドし、Liberty Maven プラグインを使用してデプロイする簡単な Java Servlet アプリケーションを作成するための完全なガイドがあります。この例では、アクセス時に「Hello World!」を返す基本的な Servlet を作成し、Maven を使用して WAR ファイルにビルドし、それを WLP にデプロイします。WLP が `servlet-4.0` フェーチャーを有効にして設定されていることを前提としています。これは、必要な Servlet サポートを提供します。

---

## ステップバイステップガイド

### 1. Maven プロジェクト構造の作成
まず、標準的な Maven Web アプリケーション構造を設定します。これを手動で作成するか、Maven を使用して生成します。

- **ディレクトリ構造:**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **オプションで Maven を使用して生成:**
  次のコマンドを実行して構造を作成し、必要に応じて調整します:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  これは基本的な Web アプリ構造を作成し、次のステップで修正します。

### 2. Servlet コードの作成
`src/main/java/com/example/` に `HelloServlet.java` という名前のファイルを作成し、次の内容を追加します:

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

- **説明:** この Servlet は、HTTP GET リクエストに対して「Hello World!」をプレーンテキストで応答します。簡単な `doGet` メソッドを使用し、明示的な `web.xml` 設定との互換性のためにアノテーションを避けています。

### 3. `web.xml` デプロイメント記述子の作成
`src/main/webapp/WEB-INF/` に `web.xml` という名前のファイルを作成し、次の内容を追加します:

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

- **説明:** `web.xml` ファイルは `HelloServlet` クラスを定義し、`/hello` URL パターンにマッピングします。これは、アノテーション `@WebServlet` を使用していないため必要です。

### 4. Maven `pom.xml` の設定
`SimpleServletApp/` ディレクトリに `pom.xml` を作成または更新し、次の内容を追加します:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (provided by WLP) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin to build the WAR file -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin for deployment -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **説明:**
  - **コーディネート:** `groupId`、`artifactId`、`version` でプロジェクトを定義し、`packaging` を `war` に設定します。
  - **プロパティ:** ソースおよびターゲットバージョンを Java 8 に設定します。
  - **依存関係:** `provided` スコープで Servlet API を含めます。これは、ランタイムで WLP によって提供されます。
  - **Maven WAR プラグイン:** `<finalName>` を使用して WAR ファイル名を `myapp.war` に設定します。
  - **Liberty Maven プラグイン:** `/opt/ibm/wlp` にある Liberty サーバーにデプロイするように設定されています。サーバー名は `myServer` で、`dropins` ディレクトリにデプロイします。

### 5. プロジェクトのビルド
`SimpleServletApp/` ディレクトリから、Maven を使用して WAR ファイルをビルドします:

```bash
mvn clean package
```

- **結果:** これは、Servlet をコンパイルし、`web.xml` と一緒に `target/myapp.war` にパッケージ化し、デプロイのために準備します。

### 6. WebSphere Liberty にデプロイして実行
Liberty サーバー (`myServer`) が `servlet-4.0` フェーチャーを有効にして設定されていることを確認します。`server.xml` で次のように確認します:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

Liberty Maven プラグインを使用してアプリケーションをデプロイし、実行します:

```bash
mvn liberty:run
```

- **何が起こるか:**
  - サーバーが既に実行中でない場合は、フォアグラウンドでサーバーを起動します。
  - `myapp.war` を `dropins` ディレクトリに自動的にデプロイします。
  - サーバーが停止するまで実行を続けます。

- **デプロイの確認:** 次のようなログメッセージを確認します:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ログは通常 `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` にあります。

### 7. アプリケーションへのアクセス
ブラウザを開き、次の URL にアクセスします:

```
http://localhost:9080/myapp/hello
```

- **期待される出力:**
  ```
  Hello World!
  ```

- **URL の解説:**
  - `9080`: WLP のデフォルト HTTP ポート。
  - `/myapp`: WAR ファイル名 (`myapp.war`) からのコンテキストルート。
  - `/hello`: `web.xml` からの URL パターン。

### 8. サーバーの停止
`mvn liberty:run` はサーバーをフォアグラウンドで実行するため、ターミナルで `Ctrl+C` を押して停止します。

---

## 注意点
- **前提条件:**
  - Maven がシステムにインストールされ、設定されている必要があります。
  - Liberty が `/opt/ibm/wlp` にインストールされ、サーバーインスタンス `myServer` が存在する必要があります。`pom.xml` の `installDirectory` と `serverName` を設定が異なる場合に調整します (例: `/usr/local/wlp` または `defaultServer`)。
  - `server.xml` で `servlet-4.0` フェーチャーが有効になっている必要があります。

- **代替デプロイ:**
  - ビルドとデプロイを別々に行うには:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    必要に応じてサーバーを手動で起動します:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **ポート設定:** Liberty サーバーが異なる HTTP ポートを使用している場合、`server.xml` の `<httpEndpoint>` を確認し、URL を適宜調整します。

- **コンテキストルート:** `pom.xml` の `<finalName>` を変更して (例: `<finalName>app</finalName>`) コンテキストルートを `/app` に変更します。

- **トラブルシューティング:**
  - デプロイに失敗した場合、`pom.xml` の `installDirectory` と `serverName` を確認します。
  - エラーを確認するために `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` のログを確認します。
  - `maven.compiler` 設定と一致する Java 8 以降を使用していることを確認します。

---

## 要約
このガイドでは、以下の手順を示します:
1. Maven プロジェクトを設定し、`HelloServlet.java` と `web.xml` を作成します。
2. `pom.xml` を Servlet API、Maven WAR プラグイン、Liberty Maven プラグインで設定します。
3. `mvn clean package` を使用してアプリケーションを `myapp.war` にビルドします。
4. `mvn liberty:run` を使用して WLP にデプロイし、実行します。
5. `http://localhost:9080/myapp/hello` で「Hello World!」にアクセスします。

これにより、WebSphere Liberty Profile 上で Servlet アプリケーションを Maven ベースで開発し、デプロイする簡潔なアプローチが提供されます。