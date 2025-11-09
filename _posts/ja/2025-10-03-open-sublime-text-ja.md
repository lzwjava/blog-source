---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: CLIからSublime Textを開く
translated: true
type: note
---

### コマンドライン（CLI）から Sublime Text を開く

Sublime Text には、macOS でデフォルトで `sublime`（または `subl`）コマンドが組み込まれていません（`open -a` という記述から、おそらく macOS をご利用だと思われます）。しかし、Sublime にバンドルされている `subl` スクリプトを使用して追加する、公式で簡単な方法があります。これは `open` コマンドに依存するよりもクリーンな方法です。以下に、推奨される方法から始めて、オプションを説明します。

#### 1. **公式の `subl` CLI コマンドをインストールする（推奨）**
Sublime Text には、アプリケーションバンドル内に `subl` 実行ファイルが含まれており、これを PATH にあるディレクトリ（`/usr/local/bin` など）にシンボリックリンクできます。これにより、ターミナルのどこからでも `subl .`（現在のディレクトリを開く）や `subl file.txt` を実行できるようになります。

**macOS の場合（Sublime Text 3 または 4）:**
- ターミナルを開きます。
- 次のコマンドを実行してシンボリックリンクを作成します（管理者権限が必要なため、パスワードの入力を求められます）:
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - Sublime Text 3 を使用している場合、パスが若干異なる可能性があります: `"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"`（必要に応じてバージョン番号を調整してください）。
  - `/usr/local/bin` が PATH に含まれていない場合は、シェルプロファイル（例: `~/.zshrc` または `~/.bash_profile`）に追加してください:
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- テスト: ディレクトリに移動し（例: `cd ~/Desktop`）、次を実行します:
  ```
  subl .
  ```
  これで、Sublime Text が現在のフォルダを読み込んで開くはずです。

シンボリックリンクのパスが機能しない場合（例: バージョンの違いによる）、正確な場所を確認してください:
- `find /Applications/Sublime\ Text.app -name subl` を実行してバイナリを探します。

**この方法の利点:**
- 公式で軽量です。サードパーティ製ツールは不要です。
- システム全体で機能し、本格的な CLI のように使えます。
- Sublime Text 4 では、コンソール（View > Show Console）から `sublime_installation` または類似のオプションを実行することもできますが、シンボリックリンクが最も信頼性が高いです。

**Linux または Windows の場合:**
- Linux: 同様のシンボリックリンクのプロセスです。例: `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`
- Windows: `C:\Program Files\Sublime Text\sublime_text.exe` を PATH に追加するか、`subl` 用のバッチファイルを使用します。

#### 2. **代替案: `open` コマンドを使用する（インストール不要）**
シンボリックリンクや PATH を操作したくない場合は、macOS に組み込まれている `open` コマンドが基本的な用途には十分機能します。これは既にどこでも利用できます。

- 現在のディレクトリを Sublime で開く:
  ```
  open -a "Sublime Text" .
  ```
  - 注意: アプリ名が "Sublime Text"（スペースあり）の場合はそれを使用してください。単に "Sublime.app" の場合は適宜調整してください。正確な名前は `/Applications/` で確認できます。

- 特定のファイルを開く:
  ```
  open -a "Sublime Text" filename.txt
  ```

- 便利なようにエイリアスを設定: シェルプロファイル（`~/.zshrc` または `~/.bash_profile`）に以下を追加して `subl` を模倣できます:
  ```
  alias subl='open -a "Sublime Text"'
  ```
  その後、`source ~/.zshrc` でリロードし、通常通り `subl .` を使用します。

**長所/短所:**
- 非常にシンプルでセットアップ不要です。
- ただし、macOS 専用で、柔軟性に欠けます（例: `subl` のように行番号やプロジェクトを簡単に指定する方法がない）。

#### トラブルシューティング
- **Command not found?** PATH に `/usr/local/bin` が含まれていることを確認してください（`echo $PATH` を実行して確認）。
- **App not found?** Sublime が `/Applications/` にあることを確認してください。別の場所にある場合（例: Homebrew 経由: `brew install --cask sublime-text`）、パスを調整してください。
- **Permissions issues?** シンボリックリンクの作成には sudo が必要ですが、一度設定すれば問題ありません。
- Homebrew のようなパッケージマネージャーを使用している場合、`brew install --cask sublime-text` で Sublime をインストールすると、CLI も自動的に設定される可能性があります。

これで問題なく動作するはずです！エラーが発生したり、OS/バージョンを指定したりした場合は、手順を詳細に説明できます。