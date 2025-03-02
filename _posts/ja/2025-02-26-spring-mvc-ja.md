---
audio: false
generated: true
lang: ja
layout: post
title: スプリング MVC
translated: true
---

**Spring MVC**を**Spring Boot**なしで使用するには、Springフレームワークを手動で設定する必要があります。Spring Bootは通常、多くの設定を自動化します。以下は、XMLベースの設定を使用してシンプルなSpring MVCウェブアプリケーションを作成するためのステップバイステップガイドです。この例では、単一のコントローラーを設定してJSPページに「Welcome」メッセージを表示する基本的なアプリケーションを構築します。

---

## ステップバイステップガイド

### 1. プロジェクト構造の設定
標準的なウェブアプリケーション構造を作成します。IntelliJやEclipseのようなIDEを使用するか、手動でフォルダを作成します。構造は以下のようになります：

```
SimpleSpringMVCApp/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── example/
│                   └── controllers/
│                       └── HomeController.java
│       └── webapp/
│           └── WEB-INF/
│               ├── web.xml
│               ├── spring-mvc-config.xml
│               └── views/
│                   └── home.jsp
└── pom.xml  (Mavenを使用する場合)
```

- **`src/main/java`**: Javaソースコード（例：コントローラー）を含む。
- **`src/main/webapp/WEB-INF`**: 構成ファイル（`web.xml`、`spring-mvc-config.xml`）とJSPビューを含む。

### 2. 依存関係の追加
Mavenを使用している場合、`pom.xml`に必要な依存関係を追加します。シンプルなSpring MVCアプリケーションには、Spring Web MVCライブラリとサーブレットAPI（コンテナによって提供される）が必要です。

`pom.xml`を作成または編集して以下の内容を追加します：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>SimpleSpringMVCApp</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <dependencies>
        <!-- Spring Web MVC -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.3.10</version>
        </dependency>
        <!-- Servlet API (provided by the container) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
            </plugin>
        </plugins>
    </build>
</project>
```

- **メモ**:
  - `<packaging>war</packaging>`: プロジェクトがサーブレットコンテナにデプロイされるようにWARファイルとしてパッケージングされることを確認します。
  - Mavenを使用していない場合は、Spring MVC JARとサーブレットAPI JARを手動でダウンロードし、プロジェクトのクラスパスに追加します。

### 3. `web.xml`でDispatcherServletを設定
`web.xml`ファイルは、ウェブアプリケーションのデプロイメント記述子です。Spring MVCのフロントコントローラである`DispatcherServlet`を設定して、受信リクエストを処理します。

`src/main/webapp/WEB-INF/web.xml`を以下の内容で作成します：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <!-- DispatcherServletを定義 -->
    <servlet>
        <servlet-name>spring-mvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- DispatcherServletにすべてのリクエストを処理させる -->
    <servlet-mapping>
        <servlet-name>spring-mvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

- **説明**:
  - `<servlet-class>`: リクエストをコントローラーにルーティングする`DispatcherServlet`を指定します。
  - `<init-param>`: Spring構成ファイル（`spring-mvc-config.xml`）を指します。
  - `<url-pattern>/</url-pattern>`: サーブレットにすべてのリクエストをマッピングします。

### 4. Spring構成ファイルの作成
Spring MVCビーン（例：コントローラーとビュー解決器）を定義するために、`src/main/webapp/WEB-INF/spring-mvc-config.xml`を作成します。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
           http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
           http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd">

    <!-- コントローラーのコンポーネントスキャンを有効にする -->
    <context:component-scan base-package="com.example.controllers" />

    <!-- アノテーション駆動型MVCを有効にする -->
    <mvc:annotation-driven />

    <!-- JSPファイル用のビュー解決器を設定 -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

- **説明**:
  - `<context:component-scan>`: `com.example.controllers`パッケージ内のアノテーション付きコンポーネント（例：`@Controller`）をスキャンします。
  - `<mvc:annotation-driven>`: アノテーションベースのMVC機能（例：`@GetMapping`）を有効にします。
  - `InternalResourceViewResolver`: ビュー名を`/WEB-INF/views/`内のJSPファイルにマッピングします。

### 5. シンプルなコントローラーの作成
HTTPリクエストを処理するコントローラーを作成します。`src/main/java/com/example/controllers/`に`HomeController.java`を追加します：

```java
package com.example.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

- **説明**:
  - `@Controller`: このクラスをSpring MVCコントローラーとしてマークします。
  - `@GetMapping("/")`: ルートURL（`/`）に対するGETリクエストを`home()`メソッドにマッピングします。
  - `return "home"`: ビュー名`"home"`を返し、`/WEB-INF/views/home.jsp`に解決します。

### 6. JSPビューの作成
出力を表示するシンプルなJSPファイルを作成します。`src/main/webapp/WEB-INF/views/`に`home.jsp`を追加します：

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Spring MVC without Spring Bootへようこそ</h1>
</body>
</html>
```

### 7. アプリケーションのビルドとパッケージング
Mavenを使用している場合、プロジェクトのルートから以下のコマンドを実行してWARファイルをビルドします：

```bash
mvn clean package
```

これにより、`target`ディレクトリに`SimpleSpringMVCApp-1.0-SNAPSHOT.war`が生成されます。

- **メモ**: Mavenを使用していない場合は、Javaファイルをコンパイルし、プロジェクトをWARファイルとして手動でパッケージ化し、フォルダ構造を維持します。

### 8. アプリケーションのデプロイ
WARファイルをApache Tomcatなどのサーブレットコンテナにデプロイします：
- `SimpleSpringMVCApp-1.0-SNAPSHOT.war`をTomcatインストールの`webapps`ディレクトリにコピーします。
- Tomcatを起動します（例：Tomcatの`bin`ディレクトリから`startup.sh`または`startup.bat`を実行します）。

### 9. アプリケーションへのアクセス
ブラウザを開き、以下のURLにアクセスします：

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

以下のメッセージが表示されるはずです：
```
Spring MVC without Spring Bootへようこそ
```

- **メモ**: コンテキストパス（`/SimpleSpringMVCApp-1.0-SNAPSHOT`）はWARファイル名に依存します。WARファイルを`myapp.war`にリネームすると、URLは`http://localhost:8080/myapp/`になります。

---

## まとめ
**Spring MVCをSpring Bootなしで使用するには**:
1. **ウェブプロジェクトを設定**し、標準的な構造を使用します。
2. **依存関係**をSpring MVCとサーブレットAPIに追加します。
3. **DispatcherServletを`web.xml`で設定**します。
4. **Spring構成**をXMLファイル（例：`spring-mvc-config.xml`）で定義します。
5. **リクエストを処理するコントローラー**を作成します。
6. **レスポンス用のJSPビュー**を追加します。
7. **WARファイルをビルドし、サーブレットコンテナにデプロイ**します。

このアプローチは、設定を完全に制御できるため、Spring MVCの基本を学ぶのに最適です！