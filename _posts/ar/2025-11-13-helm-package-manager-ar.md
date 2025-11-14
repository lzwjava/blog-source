---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: 'هيلم: مدير حزم كوبرنيتس'
translated: true
type: note
---

هيلم (Helm) هو مدير الحزم لـ Kubernetes، وغالبًا ما يُطلق عليه "yum أو apt لـ Kubernetes". فهو يبسط نشر التطبيقات المعقدة وإدارتها وترقيتها على مجموعات Kubernetes من خلال تجميع الموارد المرتبطة (مثل Deployments وServices وConfigMaps وغيرها) في **charts** قابلة لإعادة الاستخدام ومرقمة.

فكر في مخطط Helm مثل صورة Docker لملفات Kubernetes manifests: فهو يحزم ملفات YAML والقوالب والإعدادات الافتراضية والمنطق في وحدة واحدة يمكن تثبيتها بأمر واحد.

في خطوط أنابيب CI/CD مثل **Jenkins**، يُستخدم Helm بشكل شائع لـ:
- بناء واختبار المخططات.
- دفع المخططات إلى المستودعات (مثل ChartMuseum أو Harbor أو Nexus).
- نشر التطبيقات إلى مجموعات التدريب/الإنتاج بأمان.

---

## لماذا نستخدم Helm؟

| المشكلة | حل Helm |
|--------|---------------|
| إدارة 50+ ملف YAML يدويًا | تجميعها في مخطط واحد |
| نشر نفس التطبيق على بيئات dev/stage/prod | استخدام `values.yaml` لتجاوز القيم |
| التراجع عن النشرات الفاشلة | `helm rollback` |
| مشاركة التطبيقات بين الفرق | نشر المخططات في مستودع |
| إصدارات البنية التحتية | استخدام الإصدار الدلالي (Semantic versioning) للمخططات |

---

## المفاهيم الأساسية

### 1. **المخطط (Chart)**
- هيكل دليل يحتوي على أوصاف Kubernetes والبيانات الوصفية.
- مثال: `my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # البيانات الوصفية (الاسم، الإصدار، إلخ)
├── values.yaml         # قيم التكوين الافتراضية
├── templates/          # قوالب Kubernetes YAML
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # مقاطع قوالب قابلة لإعادة الاستخدام
└── charts/             # المخططات الفرعية (التبعيات)
```

### 2. **الإصدار (Release)**
- نسخة من مخطط قيد التشغيل في مجموعة Kubernetes.
- مخطط واحد → إصدارات متعددة (مثال: `myapp-dev`, `myapp-prod`).

### 3. **المستودع (Repository)**
- خادم HTTP يستضيف مخططات مفهرسة (مثل سجل npm).
- أمثلة شائعة: ChartMuseum، Harbor، Nexus، GitHub Pages، S3.

### 4. **Tiller** (لم يعد مستخدمًا)
- استخدم Helm v2 مكونًا جانب الخادم يسمى Tiller.
- **أزال Helm v3+ Tiller** → أصبح يعمل من جانب العميل فقط، مما يجعله أكثر أمانًا.

---

## ملخص أوامر Helm

| الأمر | الغرض |
|-------|--------|
| `helm create mychart` | إنشاء هيكل مخطط جديد |
| `helm lint mychart/` | التحقق من صحة المخطط |
| `helm package mychart/` | إنشاء أرشيف `.tgz` |
| `helm repo add stable https://charts.helm.sh/stable` | إضافة مستودع |
| `helm repo update` | تحديث ذاكرة التخزين المؤقت المحلية |
| `helm search repo nginx` | البحث عن المخططات |
| `helm install myapp ./mychart` | نشر إصدار |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | الترقية بقيم جديدة |
| `helm rollback myapp 3` | التراجع إلى المراجعة 3 |
| `helm uninstall myapp` | حذف الإصدار |
| `helm list` | عرض قائمة الإصدارات |
| `helm status myapp` | عرض حالة الإصدار |
| `helm template ./mychart -f values.yaml` | عرض القوالب محليًا |

---

## نظرة متعمقة على هيكل المخطط

### `Chart.yaml` (مطلوب)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: تطبيق ويب نموذجي
type: application
keywords:
  - web
  - http
home: https://example.com
sources:
  - https://github.com/user/my-app
maintainers:
  - name: فريق التطوير
    email: dev@example.com
icon: https://example.com/logo.png
```

### `values.yaml` (القيم الافتراضية)
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

### `_helpers.tpl` (أفضل ممارسة)
```tpl
{{/* إنشاء تسميات أساسية */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Helm في خط أنابيب Jenkins لـ CI/CD

إليك **خط أنابيب Jenkins** نموذجي يستخدم Helm:

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

### إضافات Jenkins الرئيسية
- **Kubernetes CLI** (`kubectl`)
- **Helm** (عبر ثنائي `helm` في الوكيل)
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding** (لـ kubeconfig، السجل)

---

## أفضل الممارسات

| الممارسة | السبب |
|--------|-----|
| استخدام `helm lint` + `helm template` في CI | اكتشاف الأخطاء مبكرًا |
| إصدار المخططات دلاليًا | `1.0.0` → `1.0.1` للتكوين، `1.1.0` للميزات الجديدة |
| استخدام `appVersion` للتطبيق، `version` للمخطط | فصل التطبيق عن التغليف |
| فصل البيئات باستخدام `-f values-env.yaml` | تجنب تكرار المخططات |
| استخدام `helm secrets` أو SOPS للأسرار | عدم حفظها كنص عادي أبدًا |
- تثبيت إصدارات التبعيات | `helm dependency update --version X` |
| استخدام `{{ include "chart.labels" . }}` للمساعدين | تسمية متسقة |
| تمكين `--atomic` في ترقيات الإنتاج | التراجع التلقائي عند الفشل |

---

## الأدوات والتكاملات الشائعة

| الأداة | الاستخدام مع Helm |
|------|---------------|
| **ChartMuseum** | مستودع مخططات خفيف الوزن |
| **Harbor / Nexus** | سجل مؤسسي + مستودع Helm |
| **ArgoCD** | GitOps + Helm |
| **Flux** | GitOps مع Helm Operator |
| **helmfile** | إدارة إصدارات متعددة بطريقة تصريحية |
| **k3s / kind** | الاختبار المحلي |

---

## نصائح استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | الانتظار أو استخدام `--force` (خطير) |
| القوالب لا تعرض | استخدام `helm template .` محليًا |
| ImagePullBackOff | التحقق من الوسم، مصادقة السجل |
- الإصدار غير موجود | `helm ls --all --all-namespaces` |
| CRDs لم تطبق | إضافة مجلد `crds/` وتطبيقه بشكل منفصل |

---

## مثال: نشر NGINX باستخدام Helm

```bash
# إضافة مستودع
helm repo add bitnami https://charts.bitnami.com/bitnami

# التثبيت
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# الترقية
helm upgrade web-server bitnami/nginx --set replicaCount=5

# التراجع
helm rollback web-server 1
```

---

## الموارد

- [وثائق Helm الرسمية](https://helm.sh/docs/)
- [Helm Hub (مستودع المخططات)](https://hub.helm.sh/)
- [Artifact Hub (بحث مخططات حديث)](https://artifacthub.io/)
- [أفضل ممارسات Helm](https://helm.sh/docs/topics/charts/#chart-best-practices)

[الموقع الرسمي لـ Helm](https://helm.sh)  
[مخططات Bitnami](https://github.com/bitnami/charts)  
[Helm في Jenkins X](https://www.jenkins-x.io/docs/)