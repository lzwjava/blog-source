---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Git 憑證管理員進行 Git Push
translated: true
type: note
---

**標題：使用 Git 憑證管理員與代理設定的無縫 Git Push**

**前言：**

將本地的 Git 變更推送至遠端儲存庫（例如 GitHub）理應是順暢的過程。然而，網路配置（尤其是在使用代理伺服器時）有時會使過程變得複雜。本文將分享我成功推送變更至 `lzwjava.github.io` 儲存庫的經驗，重點說明 Git 憑證管理員 (GCM) 與正確代理設定所扮演的角色。

**情境描述：**

我需要將更新推送至 GitHub 上的 `lzwjava.github.io` 儲存庫。我的系統配置了代理伺服器，這在最初導致了認證問題。

**執行步驟：**

1.  **確認代理設定：**

    * 我首先使用 `git credential-manager` 指令確認代理設定。此指令有助於顯示當前的 HTTP 與 HTTPS 代理配置：

    ```bash
    git credential-manager
    ```

    * 輸出結果顯示：

    ```
    🚀 **偵測到代理設定：**
      - HTTP_PROXY: http://127.0.0.1:7890
      - HTTPS_PROXY: http://127.0.0.1:7890
    ```

    * 這確認了我的代理設定已正確偵測。

2.  **使用 GCM 登入 GitHub：**

    * 為確保 Git 具有正確的憑證，我使用 GCM 登入我的 GitHub 帳戶：

    ```bash
    git credential-manager github login
    ```

    * 此指令開啟了瀏覽器視窗，提示我進行 GitHub 認證。成功認證後，GCM 會安全地儲存我的憑證。

3.  **確認 GitHub 帳戶：**

    * 為確認我的 GitHub 帳戶已正確登入，我執行了以下指令：

    ```bash
    git credential-manager github list
    ```

    * 此指令顯示了我的 GitHub 帳戶名稱。

4.  **設定遠端 URL：**

    * 接著，我驗證並設定了儲存庫的遠端 URL：

    ```bash
    git remote set-url origin https://github.com/lzwjava/lzwjava.github.io.git
    ```

5.  **推送變更：**

    * 最後，我將本地變更推送至遠端儲存庫：

    ```bash
    git push
    ```

    * `git push` 指令成功上傳了我的變更。

6.  **GitHub 安全警示：**

    * 推送完成後，GitHub 顯示了關於我的儲存庫依賴項中存在漏洞的安全警示。這提醒我們必須定期檢查並處理安全問題：

    ```
    remote: GitHub 在 lzwjava/lzwjava.github.io 的預設分支上發現 3 個漏洞（2 個高風險，1 個低風險）。詳情請參閱：
    remote:    https://github.com/lzwjava/lzwjava.github.io/security/dependabot
    ```

**關鍵要點：**

* **Git 憑證管理員 (GCM)：** GCM 透過安全儲存憑證並處理認證工作流程，簡化了 Git 認證過程。
* **代理配置：** 在代理環境下工作時，請確保您的 Git 環境已正確配置以使用代理。GCM 偵測與使用代理設定的能力極為重要。
* **安全警示：** 請密切關注 GitHub 的安全警示，以確保您的儲存庫安全無虞。
* **命令列工具：** 命令列是管理 Git 儲存庫的強大工具。

**結論：**

透過使用 Git 憑證管理員並正確配置代理設定，我成功將變更推送至 GitHub。此經驗凸顯了理解與管理 Git 認證及網路配置的重要性。希望本指南能協助您簡化 Git 工作流程。