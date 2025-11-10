---
audio: false
generated: true
image: false
lang: ja
layout: post
title: VSCodeでの拡張ホストの起動
translated: true
type: note
---

Visual Studio Code (VSCode) で **F5** を押して **Extension Development Host** を起動し、VSCode 拡張機能を開発するには、以下の手順に従ってください。

1. **VSCode で拡張機能プロジェクトを開く**:
   - VSCode 拡張機能プロジェクトがセットアップされていることを確認してください。通常、必要な拡張機能設定（例: `contributes`、`activationEvents`）を含む `package.json` ファイルが含まれています。
   - `ファイル > フォルダを開く` を選択するか、`Ctrl+K, Ctrl+O` (Windows/Linux) または `Cmd+K, Cmd+O` (Mac) を使用して、拡張機能プロジェクトを含むフォルダを VSCode で開きます。

2. **拡張機能のセットアップを確認する**:
   - プロジェクトルートに有効な `package.json` ファイルがあり、少なくとも以下のフィールドが含まれていることを確認してください:
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - 拡張機能コードのエントリポイントとして `extension.js`（または同等のファイル）があることを確認してください。
   - 拡張機能が Node.js モジュールを使用する場合は、統合ターミナル (`Ctrl+``) で `npm install` を実行して依存関係をインストールしてください。

3. **F5 を押して Extension Development Host を起動する**:
   - 拡張機能プロジェクトが VSCode で開いている状態で、キーボードの **F5** を押します。
   - これにより **Extension Development Host** が起動します。これは、テスト用に拡張機能が読み込まれる別の VSCode ウィンドウです。
   - VSCode は自動的に以下を実行します:
     - 拡張機能をビルドします（TypeScript を使用している場合、`.ts` ファイルを `.js` にコンパイルします）。
     - 拡張機能が有効化された新しい VSCode インスタンスを起動します。
     - Extension Host プロセスにアタッチされたデバッガーを開きます。

4. **デバッグ設定**:
   - VSCode はデバッグ設定に `.vscode` フォルダ内の `launch.json` ファイルを使用します。存在しない場合、初めて F5 を押したときに VSCode が自動的に作成します。
   - 拡張機能用の典型的な `launch.json` は以下のようになります:
     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Run Extension",
           "type": "extensionHost",
           "request": "launch",
           "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
           "outFiles": ["${workspaceFolder}/out/**/*.js"],
           "preLaunchTask": "npm: watch"
         }
       ]
     }
     ```
   - `preLaunchTask`（存在する場合）が `tasks.json` 内のタスク（例: TypeScript のコンパイル用）と一致していることを確認してください。

5. **拡張機能をテストする**:
   - Extension Development Host ウィンドウで、拡張機能がアクティブになっているはずです。`package.json` とコードで定義された機能（例: コマンド、UI コントリビューション）をテストしてください。
   - メインの VSCode ウィンドウの **デバッグコンソール** を使用して、拡張機能からのログやエラーを確認できます。

6. **トラブルシューティング**:
   - F5 が機能しない場合:
     - 拡張機能開発に必要な Node.js と npm がインストールされていることを確認してください。
     - VSCode Extension API の依存関係 (`npm install @types/vscode`) がインストールされていることを確認してください。
     - `launch.json` の設定が正しいパスを指していることを確認してください。
     - エラーが表示される場合は、Extension Development Host ウィンドウの **出力** パネル（ドロップダウンで「Extension」を選択）を確認してください。
   - Extension Host が起動しない場合、プロジェクトの `package.json` またはメインの拡張機能ファイルに構文エラーがないことを確認してください。

**追加の注意点**:
- **実行とデバッグ** パネル (`Ctrl+Shift+D` または Mac では `Cmd+Shift+D`) を開き、ドロップダウンから「拡張機能の実行」を選択して、緑色の再生ボタンをクリックすることでも、Extension Development Host を開始できます。
   - 変更を加えた後に Extension Host をリロードするには、Extension Development Host ウィンドウで `Ctrl+R` (Windows/Linux) または `Cmd+R` (Mac) を使用するか、F5 で再起動してください。

詳細については、公式の VSCode 拡張機能開発ガイドを参照してください:  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)