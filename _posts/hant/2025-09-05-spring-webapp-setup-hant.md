---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 不使用 Boot 的 Spring 網頁應用程式設定
translated: true
type: note
---

明白了。既然你使用的是 **Java 8** 和 **Spring 5.2.2**（這裡沒有使用 Spring Boot，只有核心 Spring + web），你需要手動設定一個最小化的應用程式。以下是一個簡單範例，展示如何建立一個包含單一控制器的 web 應用程式。

---

### 1. 添加必要依賴

你已經有 `spring-context`、`spring-web` 和 `spring-core`。為了處理請求，你還需要 `spring-webmvc`：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. 建立控制器

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

* `@Controller` 告訴 Spring 這是一個 web 控制器。
* `@RequestMapping("/hello")` 映射到 `http://localhost:8080/hello`。
* `@ResponseBody` 使其返回純文字（而非 JSP）。

---

### 3. 定義 Spring 配置

由於我們沒有使用 Spring Boot，必須手動配置。

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

這會啟用 Spring MVC 並掃描你的套件以尋找控制器。

---

### 4. 設定 `web.xml`（適用於 Tomcat/Servlet 容器）

如果你要打包成 WAR：

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

這會設定 `DispatcherServlet` 並載入你的 `AppConfig`。

---

### 5. 執行應用程式

* 打包成 WAR 並部署到 Tomcat（或 Jetty）。
* 啟動 Tomcat 並訪問：

  ```
  http://localhost:8080/your-app/hello
  ```
* 你應該會看到：

  ```
  Hello, Spring Web!
  ```

---

👉 請問：你希望這個應用程式在 **Tomcat（WAR 部署）** 中運行，還是偏好使用 **獨立的 `main()` 啟動器**（嵌入式伺服器，類似 Spring Boot 但更精簡）？我可以根據你的設定展示兩種方式。