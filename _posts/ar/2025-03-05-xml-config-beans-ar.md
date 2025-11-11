---
audio: false
generated: true
lang: ar
layout: post
title: ملفات التكوين إكس إم إل للفول
translated: true
type: note
---

لمعالجة استفسارك حول كيفية عمل beans XML، بما في ذلك خصائص bean مع props وkeys، وأي فئة تستخدم ملفات XML هذه، وكيف يتم تحميلها، دعنا نقسمها بوضوح وبشكل منهجي. يفترض هذا الشرح سياقًا مثل Spring، حيث يُعد "beans XML" مصطلحًا شائعًا لتكوين beans.

### كيف يعمل Beans XML؟

في أطر العمل مثل Spring، **ملف beans XML** هو ملف تكوين يُستخدم لتحديد وإدارة كائنات تسمى *beans*. تكون هذه beans عادةً كائنات Java التي تقوم Spring بتجهيزها وتكوينها وإدارتها. يحدد ملف XML:

- **Beans**: يتم تعريف كل bean باستخدام علامة `<bean>`، والتي تتضمن `id` (معرف فريد) و`class` (الاسم المؤهل بالكامل لفئة Java المراد تجهيزها).
- **الخصائص**: يمكن أن تحتوي beans على خصائص، وهي قيم أو مراجع يتم تعيينها في bean لتكوين سلوكها. يتم تعريف الخصائص باستخدام علامة `<property>`.
- **Props و Keys**: داخل علامة `<property>`، يمكنك استخدام عنصر `<props>` لتحديد مجموعة من أزواج المفتاح-القيمة. يكون هذا مفيدًا عندما تتوقع bean كائن `java.util.Properties` أو هيكل مشابه مثل `Map`. يحتوي عنصر `<props>` على علامات `<prop>` متعددة، لكل منها سمة `key` وقيمة مقابلة.

إليك مثالاً على كيف يبدو هذا في ملف beans XML:

```xml
<bean id="myBean" class="com.example.MyBean">
    <property name="someProperty">
        <props>
            <prop key="key1">value1</prop>
            <prop key="key2">value2</prop>
        </props>
    </property>
</bean>
```

في هذا المثال:
- يتم إنشاء bean بالمعرف `myBean` من الفئة `com.example.MyBean`.
- لدى bean خاصية باسم `someProperty`.
- يحدد عنصر `<props>` مجموعة من أزواج المفتاح-القيمة (`key1=value1` و `key2=value2`)، والتي تقوم Spring بتحويلها إلى كائن `Properties` وحقنه في `myBean` عبر طريقة setter مثل `setSomeProperty(Properties props)`.

عبارة "it puts in resources" في استفسارك غير واضحة بعض الشيء، ولكنها على الأرجح تشير إلى أن ملف XML هو *مورد* (ملف في classpath التطبيق أو نظام الملفات) يستخدمه التطبيق، أو يمكن أن تعني أن beans المحددة في XML (مثل مصدر بيانات) تمثل موارد يستخدمها التطبيق. في الوقت الحالي، دعنا نفترض أنه يتعلق بملف XML نفسه كونه موردًا يتم تحميله بواسطة التطبيق.

### أي فئة ستستخدم ملفات XML هذه؟

في Spring، الفئة المسؤولة عن استخدام (أي تحميل ومعالجة) ملف beans XML هي **`ApplicationContext`**. بتحديد أكثر، إنها تطبيق لواجهة `ApplicationContext`، مثل:

- **`ClassPathXmlApplicationContext`**: يحمل ملف XML من classpath.
- **`FileSystemXmlApplicationContext`**: يحمل ملف XML من نظام الملفات.

تعتبر `ApplicationContext` الواجهة المركزية في Spring لتوفير معلومات التكوين للتطبيق. تقرأ ملف beans XML، وتقوم بتحليله، وتستخدم التعريفات لإنشاء وإدارة beans. بينما تستخدم beans نفسها (مثل `com.example.MyBean`) الخصائص المحددة في XML، فإن `ApplicationContext` هي الفئة التي تعالج ملف XML مباشرة لتحقيق هذا.

### كيف سيتم تحميله؟

يتم تحميل ملف beans XML في التطبيق عن طريق إنشاء مثيل لتطبيق `ApplicationContext` وتحديد موقع ملف XML. إليك كيف يعمل خطوة بخطوة:

1. **تحديد موقع ملف XML**: عند إنشاء `ApplicationContext`، تقوم بتقديم اسم أو مسار ملف XML. على سبيل المثال:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   هنا، يُفترض أن `"beans.xml"` موجود في classpath (على سبيل المثال، في الدليل `src/main/resources` في مشروع Java نموذجي).

2. **التحميل كمورد**: تستخدم `ApplicationContext` `ResourceLoader` لتحديد موقع وتحمل ملف XML كمورد `Resource`. في هذه الحالة، يبحث `ClassPathXmlApplicationContext` عن الملف في classpath.

3. **تحليل XML**: داخليًا، تستخدم Spring `XmlBeanDefinitionReader` لتحليل ملف XML. يفسر هذا القارئ علامات `<bean>` والخصائص وعناصر `<props>`، مما ينشئ كائنات `BeanDefinition` تصف كيف يجب بناء كل bean.

4. **إنشاء Bean**: تستخدم `ApplicationContext` (التي تمتد `BeanFactory` في Spring) تعريفات bean هذه لتجهيز beans، وتعيين خصائصها (بما في ذلك حقن كائن `Properties` من `<props>`)، وإدارة دورة حياتها.

بمجرد التحميل، يمكنك استرداد beans من `ApplicationContext` كما يلي:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### جمع كل شيء معًا

- **كيف يعمل Beans XML**: يحدد XML beans وخصائصها، بما في ذلك أزواج المفتاح-القيمة عبر `<props>`. تقوم Spring بتحليل هذا XML لتكوين وتجهيز beans.
- **الفئة التي تستخدم XML**: تستخدم `ApplicationContext` (مثل `ClassPathXmlApplicationContext`) ملف XML لإعداد التطبيق.
- **كيف يتم تحميله**: يتم تحميل XML كمورد من classpath أو نظام الملفات عند إنشاء مثيل `ApplicationContext`، مع تحديد موقع الملف.

على سبيل المثال، إذا كان `beans.xml` الخاص بك في classpath، فستقوم بتحميله باستخدام:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
ثم تقوم Spring بمعالجة الباقي، مما يجعل beans المُكونة متاحة لتطبيقك.

هذه الآلية قوية ومرنة، مما يسمح لك بتحديد تكوينات معقدة في XML تجلبها Spring إلى الحياة أثناء وقت التشغيل.