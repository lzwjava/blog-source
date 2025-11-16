---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Jenkinsジョブ設定ガイド
translated: true
type: note
---

### Jenkinsでのジョブ設定

Jenkinsはさまざまな種類のジョブ（プロジェクトとも呼ばれる）をサポートしており、最も一般的なのは**Freestyleプロジェクト**（シンプルなビルド用）と**Pipelineプロジェクト**（Jenkinsfileを使用したより複雑なスクリプト化されたワークフロー用）です。以下に両方の手順を概説します。これらは、Jenkinsが（Docker経由やサーバー上で）インストールされ実行されていることを前提としています。Jenkinsダッシュボードに `http://localhost:8080` （またはご利用のサーバーのURL）でアクセスし、ログインしてください。

#### Freestyleプロジェクトの作成と設定手順
Freestyleプロジェクトはシンプルで、GUIを使用してステップを設定します。コードのビルドやテストのようなシンプルなタスクや、初心者に最適です。

1.  **新しいジョブの作成**:
    *   Jenkinsダッシュボードから、左側のサイドバーにある**New Item**をクリックします。
    *   ジョブの名前（例: "MyFirstBuild"）を入力します。
    *   **Freestyle project**を選択し、**OK**をクリックします。

2.  **一般設定**:
    *   ジョブの説明を追加します。
    *   必要に応じて、古いビルドを破棄する（例: 最後の10ビルドのみ保持）や、パラメーター（ビルド時のユーザー入力用の文字列や選択パラメーターなど）を追加するなどの機能を有効にします。

3.  **ソースコード管理**:
    *   GitなどのSCMツールを選択します。
    *   リポジトリURL（例: GitHubリポジトリ）を入力します。
    *   必要に応じて認証情報（ユーザー名/パスワードやSSHキーなど）を追加します。
    *   ビルドするブランチ（例: `*/main`）を指定します。

4.  **ビルドトリガー**:
    *   ジョブの開始方法を選択します。例えば：
        *   **Build periodically** (例: 5分ごとのcron構文 `H/5 * * * *`)。
        *   変更をチェックする**Poll SCM**。
        *   GitHubからのWebhook用の**GitHub hook trigger**。
        *   ジョブを連鎖させる**Build after other projects**。

5.  **ビルド環境**:
    *   クリーンな状態で開始するために、**Delete workspace before build starts**などのオプションをチェックします。
    *   コンソール出力にタイムスタンプを追加したり、環境変数を設定したりします。

6.  **ビルドステップ**:
    *   **Add build step**をクリックし、以下のようなアクションを選択します：
        *   **Execute shell** (Linux/Mac用: 例: `echo "Hello World"` またはスクリプトの実行)。
        *   Javaビルド用の**Invoke top-level Maven targets**。
        *   Windows用の**Execute Windows batch command**。
    *   順次実行される複数のステップを追加できます。

7.  **ビルド後アクション**:
    *   以下のようなアクションを追加します：
        *   **Archive the artifacts** (例: JARファイルの保存)。
        *   **Publish JUnit test result report**。
        *   成功/失敗時の**Send email notifications**。
        *   **Trigger another project**。

8.  **保存と実行**:
    *   **Save**をクリックします。
    *   ジョブページに戻り、**Build Now**をクリックしてテストします。
    *   詳細についてはコンソール出力を確認します。

#### Pipelineプロジェクトの作成と設定手順
Pipelineはコード（DeclarativeまたはScripted）として定義され、CI/CDワークフローにおいてより柔軟性があります。

1.  **新しいジョブの作成**:
    *   ダッシュボードから**New Item**をクリックします。
    *   名前を入力し、**Pipeline**を選択して、**OK**をクリックします。

2.  **一般設定**:
    *   Freestyleと同様：説明、パラメーターなどを追加します。

3.  **ビルドトリガー**:
    *   Freestyleと同じオプション（例: Webhook、スケジュール）。

4.  **Pipeline定義**:
    *   インラインコードの場合は**Pipeline script**を、リポジトリ（例: Git内の`Jenkinsfile`）から取得する場合は**Pipeline script from SCM**を選択します。
    *   Declarative Pipelineスクリプトの例:
        ```
        pipeline {
            agent any
            stages {
                stage('Build') {
                    steps {
                        echo 'Building...'
                        sh 'mvn clean install'  // Mavenビルドの例
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing...'
                        sh 'mvn test'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying...'
                    }
                }
            }
            post {
                always {
                    echo 'This runs always'
                }
            }
        }
        ```
    *   これにより、ステップを含むステージ（Build、Test、Deploy）が定義されます。

5.  **保存と実行**:
    *   ジョブを保存します。
    *   ビルドし、パイプラインビューでステージの進捗を監視します。

Jenkinsには各セクションに多くのオプションがあるため、ニーズに基づいて探索してください（例: セキュリティのためには認証情報を追加、並列処理のためにはエージェント/ノードを使用）。初心者の方は、Freestyleから始め、スケーラビリティのためにPipelineに移行することをお勧めします。

### Jenkinsとのソフトウェア統合と連携

Jenkinsは**プラグイン**（2,000以上利用可能）を通じて非常に拡張性が高く、DevOpsエコシステム内の事実上あらゆるツールと統合できます。これらの統合により、ビルド、デプロイ、テスト、通知などのトリガーが可能になります。プラグインは、**Manage Jenkins > Manage Plugins**からインストールできます。

#### カテゴリー別の一般的な統合
*   **バージョン管理**: Git、GitHub、GitLab、Bitbucket、SVN – コードのプルや、コミット/プッシュイベント時のWebhookによるビルドトリガー用。
*   **コンテナ化とオーケストレーション**: Docker（イメージのビルド/プッシュ）、Kubernetes（クラスターへのデプロイ）、Helm – コンテナベースのワークフロー用。
*   **クラウドプロバイダー**: AWS (EC2、S3、Lambda via plugins)、Azure、Google Cloud – クラウドインフラへのデプロイ用。
*   **テストと品質**: SonarQube（コード品質スキャン）、Selenium（UIテスト）、JUnit（単体テスト）、Cucumber（BDD）– 自動テストのためのビルドステップへの統合。
*   **デプロイと監視**: Ansible、Terraform（Infrastructure as Code）、Prometheus、Grafana – ビルド後のオーケストレーションと監視用。
*   **通知とコラボレーション**: Slack、Microsoft Teams、Email、Jira、Trello – ビルドステータスに関するアラートの送信やチケットの更新。
*   **ビルドツール**: Maven、Gradle (Java)、npm (Node.js)、pip (Python) – 様々な言語のビルド実行用。
*   **セキュリティ**: OWASP Dependency-Check、Trivy（脆弱性スキャン）– CI中の問題スキャン用。
*   **その他**: Artifactory/Nexus（アーティファクトリポジトリ）、Zapier（ノーコード統合）、Octopus Deploy（高度なデプロイ）。

例えば、GitHubでは、GitHubプラグインをインストールしてWebhookトリガーを有効にします。Dockerでは、Docker Pipelineプラグインを使用してパイプライン内でイメージをビルドします。ニッチなツール向けにカスタムプラグインを作成することもできます。

詳細については、公式のプラグインインデックスを確認してください。セキュリティのため、プラグインは定期的に更新してください。

#### 参考文献
*   [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
*   [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
*   [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
*   [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
*   [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
*   [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
*   [Jenkins Plugins](https://plugins.jenkins.io/)
*   [Jenkins](https://www.jenkins.io/)
*   [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)