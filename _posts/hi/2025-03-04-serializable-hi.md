---
audio: false
generated: true
lang: hi
layout: post
title: जावा में ऑब्जेक्ट सीरियलाइज़ेशन
translated: true
type: note
---

मैं मानता हूं कि आपका मतलब "java.io.Serializable" से है - जावा में ऑब्जेक्ट सीरियलाइज़ेशन के लिए इस्तेमाल होने वाला एक महत्वपूर्ण इंटरफेस। यहां इसके उपयोग का एक व्यावहारिक मार्गदर्शक दिया गया है:

### Serializable क्या है?
`java.io.Serializable` एक मार्कर इंटरफेस (कोई मेथड इम्प्लीमेंट नहीं करनी होती) है जो जावा रनटाइम को बताता है कि एक क्लास को सीरियलाइज़ किया जा सकता है - यानी उसे बाइट स्ट्रीम में बदलकर फाइल में सेव किया जा सकता है, नेटवर्क पर भेजा जा सकता है, या डेटाबेस में संग्रहित किया जा सकता है, और बाद में डी-सीरियलाइज़ करके वापस ऑब्जेक्ट में बदला जा सकता है।

### Serializable का उपयोग करने के मूल चरण

1. **इंटरफेस को इम्प्लीमेंट करें**
   अपनी क्लास में `implements Serializable` जोड़ें। यह न्यूनतम आवश्यकता है।

   ```java
   import java.io.Serializable;

   public class Person implements Serializable {
       private String name;
       private int age;

       // Constructor
       public Person(String name, int age) {
           this.name = name;
           this.age = age;
       }

       // Getters and setters
       public String getName() { return name; }
       public void setName(String name) { this.name = name; }
       public int getAge() { return age; }
       public void setAge(int age) { this.age = age; }

       @Override
       public String toString() {
           return "Person{name='" + name + "', age=" + age + "}";
       }
   }
   ```

2. **सीरियलाइज़ेशन - ऑब्जेक्ट को लिखना**
   ऑब्जेक्ट को फाइल या स्ट्रीम में लिखने के लिए `ObjectOutputStream` का उपयोग करें।

   ```java
   import java.io.FileOutputStream;
   import java.io.ObjectOutputStream;
   import java.io.IOException;

   public class SerializeExample {
       public static void main(String[] args) {
           Person person = new Person("Alice", 25);

           try (FileOutputStream fileOut = new FileOutputStream("person.ser");
                ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
               out.writeObject(person);
               System.out.println("Serialized data is saved in person.ser");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }
   ```

3. **डी-सीरियलाइज़ेशन - ऑब्जेक्ट को वापस पढ़ना**
   ऑब्जेक्ट को वापस पढ़ने के लिए `ObjectInputStream` का उपयोग करें।

   ```java
   import java.io.FileInputStream;
   import java.io.ObjectInputStream;
   import java.io.IOException;

   public class DeserializeExample {
       public static void main(String[] args) {
           try (FileInputStream fileIn = new FileInputStream("person.ser");
                ObjectInputStream in = new ObjectInputStream(fileIn)) {
               Person person = (Person) in.readObject();
               System.out.println("Deserialized Person: " + person);
           } catch (IOException | ClassNotFoundException e) {
               e.printStackTrace();
           }
       }
   }
   ```

### याद रखने योग्य मुख्य बातें

- **serialVersionUID**: डी-सीरियलाइज़ेशन के दौरान संगतता सुनिश्चित करने के लिए, एक `serialVersionUID` परिभाषित करें। यदि आप ऐसा नहीं करते हैं, तो जावा स्वचालित रूप से एक जेनरेट कर देगा, लेकिन यह अलग-अलग JVM या क्लास परिवर्तनों में भिन्न हो सकता है।

   ```java
   private static final long serialVersionUID = 1L;
   ```

   इसे अपनी `Person` क्लास में जोड़ें।

- **Transient फ़ील्ड्स**: `transient` से चिह्नित फ़ील्ड्स सीरियलाइज़ नहीं होंगी।
   ```java
   private transient String temporaryData;
   ```

- **नॉन-सीरियलाइज़ेबल फ़ील्ड्स**: यदि किसी फ़ील्ड की क्लास `Serializable` को इम्प्लीमेंट नहीं करती है, तो आपको `NotSerializableException` मिलेगा। या तो उस क्लास को `Serializable` बनाएं या फ़ील्ड को `transient` चिह्नित करें।

- **इनहेरिटेंस**: यदि कोई सुपरक्लास `Serializable` को इम्प्लीमेंट करती है, तो सबक्लासेज भी सीरियलाइज़ेबल होती हैं। यदि नहीं, तो डी-सीरियलाइज़ेशन के काम करने के लिए सुपरक्लास में एक नो-आर्ग कंस्ट्रक्टर होना चाहिए।

### transient और serialVersionUID के साथ उदाहरण
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // सीरियलाइज़ नहीं होगा
    private int id;

    public Employee(String name, String password, int id) {
        this.name = name;
        this.password = password;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Employee{name='" + name + "', password='" + password + "', id=" + id + "}";
    }
}
```

### इसका परीक्षण
`Employee` को सीरियलाइज़ और डी-सीरियलाइज़ करें। आप देखेंगे कि डी-सीरियलाइज़ेशन के बाद `password` `null` है क्योंकि वह `transient` है।

### सामान्य उपयोग के मामले
- ऑब्जेक्ट की स्थिति को फाइल में सहेजना (जैसे, गेम सेव)।
- नेटवर्क पर ऑब्जेक्ट भेजना (जैसे, RMI या डिस्ट्रिब्यूटेड सिस्टम में)।
- ऑब्जेक्ट्स को कैश करना।

### समस्याएं
- **सुरक्षा**: सीरियलाइज़ेशन प्राइवेट फ़ील्ड्स को एक्सपोज़ कर सकता है यदि सावधानी से नहीं संभाला गया। संवेदनशील डेटा के लिए कस्टम `writeObject` और `readObject` मेथड्स पर विचार करें।
- **प्रदर्शन**: जटिल ऑब्जेक्ट्स के लिए सीरियलाइज़ेशन धीमा हो सकता है।
- **वर्जनिंग**: क्लास में परिवर्तन (जैसे, फ़ील्ड्स जोड़ना) `serialVersionUID` को मैनेज न करने पर डी-सीरियलाइज़ेशन को तोड़ सकते हैं।

### कस्टम सीरियलाइज़ेशन (वैकल्पिक)
यदि आपको सीरियलाइज़ेशन पर नियंत्रण की आवश्यकता है, तो इन मेथड्स को इम्प्लीमेंट करें:
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // कस्टम लॉजिक
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // कस्टम लॉजिक
}
```

मुझे बताएं यदि आप किसी भाग में गहराई से जाना चाहते हैं!