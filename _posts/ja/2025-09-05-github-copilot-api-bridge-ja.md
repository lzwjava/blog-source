---
audio: false
generated: true
image: false
lang: ja
layout: post
title: GitHub Copilot APIブリッジ
translated: true
type: note
---

**ericc-ch/copilot-api** へようこそ。この GitHub プロジェクトは、**GitHub Copilot** を **OpenAI** や **Anthropic** (例: Claude) API と互換性のあるローカル API サーバーに変えます。

以下は、表を使わずにわかりやすく説明したものです。

---

### これは何？

* **GitHub Copilot** を、`/v1/chat/completions`、`/v1/models`、`/v1/embeddings` のような慣れ親しんだ OpenAI スタイルのエンドポイント、あるいは `/v1/messages` のような Anthropic 互換エンドポイントを使って操作できるようにする、**リバースエンジニアリングされたプロキシ**です ([GitHub][1])。

* 本質的に、Claude Code のような OpenAI または Anthropic API をサポートするツールが、バックエンドとして GitHub Copilot を使用できるようになります ([GitHub][1])。

---

### 主な機能

*   **OpenAI & Anthropic 互換性**: 本物の OpenAI または Anthropic API のように動作します ([GitHub][1])。
*   **Claude Code 統合**: `--claude-code` フラグで Claude Code に簡単に接続できます ([GitHub][1])。
*   **使用状況ダッシュボード**: 組み込みの Web インターフェースで Copilot API の使用状況とクォータを監視できます ([GitHub][1])。
*   **レート制限 & 承認制御**: レート制限 (`--rate-limit`)、自動待機 (`--wait`)、手動承認 (`--manual`)、デバッグ (トークン表示) のオプションを含みます。GitHub の濫用検知システムを回避するのに最適です ([GitHub][1])。
*   **様々な Copilot プランに対応**: 個人、Business、Enterprise アカウントのすべてで動作します ([GitHub][1])。

---

### セットアップ & 使用方法

*   **前提条件**: Bun (≥ 1.2.x) と GitHub Copilot のサブスクリプションが必要です ([GitHub][1])。
*   **インストール方法**:

    *   **Docker**:

        ```bash
        docker build -t copilot-api .
        docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
        ```

        または、`GH_TOKEN` 経由で GitHub トークンを直接渡すこともできます ([GitHub][1])。
    *   **npx**:

        ```bash
        npx copilot-api@latest start --port 8080
        ```

        認証のみ行う場合は `npx copilot-api@latest auth` を実行します ([GitHub][1])。
*   **コマンド構造**:

    *   `start`: API サーバーを起動します (必要に応じて認証も処理します)。
    *   `auth`: サーバーを実行せずに GitHub ログインを開始します。
    *   `check-usage`: 現在の Copilot の使用状況をターミナルに出力します。
    *   `debug`: 診断情報 (バージョン、認証ステータスなど) を表示します。オプションで `--json` 出力も可能です ([GitHub][1])。

---

### 実際のフィードバック

Reddit ユーザーからの声:

> 「このプロジェクトは、copilot を openai 互換のエンドポイントに変えることができます。」 ([Reddit][2])
> 「これはあなたの…を作るための素晴らしいプロジェクトです」 ([Reddit][3])

---

### 重要な注意点

*   **非公式 & サポートなし**: これは **公式の GitHub 製品ではなく**、いつでも動作しなくなる可能性があります ([GitHub][1])。
*   **濫用検知のリスク**: 過度または自動化された使用は GitHub の不正利用防止機能をトリガーし、Copilot へのアクセスが停止される可能性があります ([GitHub][1])。
*   **レート制限問題の可能性**: `421 Misdirected Request` のようなエラーの報告があり、メンテナーは調査の間、開発を一時停止しています ([GitHub][4])。

---

### まとめ (表は必要ありません)

*   **何をするものか**: GitHub Copilot を OpenAI/Anthropic API であるかのように公開します。
*   **その重要性**: Claude Code のような、それらの API を想定しているツールで Copilot を利用可能にします。
*   **使い方**: Docker または npx でインストールし、起動、認証、使用状況監視のコマンドを実行します。
*   **注意して進めてください**: 便利ですが非公式であり、GitHub のレート制限やセキュリティ保護機能が大量使用時に問題を引き起こす可能性があります。

---

セットアップのヘルプや、特定のプロジェクトやツールへの統合についてご質問があれば、お知らせください！

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"