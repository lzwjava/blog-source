---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 瑞士北部 Azure 服務大規模中斷
translated: true
type: note
---

### 瑞士北部 Azure 服務中斷事件：2025年9月26-27日

此次事件是瑞士北部區域一次重大的平台級中斷，影響多個可用性區域。中斷持續約22小時，始於UTC時間9月26日23:54，並於UTC時間9月27日21:59全面恢復。雖然多數服務在UTC時間9月27日04:00左右恢復，但部分殘留問題仍需在當天稍後進行手動干預。

#### 根本原因
中斷源於對軟體負載平衡器基礎設施中授權通訊所用憑證進行的計劃性配置變更。其中一個新憑證含有**格式錯誤的數值**，且未在驗證過程中被偵測。此變更遵循加速部署路徑，意外地將配置跨多區域推送而未觸發健康防護機制，導致：
- 負載平衡器與儲存資源及節點的連線中斷
- 受影響的VM偵測到長時間磁碟斷線，為避免資料損毀而自動關機
- 影響蔓延至依賴服務，擴大衝擊範圍

#### 受影響服務
此次中斷波及瑞士北部託管的廣泛Azure服務，包括：
- **核心基礎設施**：Azure Storage、Azure Virtual Machines (VMs)、Azure Virtual Machine Scale Sets (VMSS)
- **資料庫服務**：Azure Cosmos DB、Azure SQL Database、Azure SQL Managed Instance、Azure Database for PostgreSQL
- **運算與應用**：Azure App Service、Azure API Management、Azure Kubernetes Service (AKS)、Azure Databricks
- **網路與安全**：Azure Application Gateway、Azure Firewall、Azure Cache for Redis
- **分析與監控**：Azure Synapse Analytics、Azure Data Factory、Azure Stream Analytics、Azure Data Explorer、Azure Log Analytics、Microsoft Sentinel
- **其他服務**：Azure Backup、Azure Batch、Azure Site Recovery、Azure Application Insights

依賴這些服務的應用（如自訂應用程式）同樣受到影響，導致大範圍服務不可用或效能降級。

#### 時間軸與緩解措施
- **9月26日 23:54 UTC**：配置變更部署後開始產生影響
- **9月27日 00:08 UTC**：自動化監測系統偵測到異常
- **9月27日 00:12 UTC**：Azure儲存與網路團隊啟動調查
- **9月27日 02:33 UTC**：執行配置變更回滾
- **9月27日 03:40 UTC**：憑證回滾完成
- **9月27日 04:00 UTC**：大多數服務自動恢復；識別出殘留問題（如因競爭條件或錯誤解讀關機訊號而處於停止/異常狀態的特定VM）
- **9月27日 06:19–14:15 UTC**：開發並驗證復原指令碼；對受影響資源（如SQL受控執行個體VM、Trusted Launch VM及Service Fabric叢集）執行定向重啟
- **9月27日 16:15 UTC**：殘留問題實現部分恢復
- **9月27日 21:59 UTC**：最終驗證後確認全面恢復

連線恢復後多數資源可自動復原，但部分資源（如使用自訂擴充功能的VM）需手動重啟以解決啟動順序問題。

#### 經驗總結與改進措施
微軟初步事件報告指出已實施的改進方案：
- 已完成部署系統審核機制並移除高風險加速管道
- 已完成強化自動回滾安全機制
- 預計2025年11月前實施：強化資源健康狀態監控與韌性復原流程，以減少手動操作需求

此次事件凸顯共享基礎設施中配置變更的潛在風險，但Azure的應對機制有效限制了資料損失並實現快速大範圍恢復。

[Azure狀態歷史記錄](https://azure.status.microsoft/en-us/status/history/)