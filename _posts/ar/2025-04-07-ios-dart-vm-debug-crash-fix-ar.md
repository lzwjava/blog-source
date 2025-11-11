---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح عطل تصحيح أخطاء Dart VM لنظام iOS
translated: true
type: note
---

أنت تواجه مشكلة معروفة في التفاعل بين iOS و Dart VM: تحتاج Dart VM في **وضع التصحيح (JIT)** إلى جعل صفحات الذاكرة قابلة للتنفيذ أثناء وقت التشغيل، وقد شددت إصدارات iOS الحديثة السياسات بحيث تفشل `mprotect(..., PROT_EXEC)` مع `13 (Permission denied)`. هذا يتسبب في إحباط Dart VM أثناء إنهاء الكود وينتج عن ذلك التعطل الذي لصقته (SIGABRT). هذا ليس خطأ في كود تطبيق Flutter الخاص بك — إنه عدم توافق بين المنصة (سياسة iOS / النظام) ووضع VM. ([GitHub][1])

### ملخص سريع / السبب الجذري

* تستخدم نسخ التصحيح **JIT** في Dart (إعادة تحميل فورية/إعادة تشغيل فورية) التي تحتاج إلى تغيير حماية الذاكرة لجعل كود الآلة المُنشئ قابلاً للتنفيذ. إصدارات iOS الحديثة تمنع ذلك، مسببة `mprotect failed: 13 (Permission denied)` وتأكيد فشل في Dart VM. ([GitHub][1])

---

### حلول بديلة فورية (اختر ما يناسب سير عملك)

1.  **التشغيل على المحاكي** — يقوم المحاكي بتشغيل كود محاكي x86/arm حيث لا يتم تطبيق قيود JIT، لذا يعمل وضع التصحيح والإعادة الفورية.
    الأمر: `flutter run -d <معرف-المحاكي>` (أو افتح من خلال Xcode). ([GitHub][1])

2.  **استخدم وضع Profile أو Release (AOT) على الجهاز** — أنشئ كود AOT حتى لا تحتاج VM إلى تغيير حماية الصفحات أثناء وقت التشغيل. ستفقد خاصية إعادة التحميل الفورية ولكن التطبيق سيعمل على الجهاز.
    * للتثبيت التجريبي: `flutter build ios --release` ثم قم بالتثبيت عبر Xcode أو `flutter install --release`.
    * أو `flutter run --profile` / `flutter run --release` للتشغيل مباشرة. ([GitHub][1])

3.  **استخدم جهاز iOS أو إصدار نظام أقدم** (كاختبار مؤقت فقط): ظهر هذا القيد في بعض إصدارات/بيتا iOS؛ الأجهزة التي تعمل بإصدار iOS أقدم من السياسة المشددة لن تواجه هذه المشكلة. (ليس حلًا مثاليًا على المدى الطويل.) ([Stack Overflow][2])

---

### إصلاحات / توصيات على المدى الطويل

*   **حدث iOS / Xcode** — قامت Apple بتغيير السلوك عبر إصدارات البيتا؛ أحيانًا تقوم تصحيحات بيتا iOS اللاحقة باستعادة السلوك أو تغيير السياسة. إذا كنت تستخدم إصدار بيتا من iOS أدخل هذا القيد، فقم بالتحديث إلى الإصدار الذي يحتوي على التصحيح. (هناك تقارير تشير إلى أن إصدارات بيتا معينة من iOS أدخلت/أعادت هذه المشكلة وأن إصدارات بيتا لاحقة أصلحت أو غيرت السلوك.) ([Stack Overflow][2])

*   **قم بترقية Flutter/Dart إلى أحدث إصدار مستقر** — تتبع فرق Flutter/Dart هذه المشكلة في قضايا GitHub وأصدرت تحديثات/حلول بديلة بعد تغيير المنصة؛ تأكد من أن Flutter و Dart لديك محدثان. بعد الترقية، قم بتشغيل `flutter clean` وأعد البناء. ([GitHub][3])

*   **تابع المشكلة (المشاكل) الأساسية** — هناك قضايا وطلبات سحب (PRs) نشطة في Flutter تتعلق بفشل JIT/mprotect على iOS. اشترك في مناقشات قضايا Flutter لمعرفة الإصلاحات الدائمة أو سير عمل المطور الموصى بها. (يمكنني لصق الروابط إذا أردت.) ([GitHub][1])

---

### ملاحظة إضافية حول رسالة `UIScene` التي رأيتها أيضًا

رسالة دورة حياة `UIScene` في الأعلى (“`UIScene lifecycle will soon be required`…”) هي **تحذير** من iOS حول الانتقال إلى دورة حياة التطبيق الحديثة المعتمدة على المشاهد (iOS 13+). إنها غير مرتبطة بتعطل `mprotect`. يمكنك تجاهلها مؤقتًا، أو الانتقال إلى استخدام المشاهد (نفذ `SceneDelegate` / حدث `Info.plist`) إذا كنت تريد إزالة التحذير. إنها ليست سبب SIGABRT. ([GitHub][1])

---

### خطوات عملية واضحة أوصي بها الآن

1.  إذا كنت بحاجة إلى الحفاظ على إعادة التحميل الفورية: شغل على **المحاكي**.
    `flutter run -d <معرف-المحاكي>`

2.  إذا كنت تريد الاختبار على الجهاز الفعلي الآن: أنشئ **release/profile (AOT)**.
    `flutter run --release` (أو `flutter build ios --release` + تثبيت)

3.  حدث بيئة العمل: قم بترقية iOS (إذا كنت على إصدار بيتا بهذا الخلل)، حدث Xcode، حدث Flutter/Dart، `flutter clean`، ثم أعد المحاولة على الجهاز.

4.  إذا أردت، الصق ناتج الأمر `flutter doctor -v` وإصدار iOS / الجهاز المحدد الذي تختبر عليه وسأعطيك الخطوات التالية الأكثر تحديدًا (مثلًا، "إصدار iOS هذا معروف بوجود المشكلة — قم بالتحديث إلى X.Y.Z أو استخدم نسخ release").

---

### روابط / مراجع (لتتمكن من متابعة النقاش الأساسي)

*   قضية Flutter على GitHub تتابع مشكلة JIT في وضع التصحيح / `mprotect failed: 13` (نقاش وحلول بديلة). ([GitHub][1])
*   مناقشة على StackOverflow تبلغ عن نفس المشكلة `mprotect failed: 13` في بيتا iOS — تقترح تراجعًا في المنصة وتصحيحات في بيتا iOS. ([Stack Overflow][2])
*   مدونة/ملخص يشرح الخلاف بين iOS 26 و Flutter وخيارات التطوير الموصى بها. ([Medium][4])

---

إذا أردت، سأقوم بما يلي:

*   أعطيك أوامر `flutter` المحددة لبناء IPA بنسخة release وتثبيته على جهازك، أو
*   أتحقق من `flutter doctor -v` وإصدار نظام جهازك لأوصي بأفضل إجراء واحد الآن.

ماذا تفضل؟

[1]: https://github.com/flutter/flutter/issues/163984?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[2]: https://stackoverflow.com/questions/79473408/flutter-ios-18-4-debug-build-error-mprotect-failed-13-permission-denied?utm_source=chatgpt.com "Flutter iOS 18.4 Debug Build Error: mprotect failed"
[3]: https://github.com/flutter/flutter/actions/runs/15564769770?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[4]: https://vijay-mishra.medium.com/flutter-vs-ios26-what-broke-and-what-to-do-36c6d6bf1e16?utm_source=chatgpt.com "Flutter vs iOS 26: What Broke and How to Fix It - Vijay Mishra"