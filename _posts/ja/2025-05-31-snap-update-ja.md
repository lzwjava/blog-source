---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのSnapを使用したVSCodeの更新
translated: true
type: note
---

Snapを使用してUbuntuにインストールしたVisual Studio Code（VSCode）を更新するには、以下の手順に従ってください。

1. **ターミナルを開く**: `Ctrl + Alt + T` を押すことで開くことができます。

2. **更新を確認する**: Snapはバックグラウンドで自動的に更新を確認しますが、手動で更新確認をトリガーするには以下を実行します:
   ```bash
   sudo snap refresh
   ```

3. **VSCodeを更新する**: もしVSCodeの新しいバージョンが利用可能な場合、`snap refresh` コマンドがダウンロードとインストールを行います。以下のような進捗を示す出力が表示されます:
   ```
   code 1.85.2 from Visual Studio Code (code✓) refreshed
   ```
   更新が利用できない場合は、以下のように表示されます:
   ```
   All snaps up to date.
   ```

4. **更新を確認する**: インストールされているVSCodeのバージョンを確認するには、以下を実行します:
   ```bash
   code --version
   ```
   これにより、現在のVSCodeのバージョンが表示されます。

### 注意点:
- **自動更新**: VSCodeを含むSnapパッケージは、通常バックグラウンドで自動的に更新されます。強制的に更新を実行したい場合以外は、手動で操作する必要は通常ありません。
- **ルート権限**: システム全体に対するSnap操作には `sudo` コマンドが必要です。
- **Snapステータスの確認**: インストールされているSnapパッケージとそのバージョンを確認したい場合は、以下を使用します:
   ```bash
   snap list
   ```
- **トラブルシューティング**: 更新に失敗した場合は、インターネット接続が安定していることを確認し、Snapデーモンが実行されているか確認してください (`sudo systemctl status snapd`)。また、Snapメタデータを更新して試すこともできます:
   ```bash
   sudo snap refresh --list
   ```

この手順により、VSCodeがSnapストアで利用可能な最新バージョンに保たれます。