---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: 最新バージョンへのクロードコードアップグレード
translated: true
type: note
---

Claude Codeをv2.0.0から最新バージョンにアップグレードするには、インストール方法に応じて以下のいずれかの方法を使用してください（すべてのバージョンはデフォルトで自動更新をサポートしており、次回ツール起動時に適用されます。`DISABLE_AUTOUPDATER=1`を設定することで無効化できます）：

### Claude Code組み込みコマンドによる方法
ターミナルで手動更新コマンドを実行：
```
claude update
```
これにより最新バージョンが自動的に適用されます。[1][2]

### npm経由（グローバルインストールの場合）
元々npm経由でインストールした場合は、以下で更新：
```
npm update -g @anthropic-ai/claude-code
```
または最新版を強制インストール：
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### ネイティブバイナリ（ベータインストーラー）経由
ネイティブインストールの場合は、インストーラースクリプトを再実行：
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**確認:** アップグレード後、`claude --version`でバージョンを確認し、更新されていることを確認してください（例：現在の安定版リリース）。問題が発生した場合は、npmが最新であることを確認してください（`npm install -g npm@latest`）。設定と構成は更新後も保持されます。[1][3][4]

引用：
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/