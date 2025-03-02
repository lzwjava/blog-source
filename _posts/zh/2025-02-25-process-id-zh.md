---
audio: false
generated: false
lang: zh
layout: post
title: 运行服务器的进程 ID (PID)
translated: true
---

你正在使用 WebSphere Liberty Profile (WLP) 版本 24.0.0.9，并且需要找到正在运行的服务器的进程 ID (PID)，但你指出预期的 `.pid` 文件在 `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` 位置不存在，以下是如何使用替代方法定位 PID。

标准方法依赖于 Liberty 在服务器启动后将 PID 存储在 `.pid` 文件中。然而，如果该文件丢失——可能是由于配置问题、启动失败或不同的安装设置——你仍然可以使用系统工具来识别 PID，假设服务器正在运行。以下是在类 Unix 系统（例如 Linux）上找到 PID 的可靠步骤。如果你使用的是 Windows，请告诉我，我可以相应地调整说明。

### 步骤 1：确认服务器正在运行
在搜索 PID 之前，请确保 Liberty 服务器处于活动状态。你可以：
- **检查日志**：在 `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` 或 `messages.log` 中查找启动消息，例如 "Server <serverName> started."
- **访问服务器**：如果它托管一个 Web 应用程序，请尝试通过浏览器访问它（例如 `http://localhost:<port>`）。

如果服务器没有运行，则没有 PID 可找，因此这一步是至关重要的。

### 步骤 2：使用系统命令找到 PID
由于 `.pid` 文件不可用，你可以使用命令行工具来定位与 Liberty 服务器相关联的 Java 进程。Liberty 作为 Java 进程运行，因此列出 Java 或网络进程的工具可以帮助。以下是两种有效的方法：

#### 方法 1：使用 `ps` 列出 Java 进程
`ps` 命令显示正在运行的进程。要过滤 Java 进程，包括 Liberty 服务器，请运行：
```bash
ps -ef | grep java
```
这将列出命令行中包含 "java" 的所有进程。输出可能如下所示：
```
user  12345  1  0  10:00 ?  00:00:00 /path/to/java -jar /path/to/liberty/wlp/bin/tools/ws-server.jar <serverName>
```
- 第二列（例如 `12345`）是 PID。
- 查找提到 "liberty"、"wlp" 或你的 `<serverName>`（例如 `defaultServer`）的行，以识别正确的进程。

如果你知道服务器名称，可以进一步缩小范围：
```bash
ps -ef | grep <serverName>
```

#### 方法 2：使用 `jps`（专用于 Java 的工具）
如果你安装了 Java 开发工具包（JDK），`jps` 命令是列出 Java 进程的更简单方法。运行：
```bash
jps -l
```
输出可能如下所示：
```
12345 com.ibm.ws.kernel.boot.Launcher
```
- 第一个列（例如 `12345`）是 PID。
- 查找与 Liberty 相关的类名，例如 `com.ibm.ws.kernel.boot.Launcher`，这是与 Liberty 启动常关联的。

这种方法通常比 `ps` 更干净，因为它只显示 Java 进程。

### 步骤 3：可选 - 使用端口号（如果已知）
如果你知道 Liberty 服务器监听的端口号（例如从 `server.xml` 或日志中），可以使用 `netstat` 找到 PID：
```bash
netstat -anp | grep <port_number>
```
输出可能包括：
```
tcp  0  0  0.0.0.0:<port_number>  0.0.0.0:*  LISTEN  12345/java
```
- PID（例如 `12345`）出现在端口详细信息之后。

### 建议
- **首选方法**：如果有 JDK 可用，使用 `jps -l`，因为它专为 Java 进程设计，并且可能清晰地识别 Liberty 服务器。
- **备用方法**：如果 `jps` 不是选项，使用 `ps -ef | grep java`，并通过检查命令详细信息手动识别 Liberty 进程。

### 故障排除提示
如果两个命令都找不到 Liberty 进程：
- 双重检查服务器是否正在运行（步骤 1）。
- 验证你的 `<WLP_HOME>` 和 `<serverName>` 路径；进程可能引用意外的目录。
- 使用 `server start <serverName>` 重新启动服务器，并检查 `.pid` 文件是否出现，或者查看启动日志以获取有关其缺失原因的线索。

使用这些步骤，你应该能够在没有 `.pid` 文件的情况下找到运行的 Liberty 24.0.0.9 服务器的 PID。如果需要进一步的帮助，请告诉我！