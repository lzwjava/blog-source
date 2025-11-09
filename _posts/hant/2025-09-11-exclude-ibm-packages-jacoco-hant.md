---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 於 JaCoCo 中排除 com.ibm 套件
translated: true
type: note
---

若要在 **WebSphere Liberty Profile** 環境中排除 **`com.ibm`** 套件（或其他任何套件）的 JaCoCo 涵蓋範圍，您可以在 **`pom.xml`** 檔案中設定排除項目。這通常是在 **JaCoCo Maven 外掛程式** 設定中完成。

---

### **如何在 `pom.xml` 中排除 `com.ibm` 套件**

您可以在 JaCoCo 外掛程式設定中使用 `<excludes>` 標籤，指定哪些類別或套件應從涵蓋範圍報告中排除。

#### **設定範例：**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- 請使用最新版本 -->
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
                            <!-- 排除所有 com.ibm 套件 -->
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

### **說明：**
- **`<excludes>`**：此區塊指定哪些類別或套件應從涵蓋範圍報告中排除。
- **`<exclude>com/ibm/**</exclude>`**：此設定會排除 `com.ibm` 套件及其子套件下的所有類別。

---

### **補充說明：**
- 若要排除多個套件，請新增更多 `<exclude>` 項目：
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- 若您正在 **WebSphere Liberty** 中使用 **JaCoCo**，請確保 JaCoCo 代理程式已在 `server.env` 或 `jvm.options` 檔案中正確設定，且 `pom.xml` 中的排除項目符合您的需求。

---

### **最佳實踐：**
- 請務必透過執行涵蓋範圍報告來驗證排除項目，確認已排除的套件未包含在結果中。
- 若需在執行階段排除套件（例如在 JaCoCo 代理程式參數中），您可在代理程式參數中使用 `excludes` 參數：
  ```plaintext
  -javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,excludes=com.ibm.*
  ```