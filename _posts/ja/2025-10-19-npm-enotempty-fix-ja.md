---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: npm ENOTEMPTY インストールエラーの修正
translated: true
type: note
---

### エラーの理解

`sudo npm i -g @anthropic-ai/claude-code --verbose` コマンドがインストールプロセス中に `ENOTEMPTY` エラーで失敗しています。これは、npmがパッケージの更新や再インストールの一部として既存のディレクトリの名前変更（または移動）を試みたが、ディレクトリが空ではない場合に発生する一般的なnpmの問題です。この場合、具体的には `/usr/lib/node_modules/@anthropic-ai/claude-code` を一時的なバックアップ場所（`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`）に名前変更する際に失敗しています。

これは通常、以下の理由で発生します：
- 以前の部分的なインストールまたは中断されたインストールにより、ファイルやサブディレクトリが残っている
- 他のプロセスによるファイルロック（例：パッケージが部分的に読み込まれている場合、または他のnpmコマンドが実行中の場合）
- 稀に、`sudo` でのグローバルインストールにおける権限の問題

パッケージ自体（`@anthropic-ai/claude-code`）は正当なものです - これはAnthropicの公式CLIツールで、ターミナルとコードベースと統合する「Claude Code」というエージェント型コーディングアシスタントです。

### クイックフィックス

以下の手順を順番に試してください。これらはグローバルインストールなので、rootまたは `sudo` で実行してください。

1. **既存のディレクトリを手動で削除**  
   問題のある部分的なインストールをクリアします：  
   ```
   sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
   ```  
   - 親のスコープディレクトリ（`@anthropic-ai`）が空になった場合は、それも削除できます：  
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai
     ```  
   その後、元のコマンドを再試行します：  
   ```
   sudo npm i -g @anthropic-ai/claude-code --verbose
   ```

2. **npmキャッシュのクリア**  
   上記が機能しない場合、破損したキャッシュエントリが関与している可能性があります：  
   ```
   sudo npm cache clean --force
   sudo npm cache verify
   ```  
   この後、インストールを再試行してください。

3. **実行中のプロセスの確認**  
   他のnpm/Nodeプロセスがディレクトリを使用していないことを確認します：  
   ```
   ps aux | grep npm
   ```  
   必要に応じて残存するプロセスを強制終了し（例：`sudo kill <PID>`）、再試行します。

4. **代替案：npxを使用したテスト**  
   完全なグローバルインストールなしでツールをテストしたい場合は、以下を試してください：  
   ```
   npx @anthropic-ai/claude-code --help
   ```  
   これは一時的にダウンロードして実行し、グローバルモジュールを変更しません。

### 追加のヒント
- **権限のベストプラクティス**：`sudo` を使用したグローバルインストールは、後で所有権の問題を引き起こす可能性があります。`nvm` のようなnodeバージョンマネージャーを使用して `sudo` を完全に回避するか、カスタムグローバルプレフィックスを設定することを検討してください：  
  ```
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  export PATH=~/.npm-global/bin:$PATH
  ```  
  その後、`sudo` なしでインストールします。
- **インストール後の確認**：インストール後、`claude-code --version` で確認します（これがバイナリ名であると仮定 - ドキュメントで確認してください）。
- 問題が解決しない場合は、`npm ls -g @anthropic-ai/claude-code` の出力を共有して、さらなる診断を行ってください。

これで迅速に動作するはずです。別の問題が発生した場合は、新しいログを貼り付けてください！

[Claude Code on npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[Anthropic Docs: Set up Claude Code](https://docs.claude.com/en/docs/claude-code/setup)