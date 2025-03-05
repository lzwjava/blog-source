---
audio: false
generated: true
lang: ar
layout: post
title: استخدام مكتبة مجموعات Scala في Java
translated: true
---

لاستخدام حزمة `scala.collection` في Java، يمكنك الاستفادة من التوافق بين Scala وJava، حيث أن كلا اللغتين يتحولان إلى بايت كود JVM. وهذا يسمح لكود Java بالاتصال مع فئات Scala، بما في ذلك تلك الموجودة في حزمة `scala.collection`، بشرط أن تكون مكتبة Scala متاحة لمشروعك Java. أدناه دليل خطوة بخطوة لتحقيق ذلك، مع شرحات ومثالات.

---

### **الخطوة 1: إضافة مكتبة Scala لمشروعك Java**
منذ أن حزمة `scala.collection` جزء من مكتبة Scala القياسية، يجب عليك إضافة مكتبة Scala إلى مسار تصنيفات مشروعك Java. يمكن تحقيق ذلك من خلال إضافة اعتماد مكتبة Scala إلى أداة بناءك:

- **Maven**:
  أضف التالي إلى ملف `pom.xml`:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- استخدم الإصدار الذي يتوافق مع احتياجاتك -->
  </dependency>
  ```

- **Gradle**:
  أضف التالي إلى ملف `build.gradle`:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

هذا يضمن أن فئات Scala، بما في ذلك تلك الموجودة في `scala.collection`، متاحة لكودك Java.

---

### **الخطوة 2: استيراد فئات Scala Collections**
بعد إضافة مكتبة Scala إلى مسار التصنيفات، يمكنك استيراد فئات محددة من حزمة `scala.collection` في كودك Java. على سبيل المثال، لاستخدام قائمة Scala غير قابلة للتعديل `List`، يمكنك الاستيراد:

```java
import scala.collection.immutable.List;
```

من بين المجموعات المستخدمة بشكل شائع:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

لاحظ أن مجموعات Scala تأتي في أشكال قابلة للتعديل وغير قابلة للتعديل، عكس مجموعات Java التي تكون عادةً قابلة للتعديل ما لم يتم غلفها (على سبيل المثال، من خلال `Collections.unmodifiableList`).

---

### **الخطوة 3: إنشاء مجموعات Scala في Java**
عادة ما يتم إنشاء مجموعات Scala باستخدام كائنات رفيقة، والتي توفر طرق مصنع مثل `apply`. ومع ذلك، نظرًا لأن Java لا يدعم صيغة Scala مباشرة (على سبيل المثال، `List(1, 2, 3)`)، يجب عليك العمل مع هذه الطرق بشكل صريح. بالإضافة إلى ذلك، طريقة `apply` لـ Scala للمجموعات مثل `List` تتوقع `Seq` كحجج عندما يتم استدعاؤها من Java، بسبب كيفية ترجمة Scala's varargs.

لربط مجموعات Java وScala، استخدم أدوات التحويل التي تقدمها Scala، مثل `scala.collection.JavaConverters` (لScala 2.12 وسبقه) أو `scala.jdk.CollectionConverters` (لScala 2.13 وما بعده). إليك كيفية إنشاء قائمة Scala من قائمة Java:

#### **مثال: إنشاء قائمة Scala**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // إنشاء قائمة Java
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // تحويل قائمة Java إلى Scala Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // إنشاء قائمة Scala باستخدام الكائن رفيق
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // طباعة قائمة Scala
        System.out.println(scalaList); // Output: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: يحول قائمة Java إلى Scala `Seq` (بشكل خاص `mutable.Buffer` في Scala 2.13، وهو نوع فرعي من `Seq`).
- **`List$.MODULE$`**: يوفر الوصول إلى المثال الوحيد من الكائن رفيق `List` في Scala، مما يسمح لك باستدعاء طريقة `apply` له.
- **`apply(scalaSeq)`**: يخلق قائمة Scala غير قابلة للتعديل جديدة من `Seq`.

---

### **الخطوة 4: استخدام مجموعات Scala**
بعد أن لديك مجموعة Scala في Java، يمكنك استخدام طرقها. ومع ذلك، كن على علم بالاختلافات بين Scala وJava:
- **غير قابل للتعديل**: العديد من مجموعات Scala (على سبيل المثال، `scala.collection.immutable.List`) غير قابلة للتعديل، مما يعني أن الطرق تعيد مجموعات جديدة بدلاً من تعديل الأصلية.
- **إزالة النوع**: كلا Scala وJava يستخدمان إزالة النوع، لذا قد تحتاج إلى القسط عندما تسترجع العناصر.
- **طرق وظيفية**: مجموعات Scala تدعم العمليات الوظيفية مثل `map`، `filter`، إلخ، والتي يمكنك استخدامها مع lambdas Java 8+.

#### **مثال: الوصول إلى العناصر**
```java
// الحصول على العنصر الأول
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Output: Head: 1

// الحصول على الذيل (كل شيء باستثناء الرأس)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Output: Tail: List(2, 3)
```

#### **مثال: خريطة على قائمة Scala**
استخدام lambda لتضاعف كل عنصر:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Output: Doubled: List(2, 4, 6)
```

هنا، `Function1` هو واجهة Scala تمثل وظيفة ذات حجة واحدة، والتي تتوافق مع صيغة lambda Java.

---

### **نقاط مهمة**
- **أمان النوع**: مجموعات Scala معلمة، ولكن أنواع عودة الطرق قد تظهر ك `Object` في Java بسبب إزالة النوع. قم بالقسط حسب الحاجة (على سبيل المثال، `(Integer) scalaList.head()`).
- **الأداء**: عبور الحدود بين Java وScala يجلب بعض التكلفة، ولكن عادةً ما تكون صغيرة.
- **التحول في المنطق**: مجموعات Scala تركز على عدم قابلية للتعديل وبرمجة وظيفية، والتي قد تختلف عن أسلوب Java الالتماسي. على سبيل المثال، لا يمكنك "إضافة" إلى قائمة غير قابلة للتعديل—أنت تخلق واحدة جديدة بدلاً من ذلك (على سبيل المثال، باستخدام `:+` لإضافة، والذي يرجع قائمة جديدة).
- **التوافق في الإصدار**: تأكد من أن إصدار مكتبة Scala يتوافق مع احتياجاتك. لScala 2.13+، استخدم `scala.jdk.CollectionConverters`؛ ل2.12 أو سابقه، استخدم `scala.collection.JavaConverters`.

---

### **ملخص**
يمكنك استخدام حزمة `scala.collection` في Java من خلال:
1. إضافة مكتبة Scala إلى مسار تصنيفات مشروعك (على سبيل المثال، من خلال Maven أو Gradle).
2. استيراد فئات المجموعات Scala المطلوبة (على سبيل المثال، `scala.collection.immutable.List`).
3. إنشاء مجموعات Scala باستخدام كائنات رفيقة (على سبيل المثال، `List$.MODULE$.apply`) وتحويل مجموعات Java إلى Scala `Seq` باستخدام `CollectionConverters`.
4. معالجة المجموعات باستخدام طرق Scala، باستخدام القسط و lambdas حسب الحاجة.

هذا النهج يسمح لك باستغلال مكتبة مجموعات Scala القوية في Java، مثل بنياتها غير القابلة للتعديل أو العمليات الوظيفية، بينما تعمل داخل بيئة Java.