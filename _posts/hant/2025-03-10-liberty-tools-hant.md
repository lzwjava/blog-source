---
audio: false
generated: true
lang: hant
layout: post
title: Visual Studio Code 自由工具擴充套件
translated: true
type: note
---

以下是關於如何在 Visual Studio Code 中使用 Liberty Tools 擴充功能來操作 WebSphere Liberty 伺服器的概述：

---

### 1. 安裝 Liberty Tools 擴充功能
- **尋找並安裝：**  
  開啟 VS Code 的擴充功能視圖，搜尋 **"IBM WebSphere Liberty Tools"** 並安裝。
- **擴充功能優勢：**  
  此擴充功能將伺服器管理、應用程式部署和偵錯功能整合到 VS Code 中。

---

### 2. 準備您的 WebSphere Liberty 伺服器
- **安裝或指向 Liberty 執行環境：**  
  若您尚未安裝 Liberty 伺服器，請從 IBM 下載並安裝。若已安裝，請記下其安裝目錄。
- **確保相容性：**  
  請確認您的 Liberty 執行環境版本與擴充功能相容。

---

### 3. 在 VS Code 中設定您的 Liberty 伺服器
- **建立新伺服器實例：**  
  開啟命令選擇區（`Ctrl+Shift+P` 或 `Cmd+Shift+P`）並執行指令：  
  `Liberty: Create Server`  
  依照提示：
  - 選擇執行環境安裝資料夾。
  - 指定伺服器設定檔（通常是 `server.xml`）。
- **現有專案：**  
  若您已有基於 Liberty 的應用程式，請開啟工作區以便擴充功能偵測並協助管理伺服器設定。

---

### 4. 新增您的應用程式
- **部署應用程式：**  
  您可以透過以下方式將應用程式新增至伺服器：
  - 編輯 `server.xml` 以包含應用程式的上下文和部署詳細資訊，或
  - 使用擴充功能的 UI 選項（通常在 Liberty 視圖中提供）來「新增應用程式」或「部署應用程式」。
- **建置整合：**  
  若您使用 Maven 或 Gradle，擴充功能也可能提供在部署前建置應用程式的任務。

---

### 5. 啟動、停止和偵錯伺服器
- **啟動伺服器：**  
  在 Liberty 視圖（通常在 VS Code 中以專用面板或樹狀視圖提供）中，右鍵點擊已設定的伺服器並選擇 **「啟動伺服器」**。  
  輸出面板將顯示啟動日誌和任何設定訊息。
- **停止伺服器：**  
  同樣地，右鍵點擊並選擇 **「停止伺服器」** 以關閉您的實例。
- **偵錯：**  
  若需要偵錯您的應用程式：
  - 在程式碼中設定中斷點。
  - 使用命令選擇區執行 **「Liberty: Debug Server」**（或使用 Liberty 視圖中提供的偵錯選項）以將 VS Code 偵錯工具附加到運作中的伺服器。
  - 當您的應用程式處理請求時，中斷點現在應該會被觸發。

---

### 6. 其他功能和提示
- **即時日誌監控：**  
  擴充功能提供即時檢視 Liberty 伺服器日誌的方式，讓問題診斷更加容易。
- **編輯伺服器設定：**  
  在 VS Code 中直接編輯 `server.xml` 時，可享受 IntelliSense 和建議功能。
- **任務整合：**  
  若您在開發工作流程中執行自動化建置或部署，請善用 VS Code 的任務功能。
- **容器和遠端支援：**  
  根據您的設定，您可能還可以將 Liberty 設定為在容器或遠端環境中運行，擴充功能中提供額外指令。

---

### 最後說明
使用 Liberty Tools 擴充功能可簡化在 VS Code 中直接開發、部署和偵錯 WebSphere Liberty 應用程式的流程。此整合有助於減少上下文切換並加速開發週期。

如需任何進階設定或疑難排解步驟，請隨時參考 IBM 關於 Liberty Tools 擴充功能的官方文件。