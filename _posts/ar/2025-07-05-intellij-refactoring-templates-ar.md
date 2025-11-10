---
audio: false
generated: true
lang: ar
layout: post
title: قوالب الاستبدال الهيكلية في إنتليجي
translated: true
type: note
---

إليك 10 أمثلة لقوالب الاستبدال الهيكلي في IntelliJ، مصنفة للتوضيح. يمكن أن تكون هذه القوالب قوية جدًا لإعادة الهيكلة، وإنفاذ معايير البرمجة، وأتمتة تحويلات الكود الشائعة.

**إعادة الهيكلة الأساسية والتبسيط:**

1.  **استبدال `if (condition) return true; else return false;` بـ `return condition;`**

      * **قالب البحث:**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **قالب الاستبدال:**
        ```java
        return $CONDITION$;
        ```
      * **السياق:** يبسط عبارات الإرجاع المنطقية.

2.  **استبدال `if (condition) { statement; }` بـ `if (!condition) { continue/break/return; }` (بند الحماية - Guard Clause)**

      * **قالب البحث:**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **قالب الاستبدال:** (هذا القالب أكثر اقتراحًا للتحويل، ستحتاج عادةً إلى تعديل الجزء الداخلي يدويًا)
        ```java
        if (!$CONDITION$) {
            // فكر في استخدام continue، break، أو return هنا
        }
        $STATEMENTS$;
        ```
      * **السياق:** يشجع على استخدام بنود الحماية لتحسين تدفق الكود. عادةً ما تستخدم إجراء "استبدال بـ" بعد العثور على الهيكل.

**عمليات المجموعات والتدفقات (Collections & Streams):**

3.  **استبدال `for (Type item : collection) { if (item.getProperty() == value) { ... } }` بـ Stream `filter`**

      * **قالب البحث:**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **قالب الاستبدال:**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // أو .map().collect()، إلخ.
        ```
      * **السياق:** الانتقال من الحلقات التقليدية إلى Java Streams للتصفية. هذا مثال عام؛ من المحتمل أن تحتاج إلى قوالب أكثر تحديدًا لـ `map`، `collect`، إلخ.

4.  **استبدال `new ArrayList<>().add(item1); new ArrayList<>().add(item2);` بـ `List.of(item1, item2);`**

      * **قالب البحث:** (قد يتطلب هذا قوالب متعددة لأعداد مختلفة من استدعاءات `add`، أو تعبيرًا نمطيًا أكثر تعقيدًا لاستدعاءات `add`. نهج أبريل لعنصرين):
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **قالب الاستبدال:**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **السياق:** استخدام Java 9+ `List.of()` لإنشاء قوائم غير قابلة للتعديل.

**معالجة الأخطاء وإدارة الموارد:**

5.  **استبدال `try { ... } catch (Exception e) { e.printStackTrace(); }` بتسجيل أكثر تحديدًا للخطأ**

      * **قالب البحث:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **قالب الاستبدال:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // استبدل بإطار العمل المفضل لتسجيل الأخطاء، مثال:
            // logger.error("حدث خطأ", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // أو أعد رمي استثناء محدد
        }
        ```
      * **السياق:** يشجع على تسجيل الأخطاء بشكل صحيح بدلاً من مجرد طباعة آثار المكالمات.

6.  **استبدال `try { ... } finally { closeable.close(); }` بـ `try-with-resources`**

      * **قالب البحث:**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **قالب الاستبدال:**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **السياق:** تحديث إدارة الموارد لاستخدام `try-with-resources` (Java 7+).

**هيكل الفئة والطريقة:**

7.  **البحث عن الحقول التي يمكن أن تكون `final`**

      * **قالب البحث:**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **قالب الاستبدال:** (هذا أكثر للبحث، ثم استخدام الإصلاح السريع)
        ```java
        class $CLASS$ {
            // فكر في جعل هذا الحقل نهائيًا (final) إذا تم تعيينه مرة واحدة فقط
            final $TYPE$ $FIELD$;
        }
        ```
      * **السياق:** تحديد الفرص لتحسين عدم القابلية للتغيير (immutability). ستقوم بإعداد عامل تصفية لإظهار الحقول التي ليس لها تعيينات متعددة فقط.

8.  **استبدال `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` بأداة تسجيل مخصصة**

      * **قالب البحث:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **قالب الاستبدال:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // أو getLogger($CLASS_NAME$.class) أكثر تحديدًا من الأداة المساعدة الخاصة بك
        ```
      * **السياق:** فرض نمط محدد لتهيئة التسجيل عبر قاعدة الكود الخاصة بك.

**الشرح والكود النمطي (Annotations & Boilerplate):**

9.  **إضافة `@Override` إلى الطرق التي تتجاوز طرق الفئة الأصلية (إذا كانت مفقودة)**

      * **قالب البحث:** (هذا أكثر تعقيدًا وغالبًا ما يتم التعامل معه بشكل أفضل من خلال فحوصات IntelliJ المدمجة، ولكن للتوضيح)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **قالب الاستبدال:** (مرة أخرى، للبحث ثم تطبيق الإصلاح السريع)
        ```java
        class $CLASS$ {
            @Override // أضف إذا كانت تتجاوز طريقة في الفئة الأصلية
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **السياق:** فرض الممارسات الجيدة واكتشاف الأخطاء المطبعية. ستستخدم عامل تصفية للتحقق مما إذا كانت الطريقة موجودة في فئة أصل/واجهة.

10. **استبدال طرق `getter/setter` المتكررة بشرح Lombok**

      * **قالب البحث:** (لـ getter واحد، سيكون هذا متكررًا جدًا لفئة كاملة)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **قالب الاستبدال:** (هذا تصوري، حيث ستقوم بحذف الـ getter وإضافة `@Getter` إلى الحقل أو الفئة)
        ```java
        // فكر في الاستبدال بـ @lombok.Getter على الحقل:
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **السياق:** أتمتة الانتقال إلى Lombok. بالنسبة لفئة كاملة، قد تستهدف الفئة نفسها وتقترح شرح `@Data` أو `@Getter/@Setter` بناءً على وجود هذه الطرق. هذا أحد التحولات الأكثر تقدمًا وربما متعددة الخطوات.

**كية استخدامها في IntelliJ:**

1.  انتقل إلى `Analyze` -> `Inspect Code...`
2.  في نافذة `Inspection Profile`، انقر على `...` بجوار اسم الملف الشخصي لتحريره.
3.  انتقل إلى `Java` -> `General` -> `Structural Search Inspection`.
4.  انقر على زر `+` لإضافة قالب بحث/استبدال جديد.
5.  حدد `Search Template` و `Replacement Template` الخاصين بك.
6.  استخدم علامة التبويب `Variables` لتعريف قيود للمتغيرات الخاصة بك (مثل النوع، النص، العدد).
7.  قم بتشغيل الفحص على الكود الخاص بك. ستقترح IntelliJ بدائل أو تظهر النتائج.

هذه الأمثلة توضح تنوع البحث والاستبدال الهيكلي. كلما كانت قوالبك أكثر تحديدًا ومرونة، كانت عمليات الاستبدال أكثر دقة وفائدة.