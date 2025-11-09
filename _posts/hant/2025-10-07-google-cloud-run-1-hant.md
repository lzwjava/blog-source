---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Google Cloud Run 概覽
translated: true
type: note
---

### 什麼是 Google Cloud Run？

Google Cloud Run 是 Google Cloud Platform (GCP) 上一個完全託管的無伺服器平台，專為執行容器化應用程式而設計。它讓開發者能夠部署和擴展程式碼，無需擔心底層基礎架構，自動處理資源配置、擴展和維護。它支援無狀態 HTTP/HTTPS 請求、事件驅動工作負載，並在閒置時縮減至零個執行個體，使其極具成本效益。

### 主要功能與特色
- **容器化部署**：在標準容器（例如 Docker）中執行任何語言或框架，內建支援 HTTP/gRPC 服務、背景作業和非同步處理。
- **自動擴展與按用量付費**：根據流量從零擴展至數千個執行個體；您只需為實際用量（CPU、記憶體和請求）付費。
- **整合功能**：無縫與其他 GCP 服務協作，例如 Cloud Build（用於 CI/CD）、Cloud SQL（資料庫）、Pub/Sub（訊息傳遞）、Artifact Registry（容器儲存）以及用於 GPU 加速任務的 AI 工具。
- **安全性與網路**：內建身份驗證 (IAM)、VPC 連線能力以及用於安全部署的二進位授權。
- **免費層級**：每月最多 200 萬次請求免費。

### 典型使用情境
Cloud Run 非常適合需要靈活性和低開銷的現代事件驅動應用程式。常見範例包括：
- **網路應用程式與 API**：託管無狀態微服務、RESTful API 或完整的網路應用程式（例如，從資料庫提供動態內容的 Node.js 後端）。它在處理可變流量的電子商務網站或行動後端中表現出色。
- **批次作業與資料處理**：執行排程任務，例如 ETL（擷取、轉換、載入）管道或影像/影片處理佇列，由 Cloud Scheduler 或 Pub/Sub 觸發。
- **AI/ML 工作負載**：託管大型語言模型（LLM），如 Llama 3.1 或 Gemma 2，用於即時推論，例如聊天機器人、影像識別或影片轉碼。GPU 支援使其適合計算密集型任務。
- **無伺服器遷移**：從虛擬機器或 Kubernetes（例如透過 Knative）過渡以降低成本——例如 Telegraph Media Group 在遷移後報告節省了 90% 的成本和碳排放。

本質上，它非常適合希望擁有類似 Kubernetes 的能力而無需運維負擔的開發者，尤其適用於突發性或不可預測的工作負載。

[Cloud Run 文件](https://cloud.google.com/run)