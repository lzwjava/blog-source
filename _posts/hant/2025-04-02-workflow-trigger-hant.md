---
audio: false
generated: true
lang: hant
layout: post
title: 觸發您的 GitHub 工作流程
translated: true
type: note
---

你說得對，在前端程式碼中直接嵌入 GitHub token 確實存在安全風險。任何查看你頁面原始碼的人都有可能取得並濫用你的 token。

以下是你可以在前端按鈕中安全觸發 GitHub workflow 的方法，包含解釋和程式碼範例：

**核心概念：引入安全的後端**

最安全的處理方式是引入後端元件（一個 API 端點），它將：

1. **接收來自前端的觸發請求**
2. **安全儲存並使用你的 GitHub token**
3. **向 GitHub 發送經過身份驗證的 API 呼叫來觸發你的 workflow**

這樣，你敏感的 GitHub token 就永遠不會離開你的伺服器端環境。

以下是幾種後端選項：

**1. 無伺服器函數（例如 AWS Lambda、Google Cloud Functions、Netlify Functions、Vercel Functions）**

對於簡單的 API 端點來說，這通常是一個輕量且經濟高效的解決方案。

* **運作方式：** 你編寫一個小函數，部署到無伺服器平台。該函數將包含使用你儲存的 token 呼叫 GitHub API 的邏輯。你的前端按鈕隨後將向此無伺服器函數的 URL 發送 HTTP 請求。

* **範例（概念性 - 你需要根據所選平台進行調整）：**

    **無伺服器函數程式碼（Python - AWS Lambda/API Gateway 範例）：**

    ```python
    import os
    import requests
    import json

    def handler(event, context):
        github_token = os.environ.get("GITHUB_TOKEN")
        if not github_token:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'GitHub token not configured'})
            }

        owner = "lzwjava"
        repo = "lzwjava.github.io"
        workflow_id = "nytimes.yml"
        ref = "main"
        api_url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"

        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {github_token}',
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json'
        }
        payload = {'ref': ref}

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            return {
                'statusCode': 204,
                'body': ''
            }
        except requests.exceptions.RequestException as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'Failed to trigger workflow: {e}'})
            }
    ```

    * **重要：** 你需要在無伺服器平台中配置環境變數（例如 `GITHUB_TOKEN`）來安全儲存你的 GitHub Personal Access Token。

    **前端程式碼（修改後的 `nytimes.js`）：**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // Netlify Functions 範例

    if (nytimesDiv) {
        const updateButton = document.createElement('button');
        updateButton.textContent = 'Update NYTimes Articles';
        nytimesDiv.appendChild(updateButton);

        updateButton.addEventListener('click', () => {
            fetch(backendApiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}) // 對於簡單的觸發，你可能不需要請求體
            })
            .then(response => {
                if (response.status === 204) {
                    alert('Update triggered successfully! Please wait a few minutes to see the result.');
                } else {
                    return response.json().then(data => {
                        alert(`Update failed. Status code: ${response.status}: ${data.error || 'Unknown error'}`);
                        console.error('Update failed:', response, data);
                    });
                }
            })
            .catch(error => {
                alert('Update failed. Check the console for errors.');
                console.error('Error triggering update:', error);
            });
        });
    } else {
        console.error("nytimes div not found!");
    }
    ```

* **部署：** 你需要將此無伺服器函數部署到你選擇的平台。具體的部署過程因供應商而異。

**2. 你自己的 Web 伺服器（如果你有的話）**

如果你有自己的 Web 伺服器（例如使用 Node.js、Python/Flask 等），你可以在該伺服器上創建一個簡單的 API 端點。

* **運作方式：** 你的前端按鈕向你的伺服器端點發送請求。你的伺服器端程式碼（可以安全存取你的 GitHub token，該 token 作為環境變數或配置檔案儲存）然後向 GitHub 發出 API 呼叫。

* **範例（概念性 - Node.js with Express）：**

    **伺服器端程式碼（Node.js/Express）：**

    ```javascript
    const express = require('express');
    const fetch = require('node-fetch');
    require('dotenv').config();

    const app = express();
    const port = 3000;

    app.post('/api/trigger-nytimes-update', async (req, res) => {
        const githubToken = process.env.GITHUB_TOKEN;
        if (!githubToken) {
            return res.status(500).json({ error: 'GitHub token not configured' });
        }

        const owner = "lzwjava";
        const repo = "lzwjava.github.io";
        const workflow_id = "nytimes.yml";
        const ref = "main";
        const apiUrl = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow_id}/dispatches`;

        const headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': `Bearer ${githubToken}`,
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json'
        };
        const payload = { ref: ref };

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(payload)
            });
            if (response.status === 204) {
                res.sendStatus(204);
            } else {
                const data = await response.json();
                res.status(response.status).json({ error: `Failed to trigger workflow: ${JSON.stringify(data)}` });
            }
        } catch (error) {
            console.error('Error triggering workflow:', error);
            res.status(500).json({ error: `Failed to trigger workflow: ${error.message}` });
        }
    });

    app.listen(port, () => {
        console.log(`Server listening at http://localhost:${port}`);
    });
    ```

    * **重要：** 使用 `.env` 檔案（並確保它不會提交到你的程式庫）來儲存你的 `GITHUB_TOKEN`，並使用像 `dotenv` 這樣的程式庫來讀取它。

    **前端程式碼（修改後的 `nytimes.js`）：**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // 調整為你伺服器的端點

    // ... (其餘前端程式碼與無伺服器函數範例類似)
    ```

* **部署：** 你需要將你的伺服器應用程式部署到你的 Web 伺服器。

**3. 由不同事件觸發的 GitHub Actions Workflow（較不直接）**

雖然不是直接的按鈕觸發，但你可以設定不同的事件來觸發你的 workflow，這可能間接由用戶操作啟動。例如：

* **排程 Workflow：** 定期（例如每天）執行更新 workflow。
* **Webhook 觸發：** 如果你有另一個用戶與之互動的系統或服務，該系統可以觸發一個 webhook，然後啟動你的 GitHub Actions workflow。

然而，這些選項無法提供你期望透過按鈕點擊實現的即時、按需更新。

**選擇合適的方法**

* **對於簡單的靜態網站：** 無伺服器函數通常是最簡單且最經濟高效的解決方案。像 Netlify 和 Vercel 這樣的平台內建支援無伺服器函數。
* **如果你已經有 Web 伺服器：** 在現有伺服器上創建 API 端點是一個自然的選擇。
* **安全性至關重要：** 始終優先考慮將你的 GitHub token 安全地保存在後端伺服器上，切勿在前端程式碼中暴露它。

**實施步驟（以使用無伺服器函數為例）：**

1.  **創建無伺服器函數：** 編寫無伺服器函數的程式碼（例如使用 Python 或 Node.js），其中包含呼叫 GitHub API 的邏輯。
2.  **安全儲存你的 GitHub Token：** 在無伺服器平台的設定中配置環境變數來儲存你的 GitHub Personal Access Token。
3.  **部署你的無伺服器函數：** 將函數部署到你選擇的平台（例如 Netlify、Vercel、帶有 API Gateway 的 AWS Lambda）。你將獲得已部署函數的 URL。
4.  **更新你的前端程式碼：** 修改你的 `nytimes.js` 檔案，使其在按鈕被點擊時向已部署的無伺服器函數的 URL 發送 `POST` 請求。
5.  **測試：** 部署你更新的前端，並測試點擊按鈕是否成功觸發你的 GitHub Actions workflow。

通過實施這些基於後端的解決方案之一，你可以提供一個按鈕來安全地觸發你的 GitHub workflow，而不會在前端程式碼中暴露你敏感的 API token。請記住選擇最適合你當前基礎設施和技術技能的方法。