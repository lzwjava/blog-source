---
audio: false
generated: true
lang: hi
layout: post
title: क्यारक्टर एन्कोडिंग और डिकोडिंग इन जावा
translated: true
---

`java.nio.charset` पैकेज जावा में चरित्र एन्कोडिंग और डिकोडिंग के लिए उपकरण प्रदान करता है, जो विभिन्न फॉर्मेट या विभिन्न सिस्टमों में टेक्स्ट डेटा के साथ काम करने के लिए आवश्यक है। नीचे इस पैकेज का उपयोग करने का एक व्यापक गाइड है।

---

#### **`java.nio.charset` क्या है?**
`java.nio.charset` पैकेज में ऐसे क्लास शामिल हैं जो चरसेट (charsets) को प्रबंधित करते हैं, जो चरित्रों को बाइट्स में एन्कोड करने और फिर चरित्रों में डिकोड करने की प्रक्रिया को परिभाषित करते हैं। यह फाइल पढ़ने और लिखने, नेटवर्क संचार, या विभिन्न भाषाओं में टेक्स्ट प्रोसेसिंग जैसे कार्यों के लिए महत्वपूर्ण है, जहां UTF-8, ISO-8859-1 या अन्य एन्कोडिंग का उपयोग किया जा सकता है।

इस पैकेज का प्राथमिक क्लास `Charset` है, जिसे `CharsetEncoder` और `CharsetDecoder` जैसे अतिरिक्त क्लासों का समर्थन मिलता है, जो अधिक उन्नत उपयोग के लिए हैं।

---

#### **`java.nio.charset` में मुख्य क्लास**
1. **`Charset`**
   एक चरित्र एन्कोडिंग (जैसे, UTF-8, ISO-8859-1) को दर्शाता है। इस क्लास का उपयोग बाइट्स और चरित्रों के बीच परिवर्तन के लिए एन्कोडिंग को निर्दिष्ट करने के लिए किया जाता है।

2. **`StandardCharsets`**
   एक उपयोगिता क्लास है जो आमतौर पर उपयोग किए जाने वाले चरसेटों के लिए स्थिरांक प्रदान करता है, जैसे `StandardCharsets.UTF_8` या `StandardCharsets.ISO_8859_1`। यह चरसेट नामों को मैन्युअल रूप से खोजने की आवश्यकता को दूर करता है।

3. **`CharsetEncoder` और `CharsetDecoder`**
   ये क्लास एन्कोडिंग (चरित्रों को बाइट्स में) और डिकोडिंग (बाइट्स को चरित्रों में) पर फाइन-ग्रेनेड नियंत्रण प्रदान करते हैं, आमतौर पर NIO बफर्स जैसे `ByteBuffer` और `CharBuffer` के साथ उपयोग किए जाते हैं।

---

#### **`java.nio.charset` का उपयोग कैसे करें**

##### **1. एक `Charset` इंस्टेंस प्राप्त करना**
`java.nio.charset` का उपयोग करने के लिए आपको एक `Charset` ऑब्जेक्ट की आवश्यकता होती है। इसके लिए दो मुख्य तरीके हैं:

- **`StandardCharsets` का उपयोग** (सामान्य चरसेटों के लिए अनुशंसित):
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // प्रीडिफाइंड UTF-8 चरसेट
  ```

- **`Charset.forName()` का उपयोग** (समर्थित किसी भी चरसेट के लिए):
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // UTF-8 चरसेट
  ```
  नोट: अगर चरसेट नाम अमान्य है, तो यह एक `UnsupportedCharsetException` फेंकता है, इसलिए इसे उचित रूप से संभालें:
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("Charset not supported: " + e.getMessage());
  }
  ```

---

##### **2. बुनियादी उपयोग: स्ट्रिंग और बाइट्स के बीच परिवर्तन**
बहुत से अनुप्रयोगों के लिए, आप एक `Charset` का उपयोग `String` क्लास के साथ एन्कोड या डिकोड करने के लिए कर सकते हैं।

- **बाइट्स को एक स्ट्रिंग में डिकोड करना**:
  एक बाइट एरे को एक `String` में एक विशेष चरसेट का उपयोग करके परिवर्तित करें:
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // "Hello" in UTF-8
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // Outputs: Hello
  ```

- **एक स्ट्रिंग को बाइट्स में एन्कोड करना**:
  एक `String` को एक बाइट एरे में एक विशेष चरसेट का उपयोग करके परिवर्तित करें:
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

ये तरीके सरल हैं और अधिकांश उपयोग के लिए पर्याप्त हैं, जैसे फाइल I/O या बुनियादी टेक्स्ट प्रोसेसिंग।

---

##### **3. रीडर्स और राइटर्स का उपयोग**
स्ट्रीम (जैसे, `InputStream` या `OutputStream`) के साथ काम करते समय, आप `InputStreamReader` और `OutputStreamWriter` के साथ एक `Charset` का उपयोग कर सकते हैं टेक्स्ट डेटा को प्रबंधित करने के लिए।

- **एक `InputStream` से पढ़ना**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  InputStream inputStream = new FileInputStream("file.txt");
  InputStreamReader reader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
  int data;
  while ((data = reader.read()) != -1) {
      System.out.print((char) data);
  }
  reader.close();
  ```

- **एक `OutputStream` में लिखना**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

नोट: ये क्लास एक चरसेट नाम (जैसे, `"UTF-8"`) या एक `Charset` ऑब्जेक्ट स्वीकार करते हैं।

---

##### **4. `java.nio.file.Files` के साथ सरल फाइल ऑपरेशंस**
जावा 7 से, `java.nio.file` पैकेज फाइलों को एक `Charset` का उपयोग करके पढ़ने और लिखने के लिए सुविधाजनक तरीकों प्रदान करता है:

- **एक फाइल को एक स्ट्रिंग में पढ़ना**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **एक स्ट्रिंग को एक फाइल में लिखना**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

ये तरीके एन्कोडिंग और डिकोडिंग को आंतरिक रूप से प्रबंधित करते हैं, जिससे वे सरल फाइल ऑपरेशंस के लिए आदर्श होते हैं।

---

##### **5. उन्नत उपयोग: `CharsetEncoder` और `CharsetDecoder`**
जैसे कि NIO चैनलों के साथ काम करने या आंशिक डेटा प्रोसेसिंग जैसे मामलों में अधिक नियंत्रण की आवश्यकता होती है, `CharsetEncoder` और `CharsetDecoder` का उपयोग करें।

- **`CharsetEncoder` के साथ एन्कोड करना**:
  NIO बफर्स का उपयोग करके चरित्रों को बाइट्स में परिवर्तित करें:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("Hello");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **`CharsetDecoder` के साथ डिकोड करना**:
  बाइट्स को चरित्रों में परिवर्तित करें:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // Outputs: Hello
  ```

ये क्लास `SocketChannel`, `FileChannel`, या अन्य NIO घटकों के साथ काम करने के लिए उपयोगी होते हैं जहां डेटा टुकड़ों में आता है।

---

#### **बेस्ट प्रैक्टिस**
- **हमेशा चरसेट निर्दिष्ट करें**: `Charset.defaultCharset()` पर निर्भर नहीं रहें, क्योंकि डिफॉल्ट प्लेटफॉर्म (जैसे, लिनक्स पर UTF-8, विंडोज पर windows-1252) पर बदलता है। चरसेट को स्पष्ट रूप से निर्दिष्ट करने से व्यवहार में सुसंगतता सुनिश्चित होती है:
  ```java
  // इसको न करें:
  byte[] bytes = "Hello".getBytes(); // प्लेटफॉर्म डिफॉल्ट चरसेट का उपयोग करता है

  // इसको करें:
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **`StandardCharsets` का उपयोग करें**: यह साफ़ और अमान्य चरसेट नामों से रनटाइम अपवादों से बचा देता है।

- **अपवादों को संभालें**: जब `Charset.forName()` का उपयोग करते हैं, तो अमान्य चरसेटों के लिए `UnsupportedCharsetException` को संभालें।

---

#### **सारांश**
`java.nio.charset` का उपयोग करने के लिए:
1. **एक `Charset` प्राप्त करें** `StandardCharsets` या `Charset.forName()` का उपयोग करके।
2. **परिवर्तन करें**:
   - `String` विधियों (`getBytes()`, कंस्ट्रक्टर) के लिए सरल बाइट-चरित्र परिवर्तन का उपयोग करें।
   - स्ट्रीम के लिए `InputStreamReader`/`OutputStreamWriter` का उपयोग करें।
   - फाइल ऑपरेशंस के लिए `Files.readString()`/`writeString()` का उपयोग करें।
   - उन्नत NIO मामलों के लिए `CharsetEncoder`/`CharsetDecoder` का उपयोग करें।
3. **पोर्टेबिलिटी सुनिश्चित करें** चरसेट को स्पष्ट रूप से निर्दिष्ट करके।

इस पैकेज में फ्लेक्सिबल और शक्तिशाली उपकरण शामिल हैं जो चरित्र एन्कोडिंग को प्रबंधित करने में मदद करते हैं, जिससे आपका जावा अनुप्रयोग टेक्स्ट डेटा के साथ सुदृढ़ और संगत बनता है।