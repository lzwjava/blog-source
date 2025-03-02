---
audio: false
generated: false
lang: zh
layout: post
title: 解决 Eclipse JDK 问题
translated: true
---

当你通过点击 `eclipse.exe` 启动 Eclipse 4.6.3 时，如果遇到错误 "Java was started but returned exit code"，并且引用了 `Oracle\Java\javapath\javaw.exe`，这意味着 Eclipse 正在尝试使用一个不兼容或配置错误的 Java 虚拟机 (JVM)。路径 `Oracle\Java\javapath\javaw.exe` 表明 Eclipse 默认使用系统 PATH 环境变量中定义的 JVM，这可能不适合 Eclipse 4.6.3。要解决这个问题，你需要通过配置 Eclipse 使用兼容的 JVM 来指定正确的 Java 家目录。以下是如何操作的：

### 分步解决方案

1. **了解需求**
   Eclipse 4.6.3 (Neon) 需要至少 Java 8 才能正常运行。错误提示当前 JVM（来自 `Oracle\Java\javapath`）可能不满足这个要求或存在配置问题。你需要将 Eclipse 指向一个兼容的 Java 安装，例如 Java 8 JDK。

2. **定位你的 Java 安装**
   确定系统上安装的兼容 Java 版本（例如 JDK 1.8.0）。Windows 上的常见位置包括：
   - `C:\Program Files\Java\jdk1.8.0_XXX`（用于 64 位 Java）
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX`（用于 32 位 Java）
   将 `XXX` 替换为特定的更新版本（例如 `231` 表示 JDK 1.8.0_231）。在这个目录中，`javaw.exe` 文件位于 `bin` 子目录中（例如 `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`）。

   **提示**：要确认版本和架构，打开命令提示符，导航到 `bin` 目录（例如 `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`），然后运行：
   ```
   java -version
   ```
   在输出中查找 "64-Bit" 或 "32-Bit" 以验证架构。确保它与你的 Eclipse 版本匹配（如果最近下载的，很可能是 64 位）。

3. **找到 `eclipse.ini` 文件**
   `eclipse.ini` 文件是一个配置文件，位于与 `eclipse.exe` 相同的目录中。例如，如果 Eclipse 安装在 `C:\eclipse`，文件将位于 `C:\eclipse\eclipse.ini`。这个文件允许你指定 Eclipse 应该使用的 JVM。

4. **编辑 `eclipse.ini` 文件**
   使用具有管理员权限的文本编辑器（例如记事本）打开 `eclipse.ini`。你将修改它以包含 `-vm` 参数，告诉 Eclipse 使用哪个 JVM。按照以下步骤操作：

   - **检查现有内容**：查找 `-vm` 参数。如果它已经存在，它将在下一行后跟随一个路径（例如 `-vm` 后跟 `C:/some/path/bin/javaw.exe`）。如果它指向问题的 `Oracle\Java\javapath\javaw.exe`，你将替换它。如果不存在 `-vm` 参数，你将添加它。
   - **添加或修改 `-vm` 参数**：在 `-vmargs` 部分（如果存在）之前或文件顶部的初始启动参数之后插入以下两行：
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - 使用正斜杠（`/`）而不是反斜杠（`\`）以避免解析问题。
     - 将 `C:/Program Files/Java/jdk1.8.0_XXX` 替换为你的 Java 安装的实际路径。
   - **确保正确放置**：`-vm` 参数必须出现在 `-vmargs` 部分之前，该部分通常以 `-vmargs` 开头，后跟 JVM 选项，例如 `-Xms256m` 或 `-Xmx1024m`。例如，编辑后的 `eclipse.ini` 可能如下所示：
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **避免额外的空格或空行**：确保 `-vm` 或路径行后没有不必要的空格或空行，因为这可能导致 Eclipse 误解配置。

5. **保存并测试**
   保存 `eclipse.ini` 文件，然后双击 `eclipse.exe` 启动 Eclipse。如果配置正确，Eclipse 应该不会出现 "Java was started but returned exit code" 错误。

### 附加说明
- **架构匹配**：确保 JVM 架构（32 位或 64 位）与你的 Eclipse 安装匹配。64 位 Eclipse 需要 64 位 JVM，通常在 `C:\Program Files\Java` 中找到，而 32 位 Eclipse 需要 32 位 JVM，通常在 `C:\Program Files (x86)\Java` 中找到。
- **验证路径**：双重检查 `javaw.exe` 是否存在于指定位置。如果路径不正确，Eclipse 将无法启动。
- **备用选项**：如果这不奏效，可以考虑设置 `JAVA_HOME` 环境变量（例如 `C:\Program Files\Java\jdk1.8.0_XXX`）并更新系统 PATH 以包括 `%JAVA_HOME%\bin`。然而，修改 `eclipse.ini` 是更可靠的方法。

通过编辑 `eclipse.ini` 文件以包含 `-vm` 参数和指向兼容 `javaw.exe` 的路径，你有效地为 Eclipse 指定了 Java 家目录，确保它使用正确的 JVM 启动。