---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Google Cloud Run 入門指南
translated: true
type: note
---

Cloud Run 是 GCP 中完全託管的無伺服器運算平台，讓您能直接在 Google 可擴展的基礎架構上執行無狀態容器。它專為希望部署應用程式而無需擔心底層伺服器、資源配置或擴展的開發者設計。無論您是建置網路應用程式、API、微服務還是事件驅動工作負載，Cloud Run 都能處理基礎架構，讓您專注於程式碼。

### 主要功能
- **無伺服器執行**：部署容器化程式碼（支援任何語言或執行環境），能根據傳入請求或流量從零自動擴展至數千個執行個體
- **按使用量計費**：僅按消耗的資源收費（按請求或執行個體運行時長），對變動工作負載具成本效益
- **內建整合**：與其他 GCP 服務無縫協作，如 Cloud SQL（資料庫）、Cloud Storage（檔案儲存）、Pub/Sub（訊息傳遞）等，並支援 VPC 私有網路
- **部署選項**：
  - 從 Artifact Registry 或 Docker Hub 推送預先建置的容器映像
  - 使用 Cloud Build 直接從原始碼部署（支援 Node.js、Python、Java、Go、.NET 和 Ruby 等語言）
  - 使用 Cloud Run Functions 進行更簡易的函數即服務風格部署
- **安全性與網路**：服務可設為公開或私有（需要身份驗證），支援 HTTPS 端點和自訂網域
- **其他模式**：除了請求驅動服務外，還提供 Jobs 用於批次任務（如排程腳本或資料處理）和 Worker Pools 用於長時間運行的非 HTTP 工作負載

若要開始使用，您可以透過 GCP 控制台、gcloud CLI 或 CI/CD 管道部署。例如，在幾分鐘內建置並部署一個簡單的「Hello World」容器。

### Cloud Run 管理控制台
GCP 控制台中的 Cloud Run 部分提供直觀的儀表板來管理您的部署。以下是根據您分享的服務視圖所做的細分：

- **概覽**：主要的「Cloud Run > 服務」頁面以表格形式列出所有已部署的服務。開頭會顯示實用建議橫幅，如「在完全託管的平台上運行您的應用程式」，以便新用戶快速上手

- **表格欄位**（如您提供的片段所示）：
  - **名稱**：每個服務的唯一識別碼（例如「my-api」）
  - **部署類型**：顯示部署方式——例如「容器」表示映像部署，「原始碼」表示基於程式碼的部署
  - **請求數/秒**：即時請求頻率指標，用於監控流量負載
  - **區域**：服務運行的 GCP 區域（例如 us-central1），影響延遲和合規性
  - **身份驗證**：顯示服務是公開（允許未驗證）還是需要 IAM 身份驗證
  - **傳入流量**：控制流量路由——例如「全部」表示內外部皆可，或僅限內部
  - **最後部署時間**：最近更新的時間戳記
  - **部署者**：執行部署的用戶或服務帳戶

- **篩選器與操作**：在表格上方，您可以根據任何這些欄位進行篩選以縮小清單範圍。使用「建立服務」按鈕部署新服務，或點擊服務名稱來編輯設定，如 CPU/記憶體限制、環境變數、擴展配置或用於流量分割的修訂版本

此控制台讓您無需離開瀏覽器即可輕鬆監控效能、檢視日誌並迭代部署。若要實際探索，請在啟用 API 後前往 [console.cloud.google.com/run](https://console.cloud.google.com/run)

[什麼是 Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Cloud Run 文件](https://cloud.google.com/run/docs)