---
audio: false
generated: true
lang: hant
layout: post
title: VSCode 設定
translated: true
type: note
---

此 JSON 檔案包含多種 VS Code 設定，用於自訂編輯器的行為和外觀。以下簡要說明每個設定的功能：

*   `eslint.autoFixOnSave`：在儲存檔案時自動修復 ESLint 問題。
*   `java.errors.incompleteClasspath.severity`：設定 VS Code 如何處理不完整的 Java 類別路徑錯誤。此處設定為忽略。
*   `files.associations`：將特定副檔名與語言關聯，以提供語法突顯和語言支援。
*   `emmet.syntaxProfiles`：為特定檔案類型定義 Emmet 縮寫的語法設定檔。
*   `editor.suggestSelection`：決定編輯器中建議項目的選取方式。
*   `vsintellicode.modify.editor.suggestSelection`：使用 VS IntelliCode 修改編輯器的建議選取行為。
*   `git.ignoreMissingGitWarning`：停用缺少 Git 儲存庫的警告。
*   `python.jediEnabled`：停用 Jedi 作為 Python 的自動完成引擎（偏好使用 Pylance）。
*   `editor.codeActionsOnSave`：指定在儲存時執行的程式碼動作，例如 ESLint 修復。
*   `python.languageServer`：將 Python 語言伺服器設定為 Pylance。
*   `editor.renderWhitespace`：控制編輯器中空白字元的顯示方式。
*   `workbench.editorAssociations`：將檔案模式與特定編輯器關聯。
*   `debug.console.fontSize`：設定偵錯主控台的字型大小。
*   `terminal.integrated.fontSize`：設定整合式終端機的字型大小。
*   `terminal.integrated.shell.osx`：指定在 macOS 上使用的 shell。
*   `explorer.confirmDelete`：停用在檔案總管中刪除檔案時的確認對話框。
*   `ruby.codeCompletion`：設定 Ruby 的程式碼自動完成引擎。
*   `ruby.intellisense`：設定 Ruby IntelliSense。
*   `C_Cpp.updateChannel`：設定 C/C++ 擴充功能的更新頻道。
*   `editor.formatOnType`：啟用輸入時自動格式化。
*   `[Log]`：針對識別為 "Log" 的檔案之特定編輯器設定。
*   `files.exclude`：在檔案總管中排除指定的檔案和資料夾。
*   `redhat.telemetry.enabled`：啟用或停用 Red Hat 遙測。
*   `java.configuration.runtimes`：設定 Java 執行環境。
*   `java.debug.settings.vmArgs`：設定 Java 偵錯的 VM 參數。
*   `mssql.connections`：儲存 MSSQL 資料庫的連線資訊。

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
            "**/.factorypath": true"
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