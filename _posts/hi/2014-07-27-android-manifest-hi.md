---
audio: false
generated: false
image: false
lang: hi
layout: post
title: AndroidManifest.xml फ़ाइल को समझना
translated: true
type: post
---

यदि आप एंड्रॉयड डेवलपमेंट में डाइविंग कर रहे हैं, तो आप सबसे पहले मिलने वाले फाइलों में से एक `AndroidManifest.xml` होगा। यह आपके ऐप का ब्लूप्रिंट है—यह एंड्रॉयड सिस्टम को आपके ऐप के बारे में सब कुछ बताता है, इससे पहले कि यह चलने लगे। आज हम एक ऐप "Flower" (पैकेज नाम: `com.lzw.flower`) से एक उदाहरण मैनिफेस्ट फाइल को डिसेक्ट करेंगे और इसके मुख्य घटकों, अवधारणाओं और पैटर्न को खोजेंगे।

---

#### AndroidManifest.xml क्या है?

`AndroidManifest.xml` फाइल हर एंड्रॉयड ऐप के लिए एक आवश्यक कॉन्फिगरेशन फाइल है। यह आपके प्रोजेक्ट के रूट डायरेक्टरी में रहता है और ऐप का पैकेज नाम, अनुमतियाँ, घटक (जैसे, गतिविधियाँ), और हार्डवेयर/सॉफ्टवेयर फीचर्स जैसे आवश्यक जानकारी घोषित करता है। इसे एंड्रॉयड ऑपरेटिंग सिस्टम द्वारा पढ़ा जाने वाला ऐप का आईडेंटिटी कार्ड मानें।

चलिए, हम उदाहरण को कदम दर कदम चलते हैं।

---

### मैनिफेस्ट का संरचना

यह हमारा मैनिफेस्ट है (पढ़ने के लिए थोड़ा सरल किया गया है):

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

अब, हम इसे अपने कोर सेक्शन में तोड़ते हैं और उनके पीछे की अवधारणाओं को समझाते हैं।

---

### 1. रूट `<manifest>` तत्व

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.lzw.flower"
    android:versionCode="8"
    android:versionName="1.5.2">
```

- **`xmlns:android`**: यह एंड्रॉयड-खास गुणों के लिए एक XML नामस्थान को परिभाषित करता है। यह हर मैनिफेस्ट में एक मानक बॉयलरप्लेट है।
- **`package`**: यह आपके ऐप का एकमात्र पहचानकर्ता है (जैसे, `com.lzw.flower`). यह भी आपके Java/Kotlin क्लासों के लिए डिफ़ॉल्ट नामस्थान है।
- **`android:versionCode`**: एक आंतरिक इंटीजर (यहाँ, `8`) जो अपडेट के साथ बढ़ता है।
- **`android:versionName`**: एक मानव-पठनीय संस्करण स्ट्रिंग (यहाँ, `1.5.2`) जो उपयोगकर्ताओं को दिखाया जाता है।

**अवधारणा**: `<manifest>` टैग ऐप का पहचान और संस्करण नियंत्रण सेट करता है, ताकि सिस्टम जान सके कि यह किस ऐप के साथ काम कर रहा है और कैसे अपडेट्स को संभालना है।

---

### 2. SDK संस्करण के साथ `<uses-sdk>`

```xml
<uses-sdk android:minSdkVersion="14" />
```

- **`android:minSdkVersion`**: यह ऐप का समर्थित न्यूनतम एंड्रॉयड एपीआई लेवल निर्दिष्ट करता है। एपीआई 14 एंड्रॉयड 4.0 (आईस क्रिम सैंडविच) के साथ मेल खाता है।

**अवधारणा**: यह संगतता सुनिश्चित करता है। इस ऐप को एंड्रॉयड 4.0 से नीचे चलने वाले डिवाइस पर इंस्टॉल नहीं किया जा सकता। यहाँ कोई `targetSdkVersion` या `maxSdkVersion` नहीं है, लेकिन उन्हें संगतता को और अधिक साफ करने के लिए जोड़ा जा सकता है।

---

### 3. अनुमतियों के साथ `<uses-permission>`

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

इस ऐप ने कई अनुमतियाँ मांगी हैं:
- `CAMERA`: डिवाइस के कैमरे तक पहुंचने के लिए।
- `WRITE_EXTERNAL_STORAGE`: फाइलें (जैसे, फोटो) बाहरी स्टोरेज में सेंड करने के लिए।
- `INTERNET`: नेटवर्क पहुंच के लिए।
- `ACCESS_NETWORK_STATE`: नेटवर्क कनेक्टिविटी की जांच करने के लिए।
- `READ_PHONE_STATE`: डिवाइस जानकारी (जैसे, आईएमईआई) तक पहुंचने के लिए।
- `ACCESS_WIFI_STATE`: वाई-फाई स्थिति की जांच करने के लिए।

**अवधारणा**: एंड्रॉयड एक अनुमति प्रणाली का उपयोग करता है ताकि उपयोगकर्ता की गोपनीयता और सुरक्षा को बचाया जा सके। ये घोषणाएं सिस्टम (और उपयोगकर्ता) को बताती हैं कि ऐप को कौन से संवेदनशील फीचर्स की आवश्यकता है। एंड्रॉयड 6.0 (एपीआई 23) के बाद, खतरनाक अनुमतियाँ (जैसे `CAMERA`) ऐप कोड में रनटाइम अनुरोधों की भी आवश्यकता होती हैं।

---

### 4. फीचर्स के साथ `<uses-feature>`

```xml
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```

- **`android.hardware.camera`**: यह ऐप के लिए एक कैमरा की आवश्यकता घोषित करता है।
- **`android.hardware.camera.autofocus`**: यह कैमरे में ऑटोफोकस की आवश्यकता को निर्दिष्ट करता है।

**अवधारणा**: अनुमतियों के विपरीत, `<uses-feature>` टैग ऐप को गूगल प्ले स्टोर पर फिल्टर करते हैं। यदि एक डिवाइस में कैमरा या ऑटोफोकस नहीं है, तो ऐप को इंस्टॉल करने योग्य नहीं दिखेगा, जब तक कि ये `android:required="false"` के साथ विकल्प के रूप में चिह्नित नहीं किए जाते।

---

### 5. `<application>` तत्व

```xml
<application
    android:label="@string/app_name"
    android:icon="@drawable/icon128"
    android:name=".base.App"
    android:theme="@style/AppTheme">
```

- **`android:label`**: ऐप का नाम, एक स्ट्रिंग रिसोर्स से निकाला गया (`@string/app_name`).
- **`android:icon`**: ऐप का आइकन, एक ड्रॉअबल रिसोर्स को संदर्भित करता है (`@drawable/icon128`).
- **`android:name`**: एक कस्टम एप्लिकेशन क्लास (`.base.App`), जो एंड्रॉयड के `Application` क्लास को ऐप-वाइड लॉजिक के लिए विस्तारित करता है।
- **`android:theme`**: ऐप का डिफ़ॉल्ट विजुअल थीम (`@style/AppTheme`).

**अवधारणा**: `<application>` टैग ऐप-वाइड सेटिंग्स को परिभाषित करता है। रिसोर्स जैसे `@string` और `@drawable` `res/` फोल्डरों में स्टोर किए जाते हैं, जिससे पुन: उपयोग और स्थानीकरण को बढ़ावा मिलता है।

---

### 6. गतिविधियों के साथ `<activity>`

मैनिफेस्ट में कई गतिविधियाँ सूचीबद्ध हैं, जो ऐप के यूआई स्क्रीन हैं:

#### उदाहरण 1: स्प्लैश स्क्रीन (लॉन्चर गतिविधि)
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

- **`android:name`**: क्लास नाम (`.base.SplashActivity`).
- **`intent-filter`**: इसे ऐप का प्रवेश द्वार (`MAIN` क्रिया + `LAUNCHER` श्रेणी) के रूप में चिह्नित करता है, ताकि यह डिवाइस के ऐप लॉन्चर में दिखाई दे।
- **`android:theme`**: एक पूर्ण स्क्रीन थीम बिना एक्शन बार के।

**पैटर्न**: लॉन्चर गतिविधि एक आम शुरुआत है, अक्सर एक स्प्लैश स्क्रीन या होम स्क्रीन होती है।

#### उदाहरण 2: कैमरा गतिविधि
```xml
<activity
    android:name=".deprecated.CameraActivity"
    android:screenOrientation="landscape">
```

- **`android:screenOrientation`**: लैंडस्केप मोड को मजबूर करता है।
- **`.deprecated`**: यह सुझाव देता है कि यह गतिविधि शायद पुरानी हो सकती है, लेकिन अभी भी शामिल है।

**पैटर्न**: गतिविधियाँ अक्सर विशेष उपयोग के लिए ओरिएंटेशन को ओवरराइड करती हैं (जैसे, कैमरा ऐप लैंडस्केप में बेहतर काम करते हैं).

#### अन्य गतिविधियाँ
मैनिफेस्ट में और गतिविधियाँ जैसे `DrawActivity`, `ResultActivity`, `PhotoActivity` आदि सूचीबद्ध हैं, जिनमें समान पैटर्न हैं:
- अधिकांश लैंडस्केप-ओरिएंटेड हैं, जो एक वीजुअल या मीडिया-फोकस्ड ऐप की ओर इशारा करते हैं।
- कुछ ऐप के डिफ़ॉल्ट थीम को ओवरराइड करते हैं (जैसे, `Theme.Holo.Light`).

**अवधारणा**: गतिविधियाँ एंड्रॉयड ऐप के यूआई के ब्लॉक हैं। प्रत्येक `<activity>` टैग एक स्क्रीन को सिस्टम के साथ पंजीकृत करता है।

---

### इस मैनिफेस्ट में मुख्य पैटर्न

1. **मीडिया-सेंटरेड डिजाइन**: कैमरा, स्टोरेज और ऑटोफोकस के लिए अनुमतियाँ और फीचर्स एक फोटो या ड्रॉइंग ऐप (शायद फूल पहचानने के लिए, पैकेज नाम `com.lzw.flower` के अनुसार) की ओर इशारा करते हैं।
2. **ओरिएंटेशन नियंत्रण**: `android:screenOrientation="landscape"` का भारी उपयोग वीजुअल टास्क पर ध्यान केंद्रित करता है।
3. **मॉड्यूलर गतिविधियाँ**: कई गतिविधियाँ (`CameraActivity`, `DrawActivity`, `ResultActivity`) एक बहु-चरण कार्यप्रणाली की ओर इशारा करती हैं।
4. **रिसोर्स उपयोग**: `@string`, `@drawable`, और `@style` के संदर्भ एक साफ, रखरखाव योग्य संरचना दिखाते हैं।

---

### निष्कर्ष

`AndroidManifest.xml` केवल एक कॉन्फिगरेशन फाइल से अधिक है—यह एक ऐप के उद्देश्य और व्यवहार के बारे में एक खिड़की है। इस मामले में, "Flower" शायद एक मीडिया ऐप है, जिसमें कैमरा कार्यक्षमता, ड्रॉइंग फीचर्स और नेटवर्क क्षमता शामिल हैं, शायद छवियों को अपलोड या प्रोसेस करने के लिए। इसके घटकों—अनुमतियाँ, फीचर्स और गतिविधियाँ—को समझकर, आप देख सकते हैं कि एंड्रॉयड ऐप कैसे संरचित हैं और अपने खुद के डिजाइन कैसे करें।

किसी समान चीज बनाना चाहते हैं? एक स्पष्ट उद्देश्य (जैसे फूल पहचान) से शुरू करें, अपने अनुमतियाँ और फीचर्स को परिभाषित करें, और अपने गतिविधियों का नक्शा बनाएं। मैनिफेस्ट सबको एक साथ बांधेगा!