---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Helm：Kubernetesパッケージマネージャー
translated: true
type: note
---

HelmはKubernetesのパッケージマネージャーで、「Kubernetes向けのyumやapt」と呼ばれることが多いです。関連するリソース（Deployments、Services、ConfigMapsなど）を再利用可能でバージョン管理された**チャート**にまとめることで、Kubernetesクラスター上での複雑なアプリケーションのデプロイ、管理、アップグレードを簡素化します。

Helmチャートは、Kubernetesマニフェスト用のDockerイメージのようなものと考えてください：YAMLファイル、テンプレート、デフォルト値、ロジックを単一のユニットにパッケージ化し、1つのコマンドでインストールできます。

**Jenkins**のようなCI/CDパイプラインでは、Helmは一般的に以下の目的で使用されます：
- チャートのビルドとテスト。
- チャートをリポジトリ（例：ChartMuseum、Harbor、Nexus）にプッシュ。
- アプリケーションをステージング/本番クラスターに安全にデプロイ。

---

## Helmを使用する理由

| 問題点 | Helmの解決策 |
|--------|---------------|
| 50以上のYAMLファイルを手動で管理 | 1つのチャートにバンドル |
| 同じアプリをdev/stage/prodにデプロイ | `values.yaml`のオーバーライドを使用 |
| 失敗したデプロイのロールバック | `helm rollback` |
| チーム間でのアプリ共有 | チャートをリポジトリに公開 |
| インフラのバージョン管理 | チャートのセマンティックバージョニング |

---

## コアコンセプト

### 1. **チャート**
- Kubernetesマニフェストとメタデータを含むディレクトリ構造。
- 例：`my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # メタデータ（名前、バージョンなど）
├── values.yaml         # デフォルト設定値
├── templates/          # Kubernetes YAMLテンプレート
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # 再利用可能なテンプレートスニペット
└── charts/             # サブチャート（依存関係）
```

### 2. **リリース**
- クラスター内で実行されているチャートのインスタンス。
- 1つのチャート → 複数のリリース（例：`myapp-dev`、`myapp-prod`）。

### 3. **リポジトリ**
- インデックス化されたチャートをホストするHTTPサーバー（npmレジストリのようなもの）。
- 一般的なもの：ChartMuseum、Harbor、Nexus、GitHub Pages、S3。

### 4. **Tiller** (非推奨)
- Helm v2ではサーバーサイドコンポーネントであるTillerを使用していました。
- **Helm v3+ ではTillerを削除** → クライアントのみ、より安全。

---

## Helmコマンドチートシート

| コマンド | 目的 |
|-------|--------|
| `helm create mychart` | 新しいチャートのスキャフォールディング |
| `helm lint mychart/` | チャートの検証 |
| `helm package mychart/` | `.tgz`アーカイブの作成 |
| `helm repo add stable https://charts.helm.sh/stable` | リポジトリの追加 |
| `helm repo update` | ローカルキャッシュの更新 |
| `helm search repo nginx` | チャートの検索 |
| `helm install myapp ./mychart` | リリースのデプロイ |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | 新しい値でのアップグレード |
| `helm rollback myapp 3` | リビジョン3へのロールバック |
| `helm uninstall myapp` | リリースの削除 |
| `helm list` | リリースの一覧表示 |
| `helm status myapp` | リリースステータスの表示 |
| `helm template ./mychart -f values.yaml` | ローカルでのテンプレートレンダリング |

---

## チャート構造詳細

### `Chart.yaml` (必須)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: サンプルWebアプリ
type: application
keywords:
  - web
  - http
home: https://example.com
sources:
  - https://github.com/user/my-app
maintainers:
  - name: Dev Team
    email: dev@example.com
icon: https://example.com/logo.png
```

### `values.yaml` (デフォルト値)
```yaml
replicaCount: 2
image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
resources:
  limits:
    cpu: 500m
    memory: 512Mi
```

### `templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
  labels:
    {{- include "my-app.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "my-app.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-app.selectorLabels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 80
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

### `_helpers.tpl` (ベストプラクティス)
```tpl
{{/* 基本的なラベルの生成 */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Jenkins CI/CDパイプラインでのHelm

以下は、Helmを使用する典型的な**Jenkinsパイプライン**です：

```groovy
pipeline {
    agent any
    environment {
        CHART_DIR = "helm/my-app"
        IMAGE_NAME = "myregistry/my-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        HELM_REPO = "https://charts.mycompany.com"
    }
    stages {
        stage('Build & Push Docker') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Package Helm Chart') {
            steps {
                sh """
                cd ${CHART_DIR}
                yq eval '.image.tag = "${IMAGE_TAG}"' values.yaml -i
                helm dependency update
                helm package .
                """
            }
        }

        stage('Deploy to Staging') {
            when { branch 'main' }
            steps {
                withCredentials([kubeconfigFile(credentialsId: 'kubeconfig-staging')]) {
                    sh """
                    helm upgrade --install myapp-staging ./helm/my-app*.tgz \
                      --namespace staging \
                      --values values-staging.yaml \
                      --wait --timeout 5m
                    """
                }
            }
        }

        stage('Deploy to Production') {
            when { tag "v*" }
            input { message "Deploy to production?" }
            steps {
                withCredentials([kubeconfigFile(credentialsId: 'kubeconfig-prod')]) {
                    sh """
                    helm upgrade --install myapp-prod ./helm/my-app*.tgz \
                      --namespace production \
                      --values values-prod.yaml \
                      --atomic
                    """
                }
            }
        }
    }
}
```

### 主要なJenkinsプラグイン
- **Kubernetes CLI** (`kubectl`)
- **Helm** (エージェント内の`helm`バイナリ経由)
- **Pipeline Utility Steps** (`readYaml`、`writeYaml`)
- **Credentials Binding** (kubeconfig、レジストリ用)

---

## ベストプラクティス

| プラクティス | 理由 |
|--------|-----|
| CIで`helm lint` + `helm template`を使用 | 早期にエラーを検出 |
| チャートのバージョンをセマンティックに管理 | 設定変更は`1.0.0` → `1.0.1`、新機能は`1.1.0` |
| アプリには`appVersion`、チャートには`version`を使用 | アプリとパッケージングを分離 |
| `-f values-env.yaml`で環境を分割 | チャートの重複を回避 |
| シークレットには`helm secrets`またはSOPSを使用 | 平文をコミットしない |
| 依存関係のバージョンを固定 | `helm dependency update --version X` |
| `{{ include "chart.labels" . }}`ヘルパーを使用 | 一貫したラベリング |
| 本番環境のアップグレードで`--atomic`を有効化 | 失敗時の自動ロールバック |

---

## 一般的なツールと統合

| ツール | Helmとの連携 |
|------|---------------|
| **ChartMuseum** | 軽量なチャートリポジトリ |
| **Harbor / Nexus** | エンタープライズレジストリ + Helmリポジトリ |
| **ArgoCD** | GitOps + Helm |
| **Flux** | Helm Operatorを使用したGitOps |
| **helmfile** | 複数のリリースを宣言的に管理 |
| **k3s / kind** | ローカルテスト |

---

## トラブルシューティングのヒント

| 問題点 | 解決策 |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | 待機するか`--force`を使用（危険） |
| テンプレートがレンダリングされない | ローカルで`helm template .`を使用 |
| ImagePullBackOff | タグ、レジストリ認証を確認 |
| リリースが見つからない | `helm ls --all --all-namespaces` |
| CRDが適用されない | `crds/`フォルダを追加し個別に適用 |

---

## 例：Helmを使用したNGINXのデプロイ

```bash
# リポジトリの追加
helm repo add bitnami https://charts.bitnami.com/bitnami

# インストール
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# アップグレード
helm upgrade web-server bitnami/nginx --set replicaCount=5

# ロールバック
helm rollback web-server 1
```

---

## リソース

- [公式Helmドキュメント](https://helm.sh/docs/)
- [Helm Hub (チャートリポジトリ)](https://hub.helm.sh/)
- [Artifact Hub (モダンなチャート検索)](https://artifacthub.io/)
- [Helmベストプラクティス](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Helm公式サイト](https://helm.sh)  
[Bitnami Charts](https://github.com/bitnami/charts)  
[Helm in Jenkins X](https://www.jenkins-x.io/docs/)