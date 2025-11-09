---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hant
layout: post
title: 多模組 Java 覆蓋率與 Python
translated: true
type: note
---

檢視你的設定，你正面臨一個複雜但有趣的挑戰：使用 Python 整合測試來為多模組 Java 專案生成涵蓋率報告。讓我分析現狀並提出一個全面策略。

## 當前挑戰

1. **跨語言測試**：Python 測試執行 Java 程式碼
2. **多模組涵蓋率**：需要從整合測試中捕捉所有模組的涵蓋率
3. **模組相依性**：`PlaygroundUtils` 沒有直接端點，但透過 `PlaygroundWeb` 被執行
4. **擴展性考量**：如何處理 10+ 模組的情況

## 推薦策略

### 選項 1：單一 JaCoCo 代理，合併報告（推薦）

這是最適合你使用案例的擴展性方案：

## 關鍵改進與策略

### 1. **單一 JaCoCo 代理方法**
- 在父層級使用單一 `jacoco-it.exec` 檔案
- 配置代理使用 `append=true` 和 `includes=org.lzw.*`
- 這樣可以在單次執行中捕捉所有模組的涵蓋率

### 2. **報告匯總**
- 使用 `jacoco:report-aggregate` 建立統一報告
- 這會自動找到所有模組類別並為其生成涵蓋率

### 3. **基於配置檔的執行**
- 分離關注點：`run-integration-tests` 配置檔用於執行測試
- `integration-test-coverage` 配置檔用於生成報告
- 讓建置更加模組化且易於維護

### 4. **10+ 模組的擴展性**

對於較大型專案，考慮這種增強方法：

## 總結與最佳實踐

### 針對你目前的 2 模組設定：
1. **使用單一 JaCoCo exec 檔案**在父層級並設定 `append=true`
2. **執行 Jetty 一次**並配置代理以捕捉所有模組
3. **使用 `report-aggregate`** 生成統一報告

### 擴展到 10+ 模組：
1. **模組分組**：建立邏輯群組（核心、服務、網頁）並生成獨立報告
2. **涵蓋率追蹤**：實作 Python 輔助工具來追蹤哪些模組被覆蓋
3. **平行測試**：平行執行不同測試套件以獲得更快回饋
4. **增量涵蓋率**：使用 Maven 配置檔來執行特定模組群的涵蓋率

### 關鍵配置點：
- **`append=true`**：確保多次測試執行能累積涵蓋率
- **`includes=org.lzw.*`**：在單一代理中捕捉所有模組
- **配置檔分離**：將整合測試與常規建置分開
- **單一 exec 檔案**：無需多次執行 Jetty

### 命令列用法：
```bash
# 完整涵蓋率與整合測試
mvn clean verify -Prun-integration-tests,integration-test-coverage

# 僅單元測試涵蓋率
mvn clean test

# 特定模組群組的涵蓋率
mvn clean verify -Pcoverage-by-layer
```

這種方法擴展性良好，因為：
1. 無論模組數量多少，你只需啟動/停止 Jetty 一次
2. JaCoCo 自動處理多模組類別檔案
3. Python 測試無需了解 Java 模組結構
4. 報告可以根據不同需求進行匯總或拆分

關鍵在於 JaCoCo 代理能夠捕捉 JVM 中所有類別的涵蓋率，而不僅是被測試的模組。透過使用共享的 exec 檔案和匯總目標，你可以在單次測試執行中獲得完整的涵蓋率資料。