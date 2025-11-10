---
audio: false
generated: true
lang: hant
layout: post
title: Meta智能眼鏡：功能與應用程式介面
translated: true
type: note
---

讓我們來解析 Meta 的智能眼鏡產品線，包括 Ray-Ban 和 Oakley，其用戶群體以及為開發者提供的 API 功能。

**什麼是 Meta VR 眼鏡、Ray-Ban 和 Oakley 智能眼鏡？**

首先需要釐清術語。「Meta VR 眼鏡」並非 Meta 廣泛使用的具體產品名稱。Meta 主要的 VR/MR 產品是 **Meta Quest** 系列頭戴設備（例如 Meta Quest 3）。

當人們談及「Meta 眼鏡」這種更接近傳統眼鏡形態的產品時，通常指的是：

* **Ray-Ban Meta 智能眼鏡：** 這是與 EssilorLuxottica（Ray-Ban 母公司）合作開發的消費級智能眼鏡，外觀設計類似傳統 Ray-Ban 太陽眼鏡，主要功能包括：
    * 免手持照片與影片拍攝（配備隱私指示燈）
    * 開放式耳機音頻播放（音樂、播客、通話）
    * 整合麥克風用於通話與語音指令（支援「Hey Meta」喚醒 Meta AI）
    * 即時串流至 Facebook 與 Instagram
    * 整合 Meta AI 實現多種任務（如獲取資訊、發送訊息、環境描述無障礙功能）
    * 無內建顯示屏或 AR 頭戴顯示功能（屬於「智能眼鏡」而非典型 AR 眼鏡）

* **Oakley Meta 眼鏡（如 Oakley Meta HSTN）：** 這是與同屬 EssilorLuxottica 集團的 Oakley 合作推出的新款「性能 AI 眼鏡」，具備 Ray-Ban Meta 眼鏡的多數功能，但專為運動員與高性能需求設計，特點包括：
    * 經典 Oakley 運動風格外觀
    * 增強耐用性與防潑水功能（IPX4）
    * 更長電池續航
    * 更高解析度相機（3K 影片）
    * 整合 Meta AI 提供運動專屬功能（如查詢高爾夫風況）

**用戶規模如何？**

截至 2025 年 2 月，**Ray-Ban Meta 智能眼鏡**自 2023 年 9 月上市以來已售出超過 **200 萬台**。EssilorLuxottica 計劃在 2026 年底前將年產能提升至 1,000 萬台，顯示市場需求強勁與 Meta 對產品前景的信心。

**Oakley Meta 眼鏡**作為新產品線，已於 2025 年 7 月開放預購，目前尚未公布具體用戶數據，但預期將佔據重要市場份額。

**為開發者提供哪些 API？**

需區分 VR/MR 頭戴設備（如 Meta Quest）與智能眼鏡（如 Ray-Ban Meta 與 Oakley Meta）的 API 差異。

**針對 Meta Quest（VR/MR 頭戴設備）：**

Meta 為其 Meta Horizon OS（前身為 Quest OS）提供完善的開發者平台，包含多種 API 與 SDK 用於創建沉浸式 VR 與混合實境體驗，重點領域包括：

* **OpenXR：** 建構高效能 XR 體驗的開放標準，支援跨平台 VR/MR 應用開發
* **Meta Horizon Worlds：** 在 Meta 社交 VR 平台內創建體驗的開發工具
* **Android 應用：** 使現有 Android 應用兼容 Meta Horizon OS 並運用其空間運算功能
* **網頁開發：** 設計可運用 Quest 多工能力的 2D 網頁應用
* **Meta Spatial SDK：** 專為混合實境設計，可為 2D 應用添加創新空間元素
* **穿透相機 API：** 無縫融合虛實場景，創建混合實境應用
* **互動 API：** 支援手部追蹤、控制器輸入、移動控制等功能
* **語音指令與文字轉語音 API：** 整合語音控制與語音輸出功能
* **場景理解 API：** 存取並運用實體環境數據（如場景網格、錨點）
* **社交功能 API：** 實現排行榜、挑戰賽、用戶通知等服務

**針對 Ray-Ban Meta 與 Oakley Meta 智能眼鏡：**

目前尚未發布專供第三方開發者直接在此類智能眼鏡上建置自訂應用的完整官方 SDK 或 API。

但開發者已透過創新方式與設備互動：

* **Meta AI 整合：** 主要透過 **Meta AI** 整合實現互動，開發者可運用現有大型語言模型（LLM）與 AI 服務的 API 來調用 Meta AI 功能。例如有社群專案透過 Messenger 作為橋接，將眼鏡指令傳送至 ChatGPT 或 Google Gemini 等服務處理資料
* **內容分享：** 眼鏡主要作為拍攝與分享設備，開發者可透過 **Meta View app**（眼鏡配套應用）提供內容分享管道，類似 Instagram、Facebook、WhatsApp 等平台的分享機制
* **無障礙功能：** 內建 Meta AI 提供環境描述與文字朗讀等無障礙功能，雖未直接開放開發者建置新應用，但展現未來透過更開放工具實現 AI 輔助功能的潛力

儘管 Meta 已表明未來智能眼鏡（如傳聞中的「Orion」專案）將朝向更開放開發的長期願景，但目前 Ray-Ban Meta 與 Oakley Meta 智能眼鏡的開發者存取權限仍主要透過 Meta AI 整合與內容分享功能間接實現。在缺乏專用公開 SDK 的情況下，開發社群正積極探索非官方整合方案。