---
audio: false
generated: true
lang: fr
layout: post
title: Paramètres de VSCode
translated: true
type: note
---

Ce fichier JSON contient divers paramètres VS Code qui personnalisent le comportement et l'apparence de l'éditeur. Voici un bref aperçu de ce que fait chaque paramètre :

*   `eslint.autoFixOnSave` : Corrige automatiquement les problèmes ESLint lors de l'enregistrement d'un fichier.
*   `java.errors.incompleteClasspath.severity` : Configure la manière dont VS Code gère les erreurs de classpath Java incomplet. Dans ce cas, elles sont ignorées.
*   `files.associations` : Associe des extensions de fichier spécifiques à des langages pour la coloration syntaxique et le support du langage.
*   `emmet.syntaxProfiles` : Définit les profils de syntaxe pour les abréviations Emmet dans des types de fichiers spécifiques.
*   `editor.suggestSelection` : Détermine comment les suggestions sont sélectionnées dans l'éditeur.
*   `vsintellicode.modify.editor.suggestSelection` : Modifie le comportement de sélection des suggestions de l'éditeur en utilisant VS IntelliCode.
*   `git.ignoreMissingGitWarning` : Désactive l'avertissement pour les dépôts Git manquants.
*   `python.jediEnabled` : Désactive Jedi en tant que moteur de complétion pour Python (Pylance est préféré).
*   `editor.codeActionsOnSave` : Spécifie les actions de code à exécuter lors de l'enregistrement, telles que les correctifs ESLint.
*   `python.languageServer` : Définit le serveur de langage Python sur Pylance.
*   `editor.renderWhitespace` : Contrôle la manière dont les espaces blancs sont rendus dans l'éditeur.
*   `workbench.editorAssociations` : Associe des modèles de fichiers à des éditeurs spécifiques.
*   `debug.console.fontSize` : Définit la taille de police pour la console de débogage.
*   `terminal.integrated.fontSize` : Définit la taille de police pour le terminal intégré.
*   `terminal.integrated.shell.osx` : Spécifie le shell à utiliser sur macOS.
*   `explorer.confirmDelete` : Désactive les dialogues de confirmation lors de la suppression de fichiers dans l'Explorateur.
*   `ruby.codeCompletion` : Définit le moteur de complétion de code pour Ruby.
*   `ruby.intellisense` : Configure Ruby IntelliSense.
*   `C_Cpp.updateChannel` : Définit le canal de mise à jour pour l'extension C/C++.
*   `editor.formatOnType` : Active la mise en forme pendant la saisie.
*   `[Log]` : Paramètres d'éditeur spécifiques pour les fichiers identifiés comme "Log".
*   `files.exclude` : Exclut les fichiers et dossiers spécifiés de l'Explorateur.
*   `redhat.telemetry.enabled` : Active ou désactive la télémétrie Red Hat.
*   `java.configuration.runtimes` : Configure les environnements d'exécution Java.
*   `java.debug.settings.vmArgs` : Définit les arguments VM pour le débogage Java.
*   `mssql.connections` : Stocke les informations de connexion pour les bases de données MSSQL.

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