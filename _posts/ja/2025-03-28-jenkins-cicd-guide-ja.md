---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 実践的Jenkins CI/CDガイド
translated: true
type: note
---

素晴らしい—では、すぐに職場で使える**クリーンでエンドツーエンドのJenkinsガイド**を作りましょう。見やすく、広いテーブルは使わないようにします。

# Jenkinsとは（および使用する場面）

Jenkinsはセルフホスト型のCI/CD自動化サーバーです：ソースリポジトリに接続し、`Jenkinsfile`でパイプラインを定義すると、1台または複数のマシン（「エージェント」）でビルド、テスト、デプロイを実行します。パイプラインには**Declarative**（推奨）と**Scripted**の2種類があり、どちらもプロジェクトによって文書化されています。([Jenkins][1])

---

# コアアーキテクチャ（平易な言葉で）

* **コントローラー**: Web UI、キュー、およびオーケストレーションの頭脳。
* **エージェント/ノード**: ジョブが実際に実行されるマシン（VM、コンテナ、ベアメタル）。多くのエージェントを追加し、能力（例: `java8`, `docker`）に応じてラベルを付けることができます。([Jenkins][2])
* **ジョブ/パイプライン**: 作業の定義（理想的にはコードとしてリポジトリに保存）。
* **プラグイン**: 機能を追加（認証情報、認証戦略、クラウドエージェント、JCasCなど）。

---

# インストールと初回実行時のセキュリティ強化（クイックチェックリスト）

1. **インストール**: Linuxまたはコンテナイメージにインストール。
2. **リバースプロキシ + TLS** (Nginx/Apache, 企業のロードバランサー)。
3. **Jenkinsの管理 → グローバルセキュリティの設定**

   * 実際の**セキュリティレルム**を設定（LDAP/OIDC/SAMLなど）。
   * **認証**モードを選択（下記参照）。([Jenkins][3])
4. **管理者ユーザーを作成**（共有しない）。
5. **サインアップを制限**、匿名書き込みを無効化。
6. **Credentialsプラグイン**のみを使用—ジョブにシークレットをハードコードしない。([Jenkins][4])

---

# アクセス制御（RBACとプロジェクトスコープ）

Jenkinsは、きめ細かい権限（ビルド、設定、削除など）のための**マトリックスベースのセキュリティ**を同梱しています。小規模/中規模のインスタンスやベースとして使用します。([Jenkins][3], [Jenkins Plugins][5])

大規模な組織とクリーンなチーム分離のためには、**ロールベース認証ストラテジー**（「role-strategy」プラグイン）をインストールします：

* **グローバルロール**を定義（例: `admin`, `reader`）。
* アイテム/フォルダの正規表現でスコープされた**プロジェクトロール**を定義（例: `team-alpha.*`）。
* ユーザー/グループをロールに割り当て—これでチームは自身が所有するもののみを見てビルドできます。([Jenkins Plugins][6])

> ヒント: 各チームのパイプラインを**フォルダ**内に配置し、フォルダレベルでプロジェクトロールを適用します。超きめ細かい調整が必要な場合は、**マトリックス**と組み合わせます。([Jenkins Plugins][5])

---

# 認証情報とシークレット（安全なパターン）

* **Jenkinsの管理 → 認証情報**でシークレットを追加（グローバルまたはフォルダスコープ）。
* Declarative Pipelineでは、`environment`内で`credentials()`を参照するか、オンデマンドで`withCredentials { … }`でバインドします。
* ボールトまたはプロバイダープラグインからの短命なトークンを優先し、定期的にローテーションします。([Jenkins][4])

**例 (Declarative):**

```groovy
pipeline {
  agent any
  environment {
    // Username/Password認証情報からUSERとPASS環境変数を注入
    CREDS = credentials('dockerhub-creds-id')
  }
  stages {
    stage('Login') {
      steps {
        sh 'echo $CREDS_USR | docker login -u $CREDS_USR --password-stdin'
      }
    }
  }
}
```

```groovy
pipeline {
  agent any
  stages {
    stage('Use Secret Text') {
      steps {
        withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
          sh 'curl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.example/api'
        }
      }
    }
  }
}
```

使用法とバインディングに関するドキュメントはこちらです。([Jenkins][7])

---

# スケールするエージェント

* **永続的**または**一時的**なエージェントを追加。能力に応じてラベルを付け。起動方法（SSH、JNLP、クラウド）を設定。
* Jenkinsはディスク、スワップ、一時領域、クロックドリフトを監視し、異常なノードを自動的にオフラインにできます。ラベルをクリーンに保ち、ステージでのルーティングに`agent { label 'docker' }`を使用します。([Jenkins][2])

---

# 問題を起こさないパイプライン（モダンなJenkinsfile）

**Declarative vs Scripted**: **Declarative**を優先—構造が明確で、ガードレール付き（`post`, `options`, `when`, `environment`, `input`, `parallel`）。([Jenkins][1])

**最小限のCI例:**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // またはSCMでWebhookを使用
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { sh './gradlew test' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
  }
  post {
    always { junit 'build/test-results/test/*.xml'; archiveArtifacts 'build/libs/*.jar' }
    failure { mail to: 'team@example.com', subject: "Build failed ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```

**主要な参照:** パイプライン本、シンタックスリファレンス、ステップドキュメント。([Jenkins][1])

---

# マルチブランチ、GitHub/GitLab、およびPR

**マルチブランチパイプライン**またはGitHub/Bitbucket Organizationジョブを使用して、`Jenkinsfile`を持つ各リポジトリブランチ/PRが（Webhook経由で）自動的にビルドされるようにします。ブランチの動作をコードで維持し、クリック操作を避けます。

---

# スケールでの再利用: 共有ライブラリ

リポジトリ間でステップを繰り返す場合、**Jenkins共有ライブラリ**（vars関数、パイプラインステップ）を作成し、`Jenkinsfile`で`@Library('your-lib') _`を使用してインポートします。これによりコピーペーストパイプラインを防ぎ、修正を一元化できます。

---

# Configuration as Code (JCasC)

コントローラーの設定をコードのように扱います：Gitにチェックインし、PR経由でレビューし、新しいコントローラーを再現可能にブートストラップします。

* **Configuration as Code**プラグインをインストール。
* グローバルセキュリティ、エージェントランチャー、ツールインストーラー、フォルダー、認証情報バインディングなどをキャプチャするYAMLを記述。
* 起動時（環境変数`CASC_JENKINS_CONFIG`）またはUIから読み込みます。([Jenkins Plugins][8], [Jenkins][9])

**JCasCの小さな例:**

```yaml
jenkins:
  systemMessage: "Jenkins managed by JCasC"
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "viewer"
            permissions:
              - "Overall/Read"
            assignments:
              - "devs"
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${ADMIN_PW}"
unclassified:
  location:
    url: "https://ci.example.com/"
```

公式ドキュメントとプラグインページは上記です。([Jenkins][9], [Jenkins Plugins][8])

---

# プラグイン（賢く使用する）

* **必須知識**: Credentials, Matrix/Role-Strategy, Pipeline, Git, SSH, Email, Artifact Manager (例: S3/GCS), Cloud agents (Kubernetes), JCasC。
* プラグインを**最小限に保ち、更新**し、重要なものはピン留めし、ステージングコントローラーで更新をテストします。実用的なプラグインのドキュメントはjenkins.ioと各プラグインページにあります。([Jenkins][10])

---

# 観測性とハイジーン

* **ログ**: コントローラーログレコーダーを使用 + ログをELK/CloudWatchに送信。
* **アーティファクト**: 必要なもののみをアーカイブ。
* **JUnit**: 常にテストレポートを公開。テスト失敗時にビルドを中断。
* **キューの健全性**: ビルドキューとエージェント使用率を監視。それに応じてエージェントをスケール。
* **バックアップ**: `$JENKINS_HOME`をバックアップするか、JCasC + 一時的なコントローラーを使用。

---

# セキュリティのクイックウィン

* 不要なCLIは無効化。APIトークンを優先。
* **サービス**アカウントを人間から分離。
* フォルダスコープのシークレットのみ。シークレットをエコーしない。
* スクリプト承認をロックダウン。Declarativeでの`script`ステップを制限。
* ロールを定期的に監査。Jenkinsのセキュリティドキュメントにガイダンスがあります。([Jenkins][3])

---

# 典型的な「Day-2」の改善

* **並列**テストシャーディングでビルド時間を短縮。
* **キャッシング**（例: エージェント上のGradle/Mavenキャッシュ）。
* **Docker-in-Docker**または**Kubernetesエージェント**でクリーンで再現可能なビルドイメージを実現。
* 初期ステージでの**品質ゲート**（lint, SAST/DAST）。
* `when`条件と手動`input`による**プロモーション**ジョブまたはマルチ環境デプロイステージ。

---

# トラブルシューティング早見表

* ビルドが詰まった？エージェントログ、ワークスペースのディスク、ノードのクロックスキューを確認。Jenkinsは正常性閾値を超えたノードを自動オフラインにします。([Jenkins][2])
* 認証情報が見つからない？スコープ（フォルダ対グローバル）と正しい`credentialsId`を確認。([Jenkins][4])
* 認証がおかしい？レルム ↔ 認証ストラテジーのペアリング（Matrix/Role-strategy）を再確認。([Jenkins][3], [Jenkins Plugins][6])
* パイプラインシンタックスエラー？**Declarative**バリデータステップ / オンラインエディタで検証。([Jenkins][11])

---

# コピーして使える「ゴールデン」な開始点

```groovy
pipeline {
  agent { label 'k8s || docker || linux' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '50')); ansiColor('xterm') }
  environment { JAVA_TOOL_OPTIONS = '-XX:+UseContainerSupport' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup')    { steps { sh 'python -V || true' } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { junit 'build/test-results/test/*.xml' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
    stage('Deploy')   { when { branch 'main' } steps { input 'Ship to staging?'; sh './scripts/deploy_staging.sh' } }
  }
  post {
    failure { echo "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
    always  { archiveArtifacts artifacts: 'build/libs/*.jar', fingerprint: true }
  }
}
```

---

# さらに読むべき場所（高シグナルのドキュメント）

* **パイプライン: 概要とシンタックス** (Declarative vs Scripted, すべてのディレクティブとステップ)。([Jenkins][1])
* **セキュリティと認証** (Matrix)、およびRBACのための**Role-Strategyプラグイン**。([Jenkins][3], [Jenkins Plugins][5])
* **エージェントとノード** (追加、健全性、ラベル)。([Jenkins][2])
* **認証情報の使用法** (UI & Pipeline ヘルパー/バインディング)。([Jenkins][4])
* **Configuration as Code (JCasC)** (コンセプト + プラグイン)。([Jenkins][9], [Jenkins Plugins][8])

---

必要に応じて、これを**あなたの正確なセットアップ**（GitHub vs GitLab, オンプレ vs k8sエージェント, あなたのRBACモデル）に合わせて調整し、以下を草案できます：

* **JCasC** YAMLシード、
* あなたのチームのための**role-strategy**マッピング、
* 標準化されたステージのための**共有ライブラリ**スケルトン。

[1]: https://www.jenkins.io/doc/book/pipeline/?utm_source=chatgpt.com "Pipeline"
[2]: https://www.jenkins.io/doc/book/managing/nodes/?utm_source=chatgpt.com "Managing Nodes"
[3]: https://www.jenkins.io/doc/book/security/managing-security/?utm_source=chatgpt.com "Managing Security"
[4]: https://www.jenkins.io/doc/book/using/using-credentials/?utm_source=chatgpt.com "Using credentials"
[5]: https://plugins.jenkins.io/matrix-auth/?utm_source=chatgpt.com "Matrix Authorization Strategy"
[6]: https://plugins.jenkins.io/role-strategy/?utm_source=chatgpt.com "Role-based Authorization Strategy"
[7]: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/?utm_source=chatgpt.com "Using a Jenkinsfile"
[8]: https://plugins.jenkins.io/configuration-as-code/?utm_source=chatgpt.com "Configuration as Code | Jenkins plugin"
[9]: https://www.jenkins.io/doc/book/managing/casc/?utm_source=chatgpt.com "Configuration as Code"
[10]: https://www.jenkins.io/doc/developer/publishing/documentation/?utm_source=chatgpt.com "Plugin Documentation"
[11]: https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/?utm_source=chatgpt.com "Pipeline: Declarative"