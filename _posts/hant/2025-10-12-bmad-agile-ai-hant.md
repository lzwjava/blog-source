---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: BMAD Core：敏捷人工智能開發基礎
translated: true
type: note
---

BMAD Core 是 BMAD 方法（突破性敏捷 AI 驅動開發方法）的基礎組件，這是一個開源框架，旨在透過在敏捷工作流程中協調專業 AI 代理，來簡化 AI 輔助的軟體開發（並可擴展至其他領域，如創意寫作或商業策略）。

### BMAD Core 的關鍵面向：
- **角色與目的**：它作為一個「精簡、快速的基礎」，標準化 AI 代理、工作流程、政策與模板，以確保可預測的高品質輸出。這透過使用結構化的 Markdown/YAML 檔案來定義代理角色、任務與交接，解決了 AI 開發中常見的痛點，如上下文遺失與規劃不一致。
- **核心組件**：
  - **代理**：自包含的 Markdown 檔案（例如在 `bmad-core/agents/` 中），定義如 BMAD Master（監督者）、Scrum Master（規劃）、Dev（編碼）與 QA（測試）等角色。每個檔案包含 YAML 配置，用於定義角色、指令與依賴關係。
  - **模板與標記**：自定義標記語言（定義於 `bmad-core/utils/template-format.md`），用於可重複使用的提示與處理邏輯，實現無需獨立任務的動態文件生成。
  - **配置**：集中於如 `core-config.yaml` 等檔案中，處理 API 金鑰、LLM 整合（例如 OpenAI、Claude）與資源的懶加載，以避免超載。
  - **工作流程**：基於 YAML 的藍圖，透過「故事檔案」（例如用於 PRD 創建、架構設計與迭代開發週期）來排序任務、依賴關係與代理協作。
- **安裝與使用**：透過 Python（需 3.9 以上版本）在項目目錄中設置，創建一個隱藏的 `.bmad-core` 資料夾，包含所有必要組件。可與如 Cursor 或 VS Code 等 IDE 整合，實現無縫的代理互動。
- **可擴展性**：支援用於領域特定代理的「擴展包」（例如基礎設施 DevOps 或遊戲開發），保持核心的通用性與模組化。

該框架託管於 GitHub（bmad-code-org/BMAD-METHOD），並強調使用自然語言而非嚴格的編碼，使其易於個人開發者或擴展至企業的團隊使用。它在 2025 年因「氛圍編碼」與代理敏捷性而獲得關注，儘管部分用戶指出初始 PRD 設置存在學習曲線。如需動手設置，請查閱官方文件或網站 bmadcodes.com。