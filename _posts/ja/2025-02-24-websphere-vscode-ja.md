---
audio: false
generated: true
lang: ja
layout: post
title: WebSphere Liberty サーバーを VSCode で使用する
translated: true
---

WebSphere Liberty サーバーを Visual Studio Code (VSCode) で使用するには、**Liberty Tools** 拡張機能を活用することができます。この拡張機能は、Open Liberty と WebSphere Liberty の両方をサポートしており、VSCode 内で Liberty サーバーを管理し、アプリケーションをデプロイし、デバッグすることができます。これにより、開発ワークフローがスムーズになります。

### WebSphere Liberty を VSCode で使用する手順

#### 1. **Liberty Tools 拡張機能のインストール**
   - VSCode を開き、アクティビティ バーの拡張機能アイコンをクリックするか、`Ctrl+Shift+X` を押して拡張機能ビューに移動します。
   - 拡張機能マーケットプレイスで「Liberty Tools」を検索します。
   - 「インストール」をクリックして拡張機能を VSCode に追加します。
   - プロンプトが表示された場合は、拡張機能を有効にするために VSCode を再読み込みします。

#### 2. **前提条件の設定**
   - **Java**: 互換性のあるバージョンの Java がインストールされていることを確認してください（Java 8 以降が推奨されます）。Liberty は Java ベースのサーバーであるため、Java は実行に必要です。
   - **WebSphere Liberty**: まだインストールしていない場合は、WebSphere Liberty ランタイムをダウンロードしてインストールしてください。[公式の IBM ウェブサイト](https://www.ibm.com/docs/en/was-liberty) から入手できます。インストールディレクトリをメモしておいてください。拡張機能の設定に必要です。

#### 3. **Liberty Tools 拡張機能の設定**
   - 拡張機能をインストールした後、Liberty インストールを指すように設定します。
   - VSCode のコマンドパレットを開くには、`Ctrl+Shift+P` を押します。
   - 「Liberty: Add Liberty Runtime」と入力し、コマンドを選択します。
   - Liberty インストールディレクトリのパスを指定します（例：`/opt/ibm/wlp`）。
   - 拡張機能は Liberty ランタイムを検出し、VSCode 内で使用できるようにします。

#### 4. **Liberty サーバーの管理**
   - 設定が完了すると、VSCode 内で Liberty サーバーを管理できます。
   - **Liberty ダッシュボード**: エクスプローラー ペインまたはコマンドパレットから Liberty ダッシュボードビューにアクセスします。このダッシュボードには、Liberty プロジェクトとサーバーが一覧表示されます。
   - **サーバーの開始/停止**: ダッシュボード内のサーバーを右クリックして開始、停止、または再起動します。
   - **アプリケーションのデプロイ**: Liberty プロジェクト（例：Liberty プラグインを持つ Maven または Gradle プロジェクト）を右クリックし、「Liberty にデプロイ」を選択してアプリケーションをデプロイします。
   - **開発モード (Dev Mode)**: Maven または Gradle プロジェクトの場合、サーバーをデバッグモードで開始し、コードの変更を自動的に検出し、再コンパイルし、サーバーを再起動せずにアプリケーションを再デプロイします。これは反復的な開発に最適です。

#### 5. **デバッグとテスト**
   - **デバッグ**: VSCode 内で実行中の Liberty サーバーにデバッガーをアタッチします。Liberty ダッシュボードの「デバッグ」オプションを使用するか、VSCode の実行とデバッグビューでデバッグ構成を設定します。
   - **テストの実行**: プロジェクトにテストが含まれている場合は、ダッシュボードから実行し、VSCode 内で結果を表示します。

#### 6. **追加機能**
   - **設定のサポート**: 拡張機能は、Liberty 設定ファイル（例：`server.xml`）のコード補完、検証、ホバー説明を提供し、サーバーの設定を簡素化します。
   - **言語サポート**: Java、MicroProfile、Jakarta EE API をサポートし、開発体験を向上させます。

### 主なメリット
- **シームレスな統合**: VSCode を離れずに Liberty サーバーを管理し、効率を向上させます。
- **自動デプロイ**: デバッグモードでは、コードの変更が自動的に検出され、デプロイされ、開発時間が節約されます。
- **デバッグサポート**: サーバーに簡単にデバッガーをアタッチしてトラブルシューティングができます。
- **軽量で効率的**: Liberty Tools は軽量設計されており、Liberty の速度と効率に合わせています。

### 追加リソース
- 詳細なガイドラインについては、[Open Liberty ドキュメント](https://openliberty.io/docs/)および[Liberty Tools VSCode ドキュメント](https://openliberty.io/docs/latest/develop/liberty-tools.html)を参照してください。
- 問題が発生した場合は、拡張機能のトラブルシューティングセクションを確認するか、Stack Overflow などのコミュニティでサポートを求めてください。

これらの手順に従うことで、VSCode 内で WebSphere Liberty を効果的に使用し、開発プロセスを向上させることができます。