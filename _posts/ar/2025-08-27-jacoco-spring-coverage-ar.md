---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إعداد تغطية سبرينغ متعدد الوحدات باستخدام جاكوكو
translated: true
type: note
---

ممتاز — يعمل JaCoCo بشكل جيد مع مشروع Spring متعدد الوحدات. ستحتاج إلى:

1. تغطية اختبارات الوحدة لكل وحدة؛
2. تقرير مجمع في المستوى الرئيسي (Parent)؛
3. ملف تعريف اختياري لدمج تغطية **التكامل** (مثلاً، تشغيل Liberty+EAR الذي يتم اختباره باختبارات Python).

فيما يلي إعداد مجرب ومضمون يمكنك استخدامه مباشرة.

---

### ملف `pom.xml` الرئيسي (بتغليف `pom`)

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.myco.chat</groupId>
  <artifactId>chat-parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>ChatCommon</module>
    <module>ChatLib</module>
    <module>ChatCore</module>
    <module>ChatWeb</module>
  </modules>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.12</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-failsafe-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>

  <!-- تقرير مجمع لجميع اختبارات الوحدة في جميع الوحدات -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- هذا يُفعّل 'report-aggregate' عند تشغيل 'mvn verify' في المستوى الرئيسي -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- عوامل تصفية عالمية اختيارية -->
              <excludes>
                <exclude>**/*Application.class</exclude>
                <exclude>**/*Configuration.class</exclude>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </reportSet>
        </plugins>
      </plugin>
    </plugins>
  </reporting>

  <!-- ملف تعريف لإضافة تغطية التكامل (مثلاً، Liberty + اختبارات Python) -->
  <profiles>
    <profile>
      <id>it-coverage</id>
      <activation><activeByDefault>false</activeByDefault></activation>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <!-- إنشاء تقرير مجمع يقرأ أيضًا ملفات .exec الخارجية -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- الإشارة إلى ملف .exec واحد أو أكثر التي أنشأها وكيل JVM الخاص بـ Liberty -->
                  <dataFiles>
                    <!-- مسارات مثاليه؛ عدلها لتناسب مسار CI/Liberty الخاص بك -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- يمكنك إضافة المزيد من إدخالات dataFile إذا كنت تجمع بيانات من عدة عقد وتريدها جميعًا -->
                  </dataFiles>
                  <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate-it</outputDirectory>
                  <reports>
                    <xml>true</xml>
                    <html>true</html>
                    <csv>false</csv>
                  </reports>
                  <excludes>
                    <exclude>**/generated/**</exclude>
                  </excludes>
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

---

### كل وحدة فرعية (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

```xml
<project>
  <parent>
    <groupId>com.myco.chat</groupId>
    <artifactId>chat-parent</artifactId>
    <version>1.0.0</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>ChatCommon</artifactId>
  <packaging>jar</packaging>

  <build>
    <plugins>
      <!-- إرفاق الوكيل لاختبارات الوحدة في هذه الوحدة -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- وضع argLine في خاصية مسماة، حتى نتمكن من مزجها مع وسائط أخرى -->
              <propertyName>jacocoArgLine</propertyName>
              <append>true</append>
              <excludes>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
            <configuration>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
            </configuration>
          </execution>
          <!-- اختياري: فرض حد أدنى للتغطية -->
          <execution>
            <id>check</id>
            <goals><goal>check</goal></goals>
            <configuration>
              <rules>
                <rule>
                  <element>PACKAGE</element>
                  <limits>
                    <limit>
                      <counter>LINE</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.60</minimum>
                    </limit>
                    <limit>
                      <counter>BRANCH</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.40</minimum>
                    </limit>
                  </limits>
                </rule>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- التأكد من أن Surefire يلتقط الوكيل -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- (اختياري) Failsafe لاختبارات التكامل على مستوى الوحدة -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${failsafeArgLine}</argLine>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

> افعل نفس الشيء في `ChatLib`، و `ChatCore`، و `ChatWeb`.
> بالنسبة لـ `ChatWeb` (Spring Boot WAR/JAR)، الإعداد مطابق.

---

### كيفية التشغيل

**تغطية اختبارات الوحدة عبر جميع الوحدات (تقرير XML مجمع في المستوى الرئيسي):**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**تغطية التكامل من Liberty واختبارات Python:**

1.  ابدأ تشغيل Liberty مع وكيل JaCoCo (كما نوقش سابقًا)، شغّل اختبارات Python، أوقف التشغيل أو انقل البيانات.
    تأكد من أن ملف `.exec` يتم حفظه في `${project.basedir}/.jacoco/jacoco-it.exec` (أو قم بتحديث هذا المسار في ملف التعريف الرئيسي).
2.  ابنِ التقرير المجمع متضمناً بيانات التكامل:

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### ملاحظات توفر الوقت

*   **يعمل التجميع فقط من المستوى الرئيسي** (بتغليف `pom`) مع الوحدات المعلنة. شغّل `mvn` من الدليل الرئيسي.
*   **يتم إنتاج XML** (`jacoco.xml`) عند تمكينه في `<reports>`؛ هذا ما يستخدمه Codecov/Sonar.
*   إذا قمت بجمع ملفات `.exec` متعددة (مثلاً، عدة عقد لـ Liberty)، فإما:

    *   اذكرها جميعًا تحت `<dataFiles>…</dataFiles>` في ملف التعريف `it-coverage`، أو
    *   ادمجها أولاً (باستخدام `jacococli.jar merge …`) ثم أشر إلى الملف المدمج.
*   لا تُشِر `classfiles` إلى ملف EAR؛ يحتاج تقرير JaCoCo إلى **الفئات المترجمة للوحدات** (`*/target/classes`) والمصادر — يتم التعامل مع هذا تلقائيًا بواسطة `report-aggregate`.
*   إذا كان Surefire يضبط `argLine` الخاص به أيضًا، حافظ على `${jacocoArgLine}` في المقدمة حتى لا يفقد الوكيل.

إذا شاركت معي جذور الحزم الدقيقة للوحدات الخاصة بك وأين ينتهي المطاف بملف `.exec` الخاص بـ Liberty، يمكنني تخصيص `<dataFiles>` وأي استثناءات بحيث يكون ملف XML المجمع الخاص بك نظيفًا وجاهزًا لـ CI.