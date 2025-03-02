---
audio: false
generated: false
lang: ar
layout: post
title: تكوين npm
translated: true
---

يبدو أنك تحاول استرجاع تكوين الوكيل من npm باستخدام `npm config get proxy`، ولكنك تواجه خطأ يشير إلى أن إعداد الوكيل محمي أو غير قابل للوصول بالطريقة القياسية. قد يحدث ذلك بسبب كيفية معالجة npm للمعلومات الحساسة أو بسبب قيود في بيئتك.

هنا كيفية حل المشكلة والتشخيص:

1. **تحقق من تكوين npm يدويًا**
   بدلاً من الاعتماد على `npm config get proxy` فقط، يمكنك فحص كامل تكوين npm لمعرفة إذا كان الوكيل محدد. قم بتشغيل:
   ```
   npm config list
   ```
   سيعرض هذا جميع إعدادات التكوين، بما في ذلك `proxy` و `https-proxy` إذا كانت محددة. ابحث عن أسطر مثل:
   ```
   proxy = "http://username:password@proxy-server:port"
   https-proxy = "http://username:password@proxy-server:port"
   ```

2. **إيجاد ملف تكوين npm**
   يخزن npm تكويناته في ملف `.npmrc`. يمكنك التحقق من مكانه عن طريق تشغيل:
   ```
   npm config get userconfig
   ```
   عادةً ما يشير هذا إلى `~/.npmrc` (في أنظمة مشابهة لUnix) أو `%USERPROFILE%\.npmrc` (في Windows). افتح هذا الملف في محرر النصوص لمعرفة إذا كان الوكيل محدد فيه. قد يبدو مثل:
   ```
   proxy=http://username:password@proxy-server:port
   https-proxy=http://username:password@proxy-server:port
   ```

3. **حماية البيانات الحساسة**
   إذا كان إعدادات الوكيل تحتوي على معلومات حساسة (مثل اسم المستخدم أو كلمة المرور)، قد يمنع npm الوصول المباشر لمنع الكشف عن طريق الخطأ. حاول تشغيل الأمر بصلاحيات مرفوعة (إذا كان ذلك مناسبًا) أو التحقق من أن متغيرات البيئة لا تتغلب على الإعدادات:
   ```
   echo $http_proxy  # في أنظمة مشابهة لUnix
   echo %HTTP_PROXY%  # في Windows
   ```

4. **تحديد أو تحديث إعدادات الوكيل**
   إذا كنت تحاول تأكيد الوكيل لأنه لا يعمل، قد تحتاج إلى تحديده أو تحديثه يدويًا. استخدم:
   ```
   npm config set proxy http://username:password@proxy-server:port
   npm config set https-proxy http://username:password@proxy-server:port
   ```
   ثم التحقق باستخدام `npm config list`.

5. **سياق الخطأ**
   إذا استمر الخطأ، هل يمكنك مشاركة الرسالة الخطأ الدقيقة التي يعيدها npm؟ ذلك سيساعد في تحديد ما إذا كان هذا مشكلة صلاحيات أو مشكلة في الصياغة أو شيء آخر.

أعلمني بما تجد أو إذا كنت تحتاج إلى مساعدة إضافية!