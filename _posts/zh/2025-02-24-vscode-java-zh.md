---
audio: false
generated: false
lang: zh
layout: post
title: 配置 Java 编译器在 Visual Studio Code
translated: true
---

你好！要在 Windows 上的 Visual Studio Code (VSCode) 版本 1.96.4 中配置 Java 编译器，特别是你已经安装了 Java Extension Pack，你需要设置 Java Development Kit (JDK) 路径。Java 编译器是 JDK 的一部分，VSCode 需要知道它的位置以编译你的 Java 代码。以下是一个逐步指南来帮助你设置：

---

### 第 1 步：确保安装了 JDK
在 VSCode 中配置任何内容之前，请确保你在 Windows 机器上安装了 JDK（而不是 JRE）。JDK 包含 Java 编译器（`javac`）。如果你还没有安装，可以从 Oracle、OpenJDK 或 Adoptium（例如 JDK 17 或与你的项目兼容的其他版本）下载。安装后，记下安装路径（例如 `C:\Program Files\Java\jdk-17.0.1`）。

---

### 第 2 步：打开 VSCode 设置
要告诉 VSCode 你的 JDK 位置，你需要调整其设置：

- **通过设置 UI：**
  - 按 `Ctrl + ,` 打开设置面板。
  - 或者，转到 `File > Preferences > Settings`。
- **通过 settings.json（可选）：**
  - 按 `Ctrl + Shift + P` 打开命令面板。
  - 输入 **"Open Settings (JSON)"** 并选择它以直接编辑 `settings.json` 文件。

---

### 第 3 步：使用 `java.home` 设置 JDK 路径
Java Extension Pack 依赖于 `java.home` 设置来定位 JDK 进行编译和语言功能（如 IntelliSense）。以下是如何配置它的方法：

- **在设置 UI 中：**
  - 在设置面板中，搜索 **"java.home"**。
  - 在 "Java: Home" 字段中，输入 JDK 安装的完整路径。例如：
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - 使用反斜杠（`\`），因为你在 Windows 上，并且确保路径指向 JDK 根目录（它应该包含一个包含 `javac.exe` 的 `bin` 文件夹）。

- **在 settings.json 中：**
  - 如果你正在编辑 `settings.json`，添加这行（将路径替换为你的实际 JDK 位置）：
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - 示例完整的 `settings.json`：
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - 编辑后保存文件。

---

### 第 4 步：验证路径
双重检查：
- 路径指向 JDK（而不是 JRE）。JDK 的 `bin` 文件夹应该包含 `javac.exe`。
- 路径中没有拼写错误，并且与你的 JDK 安装位置匹配（例如 `C:\Program Files\Java\jdk-17.0.1`）。

如果你不确定 JDK 安装在哪里，可以在 `C:\Program Files\Java` 或安装过程中选择的位置找到它。

---

### 第 5 步：可选 - 配置多个 JDK
如果你安装了多个 JDK 版本并且想在它们之间切换（例如，一个项目使用 JDK 8，另一个项目使用 JDK 17），可以使用 `java.configuration.runtimes` 设置：

- 将以下内容添加到你的 `settings.json`：
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- `default: true` 选项设置运行代码的默认运行时。然而，对于编译，Java 扩展主要使用 `java.home` 中指定的 JDK。

---

### 第 6 步：重新加载或重启 VSCode
设置 `java.home` 后，你可能需要：
- 重新加载 VSCode 窗口（按 `Ctrl + Shift + P`，输入 **"Reload Window"**，然后选择它）。
- 或者完全重启 VSCode 以使更改生效。

---

### 编译说明
- **单个 Java 文件：** 如果你正在处理单个 `.java` 文件（没有构建工具），Java Extension Pack 的 "Language Support for Java(TM) by Red Hat" 使用 `java.home` 中的 JDK 来编译和运行你的代码。你可以使用 "Run" 按钮或 **"Java: Run"** 命令。
- **使用构建工具的项目：** 如果你使用 Maven、Gradle 或其他构建工具，编译器由构建工具的配置管理（例如 `JAVA_HOME` 环境变量、Maven 的 `pom.xml` 或 Gradle 的 `build.gradle`）。然而，设置 `java.home` 仍然确保 VSCode 的语言功能正常工作。

---

### 故障排除
- **路径问题：** 如果 VSCode 找不到 JDK，请双重检查 `java.home` 中的路径。避免不必要的空格或引号，除非必要。
- **未安装 JDK：** 如果你收到关于缺少 `javac` 的错误，请确保安装了 JDK。
- **版本兼容性：** 确保你的 JDK 版本与项目的要求匹配（例如 JDK 8、11、17）。

---

就是这样！你现在应该已经在 VSCode 中配置了 Java 编译器。如果你遇到任何问题或有更多问题（例如使用特定的构建工具），请随时告诉我，我会很乐意进一步帮助你！ 😊

---

将 `maven.terminal.userJavaHome` 设置为 true。你可以在终端中检查 Java 版本。