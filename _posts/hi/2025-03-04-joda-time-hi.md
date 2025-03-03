---
audio: false
generated: true
lang: hi
layout: post
title: Date aur Time Operations in Java
translated: true
---

### मुख्य बिंदु
- `org.joda.time` का उपयोग करने के लिए, इसे अपने Java प्रोजेक्ट में जोड़ना और डेट और टाइम ऑपरेशन के लिए इसके क्लासेज को इम्पोर्ट करना जरूरी लगता है।
- अनुसंधान का सुझाव है कि लाइब्रेरी को Maven के साथ 2.13.1 संस्करण के साथ शामिल करें या JAR फाइल डाउनलोड करें, फिर `DateTime` और `LocalDate` जैसे क्लासेज का उपयोग करें।
- सबूत यह दर्शाता है कि Joda-Time टाइम ज़ोन, कैलेंडर सिस्टम और टाइम इंटरवल्स को संभालने में उपयोगी है, जैसे कि डेट ऑब्जेक्ट बनाना और उन्हें संशोधित करना।

### Joda-Time क्या है और इसे कैसे सेट अप करें
Joda-Time एक लाइब्रेरी है जो Java में डेट और टाइम को संभालने के लिए है, विशेष रूप से Java 8 से पहले, जो एक सुलभ API प्रदान करता है जो पुराने, कम थ्रेड-सेफ `Date` और `Calendar` क्लासेज को बदलने के लिए है। इसे उपयोग करने के लिए, पहले लाइब्रेरी को प्रोजेक्ट में शामिल करें। अगर Maven का उपयोग कर रहे हैं, तो `pom.xml` में इस निर्भरता को जोड़ें:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
अल्टर्नेटिव रूप से, JAR फाइल को [इस वेबसाइट](https://www.joda.org/joda-time/download.html) से डाउनलोड करें और इसे प्रोजेक्ट के क्लासपाथ में जोड़ें, जैसे कि Eclipse में एक "libs" फोल्डर बनाकर और JAR को प्रोजेक्ट प्रॉपर्टीज के माध्यम से लिंक करके।

### बेसिक उपयोग उदाहरण
सेट अप के बाद, `org.joda.time.DateTime` या `org.joda.time.LocalDate` जैसे क्लासेज को इम्पोर्ट करें। यहाँ कुछ उदाहरण हैं:
- वर्तमान डेट-टाइम बनाएं: `DateTime now = new DateTime();`
- फ़ील्ड्स तक पहुंचें: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- संशोधित करें: `DateTime future = now.plusDays(5);`

### एडवांस्ड फीचर्स
Joda-Time टाइम ज़ोन (जैसे, `DateTimeZone.forID("America/New_York")`) और विभिन्न कैलेंडर सिस्टम (जैसे, Coptic के माध्यम से `CopticChronology.getInstance()`) का समर्थन करता है। यह इंटरवल्स और ड्यूरेशन जैसे `Interval interval = new Interval(startDt, endDt);` को भी संभालता है।

एक अनपेक्षित विवरण यह है कि Joda-Time को एक "समाप्त" प्रोजेक्ट माना जाता है, और नए प्रोजेक्टों के लिए Java 8 के `java.time` पैकेज का सुझाव दिया जाता है, लेकिन यह पुराने सिस्टमों या विशेष आवश्यकताओं के लिए अभी भी प्रासंगिक है।

---

### सर्वेक्षण नोट: `org.joda.time` का उपयोग करने का व्यापक मार्गदर्शिका

इस खंड में `org.joda.time` लाइब्रेरी का उपयोग करने का एक विस्तृत अन्वेषण शामिल है, जो सीधे उत्तर को विस्तारित करता है, साथ ही अतिरिक्त संदर्भ और तकनीकी गहराई के साथ, जो एक पूर्ण समझ के लिए विकसित करने वाले डेवलपर्स के लिए उपयुक्त है। इसमें सेट अप, उपयोग उदाहरण, मुख्य विशेषताएं और आगे के संसाधन शामिल हैं, जिससे एक पूर्ण संदर्भ प्रदान किया जाता है।

#### Joda-Time का परिचय
Joda-Time, जो joda.org द्वारा विकसित किया गया है, एक व्यापक रूप से उपयोग किया जाने वाला डेट और टाइम प्रोसेसिंग लाइब्रेरी है, विशेष रूप से Java 8 के रिलीज से पहले। यह Java `Date` और `Calendar` क्लासेज में डिजाइन समस्याओं को सुलझाता है, जैसे कि थ्रेड-सेफी चिंताओं, अनिम्यूटेबल क्लासेज का उपयोग करके। Java 8 से पहले, `Date` क्लास और `SimpleDateFormatter` थ्रेड-सेफ नहीं थे, और ऑपरेशन जैसे दिन/माह/साल ऑफसेट्स को गैर-प्राकृतिक माना जाता था (जैसे, दिन 0 से शुरू होते हैं, माह 1 से, `Calendar` की आवश्यकता होती है)। Joda-Time एक साफ, फ्लूएंट API प्रदान करता है और आठ कैलेंडर सिस्टम का समर्थन करता है, जबकि Java के केवल दो हैं (Gregorian और Japanese Imperial)। Java 8 के बाद, लेखकों ने Joda-Time को "लगभग समाप्त" माना है, नए प्रोजेक्टों के लिए `java.time` (JSR-310) पर माइग्रेशन का सुझाव दिया है, लेकिन यह पुराने सिस्टमों या विशेष उपयोग केसों के लिए अभी भी प्रासंगिक है।

#### Joda-Time सेट अप
Joda-Time का उपयोग करने के लिए, आपको पहले इसे अपने Java प्रोजेक्ट में शामिल करना होगा। मार्च 3, 2025 तक का नवीनतम संस्करण 2.13.1 है, जो JDK 1.5 या बाद के साथ स्थिरता और संगतता सुनिश्चित करता है। Maven उपयोगकर्ताओं के लिए, अपने `pom.xml` में निम्न निर्भरता जोड़ें:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
यह [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) पर मिल सकता है। नॉन-Maven प्रोजेक्टों के लिए, [इस वेबसाइट](https://www.joda.org/joda-time/download.html) से `.tar.gz` फाइल डाउनलोड करें, इसे एक्सट्रैक्ट करें, और `joda-time-2.13.1.jar` को प्रोजेक्ट के क्लासपाथ में जोड़ें। उदाहरण के लिए, Eclipse में, एक "libs" फोल्डर बनाएं, JAR को कॉपी करें, और इसे प्रॉपर्टीज -> Java Build Path -> Libraries -> Add Jars के माध्यम से लिंक करें। सेट अप को `DateTime test = new DateTime();` के साथ टेस्ट करें ताकि कार्यक्षमता सुनिश्चित हो सके।

#### बेसिक उपयोग और उदाहरण
शामिल होने के बाद, `org.joda.time` से क्लासेज को इम्पोर्ट करें, जैसे `DateTime`, `LocalDate`, `LocalTime`, और `LocalDateTime`, सभी थ्रेड-सेफी के लिए अनिम्यूटेबल हैं। यहाँ विस्तृत उदाहरण हैं:

- **डेट-टाइम ऑब्जेक्ट बनाना:**
  - वर्तमान समय से: `DateTime now = new DateTime();` डिफॉल्ट टाइम ज़ोन और ISO कैलेंडर का उपयोग करता है।
  - एक Java `Date` से: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` के लिए इंटरऑपरेबिलिटी।
  - विशेष मानों से: कंस्ट्रक्टर लंब (मिलिसेकंड), स्ट्रिंग (ISO8601), या अन्य Joda-Time ऑब्जेक्ट्स को स्वीकार करते हैं, उदाहरण के लिए, `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **फ़ील्ड्स तक पहुंचना:**
  - गेटर विधियों का उपयोग करें: `int year = now.getYear(); int month = now.getMonthOfYear();` जहाँ जनवरी 1 और दिसंबर 12 है।
  - पाठ्य प्रतिनिधित्व के लिए: `String dayName = now.dayOfWeek().getAsText();` मार्च 3, 2025 के लिए, उदाहरण के लिए, "Monday" का आउटपुट देता है।
  - गुणों की जांच करें: `boolean isLeap = now.year().isLeap();` 2025 के लिए `false` लौटाता है।

- **डेट-टाइम संशोधित करना:**
  - संशोधित किए गए नए इंस्टेंस बनाएं: `DateTime newDt = now.withYear(2025);` या `DateTime future = now.plusDays(5);`.
  - ड्यूरेशन जोड़ें: `DateTime later = now.plusHours(2);` दो घंटे जोड़ने के लिए, एक नया इंस्टेंस लौटाता है।

GeeksforGeeks से एक प्रैक्टिकल उदाहरण उपयोग का उदाहरण देता है:
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
मार्च 3, 2025 के लिए आउटपुट में "Current Day: Monday", "Current Month: March", "Current Year: 2025", "Current Year is Leap Year: false", और एक टाइमस्टैम्प जैसे "2025-03-03T08:39:00.000" शामिल हो सकता है।

#### मुख्य विशेषताएं और एडवांस्ड उपयोग
Joda-Time जटिल डेट-टाइम ऑपरेशन के लिए मजबूत विशेषताएं प्रदान करता है, निम्नलिखित रूप में विस्तारित:

- **टाइम ज़ोन:**
  - `DateTimeZone` के माध्यम से प्रबंधित, नामित ज़ोन (जैसे, "Asia/Tokyo") और फिक्स्ड ऑफसेट का समर्थन करता है। उदाहरण:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - डिफॉल्ट ज़ोन JDK के साथ मिलता है, लेकिन `DateTimeZone.setDefault(zone);` के साथ ओवरराइड किया जा सकता है। टाइम ज़ोन डेटा कई बार साल में, [global-tz](https://github.com/JodaOrg/global-tz) के आधार पर, मैन्युअल रूप से अपडेट किया जाता है।

- **कैलेंडर सिस्टम:**
  - सात सिस्टम का समर्थन करता है: बौद्ध, कॉप्टिक, एथियोपियन, ग्रेगोरियन, ग्रेगोरियनजुलियन, इस्लामिक, जुलियन, साथ ही कस्टम सिस्टम के लिए प्रावधान। उदाहरण:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - डिफॉल्ट ISO कैलेंडर पर, जो 1583 से पहले ऐतिहासिक रूप से गलत है, लेकिन आधुनिक नागरिक उपयोग के लिए उपयुक्त है।

- **इंटरवल्स, ड्यूरेशन, और पेरियड्स:**
  - `Interval`: एक टाइम रेंज का प्रतिनिधित्व करता है, आधा-खुला (शुरू शामिल, अंत अछ喝), उदाहरण के लिए, `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: मिलिसेकंड में एक सही समय, उदाहरण के लिए, `Duration duration = new Duration(interval);`, इंस्टेंट्स को जोड़ने के लिए उपयोगी।
  - `Period`: फ़ील्ड्स (वर्ष, माह, दिन, आदि.) में परिभाषित, मिलिसेकंड में अनिश्चित, उदाहरण के लिए, `Period period = new Period(startDt, endDt);`. उदाहरण अंतर: डेलीट सैविंग्स (जैसे, 2005-03-26 12:00:00) पर 1 दिन जोड़ने के लिए `plus(Period.days(1))` 23 घंटे जोड़ता है, जबकि `plus(new Duration(24L*60L*60L*1000L))` 24 घंटे जोड़ता है, पेरियड के विपरीत ड्यूरेशन व्यवहार को दर्शाता है।

क्विक स्टार्ट गाइड एक टेबल प्रदान करता है जो मुख्य क्लासेज और उपयोग केसों का सारांश देता है:
| **अस्पेक्ट**                  | **विवरण**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **मुख्य डेट-टाइम क्लासेज**   | इंस्टेंट, DateTime, LocalDate, LocalTime, LocalDateTime (5 क्लासेज, सभी अनिम्यूटेबल)               |
| **इंस्टेंट उपयोग केस**         | एक घटना का टाइमस्टैम्प, कोई कैलेंडर सिस्टम या टाइम-ज़ोन नहीं                                          |
| **LocalDate उपयोग केस**       | जन्म तिथि, दिन का समय की आवश्यकता नहीं                                                           |
| **LocalTime उपयोग केस**       | दिन का समय, उदाहरण के लिए, दुकान खुलने/बंद होने का समय, कोई तारीख नहीं                                               |
| **DateTime उपयोग केस**        | सामान्य उद्देश्य, JDK कैलेंडर को बदलता है, टाइम-ज़ोन जानकारी शामिल है                          |
| **कंस्ट्रक्टर प्रकार**        | ऑब्जेक्ट कंस्ट्रक्टर स्वीकार करता है: Date, Calendar, String (ISO8601), Long (milliseconds), Joda-Time क्लासेज |
| **उदाहरण परिवर्तन**       | `java.util.Date` से `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **फ़ील्ड एक्सेस विधियां**     | `getMonthOfYear()` (1=January, 12=December), `getYear()`                                        |
| **संशोधन विधियां**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **गुण विधियां उदाहरण**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **डिफॉल्ट कैलेंडर सिस्टम**  | ISO कैलेंडर सिस्टम (de facto नागरिक कैलेंडर, ऐतिहासिक रूप से 1583 से पहले गलत)              |
| **डिफॉल्ट टाइम-ज़ोन**        | JDK डिफॉल्ट के साथ मिलता है, ओवरराइड किया जा सकता है                                                         |
| **Chronology क्लास**         | कई कैलेंडर सिस्टम का समर्थन करता है, उदाहरण के लिए, `CopticChronology.getInstance()`                     |
| **टाइम-ज़ोन उदाहरण**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Interval क्लास**           | `Interval` - शुरू और अंत डेट-टाइम को रखता है, ऑपरेशन रेंज पर आधारित                          |
| **Period क्लास**             | `Period` - 6 माह, 3 दिन, 7 घंटे जैसे अवधि रखता है, इंटरवल से प्राप्त किया जा सकता है               |
| **Duration क्लास**           | `Duration` - मिलिसेकंड में एक सही अवधि, इंटरवल से प्राप्त किया जा सकता है                          |
| **Period vs Duration उदाहरण**| डेलीट सैविंग्स पर 1 दिन जोड़ने (2005-03-26 12:00:00): `plus(Period.days(1))` 23 घंटे जोड़ता है, `plus(new Duration(24L*60L*60L*1000L))` 24 घंटे जोड़ता है |

एक रुचिकर विवरण है ऑब्जेक्ट कंस्ट्रक्टर का विस्तार, जो JDK `Date` या `Calendar` को सीधे पास करके, पुराने कोड से माइग्रेशन को सरल बनाता है।

#### आगे की सीखने और संसाधन
गहन अन्वेषण के लिए, [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html) पर आधिकारिक दस्तावेज़ देखें, जो फॉर्मेटिंग और पार्सिंग जैसे उन्नत विषयों को कवर करता है। [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) पर क्विक स्टार्ट गाइड एक संक्षिप्त परिचय प्रदान करता है। अतिरिक्त ट्यूटोरियल [Baeldung Joda-Time](https://www.baeldung.com/joda-time) और [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) पर उपलब्ध हैं, साथ ही कोड उदाहरण और सेट अप निर्देश शामिल हैं। [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) पर API दस्तावेज़ तकनीकी संदर्भ के लिए उपयोगी हैं, हालांकि अधिक तकनीकी हैं।

#### निष्कर्ष
Joda-Time एक मजबूत, थ्रेड-सेफ विकल्प प्रदान करता है जो डेट और टाइम ऑपरेशन के लिए है, साथ ही टाइम ज़ोन, कैलेंडर सिस्टम और टाइम कैलकुलेशन का विस्तृत समर्थन है। Java 8 के बाद, इसे "समाप्त" माना जाता है, लेकिन यह पुराने सिस्टमों के लिए अभी भी मूल्यवान है, साथ ही Maven या मैन्युअल JAR शामिल करने के माध्यम से सेट अप, और अनिम्यूटेबल क्लासेज जैसे `DateTime` और `LocalDate` के माध्यम से उपयोग। यह गाइड सुनिश्चित करता है कि डेवलपर्स को सेट अप, बेसिक उदाहरणों से लेकर एडवांस्ड फीचर्स तक, सभी आवश्यक जानकारी के साथ प्रोडक्ट को लागू करने के लिए है।

### मुख्य सन्दर्भ
- [Joda-Time होम पेज के साथ सामान्य जानकारी](https://www.joda.org/joda-time/)
- [Joda-Time क्विक स्टार्ट गाइड नए उपयोगकर्ताओं के लिए](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung पर Joda-Time उपयोग ट्यूटोरियल](https://www.baeldung.com/joda-time)
- [GeeksforGeeks पर Joda-Time के साथ उदाहरणों वाला लेख](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time उपयोगकर्ता गाइड के लिए विस्तृत संदर्भ](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time डाउनलोड और इंस्टॉलेशन पेज](https://www.joda.org/joda-time/download.html)
- [Joda-Time निर्भरता के लिए Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API दस्तावेज़ के लिए तकनीकी संदर्भ](https://www.joda.org/joda-time/apidocs/index.html)