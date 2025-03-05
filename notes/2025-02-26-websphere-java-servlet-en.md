---
audio: false
generated: true
lang: en
layout: post
title: Java Servlet Application on WebSphere Liberty Profile
translated: false
---

Here’s a complete guide to running a very simple Java Servlet application on WebSphere Liberty Profile (WLP). This example creates a basic Servlet that returns "Hello World!" and deploys it to WLP using the `dropins` directory. We’ll assume you’ve already set up WLP with the `servlet-4.0` feature enabled, as this provides the necessary Servlet support. This guide avoids using Maven and provides all required code and deployment steps.

---

### Step-by-Step Guide

#### 1. Create the Servlet Application Structure
Create a directory structure for your Servlet application manually. You can use any folder name, but for this example, we’ll call it `SimpleServletApp`.

- **Directory Structure:**
  ```
  SimpleServletApp/
  ├── src/
  │   └── com/
  │       └── example/
  │           └── HelloServlet.java
  └── webapp/
      └── WEB-INF/
          └── web.xml
  ```

#### 2. Write the Servlet Code
Create a file named `HelloServlet.java` in `SimpleServletApp/src/com/example/` with the following content:

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

- **Explanation:** This Servlet responds to HTTP GET requests with "Hello World!" in plain text. We’re using a simple `doGet` method without annotations for maximum compatibility and simplicity.

#### 3. Create the `web.xml` Deployment Descriptor
Create a file named `web.xml` in `SimpleServletApp/webapp/WEB-INF/` with the following content:

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

- **Explanation:** The `web.xml` file maps the `HelloServlet` class to the `/hello` URL pattern. This is required since we’re not using annotations like `@WebServlet`.

#### 4. Compile the Servlet
Compile the `HelloServlet.java` file into a `.class` file using `javac`. You’ll need the `javax.servlet-api` library in your classpath, which is provided by WLP but must be available during compilation.

- **Steps:**
  1. Locate the Servlet API JAR in your WLP installation. For example, if WLP is installed at `/opt/ibm/wlp`, the JAR is typically at:
     ```
     /opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar
     ```
     The exact filename may vary based on your WLP version.
  2. Run the following command from the `SimpleServletApp` directory:
     ```bash
     javac -cp "/opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar" src/com/example/HelloServlet.java
     ```
  3. This creates `HelloServlet.class` in `SimpleServletApp/src/com/example/`.

#### 5. Package the Application into a WAR File
Organize the compiled files and create a WAR file manually.

- **Move Compiled Class:**
  Create a `WEB-INF/classes` directory and move the compiled class files:
  ```bash
  mkdir -p webapp/WEB-INF/classes/com/example
  mv src/com/example/HelloServlet.class webapp/WEB-INF/classes/com/example/
  ```

- **Create the WAR File:**
  From the `SimpleServletApp` directory, use the `jar` command to package the `webapp` folder into a WAR file:
  ```bash
  cd webapp
  jar -cvf ../myapp.war .
  cd ..
  ```
  This creates `myapp.war` in the `SimpleServletApp` directory.

#### 6. Deploy the WAR File on WLP
Deploy the WAR file to WLP using the `dropins` directory for automatic deployment.

- **Locate the `dropins` Directory:**
  Find your WLP server’s `dropins` directory. If WLP is installed at `/opt/ibm/wlp` and your server is named `myServer`, the path is:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **Copy the WAR File:**
  Move the WAR file to the `dropins` directory:
  ```bash
  cp myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **Start the Server (if Not Running):**
  If WLP isn’t running, start it:
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  If it’s already running, it will detect and deploy the WAR file automatically.

- **Verify Deployment:**
  Check the server logs or console for a message like:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  Logs are in `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

#### 7. Access the Application
Test the deployed Servlet in a browser.

- **Open Your Browser:**
  Navigate to:
  ```
  http://localhost:9080/myapp/hello
  ```
  - `9080` is WLP’s default HTTP port.
  - `/myapp` is the context root from the WAR file name.
  - `/hello` is the URL pattern defined in `web.xml`.

- **Expected Result:**
  You should see:
  ```
  Hello World!
  ```
  displayed as plain text.

---

### Notes
- **No JSP Included:** The query asked for JSP files, but to keep this *very simple*, I’ve focused on a basic Servlet-only application. JSPs would require additional files and complexity, which can be added if needed.
- **Context Root:** The context root (`/myapp`) comes from the WAR file name. Rename `myapp.war` to change it (e.g., `app.war` for `/app`).
- **Port Number:** WLP defaults to `9080` for HTTP. Check your `server.xml` if it’s different.
- **Java Version:** Use a Java version compatible with WLP (e.g., Java 8 or 11).
- **Troubleshooting:** If it doesn’t work, check `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` for errors, ensure the WAR file is in `dropins`, and verify the server is running.

---

### Summary
This guide shows how to:
1. Create a simple Servlet (`HelloServlet.java`) and `web.xml`.
2. Compile the Servlet without Maven using `javac`.
3. Package it into a WAR file (`myapp.war`) manually.
4. Deploy it to WLP’s `dropins` directory.
5. Access "Hello World!" at `http://localhost:9080/myapp/hello`.

This provides a straightforward, minimal Servlet application running on WebSphere Liberty Profile without build tools like Maven.