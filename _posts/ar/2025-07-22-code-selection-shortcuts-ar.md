---
audio: false
generated: true
lang: ar
layout: post
title: الانتقاء السريع للكود والتحرير بالذكاء الاصطناعي
translated: true
type: note
---

فيما يلي نظرة عامة حول كيفية تحديد دالة أو أسلوب بسرعة باستخدام الاختصارات في **Visual Studio Code (VS Code)** و **Cursor** و **IntelliJ IDEA**، يليها الاستفادة من ميزات الذكاء الاصطناعي الخاصة بها لإصلاح الكود المحدد أو تحريره.

### Visual Studio Code (VS Code)
لا يحتوي VS Code على اختصار مباشر لتحديد دالة/أسلوب بالكامل عندما يكون المؤشر بداخلها، ولكن يمكنك استخدام الطرق التالية:
- **توسيع التحديد**: اضغط على `Ctrl+Shift+.` (Windows/Linux) أو `Cmd+Shift+.` (Mac) لتوسيع نطاق التحديد. الضغط المتكرر يحدد الكتلة المحيطة (مثل جسم الدالة، ثم الدالة بالكامل). يعمل هذا بشكل جيد مع JavaScript و Python وغيرها.
- **التحديد الذكي**: استخدم `Ctrl+Shift+Right Arrow` (Windows/Linux) أو `Cmd+Shift+Right Arrow` (Mac) لتوسيع التحديد بناءً على بناء الجملة (قد تحتاج إلى ضغطات متعددة لالتقاط الدالة بالكامل).
- **الامتداد: Select By**: قم بتثبيت امتداد "Select By" وتهيئة ربط مفتاح (مثل `Ctrl+K, Ctrl+S`) لتحديد الدالة/الأسلوب المحيط بناءً على أنماط خاصة باللغة.

**التحرير بالذكاء الاصطناعي مع GitHub Copilot**:
- بعد تحديد الدالة، اضغط على `Ctrl+I` (Windows/Linux) أو `Cmd+I` (Mac) لفتح الدردشة المضمنة لـ Copilot. اكتب مطالبة مثل "fix bugs in this function" أو "refactor to use arrow functions."
- بدلاً من ذلك، انقر بزر الماوس الأيمن على التحديد، واختر "Copilot > Fix" أو "Copilot > Refactor" للحصول على اقتراحات الذكاء الاصطناعي.
- في عرض Copilot Chat (`Ctrl+Alt+I`)، الصق الكود المحدد واطلب التعديلات (مثال: "optimize this function").

### Cursor AI Code Editor
يُحسّن Cursor، المبني على VS Code، التحديد والتكامل مع الذكاء الاصطناعي:
- **تحديد الكتلة المحيطة**: اضغط `Ctrl+Shift+.` (Windows/Linux) أو `Cmd+Shift+.` (Mac) لتوسيع التحديد إلى الدالة/الأسلوب المحيط، بشكل مشابه لـ VS Code. غالبًا ما يجعل الوعي النموذجي اللغوي في Cursor هذا أكثر دقة للغات مثل Python أو TypeScript.
- **ربطات المفاتيح المخصصة**: يمكنك تعيين ربط مفتاح مخصص في `settings.json` (مثل `editor.action.selectToBracket`) لتحديد نطاق الدالة مباشرة.

**التحرير بالذكاء الاصطناعي في Cursor**:
- بعد تحديد الدالة، اضغط على `Ctrl+K` (Windows/Linux) أو `Cmd+K` (Mac)، ثم صف التغييرات المطلوبة (مثال: "add error handling to this function"). يُظهر Cursor معاينة diff للتعديلات التي أنشأها الذكاء الاصطناعي.
- استخدم `Ctrl+I` لوضع Agent Mode لإصلاح الدالة أو تحسينها بشكل مستقل عبر الملفات، مع ملاحظات تكرارية.
- يسمح Composer Mode (يمكن الوصول إليه عبر واجهة المستخدم) بإجراء تعديلات متعددة الملفات إذا كانت الدالة تؤثر على أجزاء أخرى من قاعدة الكود.

### IntelliJ IDEA
يقدم IntelliJ IDEA اختصارات قوية لتحديد الدوال/الأساليب:
- **تحديد كتلة الكود**: مع وجود المؤشر داخل أسلوب، اضغط `Ctrl+W` (Windows/Linux) أو `Cmd+W` (Mac) لتحديد الكتلة المحيطة تدريجيًا. الضغط المتكرر يوسع التحديد إلى الأسلوب بالكامل (بما في ذلك التوقيع). يعمل هذا عبر Java و Kotlin و Python وغيرها.
- **توسيع التحديد**: استخدم `Ctrl+Shift+W` (Windows/Linux) أو `Cmd+Shift+W` (Mac) لتقليص التحديد إذا تجاوزت الحد المطلوب.
- **التحديد الواعي للهيكل**: اضغط `Ctrl+Alt+Shift+Up` (Windows/Linux) أو `Cmd+Option+Shift+Up` (Mac) لتحديد الأسلوب المحيط مباشرة عبر شجرة الهيكل.

**التحرير بالذكاء الاصطناعي مع JetBrains AI Assistant**:
- بعد تحديد الأسلوب، اضغط `Alt+Enter` أو انقر بزر الماوس الأيمن واختر "AI Actions" > "Fix with AI" أو "Suggest Refactoring." يقدم AI Assistant اقتراحات واعية بالسياق في عارض diff.
- استخدم المطالبة المضمنة (اكتب `/` متبوعًا بطلبك، مثال: `/refactor to use streams`، ثم اضغط `Tab`) لتحرير الأسلوب المحدد مباشرة.
- افتح نافذة أداة AI Assistant لوصف التغييرات المعقدة (مثال: "add logging to this method") وتطبيق الكود المُنشَأ.

### الملخص
- **VS Code**: استخدم `Ctrl+Shift+.` لتوسيع التحديد، ثم `Ctrl+I` لتعديلات Copilot بالذكاء الاصطناعي.
- **Cursor**: نفس اختصار التحديد (`Ctrl+Shift+.`) مع `Ctrl+K` للتعديلات الدقيقة المدعومة بالذكاء الاصطناعي.
- **IntelliJ IDEA**: استخدم `Ctrl+W` للتحديد السريع للأسلوب، ثم `Alt+Enter` لإصلاحات AI Assistant.

تمتلك IntelliJ أقصر اختصار مدمج دقيق لتحديد الأساليب (`Ctrl+W`)، بينما يُعد تكامل الذكاء الاصطناعي في Cursor هو الأكثر سلاسة لتحرير الكود المحدد. يعد VS Code مرنًا ولكن قد يحتاج إلى امتدادات لتحديد الدوال بشكل أسرع.

المراجع:  
[Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Code Editing in IntelliJ IDEA](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)