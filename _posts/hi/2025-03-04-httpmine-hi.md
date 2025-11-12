---
audio: false
generated: true
lang: hi
layout: post
title: HTTPmine का उपयोग करना
translated: true
type: note
---

मैं मानता हूं कि आपका मतलब "httpmine.jar" नहीं बल्कि "httpmime.jar" था, क्योंकि "httpmime" Apache HttpComponents की एक प्रसिद्ध लाइब्रेरी है जिसका उपयोग HTTP अनुरोधों में MIME मल्टीपार्ट एंटिटीज (जैसे, फ़ाइल अपलोड) को हैंडल करने के लिए किया जाता है। अगर मैं गलत हूं, तो कृपया स्पष्ट करें! यहां बताया गया है कि Java प्रोजेक्ट में `httpmime.jar` का उपयोग कैसे करें:

---

### `httpmime.jar` क्या है?
`httpmime.jar` Apache HttpComponents प्रोजेक्ट का एक हिस्सा है। यह `httpclient.jar` की कार्यक्षमता को multipart/form-data अनुरोधों के लिए सपोर्ट प्रदान करके बढ़ाता है, जिनका उपयोग आमतौर पर फ़ाइलें अपलोड करने या HTTP पर जटिल डेटा भेजने के लिए किया जाता है।

इसका उपयोग करने के लिए, आपको इसकी डिपेंडेंसीज, जैसे `httpclient.jar` और `httpcore.jar` की भी आवश्यकता होगी, क्योंकि `httpmime` इन लाइब्रेरीज पर बनती है।

---

### अपने Java प्रोजेक्ट में `httpmime.jar` का उपयोग करने के चरण

#### 1. **JAR फ़ाइल डाउनलोड करें**
- [Apache HttpComponents डाउनलोड पेज](https://hc.apache.org/downloads.cgi) पर जाएं या `httpmime` के लिए Maven रिपॉजिटरी (उदाहरण के लिए, [वर्जन 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)) पर जाएं।
- `httpmime-<version>.jar` फ़ाइल (उदाहरण के लिए, `httpmime-4.5.14.jar`) डाउनलोड करें।
- आपको इनकी भी आवश्यकता होगी:
  - `httpclient-<version>.jar` (उदाहरण के लिए, `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (उदाहरण के लिए, `httpcore-4.4.16.jar`)
- सुनिश्चित करें कि वर्जन संगत हैं ([प्रोजेक्ट डिपेंडेंसीज](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html) देखें)।

वैकल्पिक रूप से, यदि आप Maven या Gradle का उपयोग कर रहे हैं, तो मैन्युअल डाउनलोड छोड़ें और इसे अपने बिल्ड टूल के माध्यम से जोड़ें (चरण 2 देखें)।

#### 2. **JAR को अपने प्रोजेक्ट में जोड़ें**
- **मैन्युअल विधि (बिल्ड टूल्स के बिना):**
  - डाउनलोड की गई `httpmime.jar`, `httpclient.jar`, और `httpcore.jar` फ़ाइलों को एक फ़ोल्डर (उदाहरण के लिए, आपके प्रोजेक्ट डायरेक्टरी में `lib/`) में रखें।
  - यदि Eclipse या IntelliJ जैसे IDE का उपयोग कर रहे हैं:
    - **Eclipse**: अपने प्रोजेक्ट पर राइट-क्लिक करें > Properties > Java Build Path > Libraries > Add External JARs > JARs चुनें > Apply करें।
    - **IntelliJ**: File > Project Structure > Modules > Dependencies > "+" > JARs or directories > JARs चुनें > OK करें।
  - यदि कमांड लाइन से चला रहे हैं, तो JARs को अपने classpath में शामिल करें:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **Maven का उपयोग करना (अनुशंसित):**
  अपनी `pom.xml` में इसे जोड़ें:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- नवीनतम वर्जन का उपयोग करें -->
  </dependency>
  ```
  Maven स्वचालित रूप से `httpclient` और `httpcore` को ट्रांजिटिव डिपेंडेंसीज के रूप में डाउनलोड कर लेगा।

- **Gradle का उपयोग करना:**
  अपने `build.gradle` में इसे जोड़ें:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **`httpmime` का उपयोग करने के लिए कोड लिखें**
यहां एक multipart HTTP POST अनुरोध के माध्यम से फ़ाइल अपलोड करने के लिए `httpmime` का उपयोग करने का एक उदाहरण दिया गया है:

```java
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.HttpResponse;
import java.io.File;

public class FileUploadExample {
    public static void main(String[] args) throws Exception {
        // एक HTTP क्लाइंट बनाएं
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // अनुरोध भेजने के लिए URL परिभाषित करें
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // multipart एंटिटी बनाएं
        File file = new File("path/to/your/file.txt"); // अपनी फ़ाइल पथ के साथ बदलें
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // फ़ाइल जोड़ें
        builder.addTextBody("description", "This is a test file"); // टेक्स्ट फ़ील्ड जोड़ें (वैकल्पिक)

        // POST अनुरोध के लिए एंटिटी सेट करें
        httpPost.setEntity(builder.build());

        // अनुरोध निष्पादित करें
        HttpResponse response = httpClient.execute(httpPost);

        // प्रतिक्रिया स्थिति प्रिंट करें
        System.out.println("Response Code: " + response.getStatusLine().getStatusCode());

        // सफाई करें
        httpClient.close();
    }
}
```

#### 4. **मुख्य क्लासेस और उपयोग**
- **`MultipartEntityBuilder`**: multipart एंटिटी बनाने के लिए उपयोग किया जाता है। आप फ़ाइलें (`addPart`), टेक्स्ट (`addTextBody`), या बाइनरी डेटा (`addBinaryBody`) जोड़ सकते हैं।
- **`FileBody`**: अपलोड की जाने वाली फ़ाइल को दर्शाता है।
- **`CloseableHttpClient`**: अनुरोध निष्पादित करने के लिए `httpclient.jar` से HTTP क्लाइंट।

#### 5. **अपना प्रोग्राम चलाएं**
- यदि IDE का उपयोग कर रहे हैं, तो बस प्रोग्राम चलाएं।
- यदि कमांड लाइन का उपयोग कर रहे हैं, तो ऊपर दिखाए गए classpath के साथ कंपाइल और रन करें।

#### 6. **समस्या निवारण**
- **ClassNotFoundException**: सुनिश्चित करें कि सभी आवश्यक JARs (`httpmime`, `httpclient`, `httpcore`) आपके classpath में हैं।
- **वर्जन मिसमैच**: JARs के संगत वर्जन का उपयोग करें (उदाहरण के लिए, `httpmime-4.5.14` के साथ `httpclient-4.5.14` और `httpcore-4.4.16`)।
- **Android प्रोजेक्ट्स**: Android का अपना `org.apache.http` पैकेज होता है, जो संघर्ष कर सकता है। या तो बिल्ट-इन वर्जन को बाहर करें या रीपैकेज्ड JAR (उदाहरण के लिए, JarJar के माध्यम से) का उपयोग करें।

---

### उदाहरण उपयोग केस
यदि आप किसी सर्वर (जैसे REST API) पर फ़ाइल अपलोड कर रहे हैं, तो `httpmime` `multipart/form-data` अनुरोध बनाना सरल बना देता है, जो फ़ाइल अपलोड के लिए एक मानक है।

यदि आपको किसी विशिष्ट परिदृश्य के साथ स्पष्टीकरण या सहायता की आवश्यकता है, तो मुझे बताएं!