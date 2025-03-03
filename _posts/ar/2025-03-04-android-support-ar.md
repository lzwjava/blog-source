---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة دعم أندرويد
translated: true
---

المكتبة الداعمة لـ Android الإصدار `support-v4:19.1.0` هي نسخة قديمة من مكتبة Android Support (خاصة مكتبة التوافق v4)، والتي توفر واجهات برمجة التطبيقات (APIs) متوافقة للخلف لأجهزة Android التي تعمل على مستويات API أقل من أحدثها في وقت إصدارها (حوالي 2014). تسمح هذه المكتبة لك باستخدام ميزات تم تقديمها في إصدارات Android أحدث على أجهزة قديمة، مثل الفragments، loaders، ومجموعة متنوعة من الأدوات الأخرى.

منذ أن `support-v4:19.1.0` جزء من مكتبة Android Support القديمة، فقد تم استبدالها بمكتبات AndroidX. ومع ذلك، إذا كنت تحتاج إلى استخدام هذه النسخة المحددة (على سبيل المثال، للحفاظ على مشروع قديم)، إليك كيفية إعدادها واستخدامها في مشروع Android الخاص بك:

---

### الخطوة 1: إضافة التبعية
لاستخدام `support-v4:19.1.0`، عليك تضمينها كتعليقة في مشروعك. يتم ذلك عادةً في ملف `build.gradle` الخاص بك (Module: app).

#### لمشاريع Gradle
1. افتح ملف `app/build.gradle` الخاص بك.
2. أضف السطر التالي إلى كتلة `dependencies`:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. قم بمزامنة مشروعك مع Gradle عن طريق النقر على "Sync Now" في Android Studio.

#### الملاحظات:
- تأكد من أن `compileSdkVersion` تم تعيينه على الأقل إلى 19 (Android 4.4 KitKat) أو أعلى، حيث أن هذه المكتبة متوافق مع ميزات API 19.
- أدنى مستوى SDK المدعوم من `support-v4:19.1.0` هو API 4 (Android 1.6)، ولكن يجب عليك تعيين `minSdkVersion` بناءً على متطلبات تطبيقك.

مثال على `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // تعديل حسب الحاجة
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### الخطوة 2: التحقق من التوفر
تم استضافة مكتبات Android Support في مخزن Google Maven. منذ Android Studio 3.0+، يتم تضمين هذا المخزن بشكل افتراضي. إذا كنت تستخدم نسخة قديمة من Android Studio، تأكد من أن التالي موجود في `build.gradle` (مستوى المشروع):

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // ملاحظة: JCenter متقاعد، ولكن كان يستخدم لمكتبات قديمة
    }
}
```

إذا واجهت مشاكل في تحميل المكتبة، قد تحتاج إلى تثبيت Android Support Repository من خلال مدير SDK:
1. اذهب إلى `Tools > SDK Manager`.
2. تحت علامة التبويب "SDK Tools"، قم بتحديد "Android Support Repository" وقلبه.

---

### الخطوة 3: استخدام المكتبة في كودك
توفر مكتبة `support-v4` مجموعة متنوعة من الفئات مثل `Fragment`، `Loader`، `AsyncTaskLoader`، وأدوات مثل `ActivityCompat`. أدناه أمثلة على كيفية استخدام بعض المكونات الشائعة:

#### مثال 1: استخدام الفragments
تضمين مكتبة `support-v4` فئة `Fragment` تم إعادة تقديمها تعمل على إصدارات Android القديمة.

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

لاستخدام هذا الفragment في نشاط:
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

#### مثال 2: استخدام ActivityCompat
توفر فئة `ActivityCompat` طرق مساعدة للميزات متوافقة للخلف، مثل طلب الإذن (تم تقديمها في API 23 ولكن يمكن استخدامها سابقاً مع المكتبة الداعمة).

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

### الخطوة 4: المعايير
- **مكتبة متقاعدة**: مكتبة Android Support، بما في ذلك `support-v4:19.1.0`، متقاعدة. لممارسة تطوير حديثة، هاجر إلى AndroidX (على سبيل المثال، `androidx.legacy:legacy-support-v4:1.0.0`). AndroidX هو الوارث ويوفر تحديثات ودعم مستمر.
- **مطابقة الإصدار**: إذا كنت تستخدم مكتبات دعم أخرى (على سبيل المثال، `appcompat-v7`)، تأكد من أن جميعها من نفس الإصدار (19.1.0) لتجنب أخطاء عدم تطابق الإصدار.
- **أدنى SDK**: بينما يدعم `support-v4:19.1.0` API 4+، قد تتطلب بعض الميزات مستوى SDK أدنى (على سبيل المثال، API 14 لمكونات تم تقديمها لاحقًا).

---

### الخطوة 5: الهجرة إلى AndroidX (اختياري ولكن موصى به)
إذا كنت تحافظ على مشروع قديم، فاعتبر الهجرة إلى AndroidX:
1. في Android Studio، اذهب إلى `Refactor > Migrate to AndroidX`.
2. قم بتحديث تعليقاتك، على سبيل المثال، استبدل `com.android.support:support-v4:19.1.0` بـ `androidx.legacy:legacy-support-v4:1.0.0`.
3. اتبع دليل الهجرة الذي يوفره Android Studio.

---

### حل المشاكل
- **"لم يتم العثور على المكتبة"**: تأكد من أن اتصال الإنترنت فعال ومخزن Google Maven متاح.
- **عدم تطابق الإصدار**: إذا رأيت أخطاء حول عدم تطابق إصدارات مكتبة الدعم، قم بتطابق جميع تعليقات `com.android.support` إلى 19.1.0.
- **ميزات متقاعدة**: بعض APIs في `support-v4:19.1.0` (على سبيل المثال، `AsyncTask`) متقاعدة. تحقق من الوثائق للحصول على بدائل.

أعلمني إذا كنت تحتاج إلى مساعدة في حالة استخدام أو إعداد معين!