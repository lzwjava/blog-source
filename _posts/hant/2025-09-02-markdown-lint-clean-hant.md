---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Markdown 文件一致性校驗與整理
translated: true
type: note
---

以下是 David Anson 為 **markdownlint** 專案提供的簡潔易懂介紹：

---

## 什麼是 **markdownlint**？

**markdownlint** 是一款基於 Node.js 建構的 Markdown/CommonMark 檔案靜態分析工具。其核心目標是對 Markdown 內容實施一致性與風格規則——協助撰寫者維持整潔統一的格式，並避免在不同解析器中可能導致斷裂或渲染不一致的結構（[GitHub][1]）。

此工具靈感源自 Ruby 版本的 markdownlint (markdownlint/mdl)，採用了豐富的檢查規則庫。它運用 micromark 解析器提供 CommonMark 支援，並擴展了 GitHub Flavored Markdown (GFM) 功能，包括表格、自動連結、指令、註腳及數學公式（[GitHub][1]）。

## 主要功能與整合

* **規則涵蓋範圍**：提供全面的內建規則集——從標題樣式、列表縮排到尾隨空格及行長度控制（例如 MD001、MD009、MD013…）（[GitHub][1]）。
* **生態系相容性**：

  * **命令列工具**：

    * `markdownlint-cli` – 傳統 CLI 介面。
    * `markdownlint-cli2` – 更快速、基於配置的 CLI，具靈活格式化選項，支援萬用字元、輸出格式、自動修復及 CI 工作流程整合（[GitHub][2]、[GitHub][3]）。
  * **VS Code 擴充功能**：

    * `vscode‑markdownlint` 為編輯器提供即時檢查功能。違規內容會以行內標示（底線）顯示，並具備懸停提示與快速修復建議（[GitHub][4]）。
  * **GitHub Action**：

    * `markdownlint‑cli2‑action` 可將 markdownlint 嵌入 CI 流程，在 GitHub 工作流程中實現自動檢查（及可選的自動修復）（[GitHub][5]）。

---

## 為何使用它？

* **一致性**：確保 Markdown 檔案遵循既定風格指南，減少專案中的格式偏差。
* **編輯器輔助**：在 VS Code 及其他整合環境中提供行內回饋，使撰寫更流暢高效。
* **自動化**：於 CI 流程中搭配檢查工具或 GitHub Actions，在合併前強制執行標準。
* **可自訂性**：可透過設定檔或行內註解自訂規則集或停用特定規則（例如停用 MD013 以允許長行）（[GitHub][5]、[Software Recommendations Stack Exchange][6]）。

---

是否需要快速入門指南，了解如何透過 npm 安裝設定、使用 VS Code 擴充功能，或整合至 CI 工作流程？

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"