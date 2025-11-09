---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Microsoft Entra ID アクセス管理ガイド
translated: true
type: note
---

Microsoft Entra ID は、アプリケーション、データ、デバイスなどのリソースへのアクセスを保護するクラウドベースの ID およびアクセス管理サービスです。認証（例：サインイン方法、MFA）、承認（例：ロールベースのアクセス）、Azure サービスとの統合をサポートします。開始するには、Azure サブスクリプションと適切な権限（例：全体管理者ロール）が必要です。

## はじめに
1. **Azure ポータルにサインインする**: [portal.azure.com](https://portal.azure.com) にアクセスし、Microsoft アカウントでサインインします。
2. **Microsoft Entra ID に移動する**: 上部の検索バーで「Microsoft Entra ID」を検索するか、「Azure サービス」の下から見つけます。
3. **ダッシュボードを確認する**: テナントの概要（ユーザー、グループ、アプリなど）を確認します。必要に応じてカスタム ドメインなどの基本設定を行います。
4. **主要な機能を有効にする**:
   - **認証**: 「認証方法」でセルフサービス パスワード リセットや多要素認証 (MFA) を構成します。
   - **条件付きアクセス**: 「セキュリティ」 > 「条件付きアクセス」でポリシーを作成し、ユーザー、デバイス、場所に基づいてルールを適用します。

## ユーザーとグループの管理
- **ユーザーの追加**: 「ユーザー」 > 「新しいユーザー」に移動します。名前、ユーザー名（例: user@yourdomain.com）などの詳細を入力し、ロールやライセンスを割り当てます。
- **グループの作成**: 「グループ」 > 「新しいグループ」で、セキュリティまたは Microsoft 365 タイプを選択し、メンバーを追加して、アクセス割り当てに使用します。
- **ライセンスの割り当て**: ユーザー/グループの詳細で「ライセンス」に移動し、Privileged Identity Management (PIM) などの高度な機能のために Entra ID P1/P2 を割り当てます。
- **ベスト プラクティス**: 最小権限の原則に従います。最小限の権限を割り当て、グループを一括管理に使用します。

## アプリケーションの管理
- **アプリの登録**: 「アプリの登録」 > 「新規登録」で、名前、リダイレクト URI、サポートされるアカウントの種類（シングル テナント、マルチ テナントなど）を指定します。
- **エンタープライズ アプリの追加**: サードパーティ製アプリの場合、「エンタープライズ アプリケーション」 > 「新しいアプリケーション」に移動し、ギャラリーを参照するか、非ギャラリー アプリを作成します。
- **アクセスの構成**: 「ユーザーとグループ」でアプリにユーザー/グループを割り当て、SAML または OAuth 経由でシングル サインオン (SSO) を設定します。
- **ID のプロビジョニング**: 「プロビジョニング」で、ジャストインタイム アクセスのためにユーザー同期をアプリに自動化します。

ハイブリッド設定（オンプレミス AD）の場合、Microsoft Entra Connect を使用して ID を同期します。「監視」 > 「サインイン ログ」でログを確認して使用状況を監視します。

# データベース、Kubernetes (AKS)、またはその他のリソースへのアクセスを確認する方法

Azure でのアクセスは、ロールベースのアクセス制御 (RBAC) によって管理され、Entra ID と統合されています。ユーザーは Entra 資格情報で認証し、ロールが権限を定義します。アクセスを確認するには、Azure ポータルの IAM (Identity and Access Management) ツールを使用します。これにより、直接の割り当て、親スコープ（例：サブスクリプション）からの継承、および拒否割り当てが一覧表示されます。

## 任意の Azure リソースに対する一般的な手順
1. **リソースを開く**: Azure ポータルで、リソース（例：リソース グループ、VM、ストレージ アカウント）に移動します。
2. **アクセス制御 (IAM) に移動する**: 左側のメニューから「アクセス制御 (IAM)」を選択します。
3. **アクセスを確認する**:
   - 自身のアクセス権の場合:「アクセスの確認」 > 「自分のアクセスを表示」をクリックし、このスコープおよび継承された割り当てを確認します。
   - 特定のユーザー/グループ/サービス プリンシパルの場合:
     - 「アクセスの確認」 > 「アクセスの確認」をクリックします。
     - 「ユーザー、グループ、またはサービス プリンシパル」を選択します。
     - 名前またはメールで検索します。
     - 結果ペインでロールの割り当て（例：所有者、共同作成者）と有効な権限を確認します。
4. **対象となる割り当てを表示する** (PIM を使用している場合): 「対象となる割り当て」タブに切り替えて、ジャストインタイム ロールを確認します。
5. **PowerShell/CLI の代替手段**: スクリプトによる確認には `az role assignment list --assignee <user> --scope <resource-id>` を使用します。

注: 子スコープの割り当ては含まれません。必要に応じてドリルダウンしてください。

## Azure SQL Database へのアクセスを確認する
Azure SQL は、包含データベース ユーザー（SQL ログインではなく、Entra ID に紐付け）に対して Entra 認証を使用します。
1. **Entra 管理者を構成する（設定されていない場合）**: SQL サーバーの概要 > 設定の「Microsoft Entra ID」 > 「管理者の設定」で、ユーザー/グループを検索して選択し、保存します。これにより、クラスター全体で Entra 認証が有効になります。
2. **サーバーレベルのアクセスを確認する**:
   - SQL サーバー ペイン > 「Microsoft Entra ID」で、管理者フィールドを表示し、割り当てられた ID を確認します。
   - `master` データベースをクエリします: `SELECT name, type_desc FROM sys.database_principals WHERE type IN ('E', 'X');` (E は外部ユーザー、X は外部グループ)。
3. **データベースレベルのアクセスを確認する**:
   - SSMS で Entra 認証を使用してデータベースに接続します（接続ダイアログで「Microsoft Entra - Universal with MFA」を選択）。
   - `SELECT * FROM sys.database_principals;` または `EXEC sp_helprolemember;` を実行して、ユーザーとロールを一覧表示します。
4. **トラブルシューティング**: ログインが失敗する場合（例：エラー 33134）、Entra の条件付きアクセス ポリシーで Microsoft Graph API へのアクセスが許可されているか確認してください。

ユーザーはデフォルトで `CONNECT` 権限を取得します。T-SQL を使用して `db_datareader` などのロールを付与します: `ALTER ROLE db_datareader ADD MEMBER [user@domain.com];`.

## AKS (Kubernetes クラスター) へのアクセスを確認する
AKS は、認証に Entra ID を統合し、承認に Azure RBAC または Kubernetes RBAC を使用します。
1. **Azure レベルのアクセス (AKS リソースへ)**:
   - 上記の一般的な手順を AKS クラスター リソースに対して実行します。
   - 一般的なロール: 完全な kubeconfig アクセスには「Azure Kubernetes Service クラスター管理者」、表示のみには「閲覧者」。
2. **Kubernetes API アクセス**:
   - `az login` で認証します（Entra トークンを使用）。
   - kubeconfig を取得: `az aks get-credentials --resource-group <rg> --name <cluster>`.
   - バインディングを確認: `kubectl auth can-i <verb> <resource> --as <user@domain.com> -n <namespace>`.
   - クラスター ロールを一覧表示: `kubectl get clusterrolebindings | grep <user-or-group>`.
3. **Entra グループの使用**: スケーラビリティのために、Kubernetes のロール/バインディングをグループに割り当てます。名前空間ロールの YAML 例（`kubectl apply -f file.yaml` で適用）:
   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: example-binding
     namespace: default
   subjects:
   - kind: Group
     name: finance-group  # Entra グループ
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: example-role
     apiGroup: rbac.authorization.k8s.io
   ```
4. **ベスト プラクティス**: 最小権限のロールを使用し、ジャストインタイムの昇格に PIM と統合し、固定資格情報は避けて、ポッドにはワークロード ID を使用します。

ポッドがリソース（例：AKS からの SQL）にアクセスする場合、マネージド ID を割り当て、それらの ID に対する Azure RBAC で確認します。

[Microsoft Entra ID ドキュメント](https://learn.microsoft.com/en-us/entra/identity/)
[単一の Azure リソースへのアクセスを確認する](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)
[Azure SQL の Entra 認証を構成する](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?view=azuresql)
[AKS の ID とアクセスのベスト プラクティス](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity)