---
audio: false
generated: true
lang: hant
layout: post
title: GitHub Actions JAR 部署的 SSH 金鑰設定
translated: true
type: note
---

要為 GitHub Actions 生成 SSH 金鑰以部署 JAR 檔案，請遵循以下步驟：

1. **生成 SSH 金鑰對**：
   - 在本地機器或安全環境中執行：
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - 如果系統不支援 Ed25519，請使用：
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - 按 Enter 鍵接受預設檔案位置，並可選擇設定密碼（建議為安全起見）。這將創建兩個檔案：
     - `github-actions-deploy`（私密金鑰）
     - `github-actions-deploy.pub`（公開金鑰）

2. **將公開金鑰添加到目標伺服器**：
   - 複製公開金鑰：
     ```bash
     cat github-actions-deploy.pub
     ```
   - 登入您要部署 JAR 檔案的伺服器。
   - 將公開金鑰附加到伺服器上的 `~/.ssh/authorized_keys`：
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - 確保 `authorized_keys` 檔案具有正確的權限：
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **將私密金鑰儲存在 GitHub Secrets 中**：
   - 前往 GitHub 倉庫：`Settings > Secrets and variables > Actions > Secrets`。
   - 點擊 **New repository secret**。
   - 為秘密命名（例如 `SSH_PRIVATE_KEY`）。
   - 貼上私密金鑰的內容（`github-actions-deploy`）：
     ```bash
     cat github-actions-deploy
     ```
   - 儲存秘密。

4. **配置 GitHub Actions 工作流程**：
   - 創建或編輯工作流程檔案（例如 `.github/workflows/deploy.yml`）。
   - 添加使用 SSH 金鑰部署 JAR 的步驟。以下是示例工作流程：

     ```yaml
     name: Deploy JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # 調整為您的 Java 版本
             distribution: 'temurin'

         - name: Build JAR
           run: mvn clean package # 根據您的建置工具調整（例如 Gradle）

         - name: Install SSH Key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # 請參閱以下說明

         - name: Add Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # 將 <server-ip-or-hostname> 替換為您的伺服器 IP 或主機名

         - name: Deploy JAR to Server
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # 根據您的部署流程調整
     ```

   - **注意事項**：
     - 將 `target/your-app.jar` 替換為您的 JAR 檔案路徑。
     - 將 `user@<server-ip-or-hostname>` 替換為您的伺服器 SSH 用戶和地址。
     - 調整部署指令（例如 `sudo systemctl restart your-service`）以符合您在伺服器上啟動或部署 JAR 的方式。
     - `known_hosts` 步驟對於避免 SSH 主機驗證問題至關重要。如果您知道伺服器的主機金鑰，可以在 `shimataro/ssh-key-action` 步驟中預先填入，或使用如上所示的 `ssh-keyscan`。

5. **保護工作流程安全**：
   - 確保私密金鑰絕不會在日誌或輸出中暴露。
   - 限制倉庫權限以防止未經授權存取秘密。
   - 如果為 SSH 金鑰使用密碼，請將其添加為另一個秘密，並包含在 `shimataro/ssh-key-action` 步驟中：
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **測試工作流程**：
   - 推送變更到 `main` 分支（或工作流程中指定的分支）。
   - 在 GitHub 倉庫的 **Actions** 標籤頁中監控工作流程，確保 JAR 正確建置和部署。

7. **疑難排解**：
   - **Permission denied**：驗證 SSH 金鑰是否正確添加到伺服器的 `authorized_keys`，以及用戶是否有權存取目標目錄。
   - **Host verification failed**：確保 `known_hosts` 步驟已正確配置伺服器的 IP 或主機名。
   - **Build issues**：確認 Java 版本和建置指令與您的專案設定相符。

此設定可安全地將基於 SSH 的部署整合到您的 GitHub Actions 工作流程中，用於部署 JAR 檔案。如果您需要特定調整（例如針對特定伺服器設定或建置工具），請告訴我！