---
audio: false
generated: true
lang: hi
layout: post
title: Java mein Object Serialization
translated: true
---

मैं अनुमान करता हूँ कि आप "java.io.Serializable" का मतलब है - एक महत्वपूर्ण इंटरफ़ेस जो जावा में ऑब्जेक्ट सिरीलाइज़ेशन के लिए उपयोग किया जाता है। यहाँ इसका उपयोग करने का एक व्यावहारिक मार्गदर्शन है:

### Serializable क्या है?
`java.io.Serializable` एक मार्कर इंटरफ़ेस (कोई विधि लागू करने के लिए नहीं) है जो जावा रनटाइम को बताता है कि एक क्लास को सिरीलाइज़ किया जा सकता है - एक बाइट स्ट्रीम में परिवर्तित किया जा सकता है ताकि इसे एक फ़ाइल में सेंड किया जा सके, नेटवर्क के माध्यम से भेजा जा सके, या डेटाबेस में स्टोर किया जा सके, और बाद में फिर से एक ऑब्जेक्ट में डिसिरीलाइज़ किया जा सके।

### Serializable का उपयोग करने के लिए बुनियादी कदम

1. **इंटरफ़ेस लागू करें**
   अपने क्लास में `implements Serializable` जोड़ें। यह न्यूनतम आवश्यकता है।

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

2. **सिरीलाइज़ेशन - ऑब्जेक्ट लिखना**
   `ObjectOutputStream` का उपयोग करके ऑब्जेक्ट को एक फ़ाइल या स्ट्रीम में लिखें।

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

3. **डिसिरीलाइज़ेशन - ऑब्जेक्ट पढ़ना**
   `ObjectInputStream` का उपयोग करके ऑब्जेक्ट को वापस पढ़ें।

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

### याद रखने के लिए मुख्य बिंदु

- **serialVersionUID**: डिसिरीलाइज़ेशन के दौरान संगतता सुनिश्चित करने के लिए, एक `serialVersionUID` परिभाषित करें। अगर आप नहीं करते, तो जावा इसे स्वचालित रूप से बनाता है, लेकिन यह JVMs या क्लास परिवर्तन के बीच भिन्न हो सकता है।

   ```java
   private static final long serialVersionUID = 1L;
   ```

   इसे अपने `Person` क्लास में जोड़ें।

- **Transient Fields**: `transient` से चिह्नित फ़ील्ड सिरीलाइज़ नहीं होंगे।
   ```java
   private transient String temporaryData;
   ```

- **Non-Serializable Fields**: अगर एक फ़ील्ड का क्लास `Serializable` लागू नहीं करता, तो आप `NotSerializableException` प्राप्त करेंगे। या तो उस क्लास को `Serializable` बनाएं या उस फ़ील्ड को `transient` चिह्नित करें।

- **Inheritance**: अगर एक सुपरक्लास `Serializable` लागू करता है, तो उपक्लास भी सिरीलाइज़ करने योग्य होंगे। अगर नहीं, तो सुपरक्लास में एक नो-आर्ग कंस्ट्रक्टर होना चाहिए ताकि डिसिरीलाइज़ेशन काम करे।

### transient और serialVersionUID के साथ उदाहरण
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // Won't be serialized
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

### इसे टेस्ट करना
`Employee` को सिरीलाइज़ और डिसिरीलाइज़ करें। आप देखेंगे कि `password` डिसिरीलाइज़ेशन के बाद `null` है क्योंकि यह `transient` है।

### आम उपयोग मामले
- ऑब्जेक्ट स्टेट को एक फ़ाइल में सेंड करना (उदाहरण के लिए, गेम सेव्स).
- ऑब्जेक्ट को नेटवर्क के माध्यम से भेजना (उदाहरण के लिए, RMI या वितरित प्रणालियों में).
- ऑब्जेक्ट को कैश करना।

### चूक
- **सुरक्षा**: सिरीलाइज़ेशन निजी फ़ील्डों को खोल सकता है अगर सही से संभाला नहीं जाता। संवेदनशील डेटा के लिए कस्टम `writeObject` और `readObject` विधियों का विचार करें।
- **प्रदर्शन**: सिरीलाइज़ेशन जटिल ऑब्जेक्टों के लिए धीमा हो सकता है।
- **वर्सनिंग**: क्लास परिवर्तन (उदाहरण के लिए, फ़ील्ड जोड़ना) डिसिरीलाइज़ेशन को तोड़ सकते हैं जब तक कि `serialVersionUID` को संभाला नहीं जाता।

### कस्टम सिरीलाइज़ेशन (वैकल्पिक)
अगर आपको सिरीलाइज़ेशन पर नियंत्रण चाहिए, तो इन विधियों को लागू करें:
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // Custom logic
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // Custom logic
}
```

मुझे बताएं अगर आप किसी भी हिस्से में गहरी गहराई चाहते हैं!