---
audio: false
generated: true
lang: ja
layout: post
title: GitHubワークフローをトリガー
translated: true
type: note
---

おっしゃる通り、GitHubトークンをフロントエンドコードに直接埋め込むことはセキュリティリスクがあります。ページのソースコードを閲覧できる誰もが、あなたのトークンにアクセスして悪用する可能性があります。

以下は、フロントエンドのボタンからGitHubワークフローを安全にトリガーするためのアプローチと、その説明、コード例です：

**核となるアイデア：安全なバックエンドの導入**

最も安全な方法は、バックエンドコンポーネント（APIエンドポイント）を導入することです。これにより：

1. **フロントエンドからのトリガーリクエストを受け取る**
2. **GitHubトークンを安全に保存・使用する**
3. **認証済みのAPIコールをGitHubに対して行い、ワークフローをディスパッチする**

この方法では、機密性の高いGitHubトークンがサーバーサイド環境から出ていくことはありません。

以下に、バックエンドの選択肢をいくつか示します：

**1. サーバーレス関数（例：AWS Lambda、Google Cloud Functions、Netlify Functions、Vercel Functions）**

これは、このような単純なAPIエンドポイントに対して、軽量かつコスト効率の良いソリューションとなることが多いです。

* **仕組み：** サーバーレスプラットフォームにデプロイされる小さな関数を書きます。この関数には、保存されたトークンを使用してGitHub APIを呼び出すロジックが含まれます。フロントエンドのボタンは、このサーバーレス関数のURLに対してHTTPリクエストを行います。

* **例（概念的なもの - 選択したプラットフォームに合わせて調整する必要があります）：**

    **サーバーレス関数コード（Python - AWS Lambda/API Gatewayの例）：**

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
            response.raise_for_status()  # 異常なステータスコードに対して例外を発生させる
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

    * **重要：** サーバーレスプラットフォームの環境変数（例：`GITHUB_TOKEN`）を設定して、GitHub Personal Access Tokenを安全に保存します。

    **フロントエンドコード（修正された `nytimes.js`）：**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // Netlify Functionsの例

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
                body: JSON.stringify({}) // 単純なトリガーの場合、ボディは必要ないかもしれません
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

* **デプロイ：** このサーバーレス関数を選択したプラットフォームにデプロイする必要があります。具体的なデプロイプロセスはプロバイダによって異なります。

**2. 独自のWebサーバー（既にお持ちの場合）**

独自のWebサーバー（例：Node.js、Python/Flaskなどを使用）をお持ちの場合、そのサーバー上に簡単なAPIエンドポイントを作成できます。

* **仕組み：** フロントエンドのボタンがあなたのサーバーのエンドポイントにリクエストを送信します。GitHubトークンへのアクセス権を持つ（環境変数または設定ファイルとして安全に保存された）サーバーサイドコードが、GitHubへのAPIコールを実行します。

* **例（概念的なもの - Node.js with Express）：**

    **サーバーサイドコード（Node.js/Express）：**

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

    * **重要：** `.env`ファイルを使用し（そしてそれがリポジトリにコミットされないようにしてください）、`dotenv`のようなライブラリを使用して`GITHUB_TOKEN`にアクセスします。

    **フロントエンドコード（修正された `nytimes.js`）：**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // あなたのサーバーのエンドポイントに調整

    // ... (フロントエンドコードの残りはサーバーレス関数の例と同様)
    ```

* **デプロイ：** サーバーアプリケーションをWebサーバーにデプロイする必要があります。

**3. 別のイベントによってトリガーされるGitHub Actionsワークフロー（直接性に欠ける）**

ボタンの直接的なトリガーではありませんが、ユーザーアクションによって間接的に開始される可能性のある別のイベントを設定してワークフローをトリガーすることもできます。例えば：

* **スケジュールされたワークフロー：** 定期的に（例：毎日）更新ワークフローを実行する。
* **Webhookトリガー：** ユーザーが操作する別のシステムやサービスがある場合、そのシステムがWebhookをトリガーし、それがあなたのGitHub Actionsワークフローを開始する。

しかし、これらのオプションは、ボタンクリックから得られるような即時のオンデマンド更新を提供するものではありません。

**適切なアプローチの選択**

* **シンプルな静的サイトの場合：** サーバーレス関数が最も簡単でコスト効率の良いソリューションであることが多いです。NetlifyやVercelのようなプラットフォームはサーバーレス関数を組み込みでサポートしています。
* **既にWebサーバーをお持ちの場合：** 既存のサーバー上にAPIエンドポイントを作成するのが自然な選択です。
* **セキュリティが最優先：** GitHubトークンをバックエンドサーバー上で安全に保ち、フロントエンドコードで決して公開しないことを常に優先してください。

**実装の手順（サーバーレス関数を例として）：**

1.  **サーバーレス関数の作成：** GitHub APIを呼び出すロジックを含むサーバーレス関数のコードを（例：PythonまたはNode.jsで）書きます。
2.  **GitHubトークンの安全な保存：** サーバーレスプラットフォームの設定で環境変数を設定し、GitHub Personal Access Tokenを保存します。
3.  **サーバーレス関数のデプロイ：** 関数を選択したプラットフォーム（例：Netlify、Vercel、API Gatewayを備えたAWS Lambda）にデプロイします。デプロイされた関数のURLを取得します。
4.  **フロントエンドコードの更新：** `nytimes.js`ファイルを修正し、ボタンがクリックされたときにデプロイされたサーバーレス関数のURLに対して`POST`リクエストを行うようにします。
5.  **テスト：** 更新されたフロントエンドをデプロイし、ボタンをクリックしてGitHub Actionsワークフローが正常にトリガーされるかテストします。

これらのバックエンドベースのソリューションのいずれかを実装することで、機密性の高いAPIトークンをフロントエンドコードに公開することなく、GitHubワークフローを安全にトリガーするボタンを提供できます。現在のインフラストラクチャと技術スキルに最も適したアプローチを選択することを忘れないでください。