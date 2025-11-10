---
audio: false
generated: true
lang: hi
layout: post
title: स्पॉटलेस के साथ पैलेंटिर जावा फॉर्मेट कॉन्फ़िगर करें
translated: true
type: note
---

**Palantir Java Format** को **Spotless Maven Plugin** के साथ कॉन्फ़िगर करने के लिए, आपको प्लगइन को `palantirJavaFormat` का उपयोग करने और टैबस्पेस, इंडेंटेशन, इम्पोर्ट ऑर्डर और अन्य सेटिंग्स जैसे फ़ॉर्मेटिंग विकल्पों को निर्दिष्ट करने के लिए सेट अप करना होगा। नीचे Spotless प्लगइन और Palantir Java Format के आधार पर इन सेटिंग्स और उपलब्ध विकल्पों को कॉन्फ़िगर करने का विस्तृत मार्गदर्शिका दी गई है।

### Spotless Maven Plugin को Palantir Java Format के साथ जोड़ना

अपने `pom.xml` में Spotless Maven Plugin को शामिल करें और इसे `palantirJavaFormat` का उपयोग करने के लिए कॉन्फ़िगर करें। यहां टैबस्पेस, इंडेंटेशन, इम्पोर्ट ऑर्डर और अन्य विकल्पों के लिए सामान्य कॉन्फ़िगरेशन के साथ एक बुनियादी सेटअप दिया गया है:

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- नवीनतम संस्करण का उपयोग करें -->
    <configuration>
        <java>
            <!-- फ़ॉर्मेट करने के लिए फ़ाइलें निर्दिष्ट करें (वैकल्पिक, डिफ़ॉल्ट रूप से सभी .java फ़ाइलें) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- वांछित संस्करण निर्दिष्ट करें -->
                <style>GOOGLE</style> <!-- विकल्प: GOOGLE, AOSP, या PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- वैकल्पिक: Javadoc फ़ॉर्मेट करें -->
            </palantirJavaFormat>
            <!-- इंडेंटेशन सेटिंग्स -->
            <indent>
                <tabs>true</tabs> <!-- रिक्त स्थान के बजाय टैब का उपयोग करें -->
                <spacesPerTab>4</spacesPerTab> <!-- प्रति टैब रिक्त स्थान की संख्या -->
            </indent>
            <!-- इम्पोर्ट ऑर्डर कॉन्फ़िगरेशन -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- कस्टम इम्पोर्ट ऑर्डर -->
            </importOrder>
            <!-- अप्रयुक्त इम्पोर्ट हटाएं -->
            <removeUnusedImports/>
            <!-- अन्य वैकल्पिक सेटिंग्स -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- spotless:off और spotless:on टैग सक्षम करें -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- कोड को स्वचालित रूप से फ़ॉर्मेट करें -->
            </goals>
            <phase>validate</phase> <!-- validate चरण के दौरान चलाएं -->
        </execution>
    </executions>
</plugin>
```

### कॉन्फ़िगरेशन विकल्पों की व्याख्या

यहां Spotless में `palantirJavaFormat` के साथ `java` सेक्शन के लिए मुख्य कॉन्फ़िगरेशन विकल्पों का विवरण दिया गया है, जो टैबस्पेस, इंडेंटेशन, इम्पोर्ट ऑर्डर और अन्य प्रासंगिक सेटिंग्स पर केंद्रित है:

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**: उपयोग करने के लिए `palantir-java-format` का संस्करण निर्दिष्ट करता है। नवीनतम संस्करण [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) या [GitHub](https://github.com/palantir/palantir-java-format/releases) पर जांचें। उदाहरण: `<version>2.53.0</version>`.
- **`<style>`**: फ़ॉर्मेटिंग शैली को परिभाषित करता है। विकल्प हैं:
  - `GOOGLE`: Google Java Style का उपयोग करता है (2-स्पेस इंडेंटेशन, 100-कैरेक्टर लाइन सीमा).
  - `AOSP`: Android Open Source Project शैली का उपयोग करता है (4-स्पेस इंडेंटेशन, 100-कैरेक्टर लाइन सीमा).
  - `PALANTIR`: Palantir की शैली का उपयोग करता है (4-स्पेस इंडेंटेशन, 120-कैरेक्टर लाइन सीमा, लैम्ब्डा-अनुकूल फ़ॉर्मेटिंग).[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**: Javadoc फ़ॉर्मेटिंग को सक्षम/अक्षम करने के लिए बूलियन (Palantir Java Format संस्करण ≥ 2.39.0 आवश्यक). उदाहरण: `<formatJavadoc>true</formatJavadoc>`.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **कस्टम ग्रुप आर्टिफैक्ट**: शायद ही कभी आवश्यक हो, लेकिन आप फ़ॉर्मेटर के लिए एक कस्टम ग्रुप और आर्टिफैक्ट निर्दिष्ट कर सकते हैं। उदाहरण: `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`.

#### 2. **इंडेंटेशन (`<indent>`)**

- **`<tabs>`**: इंडेंटेशन के लिए टैब (`true`) या रिक्त स्थान (`false`) का उपयोग करने के लिए बूलियन। उदाहरण: `<tabs>true</tabs>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**: प्रति टैब रिक्त स्थान की संख्या (जब `<tabs>` `false` हो या मिश्रित इंडेंटेशन के लिए उपयोग किया जाता है)। सामान्य मान `2` या `4` हैं। उदाहरण: `<spacesPerTab>4</spacesPerTab>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **नोट**: Palantir Java Format की शैली (जैसे, `GOOGLE`, `AOSP`, `PALANTIR`) इंडेंटेशन व्यवहार को प्रभावित कर सकती है। उदाहरण के लिए, `GOOGLE` डिफ़ॉल्ट रूप से 2 रिक्त स्थानों का उपयोग करता है, जबकि `AOSP` और `PALANTIR` 4 रिक्त स्थानों का उपयोग करते हैं। Spotless में `<indent>` सेटिंग्स इन डिफ़ॉल्ट्स को ओवरराइड या पूरक कर सकती हैं, लेकिन संघर्षों से बचने के लिए स्थिरता सुनिश्चित करें।[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **इम्पोर्ट ऑर्डर (`<importOrder>`)**

- **`<order>`**: इम्पोर्ट समूहों के क्रम को निर्दिष्ट करता है, अल्पविराम से अलग किया गया। स्टैटिक इम्पोर्ट्स के लिए `\\#` का उपयोग करें और अनिर्दिष्ट इम्पोर्ट्स के लिए एक खाली स्ट्रिंग (`""`)। उदाहरण: `<order>java,javax,org,com,\\#</order>` पहले `java` से शुरू होने वाले इम्पोर्ट्स को क्रमबद्ध करता है, फिर `javax`, आदि, स्टैटिक इम्पोर्ट्स अंत में।[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**: वैकल्पिक रूप से, इम्पोर्ट ऑर्डर वाली एक फ़ाइल निर्दिष्ट करें। उदाहरण: `<file>${project.basedir}/eclipse.importorder</file>`. फ़ाइल प्रारूप Eclipse के इम्पोर्ट ऑर्डर कॉन्फ़िगरेशन से मेल खाता है (जैसे, `java|javax|org|com|\\#`).[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - उदाहरण फ़ाइल सामग्री:
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **अन्य उपयोगी सेटिंग्स**

- **`<removeUnusedImports>`**: अप्रयुक्त इम्पोर्ट्स को हटाता है। वैकल्पिक रूप से, इंजन निर्दिष्ट करें:
  - डिफ़ॉल्ट: हटाने के लिए `google-java-format` का उपयोग करता है।
  - विकल्प: नए Java फीचर्स (जैसे, Java 17) के साथ JDK8+ संगतता के लिए `<engine>cleanthat-javaparser-unnecessaryimport</engine>`.[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**: लाइनों से ट्रेलिंग व्हाइटस्पेस हटाता है। उदाहरण: `<trimTrailingWhitespace/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**: सुनिश्चित करता है कि फ़ाइलें एक न्यूलाइन के साथ समाप्त हों। उदाहरण: `<endWithNewline/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**: फ़ॉर्मेटिंग से कोड के सेक्शन को बाहर करने के लिए `// spotless:off` और `// spotless:on` कमेंट्स को सक्षम करता है। उदाहरण: `<toggleOffOn/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**: फ़ाइलों में एक लाइसेंस हेडर जोड़ता है। उदाहरण:
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  आप एक फ़ाइल का भी उपयोग कर सकते हैं: `<file>${project.basedir}/license.txt</file>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**: सुनिश्चित करता है कि टाइप एनोटेशन उन फ़ील्ड्स के समान लाइन पर हों जिनका वे वर्णन करते हैं। उदाहरण: `<formatAnnotations/>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**: फ़ॉर्मेटिंग को Git ब्रांच (जैसे, `origin/main`) के सापेक्ष बदली गई फ़ाइलों तक सीमित करता है। उदाहरण: `<ratchetFrom>origin/main</ratchetFrom>`.[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **POM-विशिष्ट फ़ॉर्मेटिंग (`<pom>`)**

`pom.xml` फ़ाइल को स्वयं फ़ॉर्मेट करने के लिए, `sortPom` के साथ `<pom>` सेक्शन का उपयोग करें:
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- POM के लिए इंडेंटेशन -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- मानक POM क्रम -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- डिपेंडेंसीज़ क्रमबद्ध करें -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- प्लगइन्स क्रमबद्ध करें -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **`sortPom` के लिए विकल्प**:
  - `<nrOfIndentSpace>`: इंडेंटेशन के लिए रिक्त स्थान की संख्या (जैसे, `2` या `4`).
  - `<predefinedSortOrder>`: एलिमेंट ऑर्डर के लिए `recommended_2008_06` या `custom_1` जैसे विकल्प।[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`: `groupId`, `artifactId`, या अन्य मानदंडों द्वारा क्रमबद्ध करें।
  - `<sortPlugins>`: प्लगइन्स को इसी तरह क्रमबद्ध करें।
  - `<endWithNewline>`: सुनिश्चित करें कि POM एक न्यूलाइन के साथ समाप्त हो।
  - `<expandEmptyElements>``: खाली XML टैग्स का विस्तार करें (जैसे, `<tag></tag>` बनाम `<tag/>`).[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### Spotless चलाना

- **फ़ॉर्मेटिंग जांचें**: `mvn spotless:check` – कॉन्फ़िगर किए गए नियमों के विरुद्ध कोड को मान्य करता है, यदि उल्लंघन मिलते हैं तो बिल्ड विफल कर देता है।
- **फ़ॉर्मेटिंग लागू करें**: `mvn spotless:apply` – नियमों का पालन करने के लिए कोड को स्वचालित रूप से फ़ॉर्मेट करता है।

### नोट्स और सर्वोत्तम अभ्यास

- **IDE के साथ स्थिरता**: IntelliJ या Eclipse को Spotless के साथ संरेखित करने के लिए, `palantir-java-format` IntelliJ प्लगइन इंस्टॉल करें या एक Eclipse फ़ॉर्मेटर XML फ़ाइल का उपयोग करें। IntelliJ के लिए, एक संगत शैली फ़ाइल (जैसे, Google शैली के लिए `intellij-java-google-style.xml`) इम्पोर्ट करें या Palantir सेटिंग्स से मेल खाने के लिए मैन्युअल रूप से कॉन्फ़िगर करें।[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **संस्करण संगतता**: सुनिश्चित करें कि `palantir-java-format` संस्करण आपके Java संस्करण का समर्थन करता है। Java 17+ के लिए, एक हालिया संस्करण (जैसे, 2.53.0) का उपयोग करें। पैटर्न मिलान जैसी कुछ सुविधाओं का सीमित समर्थन हो सकता है।[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **कस्टम फ़ॉर्मेटिंग**: उन्नत अनुकूलन के लिए, `<palantirJavaFormat>` के बजाय `<eclipse>` के साथ एक Eclipse फ़ॉर्मेटर XML फ़ाइल का उपयोग करें:
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  उदाहरण `custom-style.xml`:
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **सीमाएं**: Palantir Java Format, Eclipse के फ़ॉर्मेटर की तुलना में कम कॉन्फ़िगर करने योग्य है लेकिन स्थिरता और आधुनिक Java सुविधाओं (जैसे, लैम्ब्डास) के लिए डिज़ाइन किया गया है। यह सभी एज केस (जैसे, गहराई से नेस्टेड लैम्ब्डास) को हैंडल नहीं कर सकता है।[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### उपलब्ध विकल्प सारांश

| **विकल्प**                  | **विवरण**                                                                 | **उदाहरण मान**                              |
|-----------------------------|---------------------------------------------------------------------------|---------------------------------------------|
| `<palantirJavaFormat>`      | Palantir Java Format को कॉन्फ़िगर करता है।                               | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | इंडेंटेशन शैली (टैब या रिक्त स्थान) और आकार सेट करता है।                | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | इम्पोर्ट समूह क्रम को परिभाषित करता है या एक फ़ाइल का उपयोग करता है।    | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | अप्रयुक्त इम्पोर्ट्स को हटाता है, वैकल्पिक इंजन के साथ।                 | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | ट्रेलिंग व्हाइटस्पेस हटाता है।                                          | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | सुनिश्चित करता है कि फ़ाइलें एक न्यूलाइन के साथ समाप्त हों।            | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | `spotless:off`/`spotless:on` टैग्स सक्षम करता है।                      | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | एक लाइसेंस हेडर जोड़ता है।                                              | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | एनोटेशन्स को फ़ील्ड्स के समान लाइन पर फ़ॉर्मेट करता है।                | `<formatAnnotations/>`                         |
| `<sortPom>`                | `pom.xml` को सॉर्टिंग और इंडेंटेशन के साथ फ़ॉर्मेट करता है।            | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### स्रोत

- Spotless Maven Plugin प्रलेखन: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format: [GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- Spotless कॉन्फ़िगरेशन के लिए Stack Overflow और सामुदायिक उदाहरण[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

यह कॉन्फ़िगरेशन Palantir Java Format के साथ सुसंगत कोड फ़ॉर्मेटिंग सुनिश्चित करता है, जो टैबस्पेस, इंडेंटेशन और इम्पोर्ट ऑर्डर के लिए आपकी प्राथमिकताओं के अनुरूप है। यदि आपको और स्पष्टीकरण या अतिरिक्त विकल्पों की आवश्यकता है तो मुझे बताएं!