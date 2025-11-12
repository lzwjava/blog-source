---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 實用 Jenkins CI CD 指南 現已推出
translated: true
type: note
---

太棒了——讓我們為您打造一份**簡潔、端到端的 Jenkins 指南**，您可以在工作中立即使用。我將保持內容簡潔易讀，不使用寬表格。

# Jenkins 是什麼（以及何時使用它）

Jenkins 是一個自託管的 CI/CD 自動化伺服器：您將其連接到原始碼儲存庫，在 `Jenkinsfile` 中定義流水線，它會在一台或多台機器（「代理」）上執行建置、測試和部署。流水線有兩種風格——**Declarative**（首選）和 **Scripted**——兩者均有專案文件記錄。([Jenkins][1])

---

# 核心架構（簡單說明）

* **Controller**：網頁 UI、佇列和協調大腦。
* **Agents/Nodes**：實際執行任務的機器（虛擬機器、容器、實體機）。您可以添加多個代理並按功能標記它們（例如 `java8`、`docker`）。([Jenkins][2])
* **Jobs/Pipelines**：工作的定義（理想情況下以程式碼形式儲存在您的儲存庫中）。
* **Plugins**：添加功能（憑證、驗證策略、雲端代理、JCasC 等）。

---

# 安裝與首次執行強化（快速檢查清單）

1.  **安裝**在 Linux 或容器映像上。
2.  **反向代理 + TLS**（Nginx/Apache、企業負載平衡器）。
3.  **管理 Jenkins → 設定全域安全性**

    * 設定真實的**安全領域**（LDAP/OIDC/SAML 等）。
    * 選擇一種**授權**模式（見下文）。([Jenkins][3])
4.  **建立一個管理員**使用者（非共用）。
5.  **限制註冊**，停用匿名寫入權限。
6.  **僅使用憑證外掛**——切勿在任務中硬編碼密碼。([Jenkins][4])

---

# 存取控制（RBAC 與專案範圍）

Jenkins 附帶**基於矩陣的安全性**，用於細粒度的權限管理（建置、設定、刪除等）。適用於小型/中型實例或作為基礎。([Jenkins][3], [Jenkins Plugins][5])

對於較大的組織和更清晰的團隊隔離，請安裝**基於角色的授權策略**（"role-strategy" 外掛）：

* 定義**全域角色**（例如 `admin`、`reader`）。
* 定義按項目/資料夾正則表達式限定範圍的**專案角色**（例如 `team-alpha.*`）。
* 將使用者/群組分配給角色——現在團隊只能看到/建置他們擁有的內容。([Jenkins Plugins][6])

> 提示：將每個團隊的流水線放入**資料夾**中，然後在資料夾層級應用專案角色。如果需要超細微調整，可與**矩陣**結合使用。([Jenkins Plugins][5])

---

# 憑證與密碼（安全模式）

* 在**管理 Jenkins → 憑證**中添加密碼（全域或資料夾範圍）。
* 在 Declarative Pipeline 中，在 `environment` 中使用 `credentials()` 引用，或使用 `withCredentials { … }` 按需綁定。
* 優先使用來自金庫或供應商外掛的短期令牌；定期輪換。([Jenkins][4])

**範例 (Declarative):**

```groovy
pipeline {
  agent any
  environment {
    // 從 Username/Password 憑證注入 USER 和 PASS 環境變數
    CREDS = credentials('dockerhub-creds-id')
  }
  stages {
    stage('Login') {
      steps {
        sh 'echo $CREDS_USR | docker login -u $CREDS_USR --password-stdin'
      }
    }
  }
}
```

```groovy
pipeline {
  agent any
  stages {
    stage('Use Secret Text') {
      steps {
        withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
          sh 'curl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.example/api'
        }
      }
    }
  }
}
```

使用方法和綁定的文件在此。([Jenkins][7])

---

# 大規模代理

* 添加**永久**或**臨時**代理；按功能標記；設定啟動方法（SSH、JNLP、雲端）。
* Jenkins 監控磁碟、交換空間、暫存檔、時鐘漂移，並能自動將不健康的節點離線。保持標籤整潔，並在階段中使用 `agent { label 'docker' }` 進行路由。([Jenkins][2])

---

# 不會出問題的流水線（現代 Jenkinsfile）

**Declarative vs Scripted**：首選 **Declarative**——結構更清晰，有防護欄（`post`、`options`、`when`、`environment`、`input`、`parallel`）。([Jenkins][1])

**最小 CI 範例：**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // 或在您的 SCM 中使用 webhooks
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { sh './gradlew test' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
  }
  post {
    always { junit 'build/test-results/test/*.xml'; archiveArtifacts 'build/libs/*.jar' }
    failure { mail to: 'team@example.com', subject: "Build failed ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```

**關鍵參考：** Pipeline 手冊、語法參考和步驟文件。([Jenkins][1])

---

# 多分支、GitHub/GitLab 和 PRs

使用**多分支流水線**或 GitHub/Bitbucket 組織任務，以便每個帶有 `Jenkinsfile` 的儲存庫分支/PR 都能自動建置（透過 webhooks）。將分支行為保留在程式碼中，避免點擊操作。

---

# 大規模重用：共享函式庫

當您在多個儲存庫中重複步驟時，建立一個 **Jenkins 共享函式庫**（vars 函數、流水線步驟），並在 `Jenkinsfile` 中使用 `@Library('your-lib') _` 導入它。這可以防止複製貼上流水線並集中修復。

---

# Configuration as Code (JCasC)

將您的控制器配置視為程式碼：將其檢入 Git，透過 PR 審查，並可重複地引導新的控制器。

* 安裝 **Configuration as Code** 外掛。
* 編寫捕獲全域安全性、代理啟動器、工具安裝程式、資料夾、憑證綁定等的 YAML。
* 在啟動時（環境變數 `CASC_JENKINS_CONFIG`）或從 UI 載入它。([Jenkins Plugins][8], [Jenkins][9])

**JCasC 小試：**

```yaml
jenkins:
  systemMessage: "Jenkins managed by JCasC"
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "viewer"
            permissions:
              - "Overall/Read"
            assignments:
              - "devs"
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${ADMIN_PW}"
unclassified:
  location:
    url: "https://ci.example.com/"
```

官方文件和外掛頁面如上。([Jenkins][9], [Jenkins Plugins][8])

---

# 外掛（明智地使用它們）

* **必備知識**：Credentials、Matrix/Role-Strategy、Pipeline、Git、SSH、Email、Artifact Manager（例如 S3/GCS）、Cloud agents (Kubernetes)、JCasC。
* 保持外掛**最少化並更新**，固定關鍵外掛，並在臨時控制器中測試更新。實用的外掛文件位於 jenkins.io 和每個外掛的頁面上。([Jenkins][10])

---

# 可觀測性與衛生

* **日誌**：使用控制器日誌記錄器 + 將日誌發送到 ELK/CloudWatch。
* **成品**：僅歸檔您需要的內容。
* **JUnit**：始終發布測試報告；在測試失敗時中止建置。
* **佇列健康狀況**：監視建置佇列和代理利用率；相應地擴展代理。
* **備份**：備份 `$JENKINS_HOME` 或使用 JCasC + 臨時控制器。

---

# 快速安全改進

* 在不需要的地方停用 CLI；優先使用 API 令牌。
* 將**服務**帳戶與人員分開。
* 僅使用資料夾範圍的密碼；絕不回顯密碼。
* 鎖定指令碼審批；限制 Declarative 中的 `script` 步驟。
* 定期審計角色。指引在 Jenkins 的安全文件中。([Jenkins][3])

---

# 典型的「Day-2」改進

* **並行**測試分片以縮短建置時間。
* **快取**（例如，代理上的 Gradle/Maven 快取）。
* **Docker-in-Docker** 或 **Kubernetes 代理**，用於乾淨、可重複的建置映像。
* 早期階段的**品質閘道**（lint、SAST/DAST）。
* **晉升**任務或多環境部署階段，帶有 `when` 條件和手動 `input`。

---

# 疑難排解備忘錄

* 建置卡住？檢查代理日誌、工作區磁碟和節點時鐘偏差。Jenkins 會自動將超出健康閾值的節點離線。([Jenkins][2])
* 找不到憑證？確保範圍（資料夾 vs 全域）和正確的 `credentialsId`。([Jenkins][4])
* 驗證異常？重新驗證領域 ↔ 授權策略配對（Matrix/Role-strategy）。([Jenkins][3], [Jenkins Plugins][6])
* 流水線語法錯誤？使用 **Declarative** 驗證器步驟 / 線上編輯器進行驗證。([Jenkins][11])

---

# 可複製的「黃金」起點

```groovy
pipeline {
  agent { label 'k8s || docker || linux' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '50')); ansiColor('xterm') }
  environment { JAVA_TOOL_OPTIONS = '-XX:+UseContainerSupport' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup')    { steps { sh 'python -V || true' } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { junit 'build/test-results/test/*.xml' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
    stage('Deploy')   { when { branch 'main' } steps { input 'Ship to staging?'; sh './scripts/deploy_staging.sh' } }
  }
  post {
    failure { echo "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
    always  { archiveArtifacts artifacts: 'build/libs/*.jar', fingerprint: true }
  }
}
```

---

# 何處閱讀更多（高價值文件）

* **Pipeline: 概述與語法**（Declarative vs Scripted，所有指令和步驟）。([Jenkins][1])
* **安全性與授權**（Matrix），以及用於 RBAC 的 **Role-Strategy 外掛**。([Jenkins][3], [Jenkins Plugins][5])
* **代理與節點**（添加、健康狀況、標籤）。([Jenkins][2])
* **憑證使用**（UI 和 Pipeline 輔助程式/綁定）。([Jenkins][4])
* **Configuration as Code (JCasC)**（概念 + 外掛）。([Jenkins][9], [Jenkins Plugins][8])

---

如果您需要，我可以根據**您的確切設定**（GitHub vs GitLab、內部部署 vs k8s 代理，以及您的 RBAC 模型）來調整此指南，並草擬：

* 一個 **JCasC** YAML 種子，
* 一個適用於您團隊的 **role-strategy** 映射，以及
* 一個用於標準化階段的 **共享函式庫** 骨架。

[1]: https://www.jenkins.io/doc/book/pipeline/?utm_source=chatgpt.com "Pipeline"
[2]: https://www.jenkins.io/doc/book/managing/nodes/?utm_source=chatgpt.com "Managing Nodes"
[3]: https://www.jenkins.io/doc/book/security/managing-security/?utm_source=chatgpt.com "Managing Security"
[4]: https://www.jenkins.io/doc/book/using/using-credentials/?utm_source=chatgpt.com "Using credentials"
[5]: https://plugins.jenkins.io/matrix-auth/?utm_source=chatgpt.com "Matrix Authorization Strategy"
[6]: https://plugins.jenkins.io/role-strategy/?utm_source=chatgpt.com "Role-based Authorization Strategy"
[7]: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/?utm_source=chatgpt.com "Using a Jenkinsfile"
[8]: https://plugins.jenkins.io/configuration-as-code/?utm_source=chatgpt.com "Configuration as Code | Jenkins plugin"
[9]: https://www.jenkins.io/doc/book/managing/casc/?utm_source=chatgpt.com "Configuration as Code"
[10]: https://www.jenkins.io/doc/developer/publishing/documentation/?utm_source=chatgpt.com "Plugin Documentation"
[11]: https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/?utm_source=chatgpt.com "Pipeline: Declarative"