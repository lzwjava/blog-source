---
audio: false
generated: true
lang: hi
layout: post
title: एंड्रॉइड में यूनिवर्सल इमेज लोडर
translated: true
type: note
---

यूनिवर्सल इमेज लोडर (UIL) वर्जन 1.9.3 एंड्रॉइड एप्लिकेशन में इमेज लोड करने, कैश करने और दिखाने के लिए एक शक्तिशाली और लचीली लाइब्रेरी है। नीचे आपके एंड्रॉइड प्रोजेक्ट में इसका उपयोग करने के लिए चरण-दर-चरण मार्गदर्शिका दी गई है। ध्यान दें कि यह लाइब्रेरी पुरानी है और इसे बंद कर दिया गया है (आखिरी अपडेट लगभग 2015 में), इसलिए आधुनिक प्रोजेक्ट्स के लिए, आप Glide या Picasso जैसे विकल्पों पर विचार कर सकते हैं। हालाँकि, यदि आपको विशेष रूप से UIL 1.9.3 का उपयोग करने की आवश्यकता है, तो यहाँ बताया गया है कि इसे कैसे करें:

---

### चरण 1: अपने प्रोजेक्ट में लाइब्रेरी जोड़ें
चूंकि UIL 1.9.3 Maven के माध्यम से उपलब्ध है, आप इसे Gradle का उपयोग करके अपने प्रोजेक्ट में जोड़ सकते हैं। यदि आप पुराने सेटअप (जैसे, Eclipse) के साथ काम कर रहे हैं, तो आप मैन्युअल रूप से JAR फ़ाइल डाउनलोड कर सकते हैं।

#### Gradle का उपयोग करके (Android Studio):
1. अपनी ऐप की `build.gradle` फ़ाइल (Module: app) खोलें।
2. `dependencies` ब्लॉक में निम्नलिखित डिपेंडेंसी जोड़ें:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Android Studio में "Sync Now" पर क्लिक करके अपने प्रोजेक्ट को Gradle के साथ सिंक करें।

#### मैन्युअल JAR सेटअप (उदाहरण के लिए, Eclipse):
1. Maven Repository या GitHub से `universal-image-loader-1.9.3.jar` डाउनलोड करें।
2. JAR फ़ाइल को अपने प्रोजेक्ट की `libs` फ़ोल्डर में रखें।
3. अपने IDE में JAR पर राइट-क्लिक करें, फिर "Add to Build Path" (Eclipse) चुनें या इसे अपनी प्रोजेक्ट सेटिंग्स में मैन्युअल रूप से कॉन्फ़िगर करें।

---

### चरण 2: अनुमतियाँ जोड़ें
इंटरनेट से इमेज लोड करने या उन्हें स्टोरेज में सेव करने के लिए, अपने `AndroidManifest.xml` में निम्नलिखित अनुमतियाँ जोड़ें:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: URL से इमेज डाउनलोड करने के लिए आवश्यक।
- `WRITE_EXTERNAL_STORAGE`: डिस्क कैशिंग के लिए आवश्यक (वैकल्पिक, लेकिन ऑफ़लाइन उपयोग के लिए अनुशंसित)। Android 6.0+ (API 23+) के लिए, आपको रनटाइम पर इस अनुमति का अनुरोध भी करना होगा।

---

### चरण 3: ImageLoader को इनिशियलाइज़ करें
UIL का उपयोग करने से पहले, आपको इसे एक कॉन्फ़िगरेशन के साथ इनिशियलाइज़ करना होगा। यह आमतौर पर आपकी `Application` क्लास या मुख्य `Activity` में एक बार किया जाता है।

#### एक कस्टम Application क्लास बनाएँ (अनुशंसित):
1. एक नई क्लास बनाएँ (उदाहरण के लिए, `MyApplication.java`):
   ```java
   import android.app.Application;
   import com.nostra13.universalimageloader.core.ImageLoader;
   import com.nostra13.universalimageloader.core.ImageLoaderConfiguration;

   public class MyApplication extends Application {
       @Override
       public void onCreate() {
           super.onCreate();

           // ग्लोबल कॉन्फ़िगरेशन बनाएँ और ImageLoader को इनिशियलाइज़ करें
           ImageLoaderConfiguration config = new ImageLoaderConfiguration.Builder(this)
               .threadPriority(Thread.NORM_PRIORITY - 2) // इमेज लोडिंग थ्रेड्स के लिए कम प्राथमिकता
               .denyCacheImageMultipleSizesInMemory()    // मल्टीपल साइज कैश करने से रोकें
               .diskCacheSize(50 * 1024 * 1024)          // 50 MB डिस्क कैश
               .diskCacheFileCount(100)                  // कैश में अधिकतम 100 फ़ाइलें
               .build();

           ImageLoader.getInstance().init(config);
       }
   }
   ```
2. इस क्लास को अपने `AndroidManifest.xml` में रजिस्टर करें:
   ```xml
   <application
       android:name=".MyApplication"
       ... >
   ```

#### या एक Activity में इनिशियलाइज़ करें:
यदि आप `Application` क्लास का उपयोग नहीं करना चाहते हैं, तो इसे अपनी `Activity` के `onCreate()` मेथड में इनिशियलाइज़ करें (लेकिन सुनिश्चित करें कि यह केवल एक बार इनिशियलाइज़ हो):
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

### चरण 4: एक इमेज लोड करें और दिखाएँ
एक बार इनिशियलाइज़ हो जाने के बाद, आप `ImageLoader` का उपयोग `ImageView` में इमेज लोड करने के लिए कर सकते हैं।

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

        // ImageView में इमेज लोड करें
        ImageLoader.getInstance().displayImage(imageUrl, imageView);
    }
}
```

#### डिस्प्ले ऑप्शंस के साथ एडवांस्ड उपयोग:
आप `DisplayImageOptions` का उपयोग करके कस्टमाइज़ कर सकते हैं कि इमेज कैसे लोड और दिखाई जाएँ:
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

        // डिस्प्ले ऑप्शंस डिफाइन करें
        DisplayImageOptions options = new DisplayImageOptions.Builder()
            .showImageOnLoading(R.drawable.placeholder) // लोडिंग के दौरान दिखने वाली इमेज
            .showImageForEmptyUri(R.drawable.error)     // यदि URL खाली है तो दिखने वाली इमेज
            .showImageOnFail(R.drawable.error)          // यदि लोडिंग फेल होती है तो दिखने वाली इमेज
            .cacheInMemory(true)                        // RAM में कैश करें
            .cacheOnDisk(true)                          // डिस्क पर कैश करें
            .build();

        // ऑप्शंस के साथ इमेज लोड करें
        ImageLoader.getInstance().displayImage(imageUrl, imageView, options);
    }
}
```

---

### चरण 5: ListView या GridView में UIL का उपयोग करना
लिस्ट या ग्रिड के लिए, इमेज को एफिशिएंटली लोड करने के लिए अपने एडाप्टर में UIL का उपयोग करें।

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
    private String[] imageUrls; // इमेज URL की ऐरे

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

### UIL 1.9.3 की मुख्य विशेषताएं
- **समर्थित URI प्रकार**:
  - वेब: `"http://example.com/image.jpg"`
  - SD कार्ड: `"file:///mnt/sdcard/image.png"`
  - कंटेंट प्रोवाइडर: `"content://media/external/images/media/13"`
  - एसेट्स: `"assets://image.png"`
  - ड्रॉएबल्स: `"drawable://" + R.drawable.image`
- **कैशिंग**: मेमोरी और डिस्क कैशिंग का समर्थन करता है।
- **कस्टमाइज़ेशन**: कॉन्फ़िगरेशन में थ्रेड पूल साइज, कैश साइज, और इमेज डिकोडिंग ऑप्शंस को एडजस्ट किया जा सकता है।

---

### समस्या निवारण
- **क्रैश: "ImageLoader must be init with configuration"**  
  सुनिश्चित करें कि किसी भी `displayImage` कॉल से पहले `ImageLoader.getInstance().init(config)` को कॉल किया गया है।
- **इमेज लोड नहीं हो रही हैं**  
  - इंटरनेट अनुमतियाँ और URL की वैधता जांचें।
  - समस्याओं को डीबग करने के लिए कॉन्फ़िगरेशन में लॉगिंग सक्षम करें (`.writeDebugLogs()`)।
- **आउट ऑफ मेमोरी एरर्स**  
  - कॉन्फ़िगरेशन में `diskCacheSize` या `memoryCacheSize` कम करें।
  - छोटी इमेज का उपयोग करें या `DisplayImageOptions` में डाउनस्केलिंग सक्षम करें।

---

### नोट्स
- **डिप्रिकेशन**: UIL 1.9.3 पुरानी हो चुकी है (आखिरी रिलीज़ ~2014)। आधुनिक एंड्रॉइड डेवलपमेंट के लिए, Glide (`implementation 'com.github.bumptech.glide:glide:4.16.0'`) या Coil (`implementation 'io.coil-kt:coil:2.6.0'`) पर विचार करें।
- **तिथि संदर्भ**: 3 मार्च, 2025 तक, यह गाइड मानती है कि आप लीगेसी कोड के साथ काम कर रहे हैं जिसके लिए UIL 1.9.3 की आवश्यकता है।

मुझे बताएं यदि आपको किसी विशिष्ट उपयोग के मामले में मदद की आवश्यकता है!