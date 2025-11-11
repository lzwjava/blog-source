---
audio: false
generated: true
lang: ar
layout: post
title: إنشاء ملحق لـ VSCode
translated: true
type: note
---

يمكن أن يكون إنشاء إضافة لـ Visual Studio Code (VSCode) طريقة مجزية لتعزيز سير عمل التطوير لديك أو للمساهمة في المجتمع. إليك دليل شامل لمساعدتك في البدء في كتابة إضافة VSCode:

### 1. المتطلبات الأساسية
- **Node.js و npm**: تأكد من تثبيت Node.js و npm. يمكنك تنزيلهما من [nodejs.org](https://nodejs.org/).
- **Yeoman ومولد إضافة VSCode**: قم بتثبيت Yeoman ومولد إضافة VSCode بشكل عام باستخدام npm.

```bash
npm install -g yo generator-code
```

### 2. إعداد بيئة التطوير الخاصة بك
- **تثبيت Visual Studio Code**: تأكد من تثبيت VSCode. يمكنك تنزيله من [code.visualstudio.com](https://code.visualstudio.com/).

### 3. إنشاء إضافة جديدة
استخدم مولد Yeoman لإنشاء هيكل إضافة جديد. افتح طرفية وقم بتشغيل:

```bash
yo code
```

اتبع المطالبات لإعداد إضافتك. سيُطلب منك:
- نوع الإضافة (مثل: New Extension، New Color Theme، إلخ)
- اسم إضافتك
- معرّف (مثل `my-extension`)
- وصف
- تهيئة مستودع git
- اختيار اللغة (TypeScript أو JavaScript)
- تثبيت التبعيات اللازمة

### 4. فهم هيكل المشروع
سيكون لإضافتك الجديدة الهيكل التالي:
- `.vscode/`: يحتوي على تكوينات التشغيل لتصحيح الأخطاء.
- `src/`: يحتوي على الكود المصدري لإضافتك.
- `package.json`: ملف البيان (manifest) لإضافتك.
- `tsconfig.json`: ملف تكوين TypeScript (إذا كنت تستخدم TypeScript).

### 5. كتابة إضافتك
- **التفعيل**: حدد موعد تفعيل إضافتك في `package.json` تحت الحقل `activationEvents`.
- **نقاط المساهمة**: حدد ما تقدمه إضافتك لـ VSCode، مثل الأوامر، أو العروض، أو اللغات، في قسم `contributes` في `package.json`.

### 6. تنفيذ الأوامر
أنشئ أوامر يمكن للمستخدمين استدعاؤها. حددها في `package.json` ونفذها في ملف الإضافة الرئيسي (مثل `src/extension.ts` أو `src/extension.js`).

مثال على أمر في `package.json`:

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

تنفيذ الأمر في `src/extension.ts`:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. تصحيح أخطاء إضافتك
- اضغط `F5` لفتح نافذة جديدة لـ VSCode مع تحميل إضافتك.
- عيّن نقاط التوقف واستخدم وحدة تحكم تصحيح الأخطاء لاختبار إضافتك.

### 8. التعبئة والنشر
- **تعبئة الإضافة**: استخدم أداة `vsce` لتعبئة إضافتك.

```bash
npm install -g vsce
vsce package
```

- **النشر إلى Marketplace**: اتبع التعليمات على [VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) لنشر إضافتك.

### 9. التوثيق وأفضل الممارسات
- **التوثيق**: قدم توثيقًا واضحًا لإضافتك في ملف `README.md`.
- **الاختبار**: اكتب اختبارات لضمان عمل إضافتك كما هو متوقع.
- **إدارة الإصدارات**: اتبع نظام إصدارات دلالي (semantic versioning) لإصدارات إضافتك.

### 10. موارد إضافية
- **توثيق VSCode API**: [vscode-api](https://code.visualstudio.com/api)
- **نماذج الإضافات**: [vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

باتباع هذه الخطوات، ستكون على الطريق الصحيح لإنشاء إضافة VSCode وظيفية ومفيدة. تمنياتنا بالترمجة السعيدة!