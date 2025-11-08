---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: バンドラーコマンドが見つからない問題の修正
translated: true
type: note
---

### 問題の理解
`gem install jekyll bundler` は成功しました（Bundler 2.7.2を含む30個のgemをインストールしました）が、`bundle` コマンドが見つかりません。これは、Ubuntu/Debianシステムでシステム全体に対する `sudo gem install` を実行した後に発生する一般的なPATH/環境設定の問題です。Gemはバイナリを `/usr/local/bin`（または類似のパス）にインストールしますが、あなたのシェルの `$PATH` にそれが含まれていないか、変更が反映されていない（例：プロファイルの再読み込みが必要）可能性があります。

システムが提案する `apt install ruby-bundler` は、apt経由で古いバージョン（2.4.20）をインストールします。これは、gemでインストールしたBundler 2.7.2と競合する可能性があるため、当面は避けてください。snapについても同様です。snapはRubyを隔離する方法でインストールするため、gemのパスを壊す可能性があります。

### クイックフィックス: インストールされたBundlerを確認して使用する
1. **`bundle` がインストールされた場所を確認**:
   ```
   gem environment
   ```
   - "EXECUTABLE DIRECTORY"（おそらく `/usr/local/bin`）を探します。そのパスをメモしてください。

2. **`bundle` を直接探してテスト**:
   ```
   which bundle  # 何も表示されない場合: find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # "Bundler version 2.7.2" と出力されるはず
   ```
   - 動作すれば問題ありません！当面はフルパスを使用します: `/usr/local/bin/bundle install`

3. **フルパスを使用してJekyllセットアップを実行**:
   - `~/projects/blog-source` で（`Gemfile` があると仮定）:
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - これでJekyllの依存関係がインストールされ、サーバーが起動するはずです（通常は http://127.0.0.1:4000）。

### 恒久的な修正: PATHを更新する
`/usr/local/bin` があなたの `$PATH` に含まれていない場合は、追加してください:
1. `~/.bashrc`（またはログインシェルの場合は `~/.profile`）を編集:
   ```
   nano ~/.bashrc
   ```
   末尾にこの行を追加:
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. シェルを再読み込み:
   ```
   source ~/.bashrc
   ```

3. 確認:
   ```
   echo $PATH  # 現在は /usr/local/bin が含まれているはず
   bundle --version  # フルパスなしで動作するはず
   ```

これで再試行:
```
bundle install
bundle exec jekyll serve
```

### それでも動作しない場合
- **権限の問題？** （稀ですが、sudoが原因である可能性があります。）sudoなしで再インストール（ユーザーローカルインストール）:
  ```
  gem install --user-install bundler jekyll
  ```
  その後、`~/.bashrc` に `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` を追加（パスは `gem environment` の出力に基づいて調整）。

- **Rubyのバージョン不一致？** `ruby --version` で確認。システムRuby（例：2.7.x）の場合、長期的なシステム競合を避けるために `rbenv` などのRubyバージョンマネージャーの使用を検討（`curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash` でインストール後、セットアップに従う）。

- **プロキシがまだ影響している？** 環境変数（`http_proxy` など）が設定されている場合、Bundlerはそれらを継承するはずです - 実行前にエクスポートされていることを確認してください。

PATHの調整後、あなたのセットアップはスムーズに動作するはずです。エラーが発生した場合（例：`gem environment` の出力を共有）、より具体的なヘルプのためにそれを貼り付けてください！