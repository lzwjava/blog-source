---
audio: false
generated: true
lang: hant
layout: post
title: 精通 SonarQube：Java 與 Spring 項目實戰
translated: true
type: note
---

# 使用 SonarQube 與 Java 及 Spring 專案的完整指南

## 簡介
SonarQube 是一個用於持續檢測程式碼品質的開源平台。它執行靜態程式碼分析以偵測錯誤、程式碼異味、安全漏洞，並計算程式碼覆蓋率。本指南提供在 Java Spring 專案中設定和使用 SonarQube 的完整概述，包括安裝、配置、整合及最佳實踐。

## 目錄
1. [什麼是 SonarQube？](#什麼是-sonarqube)
2. [先決條件](#先決條件)
3. [安裝 SonarQube](#安裝-sonarqube)
4. [設定 Java Spring 專案](#設定-java-spring-專案)
5. [為專案配置 SonarQube](#為專案配置-sonarqube)
6. [執行 SonarQube 分析](#執行-sonarqube-分析)
7. [解讀 SonarQube 結果](#解讀-sonarqube-結果)
8. [最佳實踐](#最佳實踐)
9. [疑難排解常見問題](#疑難排解常見問題)
10. [結論](#結論)

## 什麼是 SonarQube？
SonarQube 是一個透過分析原始碼來提供持續程式碼品質檢測的工具，可分析：
- **錯誤**：程式碼中的潛在錯誤。
- **程式碼異味**：可能導致技術債的可維護性問題。
- **安全漏洞**：可能被利用的安全問題。
- **程式碼覆蓋率**：單元測試覆蓋的程式碼百分比。
- **重複程式碼**：可重構的重複程式碼區塊。

它支援多種語言，包括 Java，並能與 Maven 和 Gradle 等建置工具以及 CI/CD 管道無縫整合。

## 先決條件
在設定 SonarQube 之前，請確保您具備：
- **Java Development Kit (JDK)**：版本 11 或更高（SonarQube 需要 Java 11 或 17）。
- **Maven 或 Gradle**：用於 Java Spring 專案的建置工具。
- **SonarQube 伺服器**：版本 9.9 LTS 或更高（社群版足以應付大多數使用情況）。
- **SonarScanner**：用於執行分析的 CLI 工具。
- **資料庫**：SonarQube 需要資料庫（例如 PostgreSQL、MySQL 或用於測試的嵌入式 H2）。
- **Spring 專案**：一個可運作的 Spring Boot 或 Spring Framework 專案。
- **IDE**：用於開發的 IntelliJ IDEA、Eclipse 或 VS Code。

## 安裝 SonarQube

### 步驟 1：下載並安裝 SonarQube
1. **下載 SonarQube**：
   - 造訪 [SonarQube 下載頁面](https://www.sonarqube.org/downloads/)。
   - 根據您的需求選擇社群版（免費）或其他版本。
   - 下載 ZIP 檔案（例如 `sonarqube-9.9.0.zip`）。

2. **解壓縮 ZIP**：
   - 將下載的檔案解壓縮到目錄，例如 `/opt/sonarqube` 或 `C:\sonarqube`。

3. **配置資料庫**：
   - SonarQube 需要資料庫。對於生產環境，請使用 PostgreSQL 或 MySQL。對於測試，嵌入式 H2 資料庫已足夠。
   - PostgreSQL 範例：
     - 安裝 PostgreSQL 並建立資料庫（例如 `sonarqube`）。
     - 更新 SonarQube 配置檔案（`conf/sonar.properties`）：
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **啟動 SonarQube**：
   - 導航至 SonarQube 目錄（`bin/<platform>`）。
   - 執行啟動腳本：
     - 在 Linux/Mac 上：`./sonar.sh start`
     - 在 Windows 上：`StartSonar.bat`
   - 在 `http://localhost:9000`（預設連接埠）存取 SonarQube。

5. **登入**：
   - 預設憑證：`admin/admin`。
   - 首次登入後請變更密碼。

### 步驟 2：安裝 SonarScanner
1. **下載 SonarScanner**：
   - 從 [SonarQube Scanner 頁面](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/)下載。
   - 解壓縮到目錄，例如 `/opt/sonar-scanner`。

2. **配置環境變數**：
   - 將 SonarScanner 加入您的 PATH：
     - 在 Linux/Mac 上：`export PATH=$PATH:/opt/sonar-scanner/bin`
     - 在 Windows 上：將 `C:\sonar-scanner\bin` 加入系統 PATH。

3. **驗證安裝**：
   - 執行 `sonar-scanner --version` 以確認安裝。

## 設定 Java Spring 專案
在本指南中，我們將使用帶有 Maven 的 Spring Boot 專案。對於 Gradle 或非 Boot 的 Spring 專案，步驟類似。

1. **建立 Spring Boot 專案**：
   - 使用 [Spring Initializer](https://start.spring.io/) 建立專案，包含：
     - 依賴項：Spring Web、Spring Data JPA、H2 Database、Spring Boot Starter Test。
     - 建置工具：Maven。
   - 下載並解壓縮專案。

2. **新增單元測試**：
   - 確保您的專案有單元測試以測量程式碼覆蓋率。
   - 範例測試類別：
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **新增 Jacoco 以取得程式碼覆蓋率**：
   - 將 JaCoCo Maven 插件加入 `pom.xml` 以產生程式碼覆蓋率報告：
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## 為專案配置 SonarQube

1. **建立 SonarQube 專案**：
   - 登入 SonarQube（`http://localhost:9000`）。
   - 點擊 **Create Project** > **Manually**。
   - 提供 **Project Key**（例如 `my-spring-project`）和 **Display Name**。
   - 產生用於身份驗證的 token（例如 `my-token`）。

2. **配置 `sonar-project.properties`**：
   - 在您的 Spring 專案根目錄中，建立 `sonar-project.properties` 檔案：
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **Maven 整合（替代方案）**：
   - 除了 `sonar-project.properties`，您可以在 `pom.xml` 中配置 SonarQube：
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## 執行 SonarQube 分析

1. **使用 SonarScanner**：
   - 導航至專案根目錄。
   - 執行：
     ```bash
     sonar-scanner
     ```
   - 確保在分析之前執行測試（對於 Maven 專案為 `mvn test`）。

2. **使用 Maven**：
   - 執行：
     ```bash
     mvn clean verify sonar:sonar
     ```
   - 此指令會編譯程式碼、執行測試、產生覆蓋率報告並將結果傳送至 SonarQube。

3. **驗證結果**：
   - 開啟 SonarQube（`http://localhost:9000`）並導航至您的專案。
   - 檢查儀表板以查看分析結果。

## 解讀 SonarQube 結果
SonarQube 儀表板提供：
- **概覽**：問題、覆蓋率和重複程式碼的摘要。
- **問題**：錯誤、安全漏洞和程式碼異味的列表，包含嚴重性（阻塞、嚴重、主要等）。
- **程式碼覆蓋率**：測試覆蓋的程式碼百分比（透過 JaCoCo）。
- **重複程式碼**：重複的程式碼區塊。
- **品質閘道**：根據預先定義的閾值（例如覆蓋率 > 80%）的通過/失敗狀態。

### 範例操作：
- **修復錯誤**：處理嚴重問題，例如空指標解參考。
- **重構程式碼異味**：簡化複雜方法或移除未使用的程式碼。
- **改善覆蓋率**：為未覆蓋的程式碼編寫額外的單元測試。

## 最佳實踐
1. **與 CI/CD 整合**：
   - 將 SonarQube 分析加入您的 CI/CD 管道（例如 Jenkins、GitHub Actions）。
   - GitHub Actions 工作流程範例：
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **定義品質閘道**：
   - 在 SonarQube 中設定程式碼覆蓋率、錯誤和安全漏洞的閾值。
   - 範例：如果覆蓋率 < 80% 或存在嚴重問題，則使建置失敗。

3. **使用 SonarLint**：
   - 在您的 IDE（例如 IntelliJ IDEA）中安裝 SonarLint 插件，以在開發期間捕捉問題。

4. **定期分析**：
   - 在每次提交或每天執行 SonarQube 分析，以早期發現問題。

5. **自訂規則**：
   - 根據專案需求調整 SonarQube 規則（例如停用不相關的規則或新增自訂規則）。

## 疑難排解常見問題
1. **分析上傳失敗**：
   - 檢查配置中的 `sonar.host.url` 和 `sonar.token`。
   - 確保 SonarQube 伺服器正在執行（`http://localhost:9000`）。

2. **無程式碼覆蓋率**：
   - 驗證 `pom.xml` 中的 JaCoCo 插件是否正確配置。
   - 在分析之前執行 `mvn test` 以產生 `jacoco.exec`。

3. **資料庫連線錯誤**：
   - 確認 `sonar.properties` 中的資料庫憑證。
   - 確保資料庫伺服器正在執行。

4. **記憶體不足**：
   - 在 `sonar.properties` 中增加 JVM 記憶體：
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## 結論
SonarQube 是一個在 Java Spring 專案中維護程式碼品質的強大工具。透過將其整合到您的開發工作流程中，您可以早期發現問題、改善程式碼可維護性並確保穩健的安全性。定期分析，結合 CI/CD 整合和 SonarLint 等最佳實踐，將有助於您維護高品質的程式碼庫。