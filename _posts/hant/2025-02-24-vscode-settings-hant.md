---
audio: true
lang: hant
layout: post
title: VSCode 設定
translated: true
---

這個 JSON 文件包含各種 VS Code 設定，用於自定義編輯器的行為和外觀。以下是每個設定的簡要概述：

*   `eslint.autoFixOnSave`：在保存文件時自動修復 ESLint 問題。
*   `java.errors.incompleteClasspath.severity`：配置 VS Code 如何處理不完整的 Java 類路徑錯誤。在此情況下，忽略它們。
*   `files.associations`：將特定的文件擴展名與語言關聯，以進行語法高亮和語言支持。
*   `emmet.syntaxProfiles`：為特定文件類型定義 Emmet 縮寫的語法配置文件。
*   `editor.suggestSelection`：確定編輯器中建議的選擇方式。
*   `vsintellicode.modify.editor.suggestSelection`：使用 VS IntelliCode 修改編輯器的建議選擇行為。
*   `git.ignoreMissingGitWarning`：禁用缺少 Git 存儲庫的警告。
*   `python.jediEnabled`：禁用 Jedi 作為 Python 的補全引擎（偏好 Pylance）。
*   `editor.codeActionsOnSave`：指定保存時運行的代碼操作，例如 ESLint 修復。
*   `python.languageServer`：將 Python 語言伺服器設置為 Pylance。
*   `editor.renderWhitespace`：控制編輯器中空白的渲染方式。
*   `workbench.editorAssociations`：將文件模式與特定編輯器關聯。
*   `debug.console.fontSize`：設置調試控制台的字體大小。
*   `terminal.integrated.fontSize`：設置集成終端的字體大小。
*   `terminal.integrated.shell.osx`：指定在 macOS 上使用的 shell。
*   `explorer.confirmDelete`：禁用在 Explorer 中刪除文件時的確認對話框。
*   `ruby.codeCompletion`：設置 Ruby 的代碼補全引擎。
*   `ruby.intellisense`：配置 Ruby IntelliSense。
*   `C_Cpp.updateChannel`：設置 C/C++ 擴展的更新頻道。
*   `editor.formatOnType`：啟用輸入時的格式化。
*   `[Log]`：特定編輯器設定，適用於標識為 "Log" 的文件。
*   `files.exclude`：從 Explorer 中排除指定的文件和文件夾。
*   `redhat.telemetry.enabled`：啟用或禁用 Red Hat 遙測。
*   `java.configuration.runtimes`：配置 Java 運行時環境。
*   `java.debug.settings.vmArgs`：設置 Java 调試的 VM 參數。
*   `mssql.connections`：存儲 MSSQL 資料庫的連接信息。

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