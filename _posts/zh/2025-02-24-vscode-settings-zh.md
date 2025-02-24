---
audio: false
lang: zh
layout: post
title: VSCode 设置
translated: true
---

这个 JSON 文件包含各种 VS Code 设置，用于自定义编辑器的行为和外观。以下是每个设置的简要概述：

*   `eslint.autoFixOnSave`：在保存文件时自动修复 ESLint 问题。
*   `java.errors.incompleteClasspath.severity`：配置 VS Code 处理不完整 Java 类路径错误的方式。在这种情况下，它会忽略这些错误。
*   `files.associations`：将特定的文件扩展名与语言关联，以进行语法高亮和语言支持。
*   `emmet.syntaxProfiles`：为特定文件类型定义 Emmet 缩写的语法配置文件。
*   `editor.suggestSelection`：确定编辑器中建议的选择方式。
*   `vsintellicode.modify.editor.suggestSelection`：使用 VS IntelliCode 修改编辑器的建议选择行为。
*   `git.ignoreMissingGitWarning`：禁用缺少 Git 仓库的警告。
*   `python.jediEnabled`：禁用 Jedi 作为 Python 的补全引擎（优先使用 Pylance）。
*   `editor.codeActionsOnSave`：指定保存时运行的代码操作，例如 ESLint 修复。
*   `python.languageServer`：将 Python 语言服务器设置为 Pylance。
*   `editor.renderWhitespace`：控制编辑器中空白字符的渲染方式。
*   `workbench.editorAssociations`：将文件模式与特定编辑器关联。
*   `debug.console.fontSize`：设置调试控制台的字体大小。
*   `terminal.integrated.fontSize`：设置集成终端的字体大小。
*   `terminal.integrated.shell.osx`：指定在 macOS 上使用的 shell。
*   `explorer.confirmDelete`：禁用在 Explorer 中删除文件时的确认对话框。
*   `ruby.codeCompletion`：设置 Ruby 的代码补全引擎。
*   `ruby.intellisense`：配置 Ruby IntelliSense。
*   `C_Cpp.updateChannel`：设置 C/C++ 扩展的更新通道。
*   `editor.formatOnType`：启用输入时的格式化。
*   `[Log]`：针对标识为 "Log" 的文件的特定编辑器设置。
*   `files.exclude`：从 Explorer 中排除指定的文件和文件夹。
*   `redhat.telemetry.enabled`：启用或禁用 Red Hat 遥测。
*   `java.configuration.runtimes`：配置 Java 运行时环境。
*   `java.debug.settings.vmArgs`：设置 Java 调试的 VM 参数。
*   `mssql.connections`：存储 MSSQL 数据库的连接信息。

```json
{
      "eslint.autoFixOnSave": true,
      "java.errors.incompleteClasspath.severity": "ignore",
      "files.associations": {
            "*.vue": "vue",
            "*.wpy": "vue",
            "*.wxml": "html",
            "*.wxss": "css",
            "*.rb": "ruby"
      },
      "emmet.syntaxProfiles": {
            "vue-html": "html",
            "vue": "html"
      },
      "editor.suggestSelection": "first",
      "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
      "git.ignoreMissingGitWarning": true,
      "python.jediEnabled": false,
      "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit"
      },
      "python.languageServer": "Pylance",
      "editor.renderWhitespace": "none",
      "workbench.editorAssociations": {
            "*.ipynb": "jupyter-notebook"
      },
      "debug.console.fontSize": 13,
      "terminal.integrated.fontSize": 14,
      "terminal.integrated.shell.osx": "/bin/zsh",
      "explorer.confirmDelete": false,
      "ruby.codeCompletion": "rcodetools",
      "ruby.intellisense": "rubyLocate",
      "C_Cpp.updateChannel": "Insiders",
      "editor.formatOnType": true,
      "[Log]": {
            "editor.wordWrap": "off"
      },
      "files.exclude": {
            "**/.classpath": true,
            "**/.project": true,
            "**/.settings": true,
            "**/.factorypath": true
      },
      "redhat.telemetry.enabled": true,
      "java.configuration.runtimes": [],
      "java.debug.settings.vmArgs": "-ea",
      "mssql.connections": [
            {
                  "server": "{{put-server-name-here}}",
                  "database": "{{put-database-name-here}}",
                  "user": "{{put-username-here}}",
                  "password": "{{put-password-here}}"
            }
      ],
      "notebook.cellToolbarLocation": {
            "default": "right",
            "jupyter-notebook": "left"
      },
      "java.home": "",
      "java.saveActions.organizeImports": true,
      "java.jdt.ls.vmargs": "-XX:+UseParallelGC -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dsun.zip.disableMemoryMapping=true -Xmx1G -Xms100m -javaagent:\"/Users/lzw/.vscode/extensions/gabrielbb.vscode-lombok-1.0.1/server/lombok.jar\"",
      "editor.accessibilitySupport": "off",
      "security.workspace.trust.untrustedFiles": "newWindow",
      "explorer.confirmDragAndDrop": false,
      "workbench.colorTheme": "One Monokai",
      "C_Cpp.clang_format_fallbackStyle": "WebKit",
      "editor.unicodeHighlight.nonBasicASCII": false,
      "files.autoSave": "afterDelay",
      "grammarly.files.include": [
            "**/*.md"
      ],
      "editor.inlineSuggest.enabled": true,
      "github.copilot.enable": {
            "*": true,
            "yaml": true,
            "plaintext": false,
            "markdown": false
      },
      "yaml.customTags": [
            "!And",
            "!And sequence",
            "!If",
            "!If sequence",
            "!Not",
            "!Not sequence",
            "!Equals",
            "!Equals sequence",
            "!Or",
            "!Or sequence",
            "!FindInMap",
            "!FindInMap sequence",
            "!Base64",
            "!Join",
            "!Join sequence",
            "!Cidr",
            "!Ref",
            "!Sub",
            "!Sub sequence",
            "!GetAtt",
            "!GetAZs",
            "!ImportValue",
            "!ImportValue sequence",
            "!Select",
            "!Select sequence",
            "!Split",
            "!Split sequence"
      ],
      "editor.wordWrap": "on",
      "[python]": {
            "editor.defaultFormatter": "ms-python.autopep8"
      },
      "python.formatting.provider": "none",
      "git.openRepositoryInParentFolders": "never",
      "window.zoomLevel": 1,
      "editor.fontSize": 13,
      "debug.onTaskErrors": "abort",
      "C_Cpp.errorSquiggles": "disabled",
      "cmake.showOptionsMovedNotification": false,
      "editor.formatOnSave": true,
      "autopep8.args": [
            "\"autopep8.args\" = [\"--max-line-length\", \"120\"]"
      ],
      "dart.flutterSdkPath": "/Users/lzwjava/bin/flutter",
      "tabnine.experimentalAutoImports": true,
}
```