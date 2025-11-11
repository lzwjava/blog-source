---
audio: false
generated: true
lang: ja
layout: post
title: Git DifftoolとしてのBeyondCompareの設定
translated: true
type: note
---

`git difftool` として Beyond Compare を設定するには、以下の手順に従ってください。これらの手順は、Beyond Compare がインストールされており、システムに Git が設定されていることを前提としています。

### Beyond Compare を `git difftool` として設定する手順

1. **Beyond Compare のインストールを確認**
   Beyond Compare がインストールされ、コマンドラインからアクセスできることを確認します。次のコマンドを実行して確認できます:
   ```
   bcomp
   ```
   認識されない場合は、Beyond Compare の実行ファイル（Windows では `BCompare.exe`、macOS/Linux では `bcomp`）がシステムの PATH に含まれていることを確認してください。

2. **Git に Beyond Compare を使用するよう設定**
   ターミナルまたはコマンドプロンプトで以下の Git 設定コマンドを実行します:

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "path/to/bcomp"
   git config --global difftool.prompt false
   ```

   - `"path/to/bcomp"` は Beyond Compare の実行ファイルへの実際のパスに置き換えてください:
     - **Windows**: 通常 `"C:\Program Files\Beyond Compare 4\BCompare.exe"`。パス内では二重バックスラッシュ (`\\`) またはスラッシュ (`/`) を使用します。
     - **macOS**: 通常 `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`。
     - **Linux**: 多くの場合 `/usr/bin/bcomp` または `bcomp` がインストールされている場所。
   - `difftool.prompt false` 設定は、Git が各ファイルに対して difftool の起動を促すプロンプトを表示するのを防ぎます。

3. **（オプション）マージツールとして設定**
   Beyond Compare を `mergetool` としても使用したい場合は、以下のコマンドを追加します:

   ```bash
   git config --global merge.tool bc
   git config --global mergetool.bc.path "path/to/bcomp"
   git config --global mergetool.prompt false
   ```

4. **設定をテスト**
   設定を確認するために、変更がある Git リポジトリを作成または移動し、以下を実行します:

   ```bash
   git difftool
   ```

   これにより、変更されたファイルと最後のコミットとの差分を表示するために Beyond Compare が起動するはずです。マージツールとして使用している場合は、以下でテストします:

   ```bash
   git mergetool
   ```

   （これはマージコンフリクトがある場合にのみ適用されます。）

5. **プラットフォーム固有の注意点**
   - **Windows**: `BCompare.exe` への正しいパスを使用していることを確認してください。パスにスペースが含まれる場合は、引用符で囲んでください。
   - **macOS/Linux**: `bcomp` コマンドは、多くの場合、ターミナルに制御を戻す前に Beyond Compare が閉じるのを待つ必要があります。Beyond Compare のドキュメントではこれが自動的に処理されるとされていますが、Git が早期に終了する場合は、スクリプトを調整するか、ラッパーを使用する必要があるかもしれません（詳細は Beyond Compare のサポートを参照）。
   - 問題が発生した場合は、パスを確認し、Beyond Compare がライセンスされ機能していることを確認してください。

6. **Windows での設定例**
   Windows で Beyond Compare 4 を使用する場合、コマンドは以下のようになります:

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global difftool.prompt false
   git config --global merge.tool bc
   git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global mergetool.prompt false
   ```

7. **設定を確認**
   設定が適用されていることを確認するために、Git 設定をチェックします:

   ```bash
   git config --global --list
   ```

   `diff.tool=bc` や `difftool.bc.path` のようなエントリを探してください。

### 追加のヒント
- **特定のファイルを比較**: `git difftool <file>` を使用して特定のファイルを比較します。
- **ブランチを比較**: `git difftool branch1 branch2` を使用して2つのブランチ間の差分を比較します。
- **Beyond Compare 設定**: Beyond Compare では、インターフェースを通じて比較ルール（例: 空白を無視）をカスタマイズして、差分の視覚化を改善できます。
- **トラブルシューティング**: Beyond Compare が起動しない場合は、`difftool.bc.path` 設定のパスを再確認してください。実行ファイルの場所を確認するには `which bcomp` (macOS/Linux) または `where BCompare.exe` (Windows) を使用します。

この設定により、`git difftool` およびオプションで `git mergetool` で Beyond Compare をシームレスに使用できるようになります。特定の問題が発生した場合は、オペレーティングシステムとエラーメッセージをお知らせいただければ、より具体的なアドバイスを提供できます！