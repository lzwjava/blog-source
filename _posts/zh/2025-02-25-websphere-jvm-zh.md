---
audio: true
lang: zh
layout: post
title: JVM 选项在 WebSphere Liberty 服务器
translated: true
---

要检查 WebSphere Liberty Profile (WLP) 服务器的 `jvm.options` 文件中设置的 JVM 选项，可以使用 Java Development Kit (JDK) 提供的 `jinfo` 命令。这种方法允许你高效地验证应用于运行服务器的选项。以下是实现这一目标的分步指南：

### 检查 JVM 选项的步骤

1. **了解上下文**
   服务器目录中的 `jvm.options` 文件（通常位于 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）用于指定 JVM 参数，例如堆大小（例如 `-Xmx`）、垃圾回收设置（例如 `-XX:+UseG1GC`）或系统属性（例如 `-Dmy.property=value`），这些参数在 Liberty 服务器启动时应用。

2. **启动服务器**
   使用以下命令在后台启动您的 Liberty 服务器：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   将 `<WLP_HOME>` 替换为 WebSphere Liberty 安装的路径，将 `<serverName>` 替换为您的服务器名称。此命令将服务器启动为后台进程。

3. **定位进程 ID (PID)**
   启动服务器后，您需要运行 Java 进程的进程 ID。Liberty 方便地将其存储在以下位置的 `.pid` 文件中：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   打开此文件（例如，在类 Unix 系统上使用 `cat` 或文本编辑器）以检索 PID，这是表示服务器进程的数值。

4. **验证 JVM 标志**
   使用 `jinfo` 命令检查应用于运行服务器的 JVM 标志。运行：
   ```
   jinfo -flags <pid>
   ```
   将 `<pid>` 替换为从 `.pid` 文件获取的进程 ID。此命令输出传递给 JVM 的命令行标志，例如 `-Xmx1024m` 或 `-XX:+PrintGCDetails`。查看输出以确认您在 `jvm.options` 中设置的标志是否存在。

5. **验证系统属性**
   如果 `jvm.options` 文件包含系统属性（例如 `-Dmy.property=value`），请使用以下命令单独检查它们：
   ```
   jinfo -sysprops <pid>
   ```
   这将显示为 JVM 设置的所有系统属性。搜索输出以找到您定义的特定属性，以确保它们已正确应用。

### 前提条件
- **安装 JDK**：`jinfo` 命令是 JDK 的一部分，而不是 JRE。请确保安装了 JDK，并且 `jinfo` 可执行文件在系统的 PATH 中。
- **权限**：以启动服务器的相同用户运行 `jinfo`，或者具有足够的权限附加到进程。

### 替代方法
如果 `jinfo` 不可用或您更喜欢另一种方法，以下是两种额外选项：

- **使用 `server dump`**：
  1. 使用 `server start <serverName>` 启动服务器。
  2. 使用以下命令生成服务器转储：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 在 `<WLP_HOME>/usr/servers/<serverName>/` 中找到生成的 `.zip` 文件，提取它，并打开 `javacore.<timestamp>.txt` 文件。
  4. 搜索“CMDLINE”部分以查看完整的 Java 命令行，包括 JVM 标志，以及“系统属性”部分以查看系统属性。

- **跟踪启动脚本**（类 Unix 系统）：
  1. 使用启用跟踪的服务器脚本运行：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 审查输出以找到脚本执行的 Java 命令，其中包括 `jvm.options` 中的所有选项。

### 注意事项
- **服务器未运行**：如果服务器因无效选项而无法启动，请使用 `server run <serverName>` 在前台运行它，并检查控制台输出中的错误，或者使用脚本跟踪方法查看命令。
- **日志文件**：`<WLP_HOME>/usr/servers/<serverName>/logs/` 中的 `console.log` 文件可能包含一些启动信息，但除非启用了详细日志记录（例如 `-XX:+PrintFlagsFinal`），否则它不可靠地列出所有 JVM 选项。

### 结论
`jinfo` 方法是验证 `jvm.options` 中为运行 Liberty 服务器设置的 JVM 选项的最直接方法。通过遵循上述步骤，您可以确认 JVM 标志和系统属性是否按预期应用。

---

`jinfo` 命令报告说无法附加到进程。

此外，在使用转储命令后，无法在预期位置（`<WLP_HOME>/usr/servers/<serverName>/`）的提取的 `.zip` 文件中找到 `javacore.<timestamp>.txt` 文件。

WebSphere Liberty 服务器的版本是 24.0.0.9。

---

### 解决 WebSphere Liberty 24.0.0.9 中检查 JVM 选项的问题

您在 WebSphere Liberty Profile (WLP) 服务器版本 24.0.0.9 中使用 `jinfo` 命令检查 JVM 选项时遇到了问题，错误信息显示“无法附加到进程”。此外，在生成服务器转储后，您无法在预期位置（`<WLP_HOME>/usr/servers/<serverName>/`）的提取的 `.zip` 文件中找到 `javacore.<timestamp>.txt` 文件。以下是详细的故障排除和解决问题的指南，确保您可以验证 `jvm.options` 文件中设置的 JVM 选项。

---

### 理解问题

- **`jinfo` 失败**：“无法附加到进程”错误通常意味着 `jinfo` 无法连接到运行的 Java 虚拟机（JVM）。这通常是由于权限问题（例如，以不同于启动服务器的用户运行命令）或对 JVM 进程的限制。
- **缺少 `javacore.<timestamp>.txt`**：服务器转储过程应生成包含诊断文件（包括 `javacore.<timestamp>.txt`）的 `.zip` 文件，但其缺失表明转储失败、文件在意外位置或预期内容未生成。

由于您使用的是 WebSphere Liberty 24.0.0.9，并且根据典型的文件路径，我们将针对类 Unix 系统进行解决方案。

---

### 分步解决方案

以下是多种方法来检索您的 JVM 选项，从 `jinfo` 的最简单替代方案开始，并解决服务器转储问题。

#### 1. 验证服务器正在运行
在继续之前，请确保您的 Liberty 服务器处于活动状态：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server status <serverName>
  ```
- **预期输出**：
  如果正在运行，您将看到类似于“服务器 <serverName> 正在运行，进程 ID 为 <pid>。”的消息。如果没有，请启动它：
  ```bash
  <WLP_HOME>/bin/server start <serverName>
  ```

- **定位 PID**：
  在 `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` 中找到进程 ID，使用：
  ```bash
  cat <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
  ```
  记下此 PID 以便在后续步骤中使用。

#### 2. 使用 `jps -v` 作为 `jinfo` 的替代方案
`jps` 命令（JDK 的一部分）列出 Java 进程及其选项，通常绕过 `jinfo` 遇到的附加问题。

- **命令**：
  ```bash
  jps -v
  ```
- **输出**：
  Java 进程列表，例如：
  ```
  12345 Liberty -Xmx1024m -XX:+UseG1GC -Dmy.property=value
  ```
- **操作**：
  通过匹配 `.pid` 文件中的 PID 或在命令行中查找“Liberty”或您的 `<serverName>` 来识别您的 Liberty 服务器进程。列出的选项（例如 `-Xmx1024m`，`-Dmy.property=value`）包括来自 `jvm.options` 的选项。

- **权限检查**：
  如果 `jps -v` 失败或显示无输出，请以启动服务器的相同用户运行它（例如 `sudo -u <serverUser> jps -v`）或使用 `sudo`：
  ```bash
  sudo jps -v
  ```

#### 3. 使用 `jcmd` 获取详细的 JVM 信息
如果 `jps -v` 不足够，`jcmd`（另一个 JDK 工具）可以在不受 `jinfo` 附加限制的情况下查询运行的 JVM。

- **命令**：
  - 用于 JVM 选项：
    ```bash
    jcmd <pid> VM.command_line
    ```
    输出：完整命令行，例如 `java -Xmx1024m -XX:+UseG1GC -Dmy.property=value ...`
  - 用于系统属性：
    ```bash
    jcmd <pid> VM.system_properties
    ```
    输出：属性列表，例如 `my.property=value`。

- **操作**：
  将 `<pid>` 替换为服务器的 PID。确保您以适当的权限运行这些命令（例如，如果需要，使用 `sudo jcmd <pid> ...`）。

#### 4. 生成并检查 Javacore 文件
由于服务器转储未生成预期的 `javacore.<timestamp>.txt`，请尝试生成独立的 javacore 文件：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server javadump <serverName>
  ```
- **预期输出**：
  显示 javacore 文件位置的消息，通常为 `<WLP_HOME>/usr/servers/<serverName>/javacore.<timestamp>.txt`。

- **操作**：
  - 检查目录：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/javacore.*.txt
    ```
  - 打开文件并搜索：
    - **CMDLINE**：列出 JVM 选项（例如 `-Xmx1024m`）。
    - **系统属性**：列出 `-D` 属性。

- **故障排除**：
  如果没有文件出现，请检查服务器的 `console.log` 或 `messages.log`，位于 `<WLP_HOME>/usr/servers/<serverName>/logs/` 中，以查找命令执行期间的错误。

#### 5. 重新访问服务器转储方法
让我们确保完整的服务器转储正常工作：

- **命令**：
  ```bash
  <WLP_HOME>/bin/server dump <serverName>
  ```
- **预期输出**：
  类似 `<serverName>.dump-<timestamp>.zip` 的 `.zip` 文件，位于 `<WLP_HOME>/usr/servers/<serverName>/`。

- **操作**：
  - 验证文件是否存在：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/*.zip
    ```
  - 提取它：
    ```bash
    unzip <serverName>.dump-<timestamp>.zip -d temp_dir
    ```
  - 搜索 `javacore.<timestamp>.txt`：
    ```bash
    find temp_dir -name "javacore.*.txt"
    ```
  - 打开文件并检查“CMDLINE”和“系统属性”部分。

- **故障排除**：
  - 检查命令的控制台输出以查找错误。
  - 确保服务器在转储期间正在运行（虽然 `server dump` 可以在停止服务器时工作，但 javacore 需要运行的 JVM）。
  - 如果 `.zip` 文件丢失，请查看 `<WLP_HOME>/usr/servers/<serverName>/logs/` 中的日志以获取线索。

#### 6. 启用详细 JVM 输出（最后手段）
如果所有方法都失败，请修改 `jvm.options` 以记录所有 JVM 标志：

- **编辑 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`**：
  添加：
  ```
  -XX:+PrintFlagsFinal
  ```
- **重新启动服务器**：
  ```bash
  <WLP_HOME>/bin/server stop <serverName>
  <WLP_HOME>/bin/server start <serverName>
  ```
- **检查日志**：
  打开 `<WLP_HOME>/usr/servers/<serverName>/logs/console.log`，并搜索 JVM 标志表，例如：
  ```
  [uintx] MaxHeapSize = 1073741824 {product}
  ```

---

### 附加说明

- **权限**：
  `jinfo` 失败表明权限不匹配。始终以启动服务器的相同用户（例如，使用 `sudo -u <serverUser>` 或以该用户身份登录）运行所有命令。
- **WebSphere Liberty 24.0.0.9**：
  转储行为应与文档中所述一致（`.zip` 文件在 `<WLP_HOME>/usr/servers/<serverName>/` 中，包含 `javacore.<timestamp>.txt`）。如果不同，请检查 IBM 的文档以获取版本特定的更改，尽管 `server javadump` 方法仍然可靠。
- **JDK 要求**：
  确保安装了 JDK（而不是仅仅是 JRE），因为 `jps`、`jcmd` 和 `jinfo` 是 JDK 工具。

---

### 推荐方法

1. **首先尝试 `jps -v`**：它快速且可能避免附加问题。
2. **回退到 `jcmd`**：提供详细输出，如果 `jps` 不足够。
3. **使用 `server javadump`**：直接生成 javacore，绕过完整转储的复杂性。
4. **调试转储**：重新运行 `server dump` 并验证 `.zip` 文件的内容（如果需要）。

通过遵循这些步骤，您应该能够成功检索 JVM 选项，并解决 `jinfo` 和缺少 javacore 文件的问题。如果遇到特定错误，请告诉我！