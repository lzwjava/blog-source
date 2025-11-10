---
audio: false
generated: true
lang: ar
layout: post
title: هيكلة مافن لمشاكل يو في إيه
translated: true
type: note
---

شكرًا لك على مشاركة الهيكل الدقيق لمجلدك الفرعي `uva/106`. يبدو أن مشروعك له هيكل أكثر تفصيلاً حيث أن كل مسألة في UVA (مثل `106`) هي مجلد منفصل يحتوي على مجلد `src` الخاص به والذي بداخله ملف `Main.java` وربما ملفات إدخال مثل `1.in`. هذا يشير إلى أن كل مسألة قد يتم التعامل معها كمشروع فرعي أو وحدة منفصلة. لاستيعاب هذا في إعداد Maven متعدد الوحدات، يمكننا إما:
1.  التعامل مع كل مجلد مسألة (مثل `uva/106`) على أنه وحدة فرعية خاصة بـ Maven.
2.  الاحتفاظ بـ `uva` كوحدة واحدة وتنظيم ملفات المسائل داخل مجلد `src/main/java` الخاص بها.

نظرًا لعدد مسائل UVA (كما رأيت في قائمتك السابقة: `100`، `10000`، إلخ)، فإن إنشاء وحدة Maven منفصلة لكل مسألة قد يؤدي إلى عدد كبير من الوحدات، مما قد يكون مرهقًا. بدلاً من ذلك، سأقترح هيكلاً حيث تكون `uva` وحدة واحدة، ويتم تنظيم `Main.java` لكل مسألة داخل `uva/src/main/java` تحت هيكل حزمة (مثل `com.algorithm.solutions.uva.p106` للمسألة 106). هذا يحافظ على إمكانية إدارة المشروع مع الاستفادة من مزايا Maven.

ومع ذلك، سأقدم أيضًا نهجًا بديلاً حيث تكون كل مسألة وحدة فرعية منفصلة إذا كنت تفضل هذا المستوى من التفصيل. أدناه، سأقوم بتحديث ملفات `pom.xml` بناءً على هيكلك وسأقدم خطوات لإعادة تنظيم ملفاتك.

---

### الخيار 1: وحدة `uva` واحدة مع حزم للمسائل

#### الهيكل المحدث للمجلدات
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── pom.xml
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── com/algorithm/solutions/uva/
│   │               ├── p100/
│   │               │   └── Main.java
│   │               ├── p106/
│   │               │   └── Main.java
│   │               ├── p10000/
│   │               │   └── Main.java
│   │               └── (etc.)
│   └── resources/
│       └── uva/
│           ├── p100/
│           │   └── 1.in
│           ├── p106/
│           │   └── 1.in
│           └── (etc.)
└── README.md
```

#### ملف `pom.xml` الرئيسي (الجذر: `algorithm-solutions/pom.xml`)
هذا يبقى كما هو إلى حد كبير كما كان من قبل، مع تعريف `nowcoder` و `uva` كوحدات.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### وحدة nowcoder الفرعية `pom.xml` (`nowcoder/pom.xml`)
هذا لم يتغير عن الرد السابق، بافتراض أن ملفات `nowcoder` تم نقلها إلى `src/main/java/com/algorithm/solutions/nowcoder/`.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>nowcoder</artifactId>
    <name>Nowcoder Solutions</name>
    <description>Solutions for Nowcoder algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.nowcoder.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### وحدة UVA الفرعية `pom.xml` (`uva/pom.xml`)
تتضمن هذه الوحدة دليل `resources` لملفات الإدخال مثل `1.in`. يتم تنظيم ملفات `Main.java` لكل مسألة في حزم.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva</artifactId>
    <name>UVA Solutions</name>
    <description>Solutions for UVA algorithm problems</description>

    <build>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### تنظيم الملفات
- **نقل ملفات Java**:
  - لكل مسألة (مثل `uva/106/src/Main.java`)، انقل `Main.java` إلى `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - قم بتحديث ملف `Main.java` ليشمل تعريف الحزمة:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... existing code ...
    }
    ```
  - افعل هذا لجميع المسائل (مثل `p100`، `p10000`، إلخ.).

- **نقل ملفات الإدخال**:
  - انقل ملفات الإدخال مثل `uva/106/1.in` إلى `uva/src/main/resources/uva/p106/1.in`.
  - هذا يسمح لـ Maven بتضمين هذه الملفات في الـ JAR، ليتم الوصول إليها عبر `ClassLoader.getResource()` أو ما شابه في كود Java الخاص بك.

#### تشغيل برنامج
لتشغيل مسألة UVA محددة (مثل المسألة 106):
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### الخيار 2: كل مسألة UVA كوحدة فرعية
إذا كنت تفضل أن تكون كل مسألة UVA (مثل `106`، `100`) وحدة Maven خاصة بها، فإليك كيفية إعداد ذلك. هذا أكثر تفصيلاً ولكنه يزيد من عدد ملفات `pom.xml`.

#### الهيكل المحدث للمجلدات
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── 106/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p106/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── 1.in
│   ├── 100/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p100/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── (input files, if any)
│   └── (other problem directories)
└── README.md
```

#### ملف `pom.xml` الرئيسي (الجذر: `algorithm-solutions/pom.xml`)
أضف كل مسألة كوحدة.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva/106</module>
        <module>uva/100</module>
        <module>uva/10000</module>
        <module>uva/10006</module>
        <module>uva/10008</module>
        <module>uva/10009</module>
        <module>uva/10012</module>
        <module>uva/10013</module>
        <module>uva/10018</module>
        <module>uva/10019</module>
        <module>uva/10026</module>
        <module>uva/10033</module>
        <module>uva/10034</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### وحدة nowcoder الفرعية `pom.xml` (`nowcoder/pom.xml`)
نفس ما ورد أعلاه (بدون تغيير).

#### وحدة مسألة UVA 106 الفرعية `pom.xml` (`uva/106/pom.xml`)
كل مسألة لها ملف `pom.xml` خاص بها. إليك مثال لـ `uva/106`:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva-106</artifactId>
    <name>UVA Problem 106</name>
    <description>Solution for UVA problem 106</description>

    <build>
        <resources>
            <resource>
                <directory>resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.uva.p106.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **كرر للمسائل الأخرى**: أنشئ ملفات `pom.xml` مشابهة لـ `uva/100`، `uva/10000`، إلخ، مع تعديل `artifactId` (مثل `uva-100`)، و `name`، و `mainClass` (مثل `com.algorithm.solutions.uva.p100.Main`).

#### تنظيم الملفات
- **نقل ملفات Java**:
  - بالنسبة لـ `uva/106/src/Main.java`، انقل إلى `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - أضف تعريف الحزمة:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... existing code ...
    }
    ```
- **نقل ملفات الإدخال**:
  - انقل `uva/106/1.in` إلى `uva/106/resources/1.in`.

#### تشغيل برنامج
لتشغيل المسألة 106:
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### التوصية
- **الخيار 1 (وحدة `uva` واحدة)** هو الأبسط والأكثر قابلية للتوسع، خاصة إذا كان لديك العديد من مسائل UVA. فهو يتجنب إنشاء عدد كبير من ملفات `pom.xml` ويحافظ على هيكل المشروع نظيفًا. استخدم الحزم لتنظيم المسائل منطقيًا.
- **الخيار 2 (وحدات لكل مسألة)** هو الأفضل إذا كنت تريد أن تكون كل مسألة مستقلة تمامًا (مثلًا للنشر أو الاختبار المنفصل). ومع ذلك، فإنه يتطلب المزيد من الصيانة بسبب عدد الوحدات.

### خطوات تنفيذ الخيار 1
1.  **إنشاء هيكل المجلدات**:
    - شغّل هذه الأوامر في جذر `algorithm-solutions`:
      ```bash
      mkdir -p uva/src/main/java/com/algorithm/solutions/uva
      mkdir -p uva/src/main/resources/uva
      mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
      ```
2.  **نقل الملفات**:
    - لكل مسألة UVA (مثل `106`):
      ```bash
      mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
      mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
      mkdir -p uva/src/main/resources/uva/p106
      mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
      ```
    - لـ `nowcoder`:
      ```bash
      mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
      ```
3.  **تحديث ملفات Java**:
    - أضف تعريفات الحزمة المناسبة (مثل `package com.algorithm.solutions.uva.p106;` لـ `uva/106/Main.java`).
4.  **إضافة ملفات `pom.xml`**:
    - ضع ملف `pom.xml` الرئيسي في `algorithm-solutions/`.
    - ضع ملفات `nowcoder/pom.xml` و `uva/pom.xml` كما هو موضح.
5.  **البناء**:
    ```bash
    mvn clean install
    ```

### ملاحظات
- **ملفات الإدخال**: إذا كان `Main.java` الخاص بك يقرأ ملفات الإدخال مثل `1.in`، فقم بتحديث الكود للوصول إليها عبر `getClass().getResource("/uva/p106/1.in")` أو ما شابه، نظرًا لأنها موجودة الآن في `src/main/resources`.
- **تجاهل ملفات `.iml`**: أضف ملف `.gitignore` يحتوي على `*.iml` لاستبعاد ملفات مشروع IntelliJ من نظام التحكم في الإصدار.
- **المجلدات الأخرى**: بالنسبة لـ `codeforces`، `hacker_rank`، إلخ، يمكنك إنشاء وحدات مشابهة عندما تكون مستعدًا. دعني أعرف إذا كنت بحاجة إلى ملفات `pom.xml` لها.
- **إصدار Java**: اضبط `<maven.compiler.source>` و `<maven.compiler.target>` إذا كنت تستخدم إصدار Java مختلف.

إذا كنت تفضل الخيار 2 أو تحتاج إلى مساعدة في مسائل محددة (مثل تعديل `Main.java` لتحميل الموارد)، دعني أعرف!