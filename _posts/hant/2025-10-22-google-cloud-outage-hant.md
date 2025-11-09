---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Google 雲端平台重大服務中斷
translated: true
type: note
---

### 概述
2025年6月12日，Google Cloud Platform (GCP) 發生持續約7.5小時的全球大規模服務中斷（從太平洋夏令時間10:51至18:18）。事件源於Google服務控制系統中新功能的一個程式錯誤，該錯誤與配額政策檢查相關。這導致無效的自動化配額更新在全球範圍傳播，造成大規模API拒絕及任務超載，尤其在us-central1（愛荷華州）等高流量區域。此次中斷影響了眾多GCP服務、Google Workspace產品及依賴GCP基礎設施的第三方應用程式，在Downdetector上收到超過140萬份用戶報告。

### 時間線
（所有時間均為美國/太平洋夏令時間）

- **上午10:51**：中斷開始，多個GCP及Google Workspace產品的外部API請求出現503錯誤激增，導致間歇性存取問題。
- **上午11:46**：工程團隊確認服務大範圍受影響，展開調查。
- **中午12:09**：啟動緩解措施，除us-central1外多數區域開始恢復。
- **中午12:41**：確定根本原因為無效配額政策數據，實施配額檢查繞過方案。
- **下午1:16**：除us-central1及美國多區域外，所有區域基礎設施完全恢復。
- **下午2:00**：us-central1出現恢復跡象，預計一小時內完全緩解。
- **下午3:16**：多數GCP產品恢復，但Dataflow、Vertex AI及個人化服務健康狀態仍存在殘留問題。
- **下午5:06**：Dataflow與個人化服務健康狀態問題解決，Vertex AI問題持續，預計解決時間為晚上10:00。
- **下午6:27**：Vertex AI在所有區域完全恢復。
- **下午6:18**：事件正式結束，服務全面恢復。

主要緩解措施耗時約3小時，但殘留的積壓任務及錯誤使總影響時間延長至7.5小時。

### 根本原因
此次中斷由服務控制功能（負責管理API配額與政策）的缺陷引發。自動化系統將包含空白或空值欄位的無效配額政策插入資料庫。由於全球複製機制（設計用於實現近即時一致性），這些損壞數據在數秒內蔓延至全球。當API請求觸發配額檢查時，導致空指標異常及拒絕（503與5xx錯誤升高）。在us-central1等大型區域，大量失敗請求引發嚴重任務超載及依賴服務的連鎖故障。新功能對空白欄位等邊緣案例缺乏充分驗證，且系統未設定「故障開放」機制（允許檢查期間請求繼續執行）。

### 受影響服務
此次中斷影響了廣泛的Google產品及依賴GCP的外部服務。核心GCP與Google Workspace服務出現不同程度的癱瘓，包括API故障及UI存取問題（串流與IaaS資源未受影響）。

#### 受影響的主要Google Cloud產品
- **運算與儲存**：Google Compute Engine、Cloud Storage、Persistent Disk。
- **資料庫**：Cloud SQL、Cloud Spanner、Cloud Bigtable、Firestore。
- **數據與分析**：BigQuery、Dataflow、Dataproc、Vertex AI（包含Online Prediction與Feature Store）。
- **網絡與安全**：Cloud Load Balancing、Cloud NAT、Identity and Access Management (IAM)、Cloud Security Command Center。
- **開發者工具**：Cloud Build、Cloud Functions、Cloud Run、Artifact Registry。
- **AI/ML**：Vertex AI Search、Speech-to-Text、Document AI、Dialogflow。
- **其他**：Apigee、Cloud Monitoring、Cloud Logging、Resource Manager API。

#### 受影響的主要Google Workspace產品
- Gmail、Google Drive、Google Docs、Google Meet、Google Calendar、Google Chat。

#### 受影響的第三方服務
許多託管於或部分依賴GCP的消費級及企業級應用出現停機：
- **Spotify**：約46,000名用戶的串流及應用存取中斷。
- **Discord**：語音聊天及伺服器連線問題。
- **Fitbit**：同步及應用功能暫停。
- **其他**：OpenAI (ChatGPT)、Shopify、Snapchat、Twitch、Cloudflare（連鎖DNS問題）、Anthropic、Replit、Microsoft 365（部分）、Etsy、Nest。

由於GCP支撐全球互聯網後端基礎設施的重要部分，事件影響因全球規模而放大。

### 解決方案
Google工程團隊迅速識別無效政策，並實施配額檢查繞過方案，允許危機期間API請求無需驗證即可執行。此舉在太平洋夏令時間下午12:48前恢復了多數區域。針對us-central1，實施了針對性超載緩解措施，隨後對Dataflow與Vertex AI等受影響服務進行手動積壓清除。監控系統確認在太平洋夏令時間下午6:18實現全面恢復。未發生數據遺失，但部分服務出現暫時延遲。

### 影響
- **規模**：Downdetector收到超過140萬份報告，顯示即時全球中斷。
- **經濟**：企業可能損失數十億生產力；Spotify報告高峰時段用戶不滿。
- **聲譽**：凸顯雲端集中風險，引發對多雲端策略的呼聲。

### 經驗總結與預防措施
Google發布詳細事後分析報告，強調韌性建設：
- **架構調整**：模組化服務控制以隔離故障，啟用「故障開放」模式。
- **數據驗證**：全球變更實施增量傳播與預先驗證；加強無效輸入測試。
- **部署防護**：關鍵更新強制使用功能標誌；改進靜態分析與錯誤處理。
- **監控與通訊**：確保中斷檢測工具獨立運作；加快自動化客戶警報。
- **廣泛措施**：在重試邏輯中引入隨機退避機制，防止超載連鎖反應。

這些步驟旨在預防類似事件，並持續進行配額系統稽核。

[Google Cloud事件報告](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)  
[ThousandEyes中斷分析](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)  
[Ookla Downdetector報告](https://www.ookla.com/articles/google-cloud-outage-june-2025)  
[ByteByteGo技術解析](https://blog.bytebytego.com/p/how-the-google-cloud-outage-crashed)  
[Medium根本原因說明](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-a-single-google-cloud-bug-caused-global-internet-outage-on-june-12-2025-652a83ad9e68)