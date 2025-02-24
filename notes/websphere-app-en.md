---
audio: false
lang: en
layout: post
title: WebSphere Liberty - Hello World Application
translated: false
---

Here’s a simple example to run a "Hello World" application on your WebSphere Liberty server, assuming you’ve already set it up with the `javaee-8.0` feature enabled as per previous instructions. This example uses a basic JSP (JavaServer Pages) file and deploys it using the `dropins` directory for simplicity.

### Step-by-Step Guide

#### 1. Create the Application Directory and File
You’ll create a small web application by placing a JSP file in the `dropins` directory of your Liberty server. The `dropins` directory allows Liberty to automatically detect and deploy applications.

- **Locate the `dropins` directory**: 
  Navigate to the `dropins` directory within your server’s folder. If your Liberty installation is located at `/opt/ibm/wlp` and your server is named `myServer`, the path is:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```
  Replace `/opt/ibm/wlp` with your actual Liberty installation directory and `myServer` with your server’s name.

- **Create an exploded WAR directory**: 
  Inside the `dropins` directory, create a directory named `myApp.war`. The `.war` extension tells Liberty to treat this as a web application. Use this command:
  ```bash
  mkdir -p /opt/ibm/wlp/usr/servers/myServer/dropins/myApp.war
  ```

- **Create the `index.jsp` file**: 
  Inside `myApp.war`, create a file named `index.jsp` with the following content to display "Hello World!":
  ```jsp
  <html>
  <body>
  <h2>Hello World!</h2>
  </body>
  </html>
  ```
  You can create it directly with a command like:
  ```bash
  echo '<html><body><h2>Hello World!</h2></body></html>' > /opt/ibm/wlp/usr/servers/myServer/dropins/myApp.war/index.jsp
  ```
  Alternatively, use a text editor to create `index.jsp` and save it in that location.

#### 2. Start the Server (if Not Already Running)
If your server isn’t running, you need to start it so it can deploy and serve the application.

- **Navigate to the `bin` directory**: 
  Go to the `bin` directory in your Liberty installation:
  ```bash
  cd /opt/ibm/wlp/bin
  ```

- **Start the server**: 
  Run the server in foreground mode to see the output directly:
  ```bash
  ./server run myServer
  ```
  Alternatively, start it in the background:
  ```bash
  ./server start myServer
  ```
  If the server is already running, skip this step—Liberty will detect the new application automatically.

#### 3. Verify Application Deployment
Liberty will deploy the `myApp.war` application automatically when it detects it in the `dropins` directory.

- **Check the console output**: 
  If you started the server in foreground mode, watch for a message like:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myApp/
  ```
  This confirms the application is deployed and available.

- **Check logs (if running in background)**: 
  If the server is running in the background, look in the log file at:
  ```
  /opt/ibm/wlp/usr/servers/myServer/logs/console.log
  ```
  for the same deployment message.

#### 4. Access the Application
Now that the application is deployed, you can view it in a web browser.

- **Open your browser**: 
  Navigate to:
  ```
  http://localhost:9080/myApp/
  ```
  The context root `/myApp` comes from the `myApp.war` directory name, and `index.jsp` is served by default as a welcome file.

- **Expected result**: 
  You should see a page displaying:
  ```
  Hello World!
  ```
  in large text.

### Notes
- **Port number**: This example uses port `9080`, the default HTTP port for Liberty. If you’ve configured a different port, adjust the URL accordingly (e.g., `http://localhost:YOUR_PORT/myApp/`).
- **Permissions**: Ensure you have write permissions to the `dropins` directory.
- **JSP support**: The `javaee-8.0` feature includes JSP support, so no additional configuration is needed.
- **Troubleshooting**: If the page doesn’t load, check the server logs at `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` for errors, or ensure the server is running and the files are in the correct location.

This simple example demonstrates how to deploy and run a "Hello World" application on your WebSphere Liberty server using the `dropins` directory for automatic deployment. Enjoy your first Liberty application!