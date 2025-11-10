---
audio: false
generated: true
lang: ar
layout: post
title: حلول الخوارزميات الموحدة في مافن
translated: true
type: note
---

لدمج جميع حلول الخوارزميات الخاصة بك (`nowcoder`، `uva`، إلخ) في وحدة Maven واحدة يتم إدارتها بواسطة ملف `pom.xml` واحد في الدليل الجذري `algorithm-solutions`، سنتعامل مع المشروع بأكمله كوحدة واحدة. سيتم تنظيم ملفات Java من `nowcoder` و `uva` (والدلائل الأخرى مثل `codeforces`، `hacker_rank`، إلخ) تحت `src/main/java` مع هياكل حزم مناسبة (مثل `com.algorithm.solutions.nowcoder`، `com.algorithm.solutions.uva`). سيتم وضع ملفات الإدخال (مثل `1.in`) في `src/main/resources`.

### الافتراضات
- سيتم نقل جميع ملفات Java (مثل `nowcoder/Main.java`، `uva/106/src/Main.java`) إلى `src/main/java/com/algorithm/solutions/<platform>` (مثل `nowcoder`، `uva/p106`).
- سيتم نقل ملفات الإدخال (مثل `uva/106/1.in`) إلى `src/main/resources/<platform>` (مثل `uva/p106`).
- يستخدم المشروع Java 17 (قابل للتعديل في ملف `pom.xml`).
- سيكون ملف `pom.xml` في الدليل الجذري `algorithm-solutions`، ولن يتم استخدام وحدات فرعية.

### هيكل الدليل
بعد إعادة التنظيم (بافتراض أنك قمت بتشغيل سكريبت Python من الرد السابق لـ `uva` وآخر مشابه لـ `nowcoder`)، سيكون الهيكل كما يلي:

```
algorithm-solutions/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/algorithm/solutions/
│   │   │       ├── nowcoder/
│   │   │       │   ├── Main.java
│   │   │       │   ├── nc140.java
│   │   │       │   ├── nc45.java
│   │   │       │   ├── nc78.java
│   │   │       │   └── nc93.java
│   │   │       ├── uva/
│   │   │       │   ├── p100/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p106/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p10000/
│   │   │       │   │   └── Main.java
│   │   │       │   └── (etc.)
│   │   │       ├── codeforces/
│   │   │       └── hacker_rank/
│   │   └── resources/
│   │       ├── nowcoder/
│   │       │   └── (ملفات الإدخال، إذا وجدت)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (etc.)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### ملف `pom.xml` الرئيسي
يوجد هذا الملف `pom.xml` في الدليل الجذري `algorithm-solutions`. وهو يُهيئ المشروع كوحدة واحدة، ويشمل الموارد لملفات الإدخال، ويُجهز مترجم Maven لـ Java 17.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>Algorithm Solutions</name>
    <description>Consolidated project for algorithm solutions from multiple platforms</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

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
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
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

### ملاحظات على ملف `pom.xml`
- **التعبئة**: مضبوطة على `jar` لأن هذه وحدة قابلة للتنفيذ.
- **الموارد**: تشمل ملفات `*.in` من `src/main/resources` لملفات الإدخال.
- **الفئة الرئيسية**: مضبوطة على `com.algorithm.solutions.nowcoder.Main` كإعداد افتراضي. نظرًا لأن كل مشكلة قد تحتوي على فئة `Main` الخاصة بها، فعادةً ما تقوم بتشغيل فئات محددة باستخدام `mvn exec:java`.
- **إصدار Java**: يستخدم Java 17؛ قم بتعديل `<maven.compiler.source>` و `<maven.compiler.target>` إذا لزم الأمر.

### خطوات الإعداد
1. **إنشاء هيكل الدليل**:
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **نقل الملفات**:
   - بالنسبة لـ `nowcoder`:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     أضف تصريح الحزمة إلى كل ملف Java (مثل `Main.java`):
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... rest of the code ...
     ```
   - بالنسبة لـ `uva`، استخدم سكريبت Python من الرد السابق، أو يدويًا:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     أضف تصريح الحزمة إلى `Main.java`:
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... rest of the code ...
     ```
     كرر ذلك لمشاكل UVA الأخرى (`100`، `10000`، إلخ).

3. **ضع ملف `pom.xml`**:
   - احفظ ملف `pom.xml` أعلاه في الدليل الجذري `algorithm-solutions`.

4. **بناء المشروع**:
   ```bash
   mvn clean install
   ```

5. **تشغيل برنامج محدد**:
   - لمشكلة في `nowcoder`:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - لمشكلة في UVA (مثل المشكلة 106):
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### سكريبت Python لـ `nowcoder`
لتكملة سكريبت `uva` السابق، إليك سكريبت Python لنقل ملفات `nowcoder` إلى `src/main/java/com/algorithm/solutions/nowcoder/` وإضافة تصريحات الحزمة. قم بتشغيل هذا من الدليل الجذري `algorithm-solutions`.

```python
import os
from pathlib import Path

def add_package_declaration(java_file, package):
    """Add package declaration to the top of a Java file if not already present."""
    with open(java_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip().startswith('package '):
        new_content = f'package {package};\n\n{content}'
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added package declaration to {java_file}')

def reorganize_nowcoder():
    # Define paths
    nowcoder_root = Path('nowcoder')
    target_dir = Path('src/main/java/com/algorithm/solutions/nowcoder')

    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)

    if not nowcoder_root.exists():
        print('Error: nowcoder directory not found.')
        return

    # Move Java files
    for java_file in nowcoder_root.glob('*.java'):
        target_file = target_dir / java_file.name
        shutil.move(str(java_file), str(target_file))
        print(f'Moved {java_file} to {target_file}')
        
        # Add package declaration
        add_package_declaration(target_file, 'com.algorithm.solutions.nowcoder')

    # Remove empty nowcoder directory
    if not any(nowcoder_root.iterdir()):
        nowcoder_root.rmdir()
        print(f'Removed empty directory {nowcoder_root}')

if __name__ == '__main__':
    reorganize_nowcoder()
    print('Nowcoder reorganization complete.')
```

### ملاحظات
- **تشغيل السكريبتات**: قم بتشغيل سكريبتات `reorganize_uva.py` (من الرد السابق) و `reorganize_nowcoder.py` لنقل الملفات:
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **ملفات الإدخال**: إذا كان `nowcoder` يحتوي على ملفات إدخال، فقم بتعديل السكريبت لنقل ملفات `*.in` إلى `src/main/resources/nowcoder/`.
- **الدلائل الأخرى**: بالنسبة لـ `codeforces`، `hacker_rank`، إلخ، يمكنك تكييف سكريبت `nowcoder` عن طريق تغيير الدليل المصدر واسم الحزمة.
- **الوصول إلى الموارد**: قم بتحديث كود Java لقراءة ملفات الإدخال من `src/main/resources` (مثل `getClass().getResource("/uva/p106/1.in")`).
- **تجاهل الملفات**: أضف `*.iml` إلى ملف `.gitignore` لاستبعاد ملفات مشروع IntelliJ.

أعلمني إذا كنت بحاجة إلى سكريبتات لدلائل أخرى أو تعديلات إضافية على ملف `pom.xml`!