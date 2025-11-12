---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट में प्रॉपर्टीज़ कैसे काम करती हैं
translated: true
type: note
---

आइए जानें कि Spring Boot में properties कैसे काम करती हैं, जिसमें YAML या `.properties` फ़ाइलों का उपयोग कैसे करें, कमांड-लाइन arguments (जैसे `-D`) के साथ उन्हें कैसे override करें, properties को initialize करने के विभिन्न तरीके, और उन्हें प्रभावी ढंग से test कैसे करें शामिल है।

---

### **Spring Boot में Properties कैसे काम करती हैं**
Spring Boot, properties के माध्यम से application configuration को manage करने के लिए एक लचीली प्रणाली प्रदान करता है, जो key-value pairs होती हैं। इन properties को कई स्रोतों में परिभाषित किया जा सकता है, और Spring Boot एक विशिष्ट precedence order के आधार पर उन्हें resolve करता है। यह आपको विभिन्न environments या deployment scenarios के लिए अपने application को customize करने की अनुमति देता है। Properties **Spring Environment** में लोड हो जाती हैं, जिससे वे आपके application में हर जगह accessible होती हैं।

Properties के मुख्य स्रोतों में शामिल हैं:
- Configuration files (जैसे, `application.properties` या `application.yml`)
- Command-line arguments (जैसे, `--server.port=8081`)
- System properties (जैसे, `-Dserver.port=8081`)
- Environment variables
- Java code (जैसे, `@Value` या `@ConfigurationProperties` के माध्यम से)

---

### **YAML या Properties फ़ाइलों का उपयोग**
Spring Boot, configuration फ़ाइलों के लिए दो प्राथमिक formats का समर्थन करता है, दोनों आमतौर पर `src/main/resources` में रखी जाती हैं:

#### **1. `.properties` फ़ाइलें**
यह एक सरल, flat key-value format है:
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. `.yml` या `.yaml` फ़ाइलें**
यह एक structured, hierarchical format है जो indentation का उपयोग करता है:
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**मुख्य बिंदु:**
- सरल configurations के लिए `.properties` और nested या complex setups के लिए `.yml` का उपयोग करें।
- Environment-specific settings के लिए profile-specific files (जैसे, `application-dev.yml`) का उपयोग किया जा सकता है।
- उदाहरण: `server.port=8080` सेट करने से आपके Spring Boot application का port बदल जाता है।

---

### **Properties को Override करने के लिए Command-Line Arguments का उपयोग**
आप configuration files में परिभाषित properties को command-line arguments का उपयोग करके दो तरीकों से override कर सकते हैं:

#### **1. Spring Boot Properties के लिए `--` का उपयोग करना**
Application चलाते समय सीधे properties पास करें:
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
ये configuration files पर precedence लेते हैं।

#### **2. System Properties के लिए `-D` का उपयोग करना**
`-D` के साथ system properties सेट करें, जिन्हें Spring Boot भी पहचानता है:
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
System properties भी configuration file values को override करते हैं।

---

### **Properties को Initialize करने के विभिन्न तरीके**
Spring Boot, files और command-line arguments से परे properties को परिभाषित या initialize करने के लिए कई methods प्रदान करता है:

#### **1. Environment Variables**
Properties को environment variables के माध्यम से सेट किया जा सकता है। उदाहरण के लिए:
- अपने environment में `SERVER_PORT=8081` सेट करें, और Spring Boot इसे `server.port` पर map कर देता है।
- **Naming Convention:** Property names को uppercase में बदलें और dots (`.`) को underscores (`_`) से बदलें, उदाहरण के लिए, `spring.datasource.url` `SPRING_DATASOURCE_URL` बन जाता है।

#### **2. Java Code**
आप properties को programmatically initialize कर सकते हैं:
- **`@Value` का उपयोग करके**: एक विशिष्ट property को एक field में inject करें।
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **`@ConfigurationProperties` का उपयोग करके**: properties के एक group को एक Java object से bind करें।
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters and setters
  }
  ```
  यह `app.name` जैसी properties को `name` field से bind करता है।

#### **3. Default Values**
यदि कोई property परिभाषित नहीं है तो fallback values प्रदान करें:
- `@Value` में: `@Value("${server.port:8080}")` यदि `server.port` सेट नहीं है तो `8080` का उपयोग करता है।
- Configuration files में: `application.properties` या YAML में defaults सेट करें।

---

### **Property Precedence**
Spring Boot properties को कई स्रोतों से इस क्रम में resolve करता है (उच्च precedence निम्न को override करती है):
1. Command-line arguments (`--property=value`)
2. System properties (`-Dproperty=value`)
3. Environment variables
4. Configuration files (`application.properties` या `application.yml`)
5. Default values in code

**उदाहरण:** यदि `application.properties` में `server.port=8080` है लेकिन आप `java -jar myapp.jar --server.port=8081` चलाते हैं, तो port `8081` होगा।

---

### **Properties को कैसे Test करें**
Properties का testing यह सुनिश्चित करता है कि आपका application अपेक्षा के अनुरूप व्यवहार करता है। यहां सामान्य approaches दी गई हैं:

#### **1. `@TestPropertySource` का उपयोग करना**
Unit tests में properties को override करें:
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // Test code
}
```

#### **2. `application-test.properties` का उपयोग करना**
`src/test/resources` में एक test-specific file रखें:
```properties
server.port=9090
```
Spring Boot tests के दौरान इसे automatically लोड करता है।

#### **3. Programmatic Overrides**
Test setup में properties सेट करें:
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. `@ActiveProfiles` का उपयोग करना**
Profile-specific properties को activate करें:
- Test settings के साथ `application-test.yml` परिभाषित करें।
- उपयोग करें:
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // Test code
  }
  ```

---

### **सारांश**
- **Configuration Files**: Default settings के लिए `application.properties` या `application.yml` का उपयोग करें।
- **Command-Line Arguments**: `--property=value` या `-Dproperty=value` के साथ override करें।
- **Initialization Methods**: Environment variables, Java code (`@Value`, `@ConfigurationProperties`), या defaults का लाभ उठाएं।
- **Testing**: `@TestPropertySource`, test-specific files, programmatic overrides, या profiles का उपयोग करें।

यह Spring Boot में properties के साथ काम करने के मूल सिद्धांतों को कवर करता है। यदि आप और अधिक जानकारी चाहते हैं तो मुझे बताएं!