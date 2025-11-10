---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Springを使用しないWebアプリケーションのセットアップ
translated: true
type: note
---

了解しました。**Java 8**と**Spring 5.2.2**（Spring Bootではなく、コアSpring + web）を使用している場合、最小限のアプリケーションを手動でセットアップする必要があります。以下は、1つのコントローラーを持つWebアプリを構築する簡単な例です。

---

### 1. 必要な依存関係を追加

`spring-context`、`spring-web`、`spring-core`は既にあります。リクエストを処理するためには`spring-webmvc`も必要です：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. コントローラーを作成

```java
package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class HelloController {

    @ResponseBody
    @RequestMapping("/hello")
    public String hello() {
        return "Hello, Spring Web!";
    }
}
```

* `@Controller`はSpringにこれがWebコントローラーであることを伝えます。
* `@RequestMapping("/hello")`は`http://localhost:8080/hello`にマッピングされます。
* `@ResponseBody`はプレーンテキストを返すようにします（JSPではありません）。

---

### 3. Spring設定を定義

Spring Bootを使用していないため、手動で設定を行う必要があります。

```java
package com.example.demo;

import org.springframework.context.annotation.*;
import org.springframework.web.servlet.config.annotation.*;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.example.demo")
public class AppConfig implements WebMvcConfigurer {
}
```

これによりSpring MVCが有効になり、コントローラーを探すためにパッケージがスキャンされます。

---

### 4. `web.xml`をセットアップ（Tomcat/Servletコンテナ用）

WARとしてパッケージングする場合：

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         version="3.1">

    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextClass</param-name>
            <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
        </init-param>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>com.example.demo.AppConfig</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>

</web-app>
```

これにより`DispatcherServlet`がセットアップされ、`AppConfig`が読み込まれます。

---

### 5. アプリを実行

* WARとしてパッケージし、Tomcat（またはJetty）にデプロイします。
* Tomcatを起動し、以下にアクセス：

  ```
  http://localhost:8080/your-app/hello
  ```
* 以下が表示されるはずです：

  ```
  Hello, Spring Web!
  ```

---

👉 質問：このアプリを**Tomcat（WARデプロイメント）** 内で実行したいですか？それとも**スタンドアロンの`main()`ランチャー**（組み込みサーバー、Spring Bootのように最小限）が良いですか？設定に応じて両方の方法をお見せできます。