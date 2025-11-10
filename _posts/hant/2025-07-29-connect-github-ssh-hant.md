---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用 SSH 連接 GitHub
translated: true
type: note
---

要使用 SSH 連接 GitHub，請根據 GitHub 官方文件遵循以下步驟。本指南假設您從零開始，包含檢查現有密鑰、生成新密鑰、將其添加到 GitHub 以及測試連接。

### 1. 檢查現有 SSH 密鑰
在創建新 SSH 密鑰之前，請檢查是否已存在密鑰：
- 打開終端機（macOS/Linux）或 Git Bash（Windows）。
- 執行：
  ```bash
  ls -al ~/.ssh
  ```
- 尋找如 `id_rsa` 和 `id_rsa.pub` 的檔案（或類似檔案，例如 `id_ed25519`、`id_ed25519.pub`）。如果存在，您可能已有密鑰。如果想使用現有密鑰，請跳至步驟 3。否則，請繼續生成新密鑰。

### 2. 生成新 SSH 密鑰
如果沒有 SSH 密鑰或需要新密鑰：
- 在終端機中生成新 SSH 密鑰：
  ```bash
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```
  - 將 `your_email@example.com` 替換為與 GitHub 帳戶關聯的電郵。
  - 如果系統不支援 `ed25519`，請使用：
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
- 當提示時，按 Enter 將密鑰保存在默認位置（`~/.ssh/id_ed25519` 或 `~/.ssh/id_rsa`）。
- 可選：輸入密碼短語以增強安全性（或按 Enter 跳過）。

### 3. 將 SSH 密鑰添加到 SSH 代理
SSH 代理管理您的身份驗證密鑰：
- 啟動 SSH 代理：
  ```bash
  eval "$(ssh-agent -s)"
  ```
- 將私鑰添加到代理：
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - 如果使用 RSA，請將 `id_ed25519` 替換為 `id_rsa`。
- 如果設置了密碼短語，系統將提示您輸入。

### 4. 將 SSH 密鑰添加到 GitHub 帳戶
- 將公鑰複製到剪貼簿：
  - 在 macOS：
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - 在 Linux：
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    然後手動複製輸出內容。
  - 在 Windows（Git Bash）：
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - 如果使用 RSA，請將 `id_ed25519.pub` 替換為 `id_rsa.pub`。
- 前往 GitHub：
  - 登入 [GitHub](https://github.com)。
  - 點擊個人頭像（右上角）→ **Settings** → **SSH and GPG keys** → **New SSH key** 或 **Add SSH key**。
  - 在「Key」欄位貼上公鑰，設定標題（例如「我的筆記本電腦」），然後點擊 **Add SSH key**。

### 5. 測試 SSH 連接
驗證 SSH 密鑰是否與 GitHub 正常運作：
- 執行：
  ```bash
  ssh -T git@github.com
  ```
- 如果提示，請輸入 `yes` 確認。
- 您應該看到類似訊息：
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  這表示 SSH 連接正常。

### 6. 配置 Git 使用 SSH
確保 Git 倉庫使用 SSH 進行身份驗證：
- 檢查倉庫的遠端 URL：
  ```bash
  git remote -v
  ```
- 如果 URL 以 `https://` 開頭，請更改為 SSH：
  ```bash
  git remote set-url origin git@github.com:username/repository.git
  ```
  - 將 `username/repository` 替換為您的 GitHub 用戶名和倉庫名稱。

### 7. 可選：管理 SSH 密鑰密碼短語
如果設置了密碼短語，可以配置 SSH 代理以避免重複輸入：
- 在 macOS，將密鑰添加到鑰匙圈：
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- 在 Linux/Windows，SSH 代理通常每個會話只提示一次密碼短語。

### 8. 可選：使用 SSH 代理轉發或部署密鑰
- **SSH 代理轉發**：如果要部署到伺服器，啟用代理轉發以安全使用本地 SSH 密鑰。添加到 `~/.ssh/config`：
  ```bash
  Host example.com
      ForwardAgent yes
  ```
  將 `example.com` 替換為伺服器的主機名稱。
- **部署密鑰**：對於自動化腳本，為每個伺服器生成獨立的 SSH 密鑰，並在 GitHub 倉庫設置中添加為部署密鑰。

### 疑難排解
- 如果 `ssh -T git@github.com` 失敗，請確保：
  - 公鑰已正確添加到 GitHub。
  - SSH 代理正在運行且密鑰已添加（`ssh-add -l` 可列出已加載密鑰）。
  - 檔案權限正確：
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- 如需進一步協助，請查閱 GitHub 的疑難排解指南。

現在您可以使用 SSH 安全地與 GitHub 互動，無需重複輸入憑證。

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)