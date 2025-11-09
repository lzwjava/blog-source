---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MongoDB 為 LibreChat 帶來的靈活性
translated: true
type: note
---

LibreChat 作為一個開源 AI 聊天機器人介面，預設採用 MongoDB 作為資料庫，主要歸因於 NoSQL 資料庫（如 MongoDB）的靈活性。與 MySQL 或 PostgreSQL 這類強制使用固定結構和結構化資料表的關聯式資料庫不同，MongoDB 採用基於文件的模型，無需預先定義結構描述。這使得處理不斷演變的資料結構更加容易——尤其在快速變化的 AI 生態系統中，新的模型、對話格式和功能頻繁新增，而無需進行大量的資料庫遷移。

LibreChat 團隊的一名開發者指出，MongoDB「易於分佈且開放性足以了解其源碼，這使其廣泛可用且可靠。更重要的是，它作為 NoSQL 資料庫確實允許靈活性，尤其當 AI 服務不斷倍增和演進時，能適應持續變化的資料結構。」這與專案在自託管或基於 Docker 的設置中對可擴展性和適應性的需求相符，正如您在容器日誌（例如 `chat-mongodb` 容器）中所見。

雖然 MySQL 和 PostgreSQL 在處理交易性和關聯式資料方面非常穩健，但它們會為 LibreChat 的半結構化資料（如用戶對話、端點和中繼資料）增加複雜性。該專案官方並不支援在不進行自訂修改的情況下切換至這些資料庫，儘管社群討論中探索了與 MongoDB 相容的替代方案，例如 FerretDB，以實現完全開源的設置。

[為何 LibreChat 使用 MongoDB](https://www.librechat.ai/docs/user_guides/mongodb)  
[以自由/開源資料庫替代 MongoDB 的 GitHub 討論](https://github.com/danny-avila/LibreChat/discussions/3985)