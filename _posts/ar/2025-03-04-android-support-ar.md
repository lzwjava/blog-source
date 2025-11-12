---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة دعم أندرويد
translated: true
type: note
---

إصدار مكتبة دعم Android `support-v4:19.1.0` هو إصدار أقدم من مكتبة دعم Android (مكتبة التوافق v4 تحديدًا)، والذي يوفر واجهات برمجة تطبيقات متوافقة مع الإصدارات السابقة لأجهزة Android التي تعمل بإصدارات API أقدم من أحدث الإصدارات في وقت إصدارها (حوالي عام 2014). تتيح لك هذه المكتبة استخدام الميزات التي تم تقديمها في إصدارات Android الأحدث على الأجهزة القديمة، مثل Fragments و Loaders وأدوات مساعدة أخرى.

نظرًا لأن `support-v4:19.1.0` هو جزء من مكتبة دعم Android القديمة، فقد حلت محلها مكتبات AndroidX. ومع ذلك، إذا كنت بحاجة إلى استخدام هذا الإصدار المحدد (على سبيل المثال، للحفاظ على مشروع قديم)، فإليك كيفية إعداده واستخدامه في مشروع Android الخاص بك:

---

### الخطوة 1: إضافة التبعية
لاستخدام `support-v4:19.1.0`، تحتاج إلى تضمينه كتبعية في مشروعك. يتم ذلك عادةً في ملف `build.gradle` الخاص بك (الوحدة: app).

#### للمشاريع القائمة على Gradle
1. افتح ملف `app/build.gradle` الخاص بك.
2. أضف السطر التالي إلى كتلة `dependencies`:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. زامن مشروعك مع Gradle بالنقر على "Sync Now" في Android Studio.

#### ملاحظات:
- تأكد من ضبط `compileSdkVersion` على 19 (Android 4.4 KitKat) على الأقل أو إصدار أحدث، حيث أن هذه المكتبة تتماشى مع ميزات API 19.
- الحد الأدنى لإصدار SDK المدعوم من قبل `support-v4:19.1.0` هو API 4 (Android 1.6)، ولكن يجب عليك ضبط `minSdkVersion` بناءً على متطلبات تطبيقك.

مثال `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // اضبط حسب الحاجة
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### الخطوة 2: التحقق من التوفر
يتم استضافة مكتبات دعم Android في مستودع Maven من Google. بدءًا من Android Studio 3.0+، يتم تضمين هذا المستودع افتراضيًا. إذا كنت تستخدم إصدارًا أقدم من Android Studio، فتأكد من وجود ما يلي في ملف `build.gradle` الخاص بك (على مستوى المشروع):

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // ملاحظة: تم إيقاف JCenter، ولكنه كان مستخدمًا للمكتبات القديمة
    }
}
```

إذا واجهت مشاكل في تنزيل المكتبة، قد تحتاج إلى تثبيت "مستودع دعم Android" عبر مدير SDK:
1. انتقل إلى `Tools > SDK Manager`.
2. ضمن علامة التبويب "SDK Tools"، حدد "Android Support Repository" وقم بتثبيته.

---

### الخطوة 3: استخدام المكتبة في الكود الخاص بك
توفر مكتبة `support-v4` مجموعة متنوعة من الفئات، مثل `Fragment`، و`Loader`، و`AsyncTaskLoader`، وأدوات مساعدة مثل `ActivityCompat`. فيما يلي أمثلة حول كيفية استخدام بعض المكونات الشائعة:

#### المثال 1: استخدام Fragments
تتضمن مكتبة `support-v4` فئة `Fragment` مدعومة للإصدارات السابقة والتي تعمل على إصدارات Android القديمة.

```java
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class MyFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_layout, container, false);
    }
}
```

لاستخدام هذا الـ fragment في activity:
```java
import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.os.Bundle;

public class MainActivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FragmentManager fm = getSupportFragmentManager();
        fm.beginTransaction()
            .add(R.id.fragment_container, new MyFragment())
            .commit();
    }
}
```

#### المثال 2: استخدام ActivityCompat
توفر فئة `ActivityCompat` طرقًا مساعدة للميزات المتوافقة مع الإصدارات السابقة، مثل طلب الأذونات (التي تم تقديمها في API 23 ولكن يمكن استخدامها مسبقًا مع مكتبة الدعم).

```java
import android.support.v4.app.ActivityCompat;
import android.Manifest;
import android.content.pm.PackageManager;

public class MainActivity extends FragmentActivity {
    private static final int REQUEST_CODE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.CAMERA},
                    REQUEST_CODE);
        }
    }
}
```

---

### الخطوة 4: الاعتبارات
- **مكتبة قديمة**: مكتبة دعم Android، بما في ذلك `support-v4:19.1.0`، قديمة. للتطوير الحديث، قم بالانتقال إلى AndroidX (على سبيل المثال، `androidx.legacy:legacy-support-v4:1.0.0`). تعتبر AndroidX الخليفة وتوفر التحديثات والدعم المستمرين.
- **مطابقة الإصدار**: إذا كنت تستخدم مكتبات دعم أخرى (مثل `appcompat-v7`)، فتأكد من أن تكون بنفس الإصدار (19.1.0) لتجنب أخطاء عدم تطابق الإصدار.
- **الحد الأدنى لـ SDK**: بينما يدعم `support-v4:19.1.0` API 4+، قد تتطلب بعض الميزات `minSdkVersion` أعلى (على سبيل المثال، API 14 للمكونات المعينة التي تم تقديمها لاحقًا).

---

### الخطوة 5: الانتقال إلى AndroidX (اختياري ولكنه موصى به)
إذا كنت تقوم بالحفاظ على مشروع قديم، ففكر في الانتقال إلى AndroidX:
1. في Android Studio، انتقل إلى `Refactor > Migrate to AndroidX`.
2. قم بتحديث التبعيات الخاصة بك، على سبيل المثال، استبدل `com.android.support:support-v4:19.1.0` بـ `androidx.legacy:legacy-support-v4:1.0.0`.
3. اتبع دليل الانتقال المقدم من Android Studio.

---

### استكشاف الأخطاء وإصلاحها
- **"تعذر العثور على المكتبة"**: تأكد من أن اتصالك بالإنترنت نشط وأن مستودع Maven من Google يمكن الوصول إليه.
- **عدم تطابق الإصدار**: إذا رأيت أخطاء حول إصدارات مكتبة الدعم غير المتطابقة، فقم بمحاذاة جميع تبعيات `com.android.support` إلى الإصدار 19.1.0.
- **الميزات القديمة**: بعض واجهات برمجة التطبيقات في `support-v4:19.1.0` (مثل `AsyncTask`) قديمة. تحقق من الوثائق للبدائل.

أعلمني إذا كنت بحاجة إلى مساعدة في حالة استخدام أو إعداد معين!