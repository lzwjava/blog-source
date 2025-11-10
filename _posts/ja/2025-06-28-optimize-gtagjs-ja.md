---
audio: false
generated: true
lang: ja
layout: post
title: Jekyll GitHub Pagesにおけるgtag.jsパフォーマンスの最適化
translated: true
type: note
---

GitHub PagesでJekyllを使って構築されたサイトで`gtag.js`を使用する場合、GitHub Pagesのサーバー側制御が限られており、キャッシュヘッダーやサーバーサイドスクリプティングに直接アクセスできないという特有の制約があります。しかし、クライアントサイドの技術とJekyll特有の設定を使用して、`https://www.googletagmanager.com/gtag/js?id=UA-66656236-1`の取得速度を最適化することは可能です。以下に、このコンテキストでのパフォーマンスを改善するための具体的な戦略を示します：

---

### 1. **`gtag.js`を非同期で読み込む**
ページのレンダリングをブロックしないように、`gtag.js`スクリプトが非同期で読み込まれることを確認してください。Jekyllサイトでは：
- スクリプトをJekyllのレイアウトまたはインクルードファイル（例：`_includes/analytics.html`、または直接`default.html`レイアウト）に追加します。
- `async`属性を使用します：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- これをJekyllテンプレート（例：`_layouts/default.html`）の`<head>`内または`</body>`の直前に配置します：
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **効果**: `async`により、スクリプトがHTMLの解析をブロックしないため、体感される読み込み時間が短縮されます。

---

### 2. **GoogleのドメインへのPreconnectを追加**
`googletagmanager.com`への`preconnect`ヒントを追加して、DNSルックアップと接続のレイテンシを削減します。Jekyllレイアウト（`_layouts/default.html`または`_includes/head.html`）に以下を追加：
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- これを`<head>`内の`gtag.js`スクリプトの前に配置します。
- **効果**: DNS解決とTCP接続を早期に開始し、`gtag.js`の取得を高速化します。

---

### 3. **`gtag.js`のレイジーロード**
GitHub Pagesは静的サイトであるため、`gtag.js`をレイジーロードして重要なコンテンツを優先させることができます。以下のJavaScriptをJekyllテンプレートまたは別のJSファイル（例：`assets/js/analytics.js`）に追加します：
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- このスクリプトをJekyllレイアウトに含めます：
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **効果**: `gtag.js`の読み込みをページの重要なリソース（HTML、CSSなど）が読み込まれるまで遅らせ、初期ページ速度を改善します。

---

### 4. **Cloudflare経由のCDNプロキシを使用**
GitHub Pagesではカスタムキャッシュヘッダーを設定できませんが、CloudflareなどのCDNを通じて`gtag.js`をプロキシし、ユーザーに近い場所でキャッシュすることができます：
1. **Cloudflareの設定**:
   - GitHub PagesサイトをCloudflareに追加します（例：`username.github.io`）。
   - ドメインに対してCloudflareのDNSとプロキシを有効にします。
2. **`gtag.js`のプロキシ**:
   - CloudflareでPage Ruleを作成して`gtag.js`スクリプトをキャッシュするか、Jekyllサイトの`_site`フォルダ内（例：`assets/js/gtag.js`）にローカルコピーをホストします。
   - スクリプトタグを更新します：
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - ローカルコピーをGoogleの`gtag.js`と定期的に同期させ、最新版を維持します（手動プロセスまたはCI/CDスクリプト経由）。
3. **キャッシュ設定**:
   - Cloudflareでスクリプトに対するキャッシュルールを設定します（例：TTLを1時間に設定した`Cache Everything`）。
- **効果**: Cloudflareのエッジサーバーがスクリプトをユーザーに近い場所から配信することで、レイテンシを削減します。
- **注意**: Googleのスクリプトをプロキシする場合は、頻繁に更新される可能性があるため、トラッキングが機能することを十分にテストしてください。

---

### 5. **Jekyllのビルドと配信の最適化**
Jekyllサイトが全体的なページ読み込み時間を最小化するように最適化されていることを確認します。これは間接的に`gtag.js`のパフォーマンスに役立ちます：
- **アセットの最小化**:
  - `jekyll-compress`や`jekyll-minifier`などのJekyllプラグインを使用して、HTML、CSS、JSを最小化します。
  - `_config.yml`に追加：
```yaml
plugins:
  - jekyll-compress
```
- **Gzip圧縮の有効化**:
  - GitHub Pagesはサポートされているファイルに対して自動的にGzipを有効にしますが、ブラウザの開発者ツールで`Content-Encoding`ヘッダーを確認してCSS/JSファイルが圧縮されていることを確認してください。
- **ブロッキングリソースの削減**:
  - `gtag.js`の前に読み込まれるレンダーブロッキングとなるCSS/JSファイルの数を最小化します。
  - `jekyll-assets`などを使用してアセット配信を最適化：
```yaml
plugins:
  - jekyll-assets
```
- **クリティカルCSSのインライン化**:
  - クリティカルCSSを`<head>`内にインライン化し、非クリティカルCSSの読み込みを遅延させて、レンダーブロッキング時間を削減します。これにより`gtag.js`の読み込みが速く感じられるようになります。
- **画像最適化**:
  - `jekyll-picture-tag`などのプラグインを使用して画像を圧縮し、ページ全体の重量を減らし、`gtag.js`用の帯域幅を確保します。

---

### 6. **Minimal Analyticsへの切り替え**
`gtag.js`が依然として遅い場合、またはアナリティクスが重要でない場合：
- PlausibleやFathomなどの軽量な代替案を検討してください。これらのスクリプトは`gtag.js`（約50KB）に比べて小さく（約1KB）なっています。
- Plausibleの例：
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- これをJekyllの`_includes/analytics.html`に追加し、レイアウトに含めます。
- **効果**: 小さなスクリプトは、特にGitHub Pagesの静的インフラではより速く読み込まれます。

---

### 7. **パフォーマンスのテストと監視**
- **取得時間の計測**:
  - Chrome DevTools（Networkタブ）を使用して`gtag.js`の読み込み時間を確認します。
  - LighthouseやWebPageTestなどのツールを使用して、ページ全体のパフォーマンスを評価します。
- **ユーザー所在地のシミュレーション**:
  - Pingdomなどのツールを使用して、対象ユーザーがいる地域からの読み込み時間をテストします。GitHub PagesとGoogleのCDNのパフォーマンスは地理的に異なります。
- **実ユーザーメトリクスの監視**:
  - Google Analyticsを使用している場合は、Site Speedレポートを確認して`gtag.js`の影響を追跡します。
- **Jekyll特有のデバッグ**:
  - `jekyll build --profile`を実行して、サイト内のパフォーマンスに間接的に影響する可能性のあるビルドが遅いコンポーネントを特定します。

---

### 8. **GitHub Pagesの制限**
- **サーバーサイド制御なし**: GitHub Pagesは静的ホストであるため、`gtag.js`に対するサーバーサイドタグ付けやカスタムキャッシュヘッダーを実装できません。
- **HTTP/3なし**: GitHub PagesはHTTP/2を使用しています。これは高速ですが、HTTP/3ほど最適化されていません。CloudflareなどのCDNを使用するとHTTP/3にアップグレードできます。
- **地理的なレイテンシ**: GitHub Pagesのサーバーは主に米国に設置されているため、米国から遠く離れたユーザーは読み込みが遅くなる可能性があります。CDNを使用することでこれを緩和できます。

---

### Jekyll設定の例
`preconnect`と`async`を組み合わせた、Jekyllサイト用のサンプル`_includes/analytics.html`：
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
これをレイアウト（`_layouts/default.html`）に含めます：
```html
<head>
</head>
```

---

### 次のステップ
- **現在のパフォーマンスをテスト**: ブラウザの開発者ツールから取得した`gtag.js`の現在の取得時間、またはサイトのURLを共有していただければ、さらに分析できます。
- **地理的コンテキスト**: 主要な対象ユーザーの所在地（米国、ヨーロッパ、アジアなど）を教えてください。CDNやプロキシの推奨を調整します。
- **Cloudflareのセットアップ**: Cloudflareの使用にご興味があれば、`gtag.js`をプロキシするための詳細な手順を提供できます。
- **代替アナリティクス**: Google Analyticsからの切り替えにご興味があれば、特定の軽量ツールとそれらのJekyll連携方法を推奨できます。

これらの側面のいずれかに焦点を当ててほしいですか？または、特定の分析（サイトのパフォーマンステストやCloudflareセットアップガイドの提供など）を実行してほしいですか？