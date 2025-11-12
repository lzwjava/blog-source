---
audio: false
generated: true
lang: ar
layout: post
title: إعدادات VSCode
translated: true
type: note
---

يحتوي ملف JSON هذا على إعدادات مختلفة لـ VS Code تخصّص سلوك ومظهر المحرر. إليك نظرة عامة موجزة على وظيفة كل إعداد:

*   `eslint.autoFixOnSave`: يُصلح مشاكل ESLint تلقائيًا عند حفظ الملف.
*   `java.errors.incompleteClasspath.severity`: يهيئ كيفية تعامل VS Code مع أخطاء classpath غير المكتملة في Java. في هذه الحالة، يتم تجاهلها.
*   `files.associations`: يربط امتدادات ملفات محددة بلغات من أجل التلوين النحوي ودعم اللغة.
*   `emmet.syntaxProfiles`: يحدد ملفات تعريف syntax لاختصارات Emmet في أنواع ملفات محددة.
*   `editor.suggestSelection`: يحدد كيفية اختيار الاقتراحات في المحرر.
*   `vsintellicode.modify.editor.suggestSelection`: يعدّل سلوك اختيار اقتراحات المحرر باستخدام VS IntelliCode.
*   `git.ignoreMissingGitWarning`: يعطّل التحذير الخاص بمستودعات Git المفقودة.
*   `python.jediEnabled`: يعطّل Jedi كمحرك الإكمال لـ Python (يُفضل استخدام Pylance).
*   `editor.codeActionsOnSave`: يحدد إجراءات الكود التي سيتم تنفيذها عند الحفظ، مثل إصلاحات ESLint.
*   `python.languageServer`: يضبط خادم اللغة Python إلى Pylance.
*   `editor.renderWhitespace`: يتحكم في كيفية عرض المسافات البيضاء في المحرر.
*   `workbench.editorAssociations`: يربط أنماط الملفات بمحررين محددين.
*   `debug.console.fontSize`: يضبط حجم الخط لوحدة تحكم التصحيح.
*   `terminal.integrated.fontSize`: يضبط حجم الخط للطرفية المدمجة.
*   `terminal.integrated.shell.osx`: يحدد الـ shell المستخدم على نظام macOS.
*   `explorer.confirmDelete`: يعطّل مربعات حوار التأكيد عند حذف الملفات في Explorer.
*   `ruby.codeCompletion`: يضبط محرك إكمال الكود لـ Ruby.
*   `ruby.intellisense`: يهيء Ruby IntelliSense.
*   `C_Cpp.updateChannel`: يضبط قناة التحديث لامتداد C/C++.
*   `editor.formatOnType`: يمكّن التنسيق أثناء الكتابة.
*   `[Log]`: إعدادات محرر محددة للملفات المُعرّفة كـ "Log".
*   `files.exclude`: يستبعد ملفات ومجلدات محددة من الـ Explorer.
*   `redhat.telemetry.enabled`: يمكّن أو يعطّل جمع بيانات الاستخدام لـ Red Hat.
*   `java.configuration.runtimes`: يهيء بيئات وقت تشغيل Java.
*   `java.debug.settings.vmArgs`: يضبط وسائط VM لتصحيح Java.
*   `mssql.connections`: يخزن معلومات الاتصال لقواعد بيانات MSSQL.

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