---
audio: false
generated: true
lang: hi
layout: post
title: RocksDB के लिए Java API
translated: true
---

`org.rocksdb` लाइब्रेरी का उपयोग करने के लिए, जो RocksDB का Java API है—एक उच्च-प्रदर्शन एम्बेडेड डेटाबेस है जो की-वैल्यू डेटा के लिए ऑप्टिमाइज्ड है—आपको निम्नलिखित चरणों का पालन करना होगा। RocksDB तेज़ स्टोरेज और रिट्रीवल के लिए ऑप्टिमाइज्ड है, जिससे यह उन एप्लिकेशन के लिए आदर्श है जो जाने-माने कीज़ के माध्यम से तेज़ डेटा एक्सेस की आवश्यकता होती है। नीचे एक व्यापक गाइड है जो आपको शुरू करने में मदद करेगा:

---

### 1. **डिपेंडेंसी जोड़ें**
`org.rocksdb` को अपने Java प्रोजेक्ट में उपयोग करने के लिए, आपको RocksDB JNI (Java Native Interface) डिपेंडेंसी को शामिल करना होगा। अगर आप Maven का उपयोग कर रहे हैं, तो इसे अपने `pom.xml` फ़ाइल में जोड़ें:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

Gradle के लिए, इसे अपने `build.gradle` में जोड़ें:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**नोट**: [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) पर नवीनतम संस्करण की जांच करें, क्योंकि `7.10.2` वर्तमान नहीं हो सकता।

---

### 2. **नेटिव लाइब्रेरी लोड करें**
RocksDB नेटिव C++ कोड पर निर्भर करता है, इसलिए आप इसे उपयोग करने से पहले नेटिव लाइब्रेरी को लोड करना होगा। अपने कोड की शुरुआत में इस लाइन को जोड़ें:

```java
RocksDB.loadLibrary();
```

इससे न करने से रनटाइम त्रुटियाँ हो सकती हैं।

---

### 3. **डेटाबेस खोलें**
RocksDB का उपयोग शुरू करने के लिए, आपको डेटाबेस इंस्टेंस को खोलने के लिए एक फ़ाइल पथ पर निर्दिष्ट करना होगा जहां डेटाबेस स्टोर होगा। `Options` क्लास का उपयोग करके सेटिंग्स को कॉन्फ़िगर करें, जैसे कि डेटाबेस को बनाना अगर यह मौजूद नहीं है:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/path/to/db");
```

- **`options`**: डेटाबेस व्यवहार को कॉन्फ़िगर करता है (जैसे, `setCreateIfMissing(true)` डेटाबेस को बनाता है अगर यह मौजूद नहीं है).
- **`/path/to/db`**: इसे अपने सिस्टम पर एक वैध डायरेक्टरी पथ से बदलें जहां डेटाबेस फ़ाइलें रहेंगी।

---

### 4. **बेसिक ऑपरेशन करें**
RocksDB एक की-वैल्यू स्टोर है, और इसके कोर ऑपरेशन `put`, `get`, और `delete` हैं। कीज़ और वैल्यूज़ को बाइट एरेयज़ के रूप में स्टोर किया जाता है, इसलिए आपको डेटा (जैसे, स्ट्रिंग्स) को बाइट्स में बदलना होगा।

- **Put**: एक की-वैल्यू पेर को इंसर्ट या अपडेट करें।
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: एक की से संबद्ध वैल्यू को रिट्रीव करें।
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // "value" प्रिंट करता है
  } else {
      System.out.println("की नहीं मिला");
  }
  ```

- **Delete**: एक की-वैल्यू पेर को हटाएं।
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **डेटाबेस बंद करें**
डेटाबेस को सही तरह से बंद करना संसाधनों को मुक्त करने के लिए आवश्यक है। सबसे आसान तरीका है एक try-with-resources ब्लॉक का उपयोग करना, जो जब आप खत्म हो जाते हैं तो स्वचालित रूप से डेटाबेस को बंद करता है:

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // यहाँ ऑपरेशन करें
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **एक्सेप्शंस को संभालें**
RocksDB ऑपरेशन `RocksDBException` फेंक सकते हैं, इसलिए हमेशा संसाधनों के लीक या डेटा कोरप्शन को रोकने के लिए एक्सेप्शन हैंडलिंग शामिल करें:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **कॉन्फ़िगरेशन ऑप्शंस**
आप `Options` क्लास का उपयोग करके RocksDB की प्रदर्शन को फाइन-ट्यून कर सकते हैं। उदाहरण के लिए:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // 64MB लिखने की बफर
```

सामान्य ऑप्शंस में शामिल हैं:
- `setWriteBufferSize`: लिखने के लिए उपयोग की जाने वाली मेमोरी को नियंत्रित करता है।
- `setMaxOpenFiles`: खुले फ़ाइलों की संख्या को सीमित करता है।
- `setCompactionStyle`: डिस्क पर डेटा को कैसे कॉम्पैक्ट किया जाता है, इसे सेट करता है।

[RocksDB दस्तावेज़](https://github.com/facebook/rocksdb/wiki) पर और अधिक ऑप्शंस की खोज करें।

---

### 8. **सादा उदाहरण**
यह एक पूर्ण उदाहरण है जो डेटाबेस को खोलने, एक की-वैल्यू पेर को स्टोर करने और इसे रिट्रीव करने का प्रदर्शन करता है:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // नेटिव लाइब्रेरी लोड करें
        Options options = new Options().setCreateIfMissing(true);

        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // एक की-वैल्यू पेर को डालें
            db.put("hello".getBytes(), "world".getBytes());

            // वैल्यू को प्राप्त करें
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // "world" प्रिंट करता है
            } else {
                System.out.println("की नहीं मिला");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**आउटपुट**: `world`

---

### मुख्य विचार
- **एम्बेडेड प्रकृति**: RocksDB अपने एप्लिकेशन के प्रोसेस के भीतर चलता है, एक अलग सर्वर के रूप में नहीं।
- **बाइट एरेयज़**: कीज़ और वैल्यूज़ `byte[]` हैं, इसलिए आपको जटिल ऑब्जेक्ट के लिए सीरियलाइज़ेशन/डिसीरियलाइज़ेशन को संभालना होगा।
- **प्रदर्शन**: RocksDB तेज़ स्टोरेज (जैसे, एसएसडी) के साथ उत्कृष्ट प्रदर्शन करता है और इसे उच्च-प्रदर्शन सिस्टम जैसे Facebook में उपयोग किया जाता है, जहां इसे विकसित किया गया था।
- **नहीं रिलेशनल**: यह एक की-वैल्यू स्टोर है, नहीं एक रिलेशनल डेटाबेस—कोई SQL या जोइन्स नहीं।

---

### आम गलतियाँ
- **`RocksDB.loadLibrary()` को भूल जाना**: `UnsatisfiedLinkError` के कारण होता है।
- **अनुपयुक्त संसाधन प्रबंधन**: डेटाबेस को बंद नहीं करना, विशेष रूप से संसाधन-सीमित सिस्टम पर, समस्याएं पैदा कर सकता है।
- **डेटा प्रकार गलतियाँ**: स्ट्रिंग्स या ऑब्जेक्ट्स को सीधे पास करने के बजाय `byte[]` में बदलने से।

---

### आगे बढ़ना
- **उन्नत विशेषताएं**: ट्रांजैक्शंस, स्नैपशॉट्स, या कॉलम फैमिलीज जैसे जटिल उपयोग के लिए खोजें।
- **संसाधन**: [RocksDB Java API](https://github.com/facebook/rocksdb/tree/main/java) और [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) पर विस्तृत दस्तावेज़ और उदाहरण के लिए जांच करें।

यह गाइड `org.rocksdb` का उपयोग करने के लिए एक मजबूत आधार प्रदान करता है। अगर आपको किसी विशेष विशेषता या उपयोग के मामले में मदद चाहिए, तो स्वतंत्र रूप से पूछें!