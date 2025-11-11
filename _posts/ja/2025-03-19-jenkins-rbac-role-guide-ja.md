---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Jenkins RBACロールプラグインガイド
translated: true
type: note
---

Jenkinsにおける**ロールベースアクセス制御（RBAC）**は、誰がどこで何をできるかを定義する仕組みです。デフォルトのJenkinsは基本的なユーザー/管理者モデルのみですが、**Role-Based Strategyプラグイン**（または類似の認可戦略）を使用することで、きめ細かいアクセス制御を定義できます。

---

### JenkinsにおけるRBACの核心概念

1. **グローバルロール**
   これらはJenkinsインスタンス全体に適用されます。例:

   * **Admin**: 完全な制御権限
   * **Read-only**: ジョブを閲覧可能だが実行不可
   * **Developer**: ジョブの作成と設定が可能

2. **プロジェクト/ジョブロール**
   ジョブ単位またはフォルダ単位で権限を付与できます。例:

   * ユーザーAは*Project X*をビルド可能だが*Project Y*は閲覧不可
   * 契約者はビルドのトリガーは可能だが設定変更は不可

3. **ビルド権限**
   権限は以下のように分割可能:

   * `Job/Read`（ジョブ定義とビルド履歴の閲覧）
   * `Job/Build`（ビルドのトリガー）
   * `Job/Configure`（パイプラインや設定の変更）
   * `Job/Delete`（ジョブやビルドの削除）
   * `Job/Cancel`（実行中のビルドの中止）

---

### ジョブ/ビルドアクセス権限の管理方法

1. **Role-Based Strategyプラグインのインストール**

   * **Manage Jenkins → Plugins → Available Plugins → Role-based Authorization Strategy**に移動
   * インストール後、**Manage Jenkins → Configure Global Security → Authorization**で選択

2. **ロールの定義**

   * **Manage Jenkins → Manage and Assign Roles**に移動
   * グローバルロール（*admin*、*viewer*、*developer*など）とプロジェクトロール（*projectX-builder*など）を作成
   * 各ロールに必要な権限（`Job/Build`、`Job/Configure`など）を割り当て

3. **ユーザー/グループへのロール割り当て**

   * **Manage and Assign Roles**で、Jenkinsユーザー（またはLDAPグループが統合されている場合）をロールにマッピング
   * 例:

     * *alice* → `developer`にマッピング
     * *bob* → `viewer`にマッピング
     * *qa-team* → `projectX-builder`にマッピング

4. **より細かい制御のためのフォルダ活用**

   * **Folders Plugin**を使用してジョブをフォルダに整理
   * フォルダレベルでロール制限を適用し、適切なチームのみが内部のジョブを閲覧/ビルド/変更可能に

---

### 設定例

* **開発者**: 自身のチームのジョブをビルド・設定可能だが、管理者設定は変更不可
* **QAチーム**: ビルドのトリガーのみ可能（パイプラインの再設定は不可）
* **外部ユーザー**: ジョブステータスを閲覧可能だが、変更やビルドのトリガーは不可

---

👉 実践的には：**管理者を最小限**に抑え、**開発者には自身のジョブへの設定+ビルド権限**を付与し、その他には**読み取り専用またはビルド専用権限**を付与します。これにより一貫性が保たれ、ミスが減少し、機密性の高いジョブが保護されます。

---

**ステップバイステップの設定例**（ロール、権限、ジョブマッピングを含む）を、典型的な企業環境に合わせてご紹介しましょうか？