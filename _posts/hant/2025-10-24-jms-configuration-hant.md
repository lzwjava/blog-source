---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 WebSphere 中配置 JMS 資源
translated: true
type: note
---

### 前置準備
- 確保您擁有 IBM WebSphere Application Server (WAS) 整合解決方案主控台 (admin console) 的管理員存取權限。
- 伺服器應處於運行狀態，且您需要決定資源的範圍（例如：cell、node、server）。
- 本指南重點在於預設傳訊供應商（使用服務整合匯流排或 SIBus），這是 WAS 內建的 JMS 供應商。若使用 WebSphere MQ，則需額外配置 MQ 供應商設定。
- 若系統提示，請在進行重大變更後重新啟動伺服器。

### 步驟 1：建立服務整合匯流排
服務整合匯流排是 JMS 資源的傳訊骨幹。

1. 登入 WebSphere 整合解決方案主控台。
2. 前往 **服務整合 > 匯流排**。
3. 點擊 **新增**。
4. 輸入唯一的匯流排名稱（例如：`MyJMSBus`）。
5. 除非需要，否則請取消勾選 **匯流排安全性** 選項。
6. 點擊 **下一步**，然後點擊 **完成** 以建立匯流排。

### 步驟 2：將伺服器新增為匯流排成員
這使伺服器能夠在匯流排上託管傳訊引擎。

1. 選擇您建立的匯流排（例如：`MyJMSBus`）。
2. 在 **其他屬性** 下，點擊 **匯流排成員**。
3. 點擊 **新增**。
4. 在 **新增匯流排成員** 精靈中：
   - 選擇 **傳訊引擎** 作為匯流排成員類型。
   - 從清單中選擇您的伺服器（例如：`server1`）。
   - 對於訊息儲存庫，選擇 **檔案儲存庫**（非叢集環境的預設選項）或 **資料儲存庫**（用於資料庫持久化），並根據需要配置屬性。
5. 點擊 **下一步**，然後點擊 **完成**。
6. 重新啟動 WebSphere Application Server 以啟用匯流排成員。

### 步驟 3：建立 JMS 連線工廠
需要連線工廠才能將 JMS 用戶端連接到供應商。

1. 前往 **資源 > JMS > 連線工廠**。
2. 選擇適當的範圍（例如：`server1` 的伺服器範圍）並點擊 **新增**。
3. 選擇 **預設傳訊供應商** 並點擊 **確定**。
4. 輸入詳細資訊：
   - **名稱**：例如 `MyJMSConnectionFactory`。
   - **JNDI 名稱**：例如 `jms/MyConnectionFactory`。
   - **匯流排名稱**：從下拉選單中選擇 `MyJMSBus`。
   - 保留其他預設值（例如：供應商端點設為自動偵測）。
5. 點擊 **套用**，然後 **儲存** 至主配置。

### 步驟 4：建立 JMS 佇列
這定義了點對點傳訊的佇列目的地。

1. 前往 **資源 > JMS > 佇列**。
2. 選擇適當的範圍並點擊 **新增**。
3. 選擇 **預設傳訊供應商** 並點擊 **確定**。
4. 輸入詳細資訊：
   - **名稱**：例如 `MyJMSQueue`。
   - **JNDI 名稱**：例如 `jms/MyQueue`。
   - **匯流排名稱**：選擇 `MyJMSBus`。
   - **佇列名稱**：選擇 **建立服務整合匯流排目的地**，輸入唯一識別碼（例如：`MyQueueDestination`），並選擇先前建立的匯流排成員。
   - **基礎佇列名稱**：例如 `$MyJMSBus:MyQueueDestination`（自動生成）。
5. 根據需要配置其他屬性（例如：傳遞模式、到期設定）。
6. 點擊 **套用**，然後 **儲存** 至主配置。

### 步驟 5：（可選）為訊息驅動 Bean (MDB) 建立啟動規格
若使用 MDB 從佇列消費訊息，請配置啟動規格。

1. 前往 **資源 > JMS > 啟動規格**。
2. 選擇適當的範圍並點擊 **新增**。
3. 選擇 **預設傳訊供應商** 並點擊 **確定**。
4. 輸入詳細資訊：
   - **名稱**：例如 `MyActivationSpec`。
   - **JNDI 名稱**：例如 `jms/activation/MyActivationSpec`。
   - **匯流排名稱**：選擇 `MyJMSBus`。
   - **目的地類型**：佇列。
   - **目的地**：輸入佇列的 JNDI 名稱（例如：`jms/MyQueue`）。
5. 點擊 **套用**，然後 **儲存** 至主配置。

### 驗證與測試
- 儲存後，若處於叢集環境中，請同步節點。
- 重新啟動伺服器。
- 使用 JMS 用戶端應用程式，透過 JNDI 名稱測試傳送/接收訊息。
- 透過 **服務整合 > 匯流排 > [您的匯流排] > 匯流排成員 > [您的成員] > 傳訊引擎** 進行監控。

如需進階配置（例如：安全性、叢集），請參閱 IBM 文件。

[為 Decision Server 配置 IBM WebSphere Application Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[使用預設傳訊供應商管理傳訊](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)