---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Maven Surefire 插件單元測試指南
translated: true
type: note
---

**Maven Surefire Plugin** 是在 Maven 建置生命週期的 **test** 階段執行單元測試的外掛程式。由於幾乎每個專案都需要將自動化測試整合到建置流程中，它成為最常使用的 Maven 外掛程式之一。

---

## 功能概覽

* **名稱**: `maven-surefire-plugin`
* **用途**: 執行使用 JUnit (3、4、5)、TestNG 等測試框架編寫的測試
* **執行階段**: 綁定至 Maven 預設生命週期的 `test` 階段
* **輸出**: 生成測試報告（預設儲存於 `target/surefire-reports`）

---

## 運作原理

1. 當執行 `mvn test` 或 `mvn package` 時，Maven 會觸發 Surefire 外掛程式
2. 掃描 `src/test/java` 目錄中的測試類別
3. 預設會尋找符合以下命名規則的檔案：

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. 在隔離的類別載入器中執行測試
5. 將結果寫入 `target/surefire-reports`（純文字、XML 格式，有時透過報告外掛生成 HTML）

---

## 基礎用法

可在 `pom.xml` 中進行配置：

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- 請使用最新穩定版本 -->
    </plugin>
  </plugins>
</build>
```

配置完成後，執行：

```bash
mvn test
```

---

## 常用配置

* **包含/排除模式**：

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **系統屬性設定**：

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **並行測試執行**：

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

此配置可在多個 JVM 進程或執行緒中執行測試。

---

## 適用場景

* 需要將 **單元測試** 整合到 Maven 生命週期時
* 區分 **單元測試 (Surefire)** 與 **整合測試 (Failsafe 外掛程式)**：

  * Surefire → 單元測試 (`mvn test`)
  * Failsafe → 整合測試 (`mvn verify`)

---

✅ **簡而言之**：`maven-surefire-plugin` 是 Maven 專案中執行單元測試的首選外掛程式。您只需在 `pom.xml` 中配置，透過 `mvn test` 執行測試，並在 `target/surefire-reports` 中查看測試報告。

---

需要我進一步說明 **Surefire 與 Failsafe 的差異** 嗎（這兩者經常被混淆）？