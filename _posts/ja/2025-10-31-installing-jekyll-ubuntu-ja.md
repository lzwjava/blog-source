---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UbuntuへのJekyllインストール
translated: true
type: note
---

### Ubuntu での Jekyll のセットアップと実行

エラーメッセージ（"Command 'bundle' not found"）と実行しようとしているコマンドから、Ruby、Bundler、Jekyll が適切にインストールされていないようです。Ubuntu はこれらをデフォルトでは含んでいませんが、公式 Jekyll ガイドを使えば簡単にセットアップできます。ここでは、完全なセットアップ手順と、あなたが実行しようとしている特定のコマンドの実行方法をステップバイステップで説明します。

#### ステップ 1: システム依存関係のインストール
ターミナルを開き、以下のコマンドを実行して Ruby とビルドツールをインストールします（`ruby-full` により Ruby 3.x が含まれます）:

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- これで Ruby がセットアップされます（`ruby -v` で確認してください。3.0+ のようなバージョンが表示されるはずです）。
- 最近の Ubuntu（例: 22.04+）を使用している場合、これはそのまま動作します。パスに関する問題が発生する可能性があるため、可能であれば Ruby の Snap パッケージは避けてください。

#### ステップ 2: ユーザー Gem ディレクトリのセットアップ (Sudo を避けるための推奨事項)
ルート権限なしで gem をインストールするために設定します（後のパーミッションエラーを防ぎます）:

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- 確認: `gem env` を実行してください。`GEM_HOME` が `~/gems` と表示されるはずです。

#### ステップ 3: Jekyll と Bundler のインストール
以下のコマンドでツールをインストールします:

```bash
gem install jekyll bundler
```

- これにより、`gem`、`jekyll`、`bundle` コマンドがあなたのパスに追加されます。
- パーミッションエラーが発生した場合は、ステップ 2 を再確認するか、一時的に `sudo` を使用してください（ただし長期的な使用は避けてください）。

#### ステップ 4: ブログの作成と実行
これで、あなたのスニペットにあるコマンドを実行できるようになります。それぞれ説明します:

1. **新しい Jekyll サイトを作成**:
   ```bash
   jekyll new myblog
   ```
   - これにより、`myblog` フォルダ内に基本的なサイトが生成されます。

2. **ディレクトリに移動**:
   ```bash
   cd myblog
   ```

3. **依存関係をインストール** (ここで元の `bundle install` が失敗していましたが、これで動作するはずです):
   ```bash
   bundle install
   ```
   - Jekyll プラグインなどの gem を取得します。

4. **サイトをサーブ** (http://127.0.0.1:4000 でローカルサーバーを起動):
   ```bash
   bundle exec jekyll serve
   ```
   - ブラウザでその URL を開いてサイトを確認してください。

5. **インクリメンタルリビルドでサーブ** (開発時により高速、変更されたファイルのみリビルド):
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **下書きを含めてサーブ** (未公開の投稿を表示):
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **"webrick" エラーが発生した場合** (Ruby 3+ では標準でバンドルされていないため一般的):
   ```bash
   bundle add webrick
   ```
   - その後、サーブコマンドを再起動: `bundle exec jekyll serve`。
   - または、`Gemfile` に `gem "webrick"` を追加して `bundle install` を実行してください。

8. **Bundler なしでクイックサーブ** (`bundle exec` をスキップする場合):
   ```bash
   jekyll serve
   ```
   - ただし、プロジェクト内では一貫性のために `bundle exec` を使用することをお勧めします。

#### トラブルシューティング
- **まだ "bundle not found" ですか?** ステップ 2 で `~/.bashrc` が正しくソースされたか確認してください (`source ~/.bashrc`)。その後、ターミナルを再起動するか `hash -r` を実行してください。`which bundle` で確認できます。
- **gem でのパーミッション問題?** ステップ 2 のユーザーディレクトリ設定を守ってください。
- **Ruby のバージョンが古すぎますか?** `ruby -v` が 3.0 未満の場合、rbenv を使用して新しいバージョンをインストールすることを検討してください (`curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash` でインストールし、その後 `rbenv install 3.2.0` を実行)。
- **ファイアウォールがポート 4000 をブロックしていますか?** Ubuntu では通常ブロックしませんが、`curl http://127.0.0.1:4000` でテストできます。
- あなたのプロジェクトは `~/projects/blog-source` にあるので、これらのコマンドをそこから実行するか、パスを調整してください。

サーブを開始した後、`_posts/` または `_config.yml` 内のファイルを編集して保存すると、Jekyll は自動的にリビルドします。本番環境では、`jekyll build` でビルドし、GitHub Pages や Netlify にデプロイしてください。

[Jekyll Ubuntu インストールガイド](https://jekyllrb.com/docs/installation/ubuntu/)