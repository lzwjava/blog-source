---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: クロードコード編集確認ポップアップを無効化
translated: true
type: note
---

Claude Codeで編集確認ポップアップを無効にするには（`sync_githook.py`のようなファイルへの編集を確認なしで直接適用するため）、`settings.json`ファイルでパーミッションを設定する必要があります。これが「Claude Code JSON」と呼ばれるもので、ユーザーレベルの設定を行うClaude Codeのメイン設定ファイルです。

### 設定手順

1. **ファイルの場所と作成**:
   - ファイルは`~/.claude/settings.json`（macOS/Linux）または`%USERPROFILE%\.claude\settings.json`（Windows）にあります。`.claude`フォルダは隠しフォルダなので、ターミナルやファイルエクスプローラーで移動してください。
   - ファイルやフォルダが存在しない場合は作成します。Claude CodeのインタラクティブREPLで`/config`コマンドを実行すると、設定インターフェースを開くように案内されます。

2. **JSONの編集**:
   - テキストエディタ（VS Codeなど）で`settings.json`を開きます。
   - すべての編集アクションに対してプロンプトを無効にするには、`permissions`セクションを追加または更新します：

     ```json:disable-run
     {
       "permissions": {
         "defaultMode": "acceptEdits",
         "allow": [
           "Edit(*)",
           "Write(*)",
           "MultiEdit(*)"
         ],
         "ask": []
       }
     }
     ```

     - **この設定の効果**:
       - `"defaultMode": "acceptEdits"`: グローバルなデフォルトを編集をプロンプトなしで承認するように設定します。
       - `"allow"`: `Edit`（単一ファイル編集）、`Write`（コンテンツ書き込み）、`MultiEdit`（一括変更）などの特定のツールを任意のファイル（`*`ワイルドカード）に対して事前承認します。
       - `"ask": []`: 他の場所で明示的に拒否されない限り、どのアクションもプロンプトを表示しないようにします。
     - ファイルを保存します。変更は次のClaude Codeセッションで即時適用されます。

3. **テスト**:
   - Claude Codeを再起動するか、セッションをリロードします。
   - ファイルの編集を依頼します（例：「`sync_githook.py`にコメントを追加するように編集してください」）。ポップアップなしで変更が適用されるはずです。
   - プロジェクト固有の設定が必要な場合（例：このリポジトリのみ）、プロジェクトのルートフォルダに`.claude/settings.json`を作成してください。

4. **オプションの調整**:
   - より細かい制御が必要な場合（例：特定のディレクトリのみ編集を許可）：`"Edit(*)"`を`"Edit(./src/**)"`に変更します。
   - プロンプトが表示され続ける場合は、REPLで`/allowed-tools`を実行して現在のルールを確認するか、`/config`を使用してUIで調整します。
   - セキュリティのため、過度に広範な`allow`ルールは避け、シンプルに始めて拡張してください。

これにより、中断なしでより高速なワークフローが実現します。エンタープライズ設定の場合は、管理ポリシーがユーザー設定を上書きする可能性があるため、管理者に確認してください。

[Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)  
[Disable Claude Code Permission Prompts Guide](https://www.arsturn.com/blog/how-to-disable-claude-code-permission-prompts)