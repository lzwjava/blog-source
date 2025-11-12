---
audio: false
generated: true
lang: hi
layout: post
title: गूगल क्लाउड जावा क्लाएंट
translated: true
type: note
---

### मुख्य बिंदु
- ऐसा प्रतीत होता है कि Java में `com.google.cloud` का उपयोग करने के लिए, आपको एक Java डेवलपमेंट एनवायरनमेंट सेट अप करना होगा, Google Cloud क्लाइंट लाइब्रेरी डिपेंडेंसीज़ शामिल करनी होंगी, ऑथेंटिकेशन कॉन्फ़िगर करना होगा, और Google Cloud सेवाओं के साथ इंटरैक्ट करने के लिए लाइब्रेरीज़ का उपयोग करना होगा।
- शोध से पता चलता है कि ऑथेंटिकेशन Google Cloud प्लेटफ़ॉर्म पर स्वचालित रूप से संभाला जा सकता है या सर्विस अकाउंट क्रेडेंशियल्स का उपयोग करके लोकल डेवलपमेंट के लिए मैन्युअल रूप से सेट अप किया जा सकता है।
- साक्ष्य Cloud Storage को एक सामान्य उपयोग के मामले के रूप में प्रदर्शित करते हुए, डिपेंडेंसीज़ प्रबंधित करने के लिए Maven या Gradle के उपयोग की ओर इशारा करते हैं।

### अपना डेवलपमेंट एनवायरनमेंट सेट अप करना
शुरुआत करने के लिए, सुनिश्चित करें कि आपके पास Java डेवलपमेंट किट (JDK) वर्ज़न 8 या उससे ऊपर इंस्टॉल है, साथ ही Maven या Gradle जैसा बिल्ड टूल भी है। ये टूल आपकी प्रोजेक्ट डिपेंडेंसीज़ और बिल्ड प्रक्रियाओं को प्रबंधित करने में मदद करते हैं।

### डिपेंडेंसीज़ शामिल करना
अपनी प्रोजेक्ट में Google Cloud क्लाइंट लाइब्रेरी डिपेंडेंसीज़ जोड़ें। Maven के लिए, Bill of Materials (BOM) और विशिष्ट सर्विस लाइब्रेरीज़ को अपनी `pom.xml` फ़ाइल में शामिल करें। उदाहरण के लिए, Cloud Storage का उपयोग करने के लिए:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

"latest_version" को [Google Cloud Java क्लाइंट लाइब्रेरीज़ GitHub रिपॉजिटरी](https://github.com/googleapis/google-cloud-java) से वास्तविक वर्ज़न से बदलें।

### ऑथेंटिकेशन कॉन्फ़िगर करना
ऑथेंटिकेशन अक्सर स्वचालित रूप से संभाला जाता है यदि आपका एप्लिकेशन Google Cloud प्लेटफ़ॉर्म जैसे Compute Engine या App Engine पर चलता है। लोकल डेवलपमेंट के लिए, `GOOGLE_APPLICATION_CREDENTIALS` एनवायरनमेंट वेरिएबल को एक सर्विस अकाउंट की JSON key फ़ाइल की ओर इंगित करने के लिए सेट करें, या इसे प्रोग्रामेटिक रूप से कॉन्फ़िगर करें।

### लाइब्रेरीज़ का उपयोग करना
एक बार सेट अप हो जाने के बाद, आवश्यक क्लासेज़ को इम्पोर्ट करें, एक सर्विस ऑब्जेक्ट बनाएं, और API कॉल करें। उदाहरण के लिए, Cloud Storage में बकेट्स की सूची बनाने के लिए:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

एक अप्रत्याशित विवरण यह है कि लाइब्रेरीज़ विभिन्न Google Cloud सेवाओं का समर्थन करती हैं, जिनमें से प्रत्येक का अपना सबपैकेज `com.google.cloud` के अंतर्गत होता है, जैसे कि BigQuery के लिए `com.google.cloud.bigquery`, जो स्टोरेज से परे व्यापक कार्यक्षमता प्रदान करता है।

---

### सर्वे नोट: Java में `com.google.cloud` का उपयोग करने पर व्यापक गाइड

यह नोट Google Cloud Java क्लाइंट लाइब्रेरीज़ का उपयोग करने, विशेष रूप से `com.google.cloud` पैकेज पर ध्यान केंद्रित करते हुए, Google Cloud सेवाओं के साथ इंटरैक्ट करने का एक विस्तृत अन्वेषण प्रदान करता है। यह सीधे उत्तर का विस्तार करते हुए, शोध से प्राप्त सभी प्रासंगिक विवरणों को शामिल करता है, जो स्पष्टता और गहराई के लिए व्यवस्थित है, और डेवलपर्स के लिए उपयुक्त है जो पूर्ण समझ चाहते हैं।

#### Google Cloud Java क्लाइंट लाइब्रेरीज़ का परिचय
Google Cloud Java क्लाइंट लाइब्रेरीज़, जो `com.google.cloud` पैकेज के अंतर्गत सुलभ हैं, Cloud Storage, BigQuery, और Compute Engine जैसी Google Cloud सेवाओं के साथ इंटरैक्ट करने के लिए स्वाभाविक और सहज इंटरफेस प्रदान करती हैं। ये लाइब्रेरीज़ बॉयलरप्लेट कोड को कम करने, लो-लेवल कम्युनिकेशन विवरणों को संभालने और Java डेवलपमेंट प्रथाओं के साथ सहजता से एकीकृत होने के लिए डिज़ाइन की गई हैं। ये क्लाउड-नेटिव एप्लिकेशन बनाने, Spring, Maven, और Kubernetes जैसे टूल्स का लाभ उठाने के लिए विशेष रूप से उपयोगी हैं, जैसा कि आधिकारिक डॉक्यूमेंटेशन में हाइलाइट किया गया है।

#### डेवलपमेंट एनवायरनमेंट सेट अप करना
शुरुआत करने के लिए, Java डेवलपमेंट किट (JDK) वर्ज़न 8 या उससे ऊपर की आवश्यकता होती है, जो लाइब्रेरीज़ के साथ संगतता सुनिश्चित करता है। अनुशंसित डिस्ट्रीब्यूशन Eclipse Temurin है, जो एक ओपन-सोर्स, Java SE TCK-प्रमाणित विकल्प है, जैसा कि सेटअप गाइड में नोट किया गया है। इसके अतिरिक्त, डिपेंडेंसीज़ प्रबंधित करने के लिए Maven या Gradle जैसा बिल्ड ऑटोमेशन टूल आवश्यक है। Google Cloud CLI (`gcloud`) भी इंस्टॉल किया जा सकता है ताकि कमांड लाइन से संसाधनों के साथ इंटरैक्ट किया जा सके, जिससे डिप्लॉयमेंट और मॉनिटरिंग कार्यों में सुविधा होती है।

#### डिपेंडेंसीज़ प्रबंधित करना
डिपेंडेंसी प्रबंधन Google Cloud द्वारा प्रदान की गई Bill of Materials (BOM) का उपयोग करके सुव्यवस्थित है, जो कई लाइब्रेरीज़ में वर्ज़न प्रबंधित करने में मदद करती है। Maven के लिए, अपनी `pom.xml` में निम्नलिखित जोड़ें:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Gradle के लिए, समान कॉन्फ़िगरेशन लागू होते हैं, जो वर्ज़न स्थिरता सुनिश्चित करते हैं। वर्ज़न नंबर को नवीनतम अपडेट के लिए [Google Cloud Java क्लाइंट लाइब्रेरीज़ GitHub रिपॉजिटरी](https://github.com/googleapis/google-cloud-java) के विरुद्ध जाँचा जाना चाहिए। यह रिपॉजिटरी समर्थित प्लेटफ़ॉर्म के विवरण भी प्रदान करती है, जिसमें x86_64, Mac OS X, Windows, और Linux शामिल हैं, लेकिन Android और Raspberry Pi पर सीमाओं को नोट करती है।

#### ऑथेंटिकेशन मैकेनिज़्म
ऑथेंटिकेशन एक महत्वपूर्ण कदम है, जिसके विकल्प पर्यावरण के अनुसार भिन्न होते हैं। Google Cloud प्लेटफ़ॉर्म जैसे Compute Engine, Kubernetes Engine, या App Engine पर, क्रेडेंशियल्स स्वचालित रूप से अनुमानित होते हैं, जिससे प्रक्रिया सरल हो जाती है। अन्य वातावरणों के लिए, जैसे कि लोकल डेवलपमेंट, निम्नलिखित विधियाँ उपलब्ध हैं:

- **सर्विस अकाउंट (अनुशंसित):** Google Cloud Console से एक JSON key फ़ाइल जनरेट करें और `GOOGLE_APPLICATION_CREDENTIALS` एनवायरनमेंट वेरिएबल को इसके पथ पर सेट करें। वैकल्पिक रूप से, इसे प्रोग्रामेटिक रूप से लोड करें:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **लोकल डेवलपमेंट/टेस्टिंग:** अस्थायी क्रेडेंशियल्स के लिए Google Cloud SDK के साथ `gcloud auth application-default login` का उपयोग करें।
- **मौजूदा OAuth2 टोकन:** विशिष्ट उपयोग के मामलों के लिए `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` का उपयोग करें।

प्रोजेक्ट ID निर्दिष्ट करने के लिए प्राथमिकता का क्रम इसमें शामिल है: सर्विस विकल्प, एनवायरनमेंट वेरिएबल `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, JSON क्रेडेंशियल फ़ाइल, और Google Cloud SDK, जिसमें `ServiceOptions.getDefaultProjectId()` प्रोजेक्ट ID को अनुमान लगाने में मदद करता है।

#### क्लाइंट लाइब्रेरीज़ का उपयोग करना
एक बार डिपेंडेंसीज़ और ऑथेंटिकेशन सेट हो जाने के बाद, डेवलपर्स Google Cloud सेवाओं के साथ इंटरैक्ट करने के लिए लाइब्रेरीज़ का उपयोग कर सकते हैं। प्रत्येक सर्विस का अपना सबपैकेज `com.google.cloud` के अंतर्गत होता है, जैसे कि Cloud Storage के लिए `com.google.cloud.storage` या BigQuery के लिए `com.google.cloud.bigquery`। यहाँ Cloud Storage के लिए एक विस्तृत उदाहरण दिया गया है:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

यह उदाहरण सभी बकेट्स की सूची बनाता है, लेकिन लाइब्रेरी ऑपरेशंस जैसे ऑब्जेक्ट अपलोड करना, फ़ाइलें डाउनलोड करना, और बकेट पॉलिसी प्रबंधित करने का समर्थन करती है। अन्य सेवाओं के लिए, समान पैटर्न लागू होते हैं, जिनके विस्तृत तरीके संबंधित javadocs में उपलब्ध हैं, जैसे कि BigQuery के लिए [Google Cloud Java रेफरेंस डॉक्स](https://googleapis.dev/java/google-cloud-clients/latest/) पर।

#### उन्नत सुविधाएँ और विचार
लाइब्रेरीज़ उन्नत सुविधाओं का समर्थन करती हैं जैसे लॉन्ग-रनिंग ऑपरेशंस (LROs) `OperationFuture` का उपयोग करके, जिसमें कॉन्फ़िगर करने योग्य टाइमआउट और रिट्री पॉलिसीज़ शामिल हैं। उदाहरण के लिए, AI Platform (v3.24.0) के डिफ़ॉल्ट में 5000ms की प्रारंभिक रिट्री देरी, 1.5 का मल्टीप्लायर, 45000ms का अधिकतम रिट्री देरी, और 300000ms का कुल टाइमआउट शामिल है। प्रॉक्सी कॉन्फ़िगरेशन भी समर्थित है, जो HTTPS/gRPC के लिए `https.proxyHost` और `https.proxyPort` का उपयोग करता है, जिसमें gRPC के लिए कस्टम विकल्प `ProxyDetector` के माध्यम से उपलब्ध हैं।

API key ऑथेंटिकेशन कुछ APIs के लिए उपलब्ध है, जिसे gRPC या REST के लिए हेडर्स के माध्यम से मैन्युअल रूप से सेट किया जाता है, जैसा कि Language service के उदाहरणों में दिखाया गया है। टेस्टिंग प्रदान किए गए टूल्स के साथ सुगम है, जिसका विवरण रिपॉजिटरी के TESTING.md में है, और IntelliJ और Eclipse के लिए IDE प्लगइन लाइब्रेरी एकीकरण के साथ डेवलपमेंट को बढ़ाते हैं।

#### समर्थित प्लेटफ़ॉर्म और सीमाएँ
लाइब्रेरीज़ विभिन्न प्लेटफ़ॉर्म के साथ संगत हैं, जिसमें HTTP क्लाइंट हर जगह काम करते हैं और gRPC क्लाइंट x86_64, Mac OS X, Windows, और Linux पर समर्थित हैं। हालाँकि, वे Android, Raspberry Pi, या App Engine Standard Java 7 पर समर्थित नहीं हैं, सिवाय Datastore, Storage, और BigQuery के। समर्थित वातावरणों में Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex, और Alpine Linux (Java 11+) शामिल हैं।

#### संसाधन और आगे पढ़ना
अतिरिक्त मार्गदर्शन के लिए, [Google Cloud Java क्लाइंट लाइब्रेरीज़ GitHub रिपॉजिटरी](https://github.com/googleapis/google-cloud-java) कोड सैंपल, योगदान दिशानिर्देश, और समस्या निवारण संसाधन प्रदान करती है। [Baeldung](https://www.baeldung.com/java-google-cloud-storage) जैसे ट्यूटोरियल व्यावहारिक उदाहरण प्रदान करते हैं, जैसे कि Cloud Storage का उपयोग करना, जबकि [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) पर आधिकारिक डॉक्यूमेंटेशन व्यापक ऐप डेवलपमेंट अवधारणाओं को कवर करता है।

#### तालिका: मुख्य कॉन्फ़िगरेशन विवरण

| **पहलू**               | **विवरण**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java वर्ज़न             | Java 8 या उससे ऊपर की आवश्यकता है।                                                                       |
| डिपेंडेंसी प्रबंधन    | वर्ज़न स्थिरता के लिए BOM का उपयोग करें, उदा. Maven `libraries-bom`।                                  |
| ऑथेंटिकेशन विधियाँ   | GCE/GKE/GAE पर स्वचालित, `GOOGLE_APPLICATION_CREDENTIALS` के माध्यम से या प्रोग्रामेटिक रूप से मैन्युअल।          |
| समर्थित प्लेटफ़ॉर्म      | HTTP क्लाइंट हर जगह, gRPC x86_64, Mac OS X, Windows, Linux पर; Android, Raspberry Pi पर नहीं।|
| उदाहरण सेवा          | Cloud Storage: `com.google.cloud.storage`, बकेट लिस्टिंग, ऑब्जेक्ट प्रबंधन के तरीके।       |

यह व्यापक गाइड यह सुनिश्चित करती है कि डेवलपर्स के पास Java में `com.google.cloud` का प्रभावी ढंग से उपयोग करने के लिए सभी आवश्यक जानकारी है, जिसमें सेटअप, ऑथेंटिकेशन, उपयोग, और उन्नत सुविधाओं को संबोधित किया गया है, साथ ही आगे के अन्वेषण के लिए आधिकारिक स्रोतों के संदर्भ दिए गए हैं।

#### मुख्य उद्धरण
- [Google Cloud Java क्लाइंट लाइब्रेरीज़ GitHub रिपॉजिटरी विस्तृत कोड और सेटअप](https://github.com/googleapis/google-cloud-java)
- [Java डेवलपमेंट अवलोकन के लिए Google Cloud डॉक्यूमेंटेशन](https://cloud.google.com/products/anthos)
- [Java के साथ Google Cloud Storage पर Baeldung ट्यूटोरियल व्यावहारिक उदाहरण](https://www.baeldung.com/java-google-cloud-storage)