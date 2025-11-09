---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Eclipse 進行 WebSphere 開發
translated: true
type: note
---

### 在 Eclipse 中使用 IBM WebSphere Application Server (WAS) 進行開發

IBM WebSphere Application Server (WAS) 是一個 Java EE 應用程式伺服器，而 Eclipse 則是開發、組裝及部署應用程式至 WAS 的絕佳 IDE。實現此整合的主要工具是 **IBM WebSphere Application Server Developer Tools for Eclipse**（常簡稱為 WDT）。此外掛程式直接在 Eclipse 內提供伺服器管理、專案建立、部署及偵錯功能。它同時支援傳統的 WAS（例如 v8.5 及 v9.x）與輕量級的 Liberty profile。

#### 必要外掛程式
- **IBM WebSphere Application Server Developer Tools for Eclipse**：這是必要的外掛程式。請選擇與您的 WAS 執行時期版本相符的版本（例如 V8.5x 或 V9.x 工具）。它可以免費從 Eclipse Marketplace 取得，並支援近期的 Eclipse 版本，如 2024-06 或 2025-03。

嚴格來說不需要其他外掛程式，但為了進行完整的 Java EE 開發，請確保您的 Eclipse 安裝包含了 Web Tools Platform (WTP)，這在 Eclipse IDE for Java EE Developers 套件中是標準配備。

#### 必要條件
- Eclipse IDE for Java EE Developers（建議使用 2023-09 或更新版本以確保相容性）。
- 本機已安裝 IBM WAS 執行時期（傳統版或 Liberty）以進行測試與部署。
- 需有網際網路連線以透過 Marketplace 安裝（或下載離線檔案）。

#### 安裝步驟
您可以透過 Eclipse Marketplace（最簡易的方法）、更新站台或下載的檔案來安裝 WDT。安裝後請重新啟動 Eclipse。

1. **透過 Eclipse Marketplace**（推薦）：
   - 開啟 Eclipse 並前往 **Help > Eclipse Marketplace**。
   - 搜尋 "IBM WebSphere Application Server Developer Tools"。
   - 選擇適當的版本（例如 for V9.x 或 V8.5x）。
   - 點擊 **Install** 並遵循提示操作。接受授權協議並在完成時重新啟動 Eclipse。

2. **透過更新站台**：
   - 前往 **Help > Install New Software**。
   - 點擊 **Add** 並輸入更新站台 URL（例如，對於近期版本：`https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` — 請查閱 IBM 文件以取得最新資訊）。
   - 選擇 WDT 功能（例如 WebSphere Application Server V9.x Developer Tools）並安裝。

3. **從下載的檔案安裝**（離線選項）：
   - 從 [IBM Developer 網站](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) 下載 ZIP 封存檔（例如 `wdt-update-site_<version>.zip`）。
   - 解壓縮至本機資料夾。
   - 在 Eclipse 中，前往 **Help > Install New Software > Add > Archive** 並選擇已解壓縮站台中的 `site.xml`。
   - 選擇並安裝所需功能，然後重新啟動。

安裝後，請透過檢查 **Window > Show View > Servers** 來驗證 — WAS 應顯示為可用的伺服器類型選項。

#### 開發和部署 WAS 應用程式的基本步驟
安裝完成後，您就可以建立、建置及執行以 WAS 為目標的 Java EE 應用程式。

1. **建立新專案**：
   - 前往 **File > New > Project**。
   - 選擇 **Web > Dynamic Web Project**（適用於 Web 應用程式）或 **Java EE > Enterprise Application Project**（適用於完整的 EAR）。
   - 在專案精靈中，將目標執行時期設定為您的本機 WAS 安裝（如果清單中沒有，請透過 **Window > Preferences > Server > Runtime Environments > Add > WebSphere** 新增）。
   - 設定與您的 WAS 相符的 Java EE 版本（例如 7 或 8）的 Facet。

2. **設定伺服器**：
   - 開啟 **Servers** 視圖（**Window > Show View > Servers**）。
   - 在視圖中按右鍵並選擇 **New > Server**。
   - 選擇 **WebSphere Application Server**（傳統版或 Liberty）並指向您的本機 WAS 安裝目錄。
   - 完成設定並啟動伺服器（按右鍵 > Start）。

3. **開發您的應用程式**：
   - 在您的專案中加入 Java 類別、JSPs、servlets、EJBs 等。
   - 使用 Eclipse 的編輯器處理 XML 設定檔（例如 web.xml、適用於 WAS 特定綁定的 ibm-web-bnd.xml）。
   - 建置專案（**Project > Build Project**）。

4. **部署與執行**：
   - 在您的專案上按右鍵 > **Run As > Run on Server**（選擇您的 WAS 伺服器）。
   - Eclipse 會發布應用程式（開發模式下為自動發布）並啟動伺服器。
   - 透過設定中斷點並在 Debug 模式下執行來進行偵錯。
   - 為了實現熱部署（無需重新啟動即可快速更新），請在伺服器設定中啟用 "Publish server changes immediately"。

5. **進階提示**：
   - 使用 Liberty profile 進行更快的本機測試 — 它包含在 WDT 中並模擬傳統 WAS 的行為。
   - 對於 OSGi 或微服務，可透過此外掛程式建立 OSGi Bundle Projects。
   - 在執行時期於 **Console** 視圖中監控日誌。

如果您遇到問題（例如相容性錯誤），請查閱 IBM 的已知問題頁面，或確保您的 Eclipse 和 WAS 版本一致。

#### 參考資料
- [IBM WebSphere Application Server Developer Tools 概覽](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace: V9.x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace: V8.5x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [IBM 文件中的安裝指南](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)