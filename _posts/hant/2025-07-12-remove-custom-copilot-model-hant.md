---
audio: false
generated: true
lang: hant
layout: post
title: 移除 GitHub Copilot 中的自訂模型
translated: true
type: note
---

若要移除 Visual Studio Code (VS Code) 中 GitHub Copilot 擴充功能的模型，請注意內建模型（例如預設的 GitHub Copilot 模型）無法移除，因為它們是擴充功能的一部分。但若您指的是透過第三方供應商（例如 Anthropic、OpenAI、Google Gemini 或其他）使用自己的 API 金鑰所新增的自訂模型，您可以透過刪除相關的 API 金鑰與供應商詳細資訊來有效移除該模型。此功能目前處於預覽階段，可能尚未提供給 Copilot Business 或 Enterprise 用戶使用。

根據官方文件，以下是操作步驟：

1. 在 VS Code 中開啟 Chat 視圖（若未開啟，可使用命令選擇器，按下 `Ctrl+Shift+P` 或 macOS 上的 `Cmd+Shift+P`，然後搜尋「Copilot: Open Chat」）。
2. 在 Chat 視圖中，點擊模型選擇下拉選單（位於輸入欄位旁）並選擇 **Manage Models**。或者，開啟命令選擇器並執行 **GitHub Copilot: Manage Models** 命令。
3. 在 Manage Models 介面中，將滑鼠懸停在要移除模型的供應商上，點擊齒輪圖標以編輯其詳細資訊。
4. 從欄位中刪除 API 金鑰（以及適用的端點 URL），然後儲存變更。這應會從選擇器中移除該模型的可用性。

若您遇到問題（例如 API 金鑰欄位無法正常更新或清除，此問題在某些情況下被回報為錯誤），請先嘗試以下解決方法：
- 在 Chat 視圖的模型選擇器中選擇其他模型，以取消選取您要移除的模型。
- 返回 Manage Models，編輯供應商，然後刪除 API 金鑰。

先決條件與注意事項：
- 此操作僅適用於聊天功能，不影響程式碼補全或其他工具。
- 請確保您的 Copilot 訂閱允許存取多個模型（例如 Individual、Pro 或為組織啟用的預覽功能）。
- 若模型仍然存在或您遇到錯誤，請重新啟動 VS Code 或檢查擴充功能更新。

若這與您所說的「移除模型」不符（例如您想停用整個擴充功能或隱藏 Copilot 功能），請進一步說明以獲得更具體的步驟。