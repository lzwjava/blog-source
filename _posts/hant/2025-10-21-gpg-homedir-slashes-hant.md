---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用正斜線作為 GPG 主目錄
translated: true
type: note
---

### GPG 的 `--homedir` 路徑分隔符在 Git Bash（Windows）中的使用

在 Windows 的 Git Bash 中，**請一律使用正斜線 (`/`)** 作為 `--homedir` 的路徑分隔符。Git Bash 是一個類 Unix 環境（基於 MSYS2），因此它預期使用 POSIX 風格的路徑，並以 `/` 作為分隔符。反斜線 (`\`) 很可能會導致錯誤，因為在此環境中，GPG 無法原生處理未經轉義的反斜線，且這會帶來不必要的麻煩。

#### 為何使用 `/`？
- Git Bash 將 Windows 磁碟機映射為類 Unix 結構：`C:\Users\YourName` 會變成 `/c/Users/YourName`。
- GPG（隨附於 Git for Windows）遵循相同的慣例。使用 `\` 可能導致路徑解析失敗，或需要雙重轉義（例如 `\\`），這容易出錯。
- 官方範例與社群設定（例如用於 Git 簽署）在 Git Bash 中一致使用 `/`。

#### 使用範例
```
gpg --homedir /c/Users/YourName/.gnupg --list-secret-keys
```
- 這指向 C: 磁碟機上的預設 GPG 目錄。
- 若為自訂目錄：`gpg --homedir /d/MyCustomGpgDir --full-generate-key`（D: 磁碟機）。

#### 快速測試
在 Git Bash 中：
1. 執行 `pwd` — 它會輸出類似 `/c/Users/YourName` 的結果（全部使用 `/`）。
2. 嘗試 `gpg --homedir /c/Users/YourName/.gnupg --version`（可正常運作）。
3. 與使用 `\` 的情況比較：`gpg --homedir C:\Users\YourName\.gnupg --version`（會失敗或顯示警告）。

若您同時使用 Windows CMD/PowerShell，這些環境可接受 `/` 與 `\`，但為了保持一致，請在 Git Bash 中堅持使用 `/`。更多資訊請參閱 [GnuPG 手冊中的配置選項](https://www.gnupg.org/documentation/manuals/gnupg/Configuration-Options.html)。