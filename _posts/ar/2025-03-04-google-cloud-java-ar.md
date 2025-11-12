---
audio: false
generated: true
lang: ar
layout: post
title: عميل جافا لجوجل كلاود
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المرجح أنه لاستخدام `com.google.cloud` في جافا، تحتاج إلى إعداد بيئة تطوير جافا، وتضمين تبعيات مكتبة عميل Google Cloud، وتهيئة المصادقة، واستخدام المكتبات للتفاعل مع خدمات Google Cloud.
- تشير الأبحاث إلى أنه يمكن التعامل مع المصادقة تلقائيًا على منصات Google Cloud أو إعدادها يدويًا للتطوير المحلي باستخدام بيانات اعتماد حساب الخدمة.
- تميل الأدلة إلى استخدام Maven أو Gradle لإدارة التبعيات، مع توفير أمثلة على Cloud Storage كحالة استخدام شائعة.

### إعداد بيئة التطوير الخاصة بك
للبدء، تأكد من تثبيت Java Development Kit (JDk) الإصدار 8 أو أعلى، جنبًا إلى جنب مع أداة بناء مثل Maven أو Gradle. تساعدك هذه الأدوات في إدارة تبعيات مشروعك وعمليات البناء.

### تضمين التبعيات
أضف تبعيات مكتبة عميل Google Cloud إلى مشروعك. بالنسبة لـ Maven، قم بتضمين Bill of Materials (BOM) ومكتبات الخدمات المحددة في ملف `pom.xml` الخاص بك. على سبيل المثال، لاستخدام Cloud Storage:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

استبدل "latest_version" بالإصدار الفعلي من [مستودع Google Cloud Java client libraries على GitHub](https://github.com/googleapis/google-cloud-java).

### تهيئة المصادقة
غالبًا ما يتم التعامل مع المصادقة تلقائيًا إذا كان تطبيقك يعمل على منصات Google Cloud مثل Compute Engine أو App Engine. للتطوير المحلي، عيّن متغير البيئة `GOOGLE_APPLICATION_CREDENTIALS` ليشير إلى ملف مفتاح JSON لحساب خدمة، أو قم بتهيئته برمجيًا.

### استخدام المكتبات
بمجرد الإعداد، قم باستيراد الفئات الضرورية، وإنشاء كائن خدمة، وإجراء مكالمات API. على سبيل المثال، لسرد buckets في Cloud Storage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

من التفاصيل غير المتوقعة أن المكتبات تدعم خدمات Google Cloud المختلفة، لكل منها حزمة فرعية خاصة تحت `com.google.cloud`، مثل `com.google.cloud.bigquery` لـ BigQuery، مما يوفر وظائف شاملة تتجاوز التخزين.

---

### ملاحظة المسح: دليل شامل حول استخدام `com.google.cloud` في جافا

توفر هذه الملاحظة استكشافًا مفصلاً لاستخدام مكتبات عميل Google Cloud لجافا، مع التركيز تحديدًا على حزمة `com.google.cloud`، للتفاعل مع خدمات Google Cloud. وهي توسع نطاق الإجابة المباشرة من خلال تضمين جميع التفاصيل ذات الصلة من البحث، منظمة من أجل الوضوح والعمق، مما يجعلها مناسبة للمطورين الذين يسعون للحصول على فهم شامل.

#### مقدمة إلى مكتبات عميل Google Cloud لجافا
توفر مكتبات عميل Google Cloud لجافا، التي يمكن الوصول إليها تحت حزمة `com.google.cloud`، واجهات بديهية ومطابقة للغة للتفاعل مع خدمات Google Cloud مثل Cloud Storage وBigQuery وCompute Engine. تم تصميم هذه المكتبات لتقليل التعليمات البرمجية النمطية، والتعامل مع تفاصيل الاتصال منخفضة المستوى، والدمج بسلاسة مع ممارسات تطوير جافا. وهي مفيدة بشكل خاص لبناء تطبيقات سحابية أصلية، والاستفادة من أدوات مثل Spring وMaven وKubernetes، كما هو موضح في الوثائق الرسمية.

#### إعداد بيئة التطوير
للبدء، يلزم وجود Java Development Kit (JDk) الإصدار 8 أو أعلى، لضمان التوافق مع المكتبات. التوزيعة الموصى بها هي Eclipse Temurin، وهي خيار مفتوح المصدر ومعتمد من Java SE TCK، كما هو مذكور في أدلة الإعداد. بالإضافة إلى ذلك، تعتبر أداة أتمتة البناء مثل Maven أو Gradle ضرورية لإدارة التبعيات. يمكن أيضًا تثبيت Google Cloud CLI (`gcloud`) للتفاعل مع الموارد من سطر الأوامر، مما يسهل مهام النشر والمراقبة.

#### إدارة التبعيات
يتم تبسيط إدارة التبعيات باستخدام Bill of Materials (BOM) المقدم من Google Cloud، والذي يساعد في إدارة الإصدارات عبر المكتبات المتعددة. بالنسبة لـ Maven، أضف ما يلي إلى ملف `pom.xml` الخاص بك:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

بالنسبة لـ Gradle، تنطبق تكوينات مماثلة، مما يضمن اتساق الإصدار. يجب التحقق من رقم الإصدار مقابل [مستودع Google Cloud Java client libraries على GitHub](https://github.com/googleapis/google-cloud-java) للحصول على آخر التحديثات. يسرد هذا المستودع أيضًا المنصات المدعومة، بما في ذلك x86_64 وMac OS X وWindows وLinux، لكنه يذكر القيود على Android وRaspberry Pi.

#### آليات المصادقة
المصادقة خطوة حاسمة، مع اختلاف الخيارات حسب البيئة. على منصات Google Cloud مثل Compute Engine أو Kubernetes Engine أو App Engine، يتم استنتاج بيانات الاعتماد تلقائيًا، مما يبسط العملية. للبيئات الأخرى، مثل التطوير المحلي، الطرق التالية متاحة:

- **حساب الخدمة (مُوصى به):** قم بإنشاء ملف مفتاح JSON من Google Cloud Console وعيّن متغير البيئة `GOOGLE_APPLICATION_CREDENTIALS` ليشير إلى مساره. بدلاً من ذلك، يمكن تحميله برمجيًا:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **التطوير/الاختبار المحلي:** استخدم Google Cloud SDK مع `gcloud auth application-default login` للحصول على بيانات اعتماد مؤقتة.
- **رمز OAuth2 موجود:** استخدم `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` لحالات استخدام محددة.

ترتيب الأسبقية لتحديد معرف المشروع يشمل خيارات الخدمة، ومتغير البيئة `GOOGLE_CLOUD_PROJECT`، وApp Engine/Compute Engine، وملف بيانات اعتماد JSON، وGoogle Cloud SDK، مع مساعدة `ServiceOptions.getDefaultProjectId()` في استنتاج معرف المشروع.

#### استخدام مكتبات العميل
بمجرد إعداد التبعيات والمصادقة، يمكن للمطورين استخدام المكتبات للتفاعل مع خدمات Google Cloud. لكل خدمة حزمتها الفرعية الخاصة تحت `com.google.cloud`، مثل `com.google.cloud.storage` لـ Cloud Storage أو `com.google.cloud.bigquery` لـ BigQuery. إليك مثال تفصيلي لـ Cloud Storage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

يسرد هذا المثال جميع الـ buckets، لكن المكتبة تدعم عمليات مثل تحميل الكائنات، وتنزيل الملفات، وإدارة سياسات الـ bucket. بالنسبة للخدمات الأخرى، تنطبق أنماط مماثلة، مع توفر طرق مفصلة في ملفات javadoc الخاصة بكل منها، مثل تلك الخاصة بـ BigQuery في [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### الميزات المتقدمة والاعتبارات
تدعم المكتبات ميزات متقدمة مثل العمليات طويلة المدى (LROs) باستخدام `OperationFuture`، مع سياسات مهلة قابلة للتكوين وإعادة المحاولة. على سبيل المثال، تتضمن الإعدادات الافتراضية لـ AI Platform (v3.24.0) تأخير إعادة محاولة أولية قدره 5000 مللي ثانية، ومضاعف 1.5، وأقصى تأخير لإعادة المحاولة 45000 مللي ثانية، وإجمالي مهلة 300000 مللي ثانية. كما يتم دعم تكوين الوكيل، باستخدام `https.proxyHost` و`https.proxyPort` لـ HTTPS/gRPC، مع خيارات مخصصة لـ gRPC عبر `ProxyDetector`.

تتوفر مصادقة مفتاح API لبعض واجهات برمجة التطبيقات، يتم تعيينها يدويًا عبر عناوين لـ gRPC أو REST، كما هو موضح في أمثلة خدمة اللغة. يتم تسهيل الاختبار بالأدوات المقدمة، والمفصلة في TESTING.md في المستودع، وتعمل إضافات IDE لـ IntelliJ وEclipse على تحسين التطوير مع دمج المكتبة.

#### المنصات المدعومة والقيود
المكتبات متوافقة مع منصات مختلفة، حيث تعمل عملاء HTTP في كل مكان وتدعم عملاء gRPC على x86_64 وMac OS X وWindows وLinux. ومع ذلك، لا يتم دعمها على Android أو Raspberry Pi أو App Engine Standard Java 7، باستثناء Datastore وStorage وBigQuery. تشمل البيئات المدعومة Windows x86_64 وMac OS X x86_64 وLinux x86_64 وGCE وGKE وGAE Std J8 وGAE Flex وAlpine Linux (Java 11+).

#### المو资源和 القراءة الإضافية
للحصول على إرشادات إضافية، يقدم [مستودع Google Cloud Java client libraries على GitHub](https://github.com/googleapis/google-cloud-java) عينات برمجية، وإرشادات المساهمة، وموارد استكشاف الأخطاء وإصلاحها. توفر البرامج التعليمية مثل تلك الموجودة على [Baeldung](https://www.baeldung.com/java-google-cloud-storage) أمثلة عملية، مثل استخدام Cloud Storage، بينما تغطي الوثائق الرسمية على [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) مفاهيم تطوير التطبيقات الأوسع نطاقًا.

#### الجدول: تفاصيل التكوين الرئيسية

| **الجانب**               | **التفاصيل**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| إصدار جافا             | يتطلب جافا 8 أو أعلى.                                                                       |
| إدارة التبعيات    | استخدم BOM لضمان اتساق الإصدار، على سبيل المثال، Maven `libraries-bom`.                                  |
| طرق المصادقة   | تلقائي على GCE/GKE/GAE، يدوي عبر `GOOGLE_APPLICATION_CREDENTIALS` أو برمجي.          |
| المنصات المدعومة      | عملاء HTTP في كل مكان، gRPC على x86_64 وMac OS X وWindows وLinux؛ غير مدعوم على Android أو Raspberry Pi.|
| مثال على الخدمة          | Cloud Storage: `com.google.cloud.storage`، طرق لسرد buckets، إدارة الكائنات.       |

يضمن هذا الدليل الشامل أن يكون لدى المطورين جميع المعلومات اللازمة لاستخدام `com.google.cloud` في جافا بفعالية، معالجة الإعداد، والمصادقة، والاستخدام، والميزات المتقدمة، مع الإشارة إلى مصادر موثوقة لمزيد من الاستكشاف.

#### الاقتباسات الرئيسية
- [مستودع Google Cloud Java client libraries على GitHub - كود وتفاصيل إعداد مفصلة](https://github.com/googleapis/google-cloud-java)
- [وثائق Google Cloud لنظرة عامة على تطوير جافا](https://cloud.google.com/products/anthos)
- [برنامج تعليمي على Baeldung حول Google Cloud Storage مع جافا - أمثلة عملية](https://www.baeldung.com/java-google-cloud-storage)