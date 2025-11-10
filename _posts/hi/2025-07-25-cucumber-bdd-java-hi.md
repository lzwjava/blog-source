---
audio: false
generated: true
image: false
lang: hi
layout: post
title: जावा डेवलपर्स के लिए कुकुम्बर बीडीडी गाइड
translated: true
type: note
---

यहाँ **Cucumber** का एक व्यावहारिक, एंड-टू-एंड परिचय दिया गया है — यह क्या है, टीमें इसका उपयोग क्यों करती हैं, और Java में इसके साथ उत्पादक कैसे बनें (साथ ही JS/Python उपयोगकर्ताओं के लिए त्वरित नोट्स)।

---

# Cucumber क्या है (और क्या नहीं है)

* **Cucumber** एक **BDD (Behavior-Driven Development)** टेस्ट फ्रेमवर्क है। यह आपको सादे भाषा (Gherkin) में व्यवहार का वर्णन करने और उन वाक्यों को निष्पादन योग्य कोड (step definitions) से बांधने देता है।
* यह आदर्श है जब आप उत्पाद, QA, और इंजीनियरिंग के बीच **साझा समझ**, और **लिविंग डॉक्यूमेंटेशन** चाहते हैं जो टेस्ट्स के रूप में भी काम करे।
* यह यूनिट टेस्टिंग फ्रेमवर्क (JUnit/TestNG/Jest/PyTest) का **प्रतिस्थापन नहीं** है। यह **बिजनेस-लेवल एक्सेप्टेंस टेस्ट्स** पर ध्यान केंद्रित करके उन्हें पूरक करता है।

---

# मुख्य भाग

**1) Gherkin (सादे-पाठ वाले स्पेक्स)**

* `.feature` फाइलों में लिखा जाता है।
* कीवर्ड: `Feature`, `Scenario`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`, `@tags`, (और वैकल्पिक रूप से नए Gherkin में `Rule`)।
* प्राकृतिक-भाषा शैली; कई लोकेल्स का समर्थन करता है।

**2) स्टेप डेफिनिशन्स (कोड)**

* **Cucumber Expressions** (या regex) के माध्यम से Gherkin स्टेप्स को कोड से बांधता है।
* पेज ऑब्जेक्ट्स, API क्लाइंट्स, सर्विसेज, DB हेल्पर्स, आदि को कॉल कर सकता है।

**3) रनर**

* Cucumber को शुरू करता है, ग्लू पाथ्स, कॉन्फ़िग और टैग्स द्वारा फीचर्स/स्टेप्स की खोज करता है।
* JVM पर, आप आमतौर पर **JUnit** (4 या 5) या **TestNG** के माध्यम से चलाते हैं।

**4) रिपोर्ट्स**

* HTML/JSON/JUnit XML जेनरेट करें; CI डैशबोर्ड और **Allure** जैसे टूल्स के साथ एकीकृत करें।

---

# न्यूनतम उदाहरण (Java, Maven)

**pom.xml (मुख्य अंश)**

```xml
<dependencies>
  <!-- JUnit 5 -->
  <dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
  </dependency>

  <!-- Cucumber JVM + JUnit Platform -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit-platform-engine</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <plugins>
    <plugin>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version>
      <configuration>
        <!-- run by tag, parallel, etc., if needed -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**प्रोजेक्ट लेआउट**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**एक फीचर फाइल (`src/test/resources/features/login.feature`)**

```gherkin
Feature: लॉगिन
  एक पंजीकृत उपयोगकर्ता के रूप में
  मैं साइन इन करना चाहता हूँ
  ताकि मैं अपने अकाउंट तक पहुंच सकूं

  Background:
    Given एप्लिकेशन चल रहा है

  @smoke
  Scenario: सफल लॉगिन
    Given मैं लॉगिन पेज पर हूं
    When मैं यूजरनेम "alice" और पासवर्ड "secret" के साथ साइन इन करता हूं
    Then मुझे "Welcome, alice" दिखाई देना चाहिए

  Scenario Outline: असफल लॉगिन
    Given मैं लॉगिन पेज पर हूं
    When मैं यूजरनेम "<user>" और पासवर्ड "<pass>" के साथ साइन इन करता हूं
    Then मुझे "Invalid credentials" दिखाई देना चाहिए
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**स्टेप डेफिनिशन्स (Java, Cucumber Expressions)**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("एप्लिकेशन चल रहा है")
  public void app_running() {
    // टेस्ट ऐप बूटस्ट्रैप करें / सर्वर शुरू करें / स्टेट रीसेट करें
  }

  @Given("मैं लॉगिन पेज पर हूं")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("मैं यूजरनेम {string} और पासवर्ड {string} के साथ साइन इन करता हूं")
  public void i_sign_in(String user, String pass) {
    // UI या API को कॉल करें; यहां नकली बनाएं:
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Welcome, alice";
    } else {
      message = "Invalid credentials";
    }
  }

  @Then("मुझे {string} दिखाई देना चाहिए")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**JUnit 5 रनर (इंजन द्वारा डिस्कवरी)**

```java
// JUnit Platform के साथ किसी एक्सप्लिसिट रनर क्लास की आवश्यकता नहीं है।
// यदि आप टैग फिल्टरिंग चाहते हैं तो एक टेस्ट सूट बनाएं:
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // उदाहरण
public class RunCucumberTest {}
```

चलाएं:

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# Gherkin के आवश्यक तत्व जो आप रोजाना उपयोग करेंगे

* **Background**: प्रति सिनैरियो सामान्य सेटअप (जैसे, "Given I'm logged in")।
* **Scenario Outline + Examples**: स्टेप्स को कॉपी-पेस्ट किए बिना डेटा-ड्रिवन टेस्ट्स।
* **Doc Strings**: स्टेप्स में मल्टीलाइन पेलोड (जैसे, JSON बॉडीज)।
* **Data Tables**: किसी स्टेप की टेबल को ऑब्जेक्ट्स या मैप्स में बदलें।
* **Tags**: CI पाइपलाइन्स के लिए सूट को स्लाइस करें (`@smoke`, `@api`, `@slow`)।
* **Rule** (वैकल्पिक): पठनीयता के लिए बिजनेस रूल द्वारा सिनैरियोस को ग्रुप करें।

---

# Cucumber Expressions (regex से अधिक मित्रवत)

* प्लेसहोल्डर्स जैसे `{string}`, `{int}`, `{word}`, `{float}`।
* **कस्टम पैरामीटर टाइप्स** आपको डोमेन ऑब्जेक्ट्स पार्स करने देते हैं:

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

फिर उपयोग करें: `When I pay 100 {currency}`।

---

# हुक्स और टेस्ट लाइफसाइकल

* JVM/JS/Ruby वेरिएंट में `@Before`, `@After`, `@BeforeStep`, `@AfterStep`।
* **क्लीन सेटअप/टीयरडाउन**, फेल्योर पर स्क्रीनशॉट्स, DB रीसेट्स, आदि के लिए हुक्स का उपयोग करें।
* DI के लिए, स्टेट शेयर करने के लिए **Spring** (cucumber-spring) या **PicoContainer** का उपयोग करें:

  * Spring Boot के साथ, स्टेप क्लासेज को बीन्स के रूप में एनोटेट करें; वायरिंग और आवश्यकतानुसार टेस्ट स्लाइस के लिए `@SpringBootTest` का उपयोग करें।

---

# एकीकरण जिनकी आपको संभावित आवश्यकता होगी

* **Web UI**: Selenium/WebDriver, Playwright। इन्हें **पेज ऑब्जेक्ट्स** में रैप करें और स्टेप्स से कॉल करें।
* **API**: REST Assured/HTTP क्लाइंट्स; JSON असेर्शन्स के साथ वैलिडेट करें।
* **DB**: स्कीमा के लिए Flyway/Liquibase, टेस्ट डेटा लोडर्स, एम्बेडेड DBs।
* **मॉकिंग**: एक्सटर्नल सिस्टम्स के लिए WireMock/Testcontainers।
* **रिपोर्टिंग**: बिल्ट-इन HTML/JSON; समृद्ध टाइमलाइन्स और अटैचमेंट्स के लिए **Allure**।
* **पैरेलल**: JUnit Platform (या पुराने स्टैक्स में TestNG के साथ `cucumber-jvm-parallel-plugin`)। सिनैरियोस को आइसोलेटेड रखें; शेयर्ड म्यूटेबल स्टेट से बचें।

---

# CI/CD और स्केलिंग

* **टैग-आधारित पाइपलाइन्स**: PRs पर `@smoke` चलाएं, दैनिक `@regression`, क्रॉन `@slow`।
* **गति के लिए एजेंट्स के बीच फाइल या टैग द्वारा शार्ड करें**।
* **आर्टिफैक्ट्स**: HTML/JSON/Allure और स्क्रीनशॉट्स/वीडियोज (UI) प्रकाशित करें।
* **फ्लैकी टेस्ट्स**: उनके मूल कारण का पता लगाएं — "हरा दिखाने के लिए रिट्राई" करके समस्या से न बचें।

---

# अच्छी प्रथाएं (बैटल-टेस्टेड)

* Gherkin में **एक स्वर**: स्टेप फ्रेजिंग को सुसंगत रखें; UI की बातचीत ("नीले बटन पर क्लिक करें") से बचें — **इरादे** ("क्रेडेंशियल्स सबमिट करें") पर ध्यान केंद्रित करें।
* **पतले स्टेप्स, मोटे हेल्पर्स**: स्टेप कोड को पेज ऑब्जेक्ट्स/सर्विसेज को डेलिगेट करना चाहिए; स्टेप्स से लॉजिक को बाहर रखें।
* **स्थिर टेस्ट डेटा**: APIs/DB फिक्स्चर्स के माध्यम से सीड करें; प्रोडक्शन-जैसी रैंडमनेस से कपलिंग से बचें।
* **तेज, स्वतंत्र सिनैरियो**: कोई ऑर्डरिंग धारणाएं नहीं; प्रति सिनैरियो साफ स्टेट।
* **सूट के आकार को सीमित रखें**: **बिजनेस व्यवहार** के लिए Cucumber को रिजर्व करें; निम्न-स्तरीय विवरणों के लिए यूनिट टेस्ट्स को JUnit/TestNG/Jest में रखें।

---

# एंटी-पैटर्न्स जिनसे बचना है

* Cucumber को एक सुंदर यूनिट टेस्ट रनर के रूप में मानना।
* लंबी प्रक्रियात्मक अनुक्रमों (इम्पेरेटिव, भंगुर) के साथ `And` का अत्यधिक उपयोग।
* स्टेप वर्डिंग में CSS सेलेक्टर्स या अस्थिर UI विवरणों से कपलिंग।
* विशाल Backgrounds जो छिपाती हैं कि प्रत्येक सिनैरियो को वास्तव में क्या चाहिए।

---

# अन्य भाषाओं के लिए त्वरित नोट्स

**JavaScript/TypeScript**

* **`@cucumber/cucumber`** का उपयोग करें।
* विशिष्ट स्क्रिप्ट्स:

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
* **Playwright** और **Allure** के साथ अच्छी तरह से काम करता है।

**Python**

* **behave** (Cucumber-जैसा) या **pytest-bdd** का उपयोग करें।
* संरचना और अवधारणाएं समान हैं: फीचर्स + स्टेप्स + फिक्स्चर्स।

**Ruby**

* मूल Cucumber इम्प्लीमेंटेशन; मुहावरे JVM और JS वर्जन को दर्पण करते हैं।

---

# Cucumber कब चुनें

* आप **लिविंग डॉक्यूमेंटेशन** चाहते हैं जो गैर-इंजीनियरों द्वारा पठनीय हो।
* स्वीकृति मानदंडों को **निष्पादन योग्य** और रिलीज से **ट्रेस करने योग्य** होने की आवश्यकता है।
* क्रॉस-फंक्शनल टीमें इम्प्लीमेंटेशन से **पहले** व्यवहार पर सहमत होती हैं (BDD triads)।

इसे छोड़ दें (या संयम से उपयोग करें) यदि टीम Gherkin को मेंटेन नहीं करेगी, या यदि टेस्ट्स पूरी तरह से तकनीकी हैं जहां यूनिट/इंटीग्रेशन टेस्ट्स पहले से ही स्पष्टता प्रदान करते हैं।

---

यदि आप मुझे अपना स्टैक बताएं (Spring/Quarkus? REST/UI? आप कैसे डिप्लॉय/CI करते हैं?), तो मैं Maven/Gradle, अनुशंसित प्लगइन्स और एक नमूना पाइपलाइन के साथ एक रन-रेडी Cucumber स्केलेटन बना सकता हूं जो आपके सेटअप के अनुरूप हो।