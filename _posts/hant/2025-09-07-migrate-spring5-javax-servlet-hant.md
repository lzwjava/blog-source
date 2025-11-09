---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: Spring 5 WAR 遷移至 javax.servlet
translated: true
type: note
---

你已經接近完成了。由於這個專案是 Spring 5（javax.* 時代）且為 WAR 檔，最乾淨的解決方式是：**使用 `javax.servlet-api` 4.x**，添加一個精簡的 `web.xml`、Java 配置和一個小型控制器。

### 0) 修復 servlet API（重要）

Spring 5.2.x 使用 `javax.servlet.*`，但你的 POM 引入了 **`jakarta.servlet-api:5.0.0`**。請替換為 `javax`：

```xml
<!-- 將 jakarta 依賴替換為此 -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

（保留 Jetty 9.4 — 它與 javax 相容且支援 Servlet 3.1/4.0。）

### 1) `web.xml`（因你設定了 `failOnMissingWebXml=true`）

建立 `src/main/webapp/WEB-INF/web.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- 根 Spring 上下文（若後續添加服務/儲存庫） -->
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

  <!-- 用於 MVC 的 DispatcherServlet -->
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

### 2) Java 配置

建立兩個配置類別。

`src/main/java/com/lzw/config/RootConfig.java`：

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // 若後續有服務/儲存庫，可在此添加 @Bean 定義。
}
```

`src/main/java/com/lzw/config/WebConfig.java`：

```java
package com.lzw.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.lzw.web")
public class WebConfig {
    // 若僅需 REST 功能可保留空白。後續如需視圖解析器/靜態資源處理器可再添加。
}
```

### 3) Hello 控制器

`src/main/java/com/lzw/web/HelloController.java`：

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

### 4) 目錄結構檢查

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) 執行

因你已在 POM 中配置 Jetty：

```bash
mvn clean package
mvn jetty:run
```

開啟：`http://localhost:8080/hello` → 應顯示 `Hello, Spring MVC!`。

---

#### 注意事項與常見問題

* 若你**必須**使用 `jakarta.servlet-api:5.x`，則需升級至 Spring 6 / Spring Boot 3+（Jakarta 命名空間）並使用新版 servlet 容器。就當前技術棧（Spring 5.2.2）而言，**請使用 `javax.servlet-api:4.0.1`**。
* 由於你在 `maven-war-plugin` 中設定了 `failOnMissingWebXml=true`，即使 Spring 3.1+ 可在無 `web.xml` 情況下運行，此處仍需要該檔案。
* 後續若需視圖（JSP/Thymeleaf），請在 `WebConfig` 中添加視圖解析器；若僅需 JSON 輸出，上述 `@RestController` 方式已足夠。