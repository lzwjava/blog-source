---
audio: false
generated: true
lang: ja
layout: post
title: Googleアナリティクスの使い方
translated: true
type: note
---

Google Analyticsを使用するには、フロントエンドプロジェクトに統合し、アプリとウェブサイトの両方でデータを確認する必要があります。以下の手順に従ってください。このガイドは、フロントエンドプロジェクトがウェブサイトまたはモバイルアプリのいずれかであり、**Google Analytics 4 (GA4)** を使用していることを前提としています（2023年現在の標準であり、Universal Analyticsは新しいデータ収集ではサポートされていません）。

---

### 1. Google Analyticsの設定
プロジェクトにGoogle Analyticsを統合する前に、アカウントを作成して設定する必要があります：

- **アカウントの作成**: [analytics.google.com](https://analytics.google.com) にアクセスし、Googleアカウントでサインアップします（まだ持っていない場合）。
- **GA4プロパティの作成**:
  - 左下の「管理」をクリックします。
  - 「プロパティ」で「プロパティを作成」をクリックし、プロジェクトの詳細を入力して **Google Analytics 4** を選択します。
- **データストリームの追加**: フロントエンドプロジェクトのタイプに応じて：
  - **ウェブサイトの場合**: 「ウェブ」を選択し、ウェブサイトのURLを入力し、ストリームに名前を付けます（例：「My Website」）。
  - **モバイルアプリの場合**: 「アプリ」を選択し、iOSまたはAndroidを選択し、アプリの詳細（例：パッケージ名）を入力します。

データストリームを設定すると、**測定ID**（例：`G-XXXXXXXXXX`）が取得されます。これは統合に使用します。

---

### 2. フロントエンドプロジェクトへのGoogle Analyticsの統合
統合プロセスは、フロントエンドプロジェクトがウェブサイトかモバイルアプリかによって異なります。

#### ウェブサイトの場合
- **Googleタグの追加**:
  - GA4プロパティで「データストリーム」に移動し、ウェブストリームを選択して「タグ付けの手順」を見つけます。
  - 提供された**Googleタグ**スクリプトをコピーします。以下のような形式です：
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
  - このコードをウェブサイトのHTMLの`<head>`セクションに貼り付け、`YOUR_MEASUREMENT_ID`を実際の測定IDに置き換えます。
- **シングルページアプリケーション (SPA)** の場合（例：React、Angular、Vue）:
  - デフォルトのスクリプトは初期ページ読み込みのみを追跡します。ルート変更時にページが再読み込みされないSPAでは、ナビゲーションを追跡するためにライブラリを使用します。例えば、**React**の場合：
    1. `react-ga4`ライブラリをインストールします：
       ```bash
       npm install react-ga4
       ```
    2. アプリで初期化します（例：`index.js`または`App.js`）：
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. ルート変更時にページビューを追跡します（例：React Routerを使用）：
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       これをルーターのロケーションに紐付いた`useEffect`フックなどで、ルートが変更されるたびに呼び出します。
  - 他のフレームワークにも同様のライブラリがあります（例：Angular用の`ngx-analytics`、Vue用の`vue-ga`—GA4互換性を確認してください）。
- **オプション**: トラッキングスクリプトの管理を容易にするために、タグをハードコーディングする代わりに **Google Tag Manager (GTM)** を使用します。

#### モバイルアプリの場合
- **Firebaseを使用する（推奨）**:
  - アプリがFirebaseを使用している場合、**Google Analytics for Firebase**を有効にします：
    1. [console.firebase.google.com](https://console.firebase.google.com) でFirebaseプロジェクトを作成します。
    2. プロジェクトにアプリを追加します（iOSまたはAndroid）。
    3. プロンプトに従って設定ファイル（例：iOS用の`GoogleService-Info.plist`、Android用の`google-services.json`）をダウンロードし、アプリに追加します。
    4. Firebase SDKをインストールします：
       - **iOS**: CocoaPods（`pod 'Firebase/Analytics'`）を使用し、`AppDelegate`で初期化します。
       - **Android**: `build.gradle`に依存関係を追加し、アプリで初期化します。
    5. Firebaseは自動的にGA4プロパティにリンクされ、データ収集を開始します。
- **Firebaseを使用しない場合**:
  - スタンドアロンの **Google Analytics SDK** をiOSまたはAndroid用に使用します（GA4のFirebase統合により現在ではあまり一般的ではありません）。プラットフォームによって設定が異なるため、公式ドキュメントを参照してください。

---

### 3. 統合の検証
- **ウェブサイトの場合**: トラッキングコードを追加した後：
  - ウェブサイトにアクセスし、Google Analyticsの**リアルタイム**レポート（「レポート」>「リアルタイム」）を開きます。
  - 訪問が記録されていれば、統合は成功しています。
  - 代替として、**GA Checker**などのブラウザツールやChrome DevToolsコンソールを使用して`gtag`呼び出しを確認します。
- **アプリの場合**: SDKをインストールしたアプリを起動した後、FirebaseコンソールまたはGA4のリアルタイムレポートを確認します。データが表示されるまで数分かかる場合があります。

---

### 4. アプリとウェブサイトを使用したデータの確認
Google Analyticsがデータの収集を開始したら、以下の2つの方法でデータを確認できます：
- **Google Analyticsウェブインターフェース**:
  - [analytics.google.com](https://analytics.google.com) にログインします。
  - GA4プロパティを選択します。
  - 以下のようなレポートを確認します：
    - **リアルタイム**: ライブユーザーアクティビティを表示します。
    - **ユーザー**: ユーザーのデモグラフィックを理解します。
    - **集客**: ユーザーの流入元を追跡します。
    - **行動**: ユーザーのインタラクション（例：ページビュー、イベント）を分析します。
- **Google Analyticsモバイルアプリ**:
  - App Store（iOS）またはGoogle Play Store（Android）から公式の **Google Analyticsアプリ** をダウンロードします。
  - Googleアカウントでサインインし、プロパティを選択します。
  - 外出先でレポートの一部（例：リアルタイム、ユーザー）を表示します。

---

### 追加の注意点
- **プロジェクトにウェブサイトとアプリの両方が含まれる場合**: 同じGA4プロパティの下に複数のデータストリーム（例：ウェブサイト用とアプリ用）を追加できます。これにより、同じインターフェースで統合または個別の分析を表示できます。
- **イベントの追跡**: ページビューに加えて、カスタムイベント（例：ボタンクリック）を追跡します。ウェブサイトの場合は`gtag('event', ...)`を、アプリの場合はFirebaseの`logEvent`を使用します。ウェブサイトの例：
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4とUniversal Analytics**: Universal Analyticsは2023年7月1日以降データ処理を停止したため、新しいプロジェクトにはGA4を使用してください。

これらの手順に従うことで、Google Analyticsをフロントエンドプロジェクトに正常に統合し、Google Analyticsのウェブサイトとモバイルアプリの両方を使用してユーザーデータを監視できるようになります。プロジェクトタイプ（ウェブサイトまたはアプリ）に特定の説明が必要な場合は、統合手順を適宜調整してください！