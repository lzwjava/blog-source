---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड सेटिंग्स
translated: true
type: note
---

यह JSON फ़ाइल विभिन्न VS Code सेटिंग्स शामिल करती है जो एडिटर के व्यवहार और रूप को अनुकूलित करती हैं। यहां प्रत्येक सेटिंग का संक्षिप्त विवरण दिया गया है:

*   `eslint.autoFixOnSave`: फ़ाइल सेव करते समय ESLint समस्याओं को स्वचालित रूप से ठीक करता है।
*   `java.errors.incompleteClasspath.severity`: कॉन्फ़िगर करता है कि VS Code अपूर्ण Java classpath त्रुटियों को कैसे संभालता है। इस मामले में, यह उन्हें नजरअंदाज कर देता है।
*   `files.associations`: सिंटैक्स हाइलाइटिंग और भाषा समर्थन के लिए विशिष्ट फ़ाइल एक्सटेंशन को भाषाओं से जोड़ता है।
*   `emmet.syntaxProfiles`: विशिष्ट फ़ाइल प्रकारों में Emmet संक्षिप्तियों के लिए सिंटैक्स प्रोफाइल को परिभाषित करता है।
*   `editor.suggestSelection`: निर्धारित करता है कि एडिटर में सुझावों का चयन कैसे किया जाता है।
*   `vsintellicode.modify.editor.suggestSelection`: VS IntelliCode का उपयोग करके एडिटर के सुझाव चयन व्यवहार को संशोधित करता है।
*   `git.ignoreMissingGitWarning`: गायब Git रिपॉजिटरी के लिए चेतावनी को अक्षम करता है।
*   `python.jediEnabled`: Python के लिए पूर्णता इंजन के रूप में Jedi को अक्षम करता है (Pylance को प्राथमिकता दी जाती है)।
*   `editor.codeActionsOnSave`: सेव करने पर चलने के लिए कोड एक्शन निर्दिष्ट करता है, जैसे ESLint फिक्स।
*   `python.languageServer`: Python लैंग्वेज सर्वर को Pylance पर सेट करता है।
*   `editor.renderWhitespace`: नियंत्रित करता है कि एडिटर में व्हाइटस्पेस कैसे रेंडर किया जाता है।
*   `workbench.editorAssociations`: फ़ाइल पैटर्न को विशिष्ट एडिटरों से जोड़ता है।
*   `debug.console.fontSize`: डिबग कंसोल के लिए फ़ॉन्ट आकार सेट करता है।
*   `terminal.integrated.fontSize`: एकीकृत टर्मिनल के लिए फ़ॉन्ट आकार सेट करता है।
*   `terminal.integrated.shell.osx`: macOS पर उपयोग करने के लिए शेल निर्दिष्ट करता है।
*   `explorer.confirmDelete`: एक्सप्लोरर में फ़ाइलें हटाते समय पुष्टि संवादों को अक्षम करता है।
*   `ruby.codeCompletion`: Ruby के लिए कोड पूर्णता इंजन सेट करता है।
*   `ruby.intellisense`: Ruby IntelliSense को कॉन्फ़िगर करता है।
*   `C_Cpp.updateChannel`: C/C++ एक्सटेंशन के लिए अपडेट चैनल सेट करता है।
*   `editor.formatOnType`: टाइप करते समय फॉर्मेटिंग सक्षम करता है।
*   `[Log]`: "लॉग" के रूप में पहचानी गई फ़ाइलों के लिए विशिष्ट एडिटर सेटिंग्स।
*   `files.exclude`: एक्सप्लोरर से निर्दिष्ट फ़ाइलों और फ़ोल्डरों को बाहर करता है।
*   `redhat.telemetry.enabled`: Red Hat टेलीमेट्री को सक्षम या अक्षम करता है।
*   `java.configuration.runtimes`: Java रनटाइम वातावरण को कॉन्फ़िगर करता है।
*   `java.debug.settings.vmArgs`: Java डिबगिंग के लिए VM तर्क सेट करता है।
*   `mssql.connections`: MSSQL डेटाबेस के लिए कनेक्शन जानकारी संग्रहीत करता है।

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