---
audio: false
generated: true
lang: ja
layout: post
title: クロードコードCLIの更新
translated: true
type: note
---

こんにちは！AnthropicのClaude Code CLIツールについてお困りのようですね。貼り付けていただいた出力結果から判断すると、すでにバージョン1.0.61への自動更新が試みられたようですが、もしそれが機能していない場合や手動で更新する必要がある場合は、以下の方法をお試しください：

Claude Code CLIを更新するには：
- ターミナルを開きます
- コマンドを実行：`claude update`
この組み込みコマンドで最新バージョンを取得してインストールできるはずです

もし更新に失敗した場合（権限やネットワークの問題など）、npm経由での再インストールをお試しください（Node.jsとnpmがインストールされている前提）：
- 実行：`npm install -g @anthropic-ai/claude-code`

更新後、`claude /login`（またはバージョンによっては`claude login`）を実行して再度ログインする必要があるかもしれません。まだエラーが表示される場合は、インターネット接続を確認し、APIキーが有効であることを確認するか、公式のトラブルシューティングドキュメントを参照してください。

コマンドの詳細については、実行された`claude --help`で更新後のバージョンのオプションが表示されるはずです。

[CLI reference - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[How to Set Up and Use the Claude CLI Tool Like a Pro](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Claude Code overview - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)