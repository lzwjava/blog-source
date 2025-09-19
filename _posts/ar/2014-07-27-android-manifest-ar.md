---
audio: false
generated: false
image: false
lang: ar
layout: post
title: فهم ملف AndroidManifest.xml
translated: true
---

إذا كنت تغمق في تطوير تطبيقات Android، من بين أول الملفات التي ستواجهها هو `AndroidManifest.xml`. إنه مثل المخطط المعماري لتطبيقك - يشرح نظام Android كل ما يحتاجه عن تطبيقك قبل أن يبدأ حتى في التشغيل. اليوم، سنفصل ملف بيان مثال من تطبيق يُدعى "Flower" (اسم الحزمة: `com.lzw.flower`) ونستكشف مكوناته الرئيسية، المفاهيم، والنماذج.

---

#### ما هو AndroidManifest.xml؟

`AndroidManifest.xml` هو ملف تكوين مطلوب لكل تطبيق Android. يعيش في الدليل الجذر لمشروعك ويعلن معلومات أساسية مثل اسم حزمة التطبيق، الإذنات، المكونات (مثل الأنشطة)، والميزات المادية/برمجية التي يحتاجها. افهمه كبطاقة هوية للتطبيق التي يقرأها نظام التشغيل Android.

دعونا نمر عبر المثال خطوة بخطوة.

---

### هيكل البيان

هنا البيان الذي نعمل عليه (مبسط قليلاً لمسهولة القراءة):

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.lzw.flower"
    android:versionCode="8"
    android:versionName="1.5.2">

    <uses-sdk android:minSdkVersion="14" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-feature android:name="android.hardware.camera" />
    <uses-feature android:name="android.hardware.camera.autofocus" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

    <application
        android:label="@string/app_name"
        android:icon="@drawable/icon128"
        android:name=".base.App"
        android:theme="@style/AppTheme">

        <activity android:name=".deprecated.CameraActivity" android:screenOrientation="landscape" />
        <activity android:name=".base.SplashActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity android:name=".draw.DrawActivity" android:screenOrientation="landscape" />
        <activity android:name=".result.ResultActivity" android:screenOrientation="landscape" />
        <activity android:name=".material.MaterialActivity" android:screenOrientation="landscape" />
        <activity android:name=".activity.PhotoActivity" android:screenOrientation="landscape" />
        <activity android:name=".activity.LoginActivity" android:screenOrientation="portrait" />
    </application>
</manifest>
```

الآن دعونا نفصله إلى أقسامه الأساسية ونشرح المفاهيم وراءها.

---

### 1. العنصر الجذر `<manifest>`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.lzw.flower"
    android:versionCode="8"
    android:versionName="1.5.2">
```

- **`xmlns:android`**: يحدد مساحة الاسم XML للميزات الخاصة بAndroid. إنه نموذج قياسي ستجده في كل بيان.
- **`package`**: هو المعرف الفريد لتطبيقك (مثل `com.lzw.flower`). إنه أيضًا مساحة الاسم الافتراضية لمفاتيح Java/Kotlin.
- **`android:versionCode`**: عدد صحيح داخلي (هنا، `8`) يستخدم لتتبع الإصدارات. يزداد مع كل تحديث.
- **`android:versionName`**: سلسلة إصدارات قابلة للقراءة من قبل البشر (هنا، `1.5.2`) تظهر للمستخدمين.

**المفهوم**: يحدد علامة `<manifest>` هوية التطبيق وإصداراته، مما يضمن أن يعرف النظام ما هو التطبيق الذي يعمل عليه وكيفية معالجة التحديثات.

---

### 2. إصدار SDK مع `<uses-sdk>`

```xml
<uses-sdk android:minSdkVersion="14" />
```

- **`android:minSdkVersion`**: يحدد المستوى الأدنى لمجموعة API Android التي يدعمها التطبيق. API 14 يعادل Android 4.0 (Ice Cream Sandwich).

**المفهوم**: هذا يضمن التوافق. لا يمكن لأجهزة تشغيل Android أقل من 4.0 تثبيت هذا التطبيق. لا يوجد `targetSdkVersion` أو `maxSdkVersion` هنا، ولكن يمكن إضافتهما لتعديل التوافق بشكل أكبر.

---

### 3. الإذنات مع `<uses-permission>`

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

يطلب هذا التطبيق عدة إذنات:
- `CAMERA`: للوصول إلى كاميرا الجهاز.
- `WRITE_EXTERNAL_STORAGE`: لحفظ الملفات (مثل الصور) في التخزين الخارجي.
- `INTERNET`: للوصول إلى الشبكة.
- `ACCESS_NETWORK_STATE`: للتحقق من اتصال الشبكة.
- `READ_PHONE_STATE`: للوصول إلى معلومات الجهاز (مثل IMEI).
- `ACCESS_WIFI_STATE`: للتحقق من حالة Wi-Fi.

**المفهوم**: يستخدم Android نظام الإذنات لحماية خصوصية المستخدم وأمنه. هذه الإعلانات تشرح للنظام (والمستخدم) ما هي الميزات الحساسة التي يحتاجها التطبيق. بعد Android 6.0 (API 23)، تتطلب الإذنات الخطرة (مثل `CAMERA`) أيضًا طلبات زمنية في كود التطبيق.

---

### 4. الميزات مع `<uses-feature>`

```xml
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```

- **`android.hardware.camera`**: يعلن أن التطبيق يحتاج إلى كاميرا.
- **`android.hardware.camera.autofocus`**: يحدد أن الكاميرا يجب أن تدعم التركيز التلقائي.

**المفهوم**: على عكس الإذنات، تفلتر علامات `<uses-feature>` التطبيق في Google Play Store. إذا لم يكن الجهاز يحتوي على كاميرا أو التركيز التلقائي، فلن يظهر التطبيق حتى كقابل للتثبيت إلا إذا تم تحديدهما كاختياريين مع `android:required="false"`.

---

### 5. العنصر `<application>`

```xml
<application
    android:label="@string/app_name"
    android:icon="@drawable/icon128"
    android:name=".base.App"
    android:theme="@style/AppTheme">
```

- **`android:label`**: اسم التطبيق، مستخرج من مصدر السلسلة (`@string/app_name`).
- **`android:icon`**: أيقونة التطبيق، مرجع إلى مصدر رسم (`@drawable/icon128`).
- **`android:name`**: فئة تطبيق مخصصة (`.base.App`) التي تم توسيعها من فئة `Application` الخاصة بAndroid لتطبيق منطق شامل.
- **`android:theme`**: نمط العرض الافتراضي للتطبيق (`@style/AppTheme`).

**المفهوم**: يحدد علامة `<application>` الإعدادات الشاملة للتطبيق. الموارد مثل `@string` و `@drawable` تخزن في مجلدات `res/`، مما يروج لإعادة الاستخدام والتحليل.

---

### 6. الأنشطة مع `<activity>`

يستعرض البيان عدة Activities، وهي شاشات واجهة المستخدم للتطبيق:

#### مثال 1: شاشة التهيئة (Activity المبتدئ)

```xml
<activity
    android:name=".base.SplashActivity"
    android:theme="@android:style/Theme.Holo.Light.NoActionBar.Fullscreen">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

- **`android:name`**: اسم الفئة (`.base.SplashActivity`).
- **`intent-filter`**: يحدد هذا كبداية التطبيق (`MAIN` الفعل + `LAUNCHER` الفئة)، بحيث يظهر في قائمة التطبيقات على الجهاز.
- **`android:theme`**: نمط شاشة كاملة بدون شريط عمل.

**النموذج**: Activity المبتدئ هو نقطة البداية الشائعة، غالبًا ما تكون شاشة التهيئة أو الشاشة الرئيسية.

#### مثال 2: Activity الكاميرا

```xml
<activity
    android:name=".deprecated.CameraActivity"
    android:screenOrientation="landscape">
```

- **`android:screenOrientation`**: يحدد الوضع الأفقي.
- **`.deprecated`**: يشير إلى أن هذه Activity قد تكون قديمة ولكن لا تزال مدمجة.

**النموذج**: غالبًا ما تحدد Activities الوضع لأغراض محددة (مثل أن تطبيقات الكاميرا تعمل بشكل أفضل في الوضع الأفقي).

#### Activities أخرى

يستعرض البيان Activities أخرى مثل `DrawActivity` و `ResultActivity` و `PhotoActivity` و `LoginActivity` مع نماذج مشابهة:
- معظمها في الوضع الأفقي، مما يشير إلى تطبيق موجه للصور أو الوسائط.
- بعضها يغير نمط التطبيق الافتراضي (مثل `Theme.Holo.Light`).

**المفهوم**: Activities هي وحدات بناء واجهة المستخدم للتطبيق Android. كل علامة `<activity>` تسجل شاشة مع النظام.

---

### نماذج رئيسية في هذا البيان

1. **تصميم موجه للوسائط**: الإذنات والميزات للكاميرا والتخزين والتفوق يشير إلى تطبيق صور أو رسم (ربما هو تحديد الزهور، بناءً على اسم الحزمة `com.lzw.flower`).
2. **تحكم في التوجه**: استخدام كبير لـ `android:screenOrientation="landscape"` يشير إلى التركيز على المهام المرئية.
3. **Activities مدمجة**: Activities متعددة (`CameraActivity` و `DrawActivity` و `ResultActivity`) تشير إلى عملية عمل متعددة الخطوات.
4. **استخدام الموارد**: مراجع إلى `@string` و `@drawable` و `@style` تظهر بنية نظيفة ومتينة.

---

### الخاتمة

`AndroidManifest.xml` أكثر من مجرد ملف تكوين - إنه نافذة إلى غرض التطبيق وسلوكه. في هذه الحالة، يبدو أن "Flower" هو تطبيق وسائط مع وظائف الكاميرا وميزات الرسم وميزات الشبكة، ربما لتحميل أو معالجة الصور. من خلال فهم مكوناته - الإذنات والميزات والActivities - يمكنك رؤية كيفية بناء تطبيقات Android وكيفية تصميم التطبيقات الخاصة بك.

هل تريد بناء شيء مشابه؟ ابدأ بمهمة واضحة (مثل تحديد الزهور)، حدد إذناتك وميزاتك، وخرط Activities. سيجمع البيان كل شيء!