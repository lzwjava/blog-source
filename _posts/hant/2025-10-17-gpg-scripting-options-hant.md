---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 適用於編寫腳本的 GPG 指令選項
translated: true
type: note
---

### GPG 指令選項解說

`--batch`、`--yes`、`-o` 及 `--pinentry-mode` 是 `gpg`（GNU Privacy Guard）指令中常用於非互動式或腳本化操作（如加密、解密或簽署）的標記。以下逐一說明：

- **`--batch`**：啟用批次模式，避免 `gpg` 提出任何互動式問題或允許互動指令。此模式適用於無法提供使用者輸入的腳本或自動化流程，可透過 `--no-batch` 停用。

- **`--yes`**：自動對大多數確認提示（例如覆寫檔案）回答「是」，避免因是非類問題導致執行中斷。

- **`-o`（或 `--output`）**：指定操作的輸出檔案，後方必須接檔名（例如 `-o output.txt`）。若未使用此選項，輸出可能會導向標準輸出或預設位置。

- **`--pinentry-mode`**：控制 GPG 代理程式處理 PIN 碼輸入（通行短語提示）的方式。可接受模式值如 `ask`（預設：彈出圖形或終端機提示）、`loopback`（允許透過 stdin 傳遞通行短語，適用腳本且無彈出視窗）、`cancel`（取消需要 PIN 的操作）或 `error`（傳回錯誤而非提示）。在批次腳本中常搭配 `loopback` 模式，以實現安全且非互動式的通行短語輸入。

這些選項經常在腳本中組合使用，例如 `gpg --batch --yes -o decrypted.txt --pinentry-mode loopback --decrypt encrypted.gpg`，以實現全自動化執行。

#### 參考資料
- [GPG 手冊頁](https://linux.die.net/man/1/gpg)
- [GnuPG 代理程式選項](https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
- [GnuPG 手冊](https://www.gnupg.org/documentation/manuals/gnupg/index.html)