---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 紅帽Linux的Vi編輯器基礎
translated: true
type: note
---

Vi 是一款功能強大、鍵盤驅動的文字編輯器，是 Linux 系統（包括 Red Hat Enterprise Linux (RHEL)）的標準配備。它輕量且高效，適合編輯配置檔案、腳本等。在 Red Hat 中，`vi` 命令通常指向 `vim`（Vi IMproved），後者增加了語法高亮等功能。本指南為初學者介紹基礎操作。

## 安裝
Vi 已預裝在大多數 Red Hat 系統上。如需完整的 `vim` 套件（或系統中缺少），可透過套件管理器安裝：

- 適用於 RHEL 7/8：  
  ```
  sudo yum install vim
  ```

- 適用於 RHEL 9+：  
  ```
  sudo dnf install vim
  ```

安裝後，`vi` 和 `vim` 可互換使用。

## 啟動 Vi
1. 開啟終端機。
2. 執行 `vi filename.txt`（將 `filename.txt` 替換為你的檔案路徑）。  
   - 若檔案存在，會開啟以供編輯。  
   - 若不存在，會建立新的空白檔案。  
3. 若想不指定檔案開啟（用於練習）：`vi`。  
Vi 會以**命令模式**啟動（預設模式）。你將看到空白畫面或檔案內容，且游標位於左上角。

## 理解模式
Vi 有三種主要模式——切換模式是關鍵：
- **命令模式**：預設模式，用於導覽、刪除及大多數操作。按 `Esc` 可從其他模式進入或返回此模式。
- **插入模式**：用於輸入/編輯文字。從命令模式進入（例如按 `i`）。
- **Ex 模式**：用於進階指令（如儲存）。在命令模式下輸入 `:` 進入。

指令區分大小寫。可前綴數字重複操作（例如 `3dd` 會刪除 3 行）。

## 基礎導覽（命令模式下）
使用 Home 列按鍵進行游標移動——無需滑鼠：
- `h`：向左一個字元
- `j`：向下一行
- `k`：向上一行
- `l`：向右一個字元
- `w`：向前一個單詞
- `b`：向後一個單詞
- `0`（零）：行首
- `$`：行尾
- `gg`：檔案頂部
- `G`：檔案底部
- `Ctrl + F`：向下翻頁
- `Ctrl + B`：向上翻頁

## 進入插入模式與編輯
從命令模式按下以下按鍵之一，切換到插入模式並開始輸入：
- `i`：在游標前插入
- `I`：在行首插入
- `a`：在游標後附加
- `A`：在行尾附加
- `o`：在下方新增一行
- `O`：在上方新增一行

退出插入模式：按 `Esc`（返回命令模式）。

常用編輯指令（命令模式下）：
- **刪除**：
  - `x`：刪除游標下的字元
  - `X`：刪除游標前的字元
  - `dd`：刪除當前行
  - `dw`：刪除當前單詞
  - `D`：刪除至行尾
- **複製（Yank）**：
  - `yy`：複製當前行
  - `y`：複製選取內容（需先按 `v` 選取）
- **貼上**：
  - `p`：貼到游標後
  - `P`：貼到游標前
- **復原**：
  - `u`：復原上一個變更
  - `U`：復原當前行所有變更
- **重複**：`.`（重複上一個指令）

## 儲存與退出
這些是 **Ex 指令**——在命令模式下輸入 `:`，接著輸入指令，然後按 `Enter`：
- `:w`：儲存（寫入）變更
- `:q`：退出（若無變更）
- `:wq` 或 `ZZ`（命令模式下）：儲存並退出
- `:q!`：不儲存退出（強制捨棄變更）
- `:w filename`：另存新檔

若操作卡住，`:q!` 可安全退出。

## 搜尋與替換
- 向前搜尋：`/pattern`（例如 `/error`），接著按 `n` 找下一個符合項，`N` 找上一個。
- 向後搜尋：`?pattern`。
- 全部替換：`:%s/old/new/g`（全域替換；加入 `c` 可確認，例如 `:%s/old/new/gc`）。

## 給 Red Hat 用戶的提示
- 在 `~/.vimrc` 中自訂（若不存在請建立）：  
  ```
  set number          # 顯示行號
  syntax on           # 語法高亮
  set tabstop=4       # Tab 寬度
  set autoindent      # 自動縮排
  ```
  使用 `vi ~/.vimrc` 編輯，加入設定後 `:wq` 儲存。
- 處理多個檔案：`vi file1.txt file2.txt`，用 `:n`（下一個）或 `:prev`（上一個）切換。
- 在測試檔案中練習，避免在系統檔案中出錯。

Vi 需要練習，但會逐漸變得直覺。從簡單操作開始，並經常使用 `Esc`！

## 參考資料
[How to get started with the Vi editor - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[LFCS #2: How to Install and Use Vi/Vim as a Full Text Editor in Linux](https://www.tecmint.com/vi-editor-usage/)  
[vi Editor in Linux - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/vi-editor-unix/)