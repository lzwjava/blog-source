---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GnuPG 主目錄內容詳解
translated: true
type: note
---

這些檔案和目錄屬於您的 GnuPG (GPG) 主目錄 (`~/.gnupg/`) 的一部分，該目錄儲存用於加密、簽署和驗證的密碼學金鑰及相關資料。GPG 是實現安全通訊和資料保護的工具。以下是基於標準 GnuPG 2.1+ 行為的詳細說明：

- **openpgp-revocs.d**：一個包含撤銷憑證 (`.rev` 檔案) 的目錄，這些憑證在您建立金鑰對時生成。若金鑰遭洩露或不再需要，可用來撤銷（使失效）您的金鑰，防止其被繼續使用。

- **private-keys-v1.d**：一個以 GnuPG 2.1 引入的現代金鑰格式儲存您私密金鑰的目錄。每個金鑰均儲存在獨立檔案中，以提升安全性和管理便利性。請嚴加保護此目錄——它如同您的數位保險庫。

- **pubring.kbx**：採用新「keybox」格式 (`.kbx`) 的公開金鑰環檔案。它儲存您從他人處匯入的公開金鑰，用於加密發送給對方的訊息或驗證其簽章。

- **pubring.kbx~**：`pubring.kbx` 的自動備份副本，由 GPG 在編輯或更新時建立。波浪號 (`~`) 後綴是 Linux 系統中常見的備份命名慣例。

- **trustdb.gpg**：信任資料庫檔案，用於記錄您為公開金鑰設定的信任等級（例如：對自身金鑰設為「ultimate」，或根據簽章為他人金鑰設定等級）。它協助 GPG 判斷金鑰在驗證過程中是否可靠。

若您近期曾生成或匯入金鑰，此目錄結構屬正常現象。請務必安全地備份整個 `~/.gnupg/` 目錄，且切勿分享私密金鑰。更多詳細資訊，請查閱官方 GnuPG 文件。

[使用 GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg.pdf)  
[GnuPG 第二部分 - 建立與管理金鑰](https://www.hacksanity.com/kb/gnupg-create-manage-keys/)  
[如何在 Linux 上備份與還原 GPG 金鑰](https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/)  
[GPG(1) 手冊](https://www.gnupg.org/(en)/documentation/manuals/gnupg24/gpg.1.html)