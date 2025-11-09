---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: npmインストールエラーの修正
translated: true
type: note
---

### エラーの理解

これは `@anthropic-ai/claude-code` パッケージのグローバルアップデート（またはインストール）中に発生した npm インストールの失敗です。主要な問題は、npm が新しいバージョンをインストールする前に既存のパッケージディレクトリを「退避」（バックアップ）しようとする「reify」フェーズにあります。具体的には：

- npm は `/usr/lib/node_modules/@anthropic-ai/claude-code` を `/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ` のような一時的なバックアップに名前変更しようとしています。
- これが `ENOTEMPTY: directory not empty` (errno -39) で失敗しています。これは通常、以下の場合に発生します：
  - ソースディレクトリにロックされている、使用中である、またはパーミッションの問題があるファイル/サブディレクトリが含まれている。
  - 壊れたシンボリックリンク、開いているファイルハンドル（例：実行中の `claude` プロセスからのもの）、または Linux 上のファイルシステムの特性の問題がある。
  - 稀に、npm の内部 move-file ロジックが競合状態に陥る。

あなたの環境：
- Node: v22.18.0
- npm: v11.6.1
- OS: Linux 6.14.0-29-generic (おそらく Ubuntu/Debian)
- root として実行（ログパス `/root/.npm/_logs/` に基づく）なので、パーミッションが根本的な原因ではない。
- 作業ディレクトリ: `/home/lzwjava/projects/blog-source`（ただし、これはグローバルインストールなので無関係）。

このパッケージは Anthropic の Claude Code ツール（AI コーディングアシスタンス用 CLI）のようです。73 行目に `@img/sharp-libvips-linux-x64` の依存関係の不一致警告が表示されていますが、これはクラッシュとは無関係です。

### クイックフィックス（順番に試してください）

1. **実行中のプロセスを停止**:
   - `claude` CLI または関連するプロセスを強制終了: `pkill claude`（または `ps aux | grep claude` で PID を探し、`kill <PID>`）。
   - パッケージを使用しているターミナル/IDE を閉じる。

2. **ディレクトリを手動でクリーンアップ**:
   - 既存のパッケージとバイナリを削除：
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
     sudo rm -f /usr/bin/claude
     ```
   - これにより npm のバックアップステップを回避します。その後、インストールを再試行：
     ```
     sudo npm install -g @anthropic-ai/claude-code
     ```

3. **npm キャッシュをクリアして再試行**:
   - 実行：
     ```
     sudo npm cache clean --force
     sudo npm install -g @anthropic-ai/claude-code
     ```
   - それでも続く場合は、Sharp イメージライブラリのようなオプションの依存関係をスキップするために `--no-optional` を追加。

4. **代替案: npx の使用またはグローバルインストールの回避**:
   - グローバルに必要ない場合は、プロジェクト内にローカルインストール: `npm install @anthropic-ai/claude-code`（その後 `npx claude` で実行）。
   - または Yarn を使用: `sudo yarn global add @anthropic-ai/claude-code`（Yarn は時々移動処理が異なる）。

5. **それでも解決しない場合**:
   - ファイルシステムの問題を確認: `ls -la /usr/lib/node_modules/@anthropic-ai/`（おかしなシンボリックリンクやロックを探す）。
   - npm を一時的にダウングレード: `sudo npm install -g npm@10`（v11 には時折 reify のバグがある。後で戻す）。
   - 完全なログ: `/root/.npm/_logs/2025-10-27T16_10_10_534Z-debug-0.log` を確認してさらなる手がかりを得る。

これで解決するはずです - Linux 上の npm グローバルインストールは名前変更に関して厄介なことがあります。実行した正確なコマンドやより多くのログコンテキストを共有していただければ、これをさらに改良できます。