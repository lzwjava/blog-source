---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: macOS 與 Linux 的 Unix 傳承
translated: true
type: note
---

### macOS 與 Linux 的共同起源

macOS（前身為 OS X）與 Linux 在概念上皆源自 Unix——這個由貝爾實驗室於 1970 年代開發的開創性多工作業系統。Linux 由 Linus Torvalds 於 1991 年創建，是一個仿照 Unix 但獨立開發的開源核心（並非衍生自 Unix 原始碼）。而 macOS 則建基於 Darwin（蘋果公司基於 FreeBSD 開發的類 Unix 作業系統），其中包含 Unix 組件並獲 The Open Group 認證為符合 Unix 標準。這種同源血緣解釋了兩者在工具與指令上的諸多相似性，因其皆旨在提供類 Unix 功能。

佐證依據：Unix 標準（如 POSIX）影響了這兩套系統以確保相容性。像 Ubuntu 這類 Linux 發行版明確屬於類 Unix 系統，而 macOS 則透過 BSD（柏克萊軟體套件）繼承了 Unix 工具。

### 為何兩者皆具備 'ps' 指令

'ps'（process status）指令用於顯示執行中行程的資訊，其起源可直接追溯至 1970 年代首次實作於 Unix 的設計。macOS 與 Linux 皆包含 'ps' 的原因在於：
- 這屬於其 Unix 血緣的一部分：macOS 透過 Darwin/FreeBSD 繼承，Linux 則透過 PROC 檔案系統及 GNU 或 POSIX 規範的標準工具集繼承
- 該指令對系統診斷、腳本編寫與管理至關重要，因此預設被納入核心工具集（如 macOS 的 Terminal 或 Linux 的 shell）

雖然選項可能存在細微差異（例如 macOS 採用 BSD 風格旗標，Linux 則常用 GNU 變體），但像 `ps -p pid -o pid,ppid,lstart,etime,command` 這類指令語法在兩系統皆受支援，這正是源自 POSIX 標準的共同傳承。此非巧合，而是直接承襲自 Unix 的脈絡。

### 能否稱 macOS 與 Linux 同屬 Unix？

嚴格來說並不完全正確：「Unix」是作業系統家族與註冊商標。macOS 符合 Unix 資格，因為 Darwin 獲 The Open Group 認證且符合 Single Unix Specification (SUS)。然而 Linux 作為核心構成了完整作業系統（如 Debian 等發行版）的基礎，但其核心本身及發行版並非官方認定的「Unix」——由於缺乏完整認證或共用程式碼庫，它們僅因遵循 POSIX 標準而被歸類為類 Unix 或 Unix 相容系統。

或可稱其為「類 Unix 系統」或「承載 Unix 傳統的系統」，但將 Linux 統稱為「Unix」並不精準。實務上對多數使用者影響不大，因為在執行 'ps' 等指令時行為表現相似。若需嚴格區分，請查閱認證狀態或參考官方定義。