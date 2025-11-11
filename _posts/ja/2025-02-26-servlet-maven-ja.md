---
audio: false
generated: true
lang: ja
layout: post
title: Mavenを使用したJavaサーブレットアプリケーション
translated: true
type: note
---

Mavenを使用してプロジェクトをビルドし、Liberty Mavenプラグインを使用してデプロイする、WebSphere Liberty Profile（WLP）上でシンプルなJava Servletアプリケーションを作成およびデプロイする完全なガイドです。この例では、アクセスすると「Hello World!」を返す基本的なServletを作成し、MavenでWARファイルにビルドし、WLPにデプロイします。WLPが`servlet-4.0`フィーチャーを有効にしてセットアップ済みであることを前提とします。これにより、必要なServletサポートが提供されます。

---

## ステップバイステップガイド

### 1. Mavenプロジェクト構造の作成
標準的なMaven Webアプリケーション構造をセットアップします。手動で作成するか、Mavenを使用して生成できます。

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

- **オプション: Mavenで生成:**
  このコマンドを実行して構造を作成し、必要に応じて調整します:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  これにより基本的なWebapp構造が作成されます。次のステップで変更します。

### 2. Servletコードの記述
`src/main/java/com/example/`に`HelloServlet.java`というファイルを作成し、以下の内容を記述します:

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

- **説明:** このServletはHTTP GETリクエストにプレーンテキストで「Hello World!」を返します。シンプルな`doGet`メソッドを使用し、明示的な`web.xml`設定との互換性のためにアノテーションは使用していません。

### 3. `web.xml`デプロイメント記述子の作成
`src/main/webapp/WEB-INF/`に`web.xml`というファイルを作成し、以下の内容を記述します:

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