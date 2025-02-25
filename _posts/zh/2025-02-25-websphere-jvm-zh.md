---
audio: false
lang: zh
layout: post
title: JVM 选项在 WebSphere Liberty 服务器
translated: true
---

要检查 WebSphere Liberty Profile (WLP) 服务器的 `jvm.options` 文件中设置的 JVM 选项，可以使用 Java Development Kit (JDK) 提供的 `jinfo` 命令。这种方法可以高效地验证应用于运行服务器的选项。以下是实现这一目标的分步指南：

### 检查 JVM 选项的步骤

1. **了解上下文**
   服务器目录中的 `jvm.options` 文件（通常位于 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）用于指定 JVM 参数，例如堆大小（例如 `-Xmx`）、垃圾回收设置（例如 `-XX:+UseG1GC`）或系统属性（例如 `-Dmy.property=value`），这些参数在 Liberty 服务器启动时应用。

2. **启动服务器**
   使用以下命令在后台启动您的 Liberty 服务器：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   将 `<WLP_HOME>` 替换为 WebSphere Liberty 安装路径，将 `<serverName>` 替换为服务器名称。此命令将服务器作为后台进程启动。

3. **定位进程 ID (PID)**
   启动服务器后，需要运行 Java 进程的进程 ID。Liberty 方便地将其存储在 `.pid` 文件中，位于：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   打开此文件（例如，在类 Unix 系统上使用 `cat` 或文本编辑器）以检索 PID，这是表示服务器进程的数值。

4. **验证 JVM 标志**
   使用 `jinfo` 命令检查应用于运行服务器的 JVM 标志。运行：
   ```
   jinfo -flags <pid>
   ```
   将 `<pid>` 替换为从 `.pid` 文件中获取的进程 ID。此命令输出传递给 JVM 的命令行标志，例如 `-Xmx1024m` 或 `-XX:+PrintGCDetails`。查看输出以确认您在 `jvm.options` 中设置的标志是否存在。

5. **验证系统属性**
   如果 `jvm.options` 文件包括系统属性（例如 `-Dmy.property=value`），请单独检查它们：
   ```
   jinfo -sysprops <pid>
   ```
   这将显示为 JVM 设置的所有系统属性。搜索输出以找到您定义的特定属性，以确保它们已正确应用。

### 前提条件
- **安装 JDK**：`jinfo` 命令是 JDK 的一部分，而不是 JRE。确保安装了 JDK，并且 `jinfo` 可执行文件在系统的 PATH 中。
- **权限**：使用启动服务器的相同用户运行 `jinfo`，或者具有足够的权限附加到进程。

### 替代方法
如果 `jinfo` 不可用或您更喜欢另一种方法，以下是两种额外选项：

- **使用 `server dump`**：
  1. 使用 `server start <serverName>` 启动服务器。
  2. 使用以下命令生成服务器转储：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 在 `<WLP_HOME>/usr/servers/<serverName>/` 中找到生成的 `.zip` 文件，提取它，并打开 `javacore.<timestamp>.txt` 文件。
  4. 搜索 "CMDLINE" 部分以查看完整的 Java 命令行，包括 JVM 标志，以及 "System Properties" 部分以查看系统属性。

- **跟踪启动脚本**（类 Unix 系统）：
  1. 使用启用跟踪的服务器脚本运行：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 查看输出以找到脚本执行的 Java 命令，其中包括 `jvm.options` 中的所有选项。

### 注意事项
- **服务器未运行**：如果服务器因无效选项而无法启动，请使用 `server run <serverName>` 在前台运行它，并检查控制台输出中的错误，或者使用脚本跟踪方法查看命令。
- **日志文件**：`<WLP_HOME>/usr/servers/<serverName>/logs/` 中的 `console.log` 文件可能包含一些启动信息，但除非启用了详细日志记录（例如 `-XX:+PrintFlagsFinal`），否则它不会可靠地列出所有 JVM 选项。

### 结论
`jinfo` 方法是验证 `jvm.options` 中为运行 Liberty 服务器设置的 JVM 选项的最直接方法。通过遵循上述步骤，您可以确认 JVM 标志和系统属性是否按预期应用。