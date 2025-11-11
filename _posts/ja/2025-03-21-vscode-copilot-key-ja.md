---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio Code (VSCode) Copilot プラグイン
translated: true
type: note
---

いいえ、Visual Studio Code（VSCode）のCopilotプラグインは、GeminiキーのようなカスタムAPIキーを使用することはできません。GitHub Copilotは、GitHub（Microsoft傘下）によって開発されたAI搭載のコード補完ツールであり、GitHubのインフラストラクチャと特定のAIモデル（元々はOpenAIのCodexを基盤としていました）に密接に統合されています。CopilotはGitHubアカウントとCopilotサブスクリプションによる認証に依存しており、GoogleのGeminiのような他のプロバイダーからのカスタムAPIキーで設定する組み込みオプションは提供していません。

ただし、Geminiキーをお持ちの場合、VSCode内でそれを活用する代替方法があります：

- **Gemini Code Assist**: Googleは、Gemini Code Assistと呼ばれるAI搭載のコーディングアシスタントを提供しており、VSCode用の公式拡張機能があります。この拡張機能はGoogleのGeminiモデルで動作するように設計されており、認証のためにGemini APIキーを入力できる可能性が高いです。この拡張機能をVSCode Marketplaceからインストールし、キーを設定することで、Geminiを利用したコード補完を利用できます。

- **サードパーティ製プラグイン**: Marketplaceには、複数のAIプロバイダーをサポートし、Gemini用のものを含むカスタムAPIキーの使用を可能にする他のサードパーティ製VSCode拡張機能も存在する可能性があります。これらのプラグインを使用すると、コード提案のためにGemini APIに接続できますが、追加の設定が必要になる場合があります。

### Copilotがカスタムキーをサポートしない理由
GitHub Copilotは、独自のエコシステムに最適化されたプロプライエタリなツールです。最近の展開では、GitHubがGoogleと提携してCopilotにGeminiモデルを統合していますが、この統合はGitHubによって管理されており、ユーザーが自身のGemini APIキーを直接入力することはできません。代わりに、（利用可能な場合はGeminiを含む）サポートされるモデルへのアクセスは、GitHubの管理下にあるCopilotサービス自体を通じて提供されます。

### 実用的な推奨事項
VSCodeでGeminiキーを使用することが目標である場合、**Gemini Code Assist拡張機能をインストールする**ことが最も直接的で公式にサポートされたオプションです。以下の手順で進めることができます：

1.  VSCodeを開きます。
2.  拡張機能ビューに移動します（`Ctrl+Shift+X` または macOSでは `Cmd+Shift+X`）。
3.  「Gemini Code Assist」を検索します（または正確な名前についてはGoogleの公式ドキュメントを確認してください）。
4.  拡張機能をインストールし、セットアップ手順に従ってGemini APIキーを入力します。

このアプローチにより、意図された方法でツールを使用でき、利用規約違反の可能性やCopilotへのサポートされていない変更に伴う問題を回避できます。

まとめると、VSCode Copilotプラグイン自体はGeminiキーを使用できませんが、Gemini Code Assist拡張機能または互換性のあるサードパーティ製プラグインを選択することで、VSCodeでGeminiを使用するという目標を達成できます。