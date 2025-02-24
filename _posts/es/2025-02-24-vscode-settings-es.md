---
audio: false
lang: es
layout: post
title: Configuración de VSCode
translated: true
---

Este archivo JSON contiene diversas configuraciones de VS Code que personalizan el comportamiento y la apariencia del editor. Aquí tienes un breve resumen de lo que hace cada configuración:

*   `eslint.autoFixOnSave`: Corrige automáticamente los problemas de ESLint al guardar un archivo.
*   `java.errors.incompleteClasspath.severity`: Configura cómo maneja VS Code los errores de classpath incompleto de Java. En este caso, los ignora.
*   `files.associations`: Asocia extensiones de archivo específicas con lenguajes para el resaltado de sintaxis y el soporte del lenguaje.
*   `emmet.syntaxProfiles`: Define perfiles de sintaxis para las abreviaturas de Emmet en tipos de archivo específicos.
*   `editor.suggestSelection`: Determina cómo se seleccionan las sugerencias en el editor.
*   `vsintellicode.modify.editor.suggestSelection`: Modifica el comportamiento de selección de sugerencias del editor utilizando VS IntelliCode.
*   `git.ignoreMissingGitWarning`: Desactiva la advertencia para repositorios Git faltantes.
*   `python.jediEnabled`: Desactiva Jedi como el motor de autocompletado para Python (se prefiere Pylance).
*   `editor.codeActionsOnSave`: Especifica las acciones de código para ejecutar al guardar, como las correcciones de ESLint.
*   `python.languageServer`: Establece el servidor de lenguaje de Python en Pylance.
*   `editor.renderWhitespace`: Controla cómo se representa el espacio en blanco en el editor.
*   `workbench.editorAssociations`: Asocia patrones de archivo con editores específicos.
*   `debug.console.fontSize`: Establece el tamaño de fuente para la consola de depuración.
*   `terminal.integrated.fontSize`: Establece el tamaño de fuente para la terminal integrada.
*   `terminal.integrated.shell.osx`: Especifica la shell a utilizar en macOS.
*   `explorer.confirmDelete`: Desactiva los diálogos de confirmación al eliminar archivos en el Explorador.
*   `ruby.codeCompletion`: Establece el motor de autocompletado de código para Ruby.
*   `ruby.intellisense`: Configura Ruby IntelliSense.
*   `C_Cpp.updateChannel`: Establece el canal de actualización para la extensión de C/C++.
*   `editor.formatOnType`: Habilita el formato mientras se escribe.
*   `[Log]`: Configuraciones específicas del editor para archivos identificados como "Log".
*   `files.exclude`: Excluye archivos y carpetas especificados del Explorador.
*   `redhat.telemetry.enabled`: Habilita o deshabilita la telemetría de Red Hat.
*   `java.configuration.runtimes`: Configura los entornos de ejecución de Java.
*   `java.debug.settings.vmArgs`: Establece los argumentos de VM para la depuración de Java.
*   `mssql.connections`: Almacena la información de conexión para las bases de datos MSSQL.

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
                  "server": "{{poner-nombre-del-servidor-aquí}}",
                  "database": "{{poner-nombre-de-la-base-de-datos-aquí}}",
                  "user": "{{poner-nombre-de-usuario-aquí}}",
                  "password": "{{poner-contraseña-aquí}}"
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