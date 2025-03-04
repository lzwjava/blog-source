---
audio: false
generated: true
lang: ja
layout: post
title: Google Analyticsを使用する
translated: true
---

Google Analytics を使用するには、フロントエンドプロジェクトに統合し、アプリとウェブサイトの両方でデータを確認するために、以下の手順に従ってください。このガイドは、フロントエンドプロジェクトがウェブサイトまたはモバイルアプリであり、2023年の現在の標準である **Google Analytics 4 (GA4)** を使用していることを前提としています。Universal Analytics は新しいデータ収集にはサポートされていません。

---

### 1. Google Analytics の設定
Google Analytics をプロジェクトに統合する前に、アカウントを作成し、設定する必要があります：

- **アカウントの作成**: [analytics.google.com](https://analytics.google.com) にアクセスし、Google アカウントでサインアップします（まだアカウントがない場合）。
- **GA4 プロパティの作成**:
  - 左下隅の「管理」をクリックします。
  - 「プロパティ」の下で「プロパティを作成」をクリックし、プロジェクトの詳細を入力し、**Google Analytics 4** を選択します。
- **データストリームの追加**: フロントエンドプロジェクトの種類に応じて：
  - **ウェブサイトの場合**: 「Web」を選択し、ウェブサイトの URL を入力し、ストリームに名前を付けます（例：「My Website」）。
  - **モバイルアプリの場合**: 「App」を選択し、iOS または Android を選択し、アプリの詳細を提供します（例：パッケージ名）。

データストリームの設定が完了すると、**測定 ID**（例：`G-XXXXXXXXXX`）が表示され、統合に使用します。

---

### 2. フロントエンドプロジェクトに Google Analytics を統合
統合プロセスは、フロントエンドプロジェクトがウェブサイトかモバイルアプリかによって異なります。

#### ウェブサイトの場合
- **Google タグの追加**:
  - GA4 プロパティで「データストリーム」を選択し、ウェブストリームを選択し、「タグ付けの手順」を確認します。
  - 提供された **Google タグ** スクリプトをコピーします。以下のように表示されます：
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - このコードをウェブサイトの HTML の `<head>` セクションに貼り付け、`YOUR_MEASUREMENT_ID` を実際の測定 ID に置き換えます。
- **シングルページアプリケーション (SPA)** (例：React、Angular、Vue) の場合：
  - デフォルトのスクリプトは初期ページ読み込みのみを追跡します。SPA では、ルートの変更時にページが再読み込みされないため、ナビゲーションを追跡するためのライブラリを使用します。例えば、React の場合：
    1. `react-ga4` ライブラリをインストールします：
       ```bash
       npm install react-ga4
       ```
    2. アプリで初期化します（例：`index.js` または `App.js`）：
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. ルートの変更時にページビューを追跡します（例：React Router を使用）：
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       ルートが変更されるたびにこのコールを呼び出し、ルーターの場所に関連付けられた `useEffect` フック内で呼び出します。
  - 他のフレームワーク（例：Angular の `ngx-analytics`、Vue の `vue-ga`）にも同様のライブラリがあります（GA4 対応を確認してください）。
- **オプション**: **Google Tag Manager (GTM)** を使用して、追跡スクリプトの管理を簡単にすることもできます。

#### モバイルアプリの場合
- **Firebase を使用する（推奨）**:
  - アプリが Firebase を使用している場合、Google Analytics for Firebase を有効にします：
    1. [console.firebase.google.com](https://console.firebase.google.com) で Firebase プロジェクトを作成します。
    2. プロジェクトにアプリ（iOS または Android）を追加します。
    3. プロンプトに従って設定ファイル（例：iOS の `GoogleService-Info.plist`、Android の `google-services.json`）をダウンロードし、アプリに追加します。
    4. Firebase SDK をインストールします：
       - **iOS**: CocoaPods を使用して (`pod 'Firebase/Analytics'`) インストールし、`AppDelegate` で初期化します。
       - **Android**: `build.gradle` に依存関係を追加し、アプリで初期化します。
    5. Firebase は自動的に GA4 プロパティにリンクされ、データの収集を開始します。
- **Firebase を使用しない場合**:
  - 独立した **Google Analytics SDK** を iOS または Android 用に使用します（GA4 の Firebase 統合が一般的になりました）。設定はプラットフォームによって異なるため、公式のドキュメントを参照してください。

---

### 3. 統合の確認
- **ウェブサイトの場合**: トラッキングコードを追加した後：
  - ウェブサイトにアクセスし、Google Analytics の **リアルタイム** レポートを開きます（「レポート」 > 「リアルタイム」）。
  - 訪問がログに記録されている場合、統合が正常に動作しています。
  - 代替として、ブラウザツール（例：GA Checker）または Chrome DevTools コンソールを使用して `gtag` コールを確認します。
- **アプリの場合**: SDK がインストールされたアプリを起動した後、Firebase コンソールまたは GA4 リアルタイム レポートを確認します。データが表示されるまで数分かかることがあります。

---

### 4. アプリとウェブサイトでデータを確認
Google Analytics がデータの収集を開始すると、2つの方法で確認できます：
- **Google Analytics ウェブインターフェース**:
  - [analytics.google.com](https://analytics.google.com) にログインします。
  - GA4 プロパティを選択します。
  - レポートを探索します：
    - **リアルタイム**: 実時ユーザー活動を確認します。
    - **オーディエンス**: ユーザーのデモグラフィックを理解します。
    - **アクイジション**: ユーザーがどこから来たかを追跡します。
    - **ビヘイビア**: ユーザーのインタラクションを分析します（例：ページビュー、イベント）。
- **Google Analytics モバイルアプリ**:
  - 公式の **Google Analytics アプリ** を App Store（iOS）または Google Play Store（Android）からダウンロードします。
  - Google アカウントでサインインし、プロパティを選択します。
  - 一部のレポート（例：リアルタイム、オーディエンス）を移動中に確認します。

---

### 追加の注意事項
- **プロジェクトにウェブサイトとアプリの両方が含まれている場合**: 同じ GA4 プロパティの下に複数のデータストリーム（例：ウェブサイト用、アプリ用）を追加できます。これにより、同じインターフェースで統合または個別の分析を表示できます。
- **イベントの追跡**: ページビュー以上にカスタムイベント（例：ボタンのクリック）を追跡します。ウェブサイトの場合は `gtag('event', ...)` を使用し、アプリの場合は Firebase の `logEvent` を使用します。ウェブサイトの例：
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 と Universal Analytics**: 新しいプロジェクトには GA4 を使用してください。Universal Analytics は 2023 年 7 月 1 日以降、データの処理を停止しました。

これらの手順に従うことで、フロントエンドプロジェクトに Google Analytics を成功裏に統合し、Google Analytics ウェブサイトとモバイルアプリの両方でユーザーデータを監視できます。プロジェクトの種類（ウェブサイトまたはアプリ）に応じて、統合手順を適宜調整してください！