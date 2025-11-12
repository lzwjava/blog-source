---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Claude 代碼重大更新
translated: true
type: note
---

### Claude Code 的重大更新

Anthropic 的人工智慧編碼助手 Claude Code 近期迎來顯著增強，特別是在自主性、整合性及使用者介面功能方面。根據最新消息（2025 年 9 月 29 日），關鍵更新聚焦於實現更高自主運作能力，包括推出原生 VS Code 擴充功能、升級終端介面（2.0 版），以及用於管理長時間任務的全新檢查點功能。此外，像是切換「思考」模式這類功能也屬於持續優化的一部分，讓使用者能開關 Claude 的推理步驟顯示，實現更簡潔的互動體驗 [1]。

#### 自主性與代理能力
- **原生 VS Code 擴充功能**：實現與 VS Code 編輯器的無縫整合，讓 Claude Code 能直接在開發環境中運作，進行更自主的程式碼編輯與除錯
- **終端介面 v2.0**：升級內容包含改進的權限處理、跨任務記憶體管理，以及子代理協調功能。這使 Claude Code 在複雜工作流程中能更佳平衡使用者控制與自動化操作 [1][2]
- **檢查點**：用於保存長時間任務進度的新功能，允許暫停與恢復作業而不遺失上下文。這項功能支援橫跨多日或多工作階段的任務執行

這些改變建立在 Anthropic 的 Claude Agent SDK 基礎上，為開發者提供能創建自訂 AI 代理的工具，這些代理可映射 Claude Code 的內部基礎架構 [2]。

#### 其他值得注意的變更
- **模型升級整合**：Claude Code 現預設採用 Claude Sonnet 4.5 模型，在編碼任務中提供更優異的效能且無價格變動。此模型因其增強的对齊能力與減少幻覺現象，被推薦在所有 Claude 產品中使用 [2]
- **使用者介面調整**：「關閉思考模式（按 Tab 鍵切換）」功能似乎是用於顯示或隱藏 Claude 內部推理過程的開關，這能讓輸出更加流暢。此調整符合使用者對編碼過程中透明度與可用性的反饋 [3]
- **已知問題修復嘗試**：針對 Claude Code 因訓練資料截斷而將「2024年」附加至搜索結果的報告正在處理中，儘管部分使用者指出錯誤仍持續存在。現有解決方案包含使用自訂鉤子來更新日期感知能力 [3][4]

欲瞭解完整詳情，請安裝或檢查最新版本——所有使用者都會自動套用更新 [1]。若您遇到問題，請確保用戶端為最新版本。如需查閱歷史變更記錄，可參考社群更新日誌如 ClaudeLog，但可能未涵蓋最即時的功能 [5]。

參考文獻：
[1] https://anthropic.com/news/enabling-claude-code-to-work-more-autonomously
[2] https://www.anthropic.com/news/claude-sonnet-4-5
[3] https://www.reddit.com/r/ClaudeAI/comments/1mtgjdi/claude_code_thinks_it_is_2024_and_keeps_web/
[4] https://medium.com/@dan.avila7/fixed-claude-codes-2024-tunnel-vision-with-a-simple-hook-cb32cfaf9b27
[5] https://www.claudelog.com/claude-code-changelog/