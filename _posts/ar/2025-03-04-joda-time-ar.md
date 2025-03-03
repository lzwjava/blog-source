---
audio: false
generated: true
lang: ar
layout: post
title: تاريخ ووقت العمليات في جافا
translated: true
---

### النقاط الرئيسية
- يبدو أن استخدام `org.joda.time` يتطلب إضافته إلى مشروعك Java وإدخال فئاته لعمليات التاريخ والوقت.
- تشير الأبحاث إلى إضافة المكتبة عبر Maven باستخدام الإصدار 2.13.1 أو تحميل ملف JAR، ثم استخدام الفئات مثل `DateTime` و `LocalDate`.
- تشير الأدلة إلى أن Joda-Time مفيدة في معالجة المناطق الزمنية، أنظمة التقويم، والفترات الزمنية، مع أمثلة مثل إنشاء كائنات التاريخ وتعديلها.

### ما هو Joda-Time وكيفية إعداده
Joda-Time هي مكتبة لتعامل مع التاريخ والوقت في Java، خاصة قبل Java 8، وتقدم واجهة برمجة (API) مفهومة لتحل محل الفئات القديمة الأقل أمانًا للخيوط `Date` و `Calendar`. لتستخدمها، أضف أولًا المكتبة إلى مشروعك. إذا كنت تستخدم Maven، أضف هذا التبعية إلى ملف `pom.xml`:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
بدلاً من ذلك، قم بتحميل ملف JAR من [هذا الموقع](https://www.joda.org/joda-time/download.html) واضفه إلى مسار تصنيفات مشروعك، مثل في Eclipse بإنشاء مجلد "libs" وربط JAR عبر خصائص المشروع.

### أمثلة الاستخدام الأساسي
بعد إعدادها، قم بإدخال الفئات مثل `org.joda.time.DateTime` أو `org.joda.time.LocalDate`. إليك بعض الأمثلة:
- إنشاء تاريخ-وقت الحالي: `DateTime now = new DateTime();`
- الوصول إلى الحقول: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- التعديل: `DateTime future = now.plusDays(5);`

### الميزات المتقدمة
Joda-Time يدعم المناطق الزمنية (مثل `DateTimeZone.forID("America/New_York")`) و أنظمة التقويم المختلفة (مثل Coptic عبر `CopticChronology.getInstance()`). كما أنها تتعامل مع الفترات والمدة، مثل `Interval interval = new Interval(startDt, endDt);`.

تفصيل غير متوقع هو أن Joda-Time تعتبر مشروعًا "مكتملًا"، مع توصية باستخدام حزمة `java.time` في Java 8 للمشاريع الجديدة، ولكن تبقى ذات صلة للأنظمة القديمة أو الاحتياجات الخاصة.

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام `org.joda.time`

يقدم هذا القسم استكشافًا مفصلًا لاستخدام مكتبة `org.joda.time`، ويوسع على الإجابة المباشرة مع سياق إضافي وعمق فني، مناسب للمطورين الذين يبحثون عن فهم شامل. يتضمن إعدادًا، أمثلة استخدام، ميزات رئيسية، وموارد إضافية، مما يضمن مرجعًا شاملًا للتطبيق.

#### مقدمة إلى Joda-Time
Joda-Time، التي طورتها joda.org، هي مكتبة معالجة التاريخ والوقت شائعة الاستخدام، خاصة قبل إصدار Java 8. وهي تتعامل مع مشاكل التصميم في فئات Java `Date` و `Calendar`، مثل المخاوف المتعلقة بالأمان على الخيوط، باستخدام فئات غير قابلة للتغيير. قبل Java 8، كانت فئة `Date` و `SimpleDateFormatter` غير آمنة على الخيوط، وكان عمليات مثل يوم/شهر/سنة غير مفهومة (مثل يوم يبدأ من 0، شهر يبدأ من 1، يتطلب `Calendar`). Joda-Time تقدم واجهة برمجة (API) نظيفة، وذات تدفق، وتدعم ثمانية أنظمة تقويم مقارنة باثنتين في Java (الغريغوري والياباني الإمبراطوري). بعد Java 8، يعتبر المؤلفون Joda-Time بشكل عام مكتملًا، ويوصون بالهجرة إلى `java.time` (JSR-310) للمشاريع الجديدة، ولكن تبقى ذات صلة للأنظمة القديمة أو الحالات الخاصة.

#### إعداد Joda-Time
لتستخدم Joda-Time، يجب أولاً إضافته إلى مشروعك Java. أحدث إصدار حتى 3 مارس 2025 هو 2.13.1، مما يضمن الاستقرار والتوافق مع JDK 1.5 أو أحدث. للمستخدمين Maven، أضف التبعية التالية إلى ملف `pom.xml`:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
يمكن العثور عليها على [مستودع Maven](https://mvnrepository.com/artifact/joda-time/joda-time). للمشاريع غير Maven، قم بتحميل ملف `.tar.gz` من [هذا الموقع](https://www.joda.org/joda-time/download.html)، استخرجه، واضف `joda-time-2.13.1.jar` إلى مسار تصنيفات مشروعك. على سبيل المثال، في Eclipse، قم بإنشاء مجلد "libs"، نسخ JAR، وربطه عبر Properties -> Java Build Path -> Libraries -> Add Jars. اختبر إعدادك مع `DateTime test = new DateTime();` لضمان الوظيفة.

#### الاستخدام الأساسي والأمثلة
بعد إضافته، قم بإدخال الفئات من `org.joda.time`، مثل `DateTime`، `LocalDate`، `LocalTime`، و `LocalDateTime`، جميعها غير قابلة للتغيير لأمان الخيوط. إليك أمثلة مفصلة:

- **إنشاء كائنات التاريخ والوقت:**
  - من الوقت الحالي: `DateTime now = new DateTime();` يستخدم المنطقة الزمنية الافتراضية و التقويم ISO.
  - من `Date` في Java: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` للتوافق.
  - من قيم محددة: يمكن أن يقبل المبدعين `Long` (ملي ثانية)، `String` (ISO8601)، أو كائنات Joda-Time أخرى، مثل `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **الوصول إلى الحقول:**
  - استخدم طرق الحصول: `int year = now.getYear(); int month = now.getMonthOfYear();` حيث يبدأ يناير من 1 ويصل ديسمبر إلى 12.
  - للحصول على تمثيل نصي: `String dayName = now.dayOfWeek().getAsText();` ينتج، على سبيل المثال، "Monday" لـ 3 مارس 2025.
  - التحقق من الخصائص: `boolean isLeap = now.year().isLeap();` ينتج `false` لـ 2025.

- **تعديل التاريخ والوقت:**
  - إنشاء نسخ جديدة مع التعديلات: `DateTime newDt = now.withYear(2025);` أو `DateTime future = now.plusDays(5);`.
  - إضافة مدات: `DateTime later = now.plusHours(2);` لإضافة ساعتين، ينتج نسخة جديدة.

أمثلة عملية من GeeksforGeeks توضح الاستخدام:
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Current Day: " + now.dayOfWeek().getAsText());
        System.out.println("Current Month: " + now.monthOfYear().getAsText());
        System.out.println("Current Year: " + now.year().getAsText());
        System.out.println("Current Year is Leap Year: " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
لـ 3 مارس 2025، قد يتضمن الناتج "Current Day: Monday"، "Current Month: March"، "Current Year: 2025"، "Current Year is Leap Year: false"، وTimestamp مثل "2025-03-03T08:39:00.000".

#### الميزات الرئيسية واستخدام متقدم
Joda-Time تقدم ميزات قوية لعمليات التاريخ والوقت المعقدة، كما يلي:

- **المناطق الزمنية:**
  - يديرها `DateTimeZone`، يدعم المناطق المسماة (مثل "Asia/Tokyo") و العوائد الثابتة. مثال:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - المنطقة الافتراضية تتطابق مع JDK، ولكن يمكن تجاوزها مع `DateTimeZone.setDefault(zone);`. يتم تحديث بيانات المنطقة الزمنية يدويًا عدة مرات في السنة، بناءً على [global-tz](https://github.com/JodaOrg/global-tz).

- **أنظمة التقويم:**
  - يدعم سبعة أنظمة: البوذية، القبطية، الإثيوبية، الغريغورية، الغريغورية اليولية، الإسلامية، اليولية، مع توفير أنظمة مخصصة. مثال:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - الافتراضية هي التقويم ISO، غير دقيقة تاريخيًا قبل 1583، ولكن مناسبة للاستخدام المدني الحديث.

- **الفترات والمدة:**
  - `Interval`: يمثل نطاقًا زمنيًا، نصف مفتوح (البداية شاملة، النهاية غير شاملة)، مثل `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: زمن دقيق في الملي ثانية، مثل `Duration duration = new Duration(interval);`، مفيد لإضافة إلى الأوقات.
  - `Period`: محدد في الحقول (سنوات، أشهر، أيام، إلخ.)، غير دقيق في الملي ثانية، مثل `Period period = new Period(startDt, endDt);`. مثال الفرق: إضافة يوم واحد في الحفظ الصيفي (مثل 2005-03-26 12:00:00) مع `plus(Period.days(1))` يضيف 23 ساعة، بينما `plus(new Duration(24L*60L*60L*1000L))` يضيف 24 ساعة، مما يوضح سلوك الفترة مقابل المدة.

يقدم دليل البداية السريعة جدولًا يوضح الفئات الرئيسية واستخداماتها:
| **الجانب**                  | **التفاصيل**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **الفئات الرئيسية للوقت**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 فئات، جميعها غير قابلة للتغيير)               |
| **حالة استخدام Instant**         | Timestamp لمؤتمر، بدون نظام تقويم أو منطقة زمنية                                          |
| **حالة استخدام LocalDate**       | تاريخ الميلاد، بدون وقت يوم                                                           |
| **حالة استخدام LocalTime**       | وقت يوم، مثل فتح/غلق متجر، بدون تاريخ                                               |
| **حالة استخدام DateTime**        | الغرض العام، يحل محل JDK Calendar، يتضمن معلومات المنطقة الزمنية                          |
| **أنواع المبدعين**        | المبدع يقبل: Date, Calendar, String (ISO8601), Long (ملي ثانية), فئات Joda-Time |
| **مثال التحويل**       | `java.util.Date` إلى `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **طرق الوصول إلى الحقل**     | `getMonthOfYear()` (1=يناير، 12=ديسمبر)، `getYear()`                                        |
| **طرق التعديل**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **مثال طرق الخصائص**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **نظام التقويم الافتراضي**  | نظام التقويم ISO (التقويم المدني الفعلي، غير دقيق تاريخيًا قبل 1583)              |
| **المنطقة الزمنية الافتراضية**        | نفس JDK الافتراضية، يمكن تجاوزها                                                         |
| **فئة Chronology**         | يدعم أنظمة التقويم متعددة، مثل `CopticChronology.getInstance()`                     |
| **مثال المنطقة الزمنية**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **فئة Interval**           | `Interval` - يحتفظ بالبداية والنهاية للوقت، العمليات بناءً على النطاق                          |
| **فئة Period**             | `Period` - يحتفظ بفترة مثل 6 أشهر، 3 أيام، 7 ساعات، يمكن استخلاصها من الفاصل               |
| **فئة Duration**           | `Duration` - مدة دقيقة في الملي ثانية، يمكن استخلاصها من الفاصل                          |
| **مثال الفترة مقابل المدة**| إضافة يوم واحد في الحفظ الصيفي (2005-03-26 12:00:00): `plus(Period.days(1))` يضيف 23 ساعة، `plus(new Duration(24L*60L*60L*1000L))` يضيف 24 ساعة |

تفصيل مثير للاهتمام هو قابلية توسيع المبدعين، مما يسمح بتحويل من JDK `Date` أو `Calendar` عن طريق تمريرهما مباشرة، مما يسهل الهجرة من الكود القديم.

#### مزيد من التعلم والموارد
للمزيد من الاستكشاف، استعرض الوثائق الرسمية في [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html)، التي تغطي المواضيع المتقدمة مثل الترميز والتحليل. يقدم دليل البداية السريعة في [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) مقدمة موجزة. متاحات دروس إضافية على [Baeldung Joda-Time](https://www.baeldung.com/joda-time) و [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/)، مع أمثلة الكود وإرشادات الإعداد. وثائق API في [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) مفيدة للمرجع، ولكن أكثر تقنيًا.

#### الخاتمة
Joda-Time تقدم بديلًا قويًا وآمنًا على الخيوط لعمليات التاريخ والوقت، مع دعم شامل للمناطق الزمنية، أنظمة التقويم، وحساب الوقت. بينما تعتبر مكتملة بعد Java 8، تبقى ذات صلة للأنظمة القديمة، مع إعدادها عبر Maven أو إضافة JAR يدويًا، واستخدامها عبر الفئات غير قابلة للتغيير مثل `DateTime` و `LocalDate`. يضمن هذا الدليل أن للمطورين جميع المعلومات اللازمة للتطبيق، من أمثلة أساسية إلى ميزات متقدمة، مع دعم موارد شاملة.