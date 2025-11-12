---
audio: false
generated: true
lang: hi
layout: post
title: जावा में वर्ण एन्कोडिंग और डिकोडिंग
translated: true
type: note
---

Java में `java.nio.charset` पैकेज कैरेक्टर एन्कोडिंग और डिकोडिंग को हैंडल करने के लिए टूल्स प्रदान करता है, जो विभिन्न फॉर्मेट्स में या विभिन्न सिस्टम्स में टेक्स्ट डेटा के साथ काम करते समय आवश्यक होता है। नीचे इस पैकेज का प्रभावी ढंग से उपयोग करने के बारे में एक व्यापक गाइड दी गई है।

---

#### **`java.nio.charset` क्या है?**
`java.nio.charset` पैकेज में ऐसी क्लासेस होती हैं जो कैरेक्टर सेट्स (charsets) को मैनेज करती हैं, जो परिभाषित करते हैं कि कैरेक्टर्स को बाइट्स में कैसे एन्कोड किया जाता है और वापस कैरेक्टर्स में कैसे डिकोड किया जाता है। यह फाइलों को पढ़ने और लिखने, नेटवर्क कम्युनिकेशन, या विभिन्न भाषाओं में टेक्स्ट प्रोसेसिंग जैसे कार्यों के लिए महत्वपूर्ण है, जहां UTF-8, ISO-8859-1, या अन्य एन्कोडिंग्स का उपयोग किया जा सकता है।

इस पैकेज की प्राथमिक क्लास `Charset` है, जिसे और अधिक एडवांस्ड use cases के लिए `CharsetEncoder` और `CharsetDecoder` जैसी अतिरिक्त क्लासेस द्वारा सपोर्ट किया जाता है।

---

#### **`java.nio.charset` में मुख्य क्लासेस**
1. **`Charset`**  
   एक कैरेक्टर एन्कोडिंग (जैसे, UTF-8, ISO-8859-1) को रिप्रेजेंट करता है। आप बाइट्स और कैरेक्टर्स के बीच कनवर्जन के लिए एन्कोडिंग निर्दिष्ट करने हेतु इस क्लास का उपयोग करते हैं।

2. **`StandardCharsets`**  
   एक यूटिलिटी क्लास जो आमतौर पर उपयोग होने वाले charsets के लिए कॉन्स्टेंट्स प्रदान करती है, जैसे `StandardCharsets.UTF_8` या `StandardCharsets.ISO_8859_1`। यह charset नामों को मैन्युअली देखने की आवश्यकता को समाप्त करती है।

3. **`CharsetEncoder` और `CharsetDecoder`**  
   ये क्लासेस एन्कोडिंग (कैरेक्टर्स से बाइट्स) और डिकोडिंग (बाइट्स से कैरेक्टर्स) पर बारीक नियंत्रण प्रदान करती हैं, आमतौर पर NIO बफर्स जैसे `ByteBuffer` और `CharBuffer` के साथ उपयोग की जाती हैं।

---

#### **`java.nio.charset` का उपयोग कैसे करें**

##### **1. एक `Charset` इंस्टेंस प्राप्त करना**
`java.nio.charset` का उपयोग शुरू करने के लिए, आपको एक `Charset` ऑब्जेक्ट की आवश्यकता होती है। इसे प्राप्त करने के दो मुख्य तरीके हैं:

- **`StandardCharsets` का उपयोग करना** (सामान्य charsets के लिए सिफारिश किया गया):
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // पूर्वनिर्धारित UTF-8 charset
  ```

- **`Charset.forName()` का उपयोग करना** (किसी भी सपोर्टेड charset के लिए):
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // UTF-8 charset
  ```
  नोट: यदि charset नाम अमान्य है, तो यह एक `UnsupportedCharsetException` थ्रो करता है, इसलिए इसे उचित तरीके से हैंडल करें:
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("Charset सपोर्टेड नहीं है: " + e.getMessage());
  }
  ```

---

##### **2. बेसिक उपयोग: स्ट्रिंग्स और बाइट्स के बीच कनवर्ट करना**
अधिकांश एप्लिकेशन्स के लिए, आप टेक्स्ट को एन्कोड या डिकोड करने के लिए `String` क्लास के साथ एक `Charset` का उपयोग कर सकते हैं।

- **बाइट्स को स्ट्रिंग में डिकोड करना**:
  एक विशिष्ट charset का उपयोग करके बाइट ऐरे को `String` में कन्वर्ट करें:
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // UTF-8 में "Hello"
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // आउटपुट: Hello
  ```

- **स्ट्रिंग को बाइट्स में एन्कोड करना**:
  एक विशिष्ट charset का उपयोग करके `String` को बाइट ऐरे में कन्वर्ट करें:
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

ये मेथड्स सरल हैं और अधिकांश use cases, जैसे फाइल I/O या बेसिक टेक्स्ट प्रोसेसिंग, के लिए पर्याप्त हैं।

---

##### **3. रीडर्स और राइटर्स का उपयोग करना**
जब स्ट्रीम्स (जैसे, `InputStream` या `OutputStream`) के साथ काम कर रहे हों, तो आप टेक्स्ट डेटा को हैंडल करने के लिए `InputStreamReader` और `OutputStreamWriter` का एक `Charset` के साथ उपयोग कर सकते हैं।

- **InputStream से पढ़ना**:
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

- **OutputStream में लिखना**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

नोट: ये क्लासेस या तो एक charset नाम (जैसे, `"UTF-8"`) या एक `Charset` ऑब्जेक्ट स्वीकार करती हैं।

---

##### **4. `java.nio.file.Files` के साथ सरलीकृत फाइल ऑपरेशन्स**
Java 7 के बाद से, `java.nio.file` पैकेज एक `Charset` का उपयोग करके फाइलों को पढ़ने और लिखने के लिए सुविधाजनक मेथड्स प्रदान करता है:

- **फाइल को स्ट्रिंग में पढ़ना**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **स्ट्रिंग को फाइल में लिखना**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

ये मेथड्स एन्कोडिंग और डिकोडिंग को आंतरिक रूप से हैंडल करते हैं, जिससे ये सीधे-सादे फाइल ऑपरेशन्स के लिए आदर्श बनते हैं।

---

##### **5. एडवांस्ड उपयोग: `CharsetEncoder` और `CharsetDecoder`**
ऐसे सिनेरियोस के लिए जिनमें अधिक नियंत्रण की आवश्यकता होती है (जैसे, NIO चैनल्स के साथ काम करना या आंशिक डेटा प्रोसेस करना), `CharsetEncoder` और `CharsetDecoder` का उपयोग करें।

- **`CharsetEncoder` के साथ एन्कोडिंग**:
  NIO बफर्स का उपयोग करके कैरेक्टर्स को बाइट्स में कन्वर्ट करें:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("Hello");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **`CharsetDecoder` के साथ डिकोडिंग**:
  बाइट्स को कैरेक्टर्स में कन्वर्ट करें:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // आउटपुट: Hello
  ```

ये क्लासेस तब उपयोगी होती हैं जब `SocketChannel`, `FileChannel`, या अन्य NIO कंपोनेंट्स के साथ काम कर रहे हों जहां डेटा चंक्स में आता है।

---

#### **बेस्ट प्रैक्टिसेज**
- **हमेशा Charset निर्दिष्ट करें**: `Charset.defaultCharset()` पर भरोसा करने से बचें, क्योंकि डिफॉल्ट प्लेटफॉर्म के अनुसार बदलता है (जैसे, Linux पर UTF-8, Windows पर windows-1252)। Charset को स्पष्ट रूप से निर्दिष्ट करने से सुसंगत व्यवहार सुनिश्चित होता है:
  ```java
  // इसे Avoid करें:
  byte[] bytes = "Hello".getBytes(); // प्लेटफॉर्म डिफॉल्ट charset का उपयोग करता है

  // यह करें:
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **`StandardCharsets` का उपयोग करें**: यह क्लीनर होता है और अमान्य charset नामों से होने वाले रनटाइम एक्सेप्शन्स से बचाता है।

- **एक्सेप्शन्स को हैंडल करें**: जब `Charset.forName()` का उपयोग कर रहे हों, तो असमर्थित charsets के लिए `UnsupportedCharsetException` को कैच करें।

---

#### **सारांश**
`java.nio.charset` का उपयोग करने के लिए:
1. **एक `Charset` प्राप्त करें** `StandardCharsets` या `Charset.forName()` का उपयोग करके।
2. **कनवर्जन करें**:
   - सरल बाइट-कैरेक्टर कनवर्जन के लिए `String` मेथड्स (`getBytes()`, कंस्ट्रक्टर) का उपयोग करें।
   - स्ट्रीम्स के लिए `InputStreamReader`/`OutputStreamWriter` का उपयोग करें।
   - फाइल ऑपरेशन्स के लिए `Files.readString()`/`writeString()` का उपयोग करें।
   - एडवांस्ड NIO सिनेरियोस के लिए `CharsetEncoder`/`CharsetDecoder` का उपयोग करें।
3. **पोर्टेबिलिटी सुनिश्चित करें** charsets को स्पष्ट रूप से निर्दिष्ट करके।

यह पैकेज कैरेक्टर एन्कोडिंग को मैनेज करने के लिए लचीले और शक्तिशाली टूल्स प्रदान करता है, जो आपके Java एप्लिकेशन्स को मजबूत और विविध टेक्स्ट डेटा के साथ संगत बनाता है।