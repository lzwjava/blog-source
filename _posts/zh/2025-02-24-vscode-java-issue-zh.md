---
audio: false
generated: false
lang: zh
layout: post
title: Java 语言服务器和 Maven 构建
translated: true
---

听起来你在 Visual Studio Code (VSCode) 中遇到了两个相关的问题：一个是关于需要至少 Java 21 的投诉，另一个是 VSCode 不能识别你的 Java 代码中的某些对象定义，尽管你的 Maven 构建成功编译。我们将逐步解决这个问题。

这个问题的根源在于 VSCode 的 Java 扩展（特别是 Java 语言服务器）和你的 Maven 构建在 JDK 版本或项目配置上可能不一致。VSCode 标记需要 JDK 21 才能正常运行，而解析错误表明它没有像 Maven 那样解释你的代码。以下是解决方法：

---

### 步骤 1：安装 JDK 21
由于 VSCode 明确要求 Java 21，你需要确保它已安装在你的系统上。

- **下载 JDK 21**：从可信来源获取，例如 [Oracle 网站](https://www.oracle.com/java/technologies/javase-jdk21-downloads.html) 或 [Adoptium](https://adoptium.net/)。
- **安装它**：按照安装说明进行操作，并记下安装路径（例如，Windows 上的 `C:\Program Files\Java\jdk-21` 或 Linux 上的 `/usr/lib/jvm/java-21-openjdk`）。
- **验证**：打开终端并运行 `java -version`。你应该看到类似于以下内容：
  ```
  java version "21.0.1" ...
  ```

---

### 步骤 2：配置 VSCode 使用 JDK 21
你需要告诉 VSCode 的 Java 扩展使用 JDK 21。以下是如何操作：

1. **打开 VSCode 设置**：
   - 进入 `文件 > 首选项 > 设置`（或按 `Ctrl + ,`）。
2. **设置 JDK 路径**：
   - 搜索 `java.jdt.ls.java.home`。
   - 输入 JDK 21 安装路径（例如，`C:\Program Files\Java\jdk-21`）。
   - 可选地，搜索 `java.home` 并将其设置为相同路径以保持一致。
3. **编辑 `settings.json`（替代方法）**：
   - 打开命令面板（`Ctrl + Shift + P`），输入“首选项：打开设置（JSON）”，并添加：
     ```json
     {
         "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-21",
         "java.home": "C:\\Program Files\\Java\\jdk-21"
     }
     ```
   - 根据你的系统调整路径（Linux/Mac 使用正斜杠 `/`）。

这确保了 VSCode 中的 Java 语言服务器使用 JDK 21，满足最低要求。

---

### 步骤 3：在 VSCode 中设置项目的 JDK
为了修复解析问题（例如，找不到对象定义），确保你的 VSCode 项目也使用 JDK 21：

- 在 `settings.json` 中添加以下内容，以指定项目使用 JDK 21：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-21",
          "path": "C:\\Program Files\\Java\\jdk-21",
          "default": true
      }
  ]
  ```
- 这将 VSCode 的项目运行时与 JDK 21 对齐，这应该有助于它正确解析你的代码。

---

### 步骤 4：验证 Maven 的 JDK 配置
由于你的 Maven 构建（`mvn compile`）运行良好，它可能使用的是兼容的 JDK。让我们确认并与 VSCode 对齐：

1. **检查 Maven 的 JDK**：
   - 在终端中运行 `mvn -version`。查找“Java 版本”行（例如，`Java version: 21.0.1`）。
   - 如果它没有使用 JDK 21，将 `JAVA_HOME` 环境变量设置为 JDK 21 路径：
     - **Windows**：`set JAVA_HOME=C:\Program Files\Java\jdk-21`
     - **Linux/Mac**：`export JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
   - 再次运行 `mvn -version` 以确认。
2. **在 `pom.xml` 中指定 JDK**（可选）：
   - 如果你想在 Maven 项目中强制使用 JDK 21，将以下内容添加到你的 `pom.xml`：
     ```xml
     <properties>
         <maven.compiler.source>21</maven.compiler.source>
         <maven.compiler.target>21</maven.compiler.target>
     </properties>
     ```

---

### 步骤 5：刷新 VSCode
完成这些更改后，VSCode 需要刷新以应用它们：

- 重新加载 VSCode：
  - 打开命令面板（`Ctrl + Shift + P`）并选择“开发者：重新加载窗口”。
- 或者，关闭并重新打开 VSCode。

---

### 步骤 6：确保依赖项已加载
如果 VSCode 仍然找不到对象定义，它可能没有正确加载 Maven 依赖项：

1. **清理工作区**：
   - 打开命令面板（`Ctrl + Shift + P`）。
   - 运行“Java: 清理 Java 语言服务器工作区”。
2. **强制编译**：
   - 从命令面板运行“Java: 强制 Java 编译”。
3. **检查导入**：
   - 确保你的项目的 Maven 依赖项已导入，右键点击 VSCode 中的 `pom.xml` 并选择“更新项目配置”。

---

### 故障排除
如果问题仍然存在：
- **检查日志**：
  - 将 `"java.trace.server": "verbose"` 添加到 `settings.json`。
  - 打开输出面板（`Ctrl + Shift + U`）并选择“Java 语言服务器”以查看详细日志。
- **验证代码**：
  - 双重检查缺失的对象定义是否来自你的代码或 `pom.xml` 中列出的依赖项，而不是外部问题。

---

### 总结
通过安装 JDK 21、配置 VSCode 使用它、对齐项目和 Maven 设置，并刷新环境，VSCode 应该停止投诉 Java 21 并正确解析你的代码，与 Maven 的成功编译匹配。如果你遇到任何问题，请告诉我！