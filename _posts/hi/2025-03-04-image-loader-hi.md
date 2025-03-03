---
audio: false
generated: true
lang: hi
layout: post
title: Android mein Universal Image Loader
translated: true
---

यूनिवर्सल इमेज लोडर (UIL) वर्जन 1.9.3 एक शक्तिशाली और लचीला लाइब्रेरी है जो एंड्रॉइड एप्लिकेशन में छवियों को लोड, कैश और प्रदर्शित करने के लिए उपयोग किया जाता है। नीचे एक चरण-दर-चरण गाइड है कि कैसे आप इसे अपने एंड्रॉइड प्रोजेक्ट में उपयोग कर सकते हैं। ध्यान रखें कि यह लाइब्रेरी पुरानी है और इसे बंद कर दिया गया है (लगभग 2015 में अंतिम अपडेट किया गया था), इसलिए आधुनिक प्रोजेक्टों के लिए आप Glide या Picasso जैसी विकल्पों को विचार कर सकते हैं। हालांकि, अगर आप विशेष रूप से UIL 1.9.3 का उपयोग करना चाहते हैं, तो यहाँ कैसे करना है:

---

### चरण 1: लाइब्रेरी को प्रोजेक्ट में जोड़ें
UIL 1.9.3 Maven के माध्यम से उपलब्ध है, इसलिए आप इसे Gradle का उपयोग करके अपने प्रोजेक्ट में जोड़ सकते हैं। अगर आप पुराने सेटअप (जैसे Eclipse) के साथ काम कर रहे हैं, तो आप JAR फाइल को मैन्युअल रूप से डाउनलोड कर सकते हैं।

#### Gradle का उपयोग (Android Studio):
1. अपने एप्लिकेशन के `build.gradle` फ़ाइल को खोलें (मॉड्यूल: app).
2. `dependencies` ब्लॉक में निम्नलिखित निर्भरता जोड़ें:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. अपने प्रोजेक्ट को Gradle के साथ सिंक करें, Android Studio में "Sync Now" पर क्लिक करें।

#### मैन्युअल JAR सेटअप (जैसे Eclipse):
1. `universal-image-loader-1.9.3.jar` को Maven रिपोजिटरी या GitHub से डाउनलोड करें।
2. प्रोजेक्ट के `libs` फ़ोल्डर में JAR फ़ाइल रखें।
3. अपने आईडीई में JAR पर राइट-क्लिक करें, फिर "Add to Build Path" (Eclipse) चुनें या अपने प्रोजेक्ट सेटिंग्स में इसे मैन्युअल रूप से कॉन्फ़िगर करें।

---

### चरण 2: अनुमतियाँ जोड़ें
इंटरनेट से छवियों को लोड करने या उन्हें स्टोरेज में सेभ करने के लिए, अपने `AndroidManifest.xml` में निम्नलिखित अनुमतियाँ जोड़ें:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: URL से छवियों को डाउनलोड करने के लिए आवश्यक है।
- `WRITE_EXTERNAL_STORAGE`: डिस्क कैशिंग के लिए आवश्यक है (ऑफलाइन उपयोग के लिए अनिवार्य नहीं, लेकिन अनुशंसित है)। एंड्रॉइड 6.0+ (API 23+) के लिए, आपको रनटाइम पर इस अनुमति का अनुरोध करना भी होगा।

---

### चरण 3: ImageLoader को प्रारंभ करें
UIL का उपयोग करने से पहले, आपको इसे एक कॉन्फ़िगरेशन के साथ प्रारंभ करना होगा। यह आमतौर पर आपके `Application` क्लास या मुख्य `Activity` में एक बार किया जाता है।

#### एक कस्टम एप्लिकेशन क्लास बनाएं (अनुशंसित):
1. एक नया क्लास बनाएं (जैसे `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // ग्लोबल कॉन्फ़िगरेशन बनाएं और ImageLoader प्रारंभ करें
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // छवि लोडिंग थ्रेड के लिए कम प्राथमिकता
               .denyCacheImageMultipleSizesInMemory()    // मेमोरी में कई आकारों को कैश करने से रोकें
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB डिस्क कैश
               .diskCacheFileCount(100)                  // कैश में अधिकतम 100 फ़ाइलें
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. इस क्लास को अपने `AndroidManifest.xml` में पंजीकृत करें:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### या एक एक्टिविटी में प्रारंभ करें:
अगर आप एक `Application` क्लास का उपयोग नहीं करना चाहते, तो इसे अपने `Activity` के `onCreate()` विधि में प्रारंभ करें (लेकिन सुनिश्चित करें कि यह केवल एक बार प्रारंभ किया जाता है):
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

### चरण 4: छवि लोड और प्रदर्शित करें
प्रारंभ करने के बाद, आप `ImageLoader` का उपयोग कर सकते हैं `ImageView` में छवियों को लोड करने के लिए।

#### बेसिक उपयोग:
```java
import com.nostra13.universalimageloader.core.ImageLoader;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        String imageUrl = "https://example.com/image.jpg";

        // छवि को ImageView में लोड करें
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### डिस्प्ले ऑप्शंस के साथ उन्नत उपयोग:
आप `DisplayImageOptions` का उपयोग करके छवियों को कैसे लोड और प्रदर्शित किया जाता है, उसे कस्टमाइज़ कर सकते हैं:
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

        // डिस्प्ले ऑप्शंस परिभाषित करें
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // लोडिंग के दौरान प्रदर्शित छवि
            .showImageForEmptyUri(R.drawable.error)     // यदि URL खाली है तो प्रदर्शित छवि
            .showImageOnFail(R.drawable.error)          // लोडिंग विफल होने पर प्रदर्शित छवि
            .cacheInMemory(true)                        // RAM में कैश करें
            .cacheOnDisk(true)                          // डिस्क पर कैश करें
            .build();

        // ऑप्शंस के साथ छवि लोड करें
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### चरण 5: UIL का उपयोग ListView या GridView में
लिस्ट या ग्रिड के लिए, अपने एडाप्टर में UIL का उपयोग करें छवियों को प्रभावी ढंग से लोड करने के लिए।

#### उदाहरण कस्टम एडाप्टर:
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
    private String[] imageUrls; // छवि URL का एर्रे

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

#### एडाप्टर सेट करें:
```java
String[] imageUrls = {"https://example.com/image1.jpg", "https://example.com/image2.jpg"};
GridView gridView = findViewById(R.id.gridView);
gridView.setAdapter(new ImageAdapter(this, imageUrls));
```

---

### UIL 1.9.3 के प्रमुख विशेषताएं
- **सहायता URI प्रकार**:
  - वेब: `"http://example.com/image.jpg"`
  - एसडी कार्ड: `"file:///mnt/sdcard/image.png"`
  - कंटेंट प्रोवाइडर: `"content://media/external/images/media/13"`
  - एसेट्स: `"assets://image.png"`
  - ड्रॉअबल्स: `"drawable://" + R.drawable.image`
- **कैशिंग**: मेमोरी और डिस्क कैशिंग का समर्थन करता है।
- **कस्टमाइज़ेशन**: थ्रेड पूल आकार, कैश आकार और छवि डिकोडिंग ऑप्शंस को कॉन्फ़िगरेशन में समायोजित किया जा सकता है।

---

### समस्या निपटान
- **क्रैश: "ImageLoader must be init with configuration"**
  सुनिश्चित करें कि `ImageLoader.getInstance().init(config)` किसी भी `displayImage` कॉल से पहले किया गया है।
- **छवि लोड नहीं हो रही हैं**
  - इंटरनेट अनुमतियों और URL वैधता की जांच करें।
  - कॉन्फ़िगरेशन में लॉगिंग को सक्षम करें (`.writeDebugLogs()`) समस्याओं को डिबग करने के लिए।
- **मेमोरी से बाहर त्रुटियाँ**
  - कॉन्फ़िगरेशन में `diskCacheSize` या `memoryCacheSize` को कम करें।
  - छोटे छवियों का उपयोग करें या `DisplayImageOptions` में डाउनस्केलिंग को सक्षम करें।

---

### नोट्स
- **वर्जन 1.9.3 को पुराना कर दिया गया है (लगभग 2014 में अंतिम रिलीज़)। आधुनिक एंड्रॉइड विकास के लिए Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) या Coil (`implementation 'io.coil-kt:coil:2.6.0'`) को विचार करें।
- **तारीख संदर्भ**: 3 मार्च, 2025 तक, यह गाइड आपको UIL 1.9.3 को आवश्यकता वाले पुराने कोड के साथ काम कर रहे हैं, यह मानता है।

किसी विशेष उपयोग के मामले में मदद चाहिए तो मुझे बताएं!