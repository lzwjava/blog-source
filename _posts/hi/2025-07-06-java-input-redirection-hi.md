---
audio: false
generated: true
lang: hi
layout: post
title: मैवेन जावा प्रोग्राम में इनपुट पुनर्निर्देशित करना
translated: true
type: note
---

`exec:java` प्रोग्राम के लिए इनपुट रीडायरेक्ट करना थोड़ा पेचीदा हो सकता है क्योंकि `exec:java` Java प्रक्रिया को Maven के *समान JVM* के भीतर चलाता है। इसका मतलब है कि आप स्टैंडर्ड शेल रीडायरेक्शन ऑपरेटर्स (`<`, `>`) का उपयोग उसी तरह नहीं कर सकते जैसे आप एक अलग प्रक्रिया के लिए करते हैं।

हालांकि, आपके पास अभी भी अपने `exec:java` प्रोग्राम को इनपुट प्रदान करने के कुछ विकल्प हैं:

## 1. प्रोग्रामेटिक इनपुट (स्टैंडर्ड `System.in`)

सबसे सीधा तरीका यह है कि आप अपने Java प्रोग्राम को हमेशा की तरह `System.in` से पढ़ने के लिए डिज़ाइन करें। जब आप `mvn exec:java` चलाते हैं, तो आप जो कुछ भी अपने कंसोल में टाइप करेंगे वह आपके Java प्रोग्राम के `System.in` को निर्देशित किया जाएगा।

**उदाहरण Java प्रोग्राम (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**कमांड लाइन से चलाना:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

जब आप इसे चलाते हैं, तो Maven शुरू होगा, और फिर आपका प्रोग्राम आपसे इनपुट के लिए प्रॉम्प्ट करेगा। आप सीधे कंसोल में टाइप करते हैं।

## 2. इनपुट के लिए `exec.args` प्रॉपर्टी का उपयोग करना (सरल मामलों के लिए)

यदि आपका प्रोग्राम बहुत सरल, गैर-इंटरैक्टिव इनपुट की अपेक्षा करता है, तो आप *शायद* इसे एक आर्ग्युमेंट के रूप में पास कर सकते हैं, और आपका प्रोग्राम फिर उस आर्ग्युमेंट को `System.in` के बजाय पढ़ता है। यह सच्चा स्टैंडर्ड इनपुट रीडायरेक्शन नहीं है, लेकिन यह सरल डेटा के लिए एक समान उद्देश्य पूरा करता है।

**उदाहरण Java प्रोग्राम (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Received input from argument: " + inputData);
        } else {
            System.out.println("No input argument provided.");
        }
    }
}
```

**कमांड लाइन से चलाना:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

या स्पेस के साथ:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

यह दृष्टिकोण केवल तभी उपयुक्त है यदि आपके प्रोग्राम को उसके "इनपुट" को कमांड-लाइन आर्ग्युमेंट्स के रूप में स्वीकार करने के लिए संशोधित किया जा सकता है।

## 3. शेल रीडायरेक्शन का उपयोग करके इनपुट रीडायरेक्ट करना (`exec:exec` के साथ)

यदि आपको बिल्कुल फ़ाइल या पाइप से इनपुट रीडायरेक्ट करने की आवश्यकता है, तो आपको `exec:java` के बजाय `exec:exec` गोल का उपयोग **करना होगा**। `exec:exec` गोल एक अलग प्रक्रिया spawn करता है, जो शेल को स्टैंडर्ड इनपुट/आउटपुट रीडायरेक्शन को हैंडल करने की अनुमति देता है।

**`exec:exec` के लिए `pom.xml` कॉन्फ़िगरेशन:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <id>run-my-java-app</id>
                        <phase>package</phase> <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/> <argument>com.example.app.MyInputProgram</argument>
                                </arguments>
                            <workingDirectory>${project.build.directory}/classes</workingDirectory>
                            </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**उदाहरण Java प्रोग्राम (ऊपर वाला ही `MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // यह मानते हुए कि आप उम्र के लिए नाम के बाद एक और लाइन पढ़ना चाहते हैं
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**इनपुट फ़ाइल (`input.txt`):**

```
Alice
30
```

**`exec:exec` और इनपुट रीडायरेक्शन के साथ चलाना:**

पहले, अपने प्रोजेक्ट को कंपाइल करें:

```bash
mvn compile
```

फिर, `exec:exec` गोल चलाएं और अपने शेल का उपयोग करके इनपुट रीडायरेक्ट करें:

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**स्पष्टीकरण:**

  * `mvn exec:exec@run-my-java-app`: "run-my-java-app" `id` के साथ `exec-maven-plugin` के `exec` गोल को निष्पादित करता है।
  * `< input.txt`: यह एक स्टैंडर्ड शेल रीडायरेक्शन ऑपरेटर है। यह आपके शेल को `input.txt` की सामग्री लेने और इसे निष्पादित की जा रही कमांड (`java com.example.app.MyInputProgram`) के स्टैंडर्ड इनपुट के रूप में फ़ीड करने के लिए कहता है।

**`exec:exec` के लिए महत्वपूर्ण नोट्स:**

  * **`executable`:** आप स्पष्ट रूप से `java` को एक्जिक्यूटेबल के रूप में निर्दिष्ट करते हैं।
  * **`arguments`:** आपको `java` कमांड के आर्ग्युमेंट्स को मैन्युअल रूप से बनाने की आवश्यकता है, जिसमें `-classpath` और `mainClass` शामिल हैं। `<classpath/>` टैग एक विशेष मान है जिसे `exec-maven-plugin` आपके प्रोजेक्ट की वास्तविक गणना की गई classpath से बदल देता है।
  * **`workingDirectory`:** `workingDirectory` को `${project.build.directory}/classes` पर सेट करना अक्सर मददगार होता है ताकि Java आपकी कंपाइल की गई `.class` फ़ाइलों को ढूंढ सके।
  * **`outputFile` (ऑप्शनल):** `exec:exec` के लिए `exec-maven-plugin` प्रोग्राम के स्टैंडर्ड आउटपुट और एरर को शेल रीडायरेक्शन पर भरोसा करने के बजाय सीधे प्लगइन की कॉन्फ़िगरेशन के भीतर एक फ़ाइल में रीडायरेक्ट करने के लिए एक `<outputFile>` कॉन्फ़िगरेशन ऑप्शन भी प्रदान करता है। यह लॉगिंग के लिए उपयोगी हो सकता है।

**संक्षेप में:**

  * इंटरैक्टिव इनपुट के लिए जहां एक उपयोगकर्ता सीधे टाइप करता है, `exec:java` और `System.in` ठीक काम करते हैं।
  * किसी फ़ाइल या पाइप से इनपुट प्रदान करने के लिए, आपको `exec:exec` पर स्विच करना होगा और अपने शेल की इनपुट रीडायरेक्शन क्षमताओं (`<`) का लाभ उठाना होगा।