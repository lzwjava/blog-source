---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG 核心概念與操作
translated: true
type: note
---

是的，這種理解 GPG（GnuPG）的高階方式很扎實——它主要圍繞兩個核心領域：

1. **金鑰管理**：包括產生金鑰對（公開/私密）、匯入/匯出金鑰、列出/編輯金鑰、簽署金鑰、撤銷金鑰以及管理信任等級。相關指令如 `gpg --gen-key`、`--import`、`--list-keys` 和 `--edit-key` 負責處理這些操作。

2. **加密/解密（及相關操作）**：涵蓋使用公開金鑰加密檔案或訊息（因此只有收件者能用其私密金鑰解密）、使用私密金鑰解密，以及為確保真實性而進行的簽署/驗證資料。相關指令如 `gpg -e -r user@example.com`（加密）、`gpg -d`（解密）和 `-s`（簽署）都屬於此範疇。

這些功能全都建基於非對稱加密技術（如 RSA 或 ECC 這類公開金鑰系統），但 GPG 也支援對稱加密以應對較簡單的情況。若您想深入鑽研，簽署/驗證功能通常會與加密/解密工作流程結合，以實現端對端安全。

[GNU Privacy Guard 文件](https://gnupg.org/documentation/)