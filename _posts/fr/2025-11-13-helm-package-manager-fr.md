---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Helm : Gestionnaire de packages Kubernetes'
translated: true
type: note
---

Helm est le gestionnaire de paquets pour Kubernetes, souvent appelé "le yum ou apt pour Kubernetes". Il simplifie le déploiement, la gestion et la mise à niveau d'applications complexes sur les clusters Kubernetes en regroupant les ressources associées (Deployments, Services, ConfigMaps, etc.) dans des **charts** réutilisables et versionnés.

Considérez un chart Helm comme une image Docker pour les manifests Kubernetes : il empaquette les fichiers YAML, les templates, les valeurs par défaut et la logique en une seule unité qui peut être installée avec une seule commande.

Dans les pipelines CI/CD comme **Jenkins**, Helm est couramment utilisé pour :
- Construire et tester des charts.
- Pousser des charts vers des dépôts (par exemple, ChartMuseum, Harbor, Nexus).
- Déployer des applications de manière sécurisée sur des clusters de staging/production.

---

## Pourquoi utiliser Helm ?

| Problème | Solution Helm |
|--------|---------------|
| Gérer manuellement 50+ fichiers YAML | Regrouper en un seul chart |
| Déployer la même application sur dev/stage/prod | Utiliser des surcharges `values.yaml` |
| Annuler des déploiements échoués | `helm rollback` |
| Partager des applications entre les équipes | Publier les charts dans un dépôt |
| Versionner l'infrastructure | Version sémantique des charts |

---

## Concepts de Base

### 1. **Chart**
- Structure de répertoire contenant les manifests Kubernetes et les métadonnées.
- Exemple : `my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # Métadonnées (nom, version, etc.)
├── values.yaml         # Valeurs de configuration par défaut
├── templates/          # Templates Kubernetes YAML
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # Fragments de template réutilisables
└── charts/             # Sous-charts (dépendances)
```

### 2. **Release**
- Une instance d'un chart exécutée dans un cluster.
- Un chart → plusieurs releases (par exemple, `myapp-dev`, `myapp-prod`).

### 3. **Repository**
- Serveur HTTP hébergeant des charts indexés (comme le registre npm).
- Communs : ChartMuseum, Harbor, Nexus, GitHub Pages, S3.

### 4. **Tiller** (Obsolète)
- Helm v2 utilisait un composant côté serveur appelé Tiller.
- **Helm v3+ supprime Tiller** → client uniquement, plus sécurisé.

---

## Aide-mémoire des Commandes Helm

| Commande | Objectif |
|-------|--------|
| `helm create mychart` | Créer un squelette pour un nouveau chart |
| `helm lint mychart/` | Valider le chart |
| `helm package mychart/` | Créer une archive `.tgz` |
| `helm repo add stable https://charts.helm.sh/stable` | Ajouter un dépôt |
| `helm repo update` | Mettre à jour le cache local |
| `helm search repo nginx` | Trouver des charts |
| `helm install myapp ./mychart` | Déployer une release |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | Mettre à niveau avec de nouvelles valeurs |
| `helm rollback myapp 3` | Revenir à la révision 3 |
| `helm uninstall myapp` | Supprimer une release |
| `helm list` | Lister les releases |
| `helm status myapp` | Afficher le statut de la release |
| `helm template ./mychart -f values.yaml` | Rendre les templates localement |

---

## Structure Approfondie d'un Chart

### `Chart.yaml` (Obligatoire)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: Une application web exemple
type: application
keywords:
  - web
  - http
home: https://example.com
sources:
  - https://github.com/user/my-app
maintainers:
  - name: Équipe de Développement
    email: dev@example.com
icon: https://example.com/logo.png
```

### `values.yaml` (Valeurs par défaut)
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

### `_helpers.tpl` (Bonne Pratique)
```tpl
{{/* Générer des labels basiques */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Helm dans un Pipeline CI/CD Jenkins

Voici un **Pipeline Jenkins** typique utilisant Helm :

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
            input { message "Déployer en production ?" }
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

### Plugins Jenkins Clés
- **Kubernetes CLI** (`kubectl`)
- **Helm** (via le binaire `helm` dans l'agent)
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding** (pour kubeconfig, registre)

---

## Bonnes Pratiques

| Pratique | Pourquoi |
|--------|-----|
| Utiliser `helm lint` + `helm template` en CI | Détecter les erreurs tôt |
| Versionner les charts sémantiquement | `1.0.0` → `1.0.1` pour la config, `1.1.0` pour les nouvelles fonctionnalités |
| Utiliser `appVersion` pour l'app, `version` pour le chart | Découpler l'application et l'empaquetage |
| Séparer les environnements avec `-f values-env.yaml` | Éviter la duplication des charts |
| Utiliser `helm secrets` ou SOPS pour les secrets | Ne jamais commettre en clair |
| Épingler les versions des dépendances | `helm dependency update --version X` |
| Utiliser les helpers `{{ include "chart.labels" . }}` | Labeling cohérent |
| Activer `--atomic` pour les mises à niveau en prod | Annulation automatique en cas d'échec |

---

## Outils et Intégrations Courants

| Outil | Utilisation avec Helm |
|------|---------------|
| **ChartMuseum** | Dépôt de charts léger |
| **Harbor / Nexus** | Registre d'entreprise + dépôt Helm |
| **ArgoCD** | GitOps + Helm |
| **Flux** | GitOps avec Helm Operator |
| **helmfile** | Gérer plusieurs releases de manière déclarative |
| **k3s / kind** | Tests locaux |

---

## Conseils de Dépannage

| Problème | Solution |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | Attendre ou utiliser `--force` (dangereux) |
| Templates non rendus | Utiliser `helm template .` localement |
| ImagePullBackOff | Vérifier le tag, l'authentification du registre |
| Release introuvable | `helm ls --all --all-namespaces` |
| CRDs non appliqués | Ajouter un dossier `crds/` et les appliquer séparément |

---

## Exemple : Déployer NGINX avec Helm

```bash
# Ajouter un dépôt
helm repo add bitnami https://charts.bitnami.com/bitnami

# Installer
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# Mettre à niveau
helm upgrade web-server bitnami/nginx --set replicaCount=5

# Revenir en arrière
helm rollback web-server 1
```

---

## Ressources

- [Documentation Officielle Helm](https://helm.sh/docs/)
- [Helm Hub (Dépôt de Charts)](https://hub.helm.sh/)
- [Artifact Hub (Recherche de Charts Moderne)](https://artifacthub.io/)
- [Bonnes Pratiques Helm](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Site Officiel Helm](https://helm.sh)  
[Charts Bitnami](https://github.com/bitnami/charts)  
[Helm dans Jenkins X](https://www.jenkins-x.io/docs/)