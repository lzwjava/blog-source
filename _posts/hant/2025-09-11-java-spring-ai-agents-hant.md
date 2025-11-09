---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Java Spring 單體倉庫人工智能代理指南
translated: true
type: note
---

很棒的問題。以下是一些實用且高效的AI助手，你可以根據Java/Spring單體倉庫（多模組、Maven/Jetty/Liberty、JaCoCo等）的需求進行定制。我將專注於具體的觸發條件、產出內容以及如何串聯它們——不使用表格。

# 核心工程助手

**1) PR程式碼審查員（支援Spring框架）**

* **觸發條件：** 拉取請求時。
* **功能：** 讀取差異變更 + 受影響的Spring bean/配置；標記依賴注入問題、bean作用域錯誤、缺少`@Transactional`、JPA的N+1風險、誤用`@Scheduled`、非同步處理的執行緒洩漏、響應式鏈上的阻塞呼叫。
* **輸入：** 差異比對 + `pom.xml` + `application*.yml` + `@Configuration`類別。
* **輸出：** 行內註解建議、風險摘要、快速修復補丁。

**2) 依賴項與外掛升級器**

* **觸發條件：** 每日/每週任務。
* **功能：** 建議相容的版本升級（Spring Boot/Framework、Spring Data/Cloud、Jetty/Liberty、Maven外掛），檢查CVE漏洞，執行冒煙測試建置。
* **輸出：** 按風險分組的PR（修補程式、次要、重大），附變更日誌和回滾說明。

**3) API合約守護者**

* **觸發條件：** 當PR涉及控制器或`openapi.yaml`時。
* **功能：** 保持OpenAPI規範與Spring MVC註解同步；檢測破壞性變更（HTTP狀態碼、欄位重新命名、可空性/必需性）。
* **輸出：** 附帶API介面差異的註解；可選的Pact風格合約測試樁。

**4) 測試撰寫與不穩定測試修復員**

* **觸發條件：** 當PR（測試覆蓋率低）和每晚執行時。
* **功能：** 為服務/控制器/儲存庫生成/擴展JUnit 5測試；穩定不穩定測試（時間、臨時目錄、並行處理），建議確定性模式，使用`Clock`隔離時鐘。
* **輸出：** 新測試、參數化、提示用Awaitility取代休眠。

**5) 覆蓋率協調員（單元+整合測試，多模組）**

* **觸發條件：** CI整合測試後。
* **功能：** 將JaCoCo代理附加到Jetty/Liberty，合併`jacoco.exec`/`jacoco-it.exec`，跨模組映射類別，突顯未測試的關鍵路徑。
* **輸出：** 合併的HTML/XML報告；每個模組前10個未覆蓋方法的列表附帶測試骨架建議。

**6) 日誌與事件分類員**

* **觸發條件：** CI作業失敗時，或從預發/生產環境串流傳入時。
* **功能：** 對堆疊追蹤進行分群，與最後一次部署關聯，連結到可疑提交；建議快速差異修復和功能開關切換。
* **輸出：** 根本原因假設、「下一步」檢查清單、Grafana/ELK連結。

**7) 效能分析教練**

* **觸發條件：** 負載測試執行或慢端點警報時。
* **功能：** 讀取JFR/非同步分析器輸出 + Spring Actuator指標；發現慢`@Transactional`邊界、N+1問題、繁重的映射器、池大小設定錯誤。
* **輸出：** 聚焦的效能優化計劃（JPA抓取圖提示、索引、池大小、快取）。

**8) 資料庫遷移助手（支援Db2/MySQL/Postgres）**

* **觸發條件：** Flyway/Liquibase變更或慢查詢報告時。
* **功能：** 審查DDL的鎖定問題，添加索引，模擬遷移順序；生成回滾指令碼；將低效的JPQL/Criteria重寫為帶提示的SQL。
* **輸出：** 已審查的遷移PR、執行計劃說明、安全部署步驟。

**9) 安全與密碼哨兵**

* **觸發條件：** 每次PR和每晚掃描時。
* **功能：** SAST檢查Spring Security錯誤配置、CSRF/標頭、反序列化、SpEL注入；掃描YAML、屬性檔、測試夾具中的密碼。
* **輸出：** PR內聯註解、建議的`SecurityFilterChain`差異。

**10) 配置漂移與設定檔審計員**

* **觸發條件：** 當PR涉及`application*.yml`時。
* **功能：** 驗證設定檔覆蓋、環境變數綁定、缺少的預設值；檢測生產環境獨有的意外配置（例如不同的`spring.jpa.open-in-view`）。
* **輸出：** 按設定檔和環境的「有效配置」預覽。

**11) 建置警察（Maven多模組）**

* **觸發條件：** 每次建置時。
* **功能：** 診斷外掛順序、可重現建置、編碼警告、測試分叉設定、Surefire/Failsafe交接、模組圖退化。
* **輸出：** 具體的`pom.xml`修補程式和更快的建置配方。

**12) 發布說明與變更日誌撰寫員**

* **觸發條件：** 標籤或發布分支合併時。
* **功能：** 按約定範圍/模組對提交進行分組；提取顯著的API變更和遷移；包含升級步驟。
* **輸出：** `CHANGELOG.md`部分 + GitHub Release正文草稿。

# 跨領域「黏合」模式

**事件來源：** GitHub PRs/Actions、Jenkins、Maven階段、Gradle任務（如有）、日誌管道、JFR輸出、Actuator指標、Pact/Postman執行。
**上下文包：** 差異 + 受影響的模組、`pom.xml`樹、OpenAPI、`application*.yml`、關鍵配置（`SecurityFilterChain`、`DataSource`、`JpaRepositories`）、測試報告、JaCoCo XML、分析器/火焰圖。
**回應目標：** 帶有程式碼區塊修補程式的PR註解、狀態檢查、自動PR、儲存為建置產品的markdown報告。

# 最小化串聯（複製貼上即可用）

**1) GitHub Action步驟，為助手準備倉庫上下文**

```yaml
- name: Prepare Spring context bundle
  run: |
    mkdir -p .agent_ctx
    git diff -U0 origin/main... > .agent_ctx/diff.patch || true
    find . -name "pom.xml" -o -name "build.gradle*" > .agent_ctx/build_files.txt
    find . -name "application*.yml" -o -name "application*.properties" > .agent_ctx/configs.txt
    find . -name "openapi*.yaml" -o -name "openapi*.yml" > .agent_ctx/openapi.txt
```

**2) JaCoCo合併（單元 + 整合測試）用於多模組**

```bash
mvn -q -DskipITs=false -P it-tests verify
mvn -q org.jacoco:jacoco-maven-plugin:prepare-agent verify
mvn -q org.jacoco:jacoco-maven-plugin:report-aggregate
# 如果你使用運行的Jetty/Liberty收集外部整合測試：
# java -javaagent:jacocoagent.jar=destfile=jacoco-it.exec,append=true ...
# 然後合併：
mvn -q org.jacoco:jacoco-maven-plugin:merge \
  -DdestFile=target/jacoco-merged.exec \
  -Dfile1=target/jacoco.exec -Dfile2=target/jacoco-it.exec
mvn -q org.jacoco:jacoco-maven-plugin:report \
  -DdataFile=target/jacoco-merged.exec
```

**3) PR註解助手（ChatOps風格）**

```yaml
- name: Post agent findings
  if: always()
  run: |
    echo "### API合約變更" > agent-comment.md
    echo "" >> agent-comment.md
    cat target/api-diff.md >> agent-comment.md || true
- uses: marocchino/sticky-pull-request-comment@v2
  with:
    path: agent-comment.md
```

# 優先建置內容（最高投資回報率）

1. **PR程式碼審查 + 配置審計員**：早期捕捉70%常見的Spring錯誤。
2. **覆蓋率協調員**：合併單元和外部整合測試（你的情況），並輸出每個模組的測試待辦事項。
3. **API合約守護者**：防止破壞客戶端；投入小，避免大麻煩。
4. **依賴項升級器 + 安全哨兵**：以最小噪音保持持續衛生。

# 防護欄與品質

* **確定性：** 助手應包含規則ID和其分析的確切程式碼行連結。
* **變更預算：** 將自動編輯限制為小修補程式；較大的重構應成為草稿PR。
* **隱私/存取：** 限制生產日誌/資料庫快照；在模型呼叫前編輯密碼。
* **指標：** 追蹤平均修復時間（失敗→修復）、不穩定測試率、測試覆蓋率變化、效能SLI。使用每週助手記分卡。

# 如果你需要，我可以：

* 起草一個**可直接使用的GitHub Actions工作流程**，該工作流程使用你的模組和JaCoCo設定來執行「PR程式碼審查 + API合約守護者 + 覆蓋率協調員」。
* 生成針對你的技術堆疊（Jetty/Liberty、Db2、多模組Maven）調整的**入門規則**。

告訴我你的倉庫結構（模組名稱）以及你目前如何執行整合測試（Jetty vs Liberty），我將提供YAML和小型輔助指令碼。