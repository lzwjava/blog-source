---
audio: false
generated: true
lang: ja
layout: post
title: VS Code VSIX ダウンロード
translated: true
type: note
---

Visual Studio Code（VS Code）拡張機能の `.vsix` ファイルを手動でダウンロードするには、すべての公式拡張機能をホストしている Visual Studio Marketplace を利用できます。`.vsix` ファイルは VS Code 拡張機能のパッケージ形式ですが、Marketplace が常に直接ダウンロードボタンを提供するわけではありません。ダウンロード URL を構築するか、代替方法を使用することができます。手順は以下の通りです。

### `.vsix` ファイルを手動でダウンロードする手順

1. **Visual Studio Marketplace で拡張機能を見つける**  
   - Web ブラウザで [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) にアクセスします。
   - 目的の拡張機能（例: Microsoft の "Python"、"Prettier - Code formatter" など）を検索します。
   - 拡張機能のページを開きます。例: Python 拡張機能の URL は以下のようになります。  
     `https://marketplace.visualstudio.com/items?itemName=ms-python.python`

2. **パブリッシャーと拡張機能名を特定する**  
   - 拡張機能のページで、**パブリッシャー**と拡張機能識別子を確認します。これらは URL の一部またはページに表示されています。
   - 例: `ms-python.python` の場合、`ms-python` がパブリッシャー、`python` が拡張機能名です。

3. **ダウンロード URL を構築する**  
   - `.vsix` ファイルは、Marketplace が提供する特定の URL パターンを使用して直接ダウンロードできます。一般的な形式は以下の通りです。  
     ```
     https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - `<publisher>` をパブリッシャー名に、`<extension-name>` を拡張機能名に置き換えます。
   - Python 拡張機能（`ms-python.python`）の場合、URL は以下のようになります。  
     ```
     https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - この URL をブラウザに貼り付けると、`.vsix` ファイルのダウンロードが開始されます。

4. **代替方法: Marketplace ページの「Download Extension」リンクを使用する（利用可能な場合）**  
   - 一部の拡張機能ページには、**Resources** セクションなどに「Download Extension」リンクが含まれている場合があります。存在する場合は、それをクリックして直接 `.vsix` ファイルをダウンロードできます。ただし、これはあまり一般的ではないため、URL を使用する方法がより信頼性があります。

5. **ダウンロードを確認する**  
   - ダウンロードされたファイルは `.vsix` 拡張子を持ちます（例: `ms-python.python-<version>.vsix`）。
   - ファイルサイズと名前を確認し、目的の拡張機能とバージョンに一致することを確認します。

6. **`.vsix` ファイルを VS Code にインストールする（オプション）**  
   - VS Code を開きます。
   - 拡張機能ビュー（`Ctrl+Shift+X` または macOS では `Cmd+Shift+X`）に移動します。
   - 拡張機能ペインの右上にある三点メニュー（`...`）をクリックします。
   - **Install from VSIX** を選択し、ダウンロードした `.vsix` ファイルを参照して選択します。

### 実施例
**ESLint** 拡張機能（Dirk Baeumer 作）を入手したい場合:
- Marketplace URL: `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- パブリッシャー: `dbaeumer`
- 拡張機能名: `vscode-eslint`
- ダウンロード URL:  
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- この URL をブラウザで開くと、`.vsix` ファイル（例: `dbaeumer.vscode-eslint-<version>.vsix`）がダウンロードされます。

### 注意点
- **バージョン**: URL の `/latest/` 部分は、最新バージョンを取得することを保証します。特定のバージョンが必要な場合は、通常、バージョン番号（Marketplace の「Version History」タブで確認可能）へのアクセスが必要であり、URL を調整するか、`ovsx` のようなツールを使用する必要があるかもしれません（ただし、Marketplace API が古いバージョンを直接 URL 経由で簡単に公開するとは限りません）。
- **ダウンロードのブロック**: URL が機能しない場合、パブリッシャーが直接アクセスを制限しているか、ブラウザ/ネットワークがブロックしている可能性があります。そのような場合は、別のブラウザまたはダウンロードマネージャーを試してください。
- **代替ツール**: `ovsx`（Open VSX Registry のコマンドラインツール）を使用して拡張機能をダウンロードできます。npm でインストール（`npm install -g ovsx`）し、以下のコマンドを実行します。  
  ```
  ovsx download ms-python.python
  ```
  これにより、プログラムで `.vsix` ファイルがダウンロードされます。

### まとめ
VS Code 拡張機能の `.vsix` ファイルを手動でダウンロードするには:
1. [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) で拡張機能のページに移動します。
2. パブリッシャーと拡張機能名（例: `ms-python.python`）を特定します。
3. ブラウザで以下の URL 形式を使用します。  
   ```
   https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
   ```
4. `.vsix` ファイルをダウンロードし、必要に応じて VS Code にインストールします。