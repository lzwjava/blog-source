---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: Spring 5 WARのjavax.servletへの移行
translated: true
type: note
---

あと一歩です。このプロジェクトはSpring 5（javax.*時代）かつWARのため、最もクリーンな方法は: **`javax.servlet-api` 4.xを使用**し、最小限の`web.xml`、Java設定、小さなコントローラーを追加することです。

### 0) servlet APIの修正（重要）

Spring 5.2.xは`javax.servlet.*`を使用しますが、あなたのPOMは**`jakarta.servlet-api:5.0.0`**を参照しています。これを`javax`に置き換えてください:

```xml
<!-- jakarta依存関係を以下で置き換え -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

（Jetty 9.4は維持 - これはServlet 3.1/4.0互換でjavax対応です。）

### 1) `web.xml` (`failOnMissingWebXml=true`と設定したため)

`src/main/webapp/WEB-INF/web.xml`を作成:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- ルートSpringコンテキスト（後でサービス/リポジトリを追加する場合） -->
  <listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
  <context-param>
    <param-name>contextClass</param-name>
    <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
  </context-param>
  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>com.lzw.config.RootConfig</param-value>
  </context-param>

  <!-- MVC用DispatcherServlet -->
  <servlet>
    <servlet-name>dispatcher</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
      <param-name>contextClass</param-name>
      <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
    </init-param>
    <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>com.lzw.config.WebConfig</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>dispatcher</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>

</web-app>
```

### 2) Java設定

2つの設定クラスを作成します。

`src/main/java/com/lzw/config/RootConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // サービス/リポジトリがある場合（または将来追加する場合）、@Bean定義を追加
}
```

`src/main/java/com/lzw/config/WebConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.lzw.web")
public class WebConfig {
    // RESTのみの場合は空のまま。後でビューリゾルバー/静的リソースハンドラーを必要に応じて追加
}
```

### 3) Helloコントローラー

`src/main/java/com/lzw/web/HelloController.java`:

```java
package com.lzw.web;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, Spring MVC!";
    }
}
```

### 4) ディレクトリ構造の確認

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) 実行

POMにJettyが既にあるため:

```bash
mvn clean package
mvn jetty:run
```

開く: `http://localhost:8080/hello` → `Hello, Spring MVC!`と表示されるはずです。

---

#### 注意点と落とし穴

* **どうしても**`jakarta.servlet-api:5.x`を維持する必要がある場合、Spring 6 / Spring Boot 3+（Jakartaネームスペース）と新しいservletコンテナが必要です。現在のスタック（Spring 5.2.2）では、**`javax.servlet-api:4.0.1`を使用**してください。
* `maven-war-plugin`で`failOnMissingWebXml=true`と設定したため、Spring 3.1+がそれなしで実行できるにもかかわらず、`web.xml`が必要です。
* 後でビュー（JSP/Thymeleaf）を追加する場合は、`WebConfig`にビューリゾルバーを追加してください。純粋なJSONの場合は、上記の`@RestController`アプローチで十分です。