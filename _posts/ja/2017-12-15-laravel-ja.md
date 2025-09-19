---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Laravelを使って
translated: true
---

ウェブ開発に取り組み、強力で使いやすいフレームワークを探しているなら、Laravelがおすすめです。PHPのフレームワークで、優雅な構文、強力な機能、そしてサポートのあるコミュニティが人気を博しています。このブログでは、Laravelの基本を学び、なぜ時間をかける価値があるかをお伝えします。

#### ステップ1: 環境のセットアップ
Laravelで作業を始める前に、必要なツールを用意しましょう。以下が必要です：
- **PHP**: バージョン8.1以上（Laravelは進化が早いので、最新版を使用してください）。
- **Composer**: PHPの依存関係管理ツール。[getcomposer.org](https://getcomposer.org/)からダウンロードしてください。
- **ローカルサーバー**: XAMPP、WAMP、またはLaravelの組み込みサーバーなどが使えます。
- **ターミナル**: コマンドを実行するので、コマンドラインに慣れてください。

これらを用意したら、ターミナルを開いてLaravelをグローバルにインストールします：
```
composer global require laravel/installer
```
これで、1つのコマンドで新しいLaravelプロジェクトを作成できます。

#### ステップ2: 初めてのLaravelプロジェクトを作成
何かを作成する準備ができましたか？ターミナルで、プロジェクトを配置したいフォルダに移動し（例：`cd /path/to/your/folder`）、以下を入力します：
```
laravel new my-first-app
```
数分後、Composerが新しいLaravelプロジェクト「my-first-app」をセットアップします。その中に移動します：
```
cd my-first-app
```
動作を確認するには、Laravelの組み込みサーバーを起動します：
```
php artisan serve
```
ブラウザを開き、`http://localhost:8000`にアクセスします。これで、ウェルカムページが表示されます。これがLaravelの挨拶です。

#### ステップ3: 基本を理解する
LaravelはMVC（モデル-ビュー-コントローラ）構造を採用しており、コードを整理しやすくしています：
- **モデル**: データを扱います（データベーステーブルを想像してください）。
- **ビュー**: ユーザーが見るフロントエンド部分（HTML、CSSなど）。
- **コントローラー**: モデルとビューを結びつける役割です。

これらは`app/`フォルダにあります。例えば、コントローラーは`app/Http/Controllers`に、ビューは`resources/views`にあります。

#### ステップ4: 簡単なページを作成
「Hello, World」ページを作成してみましょう。`routes/web.php`を開きます。これは、アプリのURLを定義する場所です。以下の行を追加します：
```php
Route::get('/hello', function () {
    return view('hello');
});
```
次に、`resources/views`に`hello.blade.php`というファイルを作成し、以下を追加します：
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, Laravel</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```
サーバーを再起動（または実行中にしておく）し、`http://localhost:8000/hello`にアクセスします。「Hello, World!」ページが表示されます。`.blade.php`拡張子は、LaravelのBladeテンプレートエンジンを使用していることを意味します。動的コンテンツに非常に便利です。

#### ステップ5: データベースを操作
Laravelは、Eloquent ORM（オブジェクトリレーショナルマッピング）を使ってデータベース操作を簡単にしてくれます。まず、`.env`ファイルでデータベースを設定します（例：MySQL、SQLite）：
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
```
テーブルを設定するためのマイグレーションを作成します。以下を実行します：
```
php artisan make:migration create_posts_table
```
新しいファイル`database/migrations`でテーブルを定義します：
```php
public function up()
{
    Schema::create('posts', function (Blueprint $table) {
        $table->id();
        $table->string('title');
        $table->text('body');
        $table->timestamps();
    });
}
```
マイグレーションを実行します：
```
php artisan migrate
```
これで、`posts`テーブルができました！以下で`Post`モデルを作成します：
```
php artisan make:model Post
```
これで、コードで使用できるテーブルにモデルを結びつけました。

#### ステップ6: さらに探索
Laravelには、認証、ミドルウェア、ルーティング、Composer経由のパッケージなど、さらに多くの機能があります。ユーザーログインが必要なら、以下を実行します：
```
php artisan make:auth
```
フロントエンドの強化が必要なら、Laravel BreezeやJetstreamを使用します。[公式ドキュメント](https://laravel.com/docs)は、ここでは最も信頼できる友人です。

#### Laravelを使う理由
速く、安全で、車輪の再発明を防いでくれます。ブログ、電子商取引サイト、APIなど、Laravelのツール（Artisanコマンド、Bladeテンプレート、Eloquentなど）は、生活を楽にしてくれます。

では、何を待っているのですか？小さく始めて、実験し、すぐにプロのようにウェブアプリを作成できるようになります。楽しいコーディングを！