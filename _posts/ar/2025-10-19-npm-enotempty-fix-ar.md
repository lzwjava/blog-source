---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ تثبيت npm ENOTEMPTY
translated: true
type: note
---

### فهم الخطأ

أمر `sudo npm i -g @anthropic-ai/claude-code --verbose` الخاص بك يفشل مع خطأ `ENOTEMPTY` أثناء عملية التثبيت. هذه مشكلة شائعة في npm تحدث عندما يحاول npm إعادة تسمية (أو نقل) دليل موجود كجزء من تحديث أو إعادة تثبيت حزمة، لكن الدليل ليس فارغًا. في هذه الحالة، يفشل تحديدًا في إعادة تسمية `/usr/lib/node_modules/@anthropic-ai/claude-code` إلى موقع نسخ احتياطي مؤقت (`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`).

يحدث هذا عادةً بسبب:
- تثبيت سابق جزئي أو متقطع ترك ملفات أو أدلة فرعية خلفه.
- أقفال ملفات من عملية أخرى (على سبيل المثال، إذا تم تحميل الحزمة جزئيًا أو إذا كان هناك أمر npm آخر قيد التشغيل).
- نادرًا، مشاكل صلاحيات مع التثبيت العام باستخدام `sudo`.

الحزمة نفسها (`@anthropic-ai/claude-code`) شرعية — فهي أداة CLI الرسمية من Anthropic لأداة "Claude Code"، وهي مساعد برمجة وكيل يتكامل مع طرفيتك وقاعدة التعليمات البرمجية الخاصة بك.

### الإصلاحات السريعة

جرب هذه الخطوات بالترتيب. قم بتشغيلها كـ root أو باستخدام `sudo` حيثما ذُكر، لأن هذا تثبيت عام.

١. **إزالة الدليل الموجود يدويًا**  
   هذا يزيل التثبيت الجزئي المشكلة:  
   ```
   sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
   ```  
   - إذا أصبح الدليل الرئيسي المُحدد (`@anthropic-ai`) فارغًا الآن، يمكنك إزالته أيضًا:  
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai
     ```  
   ثم أعد محاولة الأمر الأصلي:  
   ```
   sudo npm i -g @anthropic-ai/claude-code --verbose
   ```

٢. **مسح ذاكرة التخزين المؤقت لـ npm**  
   إذا لم ينجح ما ورد أعلاه، فقد تكون إدخالات ذاكرة التخزين المؤقت التالفة متورطة:  
   ```
   sudo npm cache clean --force
   sudo npm cache verify
   ```  
   أعد محاولة التثبيت بعد هذا.

٣. **التحقق من العمليات قيد التشغيل**  
   تأكد من عدم وجود عمليات npm/Node أخرى تستخدم الدليل:  
   ```
   ps aux | grep npm
   ```  
   قم بقتل أي عمليات متبقية إذا لزم الأمر (على سبيل المثال، `sudo kill <PID>`)، ثم أعد المحاولة.

٤. **بديل: استخدام npx للاختبار**  
   إذا كنت تريد فقط اختبار الأداة بدون تثبيت عام كامل، جرب:  
   ```
   npx @anthropic-ai/claude-code --help
   ```  
   يقوم هذا بتنزيلها وتشغيلها مؤقتًا بدون تعديل الوحدات النمطية العامة الخاصة بك.

### نصائح إضافية
- **أفضل ممارسة للصلاحيات**: يمكن أن تؤدي عمليات التثبيت العامة باستخدام `sudo` إلى مشاكل ملكية لاحقًا. فكر في استخدام مدير إصدارات node مثل `nvm` لتجنب `sudo` تمامًا، أو قم بتعيين بادئة عامة مخصصة:  
  ```
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  export PATH=~/.npm-global/bin:$PATH
  ```  
  ثم قم بالتثبيت بدون `sudo`.
- **التحقق بعد التثبيت**: بمجرد التثبيت، تحقق باستخدام `claude-code --version` (بافتراض أن هذا هو اسم الملف الثنائي — تأكد من الوثائق).
- إذا استمرت المشاكل، شارك ناتج `npm ls -g @anthropic-ai/claude-code` لمزيد من التشخيص.

هذا يجب أن يجعلك تعمل بسرعة. إذا واجهت مشكلة أخرى، الصق السجل الجديد!

[Claude Code على npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[وثائق Anthropic: إعداد Claude Code](https://docs.claude.com/en/docs/claude-code/setup)