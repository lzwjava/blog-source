---
audio: false
generated: true
lang: hi
layout: post
title: जावा में तिथि और समय संचालन
translated: true
type: note
---

### मुख्य बिंदु
- ऐसा प्रतीत होता है कि `org.joda.time` का उपयोग करने के लिए, आपको इसे अपने Java प्रोजेक्ट में जोड़ना होगा और तिथि एवं समय संचालन के लिए इसके classes को import करना होगा।
- शोध से पता चलता है कि Maven के माध्यम से संस्करण 2.13.1 के साथ लाइब्रेरी को शामिल करना या JAR फ़ाइल डाउनलोड करना, फिर `DateTime` और `LocalDate` जैसे classes का उपयोग करना आवश्यक है।
- प्रमाण इस ओर इशारा करते हैं कि Joda-Time समय क्षेत्रों, कैलेंडर सिस्टम और समय अंतरालों को संभालने के लिए उपयोगी है, जिसमें तिथि objects बनाने और उन्हें संशोधित करने जैसे उदाहरण शामिल हैं।

### Joda-Time क्या है और इसे कैसे सेट अप करें
Joda-Time Java में तिथियों और समय को संभालने के लिए एक लाइब्रेरी है, विशेष रूप से Java 8 से पहले उपयोगी, जो पुराने, कम thread-safe `Date` और `Calendar` classes के स्थान पर एक सहज API प्रदान करती है। इसका उपयोग करने के लिए, पहले लाइब्रेरी को अपने प्रोजेक्ट में शामिल करें। यदि Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में यह dependency जोड़ें:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
वैकल्पिक रूप से, JAR फ़ाइल को [इस वेबसाइट](https://www.joda.org/joda-time/download.html) से डाउनलोड करें और इसे अपने प्रोजेक्ट के classpath में जोड़ें, जैसे Eclipse में "libs" फ़ोल्डर बनाकर और प्रोजेक्ट properties के माध्यम से JAR को लिंक करके।

### बुनियादी उपयोग के उदाहरण
एक बार सेट अप हो जाने पर, `org.joda.time.DateTime` या `org.joda.time.LocalDate` जैसे classes को import करें। यहां कुछ उदाहरण दिए गए हैं:
- वर्तमान तिथि-समय बनाएं: `DateTime now = new DateTime();`
- फ़ील्ड्स तक पहुंचें: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- संशोधित करें: `DateTime future = now.plusDays(5);`

### उन्नत सुविधाएँ
Joda-Time समय क्षेत्रों (जैसे, `DateTimeZone.forID("America/New_York")`) और विभिन्न कैलेंडर सिस्टम (जैसे, `CopticChronology.getInstance()` के माध्यम से Coptic) का समर्थन करता है। यह अंतराल और अवधि को भी संभालता है, जैसे `Interval interval = new Interval(startDt, endDt);`।

एक अप्रत्याशित विवरण यह है कि Joda-Time को एक "पूर्ण" प्रोजेक्ट माना जाता है, जिसमें Java 8 के `java.time` पैकेज की सिफारिश नए प्रोजेक्ट्स के लिए की जाती है, लेकिन यह अभी भी legacy systems या विशिष्ट आवश्यकताओं के लिए प्रासंगिक है।

---

### सर्वेक्षण नोट: `org.joda.time` का उपयोग करने के लिए व्यापक मार्गदर्शिका

यह खंड `org.joda.time` लाइब्रेरी का उपयोग करने का एक विस्तृत अन्वेषण प्रदान करता है, जो developers को पूर्ण समझ प्रदान करने के लिए अतिरिक्त संदर्भ और तकनीकी गहराई के साथ सीधे उत्तर पर विस्तार करता है। इसमें सेटअप, उपयोग के उदाहरण, मुख्य विशेषताएं और अतिरिक्त संसाधन शामिल हैं, जो कार्यान्वयन के लिए एक संपूर्ण संदर्भ सुनिश्चित करते हैं।

#### Joda-Time का परिचय
Joda-Time, joda.org द्वारा विकसित, एक व्यापक रूप से उपयोग की जाने वाली तिथि और समय प्रसंस्करण लाइब्रेरी है, विशेष रूप से Java 8 के रिलीज़ से पहले। यह Java `Date` और `Calendar` classes में डिज़ाइन संबंधी मुद्दों, जैसे thread-safety चिंताओं, को immutable classes का उपयोग करके संबोधित करती है। Java 8 से पहले, `Date` class और `SimpleDateFormatter` thread-safe नहीं थे, और दिन/महीना/वर्ष ऑफ़सेट जैसे ऑपरेशन counterintuitive थे (जैसे, दिन 0 से शुरू, महीने 1 से, जिसके लिए `Calendar` की आवश्यकता होती थी)। Joda-Time एक साफ, fluent API प्रदान करती है और आठ कैलेंडर सिस्टम का समर्थन करती है, जबकि Java के केवल दो (Gregorian और Japanese Imperial) हैं। Java 8 के बाद, लेखक Joda-Time को काफी हद तक पूर्ण मानते हैं, नए प्रोजेक्ट्स के लिए `java.time` (JSR-310) में माइग्रेशन की सिफारिश करते हैं, लेकिन यह legacy systems या विशिष्ट use cases के लिए प्रासंगिक बनी हुई है।

#### Joda-Time सेट करना
Joda-Time का उपयोग करने के लिए, आपको पहले इसे अपने Java प्रोजेक्ट में शामिल करना होगा। 3 मार्च, 2025 तक नवीनतम संस्करण 2.13.1 है, जो JDK 1.5 या बाद के संस्करणों के साथ स्थिरता और संगतता सुनिश्चित करता है। Maven उपयोगकर्ताओं के लिए, अपनी `pom.xml` में निम्नलिखित dependency जोड़ें:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
इसे [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) पर पाया जा सकता है। गैर-Maven प्रोजेक्ट्स के लिए, [इस वेबसाइट](https://www.joda.org/joda-time/download.html) से `.tar.gz` फ़ाइल डाउनलोड करें, इसे एक्सट्रैक्ट करें, और `joda-time-2.13.1.jar` को अपने प्रोजेक्ट के classpath में जोड़ें। उदाहरण के लिए, Eclipse में, एक "libs" फ़ोल्डर बनाएं, JAR को कॉपी करें, और Properties -> Java Build Path -> Libraries -> Add Jars के माध्यम से इसे लिंक करें। कार्यक्षमता सुनिश्चित करने के लिए `DateTime test = new DateTime();` के साथ सेटअप का परीक्षण करें।

#### बुनियादी उपयोग और उदाहरण
एक बार शामिल हो जाने पर, `org.joda.time` से classes को import करें, जैसे `DateTime`, `LocalDate`, `LocalTime`, और `LocalDateTime`, जो सभी thread safety के लिए immutable हैं। यहां विस्तृत उदाहरण दिए गए हैं:

- **तिथि-समय Objects बनाना:**
  - वर्तमान समय से: `DateTime now = new DateTime();` डिफ़ॉल्ट समय क्षेत्र और ISO कैलेंडर का उपयोग करता है।
  - Java `Date` से: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` अंतरसंचालनीयता के लिए।
  - विशिष्ट मानों से: कंस्ट्रक्टर्स `Long` (मिलीसेकंड), `String` (ISO8601), या अन्य Joda-Time objects स्वीकार करते हैं, उदा., `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`।

- **फ़ील्ड्स तक पहुंचना:**
  - Getter methods का उपयोग करें: `int year = now.getYear(); int month = now.getMonthOfYear();` जहां जनवरी 1 और दिसंबर 12 है।
  - पाठ्य प्रतिनिधित्व के लिए: `String dayName = now.dayOfWeek().getAsText();` आउटपुट करता है, उदा., 3 मार्च, 2025 के लिए "Monday"।
  - गुणों की जाँच करें: `boolean isLeap = now.year().isLeap();` 2025 के लिए `false` लौटाता है।

- **तिथि-समय संशोधित करना:**
  - संशोधनों के साथ नई instances बनाएं: `DateTime newDt = now.withYear(2025);` या `DateTime future = now.plusDays(5);`।
  - अवधि जोड़ें: `DateTime later = now.plusHours(2);` दो घंटे जोड़ने के लिए, एक नया instance लौटाता है।

GeeksforGeeks से एक व्यावहारिक उदाहरण उपयोग दर्शाता है:
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
3 मार्च, 2025 के लिए, आउटपुट में "Current Day: Monday", "Current Month: March", "Current Year: 2025", "Current Year is Leap Year: false", और एक टाइमस्टैम्प जैसे "2025-03-03T08:39:00.000" शामिल हो सकते हैं।

#### मुख्य विशेषताएं और उन्नत उपयोग
Joda-Time जटिल तिथि-समय संचालन के लिए मजबूत सुविधाएँ प्रदान करती है, जिनका विवरण निम्नलिखित है:

- **समय क्षेत्र:**
  - `DateTimeZone` के माध्यम से प्रबंधित, नामित क्षेत्रों (जैसे, "Asia/Tokyo") और fixed offsets का समर्थन करता है। उदाहरण:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - डिफ़ॉल्ट क्षेत्र JDK से मेल खाता है, लेकिन `DateTimeZone.setDefault(zone);` के साथ ओवरराइड किया जा सकता है। समय क्षेत्र डेटा अपडेट साल में कई बार मैन्युअल रूप से किए जाते हैं, [global-tz](https://github.com/JodaOrg/global-tz) पर आधारित।

- **कैलेंडर सिस्टम:**
  - सात सिस्टम का समर्थन करता है: Buddhist, Coptic, Ethiopic, Gregorian, GregorianJulian, Islamic, Julian, कस्टम सिस्टम के लिए प्रावधान के साथ। उदाहरण:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - डिफ़ॉल्ट रूप से ISO कैलेंडर, 1583 से पहले ऐतिहासिक रूप से गलत, लेकिन आधुनिक नागरिक उपयोग के लिए उपयुक्त।

- **अंतराल, अवधि और पीरियड:**
  - `Interval`: एक समय सीमा का प्रतिनिधित्व करता है, half-open (start inclusive, end exclusive), उदा., `Interval interval = new Interval(startDt, endDt);`।
  - `Duration`: मिलीसेकंड में सटीक समय, उदा., `Duration duration = new Duration(interval);`, instants में जोड़ने के लिए उपयोगी।
  - `Period`: फ़ील्ड्स (वर्ष, महीने, दिन, आदि) में परिभाषित, मिलीसेकंड में अशुद्ध, उदा., `Period period = new Period(startDt, endDt);`। उदाहरण अंतर: दिन के उजाले की बचत (जैसे, 2005-03-26 12:00:00) पर 1 दिन जोड़ना `plus(Period.days(1))` 23 घंटे जोड़ता है, जबकि `plus(new Duration(24L*60L*60L*1000L))` 24 घंटे जोड़ता है, जो period बनाम duration के व्यवहार पर प्रकाश डालता है।

क्विक स्टार्ट गाइड मुख्य classes और use cases को सारांशित करते हुए एक तालिका प्रदान करती है:
| **पहलू**                  | **विवरण**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **मुख्य तिथि-समय Classes**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 classes, सभी immutable)               |
| **Instant Use Case**         | किसी घटना का टाइमस्टैम्प, कोई कैलेंडर सिस्टम या समय-क्षेत्र नहीं                                          |
| **LocalDate Use Case**       | जन्म तिथि, दिन के समय की आवश्यकता नहीं                                                           |
| **LocalTime Use Case**       | दिन का समय, उदा., दुकान खुलने/बंद होने का समय, कोई तिथि नहीं                                               |
| **DateTime Use Case**        | सामान्य उद्देश्य, JDK Calendar को प्रतिस्थापित करता है, समय-क्षेत्र जानकारी शामिल करता है                          |
| **कंस्ट्रक्टर प्रकार**        | Object constructor स्वीकार करता है: Date, Calendar, String (ISO8601), Long (मिलीसेकंड), Joda-Time classes |
| **उदाहरण रूपांतरण**       | `java.util.Date` से `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **फ़ील्ड एक्सेस Methods**     | `getMonthOfYear()` (1=जनवरी, 12=दिसंबर), `getYear()`                                        |
| **संशोधन Methods**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **प्रॉपर्टी Methods उदाहरण**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **डिफ़ॉल्ट कैलेंडर सिस्टम**  | ISO कैलेंडर सिस्टम (डी फैक्टो नागरिक कैलेंडर, 1583 से पहले ऐतिहासिक रूप से गलत)              |
| **डिफ़ॉल्ट समय-क्षेत्र**        | JDK डिफ़ॉल्ट के समान, ओवरराइड किया जा सकता है                                                         |
| **क्रोनोलॉजी Class**         | एकाधिक कैलेंडर सिस्टम का समर्थन करता है, उदा., `CopticChronology.getInstance()`                     |
| **समय-क्षेत्र उदाहरण**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Interval Class**           | `Interval` - start और end तिथि-समय रखता है, संचालन सीमा पर आधारित                          |
| **Period Class**             | `Period` - period रखता है जैसे 6 महीने, 3 दिन, 7 घंटे, interval से प्राप्त किया जा सकता है               |
| **Duration Class**           | `Duration` - मिलीसेकंड में सटीक अवधि, interval से प्राप्त किया जा सकता है                          |
| **Period बनाम Duration उदाहरण**| दिन के उजाले की बचत (2005-03-26 12:00:00) पर 1 दिन जोड़ना: `plus(Period.days(1))` 23 घंटे जोड़ता है, `plus(new Duration(24L*60L*60L*1000L))` 24 घंटे जोड़ता है |

एक दिलचस्प विवरण object constructors की एक्स्टेंसिबिलिटी है, जो JDK `Date` या `Calendar` से रूपांतरण की अनुमति देती है by passing them directly, legacy code से माइग्रेशन को सरल बनाती है।

#### आगे की सीख और संसाधन
गहन अन्वेषण के लिए, आधिकारिक दस्तावेज़ [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html) से परामर्श करें, जो फ़ॉर्मेटिंग और पार्सिंग जैसे उन्नत विषयों को कवर करती है। [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) पर क्विक स्टार्ट गाइड एक संक्षिप्त परिचय प्रदान करती है। अतिरिक्त ट्यूटोरियल [Baeldung Joda-Time](https://www.baeldung.com/joda-time) और [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) पर उपलब्ध हैं, जिनमें कोड उदाहरण और सेटअप निर्देश शामिल हैं। [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) पर API दस्तावेज़ संदर्भ के लिए उपयोगी है, हालांकि अधिक तकनीकी है।

#### निष्कर्ष
Joda-Time तिथि और समय संचालन के लिए एक मजबूत, thread-safe विकल्प प्रदान करती है, जिसमें समय क्षेत्रों, कैलेंडर सिस्टम और समय गणनाओं के लिए व्यापक समर्थन शामिल है। जबकि Java 8 के बाद इसे पूर्ण माना जाता है, यह legacy systems के लिए मूल्यवान बनी हुई है, जिसमें Maven या मैन्युअल JAR समावेशन के माध्यम से सेटअप, और `DateTime` और `LocalDate` जैसे immutable classes के माध्यम से उपयोग शामिल है। यह मार्गदर्शिका developers के पास कार्यान्वयन के लिए आवश्यक सभी जानकारी सुनिश्चित करती है, बुनियादी उदाहरणों से लेकर उन्नत सुविधाओं तक, व्यापक संसाधनों द्वारा समर्थित।

### मुख्य उद्धरण
- [Joda-Time होम पेज सामान्य जानकारी के साथ](https://www.joda.org/joda-time/)
- [शुरुआती लोगों के लिए Joda-Time क्विक स्टार्ट गाइड](https://www.joda.org/joda-time/quickstart.html)
- [Joda-Time उपयोग पर Baeldung ट्यूटोरियल](https://www.baeldung.com/joda-time)
- [Joda-Time पर GeeksforGeeks लेख उदाहरणों के साथ](https://www.geeksforgeeks.org/joda-time/)
- [विस्तृत संदर्भ के लिए Joda-Time यूजर गाइड](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time डाउनलोड और इंस्टालेशन पेज](https://www.joda.org/joda-time/download.html)
- [Joda-Time Dependency के लिए Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time)
- [तकनीकी संदर्भ के लिए Joda-Time API दस्तावेज़](https://www.joda.org/joda-time/apidocs/index.html)