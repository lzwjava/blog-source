---
audio: false
generated: true
lang: en
layout: post
title: 'ButterKnife: a View binding Library'
translated: false
---

Butter Knife هو مكتبة شائعة لتربط العناصر الوظيفية في Android التي تسهل عملية ربط عناصر الواجهة المستخدمية مع الحقول في كودك. ومع ذلك، يرجى ملاحظة أن Butter Knife الآن قد تم إهماله، ويوصي تطوير Android الحديث باستخدام ربط الرؤية (مقدمة في Android Jetpack) بدلاً من ذلك. ومع ذلك، إذا كنت تحتاج إلى استخدام Butter Knife 6.1.0 (إصدار قديم صدر حوالي 2015) مع ملف `.jar` في مشروع Android، إليك كيفية القيام بذلك في Android Studio اعتبارًا من 3 مارس 2025.

### المتطلبات الأساسية
- Android Studio مرفق (يجب أن يعمل أي إصدار حديث، على الرغم من أن العملية قد تختلف قليلاً بناءً على إصدارك).
- مشروع Android أساسي مرفق.
- ملف `butterknife-6.1.0.jar` تم تنزيله. يمكنك العثور على الإصدارات القديمة عادةً في مستودعات مثل Maven Central أو من خلال المصادر المأرشفة إذا كنت تمتلك الملف `.jar` محليًا.

### خطوات استخدام `butterknife-6.1.0.jar` في تطوير Android

#### الخطوة 1: إضافة ملف `.jar` إلى مشروعك
1. **تحديد مجلد `libs`**:
   - في مشروع Android Studio، انتقل إلى وحدة التطبيق.
   - داخل مجلد التطبيق، ايجاد أو إنشاء مجلد باسم `libs`. إذا لم يكن موجودًا، انقر بزر الفأرة الأيمن على مجلد التطبيق، اختر `New > Directory`، واسمه `libs`.

2. **نسخ ملف `.jar`**:
   - انقر بزر الفأرة الأيمن على ملف `butterknife-6.1.0.jar` واسحبه إلى مجلد `libs`. يمكنك القيام بذلك عن طريق سحب الملف إلى مجلد `libs` في Android Studio أو وضعه هناك يدويًا من خلال مستكشف الملفات.

3. **مزامنة ملف `.jar` مع Gradle**:
   - افتح ملف `build.gradle` للوحدة التطبيق (موقع في `app/build.gradle`).
   - أضف السطر التالي تحت كتلة `dependencies` لتضمين جميع ملفات `.jar` في مجلد `libs`:
     ```gradle
     dependencies {
         compile fileTree(dir: 'libs', include: ['*.jar'])
     }
     ```
   - مزامنة مشروعك عن طريق النقر على زر "Sync Project with Gradle Files" في Android Studio.

#### الخطوة 2: تهيئة مشروعك
لأن Butter Knife 6.1.0 يستخدم معالجة التعليقات، فلا تحتاج إلى اعتماد معالجة التعليقات لهذا الإصدار المحدد (خلافًا للإصدارات اللاحقة مثل 8.x وما فوق). يحتوي ملف `.jar` على المكتبة التشغيلية، ويستخدم Butter Knife 6.1.0 الاستدلال في وقت التشغيل بدلاً من إنشاء الكود في وقت التجميع لمعظم وظائفه.

ومع ذلك، تأكد من أن مشروعك مهيأ لدعم تعليقات Java:
- في `app/build.gradle`، تأكد من أن إصدار Java متوافق (Butter Knife 6.1.0 يعمل مع Java 6+):
  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_6
          targetCompatibility JavaVersion.VERSION_1_6
      }
  }
  ```

#### الخطوة 3: استخدام Butter Knife في كودك
1. **إضافة تعليقات Butter Knife**:
   - في نشاطك أو شريحة، استورد Butter Knife وعلق على مشاهدك `@InjectView` (التعليق المستخدم في الإصدار 6.1.0). على سبيل المثال:
     ```java
     import android.os.Bundle;
     import android.widget.Button;
     import android.widget.TextView;
     import butterknife.InjectView;
     import butterknife.ButterKnife;
     import androidx.appcompat.app.AppCompatActivity;

     public class MainActivity extends AppCompatActivity {

         @InjectView(R.id.my_button)
         Button myButton;

         @InjectView(R.id.my_text)
         TextView myText;

         @Override
         protected void onCreate(Bundle savedInstanceState) {
             super.onCreate(savedInstanceState);
             setContentView(R.layout.activity_main);
             ButterKnife.inject(this); // ربط المشاهد

             // استخدام مثال
             myButton.setOnClickListener(v -> myText.setText("Button clicked!"));
         }
     }
     ```

2. **XML Layout**:
   - تأكد من أن ملف التهيئة (على سبيل المثال، `res/layout/activity_main.xml`) يحتوي على المشاهد مع المعرفات المقابلة:
     ```xml
     <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         android:orientation="vertical">

         <TextView
             android:id="@+id/my_text"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Hello World" />

         <Button
             android:id="@+id/my_button"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content"
             android:text="Click Me" />
     </LinearLayout>
     ```

3. **ربط المشاهد**:
   - يدعو `ButterKnife.inject(this)` في `onCreate` إلى ربط الحقول المعلق عليها بالمشاهد من التهيئة. لاحظ أن في الإصدار 6.1.0، يتم استخدام `inject` بدلاً من `bind` (الذي تم تقديمه في الإصدارات اللاحقة مثل 7.x و 8.x).

#### الخطوة 4: تشغيل مشروعك
- بنى واسق مشروعك. إذا كان كل شيء مهيأ بشكل صحيح، فسيقوم Butter Knife بربط مشاهدك، وسترى الواجهة المستخدمية تعمل كما هو متوقع.

### ملاحظات مهمة
- **تقييد الإصدار**: Butter Knife 6.1.0 قديم جدًا (صدر في 2015) ويفتقر إلى الميزات التي تم تقديمها في الإصدارات اللاحقة، مثل إنشاء الكود في وقت التجميع (من خلال معالجات التعليقات) ودعم `@BindView` بدلاً من `@InjectView`. يستخدم الاستدلال في وقت التشغيل، والذي قد يؤثر قليلاً على الأداء مقارنة بالبدائل الحديثة.
- **حالة الإهمال**: Butter Knife لم يعد يتم صيانته (توقف التطوير حوالي 2020)، ويوصي التوصية الرسمية باستخدام ربط الرؤية أو Jetpack Compose للمشاريع الجديدة.
- **إعداد بديل**: إذا كنت تستخدم إصدارًا أحدثًا (على سبيل المثال، 10.2.3)، ستحتاج إلى إضافة اعتماد معالجة التعليقات (على سبيل المثال، `annotationProcessor 'com.jakewharton:butterknife-compiler:10.2.3'`)، ولكن لم 6.1.0 مع ملف `.jar`، فهذا ليس مطلوبًا.
- **إصلاح الأخطاء**:
  - إذا حصلت على خطأ "cannot resolve symbol" لصفوف Butter Knife، تأكد من أن ملف `.jar` تم إضافته بشكل صحيح إلى مجلد `libs` وضمنه في اعتمادات Gradle.
  - إذا انهار التطبيق مع خطأ `NoClassDefFoundError`، تأكد من أن ملف `.jar` في مجلد `libs` وتم مزامنة المشروع.

### توصية
بينما يوضح هذا الدليل كيفية استخدام `butterknife-6.1.0.jar`، فاعتبر الانتقال إلى ربط الرؤية لمتابعة أكثر حداثة ودعمًا. إليك مقارنة سريعة:
- **Butter Knife 6.1.0**: يستخدم `@InjectView`، الاستدلال في وقت التشغيل، التكامل يدوي للملف `.jar`.
- **ربط الرؤية**: مدمج في Android، لا يوجد اعتمادات خارجية، يخلق فئات الربط في وقت التجميع، وnull-safe.