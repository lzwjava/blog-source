---
audio: false
generated: true
lang: ar
layout: post
title: ملفات التكوين XML للBeans
translated: true
---

للتعامل مع استفسارك حول كيفية عمل ملفات XML للbeans، بما في ذلك خصائص beans مع props و keys، أي فئة تستخدم هذه الملفات XML، وكيف يتم تحميلها، فلنفصل ذلك بشكل واضح ومتسلسل. يتوقع هذا التفسير سياقًا مثل Spring، حيث "beans XML" هو مصطلح شائع لتكوين beans.

### كيف يعمل XML للbeans؟

في إطار عمل مثل Spring، **ملف XML للbeans** هو ملف تهيئة يستخدم لتحديد وإدارة الكائنات التي تسمى *beans*. هذه beans هي عادةً كائنات Java التي يقوم إطار عمل Spring بإنشائها وتكوينها وإدارتها. يحدد الملف XML:

- **Beans**: يتم تعريف كل bean باستخدام علامة `<bean>`، والتي تتضمن `id` (معرف فريد) و `class` (الاسم الكامل للمصفوفة Java التي سيتم إنشاؤها).
- **Properties**: يمكن أن يكون للbeans خصائص، وهي قيم أو مراجع يتم تعيينها في bean لتكوين سلوكها. يتم تعريف الخصائص باستخدام علامة `<property>`.
- **Props و Keys**: داخل علامة `<property>`، يمكنك استخدام علامة `<props>` لتحديد مجموعة من أزواج المفتاح-القيمة. هذا مفيد عندما يتوقع bean كائنًا من نوع `java.util.Properties` أو بنية مشابهة مثل `Map`. تحتوي علامة `<props>` على علامات `<prop>` متعددة، كل منها مع سمة `key` وقيمة متطابقة.

هنا مثال على كيفية ظهور ذلك في ملف XML للbeans:

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
- يتم إنشاء bean مع ID `myBean` من الفئة `com.example.MyBean`.
- يحتوي bean على خاصية تسمى `someProperty`.
- تحتوي علامة `<props>` على مجموعة من أزواج المفتاح-القيمة (`key1=value1` و `key2=value2`), والتي يتحول Spring إلى كائن `Properties` ويحقنه في `myBean` عبر طريقة مثل `setSomeProperty(Properties props)`.

العبارة "يضع في الموارد" في استفسارك غير واضحة قليلاً، ولكن يبدو أنها تشير إلى أن الملف XML هو *مورد* (ملف في مسار التطبيق أو نظام الملفات) يستخدمه التطبيق، أو يمكن أن يعني أن beans التي يتم تعريفها في XML (مثل مصدر البيانات) تمثل الموارد المستخدمة من قبل التطبيق. لنفترض الآن أنها تتعلق بالملف XML نفسه باعتباره موردًا يتم تحميله من قبل التطبيق.

### أي فئة ستستخدم هذه الملفات XML؟

في Spring، الفئة المسؤولة عن استخدام (أي تحميل وتحليل) ملف XML للbeans هي **`ApplicationContext`**. بشكل أكثر دقة، إنها تنفيذ لمواجهة `ApplicationContext` مثل:

- **`ClassPathXmlApplicationContext`**: يحمل الملف XML من مسار التطبيق.
- **`FileSystemXmlApplicationContext`**: يحمل الملف XML من نظام الملفات.

`ApplicationContext` هو واجهة Spring المركزية لتوفير معلومات التهيئة إلى التطبيق. يقرأ ملف XML للbeans، ويحلله، ويستخدم التعريفات لإنشاء وإدارة beans. بينما تستخدم beans نفسها (مثل `com.example.MyBean`) الخصائص التي يتم تعريفها في XML، `ApplicationContext` هي الفئة التي تحلل الملف XML مباشرة لتجعل هذا يحدث.

### كيف سيتم تحميله؟

يتم تحميل ملف XML للbeans في التطبيق بإنشاء مثيل لفئة `ApplicationContext` وتحديد موقع الملف XML. voici كيفية عمل ذلك خطوة بخطوة:

1. **تحديد موقع ملف XML**: عند إنشاء `ApplicationContext`، تقدم اسم أو مسار الملف XML. على سبيل المثال:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   هنا، `"beans.xml"` يُفترض أنه في مسار التطبيق (على سبيل المثال، في `src/main/resources` في مشروع Java نموذجي).

2. **تحميل كمرجع**: يستخدم `ApplicationContext` `ResourceLoader` لتحديد وتحميل ملف XML كمرجع. في هذه الحالة، يبحث `ClassPathXmlApplicationContext` عن الملف في مسار التطبيق.

3. **تحليل XML**: داخليًا، يستخدم Spring `XmlBeanDefinitionReader` لتحليل ملف XML. يقرأ هذا القارئ علامات `<bean>`، الخصائص، و `<props>`، ويخلق كائنات `BeanDefinition` التي تشرح كيفية بناء كل bean.

4. **إنشاء Bean**: يستخدم `ApplicationContext` (الذي يمد Spring’s `BeanFactory`) هذه تعريفات bean لإنشاء beans، تعيين خصائصها (بما في ذلك حقن الكائن `Properties` من `<props>`)، وإدارة دورة حياتها.

بعد التحميل، يمكنك استرداد beans من `ApplicationContext` مثل هذا:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### جمع كل شيء معًا

- **كيف يعمل XML للbeans**: يحدد XML beans وخصائصها، بما في ذلك أزواج المفتاح-القيمة عبر `<props>`. Spring يحلل هذا XML لتكوين وإنتاج beans.
- **الفئة التي تستخدم XML**: `ApplicationContext` (مثل `ClassPathXmlApplicationContext`) يستخدم ملف XML لتكوين التطبيق.
- **كيف يتم تحميله**: يتم تحميل XML كمرجع من مسار التطبيق أو نظام الملفات عند إنشاء مثيل `ApplicationContext` وتحديد موقع الملف.

على سبيل المثال، إذا كان `beans.xml` في مسار التطبيق، فستحميله مثل هذا:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
ثم يدير Spring الباقي، مما يجعل beans المهيئة متاحة للتطبيق.

يوفر هذا الآلية قوة و مرونة، مما يسمح لك بتحديد تهيئات معقدة في XML التي يحوّلها Spring إلى حياة في وقت التشغيل.