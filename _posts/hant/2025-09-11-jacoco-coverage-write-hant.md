---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: JaCoCo 覆蓋數據寫入行為
translated: true
type: note
---

在**整合測試**（或任何 JVM 程序）中使用 **JaCoCo 代理**時，覆蓋率資料**不會在 JVM 結束時自動寫入 `.exec` 檔案**。其運作機制如下：

---

### JaCoCo 何時寫入覆蓋率資料？
- **在 JVM 關閉期間**：當 JVM 正常關閉時（例如主方法結束或測試套件完成），JaCoCo 代理會**刷新並寫入**收集到的覆蓋率資料至 `.exec` 檔案。
- **若 JVM 崩潰**：若 JVM 異常終止（例如因崩潰或 `System.exit()` 導致），代理可能**沒有機會**寫入資料，部分覆蓋率資訊可能會遺失。

---

### 如何確保資料寫入
1. **正常關閉**：確保您的整合測試或應用程式正常結束（例如不強制退出）。
2. **明確傾印（可選）**：您可以在運行期間使用 JaCoCo 運行時 API（例如 `org.jacoco.agent.rt.RT.getAgentRuntime().dump(true, outputFile)`）手動觸發覆蓋率資料傾印。這對於長時間運行的程序或需要擷取中間資料的情況非常有用。

---

### 範例情境
- 若您的整合測試套件正常運行並完成，JaCoCo 代理會**在 JVM 程序結束時**將覆蓋率資料寫入 `jacoco.exec`（或您指定的檔案）。
- 若 JVM 被強制終止（例如 `kill -9`），資料可能無法寫入。

---

### 最佳實踐
- **使用 `append=true`**：若您執行多個測試套件，請在 JaCoCo 代理參數中設定 `append=true` 以累積跨次執行的覆蓋率資料。
- **檢查部分資料**：若 JVM 崩潰，`.exec` 檔案可能不完整或遺失最後一次執行的資料。

---