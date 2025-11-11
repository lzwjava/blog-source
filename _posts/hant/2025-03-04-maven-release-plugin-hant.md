---
audio: false
generated: true
lang: hant
layout: post
title: Maven 發佈插件
translated: true
type: note
---

這是一份關於如何使用 **Maven Release Plugin** 來管理和自動化 Maven 專案發佈流程的完整指南。

---

### 什麼是 Maven Release Plugin？

**Maven Release Plugin** 是一個用於自動化 Maven 專案發佈流程的工具。它負責處理以下任務：

- 更新專案 POM 檔案中的版本號碼。
- 將變更提交到你的版本控制系統（VCS），例如 Git。
- 在 VCS 中為發佈建立標籤。
- 建置並部署發佈成品。
- 透過再次更新版本號碼，為下一個開發週期做準備。

該外掛的兩個主要目標是：

- **`release:prepare`**：透過更新版本、提交變更並在 VCS 中標記發佈，來準備專案發佈。
- **`release:perform`**：使用 VCS 中標記的程式碼來建置和部署已發佈的版本。

---

### 使用 Maven Release Plugin 的逐步指南

#### 1. 將 Maven Release Plugin 加入你的 POM 檔案

要使用此外掛，你需要將它包含在專案的 `pom.xml` 中。請在 `<build><plugins>` 區段下加入如下內容：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- 請使用最新的穩定版本 -->
        </plugin>
    </plugins>
</build>
```

**注意**：請查閱 [官方 Maven Release Plugin 頁面](https://maven.apache.org/maven-release/maven-release-plugin/) 以獲取最新版本，並相應地替換 `2.5.3`。

#### 2. 配置 SCM（原始碼控制管理）區段

此外掛會與你的 VCS（例如 Git）互動以提交變更和建立標籤。你必須在 `pom.xml` 的 `<scm>` 區段中指定你的 VCS 詳細資訊。對於託管在 GitHub 上的 Git 儲存庫，可能如下所示：

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- 將 `username` 和 `project` 替換為你實際的 GitHub 使用者名稱和儲存庫名稱。
- 如果你使用其他 Git 託管服務（例如 GitLab、Bitbucket），請調整 URL。
- 確保你已配置必要的憑證（例如 SSH 金鑰或個人存取權杖）以推送變更到儲存庫。

#### 3. 準備專案發佈

在執行發佈指令之前，請確保你的專案已準備就緒：

- 所有測試通過 (`mvn test`)。
- 工作目錄中沒有未提交的變更（執行 `git status` 檢查）。
- 你位於正確的分支（例如 `master` 或 `main`）以進行發佈。

#### 4. 執行 `release:prepare`

`release:prepare` 目標會準備你的專案進行發佈。在終端機中執行以下指令：

```bash
mvn release:prepare
```

**`release:prepare` 期間會發生什麼**：

- **檢查未提交的變更**：確保你的工作目錄是乾淨的。
- **提示輸入版本**：要求輸入發佈版本和下一個開發版本。
  - 範例：如果你目前的版本是 `1.0-SNAPSHOT`，它可能會建議 `1.0` 作為發佈版本，`1.1-SNAPSHOT` 作為下一個開發版本。你可以接受預設值或輸入自訂版本（例如，修補程式發佈使用 `1.0.1`）。
- **更新 POM 檔案**：將版本更改為發佈版本（例如 `1.0`），提交變更，並在 VCS 中為其建立標籤（例如 `project-1.0`）。
- **為下個週期做準備**：將 POM 更新為下一個開發版本（例如 `1.1-SNAPSHOT`）並提交。

**可選的乾跑**：要在不進行實際變更的情況下測試流程，請使用：

```bash
mvn release:prepare -DdryRun=true
```

這將模擬準備步驟，而不進行提交或標記。

#### 5. 執行 `release:perform`

準備好發佈後，使用以下指令建置並部署：

```bash
mvn release:perform
```

**`release:perform` 期間會發生什麼**：

- 從 VCS 中簽出標記的版本。
- 建置專案。
- 將成品部署到你的 POM 中 `<distributionManagement>` 區段指定的儲存庫。

**配置 `<distributionManagement>`**（如果要部署到遠端儲存庫）：

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

- 將 URL 替換為你的儲存庫管理器的地址（例如 Nexus、Artifactory）。
- 確保憑證已在你的 `~/.m2/settings.xml` 檔案中的 `<servers>` 下設定，並具有匹配的 `id`。

#### 6. 驗證發佈

在 `release:perform` 之後，請驗證發佈：

- 檢查你的儲存庫管理器，確保成品（例如 JARs、原始碼）已部署。
- 在另一個專案中，透過在其 POM 中加入其作為依賴項來測試已發佈的版本。

---

### 其他配置與提示

#### 處理失敗

- **清理**：如果發佈流程失敗，請使用：
  ```bash
  mvn release:clean
  ```
  來移除此外掛建立的暫存檔案。
- **回滾**：要復原 `release:prepare` 所做的變更：
  ```bash
  mvn release:rollback
  ```
  請謹慎操作，並驗證哪些變更被復原。

#### 多模組專案

對於多模組專案，此外掛預設會在所有模組中一致地更新版本。請確保父 POM 包含此外掛和 SCM 配置。

#### 用於自動化的批次模式

要以非互動方式執行發佈（例如在 CI/CD 管道中），請使用 `-B` 標幟並指定版本：

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### 常見問題與解決方案

- **VCS 錯誤**：確保 Git 指令（例如 `git commit`、`git push`）可以手動執行。檢查認證（SSH 金鑰、權杖）。
- **建置失敗**：驗證本地建置是否成功 (`mvn clean install`) 以及依賴項是否正確解析。
- **版本策略**：如果預設值不符合你的需求，可以在提示期間或透過屬性自訂版本。

---

### 指令摘要

1. **準備發佈**：
   ```bash
   mvn release:prepare
   ```
2. **執行發佈**：
   ```bash
   mvn release:perform
   ```
3. **可選乾跑**：
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **如有需要，進行清理或回滾**：
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### 結論

Maven Release Plugin 透過自動化版本管理、VCS 互動和部署，簡化了發佈流程。透過將此外掛加入你的 POM、配置你的 SCM，並遵循 `release:prepare` 和 `release:perform` 步驟，你可以有效地發佈你的 Maven 專案。請務必使用乾跑測試你的配置，並驗證結果以確保發佈流程順利。