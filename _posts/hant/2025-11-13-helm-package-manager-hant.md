---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Helm：Kubernetes 套件管理員
translated: true
type: note
---

Helm 是 Kubernetes 的套件管理工具，常被稱為「Kubernetes 的 yum 或 apt」。它透過將相關資源（Deployments、Services、ConfigMaps 等）打包成可重複使用、具版本控制的 **charts**，簡化了在 Kubernetes 集群上部署、管理和升級複雜應用程式的流程。

可將 Helm chart 視為 Kubernetes 清單的 Docker 映像檔：它將 YAML 檔案、模板、預設值和邏輯打包成一個單元，只需一條指令即可安裝。

在 **Jenkins** 這類 CI/CD 流程中，Helm 常用於：
- 建置和測試 charts。
- 將 charts 推送至儲存庫（例如 ChartMuseum、Harbor、Nexus）。
- 安全地將應用程式部署到測試/生產集群。

---

## 為何使用 Helm？

| 問題 | Helm 解決方案 |
|--------|---------------|
| 手動管理 50 多個 YAML 檔案 | 打包成單一 chart |
| 將相同應用部署到開發/測試/生產環境 | 使用 `values.yaml` 覆寫設定 |
| 回滾失敗的部署 | `helm rollback` |
| 跨團隊共享應用 | 將 charts 發佈到儲存庫 |
| 基礎設施版本控制 | Charts 語意化版本控制 |

---

## 核心概念

### 1. **Chart**
- 包含 Kubernetes 清單和中繼資料的目錄結構。
- 範例：`my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # 中繼資料（名稱、版本等）
├── values.yaml         # 預設配置值
├── templates/          # Kubernetes YAML 模板
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # 可重複使用的模板片段
└── charts/             # 子 charts（依賴項）
```

### 2. **Release**
- 在集群中運行的 chart 實例。
- 一個 chart → 多個 releases（例如 `myapp-dev`、`myapp-prod`）。

### 3. **Repository**
- 託管已索引 charts 的 HTTP 伺服器（類似 npm registry）。
- 常見：ChartMuseum、Harbor、Nexus、GitHub Pages、S3。

### 4. **Tiller**（已棄用）
- Helm v2 使用名為 Tiller 的伺服器端元件。
- **Helm v3+ 移除了 Tiller** → 僅客戶端，更安全。

---

## Helm 指令速查表

| 指令 | 用途 |
|-------|--------|
| `helm create mychart` | 建立新 chart 框架 |
| `helm lint mychart/` | 驗證 chart |
| `helm package mychart/` | 建立 `.tgz` 歸檔檔案 |
| `helm repo add stable https://charts.helm.sh/stable` | 新增儲存庫 |
| `helm repo update` | 更新本地快取 |
| `helm search repo nginx` | 搜尋 charts |
| `helm install myapp ./mychart` | 部署 release |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | 使用新值升級 |
| `helm rollback myapp 3` | 回滾至修訂版 3 |
| `helm uninstall myapp` | 刪除 release |
| `helm list` | 列出 releases |
| `helm status myapp` | 顯示 release 狀態 |
| `helm template ./mychart -f values.yaml` | 本地渲染模板 |

---

## Chart 結構詳解

### `Chart.yaml`（必需）
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: 範例網頁應用程式
type: application
keywords:
  - web
  - http
home: https://example.com
sources:
  - https://github.com/user/my-app
maintainers:
  - name: 開發團隊
    email: dev@example.com
icon: https://example.com/logo.png
```

### `values.yaml`（預設值）
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

### `_helpers.tpl`（最佳實踐）
```tpl
{{/* 生成基本標籤 */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Helm 在 Jenkins CI/CD 流程中的應用

以下是一個典型的 **Jenkins Pipeline** 使用 Helm 的範例：

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
        stage('建置並推送 Docker') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('打包 Helm Chart') {
            steps {
                sh """
                cd ${CHART_DIR}
                yq eval '.image.tag = "${IMAGE_TAG}"' values.yaml -i
                helm dependency update
                helm package .
                """
            }
        }

        stage('部署到測試環境') {
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

        stage('部署到生產環境') {
            when { tag "v*" }
            input { message "部署到生產環境？" }
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

### 關鍵 Jenkins 外掛
- **Kubernetes CLI** (`kubectl`)
- **Helm**（透過代理中的 `helm` 二進位檔）
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding**（用於 kubeconfig、儲存庫）

---

## 最佳實踐

| 實踐 | 原因 |
|--------|-----|
| 在 CI 中使用 `helm lint` + `helm template` | 及早發現錯誤 |
| 語意化版本控制 charts | `1.0.0` → `1.0.1` 用於配置，`1.1.0` 用於新功能 |
| 使用 `appVersion` 標示應用版本，`version` 標示 chart 版本 | 分離應用與打包版本 |
| 使用 `-f values-env.yaml` 分離環境配置 | 避免重複 charts |
| 使用 `helm secrets` 或 SOPS 處理密碼 | 切勿提交明文密碼 |
| 固定依賴版本 | `helm dependency update --version X` |
| 使用 `{{ include "chart.labels" . }}` 輔助函式 | 保持標籤一致性 |
| 在生產環境升級中啟用 `--atomic` | 失敗時自動回滾 |

---

## 常用工具與整合

| 工具 | 與 Helm 的搭配使用 |
|------|---------------|
| **ChartMuseum** | 輕量級 chart 儲存庫 |
| **Harbor / Nexus** | 企業級儲存庫 + Helm 儲存庫 |
| **ArgoCD** | GitOps + Helm |
| **Flux** | 使用 Helm Operator 的 GitOps |
| **helmfile** | 以宣告式管理多個 releases |
| **k3s / kind** | 本地測試 |

---

## 疑難排解提示

| 問題 | 解決方法 |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | 等待或使用 `--force`（危險） |
| 模板未渲染 | 在本地使用 `helm template .` |
| ImagePullBackOff | 檢查標籤、儲存庫認證 |
| 找不到 Release | `helm ls --all --all-namespaces` |
| CRDs 未應用 | 新增 `crds/` 資料夾並單獨應用 |

---

## 範例：使用 Helm 部署 NGINX

```bash
# 新增儲存庫
helm repo add bitnami https://charts.bitnami.com/bitnami

# 安裝
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# 升級
helm upgrade web-server bitnami/nginx --set replicaCount=5

# 回滾
helm rollback web-server 1
```

---

## 資源

- [官方 Helm 文件](https://helm.sh/docs/)
- [Helm Hub（Chart 儲存庫）](https://hub.helm.sh/)
- [Artifact Hub（現代 Chart 搜尋）](https://artifacthub.io/)
- [Helm 最佳實踐](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Helm 官方網站](https://helm.sh)  
[Bitnami Charts](https://github.com/bitnami/charts)  
[Helm in Jenkins X](https://www.jenkins-x.io/docs/)