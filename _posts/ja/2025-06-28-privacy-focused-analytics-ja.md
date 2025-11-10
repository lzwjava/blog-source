---
audio: false
generated: true
lang: ja
layout: post
title: プライバシー重視のウェブ解析ガイド
translated: true
type: note
---

Cloudflare Web Analyticsは、ユーザーのプライバシーを損なうことなく、ウェブサイト所有者がサイトのパフォーマンスと訪問者の行動を追跡・理解するのに役立つ、プライバシー重視の無料ツールです。以下は、最新の情報に基づく、Cloudflare Web Analyticsの設定と使用に関する包括的なガイドです。

### Cloudflare Web Analyticsの概要
Cloudflare Web Analyticsは、ユーザーのプライバシーを優先しながら、ウェブサイトトラフィック、ページビュー、パフォーマンスメトリクスに関する洞察を提供します。個人データを追跡したりCookieを使用したりする可能性のある従来のアナリティクスツールとは異なり、Cloudflareのソリューションは、フィンガープリンティング、Cookie、またはアナリティクス目的でのローカルストレージなどの侵入的な追跡方法を回避します。あらゆる規模のウェブサイトに適しており、Cloudflareのプロキシサービスを利用しているかどうかに関係なく使用できます。[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### 主な機能
- **プライバシー優先**: 個人データを収集せず、Cookieを使用せず、IPアドレスやユーザーエージェント経由でユーザーを追跡しないため、GDPRなどのプライバシー規制への準拠を確保します。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **2つのデータ収集方法**:
  - **JavaScript Beacon**: 軽量なJavaScriptスニペットがブラウザのPerformance APIを使用してクライアントサイドのメトリクスを収集します。ページ読み込み時間やCore Web Vitalsなどの詳細なReal User Monitoring (RUM) データに理想的です。[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Edge Analytics**: Cloudflareを経由してプロキシされたサイトについて、Cloudflareのエッジサーバーからサーバーサイドのデータを収集します。コード変更は不要で、ボットやJavaScriptが無効なユーザーからのリクエストもすべて捕捉します。[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **提供されるメトリクス**: ページビュー、訪問数、人気ページ、参照元、国、デバイスタイプ、ステータスコード、ページ読み込み時間などのパフォーマンスメトリクスを追跡します。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Adaptive Bit Rate (ABR)**: データサイズ、日付範囲、ネットワーク状態に基づいてデータ解像度を自動調整し、最適なパフォーマンスを実現します。[](https://developers.cloudflare.com/web-analytics/about/)
- **無料で利用可能**: DNSを変更したりCloudflareのプロキシを使用したりしなくても、Cloudflareアカウントを持つ誰でも利用できます。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **ダッシュボードとフィルター**: ホスト名、URL、国、時間範囲でデータを表示およびフィルタリングするための直感的なダッシュボードを提供します。特定の期間にズームインしたり、メトリクスでデータをグループ化して詳細な分析を行ったりできます。[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **Single Page Application (SPA) サポート**: History APIの`pushState`関数をオーバーライドすることで、SPA内のルート変更を自動的に追跡します（ハッシュベースのルーターはサポートされていません）。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### 制限事項
- **データ保持**: 過去30日間の履歴データに限定されており、長期的な分析を必要とするユーザーには適さない場合があります。[](https://plausible.io/vs-cloudflare-web-analytics)
- **データサンプリング**: メトリクスはページ読み込みイベントの10%サンプルに基づいており、PlausibleやFathom Analyticsなどのツールと比較して不正確さにつながる可能性があります。[](https://plausible.io/vs-cloudflare-web-analytics)
- **不正確さへの懸念**: サーバーサイドアナリティクス（Edge Analytics）はボットトラフィックを含む可能性があり、Google Analyticsなどのクライアントサイドアナリティクスと比較して数値が膨張する可能性があります。クライアントサイドアナリティクスは、JavaScriptが無効なユーザーや広告ブロッカーを使用しているユーザーのデータを捕捉できない可能性があります。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **UTMパラメータのサポートなし**: 現在、機密データの収集を避けるため、UTMパラメータなどのクエリ文字列は記録されません。[](https://developers.cloudflare.com/web-analytics/faq/)
- **エクスポートの制限**: Fathom Analyticsなどの一部の競合製品とは異なり、データをCSVなどに直接エクスポートする方法はありません。[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **基本的なアナリティクス**: Google Analyticsと比較して、コンバージョン追跡や詳細なユーザージャーニー分析などの高度な機能が欠けています。[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### Cloudflare Web Analyticsの設定
#### 前提条件
- Cloudflareアカウント（cloudflare.comで無料作成可能）。
- ウェブサイトのコード（JavaScriptビーコン用）またはDNS設定（Cloudflareプロキシ使用時のEdge Analytics用）へのアクセス権。

#### 設定手順
1.  **Cloudflareダッシュボードにログイン**:
    - [cloudflare.com](https://www.cloudflare.com) にアクセスし、ログインまたはアカウントを作成します。
    - アカウントホームから、**Analytics & Logs** > **Web Analytics**に移動します。[](https://developers.cloudflare.com/web-analytics/get-started/)

2.  **サイトを追加**:
    - Web Analyticsセクションで**Add a site**をクリックします。
    - ウェブサイトのホスト名（例: `example.com`）を入力し、**Done**を選択します。[](https://developers.cloudflare.com/web-analytics/get-started/)

3.  **データ収集方法を選択**:
    - **JavaScript Beacon (非プロキシサイト推奨)**:
      - **Manage site**セクションから提供されたJavaScriptスニペットをコピーします。
      - それをウェブサイトのHTMLの終了`</body>`タグの前に貼り付けます。スニペットが機能するために、サイトに有効なHTMLがあることを確認してください。[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
      - シングルページアプリケーションの場合は、自動ルート追跡のために設定で`spa: true`が設定されていることを確認してください（ハッシュベースのルーターはサポートされていません）。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
      - Nuxtアプリの例: `useScriptCloudflareWebAnalytics` composableを使用するか、トークンをNuxt configに追加してグローバルに読み込みます。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
    - **Edge Analytics (プロキシサイト用)**:
      - DNS設定を更新してCloudflareのネームサーバーを指すようにし、ウェブサイトをCloudflare経由でプロキシします。これは数分で完了し、コード変更は必要ありません。[](https://www.cloudflare.com/en-in/web-analytics/)
      - メトリクスはCloudflareダッシュボードの**Analytics & Logs**に表示されます。[](https://developers.cloudflare.com/web-analytics/faq/)
    - **Cloudflare Pages**:
      - Pagesプロジェクトの場合、ワンクリックでWeb Analyticsを有効にできます: **Workers & Pages**からプロジェクトを選択し、**Metrics**に移動して、Web Analyticsの下の**Enable**をクリックします。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4.  **設定を確認**:
    - データがダッシュボードに表示されるまで数分かかる場合があります。**Web Analytics Sites**セクションでサイトが追加されていることを確認してください。[](https://developers.cloudflare.com/web-analytics/get-started/)
    - Edge Analyticsを使用している場合は、DNSの伝播が完了していることを確認してください（24〜72時間かかる場合があります）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5.  **ルールを設定 (オプション)**:
    - 特定のウェブサイトやパスを追跡するためのルールを設定します。ディメンションを使用してメトリクスを分類します（例: ホスト名やURLによる）。[](https://developers.cloudflare.com/web-analytics/)

#### 注意点
- サイトに`Cache-Control: public, no-transform`ヘッダーがある場合、JavaScriptビーコンは自動的に注入されず、Web Analyticsが機能しない可能性があります。キャッシュ設定を調整するか、手動でスニペットを追加してください。[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- 一部の広告ブロッカーはJavaScriptビーコンをブロックする可能性がありますが、Edge Analyticsはサーバーログに依存するため影響を受けません。[](https://developers.cloudflare.com/web-analytics/faq/)
- 手動設定の場合、ビーコンは`cloudflareinsights.com/cdn-cgi/rum`にレポートします。プロキシサイトの場合、ドメインの`/cdn-cgi/rum`エンドポイントを使用します。[](https://developers.cloudflare.com/web-analytics/faq/)

### Cloudflare Web Analyticsの使用方法
1.  **ダッシュボードにアクセス**:
    - Cloudflareダッシュボードにログインし、アカウントとドメインを選択して、**Analytics & Logs** > **Web Analytics**に移動します。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
    - ページビュー、訪問数、人気ページ、参照元、国、デバイスタイプ、パフォーマンスデータ（ページ読み込み時間、Core Web Vitalsなど）などのメトリクスを表示します。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2.  **データのフィルタリングと分析**:
    - フィルターを使用して特定のメトリクス（ホスト名、URL、国など）に焦点を当てます。
    - 時間範囲をズームインしてトラフィックの急増を調査したり、参照元やページなどのメトリクスでデータをグループ化したりします。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
    - 上級ユーザーは、**GraphQL Analytics API**を介してデータをクエリし、カスタムダッシュボードを作成できます。[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3.  **主要メトリクスの理解**:
    - **ページビュー**: ページが読み込まれた合計回数（HTMLコンテンツタイプで成功したHTTPレスポンス）。[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
    - **訪問数**: 異なる参照元（ホスト名と一致しない）または直接リンクからのページビュー。[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
    - **ユニーク訪問者**: IPアドレスに基づきますが、プライバシー上の理由で保存されません。ボットトラフィックやJavaScriptベースの重複排除がないため、他のツールよりも高くなる可能性があります。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
    - **パフォーマンスメトリクス**: ページ読み込み時間、first paint、Core Web Vitals（クライアントサイドのみ）を含みます。[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4.  **他のツールとの比較**:
    - Google Analyticsとは異なり、Cloudflareはユーザージャーニーやコンバージョンを追跡しませんが、ボットや脅威トラフィックを含むため、数値が膨張する可能性があります（ほとんどのサイトでトラフィックの20〜50%）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
    - PlausibleやFathom Analyticsと比較して、Cloudflareのデータはサンプリングと保持期間の制限により、粒度が粗いです。[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
    - Edge Analyticsは、ボットや非JavaScriptリクエストを除外するGoogle Analyticsなどのクライアントサイドツールよりも高い数値を示す可能性があります。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### ベストプラクティス
- **適切な方法の選択**: プライバシー重視のクライアントサイドメトリクスにはJavaScriptビーコンを、サイトがプロキシされている場合の包括的なサーバーサイドデータにはEdge Analyticsを使用します。[](https://www.cloudflare.com/web-analytics/)
- **他のツールとの組み合わせ**: Cloudflareのアナリティクスは基本的なものであるため、より深い洞察を得るために、Google AnalyticsやPlausible、Fathomなどのプライバシー重視の代替ツールと組み合わせます。[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **パフォーマンスの監視**: パフォーマンスメトリクスを使用して読み込みの遅いページを特定し、Cloudflareの推奨事項（キャッシュ最適化など）を活用します。[](https://developers.cloudflare.com/web-analytics/)
- **広告ブロッカーの問題を確認**: JavaScriptビーコンを使用している場合、データ収集を確実にするために、ユーザーに`cloudflare.com`を許可するか広告ブロッカーを無効にするよう通知します。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **定期的なデータの確認**: データは30日間のみ保持されるため、傾向や異常を発見するためにダッシュボードを頻繁に確認します。[](https://plausible.io/vs-cloudflare-web-analytics)

### トラブルシューティング
- **データが表示されない**:
  - JavaScriptスニペットが正しく配置され、サイトに有効なHTMLがあることを確認してください。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - Edge Analyticsの場合、DNSがCloudflareを指していることを確認してください（伝播に24〜72時間かかる場合があります）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - 自動ビーコン注入をブロックしている`Cache-Control: no-transform`ヘッダーがないか確認してください。[](https://developers.cloudflare.com/web-analytics/get-started/)
- **不正確な統計**:
  - Edge Analyticsはボットトラフィックを含むため、数値が膨張します。より正確な訪問者数を得るにはクライアントサイドアナリティクスを使用してください。[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - データサンプリング（10%）により不一致が生じる可能性があります。他のツールと比較する際はこれを考慮してください。[](https://plausible.io/vs-cloudflare-web-analytics)
- **広告ブロッカーの問題**: 一部のブラウザ拡張機能がJavaScriptビーコンをブロックします。Edge Analyticsはこれの影響を受けません。[](https://developers.cloudflare.com/web-analytics/faq/)
- **SPAメトリクスが欠落**: SPAサポートが有効（`spa: true`）であることを確認し、ハッシュベースのルーターを避けてください。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### 高度な使用方法
- **GraphQL Analytics API**: カスタムアナリティクスの場合、CloudflareのAPIをクエリして、 tailored ダッシュボードを構築したり他のシステムと統合したりします。技術的専門知識が必要です。[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers**: アナリティクスデータを時系列データベースに送信してカスタム処理を行ったり、高度なサーバーレスアナリティクスにWorkersを使用したりします。[](https://developers.cloudflare.com/analytics/)
- **セキュリティインサイト**: CloudflareのSecurity Analyticsと組み合わせて、訪問者データとともに脅威やボットを監視します。[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### 代替手段との比較
- **Google Analytics**: 詳細なユーザージャーニー追跡とコンバージョンを提供しますが、CookieとJavaScriptに依存し、ブロックされる可能性があります。Cloudflareはよりシンプルでプライバシー重視ですが、機能は少なめです。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics**: オープンソース、プライバシー優先で、無制限のデータ保持とサンプリングなしを特徴とします。ユニーク訪問者に関してより正確ですが、有料プランが必要です。[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics**: Plausibleと同様で、エクスポート可能なデータとキャンペーン追跡などの高度な機能を備えています。Cloudflareの無料提供は堅牢さでは劣りますが、基本的なニーズにはより簡単に設定できます。[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats**: WordPress専用で、データ保持期間が限られ（28日間）、ユーザーレベルの追跡はありません。同様のプライバシー重視ですが、Cloudflareよりも柔軟性に欠けます。[](https://wordpress.com/support/stats/)

### 追加リソース
- **公式ドキュメント**: [Cloudflare Web Analytics Docs](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **設定ガイド**: [Enabling Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **FAQ**: [Cloudflare Web Analytics FAQs](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **ブログ記事**: [Cloudflare’s Privacy-First Web Analytics](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **コミュニティサポート**: 追加のヘルプについてはCloudflareのコミュニティフォーラムを確認してください。[](https://developers.cloudflare.com/web-analytics/faq/)

### 結論
Cloudflare Web Analyticsは、最小限の設定で、無料かつプライバシー重視のアナリティクスツールを求めるウェブサイト所有者にとって優れた選択肢です。基本的なトラフィックとパフォーマンスの監視には理想的ですが、データサンプリング、保持期間の制限、コンバージョン追跡などの機能の欠如により、高度なニーズには物足りない場合があります。より深い洞察を得るには、PlausibleやFathom Analyticsなどのツールと組み合わせることを検討してください。データを解釈する際は、設定の正確性を常に確認し、制限事項を認識するようにしてください。

設定に関する具体的な支援や、サイトへのCloudflare Web Analyticsの統合について質問がある場合は、お知らせください！