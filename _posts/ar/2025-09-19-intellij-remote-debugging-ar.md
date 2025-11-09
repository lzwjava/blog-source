---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: دليل إعداد تصحيح الأخطاء عن بُعد في IntelliJ
translated: true
type: note
---

إجابة قصيرة: نعم — إذا حافظت على تطابق عملية البuild وبيئة تشغيل JVM، فإن تصحيح الأخطاء عن بُعد في IntelliJ سيتصل بنجاح. إليك طريقة موثوقة وبسيطة لتحقيق ذلك على Liberty محليًا وعلى Cloud Foundry.

## ١) امنع "عدم تطابق الفئات" قبل التوصيل

* حاذِ إصدارات JDK دائمًا: يجب أن يتطابق الإصدار الرئيسي لـ JDK المستخدم في تجميع Maven، وJVM الخاص بـ Liberty، و(إذا كنت على CF) JDK الخاص بـ Java buildpack. في Maven، ثبِّت الإصدار باستخدام `maven-compiler-plugin` (`release` أو `source/target`) وتأكد من أن Liberty/CF يستخدم نفس الإصدار.
* نظِّف bytecode القديم عند تبديل الفروع أو تشغيل/إيقاف الوحدات: `mvn clean package -DskipTests` هو أبسط إجراء وقائي.
* في IntelliJ، استخدم أيضًا "Rebuild Project" مرة واحدة إذا كنت قد مزجت سابقًا بين بناء البيئة التطويرية وبناء Maven.

## ٢) أعد البناء تلقائيًا فقط عندما يكون ذلك ضروريًا (قاعدة ٣٠ دقيقة)

إذا أردت إعادة البناء فقط عندما يكون عمر الفئات المترجمة أكثر من ٣٠ دقيقة، فغَلِّف Maven بفحص بسيط.

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # no classes yet?
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # latest class mtime older than threshold?
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Classes are old (>= ${THRESHOLD_MIN}m) or missing — building…"
  mvn clean package -DskipTests
else
  echo "Classes are fresh (< ${THRESHOLD_MIN}m) — skipping build."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Classes are old (>= $thresholdMin m) or missing — building…"
  mvn clean package -DskipTests
} else {
  Write-Host "Classes are fresh (< $thresholdMin m) — skipping build."
}
```

## ٣) Liberty (محلي) — ابدأ في وضع التصحيح وتوصّل من IntelliJ

لديك خياران سهلان:

**أ. بدء تصحيح لمرة واحدة**

```bash
server debug myServer   # المنفذ الافتراضي لـ JDWP هو 7777
```

**ب. إعداد دائم**

* في `wlp/usr/servers/myServer/jvm.options`:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* أو عبر متغير البيئة:

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**التوصيل من IntelliJ**

* Run → "Edit Configurations…" → "Remote JVM Debug".
* Host: `localhost`, Port: `7777`.
* اضغط على Debug؛ يجب أن ترى "Connected to the target VM…" وسيتم ربط نقاط التوقف.

> نصيحة: بعد إعادة البناء، يلتقط Liberty الفئات المحدثة لمعظم الميزات عبر التبديل الساخن. إذا تغير توقيع دالة أو هيكل فئة، فستحتاج إلى إعادة تشغيل الخادم ليتم تحميل هذه التغييرات.

## ٤) Cloud Foundry (PCF) — ما هو الواقعي

يعمل CF على تشغيل التطبيقات خلف طبقة التوجيه الخاصة به؛ عادةً لا يمكنك تعريض منفذ JDWP مباشرة. لديك نمطان عمليان:

**الخيار ١: تصحيح Buildpack + نفق SSH (للتطوير/المراحل فقط)**

١. فعِّل تصحيح JVM في Java buildpack:

   * عيِّن متغير البيئة قبل الرفع (تختلف الأسماء قليلاً حسب إصدار buildpack):

   ```
   cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
   ```
٢. أعد التمرير:

   ```
   cf restage <APP>
   ```
٣. افتح نفق SSH:

   ```
   cf ssh -N -L 7777:localhost:7777 <APP>
   ```
٤. في IntelliJ، توصّل إلى `localhost:7777`.

**الخيار ٢: استخدم تشخيصات CF SSH JMX بدلاً من JDWP**

* عندما لا يُسمح بـ JDWP مباشرة، اعتمد على:

  * سجلات التطبيق + المسجلات المستهدفة،
  * تفريغ المؤشرات والخيوط عبر `cf ssh` + `jcmd`/`jmap` (إذا كانت موجودة)،
  * إشارات الميزات مثل تتبع Liberty ونقاط نهاية الصحة.

> تقييم الواقع: العديد من مؤسسات CF تعطّل منافذ التصحيح في بيئة الإنتاج. تعامل مع JDWP عن بُعد على CF كمسار تصحيح فقط للمساحات غير الإنتاجية. إذا منعك فريق المنصة، فارجع إلى السجلات + تشخيصات SSH.

## ٥) أسباب شائعة لـ "تعذر ربط نقاط التوقف" (والإصلاحات)

* **عدم تطابق ملف الفئة**: أعد البناء بعد التنظيف؛ تحقق من وجود نسخة واحدة فقط من الفئة في مسار الفئة أثناء التشغيل (انتبه لـ fat JARs أو الوحدات المكررة).
* **منفذ JDWP خاطئ**: تأكد من أن Liberty يستمع فعليًا (سجلات `server debug` أو `netstat` محليًا؛ بالنسبة لـ CF، يجب أن يتطابق سطر نفق SSH).
* **إصدار JDK رئيسي مختلف**: تأكد من أن إصدارات JDK لـ Maven/Liberty/CF هي نفسها (مثلًا، جميعها Java 17).
* **معلومات تصحيح المترجم مُزالَة**: تأكد من أن `maven-compiler-plugin` لا يستخدم `-g:none`. الإعداد الافتراضي جيد؛ إذا تم التخصيص، فقم بتضمين `-g`.
* **تحتاج إلى إعادة تحميل**: بعد تغييرات التوقيع، أعد تشغيل Liberty (أعد التمرير على CF).

---

إذا قمت بإعدادها كما هو موضح أعلاه — سواء باستخدام `mvn clean package` دائمًا أو باستخدام غلاف "قاعدة ٣٠ دقيقة" — فإن التصحيح عن بُعد في IntelliJ سيتصل بشكل موثوق بـ Liberty، ويمكن أن يعمل على CF عبر نفق SSH في البيئات غير الإنتاجية.