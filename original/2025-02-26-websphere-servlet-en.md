---
audio: false
generated: true
lang: en
layout: post
title: Servlet Version in WebSphere Liberty Profile
translated: false
---

### Understanding the Error

The error message from `console.log` indicates a `DDParser ParseException` related to the `web-fragment.xml` file in the `spring-web-6.2.3.jar`. Specifically, it states that the deployment descriptor specifies version "50" (which corresponds to Servlet 5.0), but the WebSphere Liberty Profile (WLP) server is currently provisioned with version "40" (Servlet 4.0). This mismatch occurs because:

- **Servlet 5.0** is part of Jakarta EE 9 and is required by newer versions of Spring Boot (e.g., Spring Boot 3.x, which includes `spring-web-6.2.3.jar`).
- **Servlet 4.0** is part of Java EE 8, and WLP is likely configured with the `javaee-8.0` feature, which does not support Servlet 5.0.

To fix this, you need to align the Servlet version supported by WLP with the version required by your application. The recommended solution is to update WLP to support Servlet 5.0 by enabling the `jakartaee-9.1` feature.

---

### Solution: Update WLP to Support Servlet 5.0

Here’s how to fix the issue by updating WLP to use the `jakartaee-9.1` feature, which includes support for Servlet 5.0:

#### 1. **Locate the `server.xml` File**
- The `server.xml` configuration file defines the features enabled in WLP.
- It is typically located in the server directory, such as `/opt/ibm/wlp/usr/servers/myServer/server.xml`, where `myServer` is the name of your server.

#### 2. **Edit the `server.xml` File**
- Open the `server.xml` file in a text editor.
- Locate the `<featureManager>` section, which lists the features enabled for the server. It might currently look like this:
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- Replace the `javaee-8.0` feature with `jakartaee-9.1` to enable Servlet 5.0 support:
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- Save the file.

#### 3. **Apply Changes in WLP Development Mode (If Applicable)**
- If you are running WLP in **development mode** (e.g., using the `wlp/bin/server run` command or an IDE integration), you can apply the changes as follows:
  - **Manual Restart:**
    - Stop the server:
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - Start the server again:
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **Development Mode Hot Reload:**
    - If WLP is running in development mode (e.g., via `server run` or an IDE), it may automatically detect changes to `server.xml`. However, to ensure the new feature is loaded, a restart is recommended.

#### 4. **Verify the Fix**
- After restarting the server, redeploy your application (e.g., by copying the WAR file to the `dropins` directory or using your deployment method).
- Check the server logs for confirmation of successful deployment. Look for messages like:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Application myapp started in X.XXX seconds.
  ```
- Access your application (e.g., `http://localhost:9080/myapp/`) to confirm it’s running without errors.

---

### Alternative Solution: Downgrade Spring Boot

If updating WLP to `jakartaee-9.1` is not an option (e.g., due to compatibility constraints with other applications), you can downgrade your Spring Boot application to a version compatible with Servlet 4.0:

#### 1. **Switch to Spring Boot 2.7.x**
- Spring Boot 2.7.x supports Servlet 4.0 (and earlier versions like Servlet 3.1).
- Update your `pom.xml` to use Spring Boot 2.7.x:
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- Use the latest 2.7.x version -->
      <relativePath/>
  </parent>
  ```

#### 2. **Rebuild and Redeploy**
- Rebuild your application:
  ```bash
  mvn clean package
  ```
- Redeploy the generated WAR file to WLP and verify it starts without errors.

---

### Summary
- **Cause of the Error:** Your application (`spring-web-6.2.3.jar`) requires Servlet 5.0, but WLP is configured for Servlet 4.0.
- **Preferred Fix:** Update WLP to use the `jakartaee-9.1` feature by modifying `server.xml` and restarting the server.
- **Alternative Fix:** Downgrade to Spring Boot 2.7.x to match WLP’s Servlet 4.0 support.

The preferred solution (updating WLP) ensures your application can use the latest features of Spring Boot 3.x and Jakarta EE 9. Follow the steps above to resolve the issue and deploy your application successfully.