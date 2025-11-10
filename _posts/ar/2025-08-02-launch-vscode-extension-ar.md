---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مضيف امتداد التشغيل في في إس كود
translated: true
type: note
---

لضغط **F5** في Visual Studio Code (VSCode) لتشغيل **Extension Development Host** لتطوير إضافة VSCode، اتبع الخطوات التالية:

1.  **افتح مشروع الإضافة الخاص بك في VSCode**:
    - تأكد من أن لديك مشروع إضافة VSCode تم إعداده. يتضمن هذا عادةً ملف `package.json` مع تكوينات الإضافة الضرورية (مثل `contributes`، `activationEvents`).
    - افتح المجلد الذي يحتوي على مشروع الإضافة الخاص بك في VSCode عن طريق تحديد `File > Open Folder` أو باستخدام `Ctrl+K, Ctrl+O` (Windows/Linux) أو `Cmd+K, Cmd+O` (Mac).

2.  **تحقق من إعداد الإضافة الخاص بك**:
    - تأكد من أن لديك ملف `package.json` صالح في جذر مشروعك يحتوي على الحقول التالية على الأقل:
      ```json
      {
        "name": "your-extension-name",
        "displayName": "Your Extension Name",
        "description": "Description of your extension",
        "version": "0.0.1",
        "engines": {
          "vscode": "^1.60.0"
        },
        "categories": ["Other"],
        "activationEvents": ["*"],
        "main": "./extension.js",
        "contributes": {}
      }
      ```
    - تأكد من أن لديك ملف `extension.js` (أو ما يعادله) كنقطة دخول لكود الإضافة الخاص بك.
    - قم بتثبيت التبعيات عن طريق تشغيل `npm install` في الطرفية المدمجة (`Ctrl+``) إذا كانت إضافتك تستخدم وحدات Node.js.

3.  **اضغط F5 لتشغيل Extension Development Host**:
    - اضغط **F5** على لوحة المفاتيح أثناء فتح مشروع الإضافة الخاص بك في VSCode.
    - يبدأ هذا **Extension Development Host**، وهو نافذة VSCode منفصلة حيث يتم تحميل إضافتك للاختبار.
    - سيقوم VSCode تلقائيًا بما يلي:
        - بناء إضافتك (إذا كنت تستخدم TypeScript، فإنه يقوم بتجميع ملفات `.ts` إلى `.js`).
        - تشغيل مثيل VSCode جديد مع تفعيل إضافتك.
        - فتح أداة تصحيح مرتبطة بعملية Extension Host.

4.  **تكوين التصحيح**:
    - يستخدم VSCode ملف `launch.json` في مجلد `.vscode` لتكوين التصحيح. إذا كان غير موجود، سيقوم VSCode بإنشائه تلقائيًا عند الضغط على F5 لأول مرة.
    - يبدو `launch.json` النموذجي للإضافة كما يلي:
      ```json
      {
        "version": "0.2.0",
        "configurations": [
          {
            "name": "Run Extension",
            "type": "extensionHost",
            "request": "launch",
            "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
            "outFiles": ["${workspaceFolder}/out/**/*.js"],
            "preLaunchTask": "npm: watch"
          }
        ]
      }
      ```
    - تأكد من أن `preLaunchTask` (إذا كان موجودًا) يطابق مهمة في ملف `tasks.json` الخاص بك (على سبيل المثال، لتجميع TypeScript).

5.  **اختبر إضافتك**:
    - في نافذة Extension Development Host، يجب أن تكون إضافتك نشطة. اختبر وظيفتها (مثل الأوامر، مساهمات واجهة المستخدم) كما هي محددة في ملف `package.json` والكود الخاص بك.
    - استخدم **Debug Console** في نافذة VSCode الرئيسية لعرض السجلات أو الأخطاء من إضافتك.

6.  **استكشاف الأخطاء وإصلاحها**:
    - إذا لم يعمل F5:
        - تأكد من تثبيت Node.js و npm، حيث أنهما مطلوبان لتطوير الإضافات.
        - تحقق من أن لديك تبعيات VSCode Extension API مثبتة (`npm install @types/vscode`).
        - تحقق من أن تكوين `launch.json` يشير إلى المسارات الصحيحة.
        - إذا رأيت أخطاء، تحقق من لوحة **Output** (اختر "Extension" في القائمة المنسدلة) في نافذة Extension Development Host.
    - إذا لم يتم تشغيل Extension Host، تأكد من أن مشروعك لا يحتوي على أخطاء في بناء الجملة في `package.json` أو ملف الإضافة الرئيسي الخاص بك.

**ملاحظات إضافية**:
- يمكنك أيضًا بدء Extension Development Host عن طريق فتح لوحة **Run and Debug** (`Ctrl+Shift+D` أو `Cmd+Shift+D` على Mac) وتحديد "Run Extension" من القائمة المنسدلة، ثم النقر على زر التشغيل الأخضر.
- لإعادة تحميل Extension Host بعد إجراء التغييرات، استخدم `Ctrl+R` (Windows/Linux) أو `Cmd+R` (Mac) في نافذة Extension Development Host، أو أعد تشغيله باستخدام F5.

لمزيد من التفاصيل، راجع دليل تطوير إضافات VSCode الرسمي:  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)