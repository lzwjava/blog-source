---
audio: false
generated: true
lang: ar
layout: post
title: استخدام مكتبة المجموعات في سكالا من جافا
translated: true
type: note
---

لاستخدام حزمة `scala.collection` في جافا، يمكنك الاستفادة من قابلة التشغيل البيني بين سكالا وجافا نظرًا لأن كلا اللغتين تُترجمان إلى bytecode خاص بآلة جافا الافتراضية (JVM). هذا يسمح لكود جافا باستدعاء فئات سكالا، بما في ذلك تلك الموجودة في حزمة `scala.collection`، بشرط أن تكون مكتبة سكالا متاحة لمشروع الجافا الخاص بك. فيما يلي دليل خطوة بخطوة لتحقيق ذلك، مكتمل بالشروحات والأمثلة.

---

### **الخطوة 1: تضمين مكتبة سكالا في مشروع الجافا الخاص بك**
نظرًا لأن حزمة `scala.collection` هي جزء من المكتبة القياسية لسكالا، فأنت بحاجة إلى تضمين مكتبة سكالا في classpath مشروع الجافا الخاص بك. يمكن القيام بذلك عن طريق إضافة dependency مكتبة سكالا إلى أداة البناء الخاصة بك:

- **Maven**:
  أضف ما يلي إلى ملف `pom.xml` الخاص بك:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- استخدم الإصدار الذي يناسب احتياجاتك -->
  </dependency>
  ```

- **Gradle**:
  أضف هذا إلى ملف `build.gradle` الخاص بك:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

هذا يضمن أن فئات سكالا، بما في تلك الموجودة في `scala.collection`، متاحة لكود الجافا الخاص بك.

---

### **الخطوة 2: استيراد فئات مجموعات سكالا**
بمجرد وجود مكتبة سكالا في classpath الخاص بك، يمكنك استيراد فئات محددة من حزمة `scala.collection` في كود الجافا الخاص بك. على سبيل المثال، لاستخدام `List` الثابت من سكالا، يمكنك الاستيراد:

```java
import scala.collection.immutable.List;
```

من المجموعات شائعة الاستخدام الأخرى:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

لاحظ أن مجموعات سكالا تأتي في نوعين: قابلة للتغيير (mutable) وغير قابلة للتغيير (immutable)، على عكس مجموعات جافا، التي تكون عادة قابلة للتغيير ما لم يتم تغليفها (على سبيل المثال، عبر `Collections.unmodifiableList`).

---

### **الخطوة 3: إنشاء مجموعات سكالا في جافا**
عادةً ما يتم إنشاء مجموعات سكالا باستخدام الكائنات المرافقة (companion objects)، التي توفر طرق مصنع (factory methods) مثل `apply`. ومع ذلك، نظرًا لأن جافا لا تدعم تركيب سكالا مباشرة (مثل `List(1, 2, 3)`)، فأنت بحاجة إلى العمل مع هذه الطرق بشكل صريح. بالإضافة إلى ذلك، فإن طريقة `apply` في سكالا لمجموعات مثل `List` تتوقع `Seq` كوسيطة عند استدعائها من جافا، بسبب كيفية ترجمة varargs في سكالا.

لربط مجموعات جافا وسكالا، استخدم أدوات التحويل المقدمة من سكالا، مثل `scala.collection.JavaConverters` (لـ Scala 2.12 والإصدارات الأقدم) أو `scala.jdk.CollectionConverters` (لـ Scala 2.13 والإصدارات الأحدث). إليك كيفية إنشاء `List` من سكالا من `List` في جافا:

#### **مثال: إنشاء قائمة سكالا**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // إنشاء قائمة جافا
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // تحويل قائمة جافا إلى Seq سكالا
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // إنشاء قائمة سكالا باستخدام الكائن المرافق
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // طباعة قائمة سكالا
        System.out.println(scalaList); // الناتج: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: يحول `List` من جافا إلى `Seq` من سكالا (تحديدًا `mutable.Buffer` في Scala 2.13، وهو نوع فرعي من `Seq`).
- **`List$.MODULE$`**: يصل إلى النموذج المفرد (singleton instance) للكائن المرافق `List` في سكالا، مما يسمح لك باستدعاء طريقته `apply`.
- **`apply(scalaSeq)`**: ينشئ `List` جديدًا غير قابل للتغيير من سكالا من الـ `Seq`.

---

### **الخطوة 4: استخدام مجموعات سكالا**
بمجرد الحصول على مجموعة سكالا في جافا، يمكنك استخدام طرقها. ومع ذلك، كن على دراية بالاختلافات بين سكالا وجافا:
- **عدم القابلية للتغيير (Immutability)**: العديد من مجموعات سكالا (مثل `scala.collection.immutable.List`) غير قابلة للتغيير، مما يعني أن الطرق تُرجع مجموعات جديدة بدلاً من تعديل المجموعة الأصلية.
- **محو النوع (Type Erasure)**: كل من سكالا وجافا يستخدمان محو النوع، لذلك قد تحتاج إلى تحويل النتائج عند استرجاع العناصر.
- **الطرق الوظيفية (Functional Methods)**: تدعم مجموعات سكالا العمليات الوظيفية مثل `map` و `filter`، إلخ، والتي يمكنك استخدامها مع تعابير لامدا (lambdas) في جافا 8 والإصدارات الأحدث.

#### **مثال: الوصول إلى العناصر**
```java
// الحصول على العنصر الأول
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // الناتج: Head: 1

// الحصول على الذيل (كل شيء ما عدا العنصر الأول)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // الناتج: Tail: List(2, 3)
```

#### **مثال: استخدام Map على قائمة سكالا**
باستخدام لامدا لمضاعفة كل عنصر:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // الناتج: Doubled: List(2, 4, 6)
```

هنا، `Function1` هو واجهة في سكالا تمثل دالة ذات وسيط واحد، والتي تتماشى مع تركيب لامدا في جافا.

---

### **اعتبارات رئيسية**
- **سلامة النوع (Type Safety)**: مجموعات سكالا لها معاملات (parameterized)، ولكن أنواع الإرجاع للطرق قد تظهر كـ `Object` في جافا بسبب محو النوع. قم بالتحويل حسب الحاجة (مثل `(Integer) scalaList.head()`).
- **الأداء**: عبور الحدود بين جافا وسكالا يقدم بعض الحمل الإضافي، على الرغم من أنه بسيط عادة.
- **تحول النموذج (Paradigm Shift)**: تركز مجموعات سكالا على عدم القابلية للتغيير والبرمجة الوظيفية، والتي قد تختلف عن النمط الأمرية (imperative) في جافا. على سبيل المثال، لا يمكنك "إضافة" عنصر إلى `List` غير القابلة للتغيير – بدلاً من ذلك تنشئ واحدة جديدة (على سبيل المثال، باستخدام `:+` للإلحاق، والذي يُرجع `List` جديدة).
- **توافق الإصدارات**: تأكد من أن إصدار مكتبة سكالا يتطابق مع احتياجاتك. لـ Scala 2.13+، استخدم `scala.jdk.CollectionConverters`؛ لـ 2.12 أو الأقدم، استخدم `scala.collection.JavaConverters`.

---

### **ملخص**
يمكنك استخدام حزمة `scala.collection` في جافا عن طريق:
1. إضافة مكتبة سكالا إلى classpath المشروع الخاص بك (عبر Maven أو Gradle مثلاً).
2. استيراد فئات مجموعات سكالا المطلوبة (مثل `scala.collection.immutable.List`).
3. إنشاء مجموعات سكالا باستخدام الكائنات المرافقة (مثل `List$.MODULE$.apply`) وتحويل مجموعات جافا إلى `Seq` في سكالا باستخدام `CollectionConverters`.
4. التعامل مع المجموعات باستخدام طرق سكالا، باستخدام التحويلات (casts) وتعبيرات لامدا حسب الحاجة.

هذا الأسلوب يسمح لك بالاستفادة من مكتبة مجموعات سكالا القوية في جافا، مثل هياكل البيانات غير القابلة للتغيير أو العمليات الوظيفية، أثناء العمل داخل نظام جافا البيئي.