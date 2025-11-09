---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح فشل توقيع كود Flutter في Xcode
translated: true
type: note
---

أنت تواجه فشل توقيع الشفرة الشائع في Flutter وXcode: لم يجد Xcode أو أداة `security` هويات توقيع صالحة، لذا لا يمكن لـ `flutter run` توقيع التطبيق لتشغيله على جهاز فعلي. أدناه سأقدم مجموعة واضحة ومُرتبة من الإصلاحات وأوامر استكشاف الأخطاء وإصلاحها — اختر المسار الذي تريده (التشغيل على المُحاكي الآن، أو إعداد التوقيع للتشغيل على جهاز حقيقي). لن أطلب المزيد من المعلومات — سأفترض أنك تريد إصلاح هذه المشكلة الآن.

---

# خيارات سريعة (اختر واحدًا)

**أ — التشغيل على المُحاكي (لا يتطلب توقيع الشفرة)**
إذا كنت تريد التشغيل بسرعة دون التعامل مع الشهادات:

1. افتح المُحاكي: `open -a Simulator`
2. شغّل Flutter مستهدفًا المُحاكي:
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   أو بشكل أبسط: `flutter run -d iPhone-14` (استبدل باسم مُحاكٍ متوفر كما يظهر في `xcrun simctl list`).

**ب — إصلاح التوقيع للنشر على جهاز حقيقي (مُوصى به لاختبار الجهاز)**
اتبع الخطوات أدناه بالترتيب.

---

# خطوات إصلاح التوقيع لنشر التطبيق على الجهاز

## 1) تأكيد بيئة العمل والفحوصات الأساسية

شغّل هذه الأوامر ولاحظ الناتج:

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

يجب أن يُظهر الأمر `security find-identity -p codesigning -v` هوية واحدة على الأقل. أظهر الأمر في حالتك `0 valid identities found` — وهذا سبب الفشل.

## 2) استخدام التوقيع التلقائي في Xcode (الطريقة الأسهل)

1. افتح مساحة العمل:
   `open ios/Runner.xcworkspace`
2. في Xcode: اختر مشروع `Runner` → الهدف `Runner` → **Signing & Capabilities**.
3. عيّن **Team** إلى معرف Apple ID / حساب Apple Developer الخاص بك. إذا لم يكن معرف Apple ID مضافًا:

   * Xcode → Preferences → Accounts → `+` → أضف Apple ID.
4. فعّل **Automatically manage signing**.
5. تأكد من أن **Bundle Identifier** فريد (بأسلوب reverse-DNS، مثل `com.yourname.yourapp`).
6. سيحاول Xcode إنشاء شهادة تطوير وملف توفير؛ إذا ظهرت لك مطالبات، اسمح لـ Xcode بإدارتها.

> ملاحظة: لنشر التطبيق بشكل كامل على أي جهاز، تحتاج إلى عضوية Apple Developer المدفوعة (99 دولار/سنويًا). يمكن لـ Xcode استخدام Apple ID مجاني لـ "Free provisioning"، لكنه محدود (عدد الأجهزة، وغياب بعض الصلاحيات).

## 3) تسجيل جهازك (إذا لزم الأمر)

إذا لم يستطع Xcode تسجيل جهازك تلقائيًا، اذهب إلى Apple Developer Portal → Certificates, IDs & Profiles → Devices → أضف UDID الجهاز. يمكنك الحصول على UDID الجهاز بتوصيل الجهاز واختياره في نافذة Devices and Simulators في Xcode.

## 4) إنشاء/استيراد الشهادة يدويًا (إذا كان لديك ملف p12 بالفعل)

إذا كان لديك شهادة `.p12` ومفتاح خاص:

```bash
security import /path/to/certificate.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORD" -T /usr/bin/codesign
```

ثم أعد تشغيل `security find-identity -p codesigning -v` لتأكيد ظهورها.

## 5) إذا كنت تفضل أن ينشئ Xcode الشهادات نيابة عنك

في Xcode → Accounts → اختر Apple ID الخاص بك → Manage Certificates → `+` → أضف **iOS Development**. سينشئ هذا شهادة في سلسلة المفاتيح الخاصة بك وستظهر في `security find-identity`.

## 6) تأكد من ضبط Command Line Tools

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

ثم قبول الترخيص إذا لزم الأمر:

```bash
sudo xcodebuild -license accept
```

## 7) بعد إعداد التوقيع، شغّل من الطرفية

من مجلد المشروع الرئيسي:

```bash
flutter clean
flutter pub get
flutter run
```

إذا كان هناك أجهزة متعددة، حدد الجهاز باستخدام `-d <معرف-الجهاز>`.

---

# نصائح استكشاف الأخطاء وإصلاحها والمشاكل الشائعة

* **استمرار ظهور "0 valid identities found"** — تأكد من أن المفتاح الخاص للشهادة موجود في سلسلة المفاتيح login (افتح Keychain Access → login). إذا قمت باستيراد الشهادة دون المفتاح الخاص، سيفشل التوقيع.
* **عدم تطابق Bundle ID** — يجب أن يتطابق App ID في Developer Portal مع bundle identifier في Xcode تمامًا (يُسمح باستخدام النمط العام wildcard في بعض الحالات).
* **لم يتم اختيار Team** — يظهر Xcode "No account" — أضف Apple ID في Xcode Preferences → Accounts.
* **انتهاء صلاحية ملف التوفير provisioning profile** — تحقق من Developer Portal وأعد إنشاء ملف التوفير.
* **قيود Free provisioning** — إذا كنت تستخدم Apple ID مجاني، قد تحتاج إلى إعادة التوفير كل 7 أيام ولديك عدد أجهزة محدود.
* **الأتمتة أو CI** — استخدم `fastlane match` أو واجهات برمجة تطبيقات App Store Connect لإدارة الشهادات وملفات التوفير مركزياً.
* **أخطاء صلاحية Codesign** — تأكد من أن عنصر Keychain يمنح صلاحية codesign؛ في بعض الأحيان يجب السماح يدويًا لـ `/usr/bin/codesign` بالوصول إلى المفتاح الخاص في Keychain.
* **إذا استمر فشل `flutter run`**، شغّل بناء Xcode لرؤية خطأ مفصل: افتح مساحة العمل واضغط Run في Xcode؛ تحقق من أخطاء Signing & Capabilities في الواجهة.

---

# أوامر مفيدة للنسخ واللصق

عرض هويات توقيع الشفرة:

```bash
security find-identity -p codesigning -v
```

استيراد `.p12`:

```bash
security import /path/to/yourcert.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORD" -T /usr/bin/codesign
```

ضبط أدوات سطر أوامر Xcode:

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

فتح مساحة العمل الخاصة بـ iOS:

```bash
open ios/Runner.xcworkspace
```

---

# إذا أردت، يمكنني

* تقديم التسلسل الدقيق للنقرات في Xcode لإنشاء شهادة/ملف توفير خطوة بخطوة (لقد ضمنت الخطوات الأساسية بالفعل)، أو
* تقديم أوامر مثال لـ `fastlane`/`match` إذا كنت تريد أتمتة لعدة أجهزة/CI، أو
* المساعدة في تفسير أي ناتج خطأ جديد بعد تجربة طريقة التوقيع التلقائي في Xcode.

أخبرني أي مسار اخترت (المُحاكي الآن / Xcode التلقائي / الاستيراد اليدوي لـ p12 / CI) والصق أي أخطاء جديدة إذا استمر الفشل — وسأقدم لك الخطوات التالية.