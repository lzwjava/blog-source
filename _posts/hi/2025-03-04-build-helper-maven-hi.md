---
audio: false
generated: true
lang: hi
layout: post
title: बिल्ड हेल्पर मेवन प्लगइन
translated: true
type: note
---

`builder-helper-maven-plugin`, जिसे अब **Build Helper Maven Plugin** के नाम से जाना जाता है, Maven build lifecycle में विभिन्न कार्यों में सहायता के लिए बनाया गया एक बहुमुखी टूल है। मूल रूप से Codehaus के तहत होस्ट किया गया, अब इसका रखरखाव MojoHaus द्वारा किया जाता है, हालाँकि इसके Maven coordinates अभी भी `org.codehaus.mojo` group ID का उपयोग करते हैं। यह प्लगइन ऑपरेशन जैसे अतिरिक्त स्रोत निर्देशिकाएँ जोड़ने, अतिरिक्त artifacts संलग्न करने, संस्करण जानकारी पार्स करने, और भी बहुत कुछ में मदद के लिए goals का एक सेट प्रदान करता है। नीचे, मैं आपको दिखाऊंगा कि कैसे इस प्लगइन का उपयोग अपने Maven प्रोजेक्ट में करें।

### Maven क्या है?
प्लगइन में गोता लगाने से पहले, संदर्भ स्थापित करते हैं। Maven एक व्यापक रूप से उपयोग किया जाने वाला build automation टूल है, मुख्य रूप से Java प्रोजेक्ट्स के लिए। यह dependencies को प्रबंधित करके, कोड compile करके, एप्लिकेशन package करके, और भी बहुत कुछ, सभी को एक केंद्रीय फ़ाइल `pom.xml` के माध्यम से कॉन्फ़िगर करके, build प्रक्रिया को सरल और मानकीकृत करता है।

### चरण 1: अपने `pom.xml` में प्लगइन शामिल करें
Build Helper Maven Plugin का उपयोग करने के लिए, आपको इसे अपने Maven प्रोजेक्ट की `pom.xml` फ़ाइल के `<build><plugins>` सेक्शन में जोड़ना होगा। यहाँ बताया गया है कि कैसे करें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- विशिष्ट goals के लिए executions यहाँ जोड़े जाएंगे -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo` (इसकी उत्पत्ति को दर्शाता है, भले ही यह अब MojoHaus के अंतर्गत है)।
- **Artifact ID**: `build-helper-maven-plugin`।
- **Version**: मेरे अंतिम अपडेट के अनुसार, `3.6.0` नवीनतम संस्करण है, लेकिन आपको सबसे recent release के लिए [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) जांच करनी चाहिए।

यह घोषणा प्लगइन को आपके प्रोजेक्ट में उपलब्ध कराती है, लेकिन जब तक आप विशिष्ट goals को कॉन्फ़िगर नहीं करते, तब तक यह कुछ नहीं करेगा।

### चरण 2: विशिष्ट Goals के लिए Executions कॉन्फ़िगर करें
Build Helper Maven Plugin कई goals प्रदान करता है, जिनमें से प्रत्येक एक विशेष कार्य के लिए डिज़ाइन किया गया है। आप प्लगइन घोषणा के भीतर `<executions>` ब्लॉक जोड़कर इन goals को कॉन्फ़िगर करते हैं, यह निर्दिष्ट करते हुए कि वे कब चलने चाहिए (एक Maven lifecycle phase के माध्यम से) और उन्हें कैसे व्यवहार करना चाहिए।

यहां कुछ commonly used goals और उनके उद्देश्य दिए गए हैं:

- **`add-source`**: आपके प्रोजेक्ट में अतिरिक्त स्रोत निर्देशिकाएँ जोड़ता है।
- **`add-test-source`**: अतिरिक्त test स्रोत निर्देशिकाएँ जोड़ता है।
- **`add-resource`**: अतिरिक्त resource निर्देशिकाएँ जोड़ता है।
- **`attach-artifact`**: इंस्टॉलेशन और deployment के लिए अतिरिक्त artifacts (जैसे, फ़ाइलें) आपके प्रोजेक्ट से संलग्न करता है।
- **`parse-version`**: प्रोजेक्ट के version को पार्स करता है और properties सेट करता है (जैसे, major, minor, incremental versions)।

प्रत्येक goal के लिए अपने स्वयं के कॉन्फ़िगरेशन की आवश्यकता होती है, जिसे आप एक `<execution>` ब्लॉक के भीतर परिभाषित करते हैं।

### चरण 3: उदाहरण – एक अतिरिक्त स्रोत निर्देशिका जोड़ना
इस प्लगइन के लिए एक सामान्य use case एक अतिरिक्त स्रोत निर्देशिका जोड़ना है, क्योंकि Maven आमतौर पर केवल एक को डिफ़ॉल्ट रूप से सपोर्ट करता है (`src/main/java`)। यहां बताया गया है कि कैसे एक अतिरिक्त स्रोत निर्देशिका को शामिल करने के लिए `add-source` goal को कॉन्फ़िगर किया जाए:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: इस execution के लिए एक unique identifier (जैसे, `add-source`)।
- **`<phase>`**: Maven lifecycle phase जब goal चलता है (जैसे, `generate-sources` यह सुनिश्चित करता है कि निर्देशिका build में जल्दी जोड़ दी जाए)।
- **`<goals>`**: execute करने के लिए goal निर्दिष्ट करता है (इस मामले में `add-source`)।
- **`<configuration>`**: अतिरिक्त स्रोत निर्देशिका को परिभाषित करता है (`path/to/your/extra/source/directory` को अपने वास्तविक path से बदलें, जैसे, `src/main/generated`)।

जब आप `mvn compile` जैसा कोई Maven कमांड चलाते हैं, तो Maven इस अतिरिक्त निर्देशिका को एक स्रोत फ़ोल्डर के रूप में शामिल करेगा।

### अतिरिक्त नोट्स
- **Version Compatibility**: संस्करण 3.0.0 के बाद से, प्लगइन के लिए Maven 3 या उच्चतर की आवश्यकता होती है। यदि आप कोई पुराना Maven version उपयोग कर रहे हैं, तो आपको प्लगइन version 1.12 या पहले के संस्करण का उपयोग करने की आवश्यकता होगी।
- **Multiple Goals**: आप विभिन्न goals को चलाने के लिए एक ही प्लगइन के भीतर कई `<execution>` ब्लॉक परिभाषित कर सकते हैं। उदाहरण के लिए, आप `add-source` और `add-test-source` के लिए executions शामिल करके स्रोत और test स्रोत दोनों निर्देशिकाएँ जोड़ सकते हैं।
- **प्लगइन चलाना**: एक बार कॉन्फ़िगर हो जाने पर, Maven कमांड (जैसे, `mvn clean install`) चलाने से निर्दिष्ट phases के दौरान प्लगइन के goals ट्रिगर होंगे।

### आगे के संसाधन
अन्य goals के और विवरण और उदाहरणों के लिए, [official usage page](https://www.mojohaus.org/build-helper-maven-plugin/usage.html) देखें। यह पृष्ठ सभी उपलब्ध goals के लिए व्यापक दस्तावेज़ीकरण और sample configurations प्रदान करता है।

### अंतिम विचार
Build Helper Maven Plugin आपके Maven टूलकिट में एक शक्तिशाली जोड़ है, खासकर उन प्रोजेक्ट्स के लिए जिन्हें गैर-मानक build configurations की आवश्यकता होती है। इसे अपने `pom.xml` में शामिल करके और उचित goals को कॉन्फ़िगर करके, आप विशिष्ट आवश्यकताओं को पूरा करने के लिए अपनी build प्रक्रिया को अनुकूलित कर सकते हैं। जबकि इसकी शुरुआत Codehaus के तहत हुई थी, इसका वर्तमान घर MojoHaus है, और यह Maven builds को बेहतर बनाने के लिए एक विश्वसनीय विकल्प बना हुआ है।