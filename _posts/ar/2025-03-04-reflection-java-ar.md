---
audio: false
generated: true
lang: ar
layout: post
title: الانعكاس في جافا
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المرجح أن `java.lang.reflect` يُستخدم للانعكاس (reflection) في جافا، مما يسمح للبرامج بفحص وتعديل هيكلها أثناء وقت التشغيل.
- تشير الأبحاث إلى أن الفئات الرئيسية تشمل `Class` و`Method` و`Field` و`Constructor` لفحص ومعالجة مكونات الفئة.
- تميل الأدلة نحو الاستخدامات الشائعة مثل استدعاء الأسلوب الديناميكي، والوصول إلى الحقول الخاصة، وإنشاء أطر عمل عامة.

### ما هو `java.lang.reflect`؟
`java.lang.reflect` هو حزمة في جافا تمكن الانعكاس (reflection)، وهي ميزة تسمح للبرامج بفحص أو تعديل هيكلها وسلوكها الخاص أثناء وقت التشغيل. هذا يعني أنه يمكنك فحص الفئات والأساليب والحقول وحتى استدعائها ديناميكيًا دون معرفتها في وقت الترجمة.

### كيفية استخدامه
لاستخدام `java.lang.reflect`، ابدأ بالحصول على كائن `Class`، الذي يمثل الفئة التي تريد فحصها. يمكنك القيام بذلك بثلاث طرق:
- استخدم `MyClass.class` إذا كنت تعرف الفئة في وقت الترجمة.
- استدعِ `instance.getClass()` على كائن.
- استخدم `Class.forName("package.ClassName")` للتحميل الديناميكي، على الرغم من أن هذا يمكن أن يلقي استثناء `ClassNotFoundException`.

بمجرد حصولك على كائن `Class`، يمكنك:
- الحصول على الأساليب باستخدام `getMethods()` للأساليب العامة أو `getDeclaredMethods()` لجميع الأساليب، بما في ذلك الخاصة.
- الوصول إلى الحقول باستخدام `getFields()` للحقول العامة أو `getDeclaredFields()` لجميع الحقول، واستخدم `setAccessible(true)` للوصول إلى الحقول الخاصة.
- العمل مع المنشئات باستخدام `getConstructors()` وإنشاء كائنات باستخدام `newInstance()`.

على سبيل المثال، لاستدعاء أسلوب خاص:
- احصل على كائن `Method`، عيّنه قابلًا للوصول باستخدام `setAccessible(true)`، ثم استخدم `invoke()` لاستدعائه.

### تفصيل غير متوقع
جانب غير متوقع هو أن الانعكاس يمكن أن يهدد الأمان بتجاوز معدلات الوصول، لذا استخدم `setAccessible(true)` بحذر، خاصة في كود الإنتاج.

---

### ملاحظة المسح: دليل شامل لاستخدام `java.lang.reflect`

توفر هذه الملاحظة استكشافًا متعمقًا لحزمة `java.lang.reflect` في جافا، مفصلة وظيفتها واستخدامها وتأثيراتها، بناءً على تحليل موسع للموارد المتاحة. الانعكاس (Reflection) هو ميزة قوية في جافا، تمكن البرامج من فحص وتعديل هيكلها أثناء وقت التشغيل، وهو ذو قيمة خاصة في سيناريوهات البرمجة الديناميكية.

#### مقدمة في الانعكاس في جافا

الانعكاس (Reflection) هو ميزة في لغة برمجة جافا تسمح لبرنامج قيد التنفيذ بفحص أو "التأمل" على نفسه ومعالجة الخصائص الداخلية. هذه القدرة غير شائعة في لغات مثل Pascal أو C أو C++، مما يجعل انعكاس جافا أداة فريدة وقوية. على سبيل المثال، تمكن فئة جافا من الحصول على أسماء جميع أعضائها وعرضها، وهو مفيد في سيناريوهات مثل JavaBeans، حيث يمكن معالجة مكونات البرمجيات بصريًا عبر أدوات البناء باستخدام الانعكاس لتحميل وفحص خصائص الفئة ديناميكيًا ([Using Java Reflection](https://www.oracle.com/technical-resources/articles/java/javareflection.html)).

توفر حزمة `java.lang.reflect` الفئات والواجهات اللازمة لتنفيذ الانعكاس، مدعمةً تطبيقات مثل المصححات (debuggers) والمترجمات (interpreters) ومدققي الكائنات (object inspectors) ومتصفحات الفئات (class browsers) وخدمات مثل Object Serialization وJavaBeans. هذه الحزمة، جنبًا إلى جنب مع `java.lang.Class`، تسهل الوصول إلى الأعضاء العامة لكائن مستهدف بناءً على فئة وقت التشغيل الخاصة به أو الأعضاء المُعلن عنها بواسطة فئة معينة، مع خيارات لقمع تحكم الوصول الانعكاسي الافتراضي إذا كان `ReflectPermission` الضروري متاحًا ([java.lang.reflect (Java Platform SE 8)](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)).

#### الفئات الرئيسية وأدوارها

تتضمن حزمة `java.lang.reflect` عدة فئات رئيسية، تخدم كل منها غرضًا محددًا في الانعكاس:

- **Class**: تمثل فئة أو واجهة في آلة جافا الافتراضية (JVM). وهي نقطة الدخول لعمليات الانعكاس، وتوفر أساليب لفحص خصائص وقت التشغيل، بما في ذلك الأعضاء ومعلومات النوع. لكل نوع من الكائنات، تقوم JVM بإنشاء مثيل غير قابل للتغيير من `java.lang.Class`، وهو أمر بالغ الأهمية لإنشاء فئات وكائنات جديدة ([Lesson: Classes (The Java™ Tutorials > The Reflection API)](https://docs.oracle.com/javase/tutorial/reflect/class/index.html)).

- **Method**: تمثل أسلوبًا (method) لفئة، مما يسمح بالاستدعاء والفحص الديناميكي. توفر أساليب مثل `getName()` و`getParameterTypes()` و`invoke()`، مما يمكن البرنامج من استدعاء الأساليب أثناء وقت التشغيل، حتى الخاصة منها، بعد تعيين إمكانية الوصول ([Guide to Java Reflection | Baeldung](https://www.baeldung.com/java-reflection)).

- **Field**: تمثل حقلًا (field) (متغير عضو) لفئة، مما يسهل الحصول على القيم أو تعيينها ديناميكيًا. تتضمن أساليب مثل `getName()` و`getType()` و`get()` و`set()`، مع القدرة على الوصول إلى الحقول الخاصة باستخدام `setAccessible(true)` ([Java Reflection Example Tutorial | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)).

- **Constructor**: تمثل منشئًا (constructor) لفئة، مما يمكن من إنشاء مثيلات جديدة ديناميكيًا. توفر أساليب مثل `getParameterTypes()` و`newInstance()`، مفيدة لإنشاء كائنات ذات وسائط منشئ محددة ([Reflection in Java - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/)).

- **AccessibleObject**: فئة أساسية لـ `Field` و`Method` و`Constructor`، تقدم أسلوب `setAccessible()` لتجاوز فحوصات تحكم الوصول، وهو أمر ضروري للوصول إلى الأعضاء الخاصة ولكن يتطلب معالجة بحذر بسبب الآثار الأمنية ([java.lang.reflect (Java SE 19 & JDK 19 [build 1])](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html)).

#### الاستخدام العملي والأمثلة

لاستخدام `java.lang.reflect`، الخطوة الأولى هي الحصول على كائن `Class`، والذي يمكن القيام به بثلاث طرق:

1. **استخدام بناء الجملة `.class`**: الرجوع إلى الفئة مباشرة، على سبيل المثال `Class<?> cls1 = String.class`.
2. **استخدام أسلوب `getClass()`**: الاستدعاء على مثيل، على سبيل المثال `String str = "hello"; Class<?> cls2 = str.getClass()`.
3. **استخدام `Class.forName()`**: التحميل الديناميكي بالاسم، على سبيل المثال `Class<?> cls3 = Class.forName("java.lang.String")`، مع ملاحظة أنه يمكن أن يلقي استثناء `ClassNotFoundException` ([Trail: The Reflection API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html)).

بمجرد الحصول عليه، يسمح كائن `Class` بفحص خصائص الفئة المختلفة:

- `getName()` تُرجع الاسم المؤهل بالكامل.
- `getSuperclass()` تسترجع الفئة الأم (superclass).
- `getInterfaces()` تسرد الواجهات المطبقة.
- `isInterface()` تتحقق مما إذا كانت واجهة.
- `isPrimitive()` تحدد ما إذا كان نوعًا بدائيًا.

##### العمل مع الأساليب (Methods)

يمكن استرداد الأساليب باستخدام:
- `getMethods()` لجميع الأساليب العامة، بما في ذلك الموروثة.
- `getDeclaredMethods()` لجميع الأساليب المُعلن عنها في الفئة، بما في ذلك الخاصة.

لاستدعاء أسلوب، استخدم أسلوب `invoke()` لكائن `Method`. على سبيل المثال، لاستدعاء أسلوب عام:
```java
Method method = cls.getMethod("toString");
String result = (String) method.invoke(str);
```
للأساليب الخاصة، عيّن إمكانية الوصول أولاً:
```java
Method privateMethod = cls.getDeclaredMethod("privateMethod");
privateMethod.setAccessible(true);
privateMethod.invoke(obj);
```
هذا النهج مفيد لاستدعاء الأسلوب الديناميكي، خاصة في أطر العمل حيث يتم تحديد أسماء الأساليب أثناء وقت التشغيل ([Invoking Methods (The Java™ Tutorials > The Reflection API > Members)](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html)).

##### العمل مع الحقول (Fields)

يتم الوصول إلى الحقول بشكل مشابه:
- `getFields()` للحقول العامة، بما في ذلك الموروثة.
- `getDeclaredFields()` لجميع الحقول المُعلن عنها.

للحصول على قيمة حقل أو تعيينها:
```java
Field field = cls.getDeclaredField("x");
field.setAccessible(true);
int value = (int) field.get(obj);
field.set(obj, 10);
```
هذا مفيد بشكل خاص لتصحيح الأخطاء أو التسجيل، حيث تحتاج جميع حقول الكائن إلى الفحص ([Java Reflection (With Examples)](https://www.programiz.com/java-programming/reflection)).

##### العمل مع المنشئات (Constructors)

يتم استرداد المنشئات باستخدام:
- `getConstructors()` للمنشئات العامة.
- `getDeclaredConstructors()` لجميع المنشئات.

لإنشاء مثيل:
```java
Constructor<?> constructor = cls.getConstructor(int.class, String.class);
Object obj = constructor.newInstance(10, "hello");
```
هذا أمر أساسي لإنشاء الكائنات الديناميكية، كما في أطر عمل حقن التبعية (dependency injection) ([Java Reflection - javatpoint](https://www.javatpoint.com/java-reflection)).

#### التعامل مع تحكم الوصول والأمان

بشكل افتراضي، يحترم الانعكاس معدلات الوصول (public, private, protected). للوصول إلى الأعضاء الخاصة، استخدم `setAccessible(true)` على الكائن المعني (مثل `Field`، `Method`، `Constructor`). ومع ذلك، يمكن أن يشكل هذا مخاطر أمنية بتجاوز التغليف (encapsulation)، لذا يُوصى باستخدامه فقط عند الضرورة ومع الأذونات المناسبة، مثل `ReflectPermission` ([java - What is reflection and why is it useful? - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)).

#### حالات الاستخدام والتطبيقات العملية

يُستخدم الانعكاس بشكل شائع في:
- **أطر العمل العامة (Generic Frameworks)**: إنشاء مكتبات تعمل مع أي فئة، مثل Spring أو Hibernate.
- **التسلسل/إلغاء التسلسل (Serialization/Deserialization)**: تحويل الكائنات من وإلى تدفقات (streams)، كما في Object Serialization في جافا.
- **أطر عمل الاختبار (Testing Frameworks)**: استدعاء الأساليب ديناميكيًا، كما يظهر في JUnit.
- **تطوير الأدوات (Tool Development)**: بناء مصححات (debuggers) وبيئات التطوير المتكاملة (IDEs) ومتصفحات الفئات التي تفحص هياكل الفئات.

على سبيل المثال، فكر في سيناريو حيث لديك قائمة بأسماء الفئات وتريد إنشاء مثيلات واستدعاء أسلوب:
```java
List<String> classNames = Arrays.asList("com.example.ClassA", "com.example.ClassB");
for (String className : classNames) {
    Class<?> cls = Class.forName(className);
    Object obj = cls.newInstance();
    Method method = cls.getMethod("doSomething");
    method.invoke(obj);
}
```
يوضح هذا التحميل الديناميكي للفئة واستدعاء الأسلوب، وهي ميزة قوية للتكيف أثناء وقت التشغيل ([Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)).

مثال عملي آخر هو آلية تسجيل عامة (generic logging mechanism):
```java
void printObjectFields(Object obj) {
    Class<?> cls = obj.getClass();
    Field[] fields = cls.getDeclaredFields();
    for (Field field : fields) {
        field.setAccessible(true);
        System.out.println(field.getName() + ": " + field.get(obj));
    }
}
```
يمكن استخدام هذا لتصحيح الأخطاء، وطباعة جميع حقول أي كائن، مما يظهر فائدة الانعكاس في مهام الفحص ([Reflection in Java - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/)).

#### المزالق المحتملة وأفضل الممارسات

بينما هي قوية، إلا أن للانعكاس عدة اعتبارات:

1. **الأداء**: عمليات الانعكاس، مثل `Method.invoke()` أو `Constructor.newInstance()`، أبطأ بشكل عام من الاستدعاءات المباشرة بسبب عمليات البحث والفحوصات الديناميكية، كما هو مذكور في تحسينات الأداء في Java SE 8 ([Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)).

2. **الأمان**: السماح بالوصول التعسفي إلى الأعضاء الخاصة يمكن أن يهدد التغليف (encapsulation) والأمان، لذا استخدم `setAccessible(true)` بشكل مقتصد، خاصة في كود الإنتاج، وعزل استخدام الانعكاس لتقليل المخاطر ([java - What is reflection and why is it useful? - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)).

3. **سلامة النوع (Type Safety)**: غالبًا ما يتضمن الانعكاس العمل مع أنواع `Object` عامة، مما يزيد من خطر `ClassCastException` إذا لم يتم التعامل معها بشكل صحيح، مما يتطلب تحويلًا دقيقًا للأنواع والتحقق منها ([Java Reflection Example Tutorial | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)).

4. **معالجة الاستثناءات (Exception Handling)**: يمكن للعديد من أساليب الانعكاس أن تلقى استثناءات مثل `NoSuchMethodException` أو `IllegalAccessException` أو `InvocationTargetException`، مما يستلزم معالجة قوية للاستثناءات لضمان استقرار البرنامج ([Trail: The Reflection API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html)).

أفضل الممارسات تشمل:
- استخدم الانعكاس فقط عند الضرورة، مفضلًا الكتابة الساكنة (static typing) حيثما أمكن.
- قلل من استخدام `setAccessible(true)` للحفاظ على التغليف.
- تأكد من سلامة النوع من خلال التحويل والتحقق المناسبين.
- تعامل مع الاستثناءات بأسلوب مناسب لمنع فشل وقت التشغيل.

#### التحليل المقارن لأساليب الانعكاس

لتنظيم الأساليب المختلفة للوصول إلى مكونات الفئة، ضع في الاعتبار الجدول التالي الذي يقارن عمليات الانعكاس الرئيسية:

| العملية                      | أسلوب الوصول العام        | أسلوب الوصول الكامل         | ملاحظات                                     |
|------------------------------|---------------------------|-----------------------------|---------------------------------------------|
| الحصول على الأساليب          | `getMethods()`           | `getDeclaredMethods()`      | يتضمن الموروث للعام، جميع المُعلن عنها للكل |
| الحصول على الحقول            | `getFields()`            | `getDeclaredFields()`       | العام يتضمن الموروث، الكل يتضمن الخاص      |
| الحصول على المنشئات          | `getConstructors()`      | `getDeclaredConstructors()` | العام فقط، الكل يتضمن الخاص                |
| استدعاء الأسلوب              | `invoke()` بعد `getMethod()` | `invoke()` بعد `getDeclaredMethod()` | يتطلب `setAccessible(true)` للنوع الخاص |
| الوصول إلى الحقل             | `get()`/`set()` بعد `getField()` | `get()`/`set()` بعد `getDeclaredField()` | يتطلب `setAccessible(true)` للنوع الخاص |

يبرز هذا الجدول التمييز بين أساليب الوصول العام والكامل، وهو أمر بالغ الأهمية لفهم نطاق الانعكاس وآثاره الأمنية ([java.lang.reflect.Method Class in Java - GeeksforGeeks](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/)).

#### الخلاصة

تمثل حزمة `java.lang.reflect` حجر الزاوية للبرمجة الديناميكية في جافا، حيث تقدم إمكانيات قوية لفحص ومعالجة هياكل الفئات أثناء وقت التشغيل. من خلال فهم فئاتها الرئيسية واستخدامها العملي وأفضل ممارساتها، يمكن للمطورين الاستفادة من الانعكاس لتطبيقات قوية مع التخفيف من مزالقه المحتملة. يضمن هذا الدليل الشامل، المستند إلى مصادر موثوقة، فهمًا شاملًا لكل من مبرمجي جافا المبتدئين وذوي الخبرة.

**الاستشهادات الرئيسية:**
- [Using Java Reflection introduction and examples](https://www.oracle.com/technical-resources/articles/java/javareflection.html)
- [Guide to Java Reflection with detailed examples](https://www.baeldung.com/java-reflection)
- [Reflection in Java comprehensive tutorial](https://www.geeksforgeeks.org/reflection-in-java/)
- [Java Reflection Example Tutorial for beginners](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)
- [Java Reflection detailed guide with examples](https://www.javatpoint.com/java-reflection)
- [What is reflection and why is it useful in Java](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)
- [java.lang.reflect.Method Class in Java detailed](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/)
- [Java Reflection with practical examples](https://www.programiz.com/java-programming/reflection)
- [java.lang.reflect package summary Java SE 8](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)
- [java.lang.reflect package summary Java SE 19](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html)
- [Core Java Reflection official documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/index.html)
- [Trail The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/index.html)
- [Trail The Reflection API Java Tutorials detailed](https://docs.oracle.com/javase/tutorial/reflect/)
- [Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)
- [Lesson Classes The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/class/index.html)
- [Invoking Methods The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html)