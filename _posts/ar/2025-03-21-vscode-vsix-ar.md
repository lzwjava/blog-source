---
audio: false
generated: true
lang: ar
layout: post
title: تنزيل VSIX لـ VS Code
translated: true
type: note
---

لتنزيل ملف `.vsix` يدويًا لملحق Visual Studio Code (VS Code)، يمكنك استخدام Visual Studio Marketplace، الذي يستضيف جميع الملحقات الرسمية. ملف `.vsix` هو التنسيق المُعبأ لملحقات VS Code، وبينما لا يوفر Marketplace دائمًا زر تنزيل مباشر، يمكنك إنشاء رابط التنزيل أو استخدام طرق بديلة. إليك كيفية القيام بذلك خطوة بخطوة:

### خطوات التنزيل اليدوي لملف `.vsix`

1.  **ابحث عن الملحق على Visual Studio Marketplace**
    *   اذهب إلى [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) في متصفح الويب الخاص بك.
    *   ابحث عن الملحق الذي تريده (مثل "Python" من Microsoft، أو "Prettier - Code formatter"، إلخ).
    *   افتح صفحة الملحق. على سبيل المثال، قد يبدو رابط ملحق Python كالتالي:
        `https://marketplace.visualstudio.com/items?itemName=ms-python.python`.

2.  **حدد الناشر واسم الملحق**
    *   في صفحة الملحق، لاحظ **اسم الناشر** و **معرف الملحق**. هذه المعلومات جزء من الرابط أو معروضة على الصفحة.
    *   على سبيل المثال، في `ms-python.python`، `ms-python` هو الناشر، و `python` هو اسم الملحق.

3.  **أنشئ رابط التنزيل**
    *   يمكن تنزيل ملف `.vsix` مباشرة باستخدام نمط رابط محدد يوفره Marketplace. الصيغة العامة هي:
        ```
        https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
        ```
    *   استبدل `<publisher>` باسم الناشر و `<extension-name>` باسم الملحق.
    *   بالنسبة لملحق Python (`ms-python.python`)، سيكون الرابط هو:
        ```
        https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
        ```
    *   الصق هذا الرابط في متصفحك، وسيبدأ تنزيل ملف `.vsix`.

4.  **بديل: استخدم رابط "Download Extension" من صفحة Marketplace (إذا كان متاحًا)**
    *   تحتوي بعض صفحات الملحقات على رابط "Download Extension" في قسم **Resources** أو في مكان آخر. إذا كان موجودًا، انقر عليه لتنزيل ملف `.vsix` مباشرة. ومع ذلك، هذا الخيار أقل شيوعًا، لذا فإن طريقة الرابط أكثر موثوقية.

5.  **تحقق من التنزيل**
    *   سيكون للملف الذي تم تنزيله امتداد `.vsix` (على سبيل المثال، `ms-python.python-<version>.vsix`).
    *   تحقق من حجم الملف واسمه للتأكد من أنه يطابق الملحق والإصدار الذي تتوقعه.

6.  **ثبت ملف `.vsix` في VS Code (اختياري)**
    *   افتح VS Code.
    *   اذهب إلى عرض الملحقات (`Ctrl+Shift+X` أو `Cmd+Shift+X` على macOS).
    *   انقر على قائمة النقاط الثلاث (`...`) في أعلى يمين لوحة الملحقات.
    *   اختر **Install from VSIX**، ثم انتقل إلى موقع ملف `.vsix` الذي تم تنزيله وحدده.

### مثال توضيحي
لنفترض أنك تريد ملحق **ESLint** من Dirk Baeumer:
*   رابط Marketplace: `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
*   الناشر: `dbaeumer`
*   اسم الملحق: `vscode-eslint`
*   رابط التنزيل:
    ```
    https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
    ```
*   افتح هذا الرابط في متصفحك، وسيتم تنزيل ملف `.vsix` (مثل `dbaeumer.vscode-eslint-<version>.vsix`).

### ملاحظات
*   **الإصدار**: يضمن جزء `/latest/` في الرابط حصولك على أحدث إصدار. إذا كنت بحاجة إلى إصدار محدد، فستحتاج عادةً إلى الوصول إلى رقم الإصدار (المرئي في علامة التبويب "Version History" في Marketplace) وقد تحتاج إلى تعديل الرابط أو استخدام أداة مثل `ovsx` (انظر أدناه)، على الرغم من أن واجهة برمجة تطبيقات Marketplace لا تعرض الإصدارات الأقدم بسهولة عبر الرابط المباشر.
*   **التنزيلات المحظورة**: إذا لم يعمل الرابط، فقد يقتصر الناشر الوصول المباشر، أو قد يحجبه متصفحك/شبكتك. في مثل هذه الحالات، جرب متصفحًا مختلفًا أو مدير تنزيلات.
*   **أدوات بديلة**: يمكنك استخدام أداة سطر أوامر مثل `ovsx` (من سجل Open VSX) لتنزيل الملحقات. قم بتثبيتها عبر npm (`npm install -g ovsx`)، ثم قم بتشغيل:
    ```
    ovsx download ms-python.python
    ```
    يقوم هذا بتنزيل ملف `.vsix` برمجيًا.

### الإجابة النهائية
لتنزيل ملف `.vsix` يدويًا لملحق VS Code:
1.  اذهب إلى صفحة الملحق على [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode).
2.  حدد اسم الناشر واسم الملحق (مثال: `ms-python.python`).
3.  استخدم صيغة الرابط هذه في متصفحك:
    ```
    https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
    ```
4.  قم بتنزيل ملف `.vsix` وقم بتثبيته في VS Code اختياريًا.