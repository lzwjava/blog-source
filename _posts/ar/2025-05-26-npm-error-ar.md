---
audio: false
generated: true
lang: ar
layout: post
title: حل خطأ npm ENOTEMPTY
translated: true
type: note
---

يحدث خطأ `ENOTEMPTY` في npm عندما يحاول إعادة تسمية دليل (في هذه الحالة، `/opt/homebrew/lib/node_modules/@anthropic-ai/claude-code` إلى `/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V`)، لكن الدليل الوجهة ليس فارغًا. يحدث هذا عادةً أثناء تثبيت الحزمة أو التحديثات عندما لا يتمكن npm من الكتابة فوق الأدلة أو نقلها بسبب وجود ملفات.

### خطوات الحل

1.  **مسح ذاكرة التخزين المؤقت (Cache) لـ npm**:
    قم بتشغيل الأمر التالي لمسح ذاكرة التخزين المؤقت لـ npm، مما يمكن أن يحل المشاكل الناتجة عن بيانات ذاكرة تخزين مؤقت تالفة أو قديمة:
    ```bash
    npm cache clean --force
    ```

2.  **إزالة الدليل المسبب للمشكلة**:
    يشير الخطأ إلى دليل `@anthropic-ai/claude-code`. احذفه يدويًا لضمان عدم بقاء أي ملفات متضاربة:
    ```bash
    rm -rf /opt/homebrew/lib/node_modules/@anthropic-ai/claude-code
    ```

3.  **التحقق من عمليات التثبيت الجزئية**:
    تحقق أيضًا من الدليل المؤقت المذكور في الخطأ (`/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V`) وقم بإزالته:
    ```bash
    rm -rf /opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V
    ```

4.  **إعادة تثبيت الحزمة**:
    بعد مسح الأدلة المسببة للمشكلة، حاول إعادة تثبيت الحزمة:
    ```bash
    npm install
    ```

5.  **التحقق من الأذونات**:
    قد يكون الخطأ ناتجًا عن عدم كفاية الصلاحيات. تأكد من أن لديك صلاحية الكتابة في `/opt/homebrew/lib/node_modules`. إذا لم يكن الأمر كذلك، قم بتعديل الأذونات أو استخدم `sudo`:
    ```bash
    sudo npm install
    ```
    بدلاً من ذلك، يمكنك إصلاح الأذونات:
    ```bash
    sudo chown -R $(whoami):admin /opt/homebrew/lib/node_modules
    ```

6.  **مراجعة سجل التصحيح (Debug Log)**:
    تحقق من ملف السجل الموجود في `/Users/lzwjava/.npm/_logs/2025-05-25T19_07_29_589Z-debug-0.log` لمزيد من التفاصيل. يمكنك عرضه باستخدام:
    ```bash
    cat /Users/lzwjava/.npm/_logs/2025-05-25T19_07_29_589Z-debug-0.log
    ```
    ابحث عن أدلة إضافية حول الملفات أو العمليات المتضاربة.

7.  **تحديث npm**:
    تأكد من أنك تستخدم أحدث إصدار من npm لتجنب الأخطاء في الإصدارات القديمة:
    ```bash
    npm install -g npm@latest
    ```

8.  **التحقق من العمليات قيد التشغيل**:
    في بعض الأحيان، تقوم عملية قيد التشغيل بقفل الدليل. تأكد من عدم وجود عمليات npm أخرى نشطة:
    ```bash
    ps aux | grep npm
    ```
    إذا كانت هناك أي عمليات npm قيد التشغيل، أوقفها:
    ```bash
    kill -9 <process-id>
    ```

9.  **محاولة تثبيت جديد (Fresh Install)**:
    إذا استمرت المشكلة، ففكر في إزالة دليل `node_modules` بالكامل وملف `package-lock.json`، ثم أعد تثبيت التبعيات:
    ```bash
    rm -rf node_modules package-lock.json
    npm install
    ```

### ملاحظات إضافية
- إذا كنت تستخدم حزمة مثل `@anthropic-ai/claude-code`، فتأكد من أنها متوافقة مع إصدارات Node.js و npm الخاصة بك.
- إذا تكرر حدوث المشكلة، تحقق من مشاكل مساحة القرص أو تلف نظام الملفات على جهازك.
- إذا كنت تستخدم نظام macOS (كما يشير إليه المسار `/opt/homebrew`)، فتأكد من أن Homebrew محدث عن طريق تشغيل `brew update` ثم `brew upgrade`.

إذا لم تحل هذه الخطوات المشكلة، شارك التفاصيل ذات الصلة من سجل التصحيح أو أي سياق محدد حول الحزمة أو الأمر الذي كنت تقوم بتشغيله.