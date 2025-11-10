---
audio: false
generated: true
image: false
lang: zh
layout: post
title: Spring Web应用无Boot配置指南
translated: true
type: note
---

明白了。既然你使用的是 **Java 8** 和 **Spring 5.2.2**（这里没有用 Spring Boot，只有核心 Spring + web），你需要手动搭建一个最简化的应用程序。下面是一个简单的示例，展示如何构建一个包含单个控制器的 web 应用。

---

### 1. 添加所需依赖

你已经有了 `spring-context`、`spring-web` 和 `spring-core`。为了处理请求，你还需要 `spring-webmvc`：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. 创建控制器

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

* `@Controller` 告诉 Spring 这是一个 web 控制器。
* `@RequestMapping("/hello")` 映射到 `http://localhost:8080/hello`。
* `@ResponseBody` 使其返回纯文本（而非 JSP）。

---

### 3. 定义 Spring 配置

由于我们没有使用 Spring Boot，必须手动配置。

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

这会启用 Spring MVC 并扫描你的包以寻找控制器。

---

### 4. 设置 `web.xml`（用于 Tomcat/Servlet 容器）

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

这会设置 `DispatcherServlet` 并加载你的 `AppConfig`。

---

### 5. 运行应用

* 打包成 WAR 并部署到 Tomcat（或 Jetty）。
* 启动 Tomcat 并访问：

  ```
  http://localhost:8080/your-app/hello
  ```
* 你应该看到：

  ```
  Hello, Spring Web!
  ```

---

👉 问一下：你希望这个应用在 **Tomcat（WAR 部署）** 中运行，还是更倾向于使用 **独立的 `main()` 启动器**（嵌入式服务器，类似 Spring Boot 但更简化）？我可以根据你的设置展示两种方式。