---
audio: false
generated: true
lang: hi
layout: post
title: HTTPmine का उपयोग
translated: true
---

मैं समझता हूँ कि आपने "httpmime.jar" के बजाय "httpmine.jar" का उल्लेख किया होगा, क्योंकि "httpmime" एक प्रसिद्ध लाइब्रेरी है जो Apache HttpComponents द्वारा HTTP अनुरोधों में MIME multipart entities (जैसे फाइल अपलोड) को संभालने के लिए उपयोग की जाती है। अगर मैं गलत हूँ, तो कृपया स्पष्ट करें! यहाँ `httpmime.jar` का उपयोग करने के तरीके हैं:

---

### `httpmime.jar` क्या है?
`httpmime.jar` Apache HttpComponents परियोजना का हिस्सा है। यह `httpclient.jar` की क्षमता को बढ़ाता है, जो multipart/form-data अनुरोधों का समर्थन प्रदान करता है, जो आमतौर पर फाइल अपलोड या HTTP पर जटिल डेटा भेजने के लिए उपयोग किए जाते हैं।

इसका उपयोग करने के लिए, आपको इसके निर्भरताओं की भी आवश्यकता होगी, जैसे `httpclient.jar` और `httpcore.jar`, क्योंकि `httpmime` इन लाइब्रेरियों पर आधारित है।

---

### `httpmime.jar` को अपने Java परियोजना में उपयोग करने के चरण

#### 1. **JAR फ़ाइल डाउनलोड करें**
- [Apache HttpComponents डाउनलोड पेज](https://hc.apache.org/downloads.cgi) या `httpmime` के लिए Maven रिपोजिटरी पर जाएं (जैसे, [वर्सन 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- `httpmime-<version>.jar` फ़ाइल डाउनलोड करें (जैसे, `httpmime-4.5.14.jar`).
- आपको भी चाहिए:
  - `httpclient-<version>.jar` (जैसे, `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (जैसे, `httpcore-4.4.16.jar`)
- सुनिश्चित करें कि वर्सन संगत हैं (परीक्षित करें [परियोजना निर्भरताओं](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

अगर आप Maven या Gradle का उपयोग कर रहे हैं, तो मैनुअल डाउनलोड को छोड़ें और इसे अपने बिल्ड टूल के माध्यम से जोड़ें (देखें चरण 2).

#### 2. **JAR को अपने परियोजना में जोड़ें**
- **मैनुअल विधि (बिल्ड टूल के बिना):**
  - डाउनलोड किए गए `httpmime.jar`, `httpclient.jar`, और `httpcore.jar` फ़ाइलें एक फ़ोल्डर में रखें (जैसे, `lib/` आपके परियोजना डायरेक्टरी में).
  - अगर आप एक IDE जैसे Eclipse या IntelliJ का उपयोग कर रहे हैं:
    - **Eclipse**: अपने परियोजना पर दाएं क्लिक करें > Properties > Java Build Path > Libraries > Add External JARs > JARs चुनें > Apply.
    - **IntelliJ**: File > Project Structure > Modules > Dependencies > "+" > JARs या डायरेक्टरी > JARs चुनें > OK.
  - अगर आप कमांड लाइन से चल रहे हैं, तो JARs को अपने क्लासपाथ में शामिल करें:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **Maven का उपयोग (सिफारिश की जाती है):**
  अपने `pom.xml` में यह जोड़ें:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- नवीनतम वर्सन का उपयोग करें -->
  </dependency>
  ```
  Maven स्वचालित रूप से `httpclient` और `httpcore` को पारित निर्भरताओं के रूप में खींच लेगा।

- **Gradle का उपयोग:**
  अपने `build.gradle` में यह जोड़ें:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **`httpmime` का उपयोग करने के लिए कोड लिखें**
यहाँ `httpmime` का उपयोग करके एक फ़ाइल को multipart HTTP POST अनुरोध के माध्यम से अपलोड करने का उदाहरण है:

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

        // multipart entity बनाएं
        File file = new File("path/to/your/file.txt"); // अपने फ़ाइल पथ से बदलें
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // फ़ाइल जोड़ें
        builder.addTextBody("description", "यह एक टेस्ट फ़ाइल है"); // पाठ फ़ील्ड जोड़ें (वैकल्पिक)

        // POST अनुरोध में entity सेट करें
        httpPost.setEntity(builder.build());

        // अनुरोध को अंजाम दें
        HttpResponse response = httpClient.execute(httpPost);

        // प्रतिक्रिया स्थिति को प्रिंट करें
        System.out.println("प्रतिक्रिया कोड: " + response.getStatusLine().getStatusCode());

        // साफ़ करें
        httpClient.close();
    }
}
```

#### 4. **मुख्य क्लास और उपयोग**
- **`MultipartEntityBuilder`**: multipart entity बनाने के लिए उपयोग किया जाता है। आप फ़ाइलें (`addPart`), पाठ (`addTextBody`), या बाइनरी डेटा (`addBinaryBody`) जोड़ सकते हैं।
- **`FileBody`**: अपलोड करने के लिए एक फ़ाइल का प्रतिनिधित्व करता है।
- **`CloseableHttpClient`**: `httpclient.jar` से HTTP क्लाइंट अनुरोध को अंजाम देने के लिए।

#### 5. **अपने प्रोग्राम को चलाएं**
- अगर आप एक IDE का उपयोग कर रहे हैं, तो बस प्रोग्राम चलाएं।
- अगर आप कमांड लाइन का उपयोग कर रहे हैं, तो ऊपर दिखाए गए क्लासपाथ के साथ कॉम्पाइल और चलाएं।

#### 6. **संघर्ष**
- **ClassNotFoundException**: सुनिश्चित करें कि सभी आवश्यक JARs (`httpmime`, `httpclient`, `httpcore`) आपके क्लासपाथ में हैं।
- **वर्सन मिसमैच**: संगत वर्सन के JARs का उपयोग करें (जैसे, `httpmime-4.5.14` के साथ `httpclient-4.5.14` और `httpcore-4.4.16`).
- **Android परियोजनाएं**: Android में अपना `org.apache.http` पैकेज है, जो संघर्ष कर सकता है। या तो बिल्ट-इन वर्सन को छोड़ें या एक पुनः पैकेज्ड JAR का उपयोग करें (जैसे, JarJar के माध्यम से).

---

### उदाहरण उपयोग मामला
अगर आप एक फ़ाइल को एक सर्वर (जैसे एक REST API) पर अपलोड कर रहे हैं, तो `httpmime` `multipart/form-data` अनुरोध बनाना सरल बनाता है, जो फ़ाइल अपलोड के लिए एक मानक है।

कृपया स्पष्टीकरण या किसी विशेष स्थिति में मदद की आवश्यकता हो तो मुझे बताएं!