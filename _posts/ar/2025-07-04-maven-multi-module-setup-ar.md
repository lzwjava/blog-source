---
audio: false
generated: true
lang: ar
layout: post
title: تحويل المستودع إلى مافن متعدد الوحدات
translated: true
type: note
---

لتحويل مستودع `algorithm-solutions` الخاص بك إلى مشروع جافا متعدد الوحدات المدار بواسطة Maven، ستحتاج إلى ملف `pom.xml` أب في الدليل الجذري وملفات `pom.xml` فردية لكل وحدة فرعية (`nowcoder` و `uva`). سيحدد ملف `pom.xml` الأب التكوينات المشتركة ويدير الوحدات الفرعية، بينما يتعامل ملف `pom.xml` لكل وحدة فرعية مع إعداداته الخاصة.

أدناه، سأقدم ملفات `pom.xml` للمشروع الأب والوحدتين الفرعيتين. سأفترض ما يلي:
- يستخدم المشروع Java 17 (إصدار شائع للمشاريع الحديثة؛ قم بالتعديل إذا لزم الأمر).
- تحتوي أدلة `nowcoder` و `uva` على ملفات مصدر جافا في بنية Maven قياسية (`src/main/java`).
- لا توجد تبعيات خارجية مطلوبة حاليًا، لكن الهيكل يسمح بالإضافة السهلة.
- سيتم تجميع كل وحدة فرعية كـ JAR (نظرًا لأن هذه الحلول الخوارزمية قائمة بذاتها على الأرجح).

### هيكل الدليل
بعد الإعداد، يجب أن يبدو هيكل الدليل الخاص بك كما يلي:

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (ملفات الجافا الخاصة بك، مثال: Main.java، nc140، إلخ)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (ملفات الجافا الخاصة بك، مثال: 100.java، 10000.java، إلخ)
└── README.md
```

### ملف `pom.xml` الأب
يوجد هذا الملف في الدليل الجذري (`algorithm-solutions/pom.xml`). يحدد المشروع الأب، ويسرد الوحدات الفرعية، ويضع التكوينات المشتركة مثل إصدار جافا وإعدادات المترجم.

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

### وحدة Nowcoder الفرعية `pom.xml`
يوجد هذا الملف في دليل `nowcoder` (`nowcoder/pom.xml`). يرث من الملف الأب ويحدد تفاصيل الـ artifact الخاصة به.

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
                            <mainClass>Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### وحدة UVA الفرعية `pom.xml`
يوجد هذا الملف في دليل `uva` (`uva/pom.xml`). هو أيضًا يرث من الملف الأب ويحدد تفاصيل الـ artifact الخاصة به. نظرًا لأن حلول UVA عادةً لا تحتوي على فئة `Main` واحدة (قد يكون كل مشكلة برنامجًا قائمًا بذاته)، لن أحدد فئة رئيسية هنا، ولكن يمكنك إضافة واحدة إذا لزم الأمر.

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

### خطوات الإعداد
1.  **إنشاء هيكل دليل Maven**:
    *   انقل ملفات الجافا الخاصة بك في `nowcoder` إلى `nowcoder/src/main/java/`.
    *   انقل ملفات الجافا الخاصة بك في `uva` إلى `uva/src/main/java/`.
    *   على سبيل المثال، يجب أن يكون `nowcoder/Main.java` في `nowcoder/src/main/java/Main.java`.

2.  **ضع ملفات `pom.xml`**:
    *   ضع ملف `pom.xml` الأب في الدليل الجذري `algorithm-solutions`.
    *   ضع ملف `nowcoder/pom.xml` في دليل `nowcoder`.
    *   ضع ملف `uva/pom.xml` في دليل `uva`.

3.  **بناء المشروع**:
    *   انتقل إلى الدليل الجذري `algorithm-solutions` في الطرفية.
    *   قم بتشغيل `mvn clean install` لبناء كلا الوحدتين الفرعيتين.

4.  **تشغيل برنامج محدد**:
    *   بالنسبة لـ `nowcoder`، إذا كانت `Main.java` هي نقطة الدخول، يمكنك تشغيلها باستخدام:
        ```bash
        mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
        ```
    *   بالنسبة لحلول UVA، نظرًا لأن كل ملف قد يكون برنامجًا قائمًا بذاته، يمكنك تشغيل فئة محددة (مثل `100.java`) باستخدام:
        ```bash
        mvn -pl uva exec:java -Dexec.mainClass="100"
        ```

### ملاحظات
- **إصدار جافا**: استخدمت Java 17. إذا كنت بحاجة إلى إصدار مختلف، قم بتحديث خصائص `<maven.compiler.source>` و `<maven.compiler.target>` في ملف `pom.xml` الأب.
- **التبعيات**: إذا كانت حلولك تتطلب مكتبات (مثل أدوات الإدخال/الإخراج)، أضفها إلى `pom.xml` للوحدة الفرعية في قسم `<dependencies>`.
- **تسمية الملفات**: تأكد من أن أسماء ملفات الجافا الخاصة بك تطابق أسماء الفئات (على سبيل المثال، يجب أن يحتوي `100.java` على `public class 100`).
- **الأدلة الأخرى**: يتضمن مستودعك `codeforces`، `hacker_rank`، إلخ. إذا كنت تريد تضمين هذه كوحدات فرعية، أضف `<module>codeforces</module>` (إلخ) إلى ملف `pom.xml` الأب وأنشئ ملفات `pom.xml` مقابلة في تلك الأدلة، مشابهة لـ `nowcoder` و `uva`.

أعلمني إذا كنت بحاجة إلى وحدات فرعية إضافية أو تكوينات محددة!