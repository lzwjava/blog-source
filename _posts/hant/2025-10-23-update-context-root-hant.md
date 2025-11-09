---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 更新 WebSphere 上下文根
translated: true
type: note
---

### 在 IBM WebSphere Application Server (WAS) 中更新 Web 上下文根目錄

Web 上下文根目錄定義了 Web 應用程式的基礎 URL 路徑（例如 `/myapp`）。在 IBM WebSphere Application Server 中，您可以透過管理控制台在初始部署時或為現有應用程式更新此設定。以下是針對現有應用程式的步驟。請確保您擁有 WAS 控制台的管理員存取權限。

#### 先決條件
- 擁有 WebSphere 管理控制台的存取權限（通常位於 `https://your-server:9043/ibm/console`）。
- 應用程式必須已安裝並在進行變更前停止（建議），以避免衝突。

#### 更新上下文根目錄的步驟
1. **登入管理控制台**：
   - 開啟網頁瀏覽器並導航至 WAS 控制台 URL。
   - 輸入您的管理員憑證。

2. **導航至應用程式**：
   - 在左側導航窗格中，展開 **Applications** > **Application Types** > **WebSphere enterprise applications**。
   - 從清單中找出並選擇您已部署的應用程式。

3. **存取上下文根目錄設定**：
   - 在應用程式詳細資料頁面上，向下滾動至 **Web Module Properties** 部分。
   - 點擊 **Context root for web modules**。

4. **編輯上下文根目錄**：
   - 在出現的表格中，找到 Web 模組（例如您的 WAR 檔案名稱）。
   - 在 **Context root** 欄位中更新新值（例如從 `/oldapp` 更改為 `/newapp`）。若非必要，請避免使用開頭斜線，但對於像 `/myapp` 這樣的路徑，請包含斜線。
   - 點擊 **OK** 儲存變更。

5. **儲存並同步配置**：
   - 在控制台中點擊 **Save**（或如果提示，則點擊 **Save directly to the master configuration**）。
   - 如果在叢集或網路部署環境中：
     - 前往 **System administration** > **Nodes**。
     - 選擇所有相關節點並點擊 **Full Resynchronize**。

6. **重新啟動應用程式**：
   - 返回 **Applications** > **WebSphere enterprise applications**。
   - 選擇您的應用程式並點擊 **Stop**，然後點擊 **Start**。
   - 或者，透過 **Servers** > **Server Types** > **WebSphere application servers** > 選擇伺服器 > **Restart** 來重新啟動整個伺服器。

7. **驗證變更**：
   - 在瀏覽器中存取應用程式 URL（例如 `http://your-server:9080/newapp`）。
   - 檢查伺服器日誌（例如 `SystemOut.log`）是否有任何與部署相關的錯誤。

#### 補充說明
- **在初始部署期間**：如果部署新應用程式，請在 **Select installation options** 步驟中，為每個 Web 模組在 **Context root** 下指定上下文根目錄。
- **EAR 檔案**：對於打包在 EAR 中的應用程式，請確保 `application.xml` 未硬編碼上下文根目錄；控制台中的覆蓋設定將優先。
- **常見問題**：
  - 如果應用程式正在運行，變更可能無法應用——請務必先停止應用程式。
  - 在 WebSphere Liberty 或 Open Liberty 中，請改用 `server.xml` 配置。
  - 對於虛擬主機或插件，請在變更後更新 Web 伺服器插件配置。
- 如果應用程式使用安全性或共享庫，請在更新後進行全面測試。

更多詳細資訊，請參閱官方 IBM 文件或社群指南。

#### 參考資料
- [Context root for web modules settings](https://www.ibm.com/docs/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/uweb_contextroot.html)
- [IBM WebSphere - Context root of an application](https://www.freekb.net/Article?id=1647)
- [WebSphere 8.5 context root change not applying to WAR file](https://stackoverflow.com/questions/24472790/websphere-8-5-context-root-change-not-applying-to-war-file)