---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: 開発依存関係とビルドツール
translated: true
type: note
---

### DevDependencies
これらは開発時に使用されるパッケージで、最終ビルドには含まれません。

- **babel-core** (6.13.0): 最新のJavaScript（ES6+）をES5にトランスパイルするためのコアBabelコンパイラ。ブラウザ互換性を向上させます。
- **babel-loader** (6.2.5): ビルドプロセスでBabelを統合し、JavaScript変換を行うWebpackローダー。
- **babel-plugin-transform-runtime** (6.12.0): トランスパイルされたコードでランタイムヘルパーを再利用し、バンドルサイズを削減するBabelプラグイン。
- **babel-preset-es2015** (6.13.2): ES2015（ES6）機能をES5にコンパイルするためのBabelプリセット。
- **babel-runtime** (6.11.6): Babelでトランスパイルされたコード向けのポリフィルとヘルパーを提供するランタイムライブラリ。
- **cross-env** (^1.0.8): シェルの違いに関係なく、環境変数（例: NODE_ENV）をクロスプラットフォームで設定します。
- **css-loader** (^0.23.1): CSSファイルを読み込み、インポートと依存関係を解決します。
- **detect-indent** (4.0.0): ファイルのインデントスタイル（スペース/タブ）を検出し、一貫したフォーマットを実現します。
- **exports-loader** (^0.6.3): モジュールのエクスポートを異なるコンテキスト（例: 非AMDモジュール向け）で利用可能にします。
- **extract-text-webpack-plugin** (^1.0.1): JavaScriptバンドルからCSSを抽出し、別ファイルとして保存します。パフォーマンス向上に役立ちます。
- **file-loader** (0.9.0): ファイル（例: 画像）を出力ディレクトリに出力し、URLを返すことでファイルの読み込みを処理します。
- **html-webpack-plugin** (^2.22.0): HTMLファイルを生成し、バンドルされたアセットを注入します。シングルページアプリの設定を簡素化します。
- **rimraf** (^2.5.4): クロスプラットフォームの再帰的文件削除ツール（Unixのrm -rfに相当）。
- **style-loader** (^0.13.1): styleタグを介してCSSをDOMに注入し、動的読み込みを可能にします。
- **stylus** (^0.54.5): 表現力豊かなシンタックスを持つCSSプリプロセッサ。CSSにコンパイルされます。
- **stylus-loader** (^2.1.1): StylusファイルをCSSに処理するWebpackローダー。
- **url-loader** (0.5.7): 小さなファイル（例: 画像）をBase64エンコードしてインライン化するか、大きなファイルは出力します。file-loaderにフォールバックします。
- **vue-hot-reload-api** (^1.2.0): 開発中にVue.jsコンポーネントのホットモジュール置換を有効にします。
- **vue-html-loader** (^1.0.0): Vueシングルファイルコンポーネント内のHTMLテンプレートを解析するWebpackローダー。
- **vue-loader** (8.5.3): Vueシングルファイルコンポーネント（.vueファイル）をJavaScriptとCSSに読み込み、処理します。
- **vue-style-loader** (^1.0.0): VueコンポーネントからのCSSを処理し、style-loaderと統合します。
- **webpack** (1.13.2): JS、CSS、画像などのWebアセットをビルドおよび最適化するモジュールバンドラー。
- **webpack-dev-server** (1.14.0): ライブリロードとホットモジュール置換を備えた開発サーバー。

### Dependencies
これらは最終アプリケーションビルドに含まれるランタイムパッケージです。

- **debug** (^2.2.0): 名前空間付きロギングと条件付き出力を提供するデバッグユーティリティ（DEBUG環境変数でのみ有効）。
- **es6-promise** (^3.0.2): 古いブラウザ/環境向けのES6 Promise APIポリフィル。
- **font-awesome** (^4.6.3): CSSクラスを介してスケーラブルなベクターアイコンを提供する人気のアイコンライブラリ。
- **github-markdown-css** (^2.4.0): GitHub風Markdownのスタイリング用CSS。
- **highlight.js** (^9.6.0): 複数言語のコードブロック用シンタックスハイライター。
- **hls.js** (^0.7.6): HTML5ビデオでHTTP Live Streaming（HLS）ビデオを再生するJavaScriptライブラリ。
- **inherit** (^2.2.6): JavaScriptオブジェクトにおける古典的およびプロトタイプ継承のためのユーティリティ。
- **jquery** (^3.1.0): DOM操作、AJAX、イベント処理のための高速で機能豊富なJavaScriptライブラリ。
- **json-loader** (^0.5.4): JSONファイルをJavaScriptモジュールとして読み込みます。
- **leancloud-realtime** (^3.2.3): LeanCloudのリアルタイムメッセージングおよびデータ同期サービスのSDK。
- **marked** (^0.3.6): MarkdownをHTMLに変換するMarkdownパーサー。
- **moment** (^2.14.1): 日付の解析、検証、フォーマットを行う日付/時刻操作ライブラリ。
- **moment-timezone** (^0.5.7): タイムゾーンと夏時間を処理するMoment.js拡張。
- **qiniu-js-sdk** (0.0.2): Qiniuクラウドストレージとの連携（ファイルのアップロード/ダウンロード）のためのJavaScript SDK。
- **raw-loader** (^0.5.1): ファイルを生の文字列（例: テキストテンプレート）として読み込むWebpackローダー。
- **rupture** (^0.6.1): Stylus用メディアクエリ拡張。レスポンシブデザインのためのブレークポイントを提供します。
- **sprintf-js** (^1.0.3): プレースホルダーを使用した文字列フォーマットのためのJavaScript sprintf実装。
- **vue** (^1.0.26): ユーザーインターフェース構築のためのプログレッシブMVVMフレームワーク（v1.x、旧バージョン）。
- **vue-resource** (^0.6.1): AJAX/APIリクエストを簡素化するVue.js用HTTPクライアント。
- **vue-router** (^0.7.13): Vue.jsの公式ルーター。シングルページアプリケーションのナビゲーションを可能にします。
- **vue-spinner** (^1.0.2): Vue.js用のスピナー/ローディングコンポーネントライブラリ。
- **vue-weui** (^0.3.2): WeUIコンポーネントのVue.jsラッパー（WeChatスタイルインターフェース用UIライブラリ）。
- **weixin-js-sdk** (^1.2.0): WeChat Web機能（共有、スキャンなど）を統合するためのWeChat JavaScript SDK。
- **weui** (^0.4.3): WeChatのデザインに触発されたモバイルインターフェース構築のためのWeUI CSSフレームワーク。
- **word-color** (^1.2.0): ハッシュや言語などの要素に基づいて単語に色を付けるライブラリ。ヒートマップのような効果を実現します。