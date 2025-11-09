---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 未命名為烏魯魯的 LeanCloud API
translated: true
type: note
---

不，LeanCloud 並未將其公開 API 命名為「Uluru API」。他們的官方 API 被稱為 LeanCloud REST API（用於數據存儲、查詢等）、Cloud Engine REST API（用於伺服器端函數和鉤子），以及類似推送通知或文件存儲等特定服務端點。這些都在其開發者網站 (docs.leancloud.cn) 上有詳細文檔記載，且沒有任何關於「Uluru」的參考資料。

然而，「Uluru」確實似乎是與其產品或 SDK 開發相關的內部或早期代號。這點可從一個名為 **uluru-js-sdk** 的存檔 npm 套件（版本 0.1.0，約 12 年前以 "avos" 發布者帳號發布）得到佐證。AVOS Cloud 是 LeanCloud 在重新品牌化前的原名，而該套件被描述為「用於 PAAS（平台即服務）的 JavaScript SDK」，這與 LeanCloud 的後端服務相符。它支援瀏覽器和 Node.js 環境的核心功能（如數據操作），與 LeanCloud 早期提供的服務相符，但從未作為主要 SDK 公開推廣。目前的 SDK 均以「LeanCloud SDK」為品牌（例如 Java、Python、JavaScript 等版本），並在 GitHub 的 leancloud/ 下提供。

若此名稱指涉的是更近期或更特定的內容（例如私有/內部工具），則並未見於公開文檔。如需官方 API 詳細資訊，請查閱 [LeanCloud 文檔](https://docs.leancloud.cn/en/)。