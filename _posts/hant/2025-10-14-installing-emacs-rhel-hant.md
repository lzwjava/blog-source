---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在RHEL上安裝Emacs
translated: true
type: note
---

### 在 Red Hat Enterprise Linux 上安裝 Emacs

Red Hat Enterprise Linux (RHEL) 主要使用 DNF 套件管理工具來安裝軟體。Emacs 在預設軟體庫中即可取得，因此安裝過程相當簡單。以下是適用於現代版本（RHEL 8 及更新版本）的步驟。若為舊版（例如 RHEL 7），請將 `dnf` 替換為 `yum`。

#### 必要條件
- 確保您擁有 root 權限（使用 `sudo`）。
- 若使用官方 RHEL 軟體庫，您的系統應已註冊 Red Hat Subscription Management。

#### 安裝步驟
1. **更新套件快取**（建議執行以確保取得最新可用版本）：  
   ```
   sudo dnf update
   ```

2. **安裝 Emacs**：  
   ```
   sudo dnf install emacs
   ```  
   這將安裝軟體庫中可用的最新穩定版本（例如 Emacs 28.x 或 29.x，具體取決於您的 RHEL 版本）。

3. **驗證安裝**：  
   執行以下指令檢查版本：  
   ```
   emacs --version
   ```  
   您應該會看到類似 `GNU Emacs 28.2`（或相近版本）的輸出。

#### 注意事項
- 若您使用舊版 RHEL 並採用 YUM（例如 RHEL 7），指令應改為 `sudo yum install emacs`。
- 若要取得最新版 Emacs（例如 29+），您可能需要從原始碼編譯或使用第三方軟體庫（如 EPEL），因為基礎軟體庫的版本可能較舊。
- 若要啟動 Emacs，只需在終端機中輸入 `emacs`。

[GNU Emacs 常見問題：安裝 Emacs](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[Red Hat 文件：使用 DNF 管理軟體](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)