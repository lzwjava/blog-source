---
audio: false
generated: true
lang: hant
layout: post
title: Maven 發布插件
translated: true
---

這是一個全面的指南，介紹如何使用 **Maven Release Plugin** 來管理和自動化 Maven 專案的發布流程。

---

### 什麼是 Maven Release Plugin？

**Maven Release Plugin** 是一個自動化 Maven 專案發布流程的工具。它處理以下任務：

- 更新專案 POM 文件中的版本號。
- 提交更改到版本控制系統 (VCS)，例如 Git。
- 在 VCS 中為發布創建標籤。
- 建立和部署發布工件。
- 通過更新版本號來為下一個開發週期做準備。

該插件的兩個主要目標是：

- **`release:prepare`**：通過更新版本、提交更改和在 VCS 中標記發布來準備專案進行發布。
- **`release:perform`**：使用 VCS 中標記的代碼來建立和部署已發布的版本。

---

### 使用 Maven Release Plugin 的逐步指南

#### 1. 在 POM 文件中添加 Maven Release Plugin

要使用插件，您需要在專案的 `pom.xml` 中包含它。將其添加到 `<build><plugins>` 部分，如下所示：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- 使用最新的穩定版本 -->
        </plugin>
    </plugins>
</build>
```

**注意**：請查看 [官方 Maven Release Plugin 頁面](https://maven.apache.org/maven-release/maven-release-plugin/) 以獲取最新版本，並相應地替換 `2.5.3`。

#### 2. 配置 SCM (源代碼管理) 部分

插件與您的 VCS（例如 Git）交互以提交更改和創建標籤。您必須在 `pom.xml` 的 `<scm>` 部分指定 VCS 詳細信息。對於 GitHub 上的 Git 存儲庫，它可能看起來像這樣：

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- 將 `username` 和 `project` 替換為您的實際 GitHub 用戶名和存儲庫名稱。
- 如果您使用不同的 Git 托管服務（例如 GitLab、Bitbucket），請調整 URL。
- 確保您已配置必要的憑證（例如 SSH 密鑰或個人訪問令牌）以將更改推送到存儲庫。

#### 3. 準備專案進行發布

在運行發布命令之前，請確保您的專案已準備就緒：

- 所有測試都通過 (`mvn test`)。
- 工作目錄中沒有未提交的更改（運行 `git status` 進行檢查）。
- 您在正確的分支（例如 `master` 或 `main`）上進行發布。

#### 4. 運行 `release:prepare`

`release:prepare` 目標為您的專案進行發布準備。在終端中執行以下命令：

```bash
mvn release:prepare
```

**`release:prepare` 期間發生的情況**：

- **檢查未提交的更改**：確保工作目錄是乾淨的。
- **提示版本**：要求發布版本和下一個開發版本。
  - 例如：如果您的當前版本是 `1.0-SNAPSHOT`，它可能建議 `1.0` 進行發布和 `1.1-SNAPSHOT` 進行下一個開發版本。您可以接受默認值或輸入自定義版本（例如，`1.0.1` 進行補丁發布）。
- **更新 POM 文件**：將版本更改為發布版本（例如 `1.0`），提交更改並在 VCS 中標記它（例如 `project-1.0`）。
- **為下一個週期做準備**：將 POM 更新為下一個開發版本（例如 `1.1-SNAPSHOT`）並提交它。

**可選的乾跑**：要測試流程而不進行更改，請使用：

```bash
mvn release:prepare -DdryRun=true
```

這模擬準備步驟而不提交或標記。

#### 5. 運行 `release:perform`

準備好發布後，使用以下命令進行建立和部署：

```bash
mvn release:perform
```

**`release:perform` 期間發生的情況**：

- 從 VCS 中檢出標記的版本。
- 建立專案。
- 將工件部署到 POM 的 `<distributionManagement>` 部分中指定的存儲庫。

**配置 `<distributionManagement>`**（如果部署到遠程存儲庫）：

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- 將 URL 替換為您的存儲庫管理器的地址（例如 Nexus、Artifactory）。
- 確保在 `~/.m2/settings.xml` 文件的 `<servers>` 下配置了匹配 `id` 的憑證。

#### 6. 驗證發布

`release:perform` 後，驗證發布：

- 檢查您的存儲庫管理器，確保工件（例如 JAR、源代碼）已部署。
- 通過在其 POM 中將其添加為依賴項來在另一個專案中測試已發布的版本。

---

### 額外配置和技巧

#### 處理失敗

- **清理**：如果發布流程失敗，請使用：
  ```bash
  mvn release:clean
  ```
  以移除插件創建的臨時文件。
- **回滾**：要撤消 `release:prepare` 所做的更改：
  ```bash
  mvn release:rollback
  ```
  請謹慎並驗證哪些更改已被撤消。

#### 多模塊專案

對於多模塊專案，插件默認情況下會一致地更新所有模塊的版本。確保父 POM 包含插件和 SCM 配置。

#### 批處理模式用於自動化

要在非交互模式下運行發布（例如在 CI/CD 管道中），請使用 `-B` 旗標並指定版本：

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### 常見問題及解決方案

- **VCS 錯誤**：確保 Git 命令（例如 `git commit`、`git push`）手動工作。檢查身份驗證（SSH 密鑰、令牌）。
- **建立失敗**：驗證本地建立成功 (`mvn clean install`) 並正確解析依賴項。
- **版本策略**：在提示或通過屬性自定義版本，如果默認值不適合您的需求。

---

### 命令摘要

1. **準備發布**：
   ```bash
   mvn release:prepare
   ```
2. **執行發布**：
   ```bash
   mvn release:perform
   ```
3. **可選的乾跑**：
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **如果需要清理或回滾**：
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### 結論

Maven Release Plugin 通過自動化版本管理、VCS 交互和部署來簡化發布流程。通過將插件添加到您的 POM、配置您的 SCM 並遵循 `release:prepare` 和 `release:perform` 步驟，您可以高效地發布 Maven 專案。始終使用乾跑測試您的配置並驗證結果，以確保順利的發布流程。