---
audio: false
lang: ar
layout: post
title: إعدادات VSCode
translated: true
---

هذا ملف JSON يحتوي على إعدادات مختلفة لـ VS Code التي تخصيص سلوك المحرر و مظهره. إليك نظرة عامة موجزة على ما يفعله كل إعداد:

*   `eslint.autoFixOnSave`: يصلح تلقائيًا مشاكل ESLint عند حفظ الملف.
*   `java.errors.incompleteClasspath.severity`: يحدد كيفية معالجة VS Code للأخطاء غير المكتملة في مسار Java. في هذه الحالة، يتم تجاهلها.
*   `files.associations`: يربط امتداد ملفات معين مع لغات لتسليط الضوء على النطق والتدعم اللغوي.
*   `emmet.syntaxProfiles`: يحدد ملفات النطق لاختصارات Emmet في أنواع الملفات المحددة.
*   `editor.suggestSelection`: يحدد كيفية اختيار الاقتراحات في المحرر.
*   `vsintellicode.modify.editor.suggestSelection`: يغير سلوك اختيار الاقتراحات في المحرر باستخدام VS IntelliCode.
*   `git.ignoreMissingGitWarning`: يوقف تحذير عدم وجود مستودعات Git.
*   `python.jediEnabled`: يوقف Jedi كمحرك إكمال Python (Pylance هو المفضل).
*   `editor.codeActionsOnSave`: يحدد إجراءات الكود التي يتم تنفيذها عند الحفظ، مثل إصلاحات ESLint.
*   `python.languageServer`: يحدد خادم لغة Python إلى Pylance.
*   `editor.renderWhitespace`: يسيطر على كيفية عرض الفراغات البيضاء في المحرر.
*   `workbench.editorAssociations`: يربط نماذج الملفات مع محررات محددة.
*   `debug.console.fontSize`: يحدد حجم الخط للمحطة التوضيحية.
*   `terminal.integrated.fontSize`: يحدد حجم الخط للمشغل المتكامل.
*   `terminal.integrated.shell.osx`: يحدد القشرة المستخدمة على macOS.
*   `explorer.confirmDelete`: يوقف حوار التأكيد عند حذف الملفات في المستكشف.
*   `ruby.codeCompletion`: يحدد محرك إكمال الكود لـ Ruby.
*   `ruby.intellisense`: يحدد Ruby IntelliSense.
*   `C_Cpp.updateChannel`: يحدد قناة التحديثات للمكمل C/C++.
*   `editor.formatOnType`: يفعّل التصفير أثناء الكتابة.
*   `[Log]`: إعدادات المحرر الخاصة للملفات المعرّفة كـ "Log".
*   `files.exclude`: يبعد الملفات والمجلدات المحددة عن المستكشف.
*   `redhat.telemetry.enabled`: يفعّل أو يوقف بيانات Red Hat.
*   `java.configuration.runtimes`: يحدد بيئات تشغيل Java.
*   `java.debug.settings.vmArgs`: يحدد حجج VM للتصحيح في Java.
*   `mssql.connections`: يخزن معلومات الاتصال لمستودعات MSSQL.

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