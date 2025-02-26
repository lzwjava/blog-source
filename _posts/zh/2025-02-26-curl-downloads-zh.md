---
audio: false
lang: zh
layout: post
title: curl下载故障排除
translated: true
---

当你尝试使用 `curl -O` 从 eclipse.org 下载 Eclipse ZIP 文件时，可能会遇到一个问题，即下载的是 HTML 文件而不是所需的 ZIP 文件，并伴随着一个 "301 Moved Permanently" 错误。这是因为你使用的 URL 正在重定向到另一个位置，而 `curl` 没有自动跟随该重定向到实际的文件。以下是如何解决这个问题的方法：

### 理解问题

- **301 Moved Permanently**：这个 HTTP 状态码表示资源（ZIP 文件）已经永久移动到一个新的 URL。服务器通常使用重定向来指向镜像站点或更新的位置。
- **`curl -O` 行为**：`-O` 选项告诉 `curl` 将下载的内容保存到一个以远程文件命名的文件中。然而，如果不显式处理重定向，`curl` 可能会保存中间重定向响应的内容（通常是一个 HTML 页面），而不是跟随它到 ZIP 文件。

### 解决方案

为了确保 `curl` 跟随重定向并下载 Eclipse ZIP 文件，请使用 `-L` 选项与 `-O` 一起使用。`-L` 标志指示 `curl` 跟随任何重定向，直到到达最终目的地。

#### 命令

```bash
curl -L -O <URL>
```

- **`-L`**：跟随重定向，例如 301 重定向，到新位置。
- **`-O`**：使用最终 URL 的原始名称保存文件。
- **`<URL>`**：将其替换为特定的 Eclipse 下载 URL，例如 `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`。

### 逐步说明

1. **找到正确的 URL**：
   - 访问 Eclipse 网站（例如 `https://www.eclipse.org/downloads/`）。
   - 选择所需的软件包（例如 Eclipse IDE for Java Developers）。
   - 右键点击下载链接或按钮并复制 URL。或者，使用浏览器的开发者工具（F12，Network 选项卡）在点击下载时捕获精确的 URL。

2. **运行命令**：
   - 打开终端。
   - 使用 `-L` 和 `-O` 选项执行 `curl` 命令，使用你复制的 URL：
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - 这应该会将 ZIP 文件（例如 `eclipse-java-2023-03-R-win32-x86_64.zip`）下载到你的当前目录。

### 故障排除

如果你仍然遇到问题，请尝试以下额外步骤：

- **使用详细输出检查重定向**：
  - 使用 `-v` 选项查看请求和重定向的详细信息：
    ```bash
    curl -v -L -O <URL>
    ```
  - 查看 301 响应中的 `Location` 头，看看它重定向到哪里。如果它指向的是 HTML 页面而不是 ZIP 文件，URL 可能不是直接下载链接。

- **验证 URL**：
  - Eclipse 通常使用 `download.php` 脚本，可能会重定向到一个镜像。确保你的 URL 要么是直接指向 ZIP 文件的链接，要么是重定向链接，最终解析为文件。例如，直接镜像链接可能看起来像：
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **设置 User-Agent 头**：
  - 一些服务器根据客户端的不同行为不同。如果服务器返回 HTML 因为它检测到 `curl`，可以通过添加 User-Agent 来模仿浏览器：
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### 为什么有效

Eclipse 网站可能会将下载请求重定向到镜像或更新的 URL。没有 `-L`，`curl -O` 会保存重定向响应（HTML 页面），而不是跟随它到实际的 ZIP 文件。添加 `-L` 确保 `curl` 跟踪 301 重定向到实际的 ZIP 文件，解决了问题。

通过遵循这些步骤，你应该能够成功从 eclipse.org 使用 `curl` 下载 Eclipse ZIP 文件。