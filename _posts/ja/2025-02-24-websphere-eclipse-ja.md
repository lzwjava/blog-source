---
audio: false
lang: ja
layout: post
title: WebSphere Liberty を Eclipse で使用する
translated: true
---

WebSphere プラグインツールを Eclipse で使用し、WebSphere Liberty と統合して作業するには、2つの主要なオプションを選択できます：**IBM Liberty Developer Tools** と **Liberty Tools**。どちらも Eclipse Marketplace を通じて利用可能であり、WebSphere Liberty 上でアプリケーションをビルド、デプロイ、管理するための機能を提供します。以下は、これらのツールを使用して統合するための詳細なガイドです。

---

### **ツールの概要**
- **IBM Liberty Developer Tools**: IBM が提供する伝統的なプラグインで、Eclipse 内で Liberty サーバーを管理します。Liberty サーバーを作成および管理し、アプリケーションをデプロイし、IDE からデバッグすることができます。このツールは、サーバー中心のワークフローや Maven や Gradle を使用していないプロジェクトに適しています。
- **Liberty Tools**: Maven と Gradle プロジェクトに焦点を当てた次世代のオープンソースの代替手段です。ビルドツールとの統合が強化され、Liberty プロジェクトの自動検出、Liberty の開発モード（dev モード）のサポートが提供されます。このツールは、現代的なビルドツール中心のワークフローに適しています。

どちらのツールも WebSphere Liberty の開発を効率化しますが、アプローチが異なります。プロジェクトの種類と開発の好みに最適なものを選択してください。

---

### **インストール**
1. **Eclipse のインストール**:
   - 互換性のあるバージョンを使用します。例えば、**Eclipse for Enterprise Java and Web Developers**。
   - Eclipse のバージョンが選択したプラグインをサポートしていることを確認します（マーケットプレイスのリストで互換性を確認）。

2. **プラグインのインストール**:
   - Eclipse を開き、**Help > Eclipse Marketplace** に移動します。
   - 検索:
     - 伝統的な IBM ツールセットの場合は「IBM Liberty Developer Tools」、または
     - オープンソースの代替手段の場合は「Liberty Tools」。
   - プロンプトに従って希望のプラグインをインストールします。

---

### **Liberty ランタイムの設定**
- **Liberty のダウンロード**:
  - まだダウンロードしていない場合は、[公式の IBM ウェブサイト](https://www.ibm.com/docs/en/was-liberty) から WebSphere Liberty ランタイムをダウンロードします。
  - Liberty のバージョンがインストールしたプラグインと互換性があることを確認します。

- **Eclipse でのランタイムの設定**:
  - **IBM Liberty Developer Tools** の場合:
    - **Window > Preferences > Server > Runtime Environments** に移動します。
    - 「Add」をクリックし、「Liberty Server」を選択し、Liberty のインストールディレクトリのパスを指定します。
  - **Liberty Tools** の場合:
    - 明示的なランタイム設定は必要ありません。Liberty Tools は Maven または Gradle の設定を通じて Liberty プロジェクトを検出するため、プロジェクトが適切に設定されていることを確認します（以下を参照）。

---

### **プロジェクトとの統合**
統合プロセスはツールによって少し異なります。インストールしたツールに基づいて以下の手順を実行します。

#### **IBM Liberty Developer Tools の場合**
1. **Liberty サーバーの作成**:
   - **Servers** ビューを開きます (**Window > Show View > Servers**).
   - Servers ビューで右クリックし、**New > Server** を選択します。
   - リストから「Liberty Server」を選択し、サーバーの設定ウィザードに従って設定します。Liberty のインストールディレクトリのパスを指定します。

2. **プロジェクトの追加**:
   - Servers ビューでサーバーを右クリックし、**Add and Remove...** を選択します。
   - プロジェクトを選択し、「Configured」側に移動します。

3. **サーバーの起動**:
   - サーバーを右クリックし、**Start** または **Debug** を選択してアプリケーションを実行します。
   - 指定された URL（デフォルト: `http://localhost:9080/<context-root>`）でアプリケーションにアクセスします。

#### **Liberty Tools (Maven/Gradle プロジェクト) の場合**
1. **プロジェクト設定の確認**:
   - プロジェクトには必要な Liberty プラグインが含まれている必要があります:
     - Maven の場合: `pom.xml` に `liberty-maven-plugin` を追加します。
     - Gradle の場合: `build.gradle` に `liberty-gradle-plugin` を追加します。
   - `server.xml` 構成ファイルは標準の場所にあります:
     - Maven の場合: `src/main/liberty/config`。
     - Gradle の場合: プロジェクト構造に基づいて調整します。

2. **Liberty ダッシュボードの使用**:
   - Eclipse ツールバーの Liberty アイコンをクリックして **Liberty Dashboard** を開きます。
   - Liberty Tools は自動的にプロジェクトを検出し、ダッシュボードにリストします。
   - ダッシュボード内のプロジェクトを右クリックして、以下のコマンドにアクセスします:
     - 「dev モードで開始」（サーバーを再起動せずに変更を自動的に再デプロイ）。
     - 「テストの実行」。
     - 「テストレポートの表示」。

3. **アプリケーションへのアクセス**:
   - サーバーが実行中の場合、指定された URL（デフォルト: `http://localhost:9080/<context-root>`）でアプリケーションにアクセスします。
   - dev モードでは、コードに変更を加えると、Liberty が自動的に再デプロイします。

---

### **主要機能**
両方のツールは生産性を向上させる強力な機能を提供します:

- **サーバー管理**:
  - Eclipse から Liberty サーバーを開始、停止、デバッグします。
- **アプリケーションのデプロイ**:
  - アプリケーションを簡単にデプロイおよび再デプロイします。
- **構成のサポート**:
  - 両方のツールは、Liberty 構成ファイル（例: `server.xml`）のコード補完、検証、ホバー説明を提供します。
- **開発モード**:
  - サーバーを再起動せずにコードの変更を自動的に検出および再デプロイします（特に Liberty Tools の dev モード）。
- **デバッグ**:
  - Eclipse デバッガを Liberty サーバーにアタッチしてトラブルシューティングを行います。

---

### **考慮事項と潜在的な問題**
- **バージョンの互換性**:
  - Eclipse、プラグイン、Liberty ランタイムのバージョンが互換性があることを確認します。特定の要件についてはドキュメントを参照してください。
- **プロジェクトの設定**:
  - Liberty Tools の場合、プロジェクトは適切に設定された Maven または Gradle プロジェクトで、Liberty プラグインが含まれている必要があります。
  - ツールがプロジェクトを認識するために、`server.xml` が期待される場所にあることを確認します。
- **ネットワーク設定**:
  - デフォルトの Liberty ポート（例: HTTP の 9080、HTTPS の 9443）が開いており、ファイアウォールによってブロックされていないことを確認します。
- **Java の互換性**:
  - Liberty は Java ベースのサーバーであるため、Liberty ランタイムに対応する Java バージョンがインストールされていることを確認します。

---

### **Liberty Tools (Maven/Gradle) のクイックスタート**
Maven または Gradle を使用している場合、Liberty Tools はスムーズな体験を提供します。以下はステップバイステップのガイドです:

1. **Eclipse for Enterprise Java and Web Developers** をインストールします。
2. **Help > Eclipse Marketplace** に移動し、「Liberty Tools」を検索してプラグインをインストールします。
3. Maven/Gradle プロジェクトを作成またはインポートし、Liberty に設定します:
   - [Open Liberty Starter](https://openliberty.io/start/) を使用してサンプルプロジェクトを生成できます。
4. プロジェクトに `liberty-maven-plugin`（Maven）または `liberty-gradle-plugin`（Gradle）が設定されていることを確認します。
5. ツールバーの Liberty アイコンをクリックして **Liberty Dashboard** を開きます。
6. プロジェクトがダッシュボードに表示されるはずです。右クリックして「dev モードで開始」を選択します。
7. 指定された URL（デフォルト: `http://localhost:9080/<context-root>`）でアプリケーションにアクセスします。
8. コードに変更を加えると、Liberty dev モードが自動的に再デプロイします。
9. ダッシュボードを使用してテストを実行またはテストレポートを表示します。

---

### **ツールの選択**
- **IBM Liberty Developer Tools**:
  - 伝統的なサーバー管理アプローチや Maven や Gradle を使用していないプロジェクトに適しています。
  - Liberty サーバーを明示的に管理するための Servers ビューを提供します。
- **Liberty Tools**:
  - Maven または Gradle プロジェクトに適しており、これらのビルドシステムとの統合が強化されています。
  - プロジェクト中心の管理と dev モードのサポートを提供する Liberty ダッシュボードを提供します。
  - オープンソースであり、コミュニティの寄稿と更新が可能です。

どちらのツールも Eclipse Marketplace から利用可能なので、両方を試してワークフローに最適なものを選択してください。

---

要約すると、Eclipse で WebSphere プラグインツールを使用することは、適切なプラグインをインストールし、Liberty ランタイムを設定し、プロジェクトを Liberty と統合することです。IBM Liberty Developer Tools または Liberty Tools を選択しても、どちらも Eclipse IDE 内で WebSphere Liberty の開発を効率化するための強力な機能を提供します。