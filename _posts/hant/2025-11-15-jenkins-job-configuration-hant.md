---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Jenkins 任務配置指南
translated: true
type: note
---

### 在 Jenkins 中配置任務

Jenkins 支援不同類型的任務（亦稱為專案），最常見的是**自由風格專案**（適用於簡單建置）和**流水線專案**（適用於使用 Jenkinsfile 的複雜腳本化工作流程）。以下將概述兩者的步驟。假設您已安裝並運行 Jenkins（例如透過 Docker 或在伺服器上）。請存取 Jenkins 儀表板 `http://localhost:8080`（或您的伺服器 URL）並登入。

#### 建立與配置自由風格專案的步驟
自由風格專案操作簡單，使用圖形介面配置步驟，非常適合初學者或簡單任務，例如建置和測試程式碼。

1. **建立新任務**：
   - 在 Jenkins 儀表板左側導覽列中，點擊**新增任務**。
   - 輸入任務名稱（例如 "MyFirstBuild"）。
   - 選擇**自由風格專案**，然後點擊**確定**。

2. **一般設定**：
   - 為任務添加描述。
   - 可選啟用功能，例如丟棄舊建置（例如僅保留最近 10 次建置）或添加參數（例如在建置期間供使用者輸入的字串或選擇參數）。

3. **原始碼管理**：
   - 選擇您的 SCM 工具，例如 Git。
   - 輸入儲存庫 URL（例如 GitHub 儲存庫）。
   - 如有需要，添加憑證（例如使用者名稱/密碼或 SSH 金鑰）。
   - 指定要建置的分支（例如 `*/main`）。

4. **建置觸發器**：
   - 選擇任務啟動方式，例如：
     - **定期建置**（例如 cron 語法如 `H/5 * * * *` 表示每 5 分鐘）。
     - **輪詢 SCM** 以檢查變更。
     - **GitHub hook trigger** 用於來自 GitHub 的 webhook。
     - **在其他專案後建置** 以鏈接任務。

5. **建置環境**：
   - 勾選選項，例如**在建置開始前刪除工作區**以獲得乾淨的初始狀態。
   - 在控制台輸出中添加時間戳記或設定環境變數。

6. **建置步驟**：
   - 點擊**增加建置步驟**並選擇操作，例如：
     - **執行 shell**（適用於 Linux/Mac：例如 `echo "Hello World"` 或執行腳本）。
     - **呼叫頂層 Maven 目標** 用於 Java 建置。
     - **執行 Windows 批次命令** 用於 Windows。
   - 您可以添加多個按順序執行的步驟。

7. **建置後操作**：
   - 添加操作，例如：
     - **封存成品**（例如儲存 JAR 檔案）。
     - **發佈 JUnit 測試結果報告**。
     - **傳送電子郵件通知**（根據成功/失敗）。
     - **觸發其他專案**。

8. **儲存並執行**：
   - 點擊**儲存**。
   - 返回任務頁面，點擊**立即建置**進行測試。
   - 查看控制台輸出以獲取詳細資訊。

#### 建立與配置流水線專案的步驟
流水線以程式碼形式定義（宣告式或腳本式），對於 CI/CD 工作流程更具靈活性。

1. **建立新任務**：
   - 從儀表板點擊**新增任務**。
   - 輸入名稱並選擇**流水線**，然後點擊**確定**。

2. **一般設定**：
   - 與自由風格類似：添加描述、參數等。

3. **建置觸發器**：
   - 與自由風格相同的選項（例如 webhook、排程）。

4. **流水線定義**：
   - 選擇**流水線腳本**用於內嵌程式碼，或**從 SCM 取得流水線腳本**以從儲存庫拉取（例如 Git 中的 `Jenkinsfile`）。
   - 範例宣告式流水線腳本：
     ```
     pipeline {
         agent any
         stages {
             stage('Build') {
                 steps {
                     echo 'Building...'
                     sh 'mvn clean install'  // 範例 Maven 建置
                 }
             }
             stage('Test') {
                 steps {
                     echo 'Testing...'
                     sh 'mvn test'
                 }
             }
             stage('Deploy') {
                 steps {
                     echo 'Deploying...'
                 }
             }
         }
         post {
             always {
                 echo 'This runs always'
             }
         }
     }
     ```
   - 此腳本定義了階段（建置、測試、部署）及其步驟。

5. **儲存並執行**：
   - 儲存任務。
   - 建置並在流水線視圖中監控階段進度。

Jenkins 在每個部分都有許多選項，請根據您的需求進行探索（例如，為了安全性，添加憑證；為了並行處理，使用代理/節點）。如果您是新手，請從自由風格開始，並在需要擴展時轉向流水線。

### Jenkins 的軟體整合與協作

Jenkins 透過**外掛程式**（超過 2,000 個可用）具有高度可擴展性，可與 DevOps 生態系統中的幾乎任何工具整合。這些整合實現了觸發建置、部署、測試、通知等功能。外掛程式可透過**管理 Jenkins > 管理外掛程式**安裝。

#### 按類別劃分的常見整合
- **版本控制**：Git、GitHub、GitLab、Bitbucket、SVN – 用於拉取程式碼並透過 webhook 在提交/推送事件時觸發建置。
- **容器化與編排**：Docker（建置/推送映像）、Kubernetes（部署到集群）、Helm – 用於基於容器的工作流程。
- **雲端供應商**：AWS（透過外掛程式使用 EC2、S3、Lambda）、Azure、Google Cloud – 用於部署到雲端基礎設施。
- **測試與品質**：SonarQube（程式碼品質掃描）、Selenium（UI 測試）、JUnit（單元測試）、Cucumber（BDD）– 整合到建置步驟中以實現自動化測試。
- **部署與監控**：Ansible、Terraform（基礎設施即程式碼）、Prometheus、Grafana – 用於建置後的編排與監控。
- **通知與協作**：Slack、Microsoft Teams、電子郵件、Jira、Trello – 傳送警報或根據建置狀態更新工單。
- **建置工具**：Maven、Gradle（Java）、npm（Node.js）、pip（Python）– 執行各種語言的建置。
- **安全性**：OWASP Dependency-Check、Trivy（弱點掃描）– 在 CI 期間掃描問題。
- **其他**：Artifactory/Nexus（成品儲存庫）、Zapier（無程式碼整合）、Octopus Deploy（進階部署）。

例如，對於 GitHub，安裝 GitHub 外掛程式以啟用 webhook 觸發。對於 Docker，使用 Docker Pipeline 外掛程式在流水線中建置映像。甚至可以為小眾工具建立自訂外掛程式。

要探索更多，請查閱官方外掛程式索引。請定期更新外掛程式以確保安全性。

#### 參考資料
- [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
- [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
- [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
- [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
- [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
- [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
- [Jenkins Plugins](https://plugins.jenkins.io/)
- [Jenkins](https://www.jenkins.io/)
- [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)