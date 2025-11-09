---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: GPG 密鑰管理基礎
translated: true
type: note
---

## GPG 金鑰管理簡介

GPG（GNU Privacy Guard）是 OpenPGP 標準的免費實作，用於安全通訊、加密、簽署及驗證資料。其核心是**公開金鑰加密**，每位使用者擁有**公開金鑰**（公開分享用於加密與驗證）和**私密金鑰**（秘密保存用於解密與簽署）。金鑰管理涉及創建、分發、維護與保護這些金鑰，以防篡改、洩露或濫用。管理不當可能導致金鑰替換等攻擊，即攻擊者替換您的金鑰以攔截通訊。

GPG 的「信任網」模型讓使用者能相互認證金鑰，建立驗證身分的網絡。金鑰儲存於**金鑰環**（公開與私密檔案，例如舊版中的 `pubring.kbx` 和 `secring.gpg`，或新版中統一管理）。請務必備份私密金鑰並使用高強度密碼。

## 金鑰結構

GPG 金鑰對不單單是一把金鑰——它是一個組合：
- **主金鑰**：用於認證（簽署）其他金鑰及自我簽署金鑰元件的核心簽署金鑰（例如 RSA 或 DSA）。
- **子金鑰**：用於特定任務的附屬金鑰：
  - 簽署子金鑰：用於簽署訊息。
  - 加密子金鑰：用於加密資料（通常定期輪換）。
  - 認證子金鑰：用於 SSH 或類似用途。
- **使用者識別碼 (UID)**：如「Alice (註解) <alice@example.com>」的字串，將金鑰與真實身分連結。可存在多個 UID 對應不同角色。
- **自我簽章**：主金鑰簽署自身元件以防篡改。

以互動方式檢視金鑰結構：
```
gpg --edit-key <金鑰識別碼或電郵>
```
在選單內使用 `check` 驗證自我簽章，或 `toggle` 檢視私密部分（如有權限）。

## 產生金鑰

從主金鑰對開始。初學者建議使用互動方式：

1. 執行 `gpg --full-gen-key`（或 `--gen-key` 使用預設值）。
2. 選擇金鑰類型（預設：RSA，同時用於簽署與加密）。
3. 選擇金鑰長度（例如 4096 位元以增強安全性；建議至少 2048）。
4. 設定到期日（例如 1y 為一年；「0」為永不過期——盡量避免無限期）。
5. 輸入使用者識別碼（姓名、電郵）。
6. 設定高強度密碼（20+ 字元，混合大小寫/符號）。

快速產生（非互動式）：
```
gpg --quick-generate-key "Alice <alice@example.com>" rsa default 1y
```

產生後，建立**撤銷憑證**（用於金鑰洩露時使其失效的檔案）：
```
gpg --output revoke.asc --gen-revoke <您的金鑰識別碼>
```
安全儲存此憑證（例如列印存放於保險庫）——需使用前勿分享。

後續新增子金鑰或 UID：
- 進入 `gpg --edit-key <金鑰識別碼>`，然後使用 `addkey`（新增子金鑰）或 `adduid`（新增 UID）。這些將自動獲得自我簽署。

## 列出與檢視金鑰

- 列出公開金鑰：`gpg --list-keys`（或 `--list-public-keys`）。
- 列出私密金鑰：`gpg --list-secret-keys`。
- 詳細檢視：`gpg --list-keys --with-subkey-fingerprint <金鑰識別碼>`（顯示子金鑰指紋）。

輸出顯示金鑰識別碼（短/長格式）、建立/到期日期、功能（例如 `[SC]` 表示簽署/認證）及 UID。

## 匯出與匯入金鑰

**匯出**用於分享公開金鑰或備份私密金鑰：
- 公開金鑰：`gpg --armor --export <金鑰識別碼> > mykey.asc`（ASCII 編碼方便電郵傳送）。
- 私密金鑰（僅備份）：`gpg --armor --export-secret-keys <金鑰識別碼> > private.asc`。
- 上傳至金鑰伺服器：`gpg --keyserver hkps://keys.openpgp.org --send-keys <金鑰識別碼>`。

**匯入**將他人金鑰加入您的公開金鑰環：
- `gpg --import <檔案.asc>`（與現有合併；新增簽章/子金鑰）。
- 從金鑰伺服器：`gpg --keyserver hkps://keys.openpgp.org --recv-keys <金鑰識別碼>`。

匯入後，使用 `gpg --edit-key <金鑰識別碼>` 及 `check` 驗證自我簽章。

## 簽署與認證金鑰

建立信任關係：
- 簽署金鑰（認證其有效性）：`gpg --sign-key <他人金鑰識別碼>`（或 `lsign-key` 僅限本地）。
- 快速簽署：`gpg --quick-sign-key <指紋> "使用者識別碼"`。
- 設定信任等級：在 `--edit-key` 中使用 `trust`（例如「5」為絕對信任）。

這會在金鑰上建立簽章，於清單中可見。信任網根據您對簽署者的信任計算有效性。

## 撤銷金鑰

撤銷使金鑰或元件失效而不刪除，確保他人知悉其無效：
- 完整金鑰：匯入您的撤銷憑證：`gpg --import revoke.asc`，然後匯出/傳送更新後的金鑰。
- 子金鑰/UID：在 `--edit-key` 中，用 `key 1` 或 `uid 1` 選擇，然後使用 `revkey` 或 `revuid`。
- 快速撤銷 UID：`gpg --quick-revoke-uid <金鑰識別碼> <欲撤銷的 UID>`。

撤銷原因：洩露、停用、被取代。請務必發布已撤銷的金鑰。

## 最佳實踐

- **安全性**：使用硬體權杖（例如 YubiKey）儲存私密金鑰。每年輪換加密子金鑰（`gpg --quick-add-key <指紋> rsa encr 1y`）。定期更改密碼（`gpg --change-passphrase <金鑰識別碼>`）。
- **到期日**：設定合理到期日（1-2 年）以強制更新並偵測洩露。
- **分發**：透過金鑰伺服器或直接分享公開金鑰；當面或經可信管道驗證指紋以防中間人攻擊。
- **備份**：將私密金鑰匯出至加密儲存。立即產生撤銷憑證。
- **清理**：使用 `gpg --edit-key` 的 `clean` 移除無效簽章。
- **更新**：截至 2025 年，GnuPG 2.5+ 支援抗量子演算法（例如 `--quick-generate-key ... pqc`）；考慮遷移以確保未來相容性。
- **常見陷阱**：切勿分享私密金鑰。避免無限期到期日。在沙箱環境測試撤銷流程。

實作練習可在測試目錄使用 `gpg --homedir ./test-gpg` 進行。

[GnuPG 手冊：金鑰管理](https://www.gnupg.org/gph/en/manual/c235.html)  
[GNU Privacy Guard 手冊：OpenPGP 金鑰管理](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html)  
[GnuPG 入門指南](https://www.gnupg.org/gph/en/manual/c14.html)