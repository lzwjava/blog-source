---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: IBM MQ WebSphere 應用伺服器配置
translated: true
type: note
---

### 先決條件
在配置 IBM WebSphere Application Server (WAS) 中的 IBM MQ（前稱 WebSphere MQ）之前，請確保以下事項：
- IBM MQ 已安裝在專用伺服器上（若為本地綁定模式，可與 WAS 安裝於同一伺服器）。
- 已在 IBM MQ 中建立佇列管理員（例如使用 `crtmqm QMNAME`）。
- 已在佇列管理員中建立所需佇列（例如使用 MQ Explorer 或 `runmqsc`）。
- IBM MQ 用戶端函式庫（JAR 檔案如 `com.ibm.mq.allclient.jar`、`com.ibm.mqjms.jar`）已備妥。若 WAS 與 MQ 位於不同伺服器，請在 WAS 機器上安裝 IBM MQ 用戶端。
- 將 WAS 程序使用者加入 `mqm` 群組以取得權限。
- 在類 Unix 系統上，若非 root 使用者，請使用 `setmqaut` 授予權限。

### 逐步配置說明
此配置涉及在 WAS 管理控制台中設定 JMS 提供者、連線工廠和目的地。此處假設為透過 TCP/IP 的分散式（用戶端）模式連線；若為本地模式請相應調整綁定模式設定。

1. **存取 WAS 管理控制台**：
   - 啟動 WAS 伺服器。
   - 開啟瀏覽器並前往 `https://localhost:9043/ibm/console`（請替換為實際主機/埠號）。
   - 使用管理員憑證登入。

2. **配置 IBM MQ JMS 提供者**：
   - 前往 **Resources > JMS > Providers**。
   - 點擊 **New**。
   - 選擇 **WebSphere MQ messaging provider**。
   - 填寫詳細資訊：
     - **Name**：例如 `MQProvider`。
     - **Description**：選填。
     - **Class path**：MQ JAR 檔案路徑（例如 `/opt/mqm/java/lib/*` 或複製至 `<WAS_HOME>/lib/ext`）。
     - **Native library path**：綁定模式需填寫（MQ 函式庫路徑，例如 `/opt/mqm/lib64`）。
     - **External initial context factory name**：`com.ibm.mq.jms.context.WMQInitialContextFactory`（適用用戶端模式）。
     - **External context provider URL**：例如 `host:1414/CHANNEL`（host = MQ 伺服器 IP，1414 = 預設埠號，CHANNEL = 例如 `SYSTEM.DEF.SVRCONN`）。
   - 儲存配置。

3. **建立佇列連線工廠**：
   - 前往 **Resources > JMS > Queue connection factories**（選擇適用範圍至伺服器或 cell）。
   - 點擊 **New**。
   - 選擇步驟 2 建立的提供者。
   - 填寫：
     - **Name**：例如 `MQQueueCF`。
     - **JNDI name**：例如 `jms/MQQueueCF`。
     - **Queue manager**：您的 MQ 佇列管理員名稱（例如 `QM1`）。
     - **Host**：MQ 伺服器主機名稱或 IP。
     - **Port**：1414（預設值）。
     - **Channel**：例如 `SYSTEM.DEF.SVRCONN`。
     - **Transport type**：`CLIENT`（適用 TCP/IP）或 `BINDINGS`（本地模式）。
     - **Security credentials**：如需認證請填寫使用者 ID 與密碼。
   - 進階屬性選項：設定連線池大小（例如根據負載調整最大連線數）。
   - 儲存。

4. **建立佇列目的地**：
   - 前往 **Resources > JMS > Queues**。
   - 點擊 **New**。
   - 選擇提供者。
   - 為每個佇列設定：
     - **Name**：例如 `MyQueue`。
     - **JNDI name**：例如 `jms/MyQueue`。
     - **Queue name**：MQ 中的確切佇列名稱（例如 `MY.LOCAL.QUEUE`）。
     - **Queue manager**：同上步驟。
     - **Target client type**：`MQ` 或 `JMS`。
   - 儲存。若使用發佈/訂閱模式請重複建立主題。

5. **（可選）配置 WebSphere MQ 伺服器綁定模式**：
   - 若使用本地綁定，請前往 **Servers > Server Types > WebSphere MQ servers**。
   - 點擊 **New**。
   - 設定 **Name**、**Queue manager name**。
   - 指定 **MQ installations**（MQ 安裝路徑）。
   - 儲存並重啟伺服器。

6. **配置 JCA 資源配接器（適用 MDB）**：
   - 前往 **Resources > Resource Adapters > J2C connection factories**。
   - 若使用內建 MQ RA，請確認已部署（WAS 包含 `wmq.jmsra.rar`）。
   - 設定屬性如最大連線數（例如根據負載設定 10-50）。

7. **測試配置**：
   - 部署範例 JMS 應用程式或使用 WAS JMS 範例。
   - 檢查日誌是否有錯誤（例如埠號 1414 連線被拒）。
   - 在 MQ 中驗證：使用 MQ Explorer 監控佇列深度與通道狀態。

8. **安全性與進階設定**：
   - 啟用 SSL：在 WAS 與 MQ 中配置金鑰庫（通道需設定 `SSLCIPH`）。
   - 設定認證：使用 MQ 使用者群組或替代使用者 ID。
   - 對於叢集環境：同步所有節點的配置。

### 疑難排解提示
- **ClassNotFoundException**：確認 MQ JAR 檔案位於 classpath 中。
- **連線失敗**：檢查埠號 1414 的防火牆設定、通道狀態（在 runmqsc 中使用 `DISPLAY CHSTATUS(*)`）。
- **綁定模式問題**：確認原生函式庫及使用者是否在 `mqm` 群組中。
- 變更配置後請重啟 WAS。

如需版本特定詳細資訊（例如 WAS 9.x 與 MQ 9.x），請參閱官方 IBM 文件。

[Using WebSphere Application Server with IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuring WebSphere Application Server for use with IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Creating a WebSphere MQ server definition](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)