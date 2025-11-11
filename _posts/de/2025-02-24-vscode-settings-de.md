---
audio: false
generated: true
lang: de
layout: post
title: VSCode-Einstellungen
translated: true
type: note
---

Diese JSON-Datei enthält verschiedene VS Code-Einstellungen, die das Verhalten und Erscheinungsbild des Editors anpassen. Hier ist eine kurze Übersicht darüber, was jede Einstellung bewirkt:

*   `eslint.autoFixOnSave`: Behebt ESLint-Probleme automatisch beim Speichern einer Datei.
*   `java.errors.incompleteClasspath.severity`: Konfiguriert, wie VS Code mit Fehlern aufgrund eines unvollständigen Java-Classpaths umgeht. In diesem Fall werden sie ignoriert.
*   `files.associations`: Ordnet bestimmte Dateierweiterungen Sprachen für Syntax-Hervorhebung und Sprachunterstützung zu.
*   `emmet.syntaxProfiles`: Definiert Syntax-Profile für Emmet-Abkürzungen in bestimmten Dateitypen.
*   `editor.suggestSelection`: Legt fest, wie Vorschläge im Editor ausgewählt werden.
*   `vsintellicode.modify.editor.suggestSelection`: Modifiziert das Auswahlverhalten für Vorschläge des Editors mithilfe von VS IntelliCode.
*   `git.ignoreMissingGitWarning`: Deaktiviert die Warnung für fehlende Git-Repositories.
*   `python.jediEnabled`: Deaktiviert Jedi als Completion-Engine für Python (Pylance wird bevorzugt).
*   `editor.codeActionsOnSave`: Gibt Code-Aktionen an, die beim Speichern ausgeführt werden sollen, z. B. ESLint-Korrekturen.
*   `python.languageServer`: Setzt den Python Language Server auf Pylance.
*   `editor.renderWhitespace`: Steuert, wie Leerzeichen im Editor dargestellt werden.
*   `workbench.editorAssociations`: Ordnet Dateimuster bestimmten Editoren zu.
*   `debug.console.fontSize`: Legt die Schriftgröße für die Debug-Konsole fest.
*   `terminal.integrated.fontSize`: Legt die Schriftgröße für das integrierte Terminal fest.
*   `terminal.integrated.shell.osx`: Spezifiziert die Shell, die unter macOS verwendet werden soll.
*   `explorer.confirmDelete`: Deaktiviert Bestätigungsdialoge beim Löschen von Dateien im Explorer.
*   `ruby.codeCompletion`: Legt die Code Completion Engine für Ruby fest.
*   `ruby.intellisense`: Konfiguriert Ruby IntelliSense.
*   `C_Cpp.updateChannel`: Legt den Update-Kanal für die C/C++-Erweiterung fest.
*   `editor.formatOnType`: Aktiviert die Formatierung während der Eingabe.
*   `[Log]`: Spezifische Editor-Einstellungen für Dateien, die als "Log" identifiziert werden.
*   `files.exclude`: Schließt bestimmte Dateien und Ordner vom Explorer aus.
*   `redhat.telemetry.enabled`: Aktiviert oder deaktiviert die Red Hat Telemetrie.
*   `java.configuration.runtimes`: Konfiguriert Java-Laufzeitumgebungen.
*   `java.debug.settings.vmArgs`: Setzt VM-Argumente für das Java-Debugging.
*   `mssql.connections`: Speichert Verbindungsinformationen für MSSQL-Datenbanken.

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