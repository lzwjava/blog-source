---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل اختبار خادم الويب باستخدام أباتشي بنش
translated: true
type: note
---

### ما هو Apache Bench (ab)؟

Apache Bench (ab) هو أداة بسيطة عبر سطر الأوامر مدرجة مع خادم Apache HTTP لقياس أداء خوادم الويب. يرسل عددًا محددًا من طلبات HTTP إلى عنوان URL ويقيس مقاييس مثل الطلبات في الثانية، والوقت لكل طلب، ومعدلات النقل، ومعدلات الخطأ. إنه رائع لاختبار الحمل السريع ولكنه محدود في السيناريوهات المعقدة (على سبيل المثال، لا يدعم HTTPS افتراضيًا أو البرمجة النصية المتقدمة—فكر في استخدام أدوات مثل JMeter لتلك الأغراض).

### التثبيت

ab يأتي معبأ مع خادم Apache HTTP. إليك كيفية تثبيته:

- **على Ubuntu/Debian (Linux)**:
  ```
  sudo apt update
  sudo apt install apache2-utils
  ```

- **على macOS (عبر Homebrew)**:
  ```
  brew install httpd
  ```

- **على Windows**:
  قم بتنزيل Apache HTTP Server من الموقع الرسمي وأضف دليل `bin` الخاص به إلى PATH الخاص بك.

- **التحقق من التثبيت**:
  قم بتشغيل `ab -V` للتحقق من الإصدار.

### الاستخدام الأساسي

بناء جملة الأمر الأساسي هو:
```
ab [options] URL
```

- **تنسيق URL**: يجب أن يكون عنوان HTTP كامل، مثل `http://example.com/`. (لـ HTTPS، استخدم غلافًا مثل `openssl s_client` أو انتقل إلى أدوات مثل `wrk`).

الخيارات الرئيسية:
- `-n <requests>`: عدد الطلبات المراد تنفيذها (الافتراضي: 1). ابدأ بـ 100–1000 للاختبار.
- `-c <concurrency>`: عدد الطلبات المتعددة المراد إجراؤها في وقت واحد (الافتراضي: 1). حافظ على منخفض (مثل 10–50) لتجنب إرباك الخادم الخاص بك.
- `-t <seconds>`: التشغيل لمدة زمنية محددة بدلاً من عدد الطلبات.
- `-k`: تمكين HTTP Keep-Alive (يعيد استخدام الاتصالات).
- `-H "Header: Value"`: إضافة رؤوس مخصصة (مثلًا للمصادقة).
- `-p <file>`: بيانات POST من ملف.
- `-T <content-type>`: نوع المحتوى لطلبات POST.
- `-l`: قبول أطوال مستند متغيرة (للمحتوى الديناميكي).

### مثال خطوة بخطوة

1. **اختبار طلب GET بسيط**:
   محاكاة 100 طلب مع 10 مستخدمين متزامنين ضد خادم محلي:
   ```
   ab -n 100 -c 10 http://localhost:8080/
   ```
   نموذج للإخراج:
   ```
   Server Software:        Apache/2.4.41
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /
   Document Length:        1234 bytes

   Concurrency Level:      10
   Time taken for tests:   1.234 seconds
   Complete requests:      100
   Failed requests:        0
   Requests per second:    81.03 [#/sec] (mean)
   Time per request:       123.456 [ms] (mean)
   ```

2. **اختبار ببيانات POST** (مثل إرسال نموذج):
   أنشئ ملف `postdata.txt` يحتوي على الحمولة الخاصة بك (مثل `key=value`).
   ```
   ab -n 50 -c 5 -p postdata.txt -T application/x-www-form-urlencoded http://example.com/api/endpoint
   ```

3. **التشغيل لمدة زمنية**:
   ```
   ab -n 10000 -c 20 -t 30 http://example.com/  # حتى 10 آلاف طلب أو 30 ثانية
   ```

### تفسير النتائج

- **الطلبات في الثانية**: كلما زادت كان ذلك أفضل (الإنتاجية).
- **الوقت لكل طلب**: كلما قل كان ذلك أفضل (زمن الوصول).
- **معدل النقل**: كفاءة عرض النطاق الترددي.
- ابحث عن "Failed requests" أو "Non-2xx responses" لاكتشاف المشكلات.
- قم بتشغيل الاختبار عدة مرات ومتوسط النتائج، حيث يمكن للتخزين المؤقت/الشبكة أن يشوه النتائج الفردية.

### نصائح وقيود

- **التشغيل من جهاز منفصل**: لا تختبر ضد localhost إذا أمكن، لمحاكاة حركة المرور الحقيقية.
- **الإحماء**: أرسل بضع طلبات أولاً لتهيئة ذاكرة التخزين المؤقت.
- **التحجيم**: للحمل الأعلى، استخدم أدوات مثل `wrk` أو `siege` أو Locust.
- **HTTPS**: ab لا يدعمه بشكل أصلي؛ استخدم `ab -n 100 -c 10 http://example.com/` مع وكيل أو بدائل.
- **الأخطاء**: إذا رأيت "socket: Too many open files"، فقم بزيادة حد واصفات الملفات في نظام التشغيل الخاص بك (مثل `ulimit -n 4096`).

لمزيد من التفاصيل، تحقق من صفحة الدليل (`man ab`) أو الوثائق الرسمية.

[Apache Bench Documentation](https://httpd.apache.org/docs/2.4/programs/ab.html)