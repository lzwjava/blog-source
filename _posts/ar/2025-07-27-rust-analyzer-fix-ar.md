---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مشكلة مساحة عمل محلل رست
translated: true
type: note
---

تشير رسائل الخطأ التي تراها إلى أن rust-analyzer (خادم لغة Rust) غير قادر على اكتشاف مساحة عمل Rust صالحة في الدليل المحدد `/Users/lzwjava/projects/lzwjava.github.io`. يحدث هذا عادةً لأن المجلد يفتقر إلى ملف `Cargo.toml` (أو علامات مشروع Rust أخرى) في الجذر، أو أن rust-analyzer غير مهيئ للبحث في المكان الصحيح. يتوقع rust-analyzer العثور على مشروع Rust واحد على الأقل في مساحة العمل المفتوحة؛ إذا لم يجد، فشل في التحميل.

يشير اسم هذا الدليل (`lzwjava.github.io`) إلى أنه قد يكون موقع GitHub Pages (مثل مدونة ثابتة أو موقع ويب)، وهو ليس عادةً مشروع Rust ما لم تكن تستخدم أداة مبنية على Rust مثل مولد مواقع ثابت مخصص. إذا لم يكن من المفترض أن يكون هذا مساحة عمل Rust، فقد يكون rust-analyzer نشطًا دون داع (على سبيل المثال، بسبب إعداد امتداد عام في محررك).

بافتراض أنك تستخدم VS Code (المحرر الأكثر شيوعًا لهذه المشكلة؛ إذا لم يكن كذلك، راجع الملاحظات أدناه)، إليك الخطوات لإصلاحها:

### 1. **التحقق من مجلد مساحة العمل الصحيح وفتحه**
   - تأكد من أنك تفتح المجلد الذي يحتوي على ملف `Cargo.toml` لمشروع Rust الخاص بك كجذر مساحة العمل في VS Code.
   - إذا كان مشروعك موجودًا في دليل فرعي (مثل `/Users/lzwjava/projects/lzwjava.github.io/my-rust-app`)، فافتح ذلك المجلد الفرعي بدلاً من ذلك عبر **File > Open Folder**.
   - أعد تشغيل VS Code بعد تغيير مساحة العمل.

### 2. **تهيئة المشاريع المرتبطة في إعدادات rust-analyzer**
   - إذا كان `Cargo.toml` موجودًا ولكنه ليس في جذر مساحة العمل (مثل وجوده في مجلد فرعي)، أخبر rust-analyzer أين يمكنه العثور عليه:
     - افتح إعدادات VS Code (**Code > Preferences > Settings** أو Cmd+, على جهاز Mac).
     - ابحث عن "rust-analyzer".
     - ضمن **Rust-analyzer > Server: Extra Env** أو مباشرة في إعدادات الامتداد، ابحث عن **Linked Projects**.
     - عيّنه على مصفوفة تشير إلى مسار(مسار) `Cargo.toml` الخاص بك. على سبيل المثال، أضف هذا إلى `settings.json` لمساحة العمل الخاصة بك (عبر **Preferences: Open Workspace Settings (JSON)**):
       ```
       {
         "rust-analyzer.linkedProjects": [
           "./path/to/your/Cargo.toml"
         ]
       }
       ```
       استبدل `./path/to/your/Cargo.toml` بالمسار النسبي من جذر مساحة العمل الخاص بك.
     - احفظ وأعد تحميل النافذة (**Developer: Reload Window** عبر لوحة الأوامر، Cmd+Shift+P).

### 3. **إذا لم يكن هذا مشروع Rust**
   - عطّل rust-analyzer لمساحة العمل هذه:
     - انتقل إلى عرض الامتدادات (Cmd+Shift+X).
     - ابحث عن "rust-analyzer" > انقر على أيقونة الترس > **Disable (Workspace)**.
   - بدلاً من ذلك، ألغِ تثبيت الامتداد إذا كنت لا تحتاجه على الإطلاق.

### 4. **استكشاف الأخطاء وإصلاحها الأخرى**
   - **أعد تثبيت rust-analyzer و Rustup**: أحيانًا تسبب التثبيتات التالفة مشاكل. شغّل `rustup self uninstall` ثم `rustup self update` في طرفيتك، وأعد تثبيت امتداد VS Code.
   - **تحقق من وجود مساحات عمل متعددة**: إذا كان لديك مساحة عمل متعددة الجذور، فتأكد من أن لكل جذر تكوينه الصحيح الخاص به.
   - **حدث كل شيء**: تأكد من أن VS Code وامتداد rust-analyzer وسلسلة أدوات Rust (`rustup update`) محدثة.
   - **السجلات للحصول على مزيد من التفاصيل**: تحقق من ناتج rust-analyzer في VS Code (**View > Output**، اختر "rust-analyzer" من القائمة المنسدلة) للحصول على أدلة إضافية.

إذا كنت تستخدم محررًا مختلفًا:
- **Neovim أو Vim**: تأكد من أن تكوين LSP الخاص بك (عبر lsp-zero أو nvim-lspconfig على سبيل المثال) يشير إلى دليل الجذر الصحيح باستخدام أنماط `root_dir` مثل `util.find_git_ancestor` أو عيّنه صراحةً للعثور على `Cargo.toml`.
- **Kate أو Emacs**: قد تكون المشكلة هي أن المحرر لا يمرر مسار المشروع بشكل صحيح — حاول تعيين جذر المشروع يدويًا في تكوين LSP الخاص بك أو تحقق من وجود أخطاء خاصة بالمحرر (على سبيل المثال، تأكد من وجود مجلد `.git` إذا كان مطلوبًا).
- **بيئات التطوير المتكاملة الأخرى**: ابحث عن إعدادات مكافئة لـ "المشاريع المرتبطة" أو "جذر مساحة العمل".

إذا لم ينجح أي من هذا، قدم المزيد من التفاصيل مثل المحرر الذي تستخدمه، وما إذا كان هذا مشروع Rust، وأي ملفات Rust في ذلك الدليل.

[rust-analyzer failed to discover workspace in vscode - Stack Overflow](https://stackoverflow.com/questions/72062935/rust-analyzer-failed-to-discover-workspace-in-vscode)  
[Question about failed to find any projects in [AbsPathBuf...] - GitHub](https://github.com/rust-analyzer/rust-analyzer/issues/11666)  
[Problem with Rust-Analyzer - Rust Users Forum](https://users.rust-lang.org/t/problem-with-rust-analyzer/91453)  
[Configuration - rust-analyzer Manual](https://rust-analyzer.github.io/manual.html#configuration)