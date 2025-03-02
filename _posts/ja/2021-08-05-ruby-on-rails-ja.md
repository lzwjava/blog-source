---
audio: false
generated: false
lang: ja
layout: post
title: Ruby on Railsを使って
translated: true
---

ShowMeBugで働いている間に、Enterprise WeChat統合プロジェクトに貢献しました。これは、ShowMeBugをEnterprise WeChatと統合し、Enterprise WeChatエコシステム内で技術面接ツールへのスムーズなアクセスを提供するものでした。Ruby、Ruby on Rails、PostgreSQL、およびWeChat SDKなどの技術を利用して、面接官および応募者の両方にとってスムーズなユーザー体験を作成しました。

このブログ記事は、AIの助けを借りて2025年2月頃に作成されました。

---

Ruby on Rails（しばしば「Rails」と略される）は、Rubyプログラミング言語に基づく強力なWeb開発フレームワークです。規約より設定、DRY（Don’t Repeat Yourself）の原則を強調することで、Webアプリケーションの構築を迅速かつ楽しくするために設計されています。設定方法と簡単なアプリの作成方法を一緒に見ていきましょう。

#### ステップ1: RubyとRailsのインストール
まず、Rubyがインストールされている必要があります。RailsはRubyのgem（ライブラリ）です。ほとんどのシステムにはRubyが事前にインストールされていないため、以下のように設定します。

- **macOS/Linux:**
  - `rbenv`や`rvm`などのバージョン管理ツールを使用して柔軟性を確保します。Homebrewを使用してインストールします（`brew install rbenv`）、次に実行します：
    ```bash
    rbenv install 3.2.2  # 2025年の安定したRubyバージョン
    rbenv global 3.2.2
    ```
  - Railsをインストールします：
    ```bash
    gem install rails
    ```

- **Windows:**
  - RubyInstaller（rubyinstaller.orgからダウンロード）を使用します。3.2.2のバージョンとDevKitを選択します。
  - Rubyのインストール後、コマンドプロンプトを開き、以下を実行します：
    ```bash
    gem install rails
    ```

インストールを確認します：
```bash
ruby -v  # ruby 3.2.2などが表示されるはずです
rails -v # 最新のRailsバージョン（例：7.1.x）が表示されるはずです
```

#### ステップ2: 新しいRailsプロジェクトの作成
Railsがインストールされたら、新しいアプリを生成します：
```bash
rails new myapp --database=sqlite3
cd myapp
```
これにより、`myapp`という名前のフォルダーが作成され、SQLiteをデフォルトデータベースとして使用する完全なRails構造が含まれます（開発には最適です）。

#### ステップ3: サーバーの起動
組み込みのRailsサーバーを実行します：
```bash
rails server
```
ブラウザを開き、`http://localhost:3000`にアクセスします。歓迎ページが表示されます。おめでとうございます、Railsアプリが実行中です！

#### ステップ4: 簡単なものを作成
RailsのMVC（モデル-ビュー-コントローラ）パターンを理解するために、基本的な「投稿」機能を作成します。

- **モデルとコントローラの生成:**
  ```bash
  rails generate scaffold Post title:string body:text
  ```
  これにより、`Post`モデル、データベース移行、コントローラ、ビューがすべてワイヤリングされます。

- **移行の実行:**
  ```bash
  rails db:migrate
  ```
  これにより、投稿用のデータベーステーブルが設定されます。

- **確認:**
  サーバーを再起動（`rails server`）し、`http://localhost:3000/posts`にアクセスします。投稿を作成、読み取り、更新、削除するためのCRUDインターフェースが表示されます。

#### ステップ5: 主要な概念の探索
- **ルート:** `config/routes.rb`を開きます。`resources :posts`が表示され、RESTfulルート（例：`/posts/new`や`/posts/1/edit`）が自動生成されます。
- **コントローラ:** `app/controllers/posts_controller.rb`を確認します。これはリクエストとレスポンスを処理します。
- **ビュー:** `app/views/posts/`を確認します。これらはERBテンプレート（Rubyが埋め込まれたHTML）です。
- **モデル:** `app/models/post.rb`を確認します。これはデータベースに接続され、検証（例：`validates :title, presence: true`）を含めることができます。

#### ステップ6: カスタマイズとデプロイ
- `app/assets/stylesheets/`でCSSを追加してスタイルを設定します。
- 本番環境では、PostgreSQL（`rails new myapp --database=postgresql`）に切り替え、RenderやHerokuなどのプラットフォームにデプロイします。`Gemfile`に`gem "pg"`を追加し、`bundle install`を実行します。

#### プロのコツ
- `rails console`を使用して、モデルをリアルタイムで実験します。
- `rails generate --help`を実行して、Railsが提供するすべてのショートカットを確認します。
- `devise`を認証用に、または`pundit`を認可用に使用するなど、gemを活用します。`Gemfile`に追加し、必要に応じて設定します。

これで、基本的なRailsアプリが実行中です。ここから、公式のRailsガイド（guides.rubyonrails.org）を探索するか、実際のプロジェクトを作成してスキルを確立しましょう。どんなプロジェクトを考えているのですか？