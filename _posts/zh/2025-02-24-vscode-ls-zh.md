---
audio: false
lang: zh
layout: post
title: Java 语言服务器在 Visual Studio Code
translated: true
---

嘿！`java.jdt.ls.java.home` 设置在 Visual Studio Code (VSCode) 中是一个特定的配置选项，由 Java 语言服务器（作为 "Language Support for Java(TM) by Red Hat" 扩展的一部分，包含在 Java Extension Pack 中）使用。让我们来分解一下：

---

### 它的含义
- **JDT**：代表 "Java Development Tools"，最初是 Eclipse IDE 的一部分。VSCode 中的 Java 语言服务器基于 Eclipse 的 JDT，提供了代码补全、调试和编译等功能。
- **LS**：代表 "Language Server"，一个后台进程，为 VSCode 的 Java 支持提供动力（例如 IntelliSense 和错误检查）。
- **`java.jdt.ls.java.home`**：这个设置告诉 Java 语言服务器在其操作中使用哪个 Java Development Kit (JDK)。它与更广泛的 `java.home` 设置不同，尽管它们是相关的。

简而言之，`java.jdt.ls.java.home` 指定了 Java 语言服务器使用的 JDK 路径，以便：
- 解析你的 Java 代码。
- 提供语言功能（例如自动补全、跳转到定义）。
- 在某些情况下编译和运行代码（尽管编译通常依赖于其他设置或构建工具）。

---

### 与 `java.home` 的区别
- **`java.home`**：VSCode 的一个通用设置，指向所有 Java 相关扩展和任务的 JDK。除非被更具体的设置覆盖，否则会使用它。
- **`java.jdt.ls.java.home`**：一个更具体的设置，覆盖 `java.home` 仅用于 Java 语言服务器。如果没有设置，语言服务器会回退到 `java.home`。

因此，如果你设置了 `java.jdt.ls.java.home`，它将优先用于语言服务器的操作，允许你为语言功能使用不同的 JDK，而不是运行或调试任务。

---

### 如何配置它
既然你在 Windows 上使用 VSCode 1.96.4 和 Java Extension Pack，以下是设置它的方法：

1. **打开设置：**
   - 按 `Ctrl + ,` 打开设置界面，或者使用 `Ctrl + Shift + P` 并输入 **"Open Settings (JSON)"** 来编辑 `settings.json`。

2. **设置路径：**
   - **在设置界面：**
     - 搜索 **"java.jdt.ls.java.home"**。
     - 输入 JDK 的完整路径（例如 `C:\Program Files\Java\jdk-17.0.1`）。
   - **在 settings.json 中：**
     - 添加这行（用你的 JDK 路径替换）：
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - 示例 `settings.json`：
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **验证 JDK 路径：**
   - 确保路径指向包含 `bin` 目录的 JDK 文件夹，其中有 `javac.exe` 和 `java.exe`。

4. **重新加载 VSCode：**
   - 重新加载窗口 (`Ctrl + Shift + P` > "Reload Window") 或重启 VSCode 以应用更改。

---

### 何时使用它
你通常会设置 `java.jdt.ls.java.home` 如果：
- 你安装了多个 JDK，并且希望语言服务器使用特定的一个（例如 JDK 17），而其他 Java 任务（例如运行代码）可能通过 `java.home` 使用不同的 JDK。
- 你在排查语言服务器问题（例如它没有自动选择正确的 JDK）。
- 你的项目对语言功能有特定的 JDK 版本要求。

如果你没有设置它，语言服务器将使用 `java.home` 中的 JDK（或最后使用系统的 `JAVA_HOME` 环境变量）。

---

### 实际示例
假设你安装了 JDK 8 和 JDK 17：
- 设置 `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` 以供一般使用。
- 设置 `"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"` 以确保语言服务器使用 JDK 17 以获得现代 Java 语法支持。

这样，你可以使用 JDK 8 进行调试/运行，但获得 JDK 17 功能的语言支持。

---

这样清楚了吗？如果你想知道这如何适应你的设置，或者需要进一步调整的帮助，请告诉我！ 😊