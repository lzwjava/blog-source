---
audio: false
generated: true
lang: ar
layout: post
title: محمل الصور العالمي في أندرويد
translated: true
type: note
---

مُحمِّل الصور العالمي (UIL) الإصدار 1.9.3 هو مكتبة قوية ومرنة لتحميل وتخزين الصور مؤقتًا وعرضها في تطبيقات Android. فيما يلي دليل خطوة بخطوة حول كيفية استخدامه في مشروع Android الخاص بك. لاحظ أن هذه المكتبة قديمة وقد توقف تطويرها (آخر تحديث حوالي عام 2015)، لذلك بالنسبة للمشاريع الحديثة، قد ترغب في النظر في بدائل مثل Glide أو Picasso. ومع ذلك، إذا كنت بحاجة تحديدًا إلى استخدام UIL 1.9.3، فإليك الطريقة:

---

### الخطوة 1: إضافة المكتبة إلى مشروعك
نظرًا لأن UIL 1.9.3 متاح عبر Maven، يمكنك إضافته إلى مشروعك باستخدام Gradle. إذا كنت تعمل بإعداد قديم (مثل Eclipse)، يمكنك تنزيل ملف JAR يدويًا.

#### باستخدام Gradle (Android Studio):
1. افتح ملف `build.gradle` الخاص بتطبيقك (Module: app).
2. أضف الاعتمادية التالية في كتلة `dependencies`:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. زامن مشروعك مع Gradle من خلال النقر على "Sync Now" في Android Studio.

#### الإعداد اليدوي لـ JAR (مثل Eclipse):
1. حمِّل `universal-image-loader-1.9.3.jar` من Maven Repository أو GitHub.
2. ضع ملف JAR في مجلد `libs` الخاص بمشروعك.
3. انقر بزر الماوس الأيمن على ملف JAR في بيئة التطوير المتكاملة الخاصة بك، ثم حدد "Add to Build Path" (في Eclipse) أو قم بتكوينه يدويًا في إعدادات مشروعك.

---

### الخطوة 2: إضافة الأذونات
لتحميل الصور من الإنترنت أو حفظها في وحدة التخزين، أضف الأذونات التالية إلى ملف `AndroidManifest.xml` الخاص بك:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: مطلوبة لتنزيل الصور من عناوين URL.
- `WRITE_EXTERNAL_STORAGE`: مطلوبة للتخزين المؤقت على القرص (اختياري، ولكن موصى به للاستخدام دون اتصال). بالنسبة لـ Android 6.0+ (API 23+)، ستحتاج أيضًا إلى طلب هذا الإذن أثناء وقت التشغيل.

---

### الخطوة 3: تهيئة ImageLoader
قبل استخدام UIL، يجب عليك تهيئته باستخدام التكوين. يتم ذلك عادةً مرة واحدة في فئة `Application` الرئيسية أو `Activity`.

#### إنشاء فئة Application مخصصة (موصى بها):
1. أنشئ فئة جديدة (مثال: `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // إنشاء التكوين العام وتهيئة ImageLoader
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // أولوية أقل لخيوط تحميل الصور
               .denyCacheImageMultipleSizesInMemory()    // منع تخزين أحجام متعددة في الذاكرة مؤقتًا
               .diskCacheSize(50 * 1024 * 1024)          // تخزين مؤقت على القرص بسعة 50 ميجابايت
               .diskCacheFileCount(100)                  // 100 ملف كحد أقصى في ذاكرة التخزين المؤقت
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. سجل هذه الفئة في ملف `AndroidManifest.xml` الخاص بك:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### أو قم بالتهيئة في Activity:
إذا كنت لا تريد استخدام فئة `Application`، فقم بتهيئتها في طريقة `onCreate()` الخاصة بـ `Activity` الخاصة بك (ولكن تأكد من تهيئتها مرة واحدة فقط):
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
بمجرد التهيئة، يمكنك استخدام `ImageLoader` لتحميل الصور في `ImageView`.

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
            .showImageOnLoading(R.drawable.placeholder) // الصورة المعروضة أثناء التحميل
            .showImageForEmptyUri(R.drawable.error)     // الصورة المعروضة إذا كان عنوان URL فارغًا
            .showImageOnFail(R.drawable.error)          // الصورة المعروضة إذا فشل التحميل
            .cacheInMemory(true)                        // التخزين المؤقت في الذاكرة العشوائية (RAM)
            .cacheOnDisk(true)                          // التخزين المؤقت على القرص
            .build();

        // تحميل الصورة مع الخيارات
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### الخطوة 5: استخدام UIL في ListView أو GridView
للقيائم أو الشبكات، استخدم UIL في المحول (adapter) الخاص بك لتحميل الصور بكفاءة.

#### مثال على محول مخصص:
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
    private String[] imageUrls; // مصفوفة عناوين URL للصور

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

#### تعيين المحول:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### الميزات الرئيسية لـ UIL 1.9.3
- **أنواع URI المدعومة**:
  - الويب: `"http://example.com/image.jpg"`
  - بطاقة SD: `"file:///mnt/sdcard/image.png"`
  - موفر المحتوى: `"content://media/external/images/media/13"`
  - Assets: `"assets://image.png"`
  - Drawables: `"drawable://" + R.drawable.image`
- **التخزين المؤقت**: يدعم التخزين المؤقت في الذاكرة وعلى القرص.
- **التخصيص**: يمكن ضبط حجم مجموعة الخيوط، وحجم ذاكرة التخزين المؤقت، وخيارات فك تشفير الصور في التكوين.

---

### استكشاف الأخطاء وإصلاحها
- **تعطل: "يجب تهيئة ImageLoader باستخدام التكوين"**  
  تأكد من استدعاء `ImageLoader.getInstance().init(config)` قبل أي استدعاءات `displayImage`.
- **الصور لا يتم تحميلها**  
  - تحقق من أذونات الإنترنت وصحة عنوان URL.
  - قم بتمكين التسجيل (logging) في التكوين (`.writeDebugLogs()`) لتصحيح الأخطاء.
- **أخطاء نفاد الذاكرة**  
  - قلل `diskCacheSize` أو `memoryCacheSize` في التكوين.
  - استخدم صورًا أصغر حجمًا أو مكّن التصغير (downscaling) في `DisplayImageOptions`.

---

### ملاحظات
- **إهمال الاستخدام**: UIL 1.9.3 قديم (آخر إصدار ~2014). لتطوير Android الحديث، فكر في استخدام Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) أو Coil (`implementation 'io.coil-kt:coil:2.6.0'`).
- **سياق التاريخ**: اعتبارًا من 3 مارس 2025، يفترد هذا الدليل أنك تعمل على كود قديم يتطلب UIL 1.9.3.

دعني أعلم إذا كنت بحاجة إلى مساعدة في حالة استخدام محددة!