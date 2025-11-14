---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'Helm: Der Kubernetes-Paketmanager'
translated: true
type: note
---

Helm ist der Paketmanager für Kubernetes, oft als "der yum oder apt für Kubernetes" bezeichnet. Es vereinfacht das Bereitstellen, Verwalten und Aktualisieren komplexer Anwendungen auf Kubernetes-Clustern, indem es zusammengehörige Ressourcen (Deployments, Services, ConfigMaps usw.) in wiederverwendbare, versionierte **Charts** bündelt.

Stellen Sie sich ein Helm-Chart wie ein Docker-Image für Kubernetes-Manifeste vor: Es verpackt YAML-Dateien, Templates, Standardwerte und Logik in eine einzelne Einheit, die mit einem Befehl installiert werden kann.

In CI/CD-Pipelines wie **Jenkins** wird Helm häufig verwendet, um:
- Charts zu bauen und zu testen.
- Charts in Repositories zu pushen (z.B. ChartMuseum, Harbor, Nexus).
- Anwendungen sicher auf Staging-/Produktions-Clustern bereitzustellen.

---

## Warum Helm verwenden?

| Problem | Helm-Lösung |
|--------|---------------|
| Manuelles Verwalten von 50+ YAML-Dateien | In einem Chart bündeln |
| Bereitstellung derselben App für dev/stage/prod | `values.yaml`-Overrides verwenden |
| Rollback fehlgeschlagener Deployments | `helm rollback` |
- Freigabe von Apps für Teams | Charts im Repo veröffentlichen |
| Versionierung der Infrastruktur | Semantische Versionierung von Charts |

---

## Kernkonzepte

### 1. **Chart**
- Verzeichnisstruktur mit Kubernetes-Manifesten und Metadaten.
- Beispiel: `my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # Metadaten (Name, Version usw.)
├── values.yaml         # Standardkonfigurationswerte
├── templates/          # Kubernetes YAML-Templates
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # Wiederverwendbare Template-Snippets
└── charts/             # Sub-Charts (Abhängigkeiten)
```

### 2. **Release**
- Eine Instanz eines Charts, die in einem Cluster läuft.
- Ein Chart → mehrere Releases (z.B. `myapp-dev`, `myapp-prod`).

### 3. **Repository**
- HTTP-Server, der indizierte Charts hostet (wie npm Registry).
- Üblich: ChartMuseum, Harbor, Nexus, GitHub Pages, S3.

### 4. **Tiller** (Veraltet)
- Helm v2 verwendete eine serverseitige Komponente namens Tiller.
- **Helm v3+ entfernt Tiller** → Nur Client, sicherer.

---

## Helm-Befehle Spickzettel

| Befehl | Zweck |
|-------|--------|
| `helm create mychart` | Neues Chart erstellen |
| `helm lint mychart/` | Chart validieren |
| `helm package mychart/` | `.tgz`-Archiv erstellen |
| `helm repo add stable https://charts.helm.sh/stable` | Repo hinzufügen |
| `helm repo update` | Lokalen Cache aktualisieren |
| `helm search repo nginx` | Charts suchen |
| `helm install myapp ./mychart` | Release bereitstellen |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | Mit neuen Werten upgraden |
| `helm rollback myapp 3` | Zu Revision 3 zurücksetzen |
| `helm uninstall myapp` | Release löschen |
| `helm list` | Releases auflisten |
| `helm status myapp` | Release-Status anzeigen |
| `helm template ./mychart -f values.yaml` | Templates lokal rendern |

---

## Chart-Struktur im Detail

### `Chart.yaml` (Erforderlich)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: Eine Beispiel-Web-App
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

### `values.yaml` (Standardwerte)
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

### `_helpers.tpl` (Beste Praxis)
```tpl
{{/* Generiere grundlegende Labels */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Helm in der Jenkins CI/CD-Pipeline

Hier ist eine typische **Jenkins-Pipeline** mit Helm:

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

### Wichtige Jenkins-Plugins
- **Kubernetes CLI** (`kubectl`)
- **Helm** (über `helm`-Binary im Agent)
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding** (für Kubeconfig, Registry)

---

## Best Practices

| Praxis | Warum |
|--------|-----|
| `helm lint` + `helm template` in CI verwenden | Fehler früh erkennen |
| Charts semantisch versionieren | `1.0.0` → `1.0.1` für Konfig, `1.1.0` für neue Features |
| `appVersion` für App, `version` für Chart verwenden | App und Verpackung entkoppeln |
- Umgebungen mit `-f values-env.yaml` trennen | Duplizieren von Charts vermeiden |
| `helm secrets` oder SOPS für Secrets verwenden | Niemals Klartext committen |
| Abhängigkeitsversionen festnageln | `helm dependency update --version X` |
| `{{ include "chart.labels" . }}` Helper verwenden | Konsistentes Labeln |
| `--atomic` für Prod-Upgrades aktivieren | Auto-Rollback bei Fehlschlag |

---

## Häufige Tools & Integrationen

| Tool | Verwendung mit Helm |
|------|---------------|
| **ChartMuseum** | Einfaches Chart-Repo |
| **Harbor / Nexus** | Enterprise Registry + Helm Repo |
| **ArgoCD** | GitOps + Helm |
| **Flux** | GitOps mit Helm Operator |
| **helmfile** | Mehrere Releases deklarativ verwalten |
| **k3s / kind** | Lokales Testen |

---

## Tipps zur Fehlerbehebung

| Problem | Lösung |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | Warten oder `--force` verwenden (gefährlich) |
| Templates werden nicht gerendert | `helm template .` lokal verwenden |
| ImagePullBackOff | Tag, Registry-Auth prüfen |
| Release nicht gefunden | `helm ls --all --all-namespaces` |
| CRDs nicht angewendet | `crds/`-Ordner hinzufügen und separat anwenden |

---

## Beispiel: NGINX mit Helm bereitstellen

```bash
# Repo hinzufügen
helm repo add bitnami https://charts.bitnami.com/bitnami

# Installieren
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# Upgrade
helm upgrade web-server bitnami/nginx --set replicaCount=5

# Rollback
helm rollback web-server 1
```

---

## Ressourcen

- [Offizielle Helm-Dokumentation](https://helm.sh/docs/)
- [Helm Hub (Chart-Repository)](https://hub.helm.sh/)
- [Artifact Hub (Moderne Chart-Suche)](https://artifacthub.io/)
- [Helm Best Practices](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Helm Offizielle Website](https://helm.sh)  
[Bitnami Charts](https://github.com/bitnami/charts)  
[Helm in Jenkins X](https://www.jenkins-x.io/docs/)