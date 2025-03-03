---
audio: false
generated: true
lang: ar
layout: post
title: محمول محمول في أندرويد
translated: true
---

مكتبة Universal Image Loader (UIL) الإصدار 1.9.3 هي مكتبة قوية ومتعددة الاستخدامات لتحميل، تخزين في الذاكرة المؤقتة، وعرض الصور في تطبيقات Android. أدناه دليل خطوة بخطوة على كيفية استخدامها في مشروع Android الخاص بك. يرجى ملاحظة أن هذه المكتبة قديمة وتم إيقافها (آخر تحديث حوالي 2015)، لذلك بالنسبة للمشاريع الحديثة، قد تفضل استخدام بدائل مثل Glide أو Picasso. ومع ذلك، إذا كنت تحتاج إلى استخدام UIL 1.9.3 بشكل محدد، إليك كيفية القيام بذلك:

---

### الخطوة 1: إضافة المكتبة إلى مشروعك
منذ أن UIL 1.9.3 متاحة عبر Maven، يمكنك إضافتها إلى مشروعك باستخدام Gradle. إذا كنت تعمل مع إعدادات قديمة (مثل Eclipse)، يمكنك تحميل ملف JAR يدويًا.

#### باستخدام Gradle (Android Studio):
1. افتح ملف `build.gradle` لمودول التطبيق الخاص بك (Module: app).
2. أضف التبعية التالية في كتلة `dependencies`:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. قم بتزامن المشروع مع Gradle من خلال النقر على "Sync Now" في Android Studio.

#### إعداد JAR يدويًا (مثل Eclipse):
1. تحميل `universal-image-loader-1.9.3.jar` من مستودع Maven أو GitHub.
2. وضع ملف JAR في مجلد `libs` لمشروعك.
3. انقر باليمين على JAR في IDE الخاص بك، ثم اختر "Add to Build Path" (Eclipse) أو قم بتكوينه يدويًا في إعدادات المشروع الخاص بك.

---

### الخطوة 2: إضافة الإذن
لتحميل الصور من الإنترنت أو حفظها في التخزين، أضف الإذن التالي إلى ملف `AndroidManifest.xml` الخاص بك:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: مطلوب لتحميل الصور من URLs.
- `WRITE_EXTERNAL_STORAGE`: مطلوب لتخزين الصور المؤقتة على القرص (اختياري، ولكن موصى به للاستخدام بدون اتصال). بالنسبة لأندرويد 6.0+ (API 23+)، ستحتاج أيضًا إلى طلب هذا الإذن في وقت التشغيل.

---

### الخطوة 3: تهيئة ImageLoader
قبل استخدام UIL، يجب عليك تهيئته مع إعدادات. يتم ذلك عادةً مرة واحدة في فئة `Application` أو النشاط الرئيسي.

#### إنشاء فئة تطبيق مخصصة (الموصى به):
1. إنشاء فئة جديدة (مثل `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // إنشاء إعدادات عالمية وتهيئة ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // أولوية أقل للخطوط التي تحميل الصور
               .denyCacheImageMultipleSizesInMemory()    // منع تخزين عدة أحجام في الذاكرة
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB تخزين على القرص
               .diskCacheFileCount(100)                  // أقصى 100 ملف في التخزين المؤقت
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. تسجيل هذه الفئة في ملف `AndroidManifest.xml` الخاص بك:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### أو تهيئة في نشاط:
إذا كنت لا تريد استخدام فئة `Application`، قم بتهيئتها في طريقة `onCreate()` للنشاط الخاص بك (ولكن تأكد من أنها تهيئة مرة واحدة فقط):
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
        .build();
    ImageLoader.getInstance().init(config);
}
```

---

### الخطوة 4: تحميل وعرض صورة
بعد التهيئة، يمكنك استخدام `ImageLoader` لتحميل الصور في `ImageView`.

#### الاستخدام الأساسي:
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // تحميل الصورة في ImageView
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### الاستخدام المتقدم مع خيارات العرض:
يمكنك تخصيص كيفية تحميل الصور وعرضها باستخدام `DisplayImageOptions`:
```java
import com.nostra13.universalimageloader.core.DisplayImageOptions;
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // تعريف خيارات العرض
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // الصورة التي يتم عرضها أثناء التحميل
            .showImageForEmptyUri(R.drawable.error)     // الصورة التي يتم عرضها إذا كان URL فارغًا
            .showImageOnFail(R.drawable.error)          // الصورة التي يتم عرضها إذا فشل التحميل
            .cacheInMemory(true)                        // تخزين في الذاكرة
            .cacheOnDisk(true)                          // تخزين على القرص
            .build();

        // تحميل الصورة مع الخيارات
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### الخطوة 5: استخدام UIL في ListView أو GridView
للساعات أو الشبكات، استخدم UIL في مبدلك لتحميل الصور بشكل فعال.

#### مثال مبدل مخصص:
```java
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import com.nostra13.universalimageloader.core.ImageLoader;

public class ImageAdapter extends BaseAdapter {
    private Context context;
    private String[] imageUrls; // مصفوفة من URLs الصور

    public ImageAdapter(Context context, String[] imageUrls) {
        this.context = context;
        this.imageUrls = imageUrls;
    }

    @Override
    public int getCount() {
        return imageUrls.length;
    }

    @Override
    public Object getItem(int position) {
        return imageUrls[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.list_item, parent, false);
        }

        ImageView imageView = convertView.findViewById(R.id.imageView);
        ImageLoader.getInstance().displayImage(imageUrls[position], imageView);

        return convertView;
    }
}
```

#### تعيين المبدل:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### الميزات الرئيسية لـ UIL 1.9.3
- **أنواع URI المدعومة**:
  - ويب: `"http://example.com/image.jpg"`
  - بطاقة SD: `"file:///mnt/sdcard/image.png"`
  - مزود المحتوى: `"content://media/external/images/media/13"`
  - الأصول: `"assets://image.png"`
  - الرسومات: `"drawable://" + R.drawable.image`
- **التخزين المؤقت**: يدعم التخزين المؤقت في الذاكرة والقرص.
- **التخصيص**: يمكن تعديل حجم مجموعة الخيوط، حجم التخزين المؤقت، وخيارات فك تشفير الصورة في الإعدادات.

---

### حل المشاكل
- **الانهيار: "يجب أن يتم تهيئة ImageLoader مع الإعدادات"**  
  تأكد من أن `ImageLoader.getInstance().init(config)` يتم استدعاؤه قبل أي استدعاءات `displayImage`.
- **الصور لا تحميل**  
  - تحقق من الإذن بالإنترنت وصدق URL.
  - قم بتفعيل التسجيل في الإعدادات (`.writeDebugLogs()`) لحل المشاكل.
- **خطأ في الذاكرة**  
  - خفض `diskCacheSize` أو `memoryCacheSize` في الإعدادات.
  - استخدم صور أصغر أو قم بتفعيل تقليل الحجم في `DisplayImageOptions`.

---

### الملاحظات
- **الاستبدال**: UIL 1.9.3 قديم (آخر إصدار ~2014). بالنسبة لتطوير Android الحديث، فكري في استخدام Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) أو Coil (`implementation 'io.coil-kt:coil:2.6.0'`).
- **السياق الزمني**: اعتبارًا من 3 مارس 2025، يرجى أن تكون تعمل مع كود قديم يتطلب UIL 1.9.3.

أعلمني إذا كنت تحتاج إلى مساعدة في حالة استخدام محدد!