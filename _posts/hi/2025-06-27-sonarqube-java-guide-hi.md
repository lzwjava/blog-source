---
audio: false
generated: true
lang: hi
layout: post
title: जावा और स्प्रिंग प्रोजेक्ट्स के लिए सोनारक्यूब में महारत हासिल करना
translated: true
type: note
---

# Java और Spring प्रोजेक्ट्स के साथ SonarQube का उपयोग करने की व्यापक गाइड

## परिचय
SonarQube कोड गुणवत्ता के निरंतर निरीक्षण के लिए एक ओपन-सोर्स प्लेटफॉर्म है। यह बग्स, कोड स्मेल्स, कमजोरियों का पता लगाने और कोड कवरेज की गणना करने के लिए स्टैटिक कोड विश्लेषण करता है। यह गाइड एक Java Spring प्रोजेक्ट में SonarQube को सेट अप और उपयोग करने का एक व्यापक अवलोकन प्रदान करती है, जिसमें इंस्टालेशन, कॉन्फ़िगरेशन, एकीकरण और सर्वोत्तम प्रथाएं शामिल हैं।

## विषय सूची
1. [SonarQube क्या है?](#sonarqube-क्या-है)
2. [आवश्यक शर्तें](#आवश्यक-शर्तें)
3. [SonarQube इंस्टॉल करना](#sonarqube-इंस्टॉल-करना)
4. [Java Spring प्रोजेक्ट सेट अप करना](#java-spring-प्रोजेक्ट-सेट-अप-करना)
5. [प्रोजेक्ट के लिए SonarQube कॉन्फ़िगर करना](#प्रोजेक्ट-के-लिए-sonarqube-कॉन्फ़िगर-करना)
6. [SonarQube विश्लेषण चलाना](#sonarqube-विश्लेषण-चलाना)
7. [SonarQube परिणामों की व्याख्या](#sonarqube-परिणामों-की-व्याख्या)
8. [सर्वोत्तम प्रथाएं](#सर्वोत्तम-प्रथाएं)
9. [सामान्य समस्याओं का निवारण](#सामान्य-समस्याओं-का-निवारण)
10. [निष्कर्ष](#निष्कर्ष)

## SonarQube क्या है?
SonarQube एक टूल है जो स्रोत कोड का विश्लेषण करके निरंतर कोड गुणवत्ता निरीक्षण प्रदान करता है:
- **बग्स**: कोड में संभावित त्रुटियां।
- **कोड स्मेल्स**: रखरखाव संबंधी समस्याएं जो तकनीकी ऋण का कारण बन सकती हैं।
- **कमजोरियां**: सुरक्षा संबंधी समस्याएं जिनका दुरुपयोग किया जा सकता है।
- **कोड कवरेज**: यूनिट टेस्ट्स द्वारा कवर किए गए कोड का प्रतिशत।
- **डुप्लिकेशन**: दोहराए गए कोड ब्लॉक जिन्हें रिफैक्टर किया जा सकता है।

यह कई भाषाओं का समर्थन करता है, जिसमें Java शामिल है, और Maven और Gradle जैसे बिल्ड टूल्स के साथ-साथ CI/CD पाइपलाइनों के साथ निर्बाध रूप से एकीकृत होता है।

## आवश्यक शर्तें
SonarQube सेट अप करने से पहले, सुनिश्चित करें कि आपके पास है:
- **Java Development Kit (JDK)**: वर्जन 11 या बाद का (SonarQube को Java 11 या 17 की आवश्यकता होती है)।
- **Maven या Gradle**: Java Spring प्रोजेक्ट के लिए बिल्ड टूल।
- **SonarQube सर्वर**: वर्जन 9.9 LTS या बाद का (अधिकांश उपयोग के मामलों के लिए Community Edition पर्याप्त है)।
- **SonarScanner**: विश्लेषण चलाने के लिए CLI टूल।
- **डेटाबेस**: SonarQube को एक डेटाबेस (जैसे, PostgreSQL, MySQL, या परीक्षण के लिए एम्बेडेड H2) की आवश्यकता होती है।
- **Spring प्रोजेक्ट**: एक कार्यशील Spring Boot या Spring Framework प्रोजेक्ट।
- **IDE**: विकास के लिए IntelliJ IDEA, Eclipse, या VS Code।

## SonarQube इंस्टॉल करना

### चरण 1: SonarQube डाउनलोड और इंस्टॉल करें
1. **SonarQube डाउनलोड करें**:
   - [SonarQube डाउनलोड पेज](https://www.sonarqube.org/downloads/) पर जाएं।
   - अपनी आवश्यकताओं के आधार पर Community Edition (मुफ्त) या कोई अन्य संस्करण चुनें।
   - ZIP फ़ाइल (जैसे, `sonarqube-9.9.0.zip`) डाउनलोड करें।

2. **ZIP एक्सट्रैक्ट करें**:
   - डाउनलोड की गई फ़ाइल को एक डायरेक्टरी में अनज़िप करें, जैसे, `/opt/sonarqube` या `C:\sonarqube`।

3. **डेटाबेस कॉन्फ़िगर करें**:
   - SonarQube को एक डेटाबेस की आवश्यकता होती है। प्रोडक्शन के लिए, PostgreSQL या MySQL का उपयोग करें। परीक्षण के लिए, एम्बेडेड H2 डेटाबेस पर्याप्त है।
   - PostgreSQL के लिए उदाहरण:
     - PostgreSQL इंस्टॉल करें और एक डेटाबेस बनाएं (जैसे, `sonarqube`)।
     - SonarQube कॉन्फ़िगरेशन फ़ाइल (`conf/sonar.properties`) अपडेट करें:
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **SonarQube शुरू करें**:
   - SonarQube डायरेक्टरी (`bin/<platform>`) में नेविगेट करें।
   - स्टार्टअप स्क्रिप्ट चलाएं:
     - Linux/Mac पर: `./sonar.sh start`
     - Windows पर: `StartSonar.bat`
   - SonarQube को `http://localhost:9000` (डिफ़ॉल्ट पोर्ट) पर एक्सेस करें।

5. **लॉग इन करें**:
   - डिफ़ॉल्ट क्रेडेंशियल्स: `admin/admin`।
   - पहले लॉगिन के बाद पासवर्ड बदलें।

### चरण 2: SonarScanner इंस्टॉल करें
1. **SonarScanner डाउनलोड करें**:
   - [SonarQube Scanner पेज](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/) से डाउनलोड करें।
   - एक डायरेक्टरी में एक्सट्रैक्ट करें, जैसे, `/opt/sonar-scanner`।

2. **एनवायरनमेंट वेरिएबल्स कॉन्फ़िगर करें**:
   - अपने PATH में SonarScanner जोड़ें:
     - Linux/Mac पर: `export PATH=$PATH:/opt/sonar-scanner/bin`
     - Windows पर: सिस्टम PATH में `C:\sonar-scanner\bin` जोड़ें।

3. **इंस्टालेशन सत्यापित करें**:
   - इंस्टालेशन की पुष्टि के लिए `sonar-scanner --version` चलाएं।

## Java Spring प्रोजेक्ट सेट अप करना
इस गाइड के लिए, हम Maven के साथ एक Spring Boot प्रोजेक्ट का उपयोग करेंगे। Gradle या गैर-Boot Spring प्रोजेक्ट्स के लिए चरण समान हैं।

1. **Spring Boot प्रोजेक्ट बनाएं**:
   - [Spring Initializer](https://start.spring.io/) का उपयोग करके एक प्रोजेक्ट बनाएं:
     - निर्भरताएं: Spring Web, Spring Data JPA, H2 Database, Spring Boot Starter Test।
     - बिल्ड टूल: Maven।
   - प्रोजेक्ट डाउनलोड करें और एक्सट्रैक्ट करें।

2. **यूनिट टेस्ट्स जोड़ें**:
   - सुनिश्चित करें कि आपके प्रोजेक्ट में कोड कवरेज मापने के लिए यूनिट टेस्ट्स हैं।
   - उदाहरण टेस्ट क्लास:
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **कोड कवरेज के लिए Jacoco जोड़ें**:
   - कोड कवरेज रिपोर्ट्स जनरेट करने के लिए `pom.xml` में JaCoCo Maven प्लगइन जोड़ें:
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## प्रोजेक्ट के लिए SonarQube कॉन्फ़िगर करना

1. **SonarQube प्रोजेक्ट बनाएं**:
   - SonarQube में लॉग इन करें (`http://localhost:9000`)।
   - **Create Project** > **Manually** पर क्लिक करें।
   - एक **Project Key** (जैसे, `my-spring-project`) और **Display Name** प्रदान करें।
   - प्रमाणीकरण के लिए एक टोकन जनरेट करें (जैसे, `my-token`)।

2. **`sonar-project.properties` कॉन्फ़िगर करें**:
   - अपने Spring प्रोजेक्ट की रूट में, एक `sonar-project.properties` फ़ाइल बनाएं:
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **Maven एकीकरण (वैकल्पिक)**:
   - `sonar-project.properties` के बजाय, आप `pom.xml` में SonarQube कॉन्फ़िगर कर सकते हैं:
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## SonarQube विश्लेषण चलाना

1. **SonarScanner का उपयोग करना**:
   - प्रोजेक्ट रूट में नेविगेट करें।
   - चलाएं:
     ```bash
     sonar-scanner
     ```
   - सुनिश्चित करें कि विश्लेषण से पहले टेस्ट्स निष्पादित हो चुके हैं (Maven प्रोजेक्ट्स के लिए `mvn test`)।

2. **Maven का उपयोग करना**:
   - चलाएं:
     ```bash
     mvn clean verify sonar:sonar
     ```
   - यह कमांड कोड को कंपाइल करती है, टेस्ट्स चलाती है, कवरेज रिपोर्ट्स जनरेट करती है और परिणाम SonarQube को भेजती है।

3. **परिणाम सत्यापित करें**:
   - SonarQube (`http://localhost:9000`) खोलें और अपने प्रोजेक्ट पर नेविगेट करें।
   - विश्लेषण परिणामों के लिए डैशबोर्ड जांचें।

## SonarQube परिणामों की व्याख्या
SonarQube डैशबोर्ड प्रदान करता है:
- **अवलोकन**: समस्याओं, कवरेज और डुप्लिकेशन का सारांश।
- **समस्याएं**: गंभीरता (ब्लॉकर, क्रिटिकल, मेजर, आदि) के साथ बग्स, कमजोरियों और कोड स्मेल्स की सूची।
- **कोड कवरेज**: टेस्ट्स द्वारा कवर किए गए कोड का प्रतिशत (JaCoCo के माध्यम से)।
- **डुप्लिकेशन**: दोहराए गए कोड ब्लॉक।
- **गुणवत्ता द्वार**: पूर्वनिर्धारित सीमाओं (जैसे, कवरेज > 80%) के आधार पर पास/फेल स्थिति।

### उदाहरण कार्य:
- **बग्स ठीक करें**: नल पॉइंटर डेरिफरेंस जैसे गंभीर मुद्दों को संबोधित करें।
- **कोड स्मेल्स रिफैक्टर करें**: जटिल विधियों को सरल बनाएं या अनुपयोगी कोड हटाएं।
- **कवरेज सुधारें**: अनकवर्ड कोड के लिए अतिरिक्त यूनिट टेस्ट्स लिखें।

## सर्वोत्तम प्रथाएं
1. **CI/CD के साथ एकीकृत करें**:
   - अपनी CI/CD पाइपलाइन (जैसे, Jenkins, GitHub Actions) में SonarQube विश्लेषण जोड़ें।
   - उदाहरण GitHub Actions वर्कफ़्लो:
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **गुणवत्ता द्वार परिभाषित करें**:
   - SonarQube में कोड कवरेज, बग्स और कमजोरियों के लिए सीमाएं निर्धारित करें।
   - उदाहरण: बिल्ड फेल करें यदि कवरेज < 80% या गंभीर समस्याएं मौजूद हैं।

3. **SonarLint का उपयोग करें**:
   - विकास के दौरान समस्याओं को पकड़ने के लिए अपने IDE (जैसे, IntelliJ IDEA) में SonarLint प्लगइन इंस्टॉल करें।

4. **नियमित विश्लेषण**:
   - समस्याओं को जल्दी पकड़ने के लिए प्रत्येक कमिट पर या दैनिक आधार पर SonarQube विश्लेषण चलाएं।

5. **नियम अनुकूलित करें**:
   - अपनी प्रोजेक्ट की आवश्यकताओं के अनुरूप SonarQube नियमों को तैयार करें (जैसे, अप्रासंगिक नियमों को अक्षम करें या कस्टम नियम जोड़ें)।

## सामान्य समस्याओं का निवारण
1. **विश्लेषण अपलोड करने में विफल**:
   - कॉन्फ़िगरेशन में `sonar.host.url` और `sonar.token` जांचें।
   - सुनिश्चित करें कि SonarQube सर्वर चल रहा है (`http://localhost:9000`)।

2. **कोई कोड कवरेज नहीं**:
   - सत्यापित करें कि JaCoCo प्लगइन `pom.xml` में सही ढंग से कॉन्फ़िगर है।
   - `jacoco.exec` जनरेट करने के लिए विश्लेषण से पहले `mvn test` चलाएं।

3. **डेटाबेस कनेक्शन त्रुटियां**:
   - `sonar.properties` में डेटाबेस क्रेडेंशियल्स की पुष्टि करें।
   - सुनिश्चित करें कि डेटाबेस सर्वर चल रहा है।

4. **मेमोरी की कमी**:
   - `sonar.properties` में JVM मेमोरी बढ़ाएं:
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## निष्कर्ष
SonarQube Java Spring प्रोजेक्ट्स में कोड गुणवत्ता बनाए रखने के लिए एक शक्तिशाली टूल है। इसे अपने विकास वर्कफ़्लो में एकीकृत करके, आप समस्याओं को जल्दी पकड़ सकते हैं, कोड रखरखाव क्षमता में सुधार कर सकते हैं और मजबूत सुरक्षा सुनिश्चित कर सकते हैं। नियमित विश्लेषण, CI/CD एकीकरण और SonarLint जैसी सर्वोत्तम प्रथाओं के संयोजन से आपको एक उच्च-गुणवत्ता वाला कोडबेस बनाए रखने में मदद मिलेगी।