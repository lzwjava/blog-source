---
audio: false
generated: true
lang: ar
layout: post
title: Google Cloud Java Client
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام `com.google.cloud` في Java يتطلب إعداد بيئة تطوير Java، إضافة متطلبات مكتبة عملاء Google Cloud، تكوين مصادقة، واستخدام المكتبات للتفاعل مع خدمات Google Cloud.
- تشير الأبحاث إلى أن المصادقة يمكن أن يتم التعامل معها تلقائيًا على منصات Google Cloud أو يمكن إعدادها يدويًا للتنمية المحلية باستخدام بيانات اعتماد الحساب الخدمة.
- يشير الدليل إلى استخدام Maven أو Gradle لإدارة المتطلبات، مع تقديم أمثلة لاستخدام التخزين السحابي كحالة استخدام شائعة.

### إعداد بيئة تطويرك
لبدء العمل، تأكد من أن لديك Java Development Kit (JDK) الإصدار 8 أو أعلى مع أداة بناء مثل Maven أو Gradle. تساعد هذه الأدوات في إدارة متطلبات مشروعك وعمليات البناء.

### إضافة المتطلبات
أضف متطلبات مكتبة عملاء Google Cloud إلى مشروعك. بالنسبة لمaven، أضف قائمة المواد (BOM) والمكتبات الخدمية المحددة في ملف `pom.xml` الخاص بك. على سبيل المثال، لاستخدام التخزين السحابي:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

استبدل "latest_version" بالنسخة الفعلية من [مستودع GitHub لمكتبات عملاء Google Cloud Java](https://github.com/googleapis/google-cloud-java).

### تكوين المصادقة
يتم التعامل مع المصادقة تلقائيًا إذا كان تطبيقك يعمل على منصات Google Cloud مثل Compute Engine أو App Engine. للتنمية المحلية، قم بإعداد المتغير البيئي `GOOGLE_APPLICATION_CREDENTIALS` ليشير إلى ملف مفتاح JSON لحساب الخدمة، أو قم بتكوينه برمجيًا.

### استخدام المكتبات
بعد الإعداد، قم بإستيراد الفئات اللازمة، إنشاء كائن خدمة، وإجراء استدعاءات API. على سبيل المثال، لاقتران حاويات في التخزين السحابي:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

تفصيل غير متوقع هو أن المكتبات تدعم خدمات Google Cloud المختلفة، لكل منها حزمة فرعية تحت `com.google.cloud` مثل `com.google.cloud.bigquery` لـ BigQuery، وتقدم وظائف شاملة أكثر من التخزين.

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام `com.google.cloud` في Java

تقدم هذه الملاحظة استكشافًا مفصلًا لاستخدام مكتبات عملاء Google Cloud Java، مع التركيز بشكل خاص على حزمة `com.google.cloud` للتفاعل مع خدمات Google Cloud. تتوسع هذه الملاحظة على الإجابة المباشرة من خلال تضمين جميع التفاصيل ذات الصلة من البحث، مع تنظيمها للوضوح والعمق، مما يجعلها مناسبة للمطورين الذين يبحثون عن فهم شامل.

#### مقدمة لمكتبات عملاء Google Cloud Java
توفر مكتبات عملاء Google Cloud Java، التي يمكن الوصول إليها تحت حزمة `com.google.cloud`، واجهات مفهومة ومباشرة للتفاعل مع خدمات Google Cloud مثل Cloud Storage، BigQuery، وCompute Engine. تم تصميم هذه المكتبات لتقلل من الكود التكراري، التعامل مع تفاصيل الاتصال المنخفضة، والتكامل بشكل سلس مع ممارسات تطوير Java. وهي مفيدة بشكل خاص لبناء تطبيقات موجهة إلى السحاب، واستخدام أدوات مثل Spring، Maven، وKubernetes، كما هو موضح في الوثائق الرسمية.

#### إعداد بيئة التطوير
لبدء العمل، يتطلب Java Development Kit (JDK) الإصدار 8 أو أعلى، مما يضمن التوافق مع المكتبات. التوزيع المفضل هو Eclipse Temurin، خيار مفتوح المصدر، معتمد على Java SE TCK، كما هو موضح في دليلات الإعداد. بالإضافة إلى ذلك، أداة بناء التلقائية مثل Maven أو Gradle ضرورية لإدارة المتطلبات. يمكن أيضًا تثبيت Google Cloud CLI (`gcloud`) للتفاعل مع الموارد من سطر الأوامر، مما يسهل عمليات النشر والتتبع.

#### إدارة المتطلبات
يتم تسهيل إدارة المتطلبات باستخدام قائمة المواد (BOM) التي تقدمها Google Cloud، والتي تساعد في إدارة الأصدارات عبر عدة مكتبات. بالنسبة لمaven، أضف التالي إلى ملف `pom.xml`:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
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

للغرادل، يتم تطبيق التكوينات المماثلة، مما يضمن توافق الأصدارات. يجب التحقق من رقم الإصدار ضد [مستودع GitHub لمكتبات عملاء Google Cloud Java](https://github.com/googleapis/google-cloud-java) للحصول على أحدث التحديثات. يوضح هذا المستودع أيضًا منصات الدعم، بما في ذلك x86_64، Mac OS X، Windows، وLinux، ولكن يوضح قيودًا على Android وRaspberry Pi.

#### آليات المصادقة
تعتبر المصادقة خطوة حاسمة، مع اختلاف الخيارات حسب البيئة. على منصات Google Cloud مثل Compute Engine، Kubernetes Engine، أو App Engine، يتم استنتاج المعطيات تلقائيًا، مما يسهل العملية. بالنسبة للبيئات الأخرى، مثل التنمية المحلية، متاحات الطرق التالية:

- **حساب الخدمة (الموصى به):** انشئ ملف مفتاح JSON من Google Cloud Console واعد المتغير البيئي `GOOGLE_APPLICATION_CREDENTIALS` إلى مساره. أو قم بتحميله برمجيًا:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **التطوير المحلي/التجربة:** استخدم Google Cloud SDK مع `gcloud auth application-default login` للحصول على بيانات اعتماد مؤقتة.
- **رمز OAuth2 الحالي:** استخدم `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` للحالات الخاصة.

يتبع ترتيب الأولوية لمحدد معرف المشروع خيارات الخدمة، المتغير البيئي `GOOGLE_CLOUD_PROJECT`، App Engine/Compute Engine، ملف بيانات اعتماد JSON، وGoogle Cloud SDK، مع `ServiceOptions.getDefaultProjectId()` يساعد في استنتاج معرف المشروع.

#### استخدام مكتبات العملاء
بعد إعداد المتطلبات والمصادقة، يمكن للمطورين استخدام المكتبات للتفاعل مع خدمات Google Cloud. لكل خدمة حزمة فرعية تحت `com.google.cloud` مثل `com.google.cloud.storage` للتخزين السحابي أو `com.google.cloud.bigquery` لـ BigQuery. voici un exemple détaillé pour le stockage en nuage:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

يستمر هذا المثال في قائمة جميع الحاويات، ولكن المكتبة تدعم عمليات مثل تحميل الكائنات، تنزيل الملفات، وإدارة سياسات الحاوية. بالنسبة للخدمات الأخرى، تتبع الأنماط المماثلة، مع طرق مفصلة متاحة في الوثائق الخاصة بها، مثل تلك لـ BigQuery في [وثائق مرجع Google Cloud Java](https://googleapis.dev/java/google-cloud-clients/latest/).

#### ميزات متقدمة والتفاصيل
تدعم المكتبات ميزات متقدمة مثل العمليات المستمرة (LROs) باستخدام `OperationFuture`، مع توقيتات وإعادة المحاولات قابلة للتكوين. على سبيل المثال، AI Platform (v3.24.0) تتضمن تأخير إعادة المحاولة الأولي 5000ms، مضاعف 1.5، تأخير إعادة المحاولة الأقصى 45000ms، ووقت إتمام إجمالي 300000ms. يدعم أيضًا تكوين الوكيل باستخدام `https.proxyHost` و`https.proxyPort` لـ HTTPS/gRPC، مع خيارات مخصصة لـ gRPC عبر `ProxyDetector`.

توفر المصادقة باستخدام مفتاح API لبعض APIs، يتم تعيينها يدويًا عبر الرؤوس لـ gRPC أو REST، كما هو موضح في أمثلة خدمة اللغة. تسهل الاختبارات باستخدام الأدوات الموفرة، مع تفاصيل في مستودع TESTING.md، وplugins IDE لـ IntelliJ وEclipse لتحسين التطوير مع تكامل المكتبات.

#### منصات الدعم والقيود
تتوافق المكتبات مع منصات مختلفة، مع عمل عملاء HTTP في كل مكان، وعميل gRPC مدعوم على x86_64، Mac OS X، Windows، وLinux. ومع ذلك، لا يدعمها على Android، Raspberry Pi، أو App Engine Standard Java 7، باستثناء Datastore، Storage، وBigQuery. تشمل البيئات المدعومة Windows x86_64، Mac OS X x86_64، Linux x86_64، GCE، GKE، GAE Std J8، GAE Flex، وAlpine Linux (Java 11+).

#### الموارد والمزيد من القراءة
للإرشاد الإضافي، يقدم [مستودع GitHub لمكتبات عملاء Google Cloud Java](https://github.com/googleapis/google-cloud-java) أمثلة الكود، دليلات المساهمة، وموارد حل المشكلات. تقدم الدروس التعليمية مثل تلك على [Baeldung](https://www.baeldung.com/java-google-cloud-storage) أمثلة عملية مثل استخدام التخزين السحابي، بينما تغطي الوثائق الرسمية على [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) مفاهيم تطوير التطبيقات الأوسع.

#### جدول: تفاصيل التكوين الرئيسية

| **الجانب**               | **التفاصيل**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| إصدار Java             | يتطلب Java 8 أو أعلى.                                                                       |
| إدارة المتطلبات    | استخدم BOM للحصول على توافق الأصدارات، مثل Maven `libraries-bom`.                                  |
| آليات المصادقة   | تلقائي على GCE/GKE/GAE، يدويًا عبر `GOOGLE_APPLICATION_CREDENTIALS` أو برمجي.          |
| منصات الدعم      | عملاء HTTP في كل مكان، gRPC على x86_64، Mac OS X، Windows، Linux؛ لا على Android، Raspberry Pi.|
| خدمة مثال          | التخزين السحابي: `com.google.cloud.storage`، طرق لاقتران الحاوية، إدارة الكائنات.       |

يضمن هذا الدليل الشامل أن للمطورين جميع المعلومات اللازمة لاستخدام `com.google.cloud` في Java بشكل فعال، مع معالجة الإعداد، المصادقة، الاستخدام، والميزات المتقدمة، مع مراجع إلى مصادر رسمية للاستكشاف الإضافي.

#### الإشارات الرئيسية
- [مستودع GitHub لمكتبات عملاء Google Cloud Java مع تفاصيل الكود والإعداد](https://github.com/googleapis/google-cloud-java)
- [وثائق Google Cloud لتطوير Java نظرة عامة](https://cloud.google.com/products/anthos)
- [دروس تعليمية Baeldung على تخزين Google Cloud مع Java أمثلة عملية](https://www.baeldung.com/java-google-cloud-storage)