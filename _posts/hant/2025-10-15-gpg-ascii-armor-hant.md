---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG ASCII 裝甲詳解
translated: true
type: note
---

在 GPG（GNU Privacy Guard）中，「armor」指的是 ASCII 裝甲格式，這種格式能將二進制的 OpenPGP 資料（如加密檔案、簽章或金鑰）編碼為人類可讀的文字化表示。這對於透過純文字通道（例如電子郵件）傳輸資料非常有用，能避免資料損壞——其原理類似 uuencode 或 base64 編碼，但額外增加了標頭（例如「-----BEGIN PGP MESSAGE-----」）和完整性校驗碼。

您可以在執行指令時透過 `--armor`（或 `-a`）選項啟用此功能，例如加密（`gpg -a -e file.txt`）或匯出金鑰（`gpg --armor --export keyid`）時，指令會以這種裝甲文字格式輸出結果，而非原始二進制資料。

## 參考資料
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)