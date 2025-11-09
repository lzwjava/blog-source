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

### Google Cloud Platform (GCP) 重大故障歷史記錄

Google Cloud Platform 自早期發展以來曾經歷多次重大故障，通常由軟件錯誤、硬件故障、環境因素或容量問題引起。下表總結了一些最引人注目的故障事件，選取標準基於其影響規模、持續時間或廣泛程度。這些記錄取材截至2025年中的歷史資料。

| 日期 | 原因 | 影響 |
|------|--------|--------|
| 2020年12月14日 | 中央用戶ID管理系統容量意外削減，影響基於OAuth的身份驗證 | 全球中斷約90分鐘；導致全球數百萬用戶無法訪問Gmail、YouTube、Google Drive、GCP服務及《Pokémon GO》等應用程式 |
| 2022年7月 | 倫敦超過40°C的極端熱浪導致europe-west2-a區域冷卻系統故障 | 區域性中斷約24小時；影響Cloud Storage、BigQuery、Compute Engine、GKE等服務，迫使故障轉移至其他區域 |
| 2022年8月8日 | 愛荷華州康瑟爾布拉夫斯數據中心電氣事故引發火災（與同期搜索/地圖問題無關） | 局部火災應對；Cloud Logging服務全球延遲持續數日，影響GCP用戶的監控和除錯功能 |
| 2023年4月28日 | 巴黎數據中心進水與火災，引發europe-west9-a多集群故障 | 歐洲、亞洲、美洲廣泛中斷；VPC、負載平衡、BigQuery及網絡服務受影響數小時至數日 |
| 2024年8月7-8日 | Vertex AI的API啟用期間Cloud TPU服務激活失敗 | 全球中斷約14小時；阻礙所有主要區域的機器學習模型上傳與訓練功能 |
| 2024年10月23日 | europe-west3-c區域（法蘭克福）電力故障與電弧效應，導致冷卻基礎設施效能下降 | 半日區域中斷（約8小時）；基礎設施部分關閉，流量轉移至其他區域 |
| 2025年1月7-8日 | Apigee的SAML身份驗證失敗、Vertex Gemini API的HTTP錯誤及Pub/Sub發布阻塞等多重關聯問題 | 超過18小時的多時段中斷；影響跨區域的API管理、AI推理與實時訊息傳遞服務 |
| 2025年6月12日 | 新服務控制功能（配額政策檢查）的錯誤導致us-central1等大型區域任務過載 | 全球中斷約7小時；導致Spotify、Discord、Fitbit及眾多GCP依賴服務癱瘓，收到超過140萬份故障報告 |

這些事件凸顯GCP從2000年代末期App Engine的早期問題，到近期系統性故障的成長陣痛。Google通常會發布事故檢討報告與改進方案，例如透過模組化組件實現「故障開放」機制。最新狀態請查閱 [Google Cloud Service Health](https://status.cloud.google.com/)。

[Google雲端與數據中心故障歷史](https://www.datacenterknowledge.com/outages/a-history-of-google-cloud-and-data-center-outages)  
[Google服務中斷 - 維基百科](https://en.wikipedia.org/wiki/Google_services_outages)  
[Google雲端故障歷史 | StatusGator](https://statusgator.com/blog/google-cloud-outage-history/)  
[2025年至今十大雲端故障 - CRN](https://www.crn.com/news/cloud/2025/the-10-biggest-cloud-outages-of-2025-so-far)  
[Google雲端故障分析：2025年6月12日 - ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)