---
audio: false
generated: true
lang: hi
layout: post
title: चेकस्टाइल कॉन्फ़िग स्थान
translated: true
type: note
---

`maven-checkstyle-plugin` के साथ `mvn clean checkstyle:check` चलाते समय आपको `checks.xml` फ़ाइल नहीं मिलने और `SuppressWithNearbyTextFilter` मॉड्यूल को इनिशियलाइज़ करने में विफल होने की समस्याओं को ठीक करने के लिए, इन चरणों का पालन करें। ये समस्याएं फ़ाइल लोकेशन और एक असंगत Checkstyle वर्जन के कारण हो रही हैं। यहाँ एक पूर्ण समाधान है:

---

### चरण 1: `checks.xml` फ़ाइल लोकेशन ठीक करें
त्रुटि इंगित करती है कि प्लगइन `checks.xml` को नहीं ढूंढ पा रहा है। चूंकि यह आपके प्रोजेक्ट रूट पर स्थित है (`src/main/resources` में नहीं, जहां प्लगइन आमतौर पर देखता है), आपको प्लगइन को स्पष्ट रूप से बताना होगा कि इसे कहां ढूंढना है।

- **कार्रवाई**: अपने `pom.xml` में `<configLocation>` को प्रोजेक्ट रूट की ओर इंगित करने के लिए अपडेट करें।

---

### चरण 2: `SuppressWithNearbyTextFilter` त्रुटि को हल करें
`SuppressWithNearbyTextFilter` मॉड्यूल इसलिए इनिशियलाइज़ होने में विफल हो रहा है क्योंकि प्लगइन द्वारा उपयोग किया जाने वाला Checkstyle वर्जन पुराना है और इस फ़िल्टर का समर्थन नहीं करता है। आपको प्लगइन को अपग्रेड करना होगा और एक संगत Checkstyle वर्जन निर्दिष्ट करना होगा।

- **कार्रवाई**: `maven-checkstyle-plugin` को वर्जन `3.3.1` पर अपग्रेड करें और Checkstyle वर्जन `10.17.0` पर एक डिपेंडेंसी जोड़ें, जो `SuppressWithNearbyTextFilter` का समर्थन करता है।

---

### अपडेट की गई `pom.xml` कॉन्फ़िगरेशन
अपने `pom.xml` में `maven-checkstyle-plugin` सेक्शन को निम्नानुसार संशोधित करें:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- नवीनतम वर्जन पर अपग्रेड करें -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- प्रोजेक्ट रूट पर checks.xml की ओर इंगित करें -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- SuppressWithNearbyTextFilter का समर्थन करता है -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### स्पष्टीकरण:
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`**: निर्दिष्ट करता है कि `checks.xml` प्रोजेक्ट रूट पर है (`${project.basedir}` रूट डायरेक्टरी के लिए एक Maven प्रॉपर्टी है)।
- **`version 3.3.1`**: बेहतर कंपैटिबिलिटी के लिए एक नए प्लगइन वर्जन का उपयोग करता है।
- **Checkstyle `10.17.0` डिपेंडेंसी**: सुनिश्चित करता है कि प्लगइन एक ऐसे Checkstyle वर्जन का उपयोग करता है जिसमें `SuppressWithNearbyTextFilter` शामिल है।

---

### चरण 3: `checks.xml` कॉन्फ़िगरेशन सत्यापित करें
सुनिश्चित करें कि आपके `checks.xml` में `SuppressWithNearbyTextFilter` मॉड्यूल सही ढंग से परिभाषित है। एक उदाहरण कॉन्फ़िगरेशन इस तरह दिख सकता है:

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **कार्रवाई**: टाइपो या गलत प्रॉपर्टीज़ के लिए `checks.xml` की जाँच करें। विवरण के लिए [Checkstyle documentation](https://checkstyle.org/filters/suppresswithnearbytextfilter.html) देखें।
- **समस्या निवारण सुझाव**: यदि त्रुटि बनी रहती है, तो अस्थायी रूप से `SuppressWithNearbyTextFilter` मॉड्यूल को `checks.xml` से हटा दें और `mvn checkstyle:check` चलाकर देखें कि क्या समस्या इस specific फ़िल्टर से है।

---

### चरण 4: फिक्स का परीक्षण करें
- परीक्षण करने के लिए निम्न कमांड चलाएँ:
  ```bash
  mvn clean checkstyle:check
  ```
- यदि यह काम करता है, तो प्लगइन को `checks.xml` मिल जाना चाहिए और सभी मॉड्यूल को errors के बिना प्रोसेस करना चाहिए।
- यह सुनिश्चित करने के लिए कि Checkstyle कंपाइलेशन के दौरान चलता है, उपयोग करें:
  ```bash
  mvn compile
  ```

---

### वैकल्पिक: वैकल्पिक फ़ाइल लोकेशन
यदि आप एक अधिक मानक Maven सेटअप पसंद करते हैं:
- `checks.xml` को `src/main/resources/checks.xml` पर ले जाएँ।
- `<configLocation>` को अपडेट करें:
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- यह Maven के कन्वेंशन के साथ संरेखित करता है कि resources को `src/main/resources` में रखा जाता है।

---

### अतिरिक्त नोट्स
- **असंबंधित चेतावनी**: यदि आप `/usr/share/maven/conf/settings.xml` में `<blocked>` टैग के बारे में एक चेतावनी देखते हैं, तो यह इस मुद्दे से संबंधित नहीं है लेकिन आपकी Maven सेटिंग्स फ़ाइल में एक समस्या का सुझाव देता है। यदि आवश्यक हो तो इसे अलग से समीक्षा करें।
- **अभी भी समस्याएँ आ रही हैं?** आगे सहायता के लिए निम्नलिखित साझा करें:
  - `checks.xml` की सामग्री (या एक स्निपेट)।
  - `mvn clean checkstyle:check -X` (debug mode) का पूर्ण आउटपुट।

---

इन परिवर्तनों को लागू करके, `maven-checkstyle-plugin` को सही ढंग से `checks.xml` का पता लगाना चाहिए और `SuppressWithNearbyTextFilter` का समर्थन करना चाहिए, जिससे आपकी errors हल हो जाएंगी।

---

आपके द्वारा पहले आई त्रुटि ने संकेत दिया था कि `maven-checkstyle-plugin` classpath में `checks.xml` नहीं ढूंढ पा रहा था और फिर `SuppressWithNearbyTextFilter` मॉड्यूल के साथ एक समस्या के कारण विफल हो गया था। आपके अपडेट किए गए प्रोजेक्ट structure से, ऐसा प्रतीत होता है कि `checks.xml` प्रोजेक्ट रूट (`~/Projects/blog-server/checks.xml`) पर स्थित है, न कि `src/main/resources` में जैसा कि पहले माना गया था। यह बताता है कि जब प्लगइन `<configLocation>classpath:checks.xml</configLocation>` या `<configLocation>checks.xml</configLocation>` के साथ कॉन्फ़िगर किया गया था, तो यह फ़ाइल क्यों नहीं ढूंढ पाया, क्योंकि वे सेटिंग्स classpath (आमतौर पर `src/main/resources`) में फ़ाइल की अपेक्षा करती हैं।

इसे ठीक करने और यह सुनिश्चित करने के लिए कि `maven-checkstyle-plugin` प्रोजेक्ट रूट पर आपके कस्टम `checks.xml` का उपयोग करके `mvn compile` के साथ चले, आपको `<configLocation>` को फ़ाइल के absolute या project-relative path की ओर इंगित करने के लिए अपडेट करना होगा। इसके अतिरिक्त, आपको Checkstyle वर्जन के साथ कंपैटिबिलिटी सुनिश्चित करके `SuppressWithNearbyTextFilter` समस्या को हल करने की आवश्यकता है। नीचे चरण-दर-चरण समाधान दिया गया है।

### अपडेट की गई `pom.xml` कॉन्फ़िगरेशन
अपने `pom.xml` में `maven-checkstyle-plugin` को प्रोजेक्ट रूट पर `checks.xml` को संदर्भित करने और `SuppressWithNearbyTextFilter` का समर्थन करने के लिए एक संगत Checkstyle वर्जन का उपयोग करने के लिए संशोधित करें।

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- बेहतर कंपैटिबिलिटी के लिए नवीनतम वर्जन -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- प्रोजेक्ट रूट पर checks.xml की ओर इंगित करें -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- SuppressWithNearbyTextFilter का समर्थन करता है -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### परिवर्तनों की व्याख्या
1. **अपडेट किया गया `<configLocation>`**:
   - `${project.basedir}/checks.xml` में बदल गया ताकि प्रोजेक्ट रूट (`~/Projects/blog-server/checks.xml`) पर `checks.xml` की ओर इंगित किया जा सके।
   - `${project.basedir}` `pom.xml` वाली डायरेक्टरी को रिज़ॉल्व करता है, यह सुनिश्चित करता है कि प्लगइन classpath की परवाह किए बिना फ़ाइल ढूंढ लेता है।

2. **अपग्रेड किया गया प्लगइन वर्जन**:
   - बेहतर कंपैटिबिलिटी और बग फिक्स के लिए `maven-checkstyle-plugin` को `3.3.1` (जून 2025 तक नवीनतम) पर अपडेट किया गया।

3. **जोड़ी गई Checkstyle डिपेंडेंसी**:
   - Checkstyle `10.17.0` के लिए `<dependency>` जोड़ी गई, जिसमें `SuppressWithNearbyTextFilter` के लिए सपोर्ट शामिल है। `maven-checkstyle-plugin:3.1.1` में डिफ़ॉल्ट Checkstyle वर्जन (`8.29`) इस फ़िल्टर का समर्थन नहीं करता है, जिससे पिछली त्रुटि हो रही थी।

4. **रखा गया `<phase>compile</phase>`**:
   - यह सुनिश्चित करता है कि `checkstyle:check` `mvn compile` के दौरान चले, जैसा अनुरोध किया गया था।

5. **Resources सेक्शन**:
   - `<resources>` सेक्शन को बनाए रखा गया ताकि यह सुनिश्चित हो सके कि `src/main/resources` फ़ाइलें (जैसे `application.yaml`) प्रोसेस हो जाती हैं, हालाँकि यह सीधे तौर पर `checks.xml` से संबंधित नहीं है क्योंकि यह अब प्रोजेक्ट रूट पर है।

### `checks.xml` सामग्री सत्यापित करें
`SuppressWithNearbyTextFilter` के बारे में त्रुटि बताती है कि आपका `checks.xml` इस फ़िल्टर को संदर्भित करता है। सुनिश्चित करें कि यह सही ढंग से कॉन्फ़िगर है। एक वैध उदाहरण:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- उदाहरण गुण, आवश्यकतानुसार समायोजित करें -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- अन्य जांचें -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **जांच**: `~/Projects/blog-server/checks.xml` पर `checks.xml` खोलें और सत्यापित करें कि `SuppressWithNearbyTextFilter` सही ढंग से spell किया गया है और इसमें कोई आवश्यक गुण शामिल हैं (देखें [Checkstyle documentation](https://checkstyle.org/filters/suppresswithnearbytextfilter.html))।
- **कार्रवाई**: यदि unsure हैं, तो अस्थायी रूप से `<module name="SuppressWithNearbyTextFilter"/>` सेक्शन को हटा दें और समस्या को अलग करने के लिए परीक्षण करें।

### कॉन्फ़िगरेशन का परीक्षण करें
1. **प्रोजेक्ट साफ़ करें**:
   ```bash
   mvn clean
   ```
   यह `target` डायरेक्टरी को हटा देता है, जिसमें `checkstyle-checker.xml` और `checkstyle-result.xml` शामिल हैं, यह सुनिश्चित करते हुए कि कोई भी stale artifacts हस्तक्षेप नहीं करते हैं।

2. **Checkstyle चलाएँ**:
   ```bash
   mvn checkstyle:check
   ```
   यह Checkstyle कॉन्फ़िगरेशन का स्वतंत्र रूप से परीक्षण करता है।

3. **कंपाइल चलाएँ**:
   ```bash
   mvn compile
   ```
   इसे Checkstyle चलाना चाहिए ( `compile` फेज बाइंडिंग के कारण) और फिर कंपाइल करना चाहिए यदि कोई उल्लंघन बिल्ड को फेल नहीं करता है।

### यदि समस्याएँ बनी रहें तो डीबग करें
यदि आपको errors का सामना करना पड़ता है:
1. **फ़ाइल पथ जांचें**:
   - पुष्टि करें कि `checks.xml` `~/Projects/blog-server/checks.xml` पर मौजूद है।
   - सत्यापित करें कि फ़ाइल का नाम बिल्कुल `checks.xml` है (case-sensitive, कोई hidden extensions नहीं)।

2. **डीबग लॉगिंग के साथ चलाएँ**:
   ```bash
   mvn clean checkstyle:check -X
   ```
   `checks.xml` लोडिंग या `SuppressWithNearbyTextFilter` initialization के बारे में संदेशों की तलाश करें। यदि त्रुटि बनी रहती है तो प्रासंगिक आउटपुट साझा करें।

3. **एक न्यूनतम `checks.xml` के साथ परीक्षण करें**:
   अस्थायी रूप से `checks.xml` को एक न्यूनतम कॉन्फ़िगरेशन के साथ बदलें ताकि फ़ाइल की सामग्री के साथ समस्याओं को दूर किया जा सके:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   फिर `mvn checkstyle:check` चलाएँ। यदि यह काम करता है, तो समस्या आपके मूल `checks.xml` में `SuppressWithNearbyTextFilter` या अन्य मॉड्यूल के साथ है।

### अतिरिक्त नोट्स
- **Settings.xml चेतावनी**: आपके आउटपुट में `/usr/share/maven/conf/settings.xml` में एक अनियंत्रित `<blocked>` टैग के बारे में एक चेतावनी दिखाई देती है। यह Checkstyle समस्या से संबंधित नहीं है लेकिन आपके Maven कॉन्फ़िगरेशन में संभावित समस्या का संकेत देती है। `/usr/share/maven/conf/settings.xml` की लाइन 164 की जाँच करें और `<blocked>` टैग को हटा दें या सही करें, क्योंकि यह एक मानक Maven सेटिंग्स तत्व नहीं है।
- **वैकल्पिक फ़ाइल लोकेशन**: यदि आप चाहें, तो आप `checks.xml` को `src/main/resources/checks.xml` पर ले जा सकते हैं और `<configLocation>` को `classpath:checks.xml` पर वापस कर सकते हैं। यह Maven प्रोजेक्ट्स के लिए अधिक पारंपरिक है, क्योंकि resources स्वचालित रूप से classpath में शामिल हो जाते हैं।
- **उल्लंघन पर विफल**: यदि Checkstyle उल्लंघन बिल्ड को फेल कर रहे हैं और आप कंपाइलेशन को आगे बढ़ने देना चाहते हैं, तो प्लगइन के `<configuration>` में `<failOnViolation>false</failOnViolation>` जोड़ें:
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### सत्यापन
परिवर्तन लागू करने के बाद:
1. `mvn clean compile` चलाएं और पुष्टि करें कि:
   - Checkstyle प्रोजेक्ट रूट से `checks.xml` का उपयोग करके चलता है।
   - `checks.xml` या `SuppressWithNearbyTextFilter` से संबंधित कोई errors नहीं होती हैं।
   - यदि Checkstyle पास हो जाता है या बिल्ड को फेल नहीं करने के लिए कॉन्फ़िगर किया गया है तो कंपाइलेशन आगे बढ़ता है।
2. Checkstyle परिणामों के लिए `target/checkstyle-result.xml` की जाँच करें।

यदि त्रुटि बनी रहती है, तो कृपया साझा करें:
- `checks.xml` की सामग्री (या प्रासंगिक स्निपेट)।
- `mvn clean checkstyle:check -X` से डीबग आउटपुट।
- `SuppressWithNearbyTextFilter` के साथ आप लागू करने का प्रयास कर रहे हैं कोई विशिष्ट Checkstyle नियम।