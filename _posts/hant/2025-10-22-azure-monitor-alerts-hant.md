---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure Monitor 警示概覽
translated: true
type: note
---

### Azure 警示功能概覽

Azure Monitor 警示是 Azure Monitor 的一項功能，當您的 Azure 資源滿足特定條件時會主動發出通知，協助您在問題影響用戶前偵測並解決問題。其運作原理是根據預先定義的規則，評估來自計量、日誌或活動日誌的資料。當條件觸發時（例如 CPU 使用率超過 80%），警示就會觸發，並可透過電子郵件、SMS 發送通知，或觸發自動化操作（如執行指令碼）。

根據您的配置，警示可以是具狀態的（問題解決後自動解除）或無狀態的（會持續觸發直到手動關閉）。它們支援單一或多個資源的監控，並根據監控的時間序列數量進行計費。

#### 警示類型
Azure Monitor 支援多種針對不同資料來源設計的警示類型：

| 警示類型              | 描述 | 最適用於 |
|-------------------------|-------------|----------|
| **計量警示**      | 定期評估數值計量（例如 CPU 百分比、磁碟空間）。支援靜態或動態閾值（基於 AI）。 | 虛擬機器、資料庫或應用程式的效能監控。 |
| **日誌搜尋警示**  | 對 Log Analytics 資料執行查詢以偵測日誌中的模式。 | 複雜事件分析，例如應用程式日誌中的錯誤激增。 |
| **活動日誌警示**| 在管理或操作事件（例如資源建立/刪除）時觸發。 | 安全性和合規性審計。 |
| **智慧偵測警示** | 透過 Application Insights 對 Web 應用程式進行 AI 驅動的異常偵測。 | 應用程式中的自動問題發現。 |
| **Prometheus 警示**  | 在受控服務（如 AKS）中查詢 Prometheus 計量。 | 容器和 Kubernetes 環境。 |

對於大多數使用情境，建議從計量警示或日誌警示開始。

### 必要條件
- 一個包含有效監控資源的 Azure 訂閱。
- 權限：目標資源的讀者角色、警示規則資源群組的參與者權限，以及任何行動群組的讀者權限。
- 熟悉 Azure 入口網站 (portal.azure.com)。

### 如何建立和使用計量警示規則（逐步指南）
計量警示是常見的起點。以下說明如何在 Azure 入口網站中建立一個計量警示。此過程大約需要 5-10 分鐘。

1. **登入 Azure 入口網站**：前往 [portal.azure.com](https://portal.azure.com) 並登入。

2. **導航至警示**：
   - 從首頁搜尋並選取 **Monitor**。
   - 在左側選單中，於 **Insights** 下選取 **Alerts**。
   - 點擊 **+ Create** > **Alert rule**。

   *替代方式*：從特定資源（例如虛擬機器）的左側選單中選取 **Alerts**，然後點擊 **+ Create** > **Alert rule**。這會自動設定範圍。

3. **設定範圍**：
   - 在 **Select a resource** 窗格中，選擇您的訂閱、資源類型（例如 Virtual machines）和特定資源。
   - 點擊 **Apply**。（對於多資源警示，請在單一區域中選取多個相同類型的資源。）

4. **設定條件**：
   - 在 **Condition** 標籤頁上，點擊 **Signal name** 並選擇一個計量（例如虛擬機器的 "Percentage CPU"）。
     - 使用 **See all signals** 來按類型篩選（例如 Platform metrics）。
   - 預覽資料：設定時間範圍（例如過去 24 小時）以查看歷史值。
   - 設定 **Alert logic**：
     - **Threshold**：靜態（例如 > 80）或動態（基於歷史記錄由 AI 調整）。
     - **Operator**：大於、小於等。
     - **Aggregation**：評估期間內的平均值、總和、最小值、最大值。
     - 對於動態閾值：選擇敏感度（低/中/高）。
   - （可選）**Split by dimensions**：按屬性（例如執行個體名稱）篩選，以實現細粒度警示（例如一組虛擬機器中的每個虛擬機器）。
   - **Evaluation**：每 1-5 分鐘檢查一次；回顧 5-15 分鐘。
   - 點擊 **Done**。

5. **新增動作（可選但建議）**：
   - 在 **Actions** 標籤頁上，選取 **Add action groups**。
   - 選擇現有的群組（用於電子郵件/SMS）或建立一個：
     - 新增收件人（例如管理員電子郵件）。
     - 新增動作，例如用於自動化的 Logic Apps 或用於整合的 webhooks。
   - 點擊 **Done**。

6. **設定規則詳細資料**：
   - 在 **Details** 標籤頁上：
     - **Subscription** 和 **Resource group**：自動填充；如有需要可變更。
     - **Severity**：Sev 0（嚴重）到 Sev 4（詳細資訊）。
     - **Alert rule name**：例如 "High CPU Alert - Prod VM"。
     - **Description**：可選的備註。
   - **Advanced options**：
     - 建立時啟用規則。
     - 自動解除警示（使其成為具狀態）。
   - 如有需要，可新增標籤以便組織。

7. **檢閱並建立**：
   - 前往 **Review + create**。
   - 驗證（修正任何錯誤，例如無效的閾值）。
   - 點擊 **Create**。如果已啟用，規則會立即生效。

建立後，當條件滿足時，警示將會觸發，發送通知並更新其狀態（例如從 "Fired" 變為 "Resolved"）。

#### 管理警示
- **檢視警示**：在 Monitor > Alerts 中，查看作用中/已觸發的警示。按時間、嚴重性或資源篩選。
- **編輯規則**：前往 Monitor > Alerts > Alert rules，選取規則，然後點擊 **Edit**。
- **測試**：使用步驟 4 中的預覽功能進行模擬。
- **擴展**：對於多個資源，使用 Azure CLI/PowerShell 或 ARM 範本。透過資源 insights 啟用內建推薦規則。

### 最佳實踐
- 從簡單開始：初始時每個規則一個條件。
- 對雜訊較多的計量使用動態閾值以減少誤報。
- 與行動群組整合以實現自動補救（例如擴展虛擬機器）。
- 監控成本：基於監控的序列（基本使用免費；請查看定價）。
- 對於日誌，遵循類似步驟，但在建立時選擇 **Log alerts** 並編寫 KQL 查詢。

對於日誌警示或其他類型，過程是類似的——將條件替換為查詢即可。

[Azure Monitor 警示概覽](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)  
[建立計量警示規則](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule)  
[建立日誌警示規則](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-log-alert-rule)  
[Azure Monitor 定價](https://azure.microsoft.com/en-us/pricing/details/monitor/)