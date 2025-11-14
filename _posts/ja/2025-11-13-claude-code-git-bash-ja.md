---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WindowsでのClaude CodeのGit Bashの使用方法
translated: true
type: note
---

はい、最近の動向に基づくと、Windows上のClaude Code（Anthropic社のAIコーディングツール）はシェルコマンドを実行するために `git-bash.exe` を起動することが確認されています。特にWSLを使用しないネイティブのWindows環境では、Git Bashをコマンド実行環境として頻繁に使用します。これにより、コマンド実行時にポップアップターミナルが表示されることがあり、Git Bashが適切に検出・使用されるようにするための設定、拡張機能（VS Codeなど）、トラブルシューティング手順が存在します。

例：
- ネイティブのWindowsインストール環境では、Claude Codeはスクリプトやコマンドを処理するためのUnixライクな互換性を得るためにGit Bashに依存しています
- デフォルトのターミナル（VS CodeやCursorなどの統合ツール内）として設定されている場合、タスク実行のために `git-bash.exe` を起動します
- Gitインストールディレクトリのパス問題やスペースに関連して、この統合に影響を与える既知のバグやガイドが報告されています

問題が発生している場合は、システムのPATHを確認し、Gitが正しくインストールされていることを確認し、IDEのターミナルプロファイルを検証してください。

参考文献：  
[Claude Code Native Windows Bash output not seen - Reddit](https://www.reddit.com/r/ClaudeAI/comments/1m06s2l/claude_code_native_windows_bash_output_not_seen/)  
[BUG Claude Code VS Code Extension Fails to Detect Git Bash on GitHub](https://github.com/anthropics/claude-code/issues/8674)  
[Troubleshooting Claude Code Installation on Windows - Medium](https://medium.com/%40tomhag_17/troubleshooting-claude-code-installation-on-windows-from-tty-errors-to-success-1f44af03c9f2)  
[Running Claude Code on Windows Without WSL - Blog](https://blog.shukebeta.com/2025/06/25/running-claude-code-on-windows-without-wsl/)  
[AI Agent Claude 4 runs commands in PowerShell even when default is Git Bash - Forum](https://forum.cursor.com/t/ai-agent-claude-4-runs-commands-in-powershell-even-when-default-terminal-is-git-bash/137164)  
[How To Install Claude Code on Windows Complete Guide 2025 - Itecsonline](https://itecsonline.com/post/how-to-install-claude-code-on-windows)  
[BUG Claude Code fails to resolve Git Bash path with space - GitHub](https://github.com/anthropics/claude-code/issues/4507)  
[Install Claude Code on Windows Without WSL Step-by-Step Guide - YouTube](https://www.youtube.com/watch?v=LtnxvLZjxAI)  
[47 Claude Code WSL Tricks Every Windows User Should Know - Medium](https://medium.com/%40joe.njenga/47-claude-code-wsl-tricks-every-windows-user-should-know-5d42aaee2d93)  
[Claude Code Installation Guide for Windows 11 Setting Up with WSL2 - Claude AI](https://claude.ai/public/artifacts/03a4aa0c-67b2-427f-838e-63770900bf1d)