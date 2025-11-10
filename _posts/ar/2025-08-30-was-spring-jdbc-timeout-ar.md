---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل فرز مهلة Spring JDBC
translated: true
type: note
---

إليك النموذج الذهني ودليل التصنيف السريع.

# آلية العمل (WAS + Spring + JDBC)

1.  **ـ DataSource موجود في WAS**

    *   تقوم بتعريف موفر JDBC وـ **DataSource** (عادةً `XA` للمعاملات الشاملة، أو غير-XA) في وحدة تحكم إدارة WAS.
    *   تقوم WAS بإدارة **ـ مجموعة اتصالات JCA** وتوزع اتصالات JDBC.

2.  **ـ يحصل Spring على الـ DataSource عبر JNDI**

    *   يتطلع تطبيق Spring إلى الـ DataSource الخاص بالخادم (مثل، `java:comp/env/jdbc/MyDS`) ويغلّفه:

        *   JDBC عادي: `JdbcTemplate` يستخدم ذلك الـ DataSource.
        *   JPA/Hibernate: `EntityManagerFactory` يستخدمه.
    *   المعاملات تكون عادةً **ـ JTA للحاوية** (`WebSphereUowTransactionManager` أو JTA قياسي). معاملة `@Transactional` الخاصة بـ Spring تنضم إلى معاملة الحاوية.

3.  **ـ مسار الاستدعاء**

    *   طلب ويب → خيط WebContainer → خدمة Spring → بدء المعاملة (JTA) → `DataSource.getConnection()` من **ـ مجموعة اتصالات WAS** → SQL عبر المشغل → قاعدة البيانات.
    *   يمكن أن تنفذ المهلات في طبقات متعددة (Spring، JPA، مجموعة اتصالات WAS، معاملة JTA، مشغل JDBC/قاعدة البيانات، الشبكة).

# عندما تحدث مهلة — حدد النوع

فكر في أربع فئات. عادةً ما تخبرك الرسالة/التتبع المكدس بالفئة.

1.  **ـ مهلة الحصول على اتصال**
    العرض: الانتظار للحصول على اتصال من المجموعة.
    ابحث عن رسائل حول استنفاد المجموعة أو `J2CA0086W / J2CA0030E`.
    المقابض النموذجية: *ـ Maximum Connections*، *ـ Connection Timeout*، *ـ Aged Timeout*، *ـ Purge Policy*.

2.  **ـ مهلة المعاملة (JTA)**
    العرض: رسائل `WTRN`/`Transaction`؛ استثناء مثل *ـ "Transaction timed out after xxx seconds"*.
    المقبض النموذجي: **ـ Total transaction lifetime timeout**. يمكنه إيقاف عمليات قاعدة البيانات الطويلة حتى لو كانت قاعدة البيانات لا تزال تعمل.

3.  **ـ مهلة الاستعلام/العبارة**
    العرض: `java.sql.SQLTimeoutException`، "query timeout" من Hibernate/JPA، أو Spring `QueryTimeoutException`.
    المقابض:

    *   Spring: `JdbcTemplate.setQueryTimeout(...)`، Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`.
    *   خصائص مخصصة لـ DataSource في WAS (أمثلة DB2): `queryTimeout`، `queryTimeoutInterruptProcessingMode`.
    *   مهلة العبارة على مستوى المشغل/قاعدة البيانات.

4.  **ـ مهلة المقبس/القراءة / الشبكة**
    العرض: بعد فترة خمول أثناء جلب طويل؛ `SocketTimeoutException` منخفض المستوى أو كود مورّد.
    المقابض: `loginTimeout`/`socketTimeout` للمشغل، جدران الحماية/NAT الخاملة، إبقاء اتصالات قاعدة البيانات نشطة.

# أين تتحقق (حسب الطبقة)

**ـ مسارات وحدة تحكم إدارة WAS (WAS التقليدي)**

*   موفر JDBC / DataSource:
  Resources → JDBC → Data sources → *ـ YourDS* →

  *   *ـ Connection pool properties*: **ـ Connection timeout**، **ـ Maximum connections**، **ـ Reap time**، **ـ Unused timeout**، **ـ Aged timeout**، **ـ Purge policy**.
  *   *ـ Custom properties*: خاصة بالمارد (مثل، `queryTimeout` لـ DB2، `currentSQLID`، `blockingReadConnectionTimeout`، `queryTimeoutInterruptProcessingMode`).
  *   *ـ JAAS – J2C* إذا كانت بيانات اعتماد المصادقة مهمة.
*   المعاملات:
  Application servers → *ـ server1* → Container Settings → **ـ Container Services → Transaction Service** → **ـ Total transaction lifetime timeout**، **ـ Maximum transaction timeout**.
*   WebContainer:
  حجم مجموعة الخيوط (إذا تراكمت الطلبات).

**ـ السجلات والتتبع**

*   WAS التقليدي: `<profile_root>/logs/<server>/SystemOut.log` و `SystemErr.log`.
    المكونات الأساسية: `RRA` (موارد المهايئ)، `JDBC`، `ConnectionPool`، `WTRN` (المعاملات).
    فعّل التتبع (بداية موجزة):

    ```
    RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
    ```

    ابحث عن:

    *   `J2CA0086W`، `J2CA0114W` (مشاكل المجموعة/الاتصال)
    *   `WTRN0037W`، `WTRN0124I` (مهلات/تراجعات المعاملات)
    *   استثناءات `DSRA`/`SQL` مع رموز SQL الخاصة بالمارد.
*   Liberty: `messages.log` تحت `wlp/usr/servers/<server>/logs/`.

**ـ PMI / المراقبة**

*   فعّل **ـ PMI** لمجموعات اتصالات JDBC ومقاييس المعاملات. راقب:

    *   حجم المجموعة، عدد الاتصالات المستخدمة، المنتظرين، وقت الانتظار، المهلات.
    *   مهلات/أعداد تراجعات المعاملات.

**ـ سجلات تطبيق Spring/JPA**

*   شغّل SQL + التوقيت في تطبيقك (`org.hibernate.SQL`، `org.hibernate.type`، تنقيح Spring JDBC) لربط المدد مقابل المهلات.

**ـ قاعدة البيانات والمشغل**

*   DB2: `db2diag.log`، `MON_GET_PKG_CACHE_STMT`، مراقبي أحداث النشاط، مهلات العبارة على مستوى قاعدة البيانات.
*   خصائص المشغل في DataSource الخاص بـ WAS أو `DriverManager` إذا كنت لا تستخدم DS الحاوية (ليس شائعًا في WAS).

**ـ الشبكة**

*   الأجهزة الوسيطة ذات مهلات الخمول. إعدادات إبقاء الاتصال نشطًا في نظام التشغيل / المشغل.

# مسار التصنيف السريع

1.  **ـ صنّف المهلة**

    *   *ـ انتظار اتصال؟* ابحث عن تحذيرات مجموعة `J2CA`. إذا كانت الإجابة نعم، زد **ـ Maximum connections**، أصلح التسريب، اضبط المجموعة، عيّن **ـ Purge Policy = EntirePool** لأحداث الاتصالات المعطلة.
    *   *ـ مهلة معاملة؟* رسائل `WTRN`. زد **ـ Total transaction lifetime timeout** أو قلّل العمل في كل معاملة؛ تجنب تغليف مهام الدُفعات الضخمة في معاملة واحدة.
    *   *ـ مهلة استعلام؟* `SQLTimeoutException` أو `QueryTimeout` من Spring/Hibernate. انسق مهلات **ـ Spring/Hibernate** مع مهلات **ـ WAS DS** و **ـ قاعدة البيانات**؛ تجنب الإعدادات المتضاربة.
    *   *ـ مهلة مقبس/قراءة؟* رسائل الشبكة/المشغل. تحقق من `socketTimeout`/`loginTimeout` للمشغل، إبقاء اتصالات قاعدة البيانات نشطة، وجدران الحماية.

2.  **ـ قارن التوقيتات**

    *   قارن مدة الفشل مع العتبات المُعدّة (مثل، "يفشل عند ~30 ثانية" → ابحث عن أي إعداد 30 ثانية: مهلة استعلام Spring 30 ثانية؟ عمر المعاملة 30 ثانية؟ انتظار المجموعة 30 ثانية؟).

3.  **ـ تحقق من صحة المجموعة**

    *   PMI: هل **ـ المنتظرون** > 0؟ هل **ـ المستخدم** قريب من **ـ الحد الأقصى**؟ هل هناك حاملون طويلو المدة؟ فكر في تفعيل **ـ كشف تسريب الاتصال** (يظهر تتبع RRA من أخذ الاتصال).

4.  **ـ رؤية قاعدة البيانات**

    *   تأكد من قاعدة البيانات: هل كانت العبارة لا تزال تعمل؟ هل أُلغيَت؟ أي انتظار للقفل؟ إذا كانت هناك أقفال → فكر في مهلة القفل مقابل مهلة العبارة.

# مقابض ومطالب مفيدة (أمثلة WAS + DB2)

*   **ـ Total transaction lifetime timeout** (على مستوى الخادم) سيقضي على الاستعلامات الطويلة حتى لو عيّنت مهلة أعلى في Spring/Hibernate. حافظ على تناسق هذه الإعدادات.
*   **ـ queryTimeoutInterruptProcessingMode** (خاصية مخصصة لـ DataSource لـ DB2): تتحكم في كيفية قيام DB2 بمقاطعة استعلام منتهي المهلة (تعاوني/قسري). يساعد في تجنب تعلق الخيوط بعد انتهاء المهلات.
*   **ـ Purge policy**: `EntirePool` يمكن أن يعيد التعافي بسرعة من حالات SQL القاتلة (مثل، إعادة تشغيل قاعدة البيانات) على حساب حدوث اضطراب بسيط.
*   **ـ Aged/Unused timeout**: أخرج الاتصالات القديمة من الخدمة لتجنب مهلات الخمول في جدران الحماية/NAT.
*   **ـ Validation**: فعّل **ـ validation by SQL** أو **ـ validation timeout** حتى يتم اكتشاف الاتصالات المعطلة قبل الاستخدام.
*   **ـ Thread pools**: إذا كانت خيوط WebContainer مشبعة، *ـ تبدو الأعراض مثل المهلات*. تأكد من أن مجموعتي خيوط WebContainer و Default مُعدّلة بالحجم المناسب.

# أمثلة تهيئة Spring الأساسية

**ـ JNDI DataSource (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**ـ مهلة استعلام JdbcTemplate (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // ثواني
  return jt;
}
```

**ـ مهلة Hibernate/JPA**

```properties
javax.persistence.query.timeout=60000  # مللي ثانية
hibernate.jdbc.timeout=60              # ثواني
```

# ما يجب التقاطه عند التصعيد

*   نص الاستثناء الدقيق + تتبع المكدس.
*   الطوابع الزمنية: بدء الطلب، بدء المعاملة، بدء الاستعلام، وقت الخطأ.
*   تهيئة مجموعة WAS DS (لقطة شاشة أو القيم)، مهلات خدمة المعاملات.
*   لقطة PMI (المنتظرون في المجموعة، المستخدم، أعداد المهلات).
*   عرض قاعدة البيانات للجلسة/العبارة في وقت الفشل.
*   ملاحظات طوبولوجيا الشبكة (جدران الحماية، الوكالات، مؤقتات الخمول).

إذا قمت بلصق جزء استثناء محدد (J2CA/WTRN/حالة SQL)، يمكنني تحديد الطبقة الدقيقة والإعداد المطابق الذي needs التعديل.