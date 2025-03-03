---
audio: false
generated: true
lang: ar
layout: post
title: تسلسل الكائنات في جاڤا
translated: true
---

أعتقد أنك قصدت "java.io.Serializable" - واجهة رئيسية في جاڤا تستخدم لتسلسل الكائنات. إليك دليل عملي على كيفية استخدامها:

### ما هو Serializable؟
`java.io.Serializable` هي واجهة علامة (لا توجد طرق للتطبيق) تعلن للمحرك التنفيذي في جاڤا أن فئة يمكن أن يتم تسلسلها - تحويلها إلى تيار من البايتات لحفظها في ملف، إرسالها عبر الشبكة، أو تخزينها في قاعدة بيانات، ثم تسلسلها مرة أخرى إلى كائن.

### الخطوات الأساسية لاستخدام Serializable

1. **تطبيق الواجهة**
   أضف `implements Serializable` إلى فئةك. هذا هو الحد الأدنى المطلوب.

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

2. **التسلسل - كتابة الكائن**
   استخدم `ObjectOutputStream` لكتابة الكائن إلى ملف أو تيار.

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

3. **التسلسل العكسي - قراءة الكائن**
   استخدم `ObjectInputStream` لقراءة الكائن مرة أخرى.

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

### النقاط الرئيسية التي يجب تذكرها

- **serialVersionUID**: لضمان التوافق أثناء التسلسل العكسي، حدد `serialVersionUID`. إذا لم تفعل ذلك، يولد جاڤا واحدًا تلقائيًا، ولكن قد يختلف عبر JVMs أو تغييرات في الفئة.

   ```java
   private static final long serialVersionUID = 1L;
   ```

   أضف هذا إلى فئة `Person`.

- **حقول مؤقتة**: الحقول المسماة بـ `transient` لن يتم تسلسلها.
   ```java
   private transient String temporaryData;
   ```

- **حقول غير قابلة للتسلسل**: إذا لم يتم تنفيذ `Serializable` في فئة الحقل، ستحصل على `NotSerializableException`. إما جعل هذه الفئة `Serializable` أو علامة الحقل `transient`.

- **الوراثة**: إذا كانت الفئة الأب تفعيل `Serializable`، فإن الفئات الفرعية قابلة للتسلسل أيضًا. إذا لم يكن ذلك، يجب أن يكون لدى الفئة الأب بناء بدون معلمات لتعمل التسلسل العكسي.

### مثال مع transient و serialVersionUID
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

### اختبار ذلك
تسلسل و تسلسل عكسي `Employee`. ستلاحظ أن `password` هو `null` بعد التسلسل العكسي لأنه `transient`.

### الحالات الشائعة

- حفظ حالة الكائن في ملف (مثل حفظ اللعبة).
- إرسال الكائنات عبر الشبكة (مثل في RMI أو الأنظمة الموزعة).
- تخزين الكائنات في الذاكرة المؤقتة.

### الأخطاء

- **الأمن**: يمكن أن يعرض التسلسل الحقول الخاصة إذا لم يتم التعامل معها بعناية. اعتبر طرق `writeObject` و `readObject` المخصصة للبيانات الحساسة.
- **الأداء**: يمكن أن يكون التسلسل بطيئًا للكائنات المعقدة.
- **التسجيل**: يمكن أن يتسبب تغييرات الفئة (مثل إضافة حقول) في كسر التسلسل العكسي ما لم يتم إدارة `serialVersionUID`.

### التسلسل المخصص (اختياري)
إذا كنت تحتاج إلى التحكم في التسلسل، قم بتطبيق هذه الطرق:
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

أعلمني إذا كنت تريد غوصًا أعمق في أي جزء!