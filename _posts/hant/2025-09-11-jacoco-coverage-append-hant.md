---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: JaCoCo 覆蓋率檔案與附加模式
translated: true
type: note
---

這是 JaCoCo 運作方式中一個細微但重要的細節。

### `jacoco:prepare-agent` 的行為

* 當 Maven 執行 **`prepare-agent`** 目標時，它並不會立即生成覆蓋率檔案。
* 相反地，它會**配置 JVM**（通常是透過 `-javaagent:jacocoagent.jar` 參數），以便在測試或應用程式執行時收集覆蓋率數據。
* `.exec` 檔案的位置由屬性 `jacoco.destFile` 控制（預設為 `target/jacoco.exec`，但通常會自定義，例如 `target/jacoco-it.exec`）。

### 如果檔案已存在會發生什麼？

* 預設情況下，**JaCoCo 會在帶有代理的 JVM 啟動時覆寫該檔案**。
* 這意味著每次執行 `prepare-agent` → 測試執行都會產生一個*全新*的 `.exec` 檔案。
* 它不會自動附加數據——除非你另行配置，否則舊數據將會丟失。

### 如何改為附加模式

如果你希望多次執行的數據累積到同一個 exec 檔案中，必須明確啟用附加模式：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <configuration>
    <destFile>${project.build.directory}/jacoco-it.exec</destFile>
    <append>true</append>   <!-- ✅ 附加覆蓋率數據 -->
  </configuration>
</plugin>
```

使用 `<append>true>` 後，如果檔案已存在，新的覆蓋率數據將會合併到該檔案中。

### 簡而言之

* **預設情況：** 每次執行都會取代舊的 `.exec` 檔案。
* **使用 `append=true`：** 來自多次 JVM 執行（或多個模組/測試）的覆蓋率數據會合併到同一個檔案中。

---

你是否還需要我解釋這如何與**多模組 Maven 構建**互動（每個模組可能會嘗試寫入自己的 JaCoCo exec 檔案）？這通常是人們遇到覆寫與附加問題的原因。