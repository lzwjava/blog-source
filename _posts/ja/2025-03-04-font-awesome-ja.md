---
audio: false
generated: true
lang: ja
layout: post
title: Font Awesome パッケージの NPM
translated: true
---

### 重要ポイント
- 「font-awesome」npmパッケージ（バージョン4）を使用するには、まず `npm install font-awesome` でインストールし、HTMLにCSSファイルをリンクし、クラスを使用してアイコンを使用する必要があります。例えば、`<i class="fa fa-home"></i>`。
- 研究によると、バージョン4は古く、更新されていないため、バージョン6にアップグレードすることを検討してください。これにより、更新とセキュリティが得られます。例えば、`@fortawesome/fontawesome-free`を使用します。

---

### インストールと基本的な使用方法
「font-awesome」npmパッケージ（バージョン4）を使用するには、まず `npm install font-awesome` コマンドを使用してインストールします。インストール後、HTMLにCSSファイルを追加することで、アイコンを使用できます。例えば、`<link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">`。その後、HTMLを使用してアイコンを追加します。例えば、`<i class="fa fa-home"></i>`。アイコン名は、[Font Awesome version 4 documentation](https://fontawesome.com/v4/cheatsheet)で確認できます。

### 代替方法
webpackなどのビルドツールを使用している場合は、JavaScriptファイルでCSSを直接インポートできます。例えば、`import 'font-awesome/css/font-awesome.min.css';`。LessやSassを使用しているプロジェクトでは、対応するファイルをインポートします。例えば、Lessでは、`@import "node_modules/font-awesome/less/font-awesome";`。パスは必要に応じて調整してください。

### バージョニングに関する注意
「font-awesome」パッケージはバージョン4であり、8年以上更新されていないため、メンテナンスされていません。最新の機能とセキュリティを得るために、バージョン6にアップグレードすることを検討してください。バージョン6は、`@fortawesome/fontawesome-free`（無料）または `@fortawesome/fontawesome-pro`（プロ、サブスクリプションが必要）で利用できます。バージョン6をインストールするには、`npm install @fortawesome/fontawesome-free` を実行し、`import '@fortawesome/fontawesome-free/css/all.min.css';` でインポートします。詳細については、[Font Awesome documentation](https://fontawesome.com/docs/web/use-with/node-js)を参照してください。

---

### アンケートノート: Font Awesome npmパッケージの使用に関する包括的なガイド

このセクションでは、「font-awesome」npmパッケージの使用に関する詳細な探求を行い、バージョン4に焦点を当てつつ、より新しいバージョン6への移行についても触れます。情報は公式ドキュメント、npmパッケージの詳細、コミュニティの議論に基づいており、すべてのレベルの開発者にとって包括的な理解を提供します。

#### 背景とコンテキスト
「font-awesome」npmパッケージは、[npm](https://www.npmjs.com/package/font-awesome)にリストされているバージョン4.7.0のFont Awesomeに対応しています。このバージョンは8年前に公開され、古く、現在はサポート終了です。Font Awesomeは、ウェブ開発でウェブサイトにアイコンを追加するために広く使用されるスケーラブルなベクタアイコンのツールキットです。バージョン4は、CSSを主に使用してアイコンを実装し、フォントファイルを使用して知られていますが、後続のバージョンに見られる最新の機能や更新が欠けています。

バージョン4のドキュメントは[Font Awesome version 4 documentation](https://fontawesome.com/v4/)でまだアクセス可能ですが、公式サイトはバージョン6に焦点を当てており、バージョン4はサポート終了とされています。これは、特にセキュリティと機能の向上のために、継続的なプロジェクトのアップグレードを検討する重要性を示しています。

#### 「font-awesome」パッケージ（バージョン4）のnpmを使用した使用方法
「font-awesome」パッケージを使用するには、以下の手順に従ってください。これらの手順は、標準的なnpmの実践とコミュニティの使用に基づいています。

1. **インストール:**
   - プロジェクトディレクトリで `npm install font-awesome` コマンドを実行します。これにより、バージョン4.7.0がインストールされ、`node_modules/font-awesome` ディレクトリにファイルが配置されます。
   - パッケージには、npmの説明に記載されているように、CSS、Less、フォントファイルが含まれています。Semantic Versioningの下でメンテナンスされ、Lessの使用方法の説明が含まれています。

2. **HTMLへの含め方:**
   - 基本的な使用には、HTMLのheadにCSSファイルをリンクします。
     ```html
     <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
     ```
   - パスが正しいことを確認してください。HTMLがルートにない場合は、適宜調整してください（例：`../node_modules/font-awesome/css/font-awesome.min.css`）。

3. **アイコンの使用:**
   - アイコンはHTMLで使用します。例えば、`<i class="fa fa-home"></i>`。ここで、`fa` はベースクラスであり、`fa-home` はアイコンを指定します。詳細なリストは、[Font Awesome version 4 cheatsheet](https://fontawesome.com/v4/cheatsheet)で確認できます。
   - この方法は、含まれるフォントファイルを利用してスケーラブルでCSSカスタマイズが可能です。

4. **ビルドツールとの代替的な統合:**
   - webpackなどのビルドツールを使用している場合は、JavaScriptでCSSをインポートします。
     ```javascript
     import 'font-awesome/css/font-awesome.min.css';
     ```
   - この方法は、CSSがプロジェクトにバンドルされることを確認するため、現代的なウェブ開発で一般的です。

5. **LessとSassのサポート:**
   - Lessを使用しているプロジェクトでは、コミュニティの議論に従ってファイルを直接インポートできます。例えば：
     ```less
     @import "node_modules/font-awesome/less/font-awesome";
     ```
   - Sassの場合も、必要に応じてパスを調整します。ただし、バージョン4は主にLessをサポートしており、Ruby GemのRails統合では `font-awesome-less` と `font-awesome-sass` が含まれています。

#### 実用的な考慮事項とコミュニティの洞察
Stack Overflowなどのコミュニティの議論では、生産用にファイルをパブリックディレクトリにコピーする、gulpタスクを使用する、必要なLessコンポーネントをインポートしてバンドルサイズを減らすなどの一般的な実践が明らかになります。例えば、1つのユーザーは必要なLessファイルのみをインポートすることを提案しましたが、バイト数の節約が少ないことを指摘しました。例えば：
   - `@import "@{fa_path}/variables.less";`
   - `@import "@{fa_path}/mixins.less";` など、`@fa_path` を `"../node_modules/font-awesome/less"` に調整します。

しかし、多くのユーザーにとっては、CSSファイルを直接リンクするだけで十分です。特に小規模から中規模のプロジェクトでは。npmパッケージの内容には、BundlerとLessプラグインの要件も含まれており、高度なユーザー向けの追加設定が示されています。例えば：
   - Lessをグローバルにインストールするには、`npm install -g less` を実行します。
   - Less Plugin Clean CSSを使用するには、`npm install -g less-plugin-clean-css` を実行します。

#### バージョン4の制限とアップグレードパスに関する注意
バージョン4は機能的ですが、サポートされておらず、バージョン5のLong Term Support (LTS)でのみ重要なバグ修正が提供され、バージョン3と4はサポート終了とされています。これは、長期的なプロジェクトにとって新機能、セキュリティパッチ、更新が提供されないことを意味します。

アップグレードするには、バージョン6はSVGとJavaScript、新しいスタイル（Solid、Regular、Light、Duotone、Thin）、分離されたブランドアイコンなどの重要な変更を導入しています。アップグレードするには、`@fortawesome/fontawesome-free` をインストールします。
   - `npm install @fortawesome/fontawesome-free`
   - `import '@fortawesome/fontawesome-free/css/all.min.css';` でインポートします。CSSファイル名はバージョン6で `all.min.css` に変更され、より広範なアイコンサポートを反映しています。

詳細なアップグレード手順は、[Font Awesome upgrade from version 4](https://fontawesome.com/docs/web/setup/upgrade/upgrade-from-v4)で確認できます。これは、互換性の注意事項とバージョン4のファイルを削除する手順を含み、スムーズな移行を確保します。

#### 比較表: バージョン4とバージョン6の使用

| アスペクト                  | バージョン4 (font-awesome)                     | バージョン6 (@fortawesome/fontawesome-free)    |
|-------------------------|---------------------------------------------|---------------------------------------------|
| インストールコマンド    | `npm install font-awesome`                  | `npm install @fortawesome/fontawesome-free` |
| CSSファイル名           | `font-awesome.min.css`                      | `all.min.css`                               |
| アイコン使用例          | `<i class="fa fa-home"></i>`                | `<i class="fas fa-home"></i>` (Solid style) |
| メンテナンスステータス  | サポート終了、更新なし                     | アクティブにメンテナンス、最新バージョン6.7.2   |
| 追加機能               | 基本的なCSS、Lessサポート                     | SVGとJS、複数のスタイル、APIサポート   |
| ドキュメントURL         | [バージョン4のドキュメント](https://fontawesome.com/v4/) | [バージョン6のドキュメント](https://fontawesome.com/docs/web/use-with/node-js) |

この表は、進化を示し、開発者がアップグレードの判断を下すのに役立ちます。

#### 結論と推奨事項
新しいプロジェクトでは、アクティブなサポートと最新の機能を得るためにバージョン6を強く検討してください。バージョン4を使用している既存のプロジェクトでは、特にセキュリティのためにアップグレードパスを評価してください。提供された手順はバージョン4で機能を確保しますが、将来に向けたアプローチはバージョン6を採用することです。詳細なガイドラインは、[Font Awesome documentation](https://fontawesome.com/docs/web/use-with/node-js)で確認できます。

この包括的なガイドは、基本的なインストールから高度な統合まで、すべての必要な情報を提供しつつ、迅速に進化する技術環境におけるアップデートの重要性を強調します。

---

### 主要な引用
- [Font Awesome version 4 documentation with cheatsheet](https://fontawesome.com/v4/)
- [font-awesome package on npm with version 4.7.0 details](https://www.npmjs.com/package/font-awesome)
- [FortAwesome Font-Awesome GitHub repository with version history](https://github.com/FortAwesome/Font-Awesome)