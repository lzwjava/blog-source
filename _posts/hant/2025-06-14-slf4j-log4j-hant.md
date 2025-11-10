---
audio: false
generated: true
lang: hant
layout: post
title: SLF4J 與 Log4j 比較
translated: true
type: note
---

在 SLF4J（配合提供的依賴項）與 Log4j 之間選擇時，需視專案需求而定：

- **SLF4J（Simple Logging Facade for Java）**：
  - **優點**：作為日誌門面，可讓您切換日誌框架（例如 Log4j、Logback、JUL）而無需修改程式碼。輕量、靈活且廣泛使用。您分享的依賴項（`slf4j-api:2.0.17`）是截至 2025 年 6 月的最新 SLF4J API。
  - **缺點**：需搭配綁定庫（例如 `slf4j-simple`、`logback-classic` 或 `log4j-slf4j-impl`）才能實際輸出日誌。增加了抽象層。
  - **適用場景**：適合需要後續靈活更換日誌實現方案的函式庫或應用程式。搭配 Logback 可組成現代化高效能組合。

- **Log4j（Apache Log4j 2）**：
  - **優點**：具備完整功能的日誌框架，支援非同步日誌、自定義輸出器等高階功能，效能出色。若確定採用 Log4j 則無需門面層。最新版本（截至 2025 年 6 月）為 `2.24.1`。
  - **缺點**：與 Log4j 實現緊密耦合。相比 SLF4J 加綁定庫的方案稍顯臃腫。歷史上曾存在安全漏洞（如 2021 年的 Log4Shell），不過近期版本已修復。
  - **適用場景**：適用於需要豐富功能且可接受直接依賴 Log4j 的應用程式。

**建議**：
- 多數專案建議使用 **SLF4J** 搭配 **Logback**（`ch.qos.logback:logback-classic:1.5.12`），兼具靈活性與現代化特性，避免被 Log4j 綁定
- 若需使用 Log4j 的特定進階功能且接受其生態系統，可直接選擇 **Log4j 2**

若需以 SLF4J 作為門面並搭配 Log4j 後端，請添加：
```xml
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-slf4j2-impl</artifactId>
    <version>2.24.1</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.24.1</version>
</dependency>
```

**注意**：為避免執行階段問題，請確保 classpath 中沒有衝突的綁定庫（例如同時存在 `slf4j-simple` 與 `logback-classic`）。