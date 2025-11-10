---
audio: false
generated: true
image: false
lang: ja
layout: post
title: MacでVSCodeのFn + F5を修正
translated: true
type: note
---

MacでVisual Studio Code（VSCode）を使用中に **Fn + F5** を押しても **Extension Development Host** が起動しない場合、Macの `Fn` キーとファンクションキーの設定、VSCodeのキーバインディングの競合、または拡張機能開発環境の設定ミスが原因である可能性があります。以下で、その理由と解決方法を説明します。

### Macで **Fn + F5** が動作しない理由

1. **Macのファンクションキーの動作**:
   - Macのキーボードでは、ファンクションキー（F1–F12）はデフォルトでシステム機能（例: F5はキーボードの輝度やメディア再生の制御）に割り当てられていることが多いです。
   - `Fn` キーは「標準的な」ファンクションキーの動作（例: `Fn + F5` はシステム機能ではなく実際のF5キーの信号を送信）にアクセスするために使用されます。
   - `Fn + F5` がVSCodeで期待通りに動作しない場合、Macのキーボード設定またはVSCodeのキーバインディングが入力を正しく解釈していない可能性があります。

2. **VSCodeのキーバインディングの競合または設定ミス**:
   - VSCodeがExtension Development Hostを起動する「Run Extension」コマンドに `F5`（または `Fn + F5`）を割り当てていない可能性があります。
   - 他の拡張機能やカスタムキーバインディングが `F5` を上書きしている可能性があります。

3. **拡張機能開発環境の設定の問題**:
   - VSCode拡張機能プロジェクトが適切に設定されていない場合（例: `launch.json` の欠落または不備）、`F5`（`Fn` の有無にかかわらず）を押してもExtension Development Hostは起動しません。

4. **macOSシステム設定**:
   - macOSが `F5` キーをシステム機能用に横取りしているか、`Fn` キーの動作がカスタマイズされており、VSCodeがそれを検出する能力に影響を与えている可能性があります。

### MacのVSCodeで **Fn + F5** が動作しない問題を修正する手順

#### 1. **macOSのキーボード設定を確認する**
   - **標準的なファンクションキーの動作を有効にする**:
     - **システム設定 > キーボード** に移動します。
     - **「F1、F2などのキーを標準のファンクションキーとして使用」** チェックボックスをオンにします。
     - 有効にした場合、`Fn` なしで `F5` を直接押すと、F5キーの信号がVSCodeに送信されます。Extension Development Hostが起動するかどうか、`F5` のみを押して試してください。
     - オフの場合、F5のみを押すとシステム機能（例: キーボードの輝度）を制御する可能性があるため、F5を送信するには `Fn + F5` を押す必要があります。
   - **F5の動作をテストする**:
     - テキストエディタ（例: TextEdit）を開き、`F5` と `Fn + F5` を押します。`F5` のみでシステムアクション（輝度調整など）がトリガーされ、`Fn + F5` で何も起こらない場合、`Fn` キーは標準のF5信号を送信するように期待通りに動作しています。
   - **NVRAM/PRAMをリセットする**（必要に応じて）:
     - Macを再起動し、起動音が2回鳴る（または新しいMacではAppleロゴが2回表示される）まで `Cmd + Option + P + R` を押し続けます。これによりキーボード関連の設定がリセットされ、検出の問題が解決される可能性があります。

#### 2. **VSCodeのキーバインディングを確認する**
   - VSCodeを開き、**Code > 環境設定 > キーボードショートカット**（`Cmd+K, Cmd+S`）に移動します。
   - 検索バーに `F5` または `Run Extension` と入力します。
   - Extension Development Hostの起動に関連するコマンド **「Debug: Start Debugging」** または **「Run Extension」** を探します。
   - それが `F5` にマッピングされていることを確認してください。そうでない場合は、コマンドをダブルクリックし、`F5`（または必要に応じて `Fn + F5`）を押して、新しいキーバインディングを保存します。
   - 競合を確認する: `F5` または `Fn + F5` にバインドされている他のコマンドを検索し、それらを削除または再割り当てします。
   - 必要に応じてキーバインディングをリセットする: キーボードショートカットエディタの3つのドット（`...`）をクリックし、**キーバインディングをリセット** を選択します。

#### 3. **拡張機能プロジェクトの設定を確認する**
   - 拡張機能プロジェクトが正しく設定されていることを確認します:
     - 拡張機能プロジェクトフォルダをVSCodeで開きます（`package.json` と `extension.js` または同等のファイルが含まれている必要があります）。
     - `package.json` に必要なフィールドが含まれていることを確認します:
       ```json
       {
         "name": "your-extension-name",
         "displayName": "Your Extension Name",
         "version": "0.0.1",
         "engines": {
           "vscode": "^1.60.0"
         },
         "categories": ["Other"],
         "activationEvents": ["*"],
         "main": "./extension.js"
       }
       ```
   - `.vscode/launch.json` ファイルを確認します:
     - 存在しない場合、`F5` を押すとVSCodeが作成するはずです。作成されない場合は、`.vscode` フォルダ内に手動で作成します:
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
     - `preLaunchTask`（例: `npm: watch`）が、TypeScriptまたはビルドステップを使用している場合の `.vscode/tasks.json` 内のタスクと一致していることを確認します。
   - VSCodeターミナル（`Cmd+``）で `npm install` を実行し、依存関係（例: `@types/vscode`）がインストールされていることを確認します。

#### 4. **Extension Development Hostの起動をテストする**
   - 拡張機能プロジェクトを開いた状態で、`F5`（または「F1、F2などのキーを標準のファンクションキーとして使用」設定がオフの場合は `Fn + F5`）を押してみます。
   - あるいは、**実行とデバッグ** パネル（`Cmd+Shift+D`）を開き、ドロップダウンから **「Run Extension」** を選択して、緑色の再生ボタンをクリックします。
   - Extension Development Hostが起動しない場合:
     - **出力** パネル（`Cmd+Shift+U`）を確認し、ドロップダウンから **「Extension」** を選択してエラーを表示します。
     - **デバッグコンソール** で、拡張機能またはデバッグプロセスに関連するエラーを確認します。
     - Node.jsがインストールされていること（ターミナルで `node -v`）と、プロジェクトに構文エラーがないことを確認します。

#### 5. **別のキーボードでテストする**
   - 外部USBキーボードをMacに接続し、VSCodeで `F5`（または `Fn + F5`）を押します。
   - 動作する場合、問題はMacの内蔵キーボードのハードウェアまたはファームウェアにある可能性があります。キーボードのファームウェアアップデートをMacの製造元（例: Apple Software Update）で確認してください。

#### 6. **VSCodeとmacOSを更新する**
   - VSCodeが最新であることを確認します: **Code > Check for Updates** に移動するか、VSCodeのWebサイトから最新バージョンをダウンロードします。
   - macOSを更新します: **システム設定 > 一般 > ソフトウェアアップデート** に移動し、利用可能なアップデートをインストールします。キーボードドライバの修正が含まれている可能性があります。

#### 7. **干渉する拡張機能またはソフトウェアを無効にする**
   - **VSCode拡張機能**:
     - すべての拡張機能を無効にします: ターミナルで `code --disable-extensions` を実行し、VSCodeを開いて `F5` を再度試します。
     - 動作する場合、拡張機能を1つずつ再有効化して原因を特定します。
   - **サードパーティ製ソフトウェア**:
     - Karabiner-ElementsやBetterTouchToolなどのキーボードリマップツールを確認します。それらの設定を開き、`F5` または `Fn + F5` がリマップされていないことを確認します。
     - テストのためにこれらのツールを一時的に無効にします。

#### 8. **デバッグログ**
   - VSCode開発者ツールを有効にしてキーイベントを検査します:
     - VSCodeを開き、`Cmd+Option+I` を押して開発者ツールを開きます。
     - **Console** タブに移動し、`Fn + F5` を押します。VSCodeが正しい入力を検出しているかどうかをキーイベントログで確認します。
   - キーイベントがログに記録されない場合、問題はシステムレベル（macOSまたはキーボードハードウェア）にある可能性が高いです。

### 問題が解決しない場合
   - 詳細を提供してください:
     - macOSバージョン（例: Ventura, Sonoma）。
     - VSCodeバージョン（**Code > About Visual Studio Code** で確認）。
     - キーボードタイプ（例: MacBook内蔵、外部キーボードモデル）。
     - `F5` または `Fn + F5` が他のアプリ（例: ブラウザで `F5` が更新するか）で動作するかどうか。
     - VSCodeの **出力** または **デバッグコンソール** でのエラーメッセージ。
   - 問題を切り分けるために最小限の拡張機能プロジェクトを作成してみてください:
     - `yo code` を実行します（YeomanとVSCodeジェネレーターが必要: `npm install -g yo generator-code`）。
     - 新しいプロジェクトをVSCodeで開き、`F5` を押してExtension Development Hostが起動するかどうかを確認します。

[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)  
[Mac Keyboard Settings](https://support.apple.com/guide/mac-help/change-the-behavior-of-the-function-keys-mchlp2882/mac)  
[VS Code Keybindings](https://code.visualstudio.com/docs/getstarted/keybindings)