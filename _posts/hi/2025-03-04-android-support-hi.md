---
audio: false
generated: true
lang: hi
layout: post
title: Android सहायता पुस्तकालय
translated: true
---

Android Support Library का संस्करण `support-v4:19.1.0` एक पुराना संस्करण है (विशेष रूप से v4 compatibility library), जो Android devices पर API levels के लिए backward-compatible APIs प्रदान करता है जो उस समय के नवीनतम ones से कम हैं (लगभग 2014). यह लाइब्रेरी आपको नए Android versions में परिचित किए गए features, जैसे कि Fragments, Loaders, और अन्य utilities, को पुराने devices पर उपयोग करने की अनुमति देता है।

`support-v4:19.1.0` legacy Android Support Library का हिस्सा है, इसलिए इसे AndroidX libraries द्वारा superseded किया गया है। फिर भी, अगर आपको इस विशेष संस्करण का उपयोग करना है (उदाहरण के लिए, एक पुराने project को maintain करने के लिए), तो यहाँ यह कैसे setup और use किया जा सकता है:

---

### Step 1: Add the Dependency
`support-v4:19.1.0` का उपयोग करने के लिए, आपको इसे project में एक dependency के रूप में include करना होगा। यह आमतौर पर `build.gradle` file (Module: app) में किया जाता है।

#### For Gradle-Based Projects
1. `app/build.gradle` file खोलें।
2. `dependencies` block में निम्नलिखित line add करें:

```gradle
dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

3. Android Studio में "Sync Now" पर क्लिक करके project को Gradle के साथ sync करें।

#### Notes:
- `compileSdkVersion` को कम से कम 19 (Android 4.4 KitKat) या उससे अधिक set करें, क्योंकि यह library API 19 features के साथ align है।
- `support-v4:19.1.0` द्वारा supported minimum SDK version API 4 (Android 1.6) है, लेकिन आप `minSdkVersion` को अपने app के requirements के आधार पर set करें।

Example `build.gradle`:
```gradle
android {
    compileSdkVersion 19
    defaultConfig {
        minSdkVersion 14  // आवश्यकता के अनुसार adjust करें
        targetSdkVersion 19
    }
}

dependencies {
    implementation 'com.android.support:support-v4:19.1.0'
}
```

---

### Step 2: Verify Availability
Android Support Libraries Google's Maven repository में hosted हैं। Android Studio 3.0+ से, यह repository default में included है। अगर आप एक पुराने version of Android Studio का उपयोग कर रहे हैं, तो ensure करें कि निम्नलिखित `build.gradle` (Project-level) में है:

```gradle
allprojects {
    repositories {
        google()
        jcenter()  // Note: JCenter is deprecated, but was used for older libraries
    }
}
```

अगर आपको library download करने में समस्या आती है, तो आपको Android Support Repository को SDK Manager के माध्यम से install करना पड़ेगा:
1. `Tools > SDK Manager` जाएँ।
2. "SDK Tools" tab के नीचे, "Android Support Repository" पर check करें और install करें।

---

### Step 3: Using the Library in Your Code
`support-v4` library में `Fragment`, `Loader`, `AsyncTaskLoader`, और utilities जैसे `ActivityCompat` जैसे विभिन्न classes शामिल हैं। नीचे कुछ common components का उपयोग करने के उदाहरण दिए गए हैं:

#### Example 1: Using Fragments
`support-v4` library में एक backported `Fragment` class शामिल है जो पुराने Android versions पर काम करता है।

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

इस fragment को एक activity में use करने के लिए:
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

#### Example 2: Using ActivityCompat
`ActivityCompat` class backward-compatible features के लिए helper methods प्रदान करता है, जैसे कि permissions request (API 23 में परिचित, लेकिन support library के साथ पहले versions में usable).

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

### Step 4: Considerations
- **Deprecated Library**: Android Support Library, जिसमें `support-v4:19.1.0` शामिल है, deprecated है। modern development के लिए, AndroidX (e.g., `androidx.legacy:legacy-support-v4:1.0.0`) पर migrate करें। AndroidX successor है और ongoing updates और support प्रदान करता है.
- **Version Matching**: अगर आप अन्य support libraries (e.g., `appcompat-v7`) का उपयोग करते हैं, तो ensure करें कि वे same version (19.1.0) पर हैं version mismatch errors से बचने के लिए.
- **Minimum SDK**: `support-v4:19.1.0` API 4+ को support करता है, लेकिन कुछ features को एक higher `minSdkVersion` (e.g., API 14 for certain components introduced later) की आवश्यकता हो सकती है.

---

### Step 5: Migrating to AndroidX (Optional but Recommended)
अगर आप एक old project maintain कर रहे हैं, तो AndroidX पर migrate करने की सोचें:
1. Android Studio में, `Refactor > Migrate to AndroidX` जाएँ.
2. dependencies update करें, उदाहरण के लिए, `com.android.support:support-v4:19.1.0` को `androidx.legacy:legacy-support-v4:1.0.0` से replace करें.
3. Android Studio द्वारा provided migration guide का पालन करें.

---

### Troubleshooting
- **"Could not find library"**: ensure करें कि आपका internet connection active है और Google Maven repository accessible है.
- **Version Mismatch**: अगर आप support library versions के mismatched errors देखते हैं, तो सभी `com.android.support` dependencies को 19.1.0 पर align करें.
- **Obsolete Features**: `support-v4:19.1.0` में कुछ APIs (e.g., `AsyncTask`) outdated हैं। documentation के लिए alternatives check करें.

मुझे एक specific use case या setup के साथ मदद चाहिए, तो मुझे बताएं!