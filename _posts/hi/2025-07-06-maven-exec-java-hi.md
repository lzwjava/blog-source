---
audio: false
generated: true
lang: hi
layout: post
title: Maven Exec के साथ Java क्लासेज़ चलाएँ
translated: true
type: note
---

Maven Exec Plugin का `exec:java` लक्ष्य आपके Maven बिल्ड से सीधे एक Java क्लास को, जिसमें `main` मेथड हो, चलाने का एक शक्तिशाली तरीका है। यह निर्दिष्ट Java क्लास को आपके Maven बिल्ड के **समान JVM के भीतर** ही execute करता है, प्रोजेक्ट की dependencies को classpath के रूप में उपयोग करते हुए।

इसका उपयोग कैसे करें, सामान्य परिदृश्यों और उदाहरणों के साथ:

## 1. कमांड लाइन से बुनियादी उपयोग

`exec:java` का उपयोग करने का सबसे सरल तरीका सीधे कमांड लाइन से है, खासकर त्वरित परीक्षणों या किसी विशिष्ट utility क्लास को चलाने के लिए।

**कमांड:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**स्पष्टीकरण:**

  * `mvn exec:java`: `exec-maven-plugin` के `java` लक्ष्य को invoke करता है।
  * `-Dexec.mainClass="com.yourcompany.YourMainClass"`: यह सिस्टम प्रॉपर्टी उस Java क्लास का fully qualified नाम निर्दिष्ट करती है जिसमें `public static void main(String[] args)` मेथड है जिसे आप execute करना चाहते हैं।

**उदाहरण:**

मान लीजिए आपके पास एक क्लास `com.example.myapp.HelloWorld` है जिसमें एक `main` मेथड है:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

आप इसे इस प्रकार चलाएंगे:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**नोट:** यह एक अच्छा अभ्यास है कि `exec:java` के चलाने का प्रयास करने से पहले यह सुनिश्चित करने के लिए `mvn compile` चलाया जाए कि आपकी क्लासेस compiled हैं।

## 2. अपने Java प्रोग्राम को आर्गुमेंट पास करना

आप `exec.args` सिस्टम प्रॉपर्टी का उपयोग करके अपने Java प्रोग्राम की `main` मेथड को आर्गुमेंट पास कर सकते हैं:

**कमांड:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**उदाहरण:**

यदि आपकी `HelloWorld` क्लास यह होती:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Arguments received: ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

आप इसे इस तरह चलाते:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

रिक्त स्थान वाले आर्गुमेंट के लिए, उन्हें quotes में enclosed करें:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. `pom.xml` में `exec:java` को कॉन्फ़िगर करना

अधिक स्थायी या डिफ़ॉल्ट कॉन्फ़िगरेशन के लिए, आप `exec-maven-plugin` को अपने `pom.xml` में जोड़ सकते हैं। यह आपको एक डिफ़ॉल्ट `mainClass` और अन्य पैरामीटर परिभाषित करने की अनुमति देता है, ताकि आपको हर बार कमांड लाइन पर उन्हें निर्दिष्ट न करना पड़े।

**`pom.xml` कॉन्फ़िगरेशन:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</modelVersion>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <goals>
                            <goal>java</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <mainClass>com.example.myapp.HelloWorld</mainClass>
                    <arguments>
                        <argument>defaultArg1</argument>
                        <argument>defaultArg2</argument>
                    </arguments>
                    <systemProperties>
                        <systemProperty>
                            <key>my.custom.property</key>
                            <value>someValue</value>
                        </systemProperty>
                    </systemProperties>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**कॉन्फ़िगरेशन विकल्पों की व्याख्या:**

  * `<groupId>org.codehaus.mojo</groupId>` और `<artifactId>exec-maven-plugin</artifactId>`: प्लगइन के लिए मानक coordinates।
  * `<version>3.2.0</version>`: प्लगइन का एक recent version हमेशा निर्दिष्ट करें।
  * `<goals><goal>java</goal></goals>`: यह `java` लक्ष्य को bind करता है। यदि आप इसे किसी विशिष्ट phase से नहीं bind करते हैं, तो यह तब executed होगा जब आप स्पष्ट रूप से `mvn exec:java` कॉल करेंगे।
  * `<mainClass>com.example.myapp.HelloWorld</mainClass>`: execute करने के लिए डिफ़ॉल्ट main क्लास सेट करता है। यदि आप कमांड लाइन पर `-Dexec.mainClass` के बिना `mvn exec:java` चलाते हैं, तो इस क्लास का उपयोग किया जाएगा।
  * `<arguments>`: `main` मेथड को पास किए जाने वाले आर्गुमेंट की एक सूची। ये डिफ़ॉल्ट आर्गुमेंट हैं जिन्हें कमांड लाइन पर `exec.args` द्वारा override किया जा सकता है।
  * `<systemProperties>`: आपको सिस्टम प्रॉपर्टीज़ (`-Dkey=value`) परिभाषित करने की अनुमति देता है जो `exec:java` के चलने पर आपके Java एप्लिकेशन के लिए उपलब्ध होंगी।

**`pom.xml` कॉन्फ़िगरेशन के साथ चलाना:**

एक बार `pom.xml` में कॉन्फ़िगर हो जाने पर:

  * डिफ़ॉल्ट main क्लास और आर्गुमेंट के साथ चलाने के लिए:
    ```bash
    mvn compile exec:java
    ```
  * कमांड लाइन से main क्लास को override करने के लिए:
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
  * कमांड लाइन से आर्गुमेंट को override/जोड़ने के लिए:
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    (नोट: यदि कमांड लाइन पर प्रदान किया जाता है तो `exec.args` आमतौर पर `pom.xml` में परिभाषित `arguments` को *replace* कर देगा।)

## 4. `exec:exec` से मुख्य अंतर

`exec:java` और `exec:exec` के बीच अंतर को समझना महत्वपूर्ण है:

  * **`exec:java`**: Java प्रोग्राम को Maven के **समान JVM** में चलाता है। यह आम तौर पर तेज़ होता है क्योंकि यह एक नई process spawn होने से बचाता है। यह स्वचालित रूप से classpath पर प्रोजेक्ट की dependencies सेट कर देता है।
  * **`exec:exec`**: एक मनमाना external प्रोग्राम (जिसमें `java` स्वयं भी शामिल है) को **एक अलग process में** चलाता है। यह तब उपयोगी होता है जब आपको एक अलग Java executable निर्दिष्ट करने की आवश्यकता हो, JVM आर्गुमेंट (जैसे `-Xmx`) पास करने हों, या non-Java executables चलाने हों। यदि आप Java प्रोग्राम चलाने के लिए `exec:exec` का उपयोग करते हैं, तो आपको आमतौर पर आर्गुमेंट में `%classpath` का उपयोग करके classpath को मैन्युअल रूप से construct करना पड़ता है।

Maven बिल्ड के भीतर अधिकांश मानक Java एप्लिकेशन execution के लिए, `exec:java` अधिक सुविधाजनक विकल्प है।

## 5. महत्वपूर्ण विचार

  * **Classpath:** `exec:java` आपके प्रोजेक्ट की compiled क्लासेस और उसकी dependencies को classpath में स्वचालित रूप से शामिल करता है।
  * **JVM Arguments:** क्योंकि `exec:java` Maven के *समान* JVM में चलता है, आप JVM आर्गुमेंट (जैसे `-Xmx`, `-XX:MaxPermSize`) को सीधे इसके कॉन्फ़िगरेशन या `exec.args` के माध्यम से `exec:java` को पास नहीं कर सकते। इन आर्गुमेंट को Maven JVM को ही पास करने की आवश्यकता होती है, आमतौर पर `MAVEN_OPTS` environment variable के माध्यम से:
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
  * **System.exit()**: यदि आपका Java प्रोग्राम `System.exit()` को कॉल करता है, तो यह पूरे Maven बिल्ड प्रक्रिया को terminate कर देगा, न कि केवल आपके प्रोग्राम को। `exec:java` का उपयोग करते समय इसका ध्यान रखें। प्लगइन में एक विकल्प `blockSystemExit` (version 3.2.0 से) है जो इसे रोकने का प्रयास करता है, लेकिन यह सबसे अच्छा है कि आप अपनी main मेथड को `System.exit()` को कॉल किए बिना gracefully complete होने के लिए design करें।
  * **Dependencies:** `exec:java` प्रोजेक्ट की dependencies पर निर्भर करता है। यदि आपको किसी dependency से एक क्लास चलाने की आवश्यकता है जो आपके प्रोजेक्ट के बिल्ड का हिस्सा नहीं है, तो आपको प्लगइन के कॉन्फ़िगरेशन को adjust करने की आवश्यकता हो सकती है या explicit classpath परिभाषा के साथ `exec:exec` का उपयोग करने पर विचार करना चाहिए।
  * **Plugin Version:** नवीनतम features और bug fixes के लिए हमेशा `exec-maven-plugin` का एक recent version उपयोग करें। सबसे अद्यतित जानकारी के लिए MojoHaus वेबसाइट जांचें।