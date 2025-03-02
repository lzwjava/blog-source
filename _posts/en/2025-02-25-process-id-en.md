---
audio: false
generated: false
lang: en
layout: post
title: Process ID (PID) Of The Running Server
translated: false
---

Since you are using WebSphere Liberty Profile (WLP) version 24.0.0.9 and need to find the Process ID (PID) of the running server, but you’ve indicated that the expected `.pid` file at `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` is not available, here’s how you can locate the PID using alternative methods.

The standard approach outlined in the instructions relies on Liberty storing the PID in a `.pid` file after the server starts. However, if this file is missing—possibly due to a configuration issue, a failed startup, or a different installation setup—you can still identify the PID using system tools, assuming the server is running. Below are reliable steps to find the PID on a Unix-like system (e.g., Linux). If you’re using Windows, let me know, and I can adjust the instructions accordingly.

### Step 1: Confirm the Server is Running
Before searching for the PID, ensure the Liberty server is active. You can:
- **Check the logs**: Look in `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` or `messages.log` for startup messages, such as "Server <serverName> started."
- **Access the server**: If it hosts a web application, try accessing it via a browser (e.g., `http://localhost:<port>`).

If the server isn’t running, there won’t be a PID to find, so this step is crucial.

### Step 2: Use System Commands to Find the PID
Since the `.pid` file is unavailable, you can use command-line tools to locate the Java process associated with the Liberty server. Liberty runs as a Java process, so tools that list Java or network processes can help. Here are two effective methods:

#### Method 1: Using `ps` to List Java Processes
The `ps` command displays running processes. To filter for Java processes, including the Liberty server, run:
```bash
ps -ef | grep java
```
This lists all processes with "java" in their command line. The output might look like:
```
user  12345  1  0  10:00 ?  00:00:00 /path/to/java -jar /path/to/liberty/wlp/bin/tools/ws-server.jar <serverName>
```
- The second column (e.g., `12345`) is the PID.
- Look for a line mentioning "liberty," "wlp," or your `<serverName>` (e.g., `defaultServer`) to identify the correct process.

To narrow it down further, if you know the server name, try:
```bash
ps -ef | grep <serverName>
```

#### Method 2: Using `jps` (Java-Specific Tool)
If you have the Java Development Kit (JDK) installed, the `jps` command is a simpler way to list Java processes. Run:
```bash
jps -l
```
The output might look like:
```
12345 com.ibm.ws.kernel.boot.Launcher
```
- The first column (e.g., `12345`) is the PID.
- Look for a class name related to Liberty, such as `com.ibm.ws.kernel.boot.Launcher`, which is commonly associated with Liberty’s startup.

This method is often cleaner than `ps` since it only shows Java processes.

### Step 3: Optional - Use Port Number (if Known)
If you know the port number the Liberty server is listening on (e.g., from `server.xml` or logs), you can use `netstat` to find the PID:
```bash
netstat -anp | grep <port_number>
```
Output might include:
```
tcp  0  0  0.0.0.0:<port_number>  0.0.0.0:*  LISTEN  12345/java
```
- The PID (e.g., `12345`) appears after the port details.

### Recommendation
- **Preferred Method**: Use `jps -l` if the JDK is available, as it’s tailored for Java processes and likely identifies the Liberty server clearly.
- **Fallback**: Use `ps -ef | grep java` if `jps` isn’t an option, and manually identify the Liberty process by inspecting the command details.

### Troubleshooting Tips
If neither command finds the Liberty process:
- Double-check the server is running (Step 1).
- Verify your `<WLP_HOME>` and `<serverName>` paths; the process might reference an unexpected directory.
- Restart the server with `server start <serverName>` and check if the `.pid` file appears, or look at startup logs for clues about why it’s missing.

Using these steps, you should be able to locate the PID of your running Liberty 24.0.0.9 server despite the absent `.pid` file. Let me know if you need further assistance!