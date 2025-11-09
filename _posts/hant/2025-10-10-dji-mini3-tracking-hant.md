---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: DJI Mini 3 追蹤限制與解決方案
translated: true
type: note
---

DJI Mini 3（基礎型號）不具備內建的 ActiveTrack（視覺目標跟隨）或 Follow Me 模式（基於 GPS 的追蹤）功能，無法自動追蹤移動車輛或懸停於車輛上方進行拍攝。這是相較於 DJI 高端無人機的主要限制。然而，DJI Mini 3 Pro 確實支援 ActiveTrack，該功能透過無人機鏡頭對車輛、人物或移動目標進行視覺追蹤，可實現從後方、上方或其他角度的智能跟隨，讓無人機在保持設定距離與高度的同時捕捉動態畫面。

關於客製化開發的 API 支援：
- DJI Mobile SDK（適用 Android/iOS 應用程式）確實支援 Mini 3 系列，包含基礎飛行控制功能（如虛擬搖桿指令調整位置/速度）與航點任務。若整合車輛即時 GPS 數據（透過藍牙、配套應用程式或外部傳輸器），可開發客製化應用實現無人機沿車輛路徑跟隨。此非「即插即用」的視覺追蹤，但可透過計算偏移量（例如保持後方 10-20 公尺與上方 50 公尺）模擬追車效果。
- 但需注意：SDK 中的 ActiveTrack 任務 API（自動視覺跟隨）**不支援** Mini 3 與 Mini 3 Pro，僅限舊款機型如 Mavic Air 2 或 Air 2S。
- 飛行中的拍攝功能可透過 SDK 相機 API 實現，支援依計時器、距離或自訂邏輯自動觸發拍攝。

若考慮使用第三方應用程式（底層基於 SDK 開發）：
- 如 Dronelink 或 Litchi 等應用可透過手機 GPS（或外部裝置）為 Mini 3 啟用基礎 "Follow Me" 模式。若要精準追蹤車輛，需搭配車載 GPS 信標（例如透過手機熱點或專用追蹤器如 Tile/AirTag 替代品向應用程式傳輸數據）。此配置已被用戶成功應用於道路或小徑的車輛追蹤，實現無人機高空跟隨或尾隨拍攝。

請注意法規與安全事項：無人機跟隨移動車輛需符合當地規範（例如美國 FAA 要求保持視距內操作，禁止超視距飛行）。建議在空曠區域測試以避免障礙物，且 Mini 3 的輕量化設計在高速追蹤時抗風能力有限。

### 參考資料
- [DJI Mini 3 Active Track 破解教程](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Mini 3 是否具備 AI 追蹤功能以跟隨車輛等物體](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [有人能解釋 Follow Me 模式嗎？Mini 3 是否支援？](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [使用 Dronelink 實現 DJI Mini 3 / Mini 3 Pro 跟隨模式](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI 產品 SDK 相容性列表](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI 發布支援 Mini 3 Pro 與 Mini 3 的 MSDK 5.3.0](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [ActiveTrackOperator 類別 - DJI Mobile SDK 文件](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)