---
audio: false
generated: true
lang: ar
layout: post
title: برمجة التفاعل في جافا
translated: true
---

لاستخدام **reactor-core**، مكتبة Java لبناء تطبيقات غير متوقفة، غير متزامنة بناءً على مواصفات Reactive Streams، اتبع هذه الخطوات:

---

### 1. إضافة reactor-core كاعتماد
أولاً، أضف **reactor-core** إلى مشروعك. اعتمادًا على أداة البناء التي تستخدمها:

- **Maven**: أضف هذا إلى ملف `pom.xml`:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: أضف هذا إلى ملف `build.gradle`:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

هذا يضمن توفر المكتبة في مشروعك. تحقق من أحدث الإصدار على [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) إذا لزم الأمر.

---

### 2. فهم المكونات الأساسية
يوفر reactor-core فئتين رئيسيتين للبرمجة التفاعلية:
- **`Flux`**: يمثل تدفقًا غير متزامنًا يمكن أن يبعث **0 إلى N عناصر**.
- **`Mono`**: يمثل تدفقًا غير متزامنًا يبعث **0 أو 1 عنصر**.

هذه هي المكونات الأساسية التي ستستخدمها لتعامل مع البيانات بشكل تفاعلي.

---

### 3. إنشاء Flux أو Mono
يمكنك إنشاءInstances من `Flux` أو `Mono` لتمثيل تدفقات البيانات الخاصة بك.

- **مثال مع Flux** (عناصر متعددة):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **مثال مع Mono** (عنصر واحد):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

طريقة `just` هي طريقة بسيطة لإنشاء تدفق من القيم الثابتة، ولكن Reactor يقدم العديد من طرق الإنشاء الأخرى (مثل من المصفوفات، أو النطاقات، أو المصادر المخصصة).

---

### 4. الاشتراك في معالجة البيانات
لاستهلاك العناصر المبعثرة، عليك **الاشتراك** في `Flux` أو `Mono`. الاشتراك يثير التدفق ليبدأ في إرسال البيانات.

- **الاشتراك في Flux**:
  ```java
  numbers.subscribe(System.out::println);  // يطبع: 1, 2, 3, 4, 5
  ```

- **الاشتراك في Mono**:
  ```java
  greeting.subscribe(System.out::println); // يطبع: Hello, World!
  ```

طريقة `subscribe` يمكن أن تأخذ مبررات إضافية مثل معالجات الأخطاء أو استدعاءات الإكمال، للحصول على مزيد من التحكم.

---

### 5. تحويل البيانات باستخدام المعالجات
يوفر Reactor مجموعة غنية من المعالجات لتعديل التدفقات مثل `map`، `filter`، وما إلى ذلك.

- **مثال مع Flux و map**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // يطبع: 2, 4, 6, 8, 10
  ```

- **مثال مع Mono و map**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // يطبع: HELLO, WORLD!
  ```

تسمح هذه المعالجات لك بتحويل، تصفية، أو دمج البيانات بطريقة إعلامية.

---

### 6. معالجة الأخطاء والضغط الخلفي
يوفر reactor-core دعمًا لمعالجة الأخطاء وإدارة الضغط الخلفي:
- **معالجة الأخطاء**: استخدم `subscribe` مع مستهلك الأخطاء:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // يطبع: Oops!
  ```
- **الضغط الخلفي**: تحكم في كيفية معالجة المتابعين لتدفقات البيانات المتفوقة باستخدام المعالجات مثل `onBackpressureBuffer()` أو `onBackpressureDrop()`.

---

### 7. استكشاف المزيد
لاستخدام متقدم:
- تحقق من [التوثيق الرسمي لـ Reactor](https://projectreactor.io/docs/core/release/reference/) للحصول على أمثلة مفصلة ومدونات تعليمية.
- انظر إلى [مستودع GitHub لـ reactor-core](https://github.com/reactor/reactor-core) للحصول على موارد إضافية.

---

### ملخص
لاستخدام **reactor-core**:
1. أضفها كاعتماد في مشروعك.
2. استخدم `Flux` للعناصر المتعددة أو `Mono` للعنصر الواحد.
3. إنشاء التدفقات باستخدام طرق مثل `just`.
4. اشترك في معالجة البيانات.
5. تطبيق المعالجات لتحويل التدفقات حسب الحاجة.

هذا هو نقطة البداية الصديقة للمبتدئين للبرمجة التفاعلية مع reactor-core. تجريب مع أمثلة صغيرة للحصول على مريحة مع فلسفة التفاعل الخاصة بها!