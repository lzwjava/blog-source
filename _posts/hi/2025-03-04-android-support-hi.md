---
audio: false
generated: true
lang: hi
layout: post
title: एंड्रॉइड सपोर्ट लाइब्रेरी
translated: true
type: note
---

Android सपोर्ट लाइब्रेरी का संस्करण `support-v4:19.1.0`, Android सपोर्ट लाइब्रेरी (विशेष रूप से v4 कम्पैटिबिलिटी लाइब्रेरी) का एक पुराना संस्करण है, जो उसके रिलीज़ के समय (लगभग 2014) की नवीनतम API लेवल से निचले स्तर पर चलने वाले Android डिवाइसों के लिए बैकवर्ड-कम्पैटिबल API प्रदान करता है। यह लाइब्रेरी आपको पुराने डिवाइसों पर नए Android संस्करणों में पेश की गई सुविधाओं, जैसे कि Fragments, Loaders और अन्य यूटिलिटीज़ का उपयोग करने की अनुमति देती है।

चूंकि `support-v4:19.1.0` लीगेसी Android सपोर्ट लाइब्रेरी का हिस्सा है, इसे AndroidX लाइब्रेरीज़ द्वारा प्रतिस्थापित कर दिया गया है। हालाँकि, यदि आपको इस विशिष्ट संस्करण का उपयोग करने की आवश्यकता है (उदाहरण के लिए, किसी पुरानी प्रोजेक्ट को मेंटेन करने के लिए), यहां बताया गया है कि आप इसे अपने Android प्रोजेक्ट में कैसे सेट अप और उपयोग कर सकते हैं:

---

### चरण 1: डिपेंडेंसी जोड़ें
`support-v4:19.1.0` का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में एक डिपेंडेंसी के रूप में शामिल करना होगा। यह आमतौर पर आपकी `build.gradle` फ़ाइल (Module: app) में किया जाता है।

#### Gradle-आधारित प्रोजेक्ट्स के लिए
1. अपनी `app/build.gradle` फ़ाइल खोलें।
2. `dependencies` ब्लॉक में निम्न पंक्ति जोड़ें:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Android Studio में "Sync Now" पर क्लिक करके अपने प्रोजेक्ट को Gradle के साथ सिंक करें।

#### नोट्स:
- सुनिश्चित करें कि आपका `compileSdkVersion` कम से कम 19 (Android 4.4 KitKat) या उससे अधिक पर सेट है, क्योंकि यह लाइब्रेरी API 19 फीचर्स के साथ संरेखित है।
- `support-v4:19.1.0` द्वारा समर्थित न्यूनतम SDK संस्करण API 4 (Android 1.6) है, लेकिन आपको अपना `minSdkVersion` अपने ऐप की आवश्यकताओं के आधार पर सेट करना चाहिए।

`build.gradle` उदाहरण:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // आवश्यकतानुसार समायोजित करें
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### चरण 2: उपलब्धता सत्यापित करें
Android सपोर्ट लाइब्रेरीज़ Google के Maven रिपॉजिटरी में होस्ट की जाती हैं। Android Studio 3.0+ से शुरू करके, यह रिपॉजिटरी डिफ़ॉल्ट रूप से शामिल होती है। यदि आप Android Studio के पुराने संस्करण का उपयोग कर रहे हैं, तो सुनिश्चित करें कि निम्नलिखित आपके `build.gradle` (प्रोजेक्ट-लेवल) में मौजूद है:

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // नोट: JCenter deprecated है, लेकिन पुरानी लाइब्रेरीज़ के लिए उपयोग किया जाता था
    }
}
```

यदि आपको लाइब्रेरी डाउनलोड करने में समस्या हो रही है, तो आपको SDK मैनेजर के माध्यम से Android सपोर्ट रिपॉजिटरी इंस्टॉल करने की आवश्यकता हो सकती है:
1. `Tools > SDK Manager` पर जाएं।
2. "SDK Tools" टैब के अंतर्गत, "Android Support Repository" चेक करें और इसे इंस्टॉल करें।

---

### चरण 3: अपने कोड में लाइब्रेरी का उपयोग करना
`support-v4` लाइब्रेरी विभिन्न प्रकार की कक्षाएं प्रदान करती है, जैसे कि `Fragment`, `Loader`, `AsyncTaskLoader`, और `ActivityCompat` जैसी यूटिलिटीज़। नीचे कुछ सामान्य कंपोनेंट्स के उपयोग के उदाहरण दिए गए हैं:

#### उदाहरण 1: Fragments का उपयोग करना
`support-v4` लाइब्रेरी में एक बैकपोर्टेड `Fragment` क्लास शामिल है जो पुराने Android संस्करणों पर काम करती है।

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

इस फ्रैगमेंट को एक एक्टिविटी में उपयोग करने के लिए:
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

#### उदाहरण 2: ActivityCompat का उपयोग करना
`ActivityCompat` क्लास बैकवर्ड-कम्पैटिबल फीचर्स के लिए हेल्पर मेथड प्रदान करती है, जैसे कि अनुमतियाँ मांगना (जो API 23 में पेश की गई थीं लेकिन सपोर्ट लाइब्रेरी के साथ पहले भी उपयोग की जा सकती हैं)।

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

### चरण 4: विचारणीय बातें
- **Deprecated लाइब्रेरी**: Android सपोर्ट लाइब्रेरी, जिसमें `support-v4:19.1.0` शामिल है, deprecated है। आधुनिक डेवलपमेंट के लिए, AndroidX (उदाहरण के लिए, `androidx.legacy:legacy-support-v4:1.0.0`) में माइग्रेट करें। AndroidX उत्तराधिकारी है और निरंतर अपडेट और सपोर्ट प्रदान करता है।
- **संस्करण मिलान**: यदि आप अन्य सपोर्ट लाइब्रेरीज़ (जैसे `appcompat-v7`) का उपयोग करते हैं, तो सुनिश्चित करें कि वे समान संस्करण (19.1.0) की हैं ताकि संस्करण मिसमैच एरर से बचा जा सके।
- **न्यूनतम SDK**: जबकि `support-v4:19.1.0` API 4+ को सपोर्ट करती है, कुछ फीचर्स के लिए उच्च `minSdkVersion` (जैसे कि बाद में पेश किए गए कुछ कंपोनेंट्स के लिए API 14) की आवश्यकता हो सकती है।

---

### चरण 5: AndroidX में माइग्रेट करना (वैकल्पिक लेकिन अनुशंसित)
यदि आप कोई पुरानी प्रोजेक्ट मेंटेन कर रहे हैं, तो AndroidX में माइग्रेट करने पर विचार करें:
1. Android Studio में, `Refactor > Migrate to AndroidX` पर जाएं।
2. अपनी डिपेंडेंसीज़ को अपडेट करें, उदाहरण के लिए, `com.android.support:support-v4:19.1.0` को `androidx.legacy:legacy-support-v4:1.0.0` से बदलें।
3. Android Studio द्वारा प्रदान किए गए माइग्रेशन गाइड का पालन करें।

---

### समस्या निवारण
- **"Could not find library"**: सुनिश्चित करें कि आपका इंटरनेट कनेक्शन सक्रिय है और Google Maven रिपॉजिटरी एक्सेसिबल है।
- **संस्करण मिसमैच**: यदि आपको मिसमैच सपोर्ट लाइब्रेरी संस्करण के बारे में एरर दिखाई देते हैं, तो सभी `com.android.support` डिपेंडेंसीज़ को 19.1.0 पर संरेखित करें।
- **अप्रचलित फीचर्स**: `support-v4:19.1.0` में कुछ APIs (जैसे `AsyncTask`) अप्रचलित हैं। विकल्पों के लिए डॉक्यूमेंटेशन चेक करें।

मुझे बताएं यदि आपको किसी विशिष्ट उपयोग के मामले या सेटअप में मदद की आवश्यकता है!