---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 建立可擴展應用程式於 Azure
translated: true
---

*本篇部落格文章是由 ChatGPT-4o 協助撰寫。*

---

### 目錄
- [簡介](#簡介)
- [開始使用 Azure 訂閱](#開始使用-azure-訂閱)
- [使用 Azure Kubernetes Service (AKS) 部署應用程式](#使用-azure-kubernetes-service-aks-部署應用程式)
  - [建立和管理 AKS 集群](#建立和管理-aks-集群)
  - [部署應用程式](#部署應用程式)
- [從 Pod 提取日誌](#從-pod-提取日誌)
- [使用 Azure Application Insights 進行監控和診斷](#使用-azure-application-insights-進行監控和診斷)
- [使用 Azure 虛擬機器 (VMs)](#使用-azure-虛擬機器-vms)
- [使用 Azure Event Hubs 進行即時數據攝取](#使用-azure-event-hubs-進行即時數據攝取)
- [使用 Azure API Management Services 管理 API](#使用-azure-api-management-services-管理-api)
- [使用 Azure SQL 資料庫](#使用-azure-sql-資料庫)
- [使用 Kusto 查詢語言 (KQL) 查詢日誌](#使用-kusto-查詢語言-kql-查詢日誌)
- [設定警示以進行主動監控](#設定警示以進行主動監控)
- [結論](#結論)

### 簡介

在雲端計算的世界中，Microsoft Azure 作為一個強大的平台，用於建立、部署和管理應用程式。在我們最近的專案中，我們利用了多項 Azure 服務，包括 Azure 訂閱、Azure Kubernetes Service (AKS)、Application Insights、虛擬機器 (VMs)、Event Hubs、API Management Services 和 SQL 資料庫，以建立一個可擴展且監控的應用程式基礎架構。本篇部落格文章概述了我們的方法、使用的工具、最佳實踐以及管理集群、提取日誌和查詢日誌的詳細步驟。

### 開始使用 Azure 訂閱

Azure 訂閱是您存取 Azure 服務的入口。它作為一個容器，包含所有您的資源，例如虛擬機器、資料庫和 Kubernetes 集群。

1. 設定 Azure 訂閱：
   - 註冊：如果您沒有 Azure 帳戶，請從 [Azure 入口網站](https://portal.azure.com/) 開始註冊。
   - 建立訂閱：導航至「訂閱」部分並建立新訂閱。這將是您的計費和管理容器。

2. 資源組織：
   - 資源群組：根據其生命週期和管理標準，將資源組織成資源群組。
   - 標籤：使用標籤以便於資源管理和計費。

### 使用 Azure Kubernetes Service (AKS) 部署應用程式

Azure Kubernetes Service (AKS) 是一項受管理的 Kubernetes 服務，簡化了部署、管理和擴展容器化應用程式的流程。

#### 建立和管理 AKS 集群

1. 在 Azure 入口網站建立 AKS 集群：
   - 設定：在 Azure 入口網站中，搜尋 AKS 並建立新的 Kubernetes 集群。
   - 設定：選擇您的集群大小，設定節點池，並設定網路。
   - 驗證：使用 Azure Active Directory (AAD) 進行安全存取控制。
   - 監控：在設定過程中啟用監控和日誌記錄。

2. 使用 Azure CLI 建立 AKS 集群：
   ```sh
   az aks create \
     --resource-group myResourceGroup \
     --name myAKSCluster \
     --node-count 3 \
     --enable-addons monitoring \
     --generate-ssh-keys
   ```

3. 管理您的 AKS 集群：
   - 擴展集群：
     ```sh
     az aks scale \
       --resource-group myResourceGroup \
       --name myAKSCluster \
       --node-count 5
     ```
   - 升級集群：
     ```sh
     az aks upgrade \
       --resource-group myResourceGroup \
       --name myAKSCluster \
       --kubernetes-version 1.21.2
     ```

#### 部署應用程式

1. 使用 Kubernetes 清單：為您的部署、服務和其他 Kubernetes 物件編寫 YAML 檔案。
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: myapp
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: myapp
     template:
       metadata:
         labels:
           app: myapp
       spec:
         containers:
         - name: myapp
           image: myregistry.azurecr.io/myapp:latest
           ports:
           - containerPort: 80
   ```

2. 使用 kubectl 部署：
   ```sh
   kubectl apply -f myapp-deployment.yaml
   ```

3. Helm 圖表：使用 Helm 管理 Kubernetes 應用程式和版本控制。
   ```sh
   helm install myapp ./mychart
   ```

### 從 Pod 提取日誌

1. 附加到 Pod 並提取日誌：
   ```sh
   kubectl logs <pod-name>
   ```
   - 以串流方式提取日誌：
     ```sh
     kubectl logs <pod-name> -f
     ```

2. 使用 Sidecar 進行日誌記錄：
   - 在 Pod 規範中建立日誌記錄 Sidecar 容器，以將日誌發送到集中式日誌記錄服務。

   ```yaml
   spec:
     containers:
     - name: myapp
       image: myregistry.azurecr.io/myapp:latest
       ...
     - name: log-shipper
       image: log-shipper:latest
       ...
   ```

### 使用 Azure Application Insights 進行監控和診斷

Application Insights 提供強大的監控和診斷功能，用於您的應用程式。

1. 設定 Application Insights：
   - 整合：將 Application Insights SDK 添加到您的應用程式代碼中。
   - 工具配置：使用 Application Insights 資源中的工具配置鍵配置您的應用程式。

2. 追蹤效能：
   - 指標：監控響應時間、失敗率和應用程式依賴性。
   - 即時指標串流：查看即時效能指標以獲取即時見解。

3. 診斷和故障排除：
   - 應用程式地圖：可視化依賴性並識別效能瓶頸。
   - 交易診斷：使用分散式追蹤跨服務追蹤請求。

### 使用 Azure 虛擬機器 (VMs)

Azure VMs 提供了靈活性，可運行未容器化的自訂應用程式和服務。

1. 配置虛擬機器：
   - 建立 VMs：在 Azure 入口網站中建立新的虛擬機器並選擇適當的大小和作業系統。
   - 網路設定：設定虛擬網路、子網和安全群組以控制流量。

2. 設定 VMs：
   - 軟體安裝：安裝所需的軟體和依賴項。
   - 安全性：定期應用補丁和更新，設定防火牆，並使用網路安全群組 (NSGs)。

3. 管理 VMs：
   - 備份和還原：使用 Azure 備份進行 VM 備份。
   - 監控：使用 Azure Monitor 監控 VM 效能。

### 使用 Azure Event Hubs 進行即時數據攝取

Azure Event Hubs 是一個大數據串流平台和事件攝取服務，能夠接收和處理每秒數百萬個事件。

1. 設定 Event Hubs：
   - 建立 Event Hub 命名空間：在 Azure 入口網站中建立 Event Hub 命名空間以容納您的 Event Hubs。
   - 建立 Event Hubs：在命名空間中建立一個或多個 Event Hubs 以捕獲您的數據串流。

2. 攝取數據：
   - 生產者：設定您的應用程式或服務以使用多種語言（例如 .NET、Java、Python）提供的 SDK 將事件發送到 Event Hubs。
   - 分區：使用分區以擴展事件處理，確保高吞吐量和並行性。

3. 處理事件：
   - 消費者：使用消費者群組讀取和處理事件。Azure 提供了多種處理選項，包括 Azure Stream Analytics、Azure Functions 和使用 Event Hubs SDK 的自訂處理。

4. 監控 Event Hubs：
   - 指標：通過 Azure 入口網站監控吞吐量、延遲和事件處理指標。
   - 警示：設定警示以通知您任何問題，例如高延遲或丟失的消息。

### 使用 Azure API Management Services 管理 API

Azure API Management Services 提供了一種方法，可為現有後端服務建立一致且現代化的 API 閘道。

1. 設定 API Management：
   - 建立 API Management 服務：在 Azure 入口網站中搜尋 API Management 並建立新服務。
   - 設定 API：從 OpenAPI 規範、Azure Functions 或其他後端定義和導入 API。

2. 保護 API：
   - 驗證和授權：使用 OAuth2、JWT 驗證和其他機制保護您的 API。
   - 速率限制和節流：實施策略以保護您的 API 不受濫用。

3. 監控和分析：
   - API Insights：追蹤使用情況、監控效能並分析日誌。
   - 開發者入口網站：為開發者提供一個入口網站以發現和使用您的 API。

4. 管理生命週期：
   - 版本控制和修訂：無縫管理您的 API 的不同版本和修訂。
   - 策略管理：應用策略以轉換、驗證和路由請求和響應。

### 使用 Azure SQL 資料庫

Azure SQL 資料庫是一個完全受管理的關聯式資料庫，具有內建智能、高可用性和可擴展性。

1. 設定 Azure SQL 資料庫：
   - 建立 SQL 資料庫：在 Azure 入口網站中導航至 SQL 資料庫並建立新資料庫。
   - 設定資料庫：設定資料庫大小、效能級別並設定網路設定。

2. 連接到 SQL 資料庫：
   - 連接字串：使用提供的連接字串將您的應用程式連接到 SQL 資料庫。
   - 防火牆規則：設定防火牆規則以允許來自您的應用程式或本地機器的存取。

3. 管理資料庫：
   - 備份和還原：使用自動備份和按時間點還原以保護您的數據。
   - 擴展：根據您的效能需求擴展或縮減資料庫。

4. 監控和效能調優：
   - 查詢效能洞察：監控和優化查詢效能。
   - 自動調優：啟用自動調優功能以提高效能。

### 使用 Kusto 查詢語言 (KQL) 查詢日誌

Kusto 查詢語言 (KQL) 用於查詢 Azure Monitor 日誌，提供強大的日誌數據洞察。

1. 基本 KQL 查詢：
   ```kql
   // 從特定表中檢索記錄
   LogTableName
   | where TimeGenerated > ago(1h)
   | project TimeGenerated, Level, Message
   ```

2. 篩選和聚合數據：
   ```kql
   LogTableName
   | where TimeGenerated > ago(1h) and Level == "Error"
   | summarize Count=count() by bin(TimeGenerated, 5m)
   ```

3. 連接表：
   ```kql
   Table1
   | join kind=inner (Table2) on $left.UserId == $right.UserId
   | project Table1.TimeGenerated, Table1.Message, Table2.AdditionalInfo
   ```

4. 根據查詢建立警示：
   - 在 Azure 入口網站中導航至 Log Analytics 工作區。
   - 點擊 `Logs` 並輸入您的 KQL 查詢。
   - 點擊 `新增警示規則` 以根據查詢結果建立警示。

### 設定警示以進行主動監控

Azure 警示可幫助您了解資源的健康狀況和效能。

1. 建立警示：
   - 指標警示：根據指標（例如 CPU 使用率、記憶體使用率和響應時間）設定警示。
   - 日誌警示：使用 KQL 建立基於日誌搜索查詢的警示。

2. 設定操作：
   - 操作群組：定義操作群組以指定誰將收到通知以及如何通知（電子郵件、短訊、網路鉤子）。
   - 整合：與 ITSM 工具（如 ServiceNow）整合以進行自動化事件管理。

3. 回應警示：
   - 儀表板：設定 Azure 儀表板以提供警示的集中式視圖。
   - 自動化：使用 Azure 自動化自動回應某些警示。

### 結論

透過利用 Azure 訂閱、AKS、Application Insights、虛擬機器、Event Hubs、API Management Services 和 SQL 資料庫，我們建立了一個可擴展、穩健且監控的應用程式基礎架構。Azure 綜合套件的工具確保我們能夠高效地部署、管理和監控應用程式。此設定不僅提高了我們的應用程式效能，還為我們提供了所需的洞察力，以主動維護和優化資源。