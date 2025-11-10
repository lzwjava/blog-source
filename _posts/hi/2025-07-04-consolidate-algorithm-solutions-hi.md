---
audio: false
generated: true
lang: hi
layout: post
title: मेवेन में एल्गोरिदम समाधानों का समेकन
translated: true
type: note
---

आपके सभी एल्गोरिदम समाधानों (`nowcoder`, `uva`, आदि) को `algorithm-solutions` रूट डायरेक्टरी में एक ही `pom.xml` फ़ाइल द्वारा प्रबंधित एक एकल Maven मॉड्यूल में समेकित करने के लिए, हम पूरे प्रोजेक्ट को एक मॉड्यूल के रूप में मानेंगे। `nowcoder` और `uva` (और अन्य डायरेक्टरीज जैसे `codeforces`, `hacker_rank`, आदि) की Java फ़ाइलों को `src/main/java` के अंतर्गत उचित पैकेज संरचनाओं (जैसे, `com.algorithm.solutions.nowcoder`, `com.algorithm.solutions.uva`) के साथ व्यवस्थित किया जाएगा। इनपुट फ़ाइलें (जैसे, `1.in`) `src/main/resources` में जाएंगी।

### मान्यताएँ
- सभी Java फ़ाइलें (जैसे, `nowcoder/Main.java`, `uva/106/src/Main.java`) को `src/main/java/com/algorithm/solutions/<platform>` (जैसे, `nowcoder`, `uva/p106`) में ले जाया जाएगा।
- इनपुट फ़ाइलें (जैसे, `uva/106/1.in`) को `src/main/resources/<platform>` (जैसे, `uva/p106`) में ले जाया जाएगा।
- प्रोजेक्ट Java 17 का उपयोग करता है (`pom.xml` में समायोज्य)।
- `pom.xml` `algorithm-solutions` रूट डायरेक्टरी में होगी, और कोई उप-मॉड्यूल उपयोग नहीं किए जाएंगे।

### डायरेक्टरी संरचना
पुनर्गठन के बाद (मानते हुए कि आप पिछले प्रतिक्रिया से `uva` के लिए Python स्क्रिप्ट और `nowcoder` के लिए इसी तरह की एक स्क्रिप्ट चलाते हैं), संरचना इस प्रकार होगी:

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
│   │   │       │   └── (आदि)
│   │   │       ├── codeforces/
│   │   │       └── hacker_rank/
│   │   └── resources/
│   │       ├── nowcoder/
│   │       │   └── (इनपुट फ़ाइलें, यदि कोई हों)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (आदि)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### पैरेंट `pom.xml`
यह `pom.xml` `algorithm-solutions` रूट डायरेक्टरी में जाती है। यह प्रोजेक्ट को एक एकल मॉड्यूल के रूप में कॉन्फ़िगर करती है, इनपुट फ़ाइलों के लिए संसाधन शामिल करती है, और Java 17 के लिए Maven कंपाइलर सेट अप करती है।

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

### `pom.xml` पर नोट्स
- **Packaging**: `jar` पर सेट किया गया है क्योंकि यह एक एकल निष्पादन योग्य मॉड्यूल है।
- **Resources**: इनपुट फ़ाइलों के लिए `src/main/resources` से `*.in` फ़ाइलें शामिल करता है।
- **Main Class**: डिफ़ॉल्ट के रूप में `com.algorithm.solutions.nowcoder.Main` पर सेट किया गया है। चूंकि प्रत्येक समस्या की अपनी `Main` क्लास हो सकती है, आप आम तौर पर विशिष्ट कक्षाओं को `mvn exec:java` का उपयोग करके चलाएंगे।
- **Java Version**: Java 17 का उपयोग करता है; यदि आवश्यक हो तो `<maven.compiler.source>` और `<maven.compiler.target>` को समायोजित करें।

### सेट अप करने के चरण
1. **डायरेक्टरी संरचना बनाएँ**:
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **फ़ाइलें ले जाएँ**:
   - `nowcoder` के लिए:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     प्रत्येक Java फ़ाइल में पैकेज घोषणा जोड़ें (जैसे, `Main.java`):
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... कोड का बाकी हिस्सा ...
     ```
   - `uva` के लिए, पिछले प्रतिक्रिया से Python स्क्रिप्ट का उपयोग करें, या मैन्युअल रूप से:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     `Main.java` में पैकेज घोषणा जोड़ें:
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... कोड का बाकी हिस्सा ...
     ```
     अन्य UVA समस्याओं (`100`, `10000`, आदि) के लिए दोहराएँ।

3. **`pom.xml` रखें**:
   - उपरोक्त `pom.xml` को `algorithm-solutions` रूट डायरेक्टरी में सहेजें।

4. **प्रोजेक्ट बिल्ड करें**:
   ```bash
   mvn clean install
   ```

5. **एक विशिष्ट प्रोग्राम चलाएँ**:
   - `nowcoder` समस्या के लिए:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - UVA समस्या के लिए (जैसे, समस्या 106):
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### `nowcoder` के लिए Python स्क्रिप्ट
पिछली `uva` स्क्रिप्ट के पूरक के रूप में, यहाँ एक Python स्क्रिप्ट है जो `nowcoder` फ़ाइलों को `src/main/java/com/algorithm/solutions/nowcoder/` में ले जाने और पैकेज घोषणाएँ जोड़ने के लिए है। इसे `algorithm-solutions` रूट डायरेक्टरी से चलाएँ।

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

### नोट्स
- **स्क्रिप्ट चलाना**: फ़ाइलों को ले जाने के लिए `reorganize_uva.py` (पिछले प्रतिक्रिया से) और `reorganize_nowcoder.py` स्क्रिप्ट चलाएँ:
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **इनपुट फ़ाइलें**: यदि `nowcoder` में इनपुट फ़ाइलें हैं, तो `*.in` फ़ाइलों को `src/main/resources/nowcoder/` में ले जाने के लिए स्क्रिप्ट को संशोधित करें।
- **अन्य डायरेक्टरीज**: `codeforces`, `hacker_rank`, आदि के लिए, आप स्रोत डायरेक्टरी और पैकेज नाम बदलकर `nowcoder` स्क्रिप्ट को अनुकूलित कर सकते हैं।
- **Resource Access**: इनपुट फ़ाइलों को `src/main/resources` से पढ़ने के लिए अपने Java कोड को अपडेट करें (जैसे, `getClass().getResource("/uva/p106/1.in")`)।
- **फ़ाइलों को अनदेखा करना**: IntelliJ प्रोजेक्ट फ़ाइलों को बाहर करने के लिए `.gitignore` फ़ाइल में `*.iml` जोड़ें।

अगर आपको अन्य डायरेक्टरीज के लिए स्क्रिप्ट या `pom.xml` में और बदलाव की आवश्यकता हो तो मुझे बताएं!