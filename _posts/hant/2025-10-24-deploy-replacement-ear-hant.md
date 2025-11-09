---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 WebSphere 中部署替換 EAR
translated: true
type: note
---

### 在 IBM WebSphere Application Server (WAS) 中部署新 EAR 檔案以替換現有檔案

在 IBM WAS 中替換 EAR（企業歸檔）檔案是一項標準部署任務，但必須遵循最佳實踐以避免停機時間、配置不匹配或運行時錯誤。以下將概述在上傳/部署過程之前、期間和之後需要確認及驗證的關鍵細節。假設您正在使用 WAS 管理控制台（或用於自動化的 wsadmin 腳本），並且在受支援的環境中操作（例如 WAS 8.5、9.x 或 Liberty 設定檔）。

#### 1. **部署前準備（上傳前確認事項）**
   - **備份當前應用程式**：
     - 從控制台導出現有 EAR（應用程式 > 企業應用程式 > [應用程式名稱] > 導出），或透過 wsadmin 使用 `backupConfig` 指令備份整個配置。
     - 原因？若新 EAR 導致問題時可進行回退。請確認備份已完成並安全儲存。

   - **相容性檢查**：
     - 確認新 EAR 是針對正確的 WAS 版本構建（例如 Java 版本、EJB 規範如 Jakarta EE 與 Java EE）。
     - 檢查您的 WAS 版本中是否有任何已棄用的功能（例如透過 IBM Knowledge Center 文檔）。如果可能，請使用 `wsadmin` 執行 `AdminConfig.validateAppDeployment`。
     - 確認 EAR 的部署描述符（application.xml、ibm-application-ext.xmi）與伺服器的模組（EAR 內的 WAR、JAR）匹配。

   - **環境與資源依賴性**：
     - 檢視 JNDI 資源：資料來源、JMS 佇列、環境變數。確保任何引用的資源（例如 JDBC 提供者）已配置且正常運作。透過控制台測試連線（資源 > JDBC > 資料來源）。
     - 安全性：確認使用者角色、安全性限制和映射（例如在 ibm-application-bnd.xmi 中）與您的領域（例如 LDAP、聯合）一致。檢查新 EAR 是否需要新的自定義領域或憑證。
     - 類別載入器策略：注意當前的 WAR 類別載入器模式（PARENT_FIRST 或 PARENT_LAST）和共享庫引用——確保與新 EAR 沒有衝突。
     - 叢集/高可用性：若在叢集環境中，確認新 EAR 在所有節點上一致，並計劃滾動部署以最小化停機時間。

   - **應用程式特定細節**：
     - 上下文根與虛擬主機：確認上下文根不與其他應用程式衝突（應用程式 > [應用程式名稱] > Web 模組的上下文根）。
     - 端口與映射：驗證 servlet 映射和任何 URL 模式。
     - 自定義屬性：檢查控制台中設定的應用程式特定自定義屬性——這些可能在部署後需要重新應用。

   - **測試新 EAR**：
     - 首先在預備/開發環境中構建並測試 EAR。使用 Rational Application Developer 或帶有 WAS 外掛的 Eclipse 等工具進行驗證。
     - 掃描已知問題：使用 IBM 的 Fix Packs 和 APARs 搜尋功能檢查您的 WAS 版本。

#### 2. **上傳與部署期間**
   - **停止當前應用程式**：
     - 在控制台中：應用程式 > 企業應用程式 > [應用程式名稱] > 停止。確認其已完全停止（若啟用工作階段親和性，則無活動工作階段）。
     - 在叢集設定中儲存配置並同步節點（系統管理 > 節點 > 同步）。

   - **上傳新 EAR**：
     - 導航至應用程式 > 新應用程式 > 新企業應用程式。
     - 上傳 EAR 檔案。在精靈過程中：
       - 如果提示，選擇「替換現有應用程式」（或先透過應用程式 > [應用程式名稱] > 卸載來解除安裝舊版）。
       - 檢視部署選項：將模組映射到伺服器、目標叢集和共享庫。
       - 在精靈中逐步確認：安全性角色綁定、資源引用和元數據完整性。
     - 如果使用 wsadmin：使用 `AdminApp.update` 或 `installInteractive` 進行替換的腳本。範例：
       ```
       wsadmin> AdminApp.update('AppName', '[-operation update -contenturi /path/to/new.ear]')
       ```
       在應用前始終使用 `AdminConfig.validateAppDeployment` 進行驗證。

   - **配置同步**：
     - 上傳後，儲存主配置並同步至部署管理器/節點。
     - 檢查部署摘要中的警告/錯誤——立即處理任何模組綁定問題。

   - **啟動應用程式**：
     - 透過控制台啟動，並確認其初始化無錯誤（監控設定檔日誌目錄中的 SystemOut.log 和 SystemErr.log）。

#### 3. **部署後驗證**
   - **日誌與監控**：
     - 追蹤日誌（例如 `tail -f profile/logs/server1/SystemOut.log`）以確認部署成功、綁定錯誤或啟動異常。
     - 如有需要，使用控制台的故障排除 > 日誌與追蹤進行詳細追蹤。確認無 ClassNotFoundException 或 NoSuchMethodError。

   - **功能測試**：
     - 冒煙測試：透過 URL 存取應用程式並驗證核心功能（例如登入、API 呼叫）。
     - 若為關鍵應用，進行負載測試——檢查記憶體洩漏或性能回歸。
     - 資料庫/外部整合：執行查詢或呼叫以確認資料流。

   - **回退計劃**：
     - 確認您可以快速重新部署已備份的 EAR。設定健康檢查（例如透過 IBM Health Center 或自定義腳本）。

#### 常見陷阱注意事項
- **工作階段管理**：如果應用程式使用 HTTPSession，在停止前清空活動工作階段以避免資料遺失。
- **檔案權限**：確保 EAR 檔案對 WAS 使用者（例如 wasadmin）具有讀取權限。
- **大小與時間**：大型 EAR 部署可能耗時——請在維護窗口內計劃。
- **Liberty 設定檔差異**：如果使用 WAS Liberty，部署是透過 server.xml 編輯或 `install-feature` 進行；確認 XML 配置匹配。
- **版本特定注意事項**：對於 WAS 9+，檢查 microProfile 或 CDI 變更。始終參考 IBM 文檔以獲取確切版本資訊。

如果您提供更多細節（例如 WAS 版本、叢集設定或遇到的特定錯誤），我可以進一步完善建議。官方指南請查閱 IBM Knowledge Center 或支援入口網站。如有其他需要協助之處，請告知！