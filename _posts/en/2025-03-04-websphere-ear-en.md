---
audio: false
generated: true
lang: en
layout: post
title: EAR Deployment in WebSphere Liberty Profile
translated: false
---

It sounds like you've successfully built an EAR (Enterprise Archive) file using `mvn package` with Maven, and the build process completed without any errors. However, when you deploy this EAR to WebSphere Liberty Profile (WLP) and start the server, you encounter the error "no module found." This is puzzling because a smooth build typically suggests everything is in order, yet the server isn't recognizing your application as expected. Let’s break this down and figure out what might be happening, along with steps to resolve it.

### Understanding the Problem
An EAR file is a standard Java EE archive that packages your application, typically containing one or more modules such as WAR files (for web applications), JAR files (for EJBs or libraries), and a deployment descriptor (`application.xml`). When you deploy an EAR to WLP, the server should detect these modules and start the application. The message "no module found" suggests that WLP either can’t find any modules within your EAR or doesn’t recognize them, preventing the application from starting.

Since your Maven build was successful ("everything is smooth"), the issue likely lies in one of three areas:
1. **The EAR file contents**: The EAR might not contain the expected modules, or the deployment descriptor might be missing or incorrect.
2. **Deployment process**: The way you’re deploying the EAR to WLP might not align with how the server expects to find and process it.
3. **Server configuration**: WLP might not be set up to recognize the modules in your EAR due to missing features or misconfiguration.

Let’s explore these possibilities and provide actionable steps to diagnose and fix the issue.

---

### Possible Causes and Solutions

#### 1. The EAR File Might Be Empty or Incorrectly Packaged
Even though the build was successful, it’s possible that your EAR doesn’t contain any modules (e.g., WAR or JAR files) or that the `application.xml` file, which tells the server what modules are included, is missing or misconfigured.

- **Why this happens**: In a Maven EAR project, the `maven-ear-plugin` is responsible for assembling the EAR. It includes modules based on your `pom.xml` configuration or dependencies. If no modules are specified, or if dependencies (like a WAR) aren’t correctly defined or resolved, the EAR could be empty or lack a proper `application.xml`.
- **How to check**:
  - Open your EAR file (it’s a ZIP archive) using a tool like `unzip` or run `jar tf myApp.ear` in the terminal to list its contents.
  - Look for:
    - Module files (e.g., `my-web.war`, `my-ejb.jar`) at the root of the EAR.
    - A `META-INF/application.xml` file.
  - Inside `application.xml`, you should see entries defining your modules, like:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <application>
        <module>
            <web>
                <web-uri>my-web.war</web-uri>
                <context-root>/myapp</context-root>
            </web>
        </module>
    </application>
    ```
- **How to fix**:
  - Verify your `pom.xml` for the EAR module. Ensure you’ve specified dependencies for the modules you want to include, e.g.:
    ```xml
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-web</artifactId>
            <type>war</type>
        </dependency>
    </dependencies>
    ```
  - Configure the `maven-ear-plugin` if needed:
    ```xml
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.3.0</version>
        <configuration>
            <modules>
                <webModule>
                    <groupId>com.example</groupId>
                    <artifactId>my-web</artifactId>
                    <contextRoot>/myapp</contextRoot>
                </webModule>
            </modules>
        </configuration>
    </plugin>
    ```
  - Rebuild with `mvn clean package` and recheck the EAR contents.

If the EAR is empty or `application.xml` is missing/incorrect, this is likely the root cause. Fixing the Maven configuration should resolve it.

---

#### 2. Deployment Method Issue
How you’re deploying the EAR to WLP could also be the problem. WLP supports two primary deployment methods: the `dropins` directory and explicit configuration in `server.xml`.

- **Using the `dropins` directory**:
  - If you placed the EAR in the `wlp/usr/servers/<serverName>/dropins/` directory, WLP should automatically detect and deploy it.
  - However, for EAR files, automatic deployment might not always work as expected, especially if additional configuration (like context roots) is needed.
- **Using `server.xml`**:
  - For EAR files, it’s often better to explicitly configure the application in `wlp/usr/servers/<serverName>/server.xml`:
    ```xml
    <server>
        <featureManager>
            <feature>servlet-3.1</feature> <!-- Ensure required features are enabled -->
        </featureManager>
        <application id="myApp" name="myApp" type="ear" location="${server.config.dir}/apps/myApp.ear"/>
    </server>
    ```
  - Place the EAR in `wlp/usr/servers/<serverName>/apps/` (or adjust the `location` path accordingly).
- **How to check**:
  - Confirm where you’ve placed the EAR and how you’re starting the server (e.g., `./bin/server run <serverName>`).
  - Check the server logs (e.g., `wlp/usr/servers/<serverName>/logs/console.log` or `messages.log`) for deployment messages.
- **How to fix**:
  - Try configuring the EAR in `server.xml` as shown above instead of relying on `dropins`.
  - Restart the server after making changes: `./bin/server stop <serverName>` followed by `./bin/server start <serverName>`.

If the EAR wasn’t properly registered with the server, this could explain the error.

---

#### 3. Missing Server Features
WLP is a lightweight server that only loads the features you enable in `server.xml`. If your EAR contains modules requiring specific features (e.g., servlets, EJBs), and those features aren’t enabled, WLP might not recognize or load the modules.

- **Why this happens**: For example, a WAR file needs the `servlet-3.1` feature (or higher), while an EJB module needs `ejbLite-3.2`. Without these, the server might fail to process the modules.
- **How to check**:
  - Look at your `server.xml` and check the `<featureManager>` section.
  - Common features include:
    - `<feature>servlet-3.1</feature>` for web modules.
    - `<feature>ejbLite-3.2</feature>` for EJB modules.
  - Review the server logs for messages about missing features (e.g., "required feature is not installed").
- **How to fix**:
  - Add the necessary features to `server.xml` based on your application’s needs:
    ```xml
    <featureManager>
        <feature>servlet-3.1</feature>
        <!-- Add other features as needed -->
    </featureManager>
    ```
  - Restart the server to apply the changes.

If the features are missing, enabling them should allow WLP to recognize the modules.

---

### Diagnostic Steps
To pinpoint the issue, follow these steps:

1. **Inspect the EAR File**:
   - Run `jar tf myApp.ear` or unzip it.
   - Ensure it contains your modules (e.g., `my-web.war`) and a valid `META-INF/application.xml`.

2. **Check the Maven Build**:
   - Review the `pom.xml` of your EAR module to confirm dependencies and `maven-ear-plugin` configuration.
   - Run `mvn clean package` again and check the build output for messages about including modules (e.g., "Adding module my-web.war").

3. **Verify Deployment**:
   - Confirm the EAR’s location (e.g., `dropins` or `apps`).
   - If using `dropins`, try moving it to `apps` and adding it to `server.xml`.

4. **Examine Server Logs**:
   - Start the server and check `console.log` or `messages.log` for detailed error messages beyond "no module found."
   - Look for clues like "application does not contain any modules" or feature-related errors.

5. **Test with a Simple EAR**:
   - Create a basic EAR with a single WAR file using a known working `pom.xml` and deploy it to WLP. If it works, the issue is specific to your original EAR’s packaging.

---

### Most Likely Cause
Given that your build was smooth but WLP reports "no module found," the most probable cause is that **the EAR file doesn’t contain any modules** or **the `application.xml` is missing/incorrect**. This could happen if your `pom.xml` doesn’t properly specify the modules to include, even though Maven didn’t flag an error. Alternatively, if the EAR is correct, the issue might be with deployment (e.g., not configured in `server.xml`) or missing server features.

### Final Recommendation
- Start by checking the EAR’s contents (`jar tf myApp.ear`) and your `pom.xml` configuration.
- If the EAR is empty or lacks `application.xml`, fix the Maven setup and rebuild.
- If the EAR looks correct, configure it in `server.xml`, ensure the required features are enabled, and redeploy.
- Check the server logs for additional context.

By following these steps, you should be able to identify whether the problem is in the build, deployment, or server configuration and get your application running on WLP successfully. Let me know if you need help with specific configurations!