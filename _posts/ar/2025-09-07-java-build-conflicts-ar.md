---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: حل تضارب إصدارات بناء جافا
translated: true
type: note
---

أنت تبني باستخدام **Java 8** (إصدار ملف الفئة 52.0)، لكن بعض إضافات البناء والمكتبات في ملف POM الخاص بك تم تجميعها لإصدارات جافا أحدث. أول ما سيفشل هو **Spotless** (إصدار ملف الفئة 55.0 = Java 11). لديك أيضًا بعض العناصر الأخرى التي تتطلب Java 11+ والتي ستسبب مشاكل حتى لو تمت إزالة Spotless (مثل Checkstyle 10.x و Logback 1.5 و Jakarta Servlet 5 مقابل namespace javax في Spring 5).

فيما يلي طريقتان نظيفتان لإصلاح المشكلة. اختر واحدة وسيكون كل شيء على ما يرام.

---

## الخيار أ — البقاء على جافا 8 (يعمل مع Spring 5.2.x و Jetty 9.4)

* قم بإزالة/تراجع عن الإضافات والمكتبات التي تتطلب Java 11+.
* استخدم **javax.servlet-api 4.0.1** (Spring 5 يستخدم `javax.*`، وليس `jakarta.*`).
* حافظ على استخدام Jetty 9.4 (من عصر Servlet 3.1/4).

الصق هذا الملف POM (فقط الأجزاء التالية تختلف عن ملفك):

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x يعمل بشكل جيد -->
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

    <!-- تبعيات الاختبار لم تتغير -->
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

    <!-- AOP جيد -->
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

    <!-- SLF4J 2.0 متوافق مع Java 8+، جيد -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ ترقية Logback إلى إصدار متوافق مع Java 8 -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ استخدم javax servlet لـ Spring 5.x + Jetty 9.4 -->
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
      <!-- احتفظ بـ exec-maven-plugin إذا كنت تحتاج JavadocRemover -->
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

      <!-- ↓ أزل Spotless أو ضعه خلف ملف تعريف (profile) يتطلب Java 11+.
           إذا كنت تريد استخدامه على Java 8 حقًا، فاستخدم إصدار قديم من Spotless مع JDK8،
           ولكن أبسط حل هو إزالته الآن. -->
      <!-- (تمت إزالة كتلة إضافة Spotless) -->

      <!-- ↓ Checkstyle: اختر محرك متوافق مع Java 8 -->
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

      <!-- Jetty 9.4 يعمل بشكل جيد على Java 8 + javax.servlet -->
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

  <!-- احتفظ بملف التعريف 'python-integration-tests'،
       لكن لاحظ أن spring-boot-maven-plugin 3.5.0 يحتاج إلى Java 17+.
       اترك هذا الملف غير مفعل عند البناء باستخدام Java 8. -->
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

          <!-- اترك إضافة Boot هنا ولكن لا تفعل هذا الملف على Java 8 -->
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

ثم شغل:

```bash
mvn -v                # تأكد من استخدام JDK 1.8.x
mvn clean package
# أو للتطوير
mvn jetty:run
```

---

## الخيار ب — ترقية JDK البناء (Java 17 نقطة جيدة)

* غيّر **بيئة البناء** إلى JDK 17+ (ويجب أن يظهر `mvn -v` إصدار Java 17).
* احتفظ بـ Spotless و Checkstyle 10.x كما هما.
* يمكنك الاحتفاظ بـ `jakarta.servlet-api` **فقط إذا** قمت أيضًا بنقل بيئة التشغيل إلى Jetty 11+ أو Tomcat 10+ وهاجرت الكود الخاص بك إلى namespaces `jakarta.*` (عالم Spring 6 / Spring Boot 3). إذا بقيت على Spring 5.2.x، فاستخدم `javax.servlet-api:4.0.1` وحاوية Servlet 4 بدلاً من ذلك.

الأوامر النموذجية:

```bash
# على Ubuntu، قم بتثبيت JDK 17 واختره:
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # يجب أن يطبع إصدار Java 17
mvn clean package
```

إذا كان يجب عليك仍然 إنشاء bytecode خاص بـ Java 8 أثناء البناء على Java 17، فاضبط:

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

(ولكن لاحظ: التبعيات مثل Logback 1.5 تتطلب Java 11+ على أي حال، لذا يجب أن تكون **بيئة التشغيل** 11+ إذا قمت بتضمينها.)

---

## سبب الفشل (نسخة مختصرة)

* `UnsupportedClassVersionError ... class file version 55.0` = تم تجميع الإضافة/المكتبة باستخدام **Java 11**، ولكن Maven يعمل تحت **Java 8**.
* العناصر المحددة التي تسبب المشكلة على Java 8:

  * Spotless plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0` لا يتطابق مع `javax.*` في Spring 5 و Jetty 9.4.

---

إذا أخبرتني بالمسار الذي تفضله (البقاء على Java 8 مقابل الانتقال إلى Java 17+)، سأضبط ملف POM بدقة لهذا الإعداد، وإذا لزم الأمر، سأعطيك أقل الاختلافات المطلوبة لملف `web.xml`/إعداد Spring وخيار Jetty/Tomcat الخاص بك.