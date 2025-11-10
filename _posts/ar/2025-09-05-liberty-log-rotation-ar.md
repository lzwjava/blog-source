---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تكوين تدوير سجلات ليبرتي
translated: true
type: note
---

إليك النسخة المختصرة، ثم أمثلة يمكنك لصقها في `server.xml`.

### كيفية عمل تدوير سجلات Liberty

* **ما يتم تدويره:** `messages.log` و `trace.log`.
  يمكن أن يكون التدوير **مبنيًا على الحجم** و/أو **مبنيًا على الوقت**. ([openliberty.io][1])
* **ما لا يتم تدويره:** `console.log` (إنه مجرد stdout/stderr). يمكنك تقليله أو تعطيله بدلاً من ذلك. ([openliberty.io][2], [IBM][3])
* **أين يتم التكوين:** عنصر `<logging …/>` في `server.xml`. (يمكنك أيضًا تعيين نفس القيم في `bootstrap.properties`/متغيرات البيئة إذا كنت بحاجة إلى تطبيقها *قبل* تحميل `server.xml`.) ([openliberty.io][2])
* **سجلات الوصول:** سجل الوصول HTTP لديه إعدادات التدوير **الخاصة به** المبنية على الوقت تحت `httpAccessLogging` / `accessLogging`. ([openliberty.io][4])
* **كل من الحجم + الوقت:** Liberty الحديث يدعم التدوير المبنى على الوقت بالإضافة إلى الخيار الكلاسيكي المبنى على الحجم، لذا يمكنك استخدام أي منهما أو كليهما (باستثناء `console.log`). ([IBM][5])

---

### وصفات شائعة لـ `server.xml`

#### ١) التدوير المبني على الحجم (كلاسيكي)

يحتفظ بما يصل إلى ١٠ ملفات، كل منها يصل إلى ٢٥٦ ميجابايت.

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

النتيجة: عندما يتجاوز `messages.log` أو `trace.log` حجم ٢٥٦ ميجابايت، يقوم Liberty بتدويره إلى ملف مؤقت بالطابع الزمني ويحتفظ بما لا يزيد عن ١٠ من هذه الملفات. (لا يؤثر على `console.log`.) ([openliberty.io][1])

#### ٢) التدوير المبني على الوقت (على سبيل المثال، يوميًا عند منتصف الليل)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

النتيجة: يتم تدوير `messages.log` و `trace.log` كل يوم في الساعة ٠٠:٠٠. يمكنك استخدام الدقائق (`m`) أو الساعات (`h`) أيضًا، على سبيل المثال، `30m` أو `6h`. ([openliberty.io][2])

#### ٣) الجمع بين الحجم والوقت (نموذجي للإنتاج)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

النتيجة: التدوير **أيهما يأتي أولاً** (الحجم أو الجدول الزمني)، والاحتفاظ بسجل تاريخي لـ ١٤ ملفًا. ([IBM][5])

#### ٤) ترويض أو تعطيل نمو `console.log`

`console.log` لا يمكن تدويره؛ قلل أو عطله واعتمد على `messages.log`.

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

ملاحظات: يؤدي تعطيل الكونسول إلى إيقاف نسخ السجل الخاص بـ Liberty إلى `console.log`، ولكن قد يظل JVM يكتب أشياء مثل `-verbose:gc` إلى stdout/stderr. ([openliberty.io][2])

#### ٥) تعديلات الاسم/التنسيق (اختياري)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON مفيد لإرسال السجلات إلى مكدس السجلات؛ اترك الإعدادات الافتراضية إذا كنت لا تحتاج إليه. ([openliberty.io][1])

---

### سجل الوصول HTTP (منفصل عما سبق)

تمكين تسجيل الوصول وتدويره يوميًا عند منتصف الليل:

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(أو ضع `rolloverStartTime`/`rolloverInterval` مباشرة على عنصر `<accessLogging …/>` تابع لـ `httpEndpoint`.) ([openliberty.io][4])

---

### قائمة مراجعة سريعة

* استخدم **`maxFileSize` + `maxFiles`** للتدوير المبني على الحجم. ([openliberty.io][1])
* استخدم **`rolloverStartTime` + `rolloverInterval`** للتدوير المبني على الوقت. ([openliberty.io][2])
* **لا تتوقع تدوير `console.log`**؛ عيّن `consoleLogLevel="OFF"` و `copySystemStreams="false"` إذا كنت تريد تجنب ملفات الكونسول الكبيرة. ([openliberty.io][2], [IBM][3])

إذا شاركت مقتطف `server.xml` الحالي أو أهداف الاحتفاظ الخاصة بك (على سبيل المثال، "الاحتفاظ بـ ~٧ أيام" أو "الحد الأقصى ٢ جيجابايت")، سأقوم بتخصيص القيم الدقيقة.

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."