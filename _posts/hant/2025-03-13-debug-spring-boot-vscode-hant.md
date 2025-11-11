---
audio: false
generated: true
lang: hant
layout: post
title: 在 Visual Studio Code 中偵錯 Spring Boot 應用程式
translated: true
type: note
---

要在 Visual Studio Code (VSCode) 中對 Maven Spring Boot 專案進行除錯，您可以按照以下簡單步驟設定並以除錯模式執行應用程式。本指南假設您已有一個基本的 Maven Spring Boot 專案，包含 `pom.xml` 檔案以及帶有 `@SpringBootApplication` 註解的主類別。具體操作如下：

### 步驟 1：安裝必要擴充功能
開始之前，請確保 VSCode 已安裝 Java 和 Spring Boot 開發所需的擴充功能：
- **Java Extension Pack**：包含 Red Hat 提供的 Java 語言支援等必要工具，具備除錯功能及其他 Java 開發實用工具。
- **Spring Boot Extension Pack**：此套件透過 Spring Boot Dashboard、Spring Boot Tools 等功能增強 Spring Boot 開發體驗。

安裝方法：
1. 開啟 VSCode。
2. 進入擴充功能檢視（Windows/Linux 按 `Ctrl+Shift+X`，macOS 按 `Cmd+Shift+X`）。
3. 搜尋「Java Extension Pack」和「Spring Boot Extension Pack」，然後分別點擊**安裝**。

### 步驟 2：開啟您的 Maven Spring Boot 專案
- 啟動 VSCode，透過選擇**檔案 > 開啟資料夾**來開啟您的專案資料夾，選取包含 `pom.xml` 檔案的目錄。
- VSCode 會偵測到 `pom.xml`，Java Extension Pack 將自動索引專案並解析相依性。此過程可能需要一些時間，請等待完成（右下角狀態列會顯示進度）。

### 步驟 3：建立或編輯 `launch.json` 檔案
要設定除錯功能，您需要在 VSCode 中設定 `launch.json` 檔案：
1. 點擊側邊欄的蟲子與播放圖示或按 `Ctrl+Shift+D` 開啟**執行與除錯**檢視。
2. 若無現有除錯設定，點擊「建立 launch.json 檔案」；若已存在，點擊齒輪圖示進行編輯。
3. 出現提示時，選擇 **Java** 作為環境。VSCode 將在專案的 `.vscode` 資料夾中生成預設的 `launch.json` 檔案。
4. 為您的 Spring Boot 應用程式新增或修改除錯設定。以下為範例設定：

    ```json
    {
        "type": "java",
        "name": "Debug Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - 將 `"com.example.demo.DemoApplication"` 替換為您主類別的完整限定名稱（例如 `com.yourcompany.yourapp.YourApplication`）。
    - 將 `"demo"` 替換為您的專案名稱，通常是 `pom.xml` 中的 `<artifactId>`。

5. 儲存 `launch.json` 檔案。

#### 可選：新增引數
若您的應用程式需要特定引數（例如 Spring 設定檔），可加入：
```json
{
    "type": "java",
    "name": "Debug Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### 步驟 4：開始除錯
- 在**執行與除錯**檢視中，從頂部下拉選單選擇 **"Debug Spring Boot"**。
- 點擊綠色播放按鈕（或按 `F5`）以除錯模式啟動應用程式。
- VSCode 將使用 Maven 編譯專案，啟動 Spring Boot 應用程式，並自動附加除錯器。

### 步驟 5：設定中斷點並進行除錯
- 在專案中開啟 Java 檔案（例如控制器或服務類別）。
- 在行號左側的裝訂線點擊以設定中斷點，紅色圓點將顯示。
- 與您的應用程式互動（例如透過瀏覽器或 API 用戶端）。當執行到中斷點時，VSCode 會暫停，讓您能夠：
  - 在**變數**面板中檢查變數值。
  - 使用**逐步執行**（`F10`）、**步入**（`F11`）或**繼續**（`F5`）等控制項逐步執行程式碼。
  - 在除錯側邊欄中檢視呼叫堆疊等資訊。

### 替代方法
雖然建議使用 `launch.json` 方法以獲得靈活性，您也可以透過以下方式進行除錯：
- **Maven 檢視**：
  1. 在側邊欄開啟 Maven 檢視（尋找「M」圖示或透過擴充功能啟用）。
  2. 展開您的專案，導覽至 Plugins 下的 `spring-boot`，右鍵點擊 `spring-boot:run` 並選擇**除錯**。
  3. 應用程式將啟動，除錯器會自動附加。
- **Spring Boot Dashboard**：
  1. 開啟 Spring Boot Dashboard（通常在 Explorer 檢視中，或透過指令選擇區：`Spring Boot Dashboard`）。
  2. 找到您的應用程式，右鍵點擊並選擇**除錯**（若可用）。

### 必要條件與注意事項
- 確保系統已安裝 **Maven** 並可透過命令列存取，或使用 VSCode 內嵌的 Maven（如有需要可透過設定配置）。
- 確認您的專案可成功建置（`mvn clean install`），以避免除錯期間出現執行階段錯誤。
- 使用 `pom.xml` 中指定的相容 Java 版本（例如透過 `<java.version>`）。

遵循這些步驟，您就能在 VSCode 中有效除錯 Maven Spring Boot 專案，利用其強大的除錯工具來識別並解決程式碼中的問題。