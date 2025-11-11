---
audio: false
generated: true
lang: ja
layout: post
title: Liberty ToolsプラグインでのカスタムJVMパラメーター設定
translated: true
type: note
---

カスタム JVM パラメータ（例: `-Dversion=5.1`）は、VS Code の Liberty dev mode 起動設定に追加することで渡すことができます。通常、プロジェクト内の `.vscode/launch.json` ファイルを編集（または作成）し、`"vmArgs"` のようなプロパティの下にパラメータを記述します（設定で Maven ゴールの引数が期待される場合は `"args"` を使用）。

例えば、Liberty Tools 拡張機能を使って dev mode を実行する場合、設定は以下のようになります：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "liberty",
      "request": "launch",
      "name": "Liberty Dev Mode",
      "goal": "dev",
      "vmArgs": "-Dversion=5.1"
    }
  ]
}
```

### 手順:
1. **起動設定を開くまたは作成する:**
   - VS Code でプロジェクトを開きます。
   - `.vscode` フォルダに移動し、`launch.json` を開く（または作成）します。

2. **Dev Mode 設定を追加する:**
   - 上記のように設定エントリを追加します。`"vmArgs"` キーを使用して、dev mode 起動時にサーバーに渡される JVM オプションを指定できます。

3. **保存して起動する:**
   - ファイルを保存します。
   - 実行とデバッグビューを使用して「Liberty Dev Mode」設定を開始します。

Maven を直接使用している場合は、コマンドラインから dev mode を開始することもできます：

```bash
mvn liberty:dev -Dversion=5.1
```

このコマンドは、サーバー起動時にカスタムプロパティを JVM に渡します。

このように設定することで、Liberty Tools 拡張機能は dev mode を起動するたびにカスタムパラメータ（`-Dversion=5.1`）を含めるようになります。