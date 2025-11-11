---
audio: false
generated: true
lang: ja
layout: post
title: Spring MVC
translated: true
type: note
---

**Spring Boot**を使用せずに**Spring MVC**を使用するには、Springフレームワークを手動で設定する必要があります。Spring Bootは通常、設定の大部分を自動化するためです。以下は、XMLベースの設定を使用してシンプルなSpring MVC Webアプリケーションを作成するステップバイステップガイドです。この例では、単一のコントローラを持ち、JSPページで「Welcome」メッセージを表示する基本的なアプリケーションを設定します。

---

## ステップバイステップガイド

### 1. プロジェクト構造を設定する
標準的なWebアプリケーション構造を作成します。IntelliJやEclipseなどのIDEを使用するか、手動でフォルダを作成できます。構造は以下のようになります：

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

- **`src/main/java`**: Javaソースコード（例：コントローラ）を含みます。
- **`src/main/webapp/WEB-INF`**: 設定ファイル（`web.xml`、`spring-mvc-config.xml`）とJSPビューを含みます。

### 2. 依存関係を追加する
Mavenを使用する場合、必要な依存関係を`pom.xml`に含めます。シンプルなSpring MVCアプリケーションには、Spring Web MVCライブラリとServlet API（コンテナによって提供）が必要です。

`pom.xml`を作成または編集し、以下の内容を追加します：

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

- **注意点**:
  - `<packaging>war</packaging>`: プロジェクトがWARファイルとしてパッケージされ、サーブレットコンテナにデプロイされることを保証します。
  - Mavenを使用しない場合は、Spring MVC JARとServlet API JARを手動でダウンロードし、プロジェクトのクラスパスに追加してください。

### 3. `web.xml`でDispatcherServletを設定する
`web.xml`ファイルは、Webアプリケーションのデプロイメント記述子です。これを使用して、Spring MVCのフロントコントローラである`DispatcherServlet`を設定し、受信リクエストを処理します。

`src/main/webapp/WEB-INF/web.xml`を作成し、以下の内容を追加します：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <!-- Define the DispatcherServlet -->
    <servlet>
        <servlet-name>spring-mvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- Map the DispatcherServlet to handle all requests -->
    <servlet-mapping>
        <servlet-name>spring-mvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

- **説明**:
  - `<servlet-class>`: リクエストをコントローラにルーティングする`DispatcherServlet`を指定します。
  - `<init-param>`: Spring設定ファイル（`spring-mvc-config.xml`）を指します。
  - `<url-pattern>/</url-pattern>`: サーブレットがアプリケーションへのすべてのリクエストを処理するようにマッピングします。

### 4. Spring設定ファイルを作成する
`src/main/webapp/WEB-INF/spring-mvc-config.xml`を作成し、コントローラやビューリゾルバなどのSpring MVC Beanを定義します。

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

    <!-- Enable component scanning for controllers -->
    <context:component-scan base-package="com.example.controllers" />

    <!-- Enable annotation-driven MVC -->
    <mvc:annotation-driven />

    <!-- Configure view resolver for JSP files -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

- **説明**:
  - `<context:component-scan>`: `com.example.controllers`パッケージをスキャンし、アノテーション付きコンポーネント（例：`@Controller`）を検出します。
  - `<mvc:annotation-driven>`: アノテーションベースのMVC機能（例：`@GetMapping`）を有効にします。
  - `InternalResourceViewResolver`: ビュー名を`/WEB-INF/views/`内の`.jsp`サフィックス付きJSPファイルにマッピングします。

### 5. シンプルなコントローラを作成する
HTTPリクエストを処理するコントローラを作成します。`src/main/java/com/example/controllers/`に`HomeController.java`を追加します：

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
  - `@Controller`: このクラスをSpring MVCコントローラとしてマークします。
  - `@GetMapping("/")`: ルートURL（`/`）へのGETリクエストを`home()`メソッドにマッピングします。
  - `return "home"`: ビュー名`"home"`を返し、`/WEB-INF/views/home.jsp`に解決されます。

### 6. JSPビューを作成する
出力を表示するシンプルなJSPファイルを作成します。`src/main/webapp/WEB-INF/views/`に`home.jsp`を追加します：

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Spring MVC without Spring Boot</h1>
</body>
</html>
```

### 7. アプリケーションをビルドしてパッケージ化する
Mavenを使用する場合、プロジェクトルートで以下のコマンドを実行してWARファイルをビルドします：

```bash
mvn clean package
```

これにより、`target`ディレクトリに`SimpleSpringMVCApp-1.0-SNAPSHOT.war`が生成されます。

- **注意**: Mavenを使用しない場合は、Javaファイルをコンパイルし、フォルダ構造を維持しながらプロジェクトを手動でWARファイルにパッケージ化してください。

### 8. アプリケーションをデプロイする
WARファイルをApache Tomcatなどのサーブレットコンテナにデプロイします：
- `SimpleSpringMVCApp-1.0-SNAPSHOT.war`をTomcatインストールの`webapps`ディレクトリにコピーします。
- Tomcatを起動します（例：Tomcatの`bin`ディレクトリから`startup.sh`または`startup.bat`を実行）。

### 9. アプリケーションにアクセスする
ブラウザを開き、以下に移動します：

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

以下の表示が確認できるはずです：
```
Welcome to Spring MVC without Spring Boot
```

- **注意**: コンテキストパス（`/SimpleSpringMVCApp-1.0-SNAPSHOT`）はWARファイル名に依存します。WARを`myapp.war`にリネームすると、URLは`http://localhost:8080/myapp/`になります。

---

## まとめ
**Spring Bootを使用せずにSpring MVCを使用する**には：
1. **Webプロジェクトを設定**し、標準的な構造を持たせます。
2. Spring MVCとServlet APIの**依存関係を追加**します。
3. `web.xml`で**DispatcherServletを設定**します。
4. XMLファイル（例：`spring-mvc-config.xml`）で**Spring設定を定義**します。
5. リクエストを処理する**コントローラを作成**します。
6. レスポンス用の**JSPビューを追加**します。
7. WARファイルをビルドしてサーブレットコンテナに**デプロイ**します。

このアプローチは設定を完全に制御できるため、Spring MVCの基礎を学ぶのに最適な方法です！