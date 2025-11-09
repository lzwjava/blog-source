---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: जावा बिल्ड संस्करण संघर्षों का समाधान
translated: true
type: note
---

आप **Java 8** (क्लास फ़ाइल 52.0) के साथ बना रहे हैं, लेकिन आपके POM में कुछ बिल्ड प्लगइन्स/लाइब्रेरीज़ नए जावा के लिए कंपाइल की गई हैं। सबसे पहली समस्या **Spotless** (क्लास फ़ाइल 55.0 = Java 11) दे रही है। आपके पास कुछ अन्य Java-11+ आइटम्स भी हैं जो Spotless को हटाने पर भी समस्या देंगे (Checkstyle 10.x, Logback 1.5, और Jakarta Servlet 5 बनाम Spring 5 का javax नेमस्पेस)।

नीचे इसे ठीक करने के दो साफ तरीके दिए गए हैं। एक को चुनें और आप ठीक हो जाएंगे।

---

## विकल्प A — Java 8 पर बने रहें (Spring 5.2.x और Jetty 9.4 के साथ काम करता है)

* Java-11+ प्लगइन्स और लाइब्रेरीज़ को हटाएँ/वापस लौटाएँ।
* **javax.servlet-api 4.0.1** का उपयोग करें (Spring 5 `javax.*` का उपयोग करता है, `jakarta.*` का नहीं)।
* Jetty 9.4 (Servlet 3.1/4 युग) बनाए रखें।

इस POM को पेस्ट करें (नीचे दिए गए भाग केवल आपके POM से अलग हैं):

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x ठीक है -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>

    <!-- Test निर्भरताएँ अपरिवर्तित -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-api</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-engine</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>5.18.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>5.2.2.RELEASE</version>
      <scope>test</scope>
    </dependency>

    <!-- AOP ठीक है -->
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjrt</artifactId>
      <version>1.9.24</version>
    </dependency>
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjweaver</artifactId>
      <version>1.9.24</version>
    </dependency>

    <!-- SLF4J 2.0, Java 8+ के लिए है, ठीक है -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ Logback को Java 8-संगत वर्जन पर डाउनग्रेड करें -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ Spring 5.x + Jetty 9.4 के लिए javax servlet का उपयोग करें -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>4.0.1</version>
      <scope>provided</scope>
    </dependency>

    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.17.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- अपना exec-maven-plugin बनाए रखें यदि आपको JavadocRemover की आवश्यकता है -->
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.1</version>
        <executions>
          <execution>
            <id>remove-javadoc</id>
            <phase>compile</phase>
            <goals><goal>java</goal></goals>
            <configuration>
              <mainClass>org.lzw.JavadocRemover</mainClass>
              <arguments><argument>src/main</argument></arguments>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- ↓ Spotless को हटा दें या इसे एक Java 11+ प्रोफाइल के पीछे रख दें।
           यदि आप इसे वास्तव में Java 8 पर चलाना चाहते हैं, तो एक पुराने Spotless + JDK8 का उपयोग करें,
           लेकिन सबसे आसान है इसे अभी हटा देना। -->
      <!-- (Spotless प्लगइन ब्लॉक हटाया गया) -->

      <!-- ↓ Checkstyle: Java 8–संगत इंजन चुनें -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.1.2</version>
        <dependencies>
          <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>9.3</version>
          </dependency>
        </dependencies>
        <configuration>
          <configLocation>${project.basedir}/checks.xml</configLocation>
          <failOnViolation>true</failOnViolation>
        </configuration>
        <executions>
          <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals><goal>check</goal></goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <failOnMissingWebXml>true</failOnMissingWebXml>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.5.3</version>
      </plugin>

      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
          </execution>
        </executions>
      </plugin>

      <!-- Jetty 9.4, Java 8 + javax.servlet पर ठीक चलता है -->
      <plugin>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-maven-plugin</artifactId>
        <version>9.4.54.v20240208</version>
        <configuration>
          <httpConnector><port>8080</port></httpConnector>
          <webApp><contextPath>/</contextPath></webApp>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <!-- अपनी 'python-integration-tests' प्रोफाइल बनाए रखें,
       लेकिन ध्यान दें spring-boot-maven-plugin 3.5.0 को Java 17+ चाहिए।
       Java 8 पर बिल्ड करते समय इस प्रोफाइल को OFF छोड़ दें। -->
  <profiles>
    <profile>
      <id>python-integration-tests</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <execution>
                <id>prepare-agent-integration</id>
                <goals><goal>prepare-agent-integration</goal></goals>
                <configuration>
                  <destFile>${project.build.directory}/jacoco-it.exec</destFile>
                  <propertyName>jacoco.agent.it</propertyName>
                </configuration>
              </execution>
            </executions>
          </plugin>

          <!-- इस Boot प्लगइन को यहाँ छोड़ दें लेकिन Java 8 पर इस प्रोफाइल को सक्रिय न करें -->
          <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.5.0</version>
          </plugin>

          <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.5.1</version>
            <executions>
              <execution>
                <id>python-integration-tests</id>
                <phase>integration-test</phase>
                <goals><goal>exec</goal></goals>
                <configuration>
                  <executable>python</executable>
                  <workingDirectory>${project.basedir}</workingDirectory>
                  <arguments>
                    <argument>-m</argument><argument>unittest</argument>
                    <argument>discover</argument><argument>tests/</argument>
                    <argument>-v</argument>
                  </arguments>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>
```

फिर चलाएँ:

```bash
mvn -v                # पुष्टि करें कि JDK 1.8.x का उपयोग हो रहा है
mvn clean package
# या डेवलपमेंट के लिए
mvn jetty:run
```

---

## विकल्प B — अपने बिल्ड JDK को अपग्रेड करें (Java 17 एक अच्छा विकल्प है)

* अपने **बिल्ड** को JDK 17+ पर स्विच करें (और `mvn -v` को Java 17 दिखाना चाहिए)।
* Spotless और Checkstyle 10.x को ज्यों का त्यों बनाए रखें।
* आप `jakarta.servlet-api` को बनाए रख सकते हैं **केवल तभी** यदि आप रनटाइम को भी Jetty 11+ या Tomcat 10+ पर ले जाते हैं और अपने कोड को `jakarta.*` नेमस्पेस में माइग्रेट करते हैं (Spring 6 / Spring Boot 3 की दुनिया)। यदि आप Spring 5.2.x पर बने रहते हैं, तो `javax.servlet-api:4.0.1` और एक Servlet 4 कंटेनर का उपयोग करें।

सामान्य कमांड:

```bash
# Ubuntu पर, एक JDK 17 इंस्टॉल करें और उसे चुनें:
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # Java वर्जन 17 प्रिंट करना चाहिए
mvn clean package
```

यदि आपको Java 17 पर बिल्ड करते समय भी Java 8 बाइटकोड जनरेट करना है, तो सेट करें:

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

(लेकिन ध्यान दें: Logback 1.5 जैसी निर्भरताएँ वैसे भी Java 11+ हैं, इसलिए यदि आप उन्हें शामिल करते हैं तो आपका **रनटाइम** 11+ होना चाहिए।)

---

## यह विफल क्यों हुआ (संक्षिप्त संस्करण)

* `UnsupportedClassVersionError ... class file version 55.0` = प्लगइन/लाइब्रेरी **Java 11** के साथ कंपाइल की गई, लेकिन Maven **Java 8** के तहत चली।
* Java 8 पर आपके विशिष्ट अपराधी:

  * Spotless plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0`, Spring 5 के `javax.*` और Jetty 9.4 से मेल नहीं खाता।

---

यदि आप मुझे बताएं कि आप कौन सा रास्ता पसंद करते हैं (Java 8 पर बने रहना है या Java 17+ पर जाना है), तो मैं उस सेटअप के लिए POM को ठीक से तैयार कर दूंगा और, यदि आवश्यक हो, तो आपके `web.xml`/Spring कॉन्फ़िग और Jetty/Tomcat विकल्प के लिए न्यूनतम अंतर दूंगा।