---
audio: false
generated: true
lang: ja
layout: post
title: Jekyllビルドの高速化：マルチスレッド手法の探求
translated: true
type: note
---

Jekyllのビルドプロセスはデフォルトでシングルスレッドであり、大規模サイトでは遅くなる可能性があります。Jekyllにはマルチスレッドビルドを有効にする組み込みの設定オプションはありませんが、並列処理を実現するためのいくつかのアプローチを検討できます。以下では、利用可能な情報と技術的考察に基づいて、可能性、課題、実践的な手順を概説します。

### Jekyllビルドがシングルスレッドである理由
Jekyllは依存関係（`site.related_posts`やLiquidテンプレートなど）が正しく処理されることを保証するために、ページを順次処理します。Liquidや特定のプラグインなど、一部のコンポーネントはスレッドセーフではない可能性があり、これがマルチスレッド化を複雑にしています（）。この設計は速度よりも正確性を優先しますが、大規模サイトでは数分のビルド時間につながる可能性があります（,）。[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### マルチスレッドJekyllビルドへのアプローチ
以下は、特に提供されたGitHub Actionsワークフローのようなコンテキストにおいて、Jekyllビルドに並列性を導入する潜在的な方法です：

#### 1. **カスタムプラグインを使用したマルチスレッドレンダリング**
マルチスレッドレンダリングのための概念実証プラグインが提案されています（）。テストケースではビルド時間を45秒から10秒に短縮しましたが、スレッド安全性の問題により不正なページコンテンツが生成されることがありました。このプラグインはまた、順次レンダリングに依存する`jekyll-feed`のようなプラグインと競合しました。[](https://github.com/jekyll/jekyll/issues/9485)

**カスタムプラグインを試す手順**:
- **プラグインの作成**: Jekyllの`Site`クラスを拡張してページレンダリングを並列化するRubyプラグインを実装します。例えば、`render_pages`メソッドを変更してRubyの`Thread`クラスやスレッドプールを使用できます（）。[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # 元のメソッドを呼び出す
        @rendering_threads.each(&:join) # スレッドの完了を待機
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **Gemfileへの追加**: プラグインを`_plugins`ディレクトリに配置し、Jekyllによってロードされることを確認します。
- **スレッド安全性のテスト**: Liquidや一部のプラグイン（例: `jekyll-feed`）が動作しなくなる可能性があるため、十分にテストします。特定の機能についてはLiquidにパッチを適用するか、マルチスレッド化を避ける必要があるかもしれません（）。[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actionsとの統合**: ワークフローを更新して、リポジトリにプラグインを含めます。`jekyll-build-pages`アクションがカスタムJekyllセットアップを使用することを確認します：
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # プラグインを含むカスタムGemfileが使用されることを確認
  ```

**課題**:
- Liquidや`jekyll-feed`のようなプラグインとのスレッド安全性の問題（）。[](https://github.com/jekyll/jekyll/issues/9485)
- 不正なページレンダリング（例: あるページのコンテンツが別のページに表示される）の可能性。
- デバッグとメンテナンスにRubyの専門知識が必要。

#### 2. **複数設定によるビルドの並列化**
単一ビルドのマルチスレッド化の代わりに、サイトを小さな部分（例: コレクションやディレクトリごと）に分割し、複数のJekyllプロセスを使用して並列にビルドできます。このアプローチはスレッド安全性の問題を回避しますが、より多くの設定が必要です。

**手順**:
- **サイトの分割**: サイトをコレクション（例: `posts`, `pages`, `docs`）やディレクトリごとに整理し、それぞれに別個の`_config.yml`ファイルを作成します（,）。[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **GitHub Actionsワークフローの更新**: ワークフローを変更して、異なる設定ファイルを使用する複数のJekyllビルドを並列に実行します。
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **出力の結合**: 並列ビルド後、出力ディレクトリを単一の`_site`フォルダにマージしてデプロイします。

**課題**:
- コレクション間の相互依存関係（例: `site.related_posts`）の管理。
- 設定とデプロイの複雑さの増加。
- 密結合なコンテンツを持つサイトではうまくスケールしない可能性。

#### 3. **大規模サイトへのスレッドプールの使用**
`amp-jekyll`プラグインへのプルリクエストでは、システムに過負荷をかけないように設定可能なスレッド数でページを処理するスレッドプールの使用が提案されました（）。このアプローチはパフォーマンスとリソース使用量のバランスを取ります。[](https://github.com/juusaw/amp-jekyll/pull/26)

**手順**:
- **スレッドプールの実装**: 修正または新規プラグインを作成して、Rubyの`Thread::Queue`を使用し、固定数のワーカースレッド（例: システムに応じて4または8）を管理します。
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4スレッド
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **設定オプションの追加**: `_config.yml`でマルチスレッドを有効/無効にしたり、スレッド数を設定できるようにします：
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **ワークフローとの統合**: プラグインがリポジトリに含まれ、GitHub Actionsビルド中にロードされることを確認します。

**課題**:
- 最初のアプローチと同様のスレッド安全性の問題。
- 多くの短いタスクを持つ大規模サイトではコンテキスト切り替えのオーバーヘッド（）。[](https://github.com/juusaw/amp-jekyll/pull/26)
- すべてのプラグインとの互換性を保証するためのテストが必要。

#### 4. **マルチスレッドなしでの最適化**
マルチスレッドが複雑すぎるかリスクが高い場合、シングルスレッドのビルドプロセスを最適化できます：
- **インクリメンタルビルドの有効化**: `jekyll build --incremental`を使用して変更されたファイルのみをリビルドします（,）。ワークフローに追加：[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **プラグイン使用の削減**: カスタムプラグインはビルドを大幅に遅くする可能性があります（）。不要なプラグインを監査して削除します。[](https://github.com/jekyll/jekyll/issues/4297)
- **高速なコンバーターの使用**: KramdownからCommonMarkのような高速なマークダウンプロセッサに切り替えるか、特定のユースケースでPandocをテストします（）。[](https://github.com/jekyll/jekyll/issues/9485)
- **依存関係のキャッシュ**: GitHub Actionsワークフローで`bundler-cache: true`を設定し、gemの再インストールを避けます（）。[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### 推奨事項
- **インクリメンタルビルドから始める**: これはスレッド安全性の問題をリスクにさらすことなくビルドを高速化する最も簡単な方法です。ワークフローに`--incremental`を追加し、その影響をテストします。
- **スレッドプールプラグインを試す**: Rubyの専門知識がある場合は、設定可能なスレッド数を持つスレッドプールプラグインの実装（オプション3）を試してください。スレッド安全性をテストするために小さなサイトから始めます。
- **当面は完全なマルチスレッド化を避ける**: Liquidやプラグインとのスレッド安全性に関する懸念（）を考慮すると、完全なマルチスレッド化には大幅なリファクタリングやカスタムLiquidフォークが必要になる可能性があり、Jekyllのコア開発に貢献しない限り実用的ではないかもしれません。[](https://github.com/jekyll/jekyll/issues/9485)
- **ビルド時間の監視**: GitHub Actionsのログを使用してビルド時間を測定し、ボトルネックを特定します。例えば、6分かかるサイト（）は、プラグインや大規模なアセット処理が問題である可能性を示唆しています。[](https://github.com/jekyll/jekyll/issues/1855)

### インクリメンタルビルドを有効にしたGitHub Actionsの例
以下は、インクリメンタルビルドを有効にしたワークフローの更新版です：
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### 注意点
- **スレッド安全性**: Jekyllでのマルチスレッドは実験的であり、プラグインを破壊したり不正な出力を生成したりする可能性があります（）。最初に小さなサイトで十分にテストしてください。[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actionsの制限**: 並列ビルド（オプション2）はリソース使用量を増加させるため、ワークフローがGitHubの無料ティア制限内に収まることを確認します。
- **Jekyll 5の可能性**: Jekyllの将来のバージョンでは、議論されている（）ようにマルチスレッドがネイティブに対応される可能性があります。現時点では、カスタムソリューションが必要です。[](https://github.com/jekyll/jekyll/issues/9485)

特定のアプローチ（例: プラグインの記述やビルドの分割）の実装にヘルプが必要な場合は、詳細なガイダンスやコードを提供できますのでお知らせください！