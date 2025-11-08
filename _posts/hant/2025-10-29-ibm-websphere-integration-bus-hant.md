---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: IBM WebSphere 服務整合匯流排
translated: true
type: note
---

### IBM WebSphere Application Server 中的服務整合匯流排

在 IBM WebSphere Application Server (WAS) 情境中，「整合匯流排」通常指的是 **服務整合匯流排 (SIB 或 SIBus)**，這是 WAS 內建的訊息傳遞基礎架構。它能實現應用程式之間可靠的非同步通訊，特別適用於採用訊息導向架構或服務導向架構 (SOA) 的應用場景。

#### 用途
SIB 在 WAS 環境中扮演虛擬訊息骨幹的角色。它讓運行於不同伺服器或叢集上的應用程式無需建立直接點對點連接即可交換訊息，從而實現鬆散耦合、可擴展性與容錯能力。主要應用場景包括：
- 支援 Java Message Service (JMS) 的佇列與發佈/訂閱模式
- 在 SOA 架構中整合企業服務
- 於分散式系統中處理訊息路由、轉換與持久化

與 IBM Integration Bus（前身為 WebSphere Message Broker）這類獨立企業服務匯流排 (ESB) 不同，SIB 原生嵌入於 WAS 中，無需單獨安裝——僅需透過配置即可啟用。

#### 核心元件與架構
- **匯流排成員**：指加入匯流排的 WAS Cell 中的應用程式伺服器或伺服器叢集，每個成員承載部分訊息傳遞基礎架構
- **訊息引擎**：負責處理訊息的核心運行時元件。每個 ME 運行於 WAS 流程中（例如在匯流排成員上），負責傳送、接收與儲存訊息。ME 會動態連結形成中介網絡以實現高可用性
- **SIB 服務**：每個 WAS 應用程式伺服器上的預設服務，預設為停用狀態。啟用後將激活訊息傳遞功能
- **目的地**：可透過 WAS 管理控制台配置的佇列或主題，用於發佈或消費訊息
- **資料儲存庫**：為實現持久化，ME 使用檔案型儲存（單一伺服器用本地儲存，叢集用共享檔案系統）或資料庫來確保訊息耐久性

此架構以 Cell 為基礎：在 WAS Network Deployment 設定中，多個匯流排成員跨節點協作，使用 SOAP/HTTP 或 JMS 等協議實現互通性。

#### 設定與使用方式
1. **建立匯流排**：透過 WAS Integrated Solutions Console（管理控制台），導覽至*服務整合 > 匯流排 > 新增*。定義匯流排名稱、新增成員（伺服器/叢集）並配置 ME（例如高可用性策略）
2. **配置**：啟用 SIB JMS 提供者，建立目的地（佇列/主題），並將其映射至 JNDI 名稱供應用程式存取
3. **使用**：應用程式部署訊息驅動 Bean (MDB) 或使用 JMS API 與匯流排互動。例如傳送方應用程式將訊息置於佇列後，匯流排會將其路由至其他成員上的接收方

SIB 支援 JMS 1.1/2.0 等標準，並可透過 WebSphere MQ 橋接器與外部系統整合。在生產環境中，建議進行效能調校，例如使用共享資料儲存庫實現容錯移轉。

**注意**：若您所指為 *IBM Integration Bus* (IIB)，這是針對更廣泛 ESB 需求的獨立產品，雖可連接 WAS/SIB 但並非「內建」於 WAS 中。

[服務整合匯流排 - IBM 文檔](https://www.ibm.com/docs/en/was/9.0.5?topic=integration-service-buses)  
[服務整合匯流排訊息提供者 - IBM 文檔](https://www.ibm.com/docs/en/was-liberty/nd?topic=providers-service-integration-bus-messaging-provider)  
[服務整合匯流排入門指南](https://www.freekb.net/Article?id=1975)