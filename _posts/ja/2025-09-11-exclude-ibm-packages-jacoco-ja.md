---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: JaCoCoでのcom.ibmパッケージ除外
translated: true
type: note
---

**`com.ibm`** パッケージ（または他のパッケージ）を **WebSphere Liberty Profile** 環境で JaCoCo カバレッジから除外するには、**`pom.xml`** ファイルで除外設定を構成できます。これは通常、**JaCoCo Maven プラグイン**の設定で行います。

---

### **`pom.xml` で `com.ibm` パッケージを除外する方法**

JaCoCo プラグイン設定の `<excludes>` タグを使用して、カバレッジレポートから除外するクラスやパッケージを指定できます。

#### **設定例:**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- 最新バージョンを使用してください -->
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
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- すべての com.ibm パッケージを除外 -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **説明:**
- **`<excludes>`**: カバレッジレポートから除外するクラスやパッケージを指定します。
- **`<exclude>com/ibm/**</exclude>`**: `com.ibm` パッケージとそのサブパッケージ配下のすべてのクラスを除外します。

---

### **補足:**
- 複数のパッケージを除外する場合は、追加の `<exclude>` エントリを追加します:
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- **JaCoCo を WebSphere Liberty で使用する**場合、JaCoCo エージェントが `server.env` または `jvm.options` ファイルで適切に構成されていること、および `pom.xml` の除外設定が要件に合致していることを確認してください。

---

### **ベストプラクティス:**
- カバレッジレポートを実行し、除外したパッケージが結果に含まれていないことを常に確認してください。
- 実行時にパッケージを除外する必要がある場合（例: JaCoCo エージェント引数で）、エージェント引数の `excludes` パラメータを使用できます:
  ```plaintext
  -javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,excludes=com.ibm.*
  ```