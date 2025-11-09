---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphereの大規模EARアップロードエラー修正
translated: true
type: note
---

### 問題の理解
「multipart file upload error」（例: `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`）は、IBM WebSphere Application Server (WAS) の管理コンソール経由で EAR ファイルを更新する際に発生することがあります。これは、大きな EAR ファイル（例: >20MB）に対して、ファイルアップロードの制限、一時ストレージ、ヒープメモリ、または OS のリソース制約が原因でよく起こります。EAR 自体の問題ではなく、コンソールが HTTP マルチパートアップロードを処理する方法に関する問題です。

### 最初に試す簡単な修正
1. **EAR をサーバーにコピーしてローカルでデプロイ**:
   - FTP/SCP を使用して新しい EAR ファイルを WAS サーバーのディレクトリ（例: `/opt/IBM/WebSphere/AppServer/installableApps/`）に転送します。
   - 管理コンソールで: **アプリケーション > アプリケーション・タイプ > WebSphere エンタープライズ・アプリケーション** に移動します。
   - 既存のアプリケーションを選択 > **更新** をクリックします。
   - **単一モジュールの置換または追加** または **アプリケーション全体の置換** を選択し、**ローカル・ファイル・システム** を選択してコピーした EAR のパスを指定します。
   - これにより、HTTP 経由のマルチパートアップロードを回避できます。

2. **OS のファイルサイズ制限の引き上げ (UNIX/Linux サーバー)**:
   - エラー `errno:27` は、多くの場合、プロセスの ulimit をファイルが超えていることを意味します。
   - WAS ユーザー（例: `webadmin`）として `ulimit -f` を実行して現在の制限を確認します。
   - 無制限に設定: ユーザーのシェルプロファイル（例: `~/.bash_profile`）またはサーバーの起動スクリプトに `ulimit -f unlimited` を追加します。
   - デプロイメント・マネージャー (dmgr) を再起動し、アップロードを再試行します。

### WAS での設定変更
1. **デプロイメント・マネージャーのヒープサイズの増加**:
   - 大きな EAR は処理中に OutOfMemory を引き起こす可能性があります。
   - 管理コンソールで: **サーバー > サーバー・タイプ > 管理サーバー > デプロイメント・マネージャー** に移動します。
   - **Java とプロセス管理 > プロセス定義 > Java 仮想マシン** の下で:
     - **初期ヒープ・サイズ** を 1024（またはそれ以上、非常に大きな EAR の場合は 2048 など）に設定します。
     - **最大ヒープ・サイズ** を 2048（またはそれ以上）に設定します。
   - 保存し、dmgr を再起動して、アップロードを再試行します。

2. **HTTP セッションまたは POST サイズ制限の調整 (該当する場合)**:
   - Web コンテナーの制限の場合: **サーバー > サーバー・タイプ > WebSphere アプリケーション・サーバー > [対象サーバー] > Web コンテナー > HTTP トランスポート** に移動します。
   - **最大 POST サイズ** (バイト単位) が低く設定されている場合は増加させます。
   - 注意: これは間接的に管理コンソールの Web アプリケーションに影響します。

### 推奨される長期的な解決策: wsadmin を使用した更新
大きなファイルや頻繁な更新の場合は、コンソールを完全に避けてください。コンソールは大きなファイルに対して信頼性が低いです。wsadmin スクリプトツール (Jython または JACL) を使用してアプリケーションを更新します。

#### 手順:
1. 新しい EAR をサーバーからアクセス可能なパス（例: `/tmp/myapp.ear`）にコピーします。
2. wsadmin を起動:  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. 以下の Jython スクリプトを実行して更新:  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - `MyAppName` をアプリケーション名に、`MyContext` をコンテキストルートに、`MyServer` をターゲットサーバー/クラスターに、`/tmp/myapp.ear` を EAR のパスに置き換えてください。
4. クラスター環境の場合はノードを同期: `AdminControl.invoke(AdminControl.completeServers(), 'sync')`。
5. アプリケーションを再起動: **アプリケーション > [アプリケーション名] > 再始動**。

この方法はより高速で、アップロード制限を回避し、自動化（例: Jenkins 経由）のためにスクリプト化可能です。

### 追加のヒント
- **ログの確認**: dmgr プロファイルの `SystemOut.log` と `SystemErr.log`（例: `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`）を詳細に確認します。
- **より小さい EAR でのテスト**: 最小バージョンを zip 化して、問題がサイズ関連かどうかを確認します。
- **WAS バージョン**: サポートされているバージョン（例: 8.5, 9.0）であることを確認します。必要に応じて最新の修正を適用します。
- エラーが解消しない場合（例: タイムアウト）、**環境 > Web アプリケーション・サーバー > [サーバー] > コンテナー設定 > Web コンテナー設定 > Web コンテナー > セッション管理 > 構成 > タイムアウト** で HTTP タイムアウトを増やします。

これらで解決しない場合は、正確なエラーメッセージと WAS バージョンを共有して、より具体的なアドバイスを受けてください。

### 参考文献
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)