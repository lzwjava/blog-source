---
audio: false
lang: en
layout: post
title: JVM options in WebShpere Liberty Server
translated: false
---

To check the JVM options set in the `jvm.options` file located in the server directory of a WebSphere Liberty Profile (WLP) server, you can use the `jinfo` command provided by the Java Development Kit (JDK). This method allows you to verify the options applied to a running server efficiently. Below is a step-by-step guide to accomplish this:

### Steps to Check JVM Options

1. **Understand the Context**  
   The `jvm.options` file in the server directory (typically `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) is used to specify JVM arguments, such as heap size (e.g., `-Xmx`), garbage collection settings (e.g., `-XX:+UseG1GC`), or system properties (e.g., `-Dmy.property=value`), which are applied when the Liberty server starts.

2. **Start the Server**  
   Begin by starting your Liberty server in the background using the following command:  
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```  
   Replace `<WLP_HOME>` with the path to your WebSphere Liberty installation and `<serverName>` with the name of your server. This command launches the server as a background process.

3. **Locate the Process ID (PID)**  
   After starting the server, you need the process ID of the running Java process. Liberty conveniently stores this in a `.pid` file located at:  
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```  
   Open this file (e.g., using `cat` on Unix-like systems or a text editor) to retrieve the PID, which is a numeric value representing the server’s process.

4. **Verify JVM Flags**  
   Use the `jinfo` command to inspect the JVM flags applied to the running server. Run:  
   ```
   jinfo -flags <pid>
   ```  
   Replace `<pid>` with the process ID obtained from the `.pid` file. This command outputs the command-line flags passed to the JVM, such as `-Xmx1024m` or `-XX:+PrintGCDetails`. Look through the output to confirm that the flags you set in `jvm.options` are present.

5. **Verify System Properties**  
   If your `jvm.options` file includes system properties (e.g., `-Dmy.property=value`), check them separately with:  
   ```
   jinfo -sysprops <pid>
   ```  
   This displays all system properties set for the JVM. Search the output for the specific properties you defined to ensure they were applied correctly.

### Prerequisites
- **JDK Installed**: The `jinfo` command is part of the JDK, not the JRE. Ensure you have a JDK installed and that the `jinfo` executable is in your system’s PATH.
- **Permissions**: Run `jinfo` with the same user that started the server or with sufficient privileges to attach to the process.

### Alternative Methods
If `jinfo` is unavailable or you prefer another approach, here are two additional options:

- **Using `server dump`**:  
  1. Start the server with `server start <serverName>`.  
  2. Generate a server dump using:  
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```  
  3. Locate the generated `.zip` file in `<WLP_HOME>/usr/servers/<serverName>/`, extract it, and open the `javacore.<timestamp>.txt` file.  
  4. Search for the "CMDLINE" section to see the full Java command line, including JVM flags, and the "System Properties" section for system properties.

- **Tracing the Startup Script** (Unix-like systems):  
  1. Run the server script with tracing enabled:  
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```  
  2. Review the output to find the Java command executed by the script, which includes all options from `jvm.options`.

### Notes
- **Server Not Running**: If the server fails to start due to invalid options, use `server run <serverName>` to run it in the foreground and check the console output for errors, or use the script tracing method to see the command.
- **Log Files**: The `console.log` file in `<WLP_HOME>/usr/servers/<serverName>/logs/` may contain some startup information, but it doesn’t reliably list all JVM options unless verbose logging is enabled (e.g., `-XX:+PrintFlagsFinal`).

### Conclusion
The `jinfo` method is the most straightforward way to verify the JVM options set in `jvm.options` for a running Liberty server. By following the steps above, you can confirm both JVM flags and system properties are applied as intended.

---

The `jinfo` command reported that it could not attach to the process.

Additionally, the `javacore.<timestamp>.txt` file could not be found after using the dump command.

The version of WebSphere Liberty Server is 24.0.0.9.
