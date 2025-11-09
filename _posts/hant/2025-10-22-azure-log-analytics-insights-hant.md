---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Azure Log Analytics 與 Azure Insights
translated: true
type: note
---

好問題——它們**密切相關**，但**並不相同**。讓我們來清楚解析一下。

---

### **1. Azure Log Analytics**

**Azure Log Analytics** 是 **Azure Monitor** 內的一個**工具/服務**，讓你能夠**收集、查詢及分析**來自雲端和本地資源的日誌。

* 它將日誌儲存在 **Log Analytics 工作區**中。
* 你可以使用 **Kusto 查詢語言 (KQL)** 執行查詢來分析數據。
* 它用於：

  * 疑難排解問題
  * 調查效能
  * 監控安全性
  * 建立自訂儀表板和警示

你可以將 Log Analytics 視為 Azure 中所有日誌數據的**數據湖和查詢引擎**。

---

### **2. Azure Insights**

**Azure Insights**（常以 **Application Insights** 或 **Azure Monitor Insights** 的形式出現）屬於同一監控生態系統，但更側重於**應用程式層面的監控**，而非原始日誌。

「Insights」有以下不同類型：

* **Application Insights** — 監控應用程式（APM）：效能、異常、依賴項、用戶行為等。
* **VM Insights**、**Container Insights**、**Network Insights** — 為特定資源類型提供預建的監控視圖。

所有這些 Insights **都將其遙測數據和指標儲存在 Log Analytics 工作區中**，因此它們**底層依賴於 Log Analytics**。

---

### **3. 關係**

* **Azure Insights = 視覺化和智能監控層**
* **Log Analytics = 底層的日誌儲存和查詢引擎**

簡而言之：

> Log Analytics 是數據*存放*和分析的地方。
> Insights 是你*查看*和*解讀*這些數據以用於特定資源類型的方式。

---

### **範例**

如果你在一個網頁應用程式上啟用 **Application Insights**：

* 它會收集遙測數據（請求、依賴項、追蹤、異常）。
* 這些數據儲存在 **Log Analytics 工作區**中。
* 你可以使用 **Log Analytics** 對同一數據執行 KQL 查詢，進行更深度的自訂分析。

---

需要我展示一個簡單的 **KQL 範例**，說明 Log Analytics 如何查詢 Application Insights 的數據嗎？