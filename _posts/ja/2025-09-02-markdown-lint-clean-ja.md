---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 整合されたクリーンファイルのためのマークダウンリンティング
translated: true
type: note
---

以下は、David Ansonによる **markdownlint** プロジェクトの、読みやすく整理された紹介です。

---

## **markdownlint** とは？

**markdownlint** は、Node.js上に構築されたMarkdown/CommonMarkファイル用の静的解析ツールです。その中核的な目的は、Markdownコンテンツ全体で一貫性とスタイルルールを強制することにあります。これにより、執筆者は清潔で統一されたフォーマットを維持し、異なるパーサー間で破損したり一貫性なくレンダリングされたりする可能性のある構造を避けることができます ([GitHub][1])。

Rubyベースのmarkdownlint (markdownlint/mdl) に触発されたこのツールは、豊富なリンティングルールのライブラリを備えています。CommonMarkサポートのためにmicromarkパーサーを活用し、テーブル、自動リンク、ディレクティブ、脚注、数式といったGitHub Flavored Markdown (GFM) の機能で拡張されています ([GitHub][1])。

## 主な機能と統合

*   **ルールカバレッジ**: 見出しスタイル、リストのインデント、末尾のスペース、行の長さ（例: MD001, MD009, MD013…）など、包括的な組み込みルールセットを提供します ([GitHub][1])。
*   **エコシステム互換性**:

    *   **コマンドラインツール**:

        *   `markdownlint-cli` – 従来型のCLIインターフェース。
        *   `markdownlint-cli2` – より高速で、設定ベースのCLI。柔軟なフォーマットオプション、グロブのサポート、出力形式、自動修正、CIワークフローとの統合を提供します ([GitHub][2], [GitHub][3])。
    *   **VS Code 拡張機能**:

        *   `vscode‑markdownlint` は、エディターにリアルタイムのリンティングをもたらします。違反はインライン（下線付き）でフラグが立てられ、ホバー対応のツールチップとクイック修正の提案が表示されます ([GitHub][4])。
    *   **GitHub Action**:

        *   `markdownlint‑cli2‑action` を使用すると、markdownlintをCIパイプラインに組み込むことができ、GitHubワークフロー中に自動チェック（およびオプションの自動修正）を実行できます ([GitHub][5])。

---

## 使用する理由

*   **一貫性**: Markdownファイルが定義されたスタイルガイドに準拠することを保証し、プロジェクト全体でのフォーマットのぶれを減らします。
*   **エディター支援**: VS Codeやその他の統合環境でのインラインフィードバックにより、よりクリーンで高速な執筆が可能になります。
*   **自動化**: CIパイプラインでリンターツールやGitHub Actionsと共に使用し、マージ前に標準を強制します。
*   **カスタマイズ可能**: 設定ファイルまたはインラインコメント（例：長い行に対するMD013の無効化）を介して、ルールセットをカスタマイズしたり、ルールを無効にしたりできます ([GitHub][5], [Software Recommendations Stack Exchange][6])。

---

npmでのセットアップ、VS Code拡張機能の使用、またはCIワークフローへの統合に関するクイックスタートガイドはいかがですか？

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"