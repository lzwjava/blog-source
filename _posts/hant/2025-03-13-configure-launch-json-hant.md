---
audio: false
generated: true
lang: hant
layout: post
title: 在 VSCode 中配置 Spring Boot 的 launch.json
translated: true
type: note
---

要為 Visual Studio Code (VSCode) 中的 Maven Spring Boot 專案設定 `launch.json` 檔案，您需要建立一個啟動配置，讓 VSCode 能夠使用其 Java 擴充功能來執行和偵錯您的應用程式。以下是逐步指南，協助您完成此設定。

### 必要條件
在繼續之前，請確保以下事項：
- 您已在 VSCode 中安裝 **Java Extension Pack**。此套件包含必要的擴充功能，例如 Red Hat 提供的 "Debugger for Java" 和 "Language Support for Java"，它們為執行和偵錯 Java 應用程式（包括 Spring Boot 專案）提供支援。
- 您的 Spring Boot 專案是 Maven 專案，且具有有效的 `pom.xml` 檔案。
- 該專案具有帶有 `@SpringBootApplication` 註解的主類別，其中包含啟動應用程式的 `main` 方法。

### 設定 `launch.json` 的步驟
1. **定位主類別**
   - 在典型的 Spring Boot 專案中，主類別位於 `src/main/java` 目錄中，並帶有 `@SpringBootApplication` 註解。例如，它可能命名為 `com.example.demo.DemoApplication`。
   - 在 VSCode 中開啟您的專案，並識別此類別的完整限定名稱（例如 `com.example.demo.DemoApplication`）。

2. **確定專案名稱**
   - Maven 專案中的專案名稱對應於您的 `pom.xml` 檔案中定義的 `artifactId`。
   - 開啟您的 `pom.xml` 檔案並尋找 `<artifactId>` 標籤。例如：
     ```xml
     <artifactId>demo</artifactId>
     ```
     此處的專案名稱將是 `demo`。

3. **開啟偵錯視圖**
   - 在 VSCode 中，點擊左側邊欄中的 **偵錯** 圖示（或在 Mac 上按 `Cmd+Shift+D`）。
   - 點擊「執行與偵錯」下拉選單旁邊的齒輪圖標 ⚙️ 以設定啟動設定。如果不存在 `launch.json`，VSCode 將提示您建立一個。

4. **建立或編輯 `launch.json`**
   - 如果提示選擇環境，請選擇 **Java**。這將在您專案的 `.vscode` 資料夾中產生一個基本的 `launch.json` 檔案。
   - 開啟 `launch.json` 檔案。如果已存在，您可以直接編輯它。

5. **新增啟動配置**
   - 在 `launch.json` 的 `"configurations"` 陣列內新增以下配置。請將佔位符替換為您專案的詳細資訊：
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **欄位說明：**
       - `"type": "java"`：指定這是一個 Java 啟動配置。
       - `"name": "Launch Spring Boot App"`：此配置的描述性名稱，將顯示在偵錯下拉選單中。
       - `"request": "launch"`：指示 VSCode 應啟動應用程式（而不是附加到現有程序）。
       - `"mainClass"`：您的 Spring Boot 主類別的完整限定名稱（例如 `com.example.demo.DemoApplication`）。
       - `"projectName"`：來自您的 `pom.xml` 的 `artifactId`（例如 `demo`），這有助於 VSCode 在多模組設定中定位專案。

   - 以下是包含此配置的完整 `launch.json` 檔案範例：
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **可選：新增 VM 參數或程式參數**
   - 如果您的應用程式需要其他設定（例如啟動 Spring 設定檔），您可以使用 `"vmArgs"` 或 `"args"` 來新增它們：
     - 帶有 Spring 設定檔的範例：
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       這將 `spring.profiles.active` 屬性設定為 `dev`。
     - 帶有程式參數的範例：
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **儲存並執行**
   - 儲存 `launch.json` 檔案。
   - 返回偵錯視圖，從下拉選單中選擇 **"Launch Spring Boot App"**，然後點擊綠色播放按鈕（或按 `F5`）。
   - VSCode 將使用 Maven 和 Java 擴充功能來建置並執行您的 Spring Boot 應用程式。您應該在偵錯主控台中看到 Spring Boot 的啟動日誌。

### 驗證配置
- 如果您的 Spring Boot 應用程式是 Web 應用程式，請開啟瀏覽器並導覽至 `http://localhost:8080`（或您的 `application.properties` 或 `application.yml` 檔案中指定的連接埠）以確認其正在執行。
- 您也可以在程式碼中設定中斷點，並使用偵錯控制項（暫停、逐步執行等）來偵錯您的應用程式。

### 注意事項
- VSCode 中的 Java 擴充功能會根據您的 `pom.xml` 自動處理類別路徑和建置過程，因此您通常不需要事先手動執行 `mvn clean install`。
- 如果您的專案是多模組 Maven 設定的一部分，請確保 `projectName` 與正確模組的 `artifactId` 相符。
- 對於進階配置（例如自訂工作目錄或啟動前任務），請參閱 [VSCode Java 偵錯文件](https://code.visualstudio.com/docs/java/java-debugging)。

透過此設定，您的 `launch.json` 應該已正確配置，以便在 VSCode 中執行和偵錯您的 Maven Spring Boot 專案！