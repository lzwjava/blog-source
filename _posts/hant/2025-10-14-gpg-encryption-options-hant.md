---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG 加密選項詳解
translated: true
type: note
---

### GPG 選項說明

`gpg` 指令（GNU Privacy Guard）是用於加密、解密與金鑰管理的工具。以下將解釋您提到的幾個常用於檔案加密的選項組合：

- **`--homedir <directory>`**：指定 GnuPG 主目錄（預設為 `~/.gnupg`）。此目錄存放金鑰環、設定檔及其他資料。此選項會覆蓋 `GNUPGHOME` 環境變數，適用於將 GPG 操作隔離至自訂位置（例如多設定檔或安全考量）。必須透過命令列提供此參數。

- **`-e`（或 `--encrypt`）**：使用公開金鑰加密技術對輸入資料進行加密。此為非對稱加密的主要模式，資料會以收件者的公開金鑰加密。可與其他選項（如簽署）合併使用。

- **`-r <user-id>`（或 `--recipient <user-id>`）**：指定加密的收件者。`<user-id>` 可以是金鑰 ID、電子郵件或與公開金鑰關聯的名稱。GPG 將使用對應的公開金鑰加密資料。可列出多位收件者進行群組加密。

#### 使用範例
結合這些選項的典型指令如下：
```
gpg --homedir /path/to/custom/dir -e -r recipient@example.com inputfile.txt
```
此指令會使用 `/path/to/custom/dir` 中的金鑰，將 `inputfile.txt` 加密給 `recipient@example.com`，並產生 `inputfile.txt.gpg` 檔案。

如需完整說明，請執行 `gpg --help` 或查閱手冊頁。

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)  
[GPG 速查表](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)  
[Linux 中的 GPG 指令](https://www.tutorialspoint.com/unix_commands/gpg.htm)