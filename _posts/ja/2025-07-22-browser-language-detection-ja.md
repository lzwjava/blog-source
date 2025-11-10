---
audio: false
generated: true
lang: ja
layout: post
title: ユーザーの言語設定の検出
translated: true
type: note
---

### ユーザーの国と言語設定の検出

あなたのJekyllブログは静的（生成されたHTML/JS）であるため、ホスティングプラットフォームとの統合（Netlify関数やGitHub Pagesの制限付きサポートなど）なしでは、サーバーサイドでの検出を簡単に行うことはできません。最適なアプローチは、ページ読み込み時のクライアントサイドJavaScript検出です。主に2つの選択肢があります：

1. **ブラウザ言語設定（あなたのユースケースに推奨）**：これはユーザーのブラウザ設定から優先言語を検出します（`navigator.language` または `navigator.languages` 経由）。高速で、外部APIを必要とせず、ユーザーのプライバシーを尊重し（IP共有なし）、国ではなく言語に直接関連付けられます。国には複数の言語が存在することが多いため（例：インドではヒンディー語と並んで英語が広く使用される）、ドロップダウンの自動設定にはより正確です。

2. **IPベースの国検出**：これは無料の地理位置情報APIを使用してユーザーのIPアドレスから国を取得し、それを言語にマッピングします。国情報が特に必要な場合（例：分析用）に有用ですが、外部フェッチが必要で、プライバシー上の問題がある可能性があり、常に正確とは限りません（VPN、プロキシ）。国から言語へのマッピングは近似値です。

あなたの目標は、`<select id="sort-select">` ドロップダウンで言語を自動選択すること（例：英語の場合は 'date-desc|en'）のようです。両方の方法のコードを提供しますので、`<script>` タグ内の `const sortSelect = document.getElementById('sort-select');` の直後に追加してください。

`localStorage` のチェックを優先し（あなたのコードですでに行われている通り）、保存された設定がない場合に検出にフォールバックします。

#### オプション1: ブラウザ言語の使用（よりシンプルで推奨）
このコードスニペットを追加してください。`navigator.language` から主要言語コードをチェックし（例：'en-US' -> 'en', 'zh-CN' -> 'zh'）、あなたのドロップダウン値にマッピングします。一致がない場合は英語にデフォルト設定します。

```javascript
// Inside window.addEventListener('load', function () { ... });

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detect browser language if no saved preference
  let lang = navigator.language.toLowerCase().split('-')[0]; // e.g., 'en-US' -> 'en'
  
  // Special handling for Chinese variants (zh-Hant for traditional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Simplified Chinese
    }
  }

  // Map to your dropdown options (add more if needed)
  const langMap = {
    'en': 'date-desc|en',
    'zh': 'date-desc|zh',
    'ja': 'date-desc|ja',
    'es': 'date-desc|es',
    'hi': 'date-desc|hi',
    'fr': 'date-desc|fr',
    'de': 'date-desc|de',
    'ar': 'date-desc|ar',
    'hant': 'date-desc|hant'
  };

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Default to English
}

updatePosts();
```

これは読み込み時に同期的に実行されるため、遅延はありません。ブラウザの言語設定を変更してテストしてください（例：Chrome：設定 > 言語）。

#### オプション2: IPベースの国検出の使用
これには無料APIへの非同期フェッチが必要です。シンプルで国コードのみを返す（例：{country: 'US'}）`country.is` を推奨します。無料で、APIキー不要、オープンソースです。

このコードを追加してください。注意：非同期であるため、UIのブロックを避けるために `await` を使用し、async関数内でラップします。フェッチが失敗した場合（例：アドブロッカー）、英語にデフォルト設定します。

```javascript
// Inside window.addEventListener('load', async function () { ... });  // Make the load handler async

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Fetch country code
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // e.g., 'US'

    // Map country codes to your languages (ISO 3166-1 alpha-2 codes)
    // This is approximate; expand as needed (e.g., multiple countries per language)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> English
      'GB': 'date-desc|en',  // UK -> English
      'CN': 'date-desc|zh',  // China -> Simplified Chinese
      'TW': 'date-desc|hant', // Taiwan -> Traditional Chinese
      'HK': 'date-desc|hant', // Hong Kong -> Traditional Chinese
      'JP': 'date-desc|ja',  // Japan -> Japanese
      'ES': 'date-desc|es',  // Spain -> Spanish
      'MX': 'date-desc|es',  // Mexico -> Spanish (example for Latin America)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // France -> French
      'DE': 'date-desc|de',  // Germany -> German
      'SA': 'date-desc|ar',  // Saudi Arabia -> Arabic
      'AE': 'date-desc|ar'   // UAE -> Arabic
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Default to English
  } catch (error) {
    console.warn('Country detection failed:', error);
    sortSelect.value = 'date-desc|en'; // Fallback
  }

  updatePosts();
}
```

- **注意点**:
  - `window.addEventListener` を `async function ()` に更新してください（上記の通り）。
  - プライバシーについて：必要に応じてユーザーに通知してください（EUのGDPR）。一部のブラウザ/APIはクロスオリジンリクエストをブロックする可能性があるため、十分にテストしてください。
  - 別のAPIを希望する場合、代替として `https://ip-api.com/json/`（`{ "countryCode": "US" }` のようにより多くのデータを返す）や `https://ipgeolocation.io/ip_location/`（無料ティアに登録）があります。
  - レート制限：個人ブログには十分ですが、トラフィックが増加した場合は監視してください。

#### 追加の考慮事項
- **フォールバックとユーザーオーバーライド**：ユーザーはいつでもドロップダウンを変更でき、それはlocalStorageに保存されます。自動検出が常に望ましくない場合は、「言語を検出」ボタンを追加することもできます。
- **テスト**：VPNを使用して異なる国をシミュレートしたり、ブラウザ拡張機能を使用して言語を偽装したりしてください。
- **プライバシー**：ブラウザ言語はリスクが低いです。IPメソッドの場合、対象ユーザーが敏感な場合は同意プロンプトの追加を検討してください。
- **両方の組み合わせ**：まずブラウザ言語を使用し、サポートされている言語と一致しない場合にIPを使用します（ただし、シンプルに保ってください）。
- **Jekyll固有**：Jekyll設定の変更は必要ありません。Netlify/Vercelでホストする場合、サーバーサイド検出にエッジ関数を使用できますが、ここでは過剰です。

これが機能しない場合やエラーを共有できる場合は、詳細を提供してください！

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)