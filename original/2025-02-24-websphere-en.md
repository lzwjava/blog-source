---
audio: false
generated: false
lang: en
layout: post
title: WebSphere Liberty Server Commands
translated: false
---

When managing a WebSphere Liberty server, several commands are frequently used to perform essential tasks such as creating, starting, stopping, and monitoring the server. Below is a list of the most commonly used commands, along with a brief description of each:

- **`./server create <server_name>`**  
  Creates a new server instance with the specified name. This command sets up the necessary directory structure and default configuration files (e.g., `server.xml`) for the server.

- **`./server start <server_name>`**  
  Starts the server in the background. The server runs as a background process, and logs are written to the server's log files.

- **`./server stop <server_name>`**  
  Stops a running server instance. This command gracefully shuts down the server.

- **`./server status <server_name>`**  
  Checks whether the specified server is running. It returns the current status (e.g., started or stopped).

- **`./server run <server_name>`**  
  Starts the server in the foreground. This is useful for debugging or monitoring, as server output is displayed directly in the console.

- **`./server package <server_name>`**  
  Packages the server, including its configuration and applications, into a zip file. This is helpful for deploying the server to another environment or for backup purposes.

- **`./server debug <server_name>`**  
  Starts the server in debug mode, allowing you to attach a debugger to the server process for troubleshooting.

These commands cover the basic operations needed to manage a WebSphere Liberty server effectively. For more advanced tasks, such as installing features or managing security, additional utilities like `featureUtility` or `securityUtility` are available but are less frequently used in day-to-day operations.