---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Eclipse による WebSphere 開発
translated: true
type: note
---

### Eclipse での IBM WebSphere Application Server (WAS) を使用した開発

IBM WebSphere Application Server (WAS) は Java EE アプリケーションサーバーであり、Eclipse は WAS 向けのアプリケーションを開発、アセンブル、デプロイするための優れた IDE として機能します。この統合を実現する主要なツールが **IBM WebSphere Application Server Developer Tools for Eclipse** (略して WDT) です。このプラグインは、Eclipse 内で直接、サーバー管理、プロジェクト作成、デプロイ、デバッグ機能を提供します。従来型の WAS (v8.5 や v9.x など) と軽量な Liberty プロファイルの両方をサポートしています。

#### 必要なプラグイン
- **IBM WebSphere Application Server Developer Tools for Eclipse**: これが必須のプラグインです。使用する WAS ランタイム (例: V8.5x または V9.x ツール) に合ったバージョンを選択してください。Eclipse Marketplace から無料で入手可能で、Eclipse 2024-06 や 2025-03 などの最近のリリースをサポートしています。

他のプラグインは厳密には必須ではありませんが、フルな Java EE 開発を行うには、Eclipse インストールに Web Tools Platform (WTP) が含まれていることを確認してください。これは Eclipse IDE for Java EE Developers パッケージに標準で含まれています。

#### 前提条件
- Eclipse IDE for Java EE Developers (互換性のため、バージョン 2023-09 以降を推奨)。
- テストとデプロイ用に、ローカルにインストールされた IBM WAS ランタイム (従来型または Liberty)。
- Marketplace インストールのためのインターネットアクセス (またはオフラインファイルのダウンロード)。

#### インストール手順
WDT は、Eclipse Marketplace (最も簡単な方法)、アップデートサイト、またはダウンロードしたファイルを介してインストールできます。インストール後は Eclipse を再起動してください。

1. **Eclipse Marketplace 経由** (推奨):
   - Eclipse を開き、**ヘルプ > Eclipse Marketplace** に移動します。
   - "IBM WebSphere Application Server Developer Tools" を検索します。
   - 適切なバージョン (例: V9.x 用または V8.5x 用) を選択します。
   - **インストール** をクリックし、指示に従います。ライセンスに同意し、完了したら Eclipse を再起動します。

2. **アップデートサイト経由**:
   - **ヘルプ > 新規ソフトウェアのインストール** に移動します。
   - **追加** をクリックし、アップデートサイトの URL (例: 最新バージョンの場合は `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` — 最新版は IBM ドキュメントで確認) を入力します。
   - WDT 機能 (例: WebSphere Application Server V9.x Developer Tools) を選択してインストールします。

3. **ダウンロードしたファイルから** (オフラインオプション):
   - [IBM Developer サイト](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) から ZIP アーカイブ (例: `wdt-update-site_<バージョン>.zip`) をダウンロードします。
   - ローカルフォルダに展開します。
   - Eclipse で、**ヘルプ > 新規ソフトウェアのインストール > 追加 > アーカイブ** に移動し、展開したサイトの `site.xml` を選択します。
   - 目的の機能を選択してインストールし、再起動します。

インストール後、**ウィンドウ > ビューの表示 > サーバー** を確認して検証します — WAS がサーバータイプのオプションとして表示されるはずです。

#### WAS アプリケーションを開発およびデプロイするための基本手順
インストールが完了すると、WAS をターゲットとした Java EE アプリケーションの作成、ビルド、実行が可能になります。

1. **新規プロジェクトの作成**:
   - **ファイル > 新規 > プロジェクト** に移動します。
   - **Web > 動的 Web プロジェクト** (Web アプリ用) または **Java EE > エンタープライズ・アプリケーション・プロジェクト** (完全な EAR 用) を選択します。
   - プロジェクトウィザードで、ターゲットランタイムをローカルの WAS インストールに設定します (リストにない場合は、**ウィンドウ > 設定 > サーバー > ランタイム環境 > 追加 > WebSphere** 経由で追加)。
   - 使用する WAS に合わせて、Java EE バージョン (例: 7 または 8) のファセットを構成します。

2. **サーバーのセットアップ**:
   - **サーバー** ビュー (**ウィンドウ > ビューの表示 > サーバー**) を開きます。
   - ビュー内で右クリックし、**新規 > サーバー** を選択します。
   - **WebSphere Application Server** (従来型または Liberty) を選択し、ローカルの WAS インストールディレクトリを指定します。
   - 完了してサーバーを起動します (右クリック > 開始)。

3. **アプリケーションの開発**:
   - プロジェクトに Java クラス、JSP、サーブレット、EJB などを追加します。
   - XML 設定ファイル (例: web.xml、WAS 固有のバインディング用の ibm-web-bnd.xml) には Eclipse のエディターを使用します。
   - プロジェクトをビルドします (**プロジェクト > プロジェクトのビルド**)。

4. **デプロイと実行**:
   - プロジェクトを右クリック > **実行 > サーバーで実行** (WAS サーバーを選択)。
   - Eclipse がアプリを公開し (開発モードでは自動公開)、サーバーを起動します。
   - ブレークポイントを設定し、デバッグモードで実行してデバッグします。
   - ホットデプロイ (再起動なしでの高速更新) には、サーバー設定で「サーバー変更を即時公開」を有効にします。

5. **高度なヒント**:
   - ローカルテストの高速化には Liberty プロファイルを使用 — これは WDT に含まれており、従来型 WAS の動作を模倣します。
   - OSGi またはマイクロサービスの場合は、プラグイン経由で OSGi バンドルプロジェクトを作成します。
   - 実行中のログは **コンソール** ビューで監視します。

問題が発生した場合 (例: 互換性エラー)、IBM の既知の問題ページを確認するか、Eclipse と WAS のバージョンが一致していることを確認してください。

#### 参考資料
- [IBM WebSphere Application Server Developer Tools 概要](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace: V9.x ツール](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace: V8.5x ツール](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [IBM Docs からのインストールガイド](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)