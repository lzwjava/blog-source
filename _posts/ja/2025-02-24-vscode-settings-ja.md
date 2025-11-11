---
audio: false
generated: true
lang: ja
layout: post
title: VSCode設定
translated: true
type: note
---

このJSONファイルには、エディターの動作と外観をカスタマイズするさまざまなVS Code設定が含まれています。以下に各設定の概要を説明します：

*   `eslint.autoFixOnSave`: ファイルの保存時にESLintの問題を自動的に修正します。
*   `java.errors.incompleteClasspath.severity`: VS Codeが不完全なJavaクラスパスエラーを処理する方法を設定します。この場合、無視します。
*   `files.associations`: 特定のファイル拡張子を言語に関連付け、シンタックスハイライトと言語サポートを提供します。
*   `emmet.syntaxProfiles`: 特定のファイルタイプにおけるEmmet略語のシンタックスプロファイルを定義します。
*   `editor.suggestSelection`: エディターでの候補選択の方法を決定します。
*   `vsintellicode.modify.editor.suggestSelection`: VS IntelliCodeを使用してエディターの候補選択動作を変更します。
*   `git.ignoreMissingGitWarning`: Gitリポジトリがない場合の警告を無効にします。
*   `python.jediEnabled`: Python用の補完エンジンとしてJediを無効にします（Pylanceが推奨されます）。
*   `editor.codeActionsOnSave`: ESLintの修正など、保存時に実行するコードアクションを指定します。
*   `python.languageServer`: Pythonの言語サーバーをPylanceに設定します。
*   `editor.renderWhitespace`: エディターでの空白の表示方法を制御します。
*   `workbench.editorAssociations`: ファイルパターンを特定のエディターに関連付けます。
*   `debug.console.fontSize`: デバッグコンソールのフォントサイズを設定します。
*   `terminal.integrated.fontSize`: 統合ターミナルのフォントサイズを設定します。
*   `terminal.integrated.shell.osx`: macOSで使用するシェルを指定します。
*   `explorer.confirmDelete`: エクスプローラーでファイルを削除する際の確認ダイアログを無効にします。
*   `ruby.codeCompletion`: Rubyのコード補完エンジンを設定します。
*   `ruby.intellisense`: Ruby IntelliSenseを設定します。
*   `C_Cpp.updateChannel`: C/C++拡張機能の更新チャネルを設定します。
*   `editor.formatOnType`: 入力中のフォーマットを有効にします。
*   `[Log]`: 「Log」として識別されるファイルに対する特定のエディター設定。
*   `files.exclude`: 指定されたファイルとフォルダーをエクスプローラーから除外します。
*   `redhat.telemetry.enabled`: Red Hatのテレメトリーを有効または無効にします。
*   `java.configuration.runtimes`: Javaランタイム環境を設定します。
*   `java.debug.settings.vmArgs`: Javaデバッグ用のVM引数を設定します。
*   `mssql.connections`: MSSQLデータベースの接続情報を保存します。



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