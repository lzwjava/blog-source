---
audio: false
generated: true
lang: ar
layout: post
title: استخدام ButterKnife لربط المناظر
translated: true
type: note
---

Butter Knife هي مكتبة شائعة لربط العناصر في واجهة المستخدم لتطبيقات Android تبسط عملية ربط عناصر واجهة المستخدم بالحقول في الكود الخاص بك. ومع ذلك، يرجى ملاحظة أن Butter Knife أصبحت الآن مهملة، ويوصي تطوير Android الحديث باستخدام View Binding (الذي تم تقديمه في Android Jetpack) بدلاً من ذلك. ومع ذلك، إذا كنت بحاجة إلى استخدام Butter Knife 6.1.0 (إصدار قديم تم إصداره حوالي عام 2015) مع ملف `.jar` في مشروع Android، فإليك كيف يمكنك القيام بذلك في Android Studio اعتبارًا من 03 مارس 2025.

### المتطلبات الأساسية
- تثبيت Android Studio (أي إصدار حديث يجب أن يعمل، على الرغم أن العملية قد تختلف قليلاً بناءً على إصدارك).
- مشروع Android أساسي تم إعداده.
- ملف `butterknife-6.1.0.jar` الذي تم تنزيله. يمكنك عادةً العثور على الإصدارات القديمة في مستودعات مثل Maven Central أو من خلال المصادر المؤرشفة إذا كان لديك ملف `.jar` محليًا.

### خطوات استخدام `butterknife-6.1.0.jar` في تطوير تطبيقات Android

#### الخطوة 1: إضافة ملف `.jar` إلى مشروعك
1. **تحديد موقع مجلد `libs`**:
   - في مشروع Android Studio الخاص بك، انتقل إلى وحدة `app`.
   - داخل مجلد `app`، ابحث عن مجلد باسم `libs` أو قم بإنشائه. إذا كان غير موجود، انقر بزر الماوس الأيمن على مجلد `app`، واختر `New > Directory`، وقم بتسميته `libs`.

2. **نسخ ملف `.jar`**:
   - انسخ ملف `butterknife-6.1.0.jar` إلى مجلد `libs`. يمكنك القيام بذلك عن طريق سحب الملف وإفلاته في مجلد `libs` في Android Studio أو وضعه هناك يدويًا عبر مستكشف الملفات.

3. **مزامنة ملف `.jar` مع Gradle**:
   - افتح ملف `build.gradle` لوحدة `app` (الموجود في `app/build.gradle`).
   - أضف السطر التالي تحت كتلة `dependencies` لتضمين جميع ملفات `.jar` في مجلد `libs`:
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - قم بمزامنة مشروعك بالنقر على زر "Sync Project with Gradle Files" في Android Studio.

#### الخطوة 2: تكوين مشروعك
نظرًا لأن Butter Knife 6.1.0 يستخدم معالجة الشرح (annotation processing)، فإنك لا تحتاج إلى تبعية معالج الشرح (annotation processor) لهذا الإصدار المحدد (على عكس الإصدارات اللاحقة مثل 8.x وما فوق). يحتوي ملف `.jar` على مكتبة وقت التشغيل، وتعتمد Butter Knife 6.1.0 على الانعكاس (reflection) في وقت التشغيل بدلاً من توليد الكود في وقت الترجمة لمعظم وظائفها.

ومع ذلك، تأكد من إعداد مشروعك لدعم شروحات Java:
- في ملف `app/build.gradle` الخاص بك، تأكد من توافق إصدار Java (يعمل Butter Knife 6.1.0 مع Java 6+):
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### الخطوة 3: استخدام Butter Knife في الكود الخاص بك
1. **إضافة شروحات Butter Knife