---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 WebSphere 中的 IBM MQ
translated: true
type: note
---

### 在 IBM WebSphere Application Server 中配置訊息佇列（使用 IBM MQ 作為提供者）

IBM WebSphere Application Server (WAS) 透過 Java Message Service (JMS) 與 IBM MQ（前身為 WebSphere MQ）整合來支援訊息佇列。配置通常透過 **WebSphere Integrated Solutions Console**（管理介面）進行，可於 `https://your-server:9043/ibm/console` 存取（預設安全端口；請根據需要調整）。本指南專注於傳統完整配置檔的 WAS（例如版本 9.0+），但步驟與 WebSphere Liberty 類似，僅需微調。

#### 先決條件
- IBM MQ 必須已安裝、運行且可存取（例如佇列管理器已啟動）。
- WAS 伺服器已啟動，且您擁有管理員權限存取控制台。
- 如果尚未存在，請下載並安裝 IBM MQ JMS 客戶端函式庫（例如 `com.ibm.mq.allclient.jar`）到 WAS 的共享函式庫中（位於 **Environment > Shared Libraries**）。
- 確保 WebSphere MQ 訊息提供者已配置（位於 **Resources > JMS > JMS providers**）。如果沒有，請建立一個，並填寫詳細資訊如主機、端口（預設 1414）和佇列管理器名稱。

配置完成後，儲存變更（頂部的 **Save** 按鈕）並重新啟動應用程式伺服器以使變更生效。

#### 步驟 1：建立 JMS 佇列連線工廠
連線工廠用於建立與 IBM MQ 佇列管理器的連線。

1. 登入 WAS 管理控制台。
2. 在導覽窗格中，展開 **Resources > JMS > Queue connection factories**。
3. 從下拉選單中選擇適當的 **Scope**（例如 Cell、Node、Server）並點擊 **Apply**。
4. 點擊 **New**。
5. 選擇 **WebSphere MQ messaging provider** 並點擊 **OK**。
6. 在下一個畫面中：
   - **Name**：輸入描述性名稱（例如 `MyMQQueueConnectionFactory`）。
   - **JNDI name**：輸入 JNDI 綁定（例如 `jms/MyQueueConnectionFactory`）。
   - 點擊 **Next**。
7. 輸入連線詳細資訊：
   - **Queue manager**：您的 IBM MQ 佇列管理器名稱（例如 `QM1`）。
   - **Host name**：IBM MQ 伺服器主機名稱或 IP。
   - **Port**：監聽端口（預設：1414）。
   - **Transport type**：CHANNEL（用於客戶端模式）或 BINDINGS（用於嵌入式模式）。
   - **Channel**：預設通道名稱（例如 `SYSTEM.DEF.SVRCONN`）。
   - **User ID** 和 **Password**：用於 MQ 認證的憑證（如果需要）。
   - 點擊 **Next**。
8. 檢視摘要並點擊 **Finish**。
9. 選擇新建的工廠，前往 **Additional Properties > Connection pool**（可選），並調整設定如 **Maximum connections**（例如根據預期負載）。
10. 點擊 **Test connection** 進行驗證。

#### 步驟 2：建立 JMS 佇列目的地
這定義了用於發送/接收訊息的實際佇列端點。

1. 在導覽窗格中，展開 **Resources > JMS > Queues**。
2. 選擇適當的 **Scope**（與連線工廠匹配）並點擊 **Apply**。
3. 點擊 **New**。
4. 選擇 **WebSphere MQ messaging provider** 並點擊 **OK**。
5. 指定屬性：
   - **Name**：描述性名稱（例如 `MyRequestQueue`）。
   - **JNDI name**：JNDI 綁定（例如 `jms/MyRequestQueue`）。
   - **Base queue name**：IBM MQ 中的確切佇列名稱（例如 `REQUEST.QUEUE`；必須在 MQ 中存在或建立）。
   - **Target client**：JMS（用於 JMS 應用程式）或 MQ（用於原生 MQ 應用程式）。
   - **Target destination mode**：Once only（預設用於可靠性）。
   - 點擊 **OK**。
6. （可選）在 **Additional Properties** 下，配置持久性、過期或優先級設定。
7. 儲存配置。

#### 步驟 3：（可選）為 Message-Driven Beans (MDBs) 建立啟動規格
如果使用 MDBs 非同步消費訊息：

1. 在導覽窗格中，展開 **Resources > JMS > Activation specifications**。
2. 選擇 **Scope** 並點擊 **New**。
3. 選擇 **WebSphere MQ messaging provider** 並點擊 **OK**。
4. 輸入：
   - **Name**：例如 `MyQueueActivationSpec`。
   - **JNDI name**：例如 `jms/MyQueueActivation`。
   - **Destination type**：Queue。
   - **Destination JNDI name**：您的佇列 JNDI（例如 `jms/MyRequestQueue`）。
   - **Connection factory JNDI name**：您的連線工廠 JNDI（例如 `jms/MyQueueConnectionFactory`）。
   - Message selector（可選）：用於過濾訊息的 JMS 選擇器。
5. 在 **Additional Properties > Message Listener Service > Listener Ports** 下，如果需要，建立一個端口：
   - **Name**：例如 `MyListenerPort`。
   - **Connection factory JNDI**：如上所述。
   - **Destination JNDI**：如上所述。
   - **Component**：您的 MDB 部署描述符。
6. 點擊 **OK** 並儲存。

#### 步驟 4：驗證與測試
- **在控制台中測試**：使用工廠和規格上的 **Test connection**。
- **部署應用程式**：建立一個簡單的 JMS 客戶端或 MDB 應用程式，部署它，並透過 IBM MQ 工具（例如 MQ Explorer）發送/測試訊息。
- **監控**：在 **Monitoring and Tuning > Performance Viewer** 或 **Troubleshooting > Logs** 下，檢查 JMS 相關錯誤。
- 常見問題：
  - 連線失敗：驗證防火牆、MQ 通道狀態（`DISPLAY CHANNEL`）和憑證。
  - JNDI 查找錯誤：確保綁定正確且應用程式使用正確的範圍。
  - 持久性：在 WAS 和 MQ 之間對齊持久性設定。

如需命令列替代方案（wsadmin 腳本），請參考 IBM 文檔。根據您的版本進行調整（例如 WAS 9.0.5+ 支援 JMS 2.0）。

#### 參考資料
- [在 WebSphere Application Server 中配置 JMS 資源](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [WebSphere MQ 訊息提供者佇列設定](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [建立 WebSphere MQ 訊息提供者佇列連線工廠](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [為 WebSphere MQ 配置 JMS 佇列目的地](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)