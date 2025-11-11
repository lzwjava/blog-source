---
audio: false
generated: true
lang: hant
layout: post
title: Spring MVC
translated: true
type: note
---

要在不使用 **Spring Boot** 的情況下使用 **Spring MVC**，您需要手動配置 Spring 框架，因為 Spring Boot 通常會自動化大部分設定。以下將透過基於 XML 配置的方式，逐步指導您建立一個簡單的 Spring MVC 網路應用程式。此範例將設定一個基本應用程式，其中包含一個控制器，用於在 JSP 頁面上顯示「歡迎」訊息。

---

## 逐步指南

### 1. 設定專案結構
建立標準的網路應用程式結構。您可以使用 IntelliJ 或 Eclipse 等 IDE，或手動建立資料夾。結構應如下所示：

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
└── pom.xml  (如果使用 Maven)
```

- **`src/main/java`**：包含您的 Java 原始碼（例如控制器）。
- **`src/main/webapp/WEB-INF`**：包含配置檔案（`web.xml`、`spring-mvc-config.xml`）和 JSP 視圖。

### 2. 添加依賴項
如果您使用 Maven，請在 `pom.xml` 中包含所需的依賴項。對於簡單的 Spring MVC 應用程式，您需要 Spring Web MVC 函式庫和 Servlet API（由容器提供）。

建立或編輯 `pom.xml`，內容如下：

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

- **注意事項**：
  - `<packaging>war</packaging>`：確保專案打包為 WAR 檔案，以便部署到 servlet 容器。
  - 如果您不使用 Maven，請手動下載 Spring MVC JAR 和 Servlet API JAR，並將它們添加到專案的 classpath 中。

### 3. 在 `web.xml` 中配置 DispatcherServlet
`web.xml` 檔案是您的網路應用程式的部署描述符。它配置 `DispatcherServlet`（Spring MVC 的前端控制器）來處理傳入的請求。

建立 `src/main/webapp/WEB-INF/web.xml`，內容如下：

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

- **說明**：
  - `<servlet-class>`：指定 `DispatcherServlet`，它將請求路由到控制器。
  - `<init-param>`：指向 Spring 配置檔案（`spring-mvc-config.xml`）。
  - `<url-pattern>/</url-pattern>`：將 servlet 映射到處理所有應用程式請求。

### 4. 建立 Spring 配置檔案
建立 `src/main/webapp/WEB-INF/spring-mvc-config.xml` 來定義 Spring MVC bean，例如控制器和視圖解析器。

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

- **說明**：
  - `<context:component-scan>`：掃描 `com.example.controllers` 套件以尋找帶註解的組件（例如 `@Controller`）。
  - `<mvc:annotation-driven>`：啟用基於註解的 MVC 功能（例如 `@GetMapping`）。
  - `InternalResourceViewResolver`：將視圖名稱映射到 `/WEB-INF/views/` 中的 JSP 檔案，並使用 `.jsp` 後綴。

### 5. 建立簡單的控制器
建立一個控制器來處理 HTTP 請求。在 `src/main/java/com/example/controllers/` 中添加 `HomeController.java`：

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

- **說明**：
  - `@Controller`：將此類別標記為 Spring MVC 控制器。
  - `@GetMapping("/")`：將 GET 請求映射到根 URL（`/`）到 `home()` 方法。
  - `return "home"`：返回視圖名稱 `"home"`，該名稱將解析為 `/WEB-INF/views/home.jsp`。

### 6. 建立 JSP 視圖
建立一個簡單的 JSP 檔案來顯示輸出。在 `src/main/webapp/WEB-INF/views/` 中添加 `home.jsp`：

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

### 7. 建置和打包應用程式
如果使用 Maven，請從專案根目錄執行以下命令來建置 WAR 檔案：

```bash
mvn clean package
```

這將在 `target` 目錄中生成 `SimpleSpringMVCApp-1.0-SNAPSHOT.war`。

- **注意**：如果不使用 Maven，請編譯 Java 檔案並手動將專案打包成 WAR 檔案，同時保持資料夾結構。

### 8. 部署應用程式
將 WAR 檔案部署到像 Apache Tomcat 這樣的 servlet 容器：
- 將 `SimpleSpringMVCApp-1.0-SNAPSHOT.war` 複製到 Tomcat 安裝目錄的 `webapps` 目錄中。
- 啟動 Tomcat（例如，從 Tomcat 的 `bin` 目錄執行 `startup.sh` 或 `startup.bat`）。

### 9. 存取應用程式
打開瀏覽器並導航至：

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

您應該看到：
```
Welcome to Spring MVC without Spring Boot
```

- **注意**：上下文路徑（`/SimpleSpringMVCApp-1.0-SNAPSHOT`）取決於 WAR 檔案名稱。如果您將 WAR 重新命名為 `myapp.war`，則 URL 變為 `http://localhost:8080/myapp/`。

---

## 總結
要使用 **Spring MVC 而不使用 Spring Boot**：
1. **設定網路專案**，採用標準結構。
2. **添加依賴項**，包括 Spring MVC 和 Servlet API。
3. **在 `web.xml` 中配置 DispatcherServlet**。
4. **在 XML 檔案中定義 Spring 配置**（例如 `spring-mvc-config.xml`）。
5. **建立控制器**來處理請求。
6. **添加 JSP 視圖**以用於回應。
7. **建置並部署** WAR 檔案到 servlet 容器。

這種方法讓您完全控制配置，是學習 Spring MVC 基礎知識的絕佳方式！