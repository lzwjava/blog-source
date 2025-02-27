---
audio: false
lang: zh
layout: post
title: 启用特定文件扩展名的自动换行
translated: true
---

我假设你在问如何配置 Visual Studio Code (VS Code) 以仅对特定文件扩展名启用换行。以下是如何实现的：

1. **打开 VS Code 设置**：
   - 按 `Ctrl + ,`（或 macOS 上的 `Cmd + ,`）打开设置，或者转到 `File > Preferences > Settings`。

2. **使用 JSON 设置文件**：
   - 在设置界面中，点击右上角的 `{}` 图标打开 `settings.json` 文件。这允许更细粒度的控制。

3. **按文件类型配置换行**：
   - 使用 `"[filetype]": {}` 语法添加配置，以指定特定文件扩展名的设置。例如，要仅对 `.md`（Markdown）和 `.txt`（文本）文件启用换行，可以添加如下内容：

   ```json
   {
       "editor.wordWrap": "off", // 默认：所有文件不换行
       "[markdown]": {
           "editor.wordWrap": "on" // 仅对 .md 文件换行
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // 仅对 .txt 文件换行
       }
   }
   ```

4. **说明**：
   - `"editor.wordWrap": "off"` 将全局默认设置为不换行。
   - `"[markdown]"` 和 `"[plaintext]"` 是 Markdown 和纯文本文件的语言标识符，分别。你可以将它们替换为其他语言标识符，如 `[javascript]`、`[python]` 等，具体取决于你想要针对的文件扩展名。
   - `"editor.wordWrap": "on"` 为这些特定文件类型启用换行。

5. **查找语言标识符**：
   - 如果不确定某个文件扩展名的语言标识符，可以在 VS Code 中打开该类型的文件，点击右下角的语言模式（例如，“Plain Text”或“Python”），并在选择语言时命令面板中查看显示的标识符。

6. **保存并测试**：
   - 保存 `settings.json` 文件，VS Code 将立即应用设置。打开不同扩展名的文件以确认行为。

这种方法确保仅对指定的文件类型启用换行，其他文件类型不受影响。如果需要帮助处理特定扩展名，请告诉我！