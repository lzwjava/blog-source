---
audio: false
generated: true
lang: ar
layout: post
title: البرمجة التفاعلية في جافا
translated: true
type: note
---

لاستخدام **reactor-core**، وهي مكتبة جافا لبناء تطبيقات غير عائقية (non-blocking) وتزامنية (asynchronous) تعتمد على مواصفات Reactive Streams، اتبع الخطوات التالية:

---

### 1. إضافة reactor-core كاعتمادية
أولاً، قم بتضمين **reactor-core** في مشروعك. بناءً على أداة البناء الخاصة بك:

- **Maven**: أضف هذا إلى ملف `pom.xml` الخاص بك:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: أضف هذا إلى ملف `build.gradle` الخاص بك:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

هذا يضمن أن المكتبة متاحة في مشروعك. تحقق من أحدث إصدار على [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) إذا لزم الأمر.

---

### 2. فهم المكونات الأساسية
توفر reactor-core فئتين رئيسيتين للبرمجة التفاعلية:
- **`Flux`**: تمثل تدفقًا غير متزامن يمكنه بعث **من 0 إلى N عنصرًا**.
- **`Mono`**: تمثل تدفقًا غير متزامن يبعث **0 أو 1 عنصرًا**.

هذه هي اللبنات الأساسية التي ستستخدمها للتعامل مع البيانات بشكل تفاعلي.

---

### 3. إنشاء Flux أو Mono
يمكنك إنشاء نماذج من `Flux` أو `Mono` لتمثيل تدفقات البيانات الخاصة بك.

- **مثال مع Flux** (عناصر متعددة):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **مثال مع Mono** (عنصر واحد):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

طريقة `just` هي طريقة بسيطة لإنشاء تدفق من قيم ثابتة، لكن Reactor تقدم العديد من طرق الإنشاء الأخرى (مثل من المصفوفات، النطاقات، أو المصادر المخصصة).

---

### 4. الاشتراك لمعالجة البيانات
لاستهلاك العناصر المُبعثرة، تحتاج إلى **الاشتراك** في `Flux` أو `Mono`. يؤدي الاشتراك إلى تشغيل التدفق لبدء بث البيانات.

- **الاشتراك في Flux**:
  ```java
  numbers.subscribe(System.out::println);  // يطبع: 1, 2, 3, 4, 5
  ```

- **الاشتراك في Mono**:
  ```java
  greeting.subscribe(System.out::println); // يطبع: Hello, World!
  ```

يمكن أن تأخذ طريقة `subscribe` وسيطات إضافية أيضًا، مثل معالجات الأخطاء أو دوالات الإكمال، لمزيد من التحكم.

---

### 5. تحويل البيانات باستخدام العوامل
توفر Reactor مجموعة غنية من العوامل لمعالجة التدفقات، مثل `map`، `filter`، والمزيد.

- **مثال مع Flux و map**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // يطبع: 2, 4, 6, 8, 10
  ```

- **مثال مع Mono و map**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // يطبع: HELLO, WORLD!
  ```

تتيح لك هذه العوامل تحويل البيانات أو تصفيتها أو دمجها بطريقة تصريحية.

---

### 6. معالجة الأخطاء والضغط الخلفي (Backpressure)
يدعم reactor-core معالجة الأخطاء وإدارة الضغط الخلفي:
- **معالجة الأخطاء**: استخدم `subscribe` مع مستهلك للأخطاء:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // يطبع: Oops!
  ```
- **الضغط الخلفي**: تحكم في كيفية تعامل المشتركين مع تدفقات البيانات الساحقة باستخدام عوامل مثل `onBackpressureBuffer()` أو `onBackpressureDrop()`.

---

### 7. استكشاف المزيد
للحصول على استخدامات أكثر تقدمًا:
- راجع [الوثائق الرسمية لـ Reactor](https://projectreactor.io/docs/core/release/reference/) للحصول على أمثلة وشروحات مفصلة.
- ألق نظرة على [مستودع reactor-core على GitHub](https://github.com/reactor/reactor-core) للحصول على موارد إضافية.

---

### الملخص
لاستخدام **reactor-core**:
1. أضفه كاعتمادية في مشروعك.
2. استخدم `Flux` للعناصر المتعددة أو `Mono` للعنصر الفردي.
3. أنشئ تدفقات باستخدام طرق مثل `just`.
4. اشترك لمعالجة البيانات.
5. طبق العوامل لتحويل التدفقات حسب الحاجة.

هذه نقطة انطلاق مناسبة للمبتدئين للبرمجة التفاعلية باستخدام reactor-core. جرب أمثلة صغيرة لتعتاد على نموذجها التفاعلي!