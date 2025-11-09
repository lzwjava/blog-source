---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Vim 基本指令教學
translated: true
type: note
---

Vim（Vi IMproved 的簡稱）是一款功能強大的模態文字編輯器，亦是許多 Linux 系統（如 Red Hat）的預設編輯器。它完全由鍵盤驅動，掌握基礎後操作極為高效。Vim 有三種主要模式：**Normal 模式**（用於導航與指令，預設模式）、**Insert 模式**（用於輸入文字）及 **Visual 模式**（用於選取文字）。隨時按下 `Esc` 鍵即可返回 Normal 模式。

最推薦的實戰學習方式是於終端機中執行 `vimtutor`——它會啟動互動式教學課程。

## 1. 開啟與關閉 Vim
- 開啟或建立檔案：`vim 檔案名稱.txt`（例如 `vim notes.txt`）
- 不儲存並離開：於 Normal 模式下輸入 `:q!` 後按 Enter
- 退出 Vim：請參閱下方儲存相關說明

## 2. 模式
- **Normal 模式**：預設模式——用於執行指令。按 `Esc` 鍵進入
- **Insert 模式**：按 `i`（游標前插入）或 `a`（游標後附加）進入，底部會顯示 `-- INSERT --`
- **Visual 模式**：按 `v` 選取文字
- **Command-line 模式**：按 `:` 進入（用於儲存、離開、搜尋等操作）

## 3. 導航（於 Normal 模式下）
建議使用以下按鍵替代方向鍵以提升效率：
- `h`：向左移動一個字元
- `j`：向下移動一行
- `k`：向上移動一行
- `l`：向右移動一個字元
- `w`：向前移至下個單詞開頭
- `b`：向後移至上個單詞開頭
- `0`：移至行首
- `$`：移至行尾
- `gg`：移至檔案頂部
- `G`：移至檔案底部
- `:n`：跳至第 n 行（例如 `:5`）
- 可加上數字前綴：`5j`（向下移動 5 行）

啟用行號顯示：`:set number`

## 4. 插入與編輯文字
- 進入 Insert 模式：
  - `i`：游標前插入
  - `I`：行首插入
  - `a`：游標後附加
  - `A`：行尾附加
  - `o`：下方新增一行（進入 Insert 模式）
  - `O`：上方新增一行（進入 Insert 模式）
- 退出 Insert 模式：`Esc`
- 取代單一字元：`r`（接著輸入新字元）
- 復原：`u`
- 重做：`Ctrl + r`
- 重複上個指令：`.`

## 5. 刪除、複製與貼上
- 刪除字元：`x`
- 刪除整行：`dd`
- 刪除指定範圍：`:3,5d`（刪除第 3 至第 5 行）
- 複製（yank）整行：`yy`
- 複製選取文字：於 Visual 模式（`v`）下用方向鍵選取後按 `y`
- 游標後貼上：`p`
- 游標前貼上：`P`
- 選取文字：按 `v`（以字元為單位）後移動游標；按 `Esc` 退出 Visual 模式

## 6. 儲存與離開
- 儲存：`:w`
- 儲存並離開：`:wq` 或 `:x` 或 `ZZ`（連續按兩次大寫 Z）
- 強制儲存並離開：`:wq!`
- 不儲存並離開：`:q!` 或 `ZQ`

## 7. 搜尋
- 向前搜尋：`/pattern`（例如 `/hello`）後按 Enter；按 `n` 尋找下個符合項目
- 向後搜尋：`?pattern`
- 取代：`:%s/old/new/g`（將所有 "old" 取代為 "new"）

## 實用技巧
- 求助：`:help` 或 `:h 關鍵字`
- 分割視窗：`:split 檔案名稱`（水平分割）或 `:vsplit 檔案名稱`（垂直分割）；按 `Ctrl + w w` 切換視窗
- 建議於測試檔案中練習以避免失誤
- 語法突顯：`:syntax on`

以上內容涵蓋了快速編輯檔案所需的核心功能。若需深入瞭解，請查閱 Vim 內的 `:help` 或參考以下資源。

[Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim)  
[Basic Vim Commands](https://www.geeksforgeeks.org/linux-unix/basic-vim-commands/)  
[Vim Cheat Sheet](https://vim.rtorr.com/)