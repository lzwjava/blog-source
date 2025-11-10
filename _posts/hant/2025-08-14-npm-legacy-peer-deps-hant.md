---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 理解 npm --legacy-peer-deps 標誌
translated: true
type: note
---

### 概述
`--legacy-peer-deps` 標誌是 npm（Node 套件管理器）中的一個選項，用於控制在套件安裝過程中處理同級相依性的方式。同級相依性是指某個套件期望由其他套件提供的相依關係，但在新版本的 npm 中不會自動安裝。

### 行為表現
- **標準 npm (v7+)**：預設情況下會嚴格執行同級相依性要求。如果套件宣告的同級相依性未滿足，npm 會發出警告或中斷安裝以防止衝突。
- **使用 --legacy-peer-deps**：會回退到舊版行為（npm v3~v6），自動安裝缺失的同級相依性，即使可能導致重複或版本不匹配。這能解決某些舊版套件的問題，但可能引發錯誤。

### 使用範例
在終端機中執行：
```
npm install some-package --legacy-peer-deps
```
這通常用於依賴未更新同級相依性宣告的舊版函式庫的專案，常見於 npm 嚴格執行同級相依性處理前的 React 或 Angular 環境。

### 使用時機
請謹慎使用此選項，因為它會繞過安全機制，可能導致相依性地獄。建議優先考慮更新套件或使用 `--force`/`--save-dev` 等更好的替代方案。完整細節請查閱 npm 官方文件中有關同級相依性的說明。