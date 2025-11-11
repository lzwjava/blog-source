---
audio: false
generated: true
lang: ar
layout: post
title: تسلسل الكائنات في جافا
translated: true
type: note
---

أفترض أنك تقصد "java.io.Serializable" - واجهة أساسية في جافا تُستخدم لتسلسل الكائنات. إليك دليل عملي حول كيفية استخدامها:

### ما هي Serializable؟
`java.io.Serializable` هي واجهة واسمية (لا تحتوي على طرق للتنفيذ) تُخبر وقت تشغيل جافا أنه يمكن تسلسل الفئة - تحويلها إلى تدفق بايتات لحفظها في ملف، أو إرسالها عبر الشبكة، أو تخزينها في قاعدة بيانات، وإعادة تحويلها لاحقًا إلى كائن.

### الخطوات الأساسية لاستخدام Serializable

1. **تنفيذ الواجهة**
   أضف `implements Serializable` إلى فئتك. هذا هو الحد الأدنى المطلوب.

   ```java
   import java.io.Serializable;

   public class Person implements Serializable {
       private String name;
       private int age;

       // المُنشئ
       public Person(String name, int age) {
           this.name = name;
           this.age = age;
       }

       // الطرق الجالبة والمعدلة
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
   استخدم `ObjectOutputStream` لكتابة الكائن إلى ملف أو تدفق.

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

3. **إعادة التكوين - قراءة الكائن**
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

### نقاط رئيسية يجب تذكرها

- **serialVersionUID**: لضمان التوافق أثناء إعادة التكوين، عرّف `serialVersionUID`. إذا لم تفعل، ستقوم جافا بتوليد واحد تلقائيًا، لكنه قد يختلف عبر بيئات جافا الافتراضية أو مع تغييرات الفئة.

   ```java
   private static final long serialVersionUID = 1L;
   ```

   أضف هذا إلى فئة `Person` الخاصة بك.

- **الحقول العابرة**: الحقول المعلمة بـ `transient` لن يتم تسلسلها.
   ```java
   private transient String temporaryData;
   ```

- **الحقول غير القابلة للتسلسل**: إذا كانت فئة الحقل لا تنفذ `Serializable`، فستحصل على `NotSerializableException`. إما اجعل تلك الفئة قابلة للتسلسل `Serializable` أو علّم الحقل كعابر `transient`.

- **الوراثة**: إذا كانت الفئة الأم تنفذ `Serializable`، فإن الفئات الفرعية ستكون قابلة للتسلسل أيضًا. إذا لم تكن كذلك، يجب أن يكون للفئة الأم مُنشئ بدون وسائط حتى تعمل إعادة التكوين.

### مثال مع transient و serialVersionUID
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // لن يتم تسلسلها
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

### اختباره
قم بتسلسل وإعادة تكوين `Employee`. ستلاحظ أن `password` أصبحت `null` بعد إعادة التكوين لأنها عابرة `transient`.

### حالات الاستخدام الشائعة
- حفظ حالة الكائن في ملف (مثل حفظ اللعبة).
- إرسال كائنات عبر الشبكة (مثلًا في RMI أو الأنظمة الموزعة).
- تخزين الكائنات مؤقتًا.

### المزالق
- **الأمان**: يمكن أن يعرض التسلسل الحقول الخاصة إذا لم يتم التعامل معه بحذر. فكر في استخدام طرق `writeObject` و `readObject` المخصصة للبيانات الحساسة.
- **الأداء**: يمكن أن يكون التسلسل بطيئًا للكائنات المعقدة.
- **إدارة الإصدارات**: تغييرات الفئة (مثل إضافة حقول) يمكن أن تعطل إعادة التكوين ما لم تتم إدارة `serialVersionUID`.

### التسلسل المخصص (اختياري)
إذا كنت بحاجة إلى التحكم في التسلسل، نفذ هذه الطرق:
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // منطق مخصص
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // منطق مخصص
}
```

أعلمني إذا كنت تريد تعمقًا أكبر في أي جزء!