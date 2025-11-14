---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: 'हेल्म: कुबेरनेटेस पैकेज प्रबंधक'
translated: true
type: note
---

Helm कुबेरनेट्स के लिए पैकेज मैनेजर है, जिसे अक्सर "कुबेरनेट्स के लिए yum या apt" कहा जाता है। यह कुबेरनेट्स क्लस्टर पर जटिल एप्लिकेशन को डिप्लॉय, मैनेज और अपग्रेड करना आसान बनाता है, संबंधित संसाधनों (Deployments, Services, ConfigMaps, आदि) को पुन: प्रयोज्य, वर्जन किए गए **चार्ट** में बंडल करके।

एक Helm चार्ट को कुबेरनेट्स मैनिफेस्ट के लिए एक Docker इमेज की तरह समझें: यह YAML फ़ाइलों, टेम्प्लेट, डिफॉल्ट और लॉजिक को एक एकल इकाई में पैकेज करता है जिसे एक कमांड से इंस्टॉल किया जा सकता है।

**Jenkins** जैसी CI/CD पाइपलाइनों में, Helm का आमतौर पर उपयोग किया जाता है:
- चार्ट बनाने और टेस्ट करने के लिए।
- चार्ट को रिपॉजिटरी (जैसे, ChartMuseum, Harbor, Nexus) पर पुश करने के लिए।
- एप्लिकेशन को स्टेजिंग/प्रोडक्शन क्लस्टर पर सुरक्षित रूप से डिप्लॉय करने के लिए।

---

## Helm क्यों उपयोग करें?

| समस्या | Helm समाधान |
|--------|---------------|
| 50+ YAML फ़ाइलों को मैन्युअल रूप से प्रबंधित करना | एक चार्ट में बंडल करें |
| एक ही ऐप को dev/stage/prod में डिप्लॉय करना | `values.yaml` ओवरराइड का उपयोग करें |
| विफल डिप्लॉयमेंट को रोल बैक करना | `helm rollback` |
| टीमों के बीच ऐप साझा करना | चार्ट को रिपॉजिटरी में प्रकाशित करें |
| इन्फ्रास्ट्रक्चर का वर्जनिंग | चार्ट का सिमेंटिक वर्जनिंग |

---

## मूल अवधारणाएँ

### 1. **चार्ट**
- कुबेरनेट्स मैनिफेस्ट और मेटाडेटा युक्त डायरेक्टरी स्ट्रक्चर।
- उदाहरण: `my-app-chart/`

```
my-app-chart/
├── Chart.yaml          # मेटाडेटा (नाम, वर्जन, आदि)
├── values.yaml         # डिफॉल्ट कॉन्फ़िगरेशन वैल्यू
├── templates/          # कुबेरनेट्स YAML टेम्प्लेट
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl    # पुन: प्रयोज्य टेम्प्लेट स्निपेट
└── charts/             # सब-चार्ट (निर्भरताएं)
```

### 2. **रिलीज़**
- क्लस्टर में चल रहे एक चार्ट का उदाहरण।
- एक चार्ट → कई रिलीज़ (जैसे, `myapp-dev`, `myapp-prod`)।

### 3. **रिपॉजिटरी**
- इंडेक्स किए गए चार्ट होस्ट करने वाला HTTP सर्वर (npm रजिस्ट्री की तरह)।
- सामान्य: ChartMuseum, Harbor, Nexus, GitHub Pages, S3।

### 4. **टिलर** (अप्रचलित)
- Helm v2 एक सर्वर-साइड कंपोनेंट टिलर का उपयोग करता था।
- **Helm v3+ टिलर को हटा देता है** → केवल क्लाइंट-साइड, अधिक सुरक्षित।

---

## Helm कमांड्स चीट शीट

| कमांड | उद्देश्य |
|-------|--------|
| `helm create mychart` | नया चार्ट स्कैफोल्ड करें |
| `helm lint mychart/` | चार्ट वैलिडेट करें |
| `helm package mychart/` | `.tgz` आर्काइव बनाएं |
| `helm repo add stable https://charts.helm.sh/stable` | रिपॉजिटरी जोड़ें |
| `helm repo update` | लोकल कैश अपडेट करें |
| `helm search repo nginx` | चार्ट ढूंढें |
| `helm install myapp ./mychart` | रिलीज़ डिप्लॉय करें |
| `helm upgrade myapp ./mychart -f prod-values.yaml` | नई वैल्यूज़ के साथ अपग्रेड करें |
| `helm rollback myapp 3` | रिविज़न 3 पर रोल बैक करें |
| `helm uninstall myapp` | रिलीज़ डिलीट करें |
| `helm list` | रिलीज़ सूचीबद्ध करें |
| `helm status myapp` | रिलीज़ स्टेटस दिखाएं |
| `helm template ./mychart -f values.yaml` | टेम्प्लेट्स को लोकली रेंडर करें |

---

## चार्ट स्ट्रक्चर गहन अध्ययन

### `Chart.yaml` (आवश्यक)
```yaml
apiVersion: v2
kind: Chart
name: my-app
version: 1.2.3
appVersion: "2.5.0"
description: A sample web app
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

### `values.yaml` (डिफॉल्ट)
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

### `_helpers.tpl` (बेस्ट प्रैक्टिस)
```tpl
{{/* Generate basic labels */}}
{{- define "my-app.labels" -}}
helm.sh/chart: {{ include "my-app.chart" . }}
app.kubernetes.io/name: {{ include "my-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

---

## Jenkins CI/CD पाइपलाइन में Helm

यहाँ Helm का उपयोग करते हुए एक विशिष्ट **Jenkins पाइपलाइन** है:

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

### मुख्य Jenkins प्लगइन्स
- **Kubernetes CLI** (`kubectl`)
- **Helm** (एजेंट में `helm` बाइनरी के माध्यम से)
- **Pipeline Utility Steps** (`readYaml`, `writeYaml`)
- **Credentials Binding** (kubeconfig, रजिस्ट्री के लिए)

---

## बेस्ट प्रैक्टिसेज़

| प्रैक्टिस | क्यों |
|--------|-----|
| CI में `helm lint` + `helm template` का उपयोग करें | त्रुटियों को जल्दी पकड़ें |
| चार्ट का सिमेंटिक वर्जनिंग करें | `1.0.0` → `1.0.1` कॉन्फ़िग के लिए, `1.1.0` नई फीचर्स के लिए |
| ऐप के लिए `appVersion`, चार्ट के लिए `version` का उपयोग करें | ऐप और पैकेजिंग को अलग करें |
| `-f values-env.yaml` के साथ एनवायरनमेंट अलग करें | चार्ट डुप्लिकेट करने से बचें |
| सीक्रेट्स के लिए `helm secrets` या SOPS का उपयोग करें | प्लेनटेक्स्ट कभी कमिट न करें |
| डिपेंडेंसी वर्जन पिन करें | `helm dependency update --version X` |
| `{{ include "chart.labels" . }}` हेल्पर्स का उपयोग करें | सुसंगत लेबलिंग |
| prod अपग्रेड में `--atomic` सक्षम करें | विफलता पर ऑटो-रोलबैक |

---

## सामान्य टूल्स और इंटीग्रेशन

| टूल | Helm के साथ उपयोग |
|------|---------------|
| **ChartMuseum** | लाइटवेट चार्ट रिपॉजिटरी |
| **Harbor / Nexus** | एंटरप्राइज़ रजिस्ट्री + Helm रिपॉजिटरी |
| **ArgoCD** | GitOps + Helm |
| **Flux** | Helm ऑपरेटर के साथ GitOps |
| **helmfile** | कई रिलीज़ को डिक्लेरेटिव तरीके से प्रबंधित करें |
| **k3s / kind** | लोकल टेस्टिंग |

---

## ट्रबलशूटिंग टिप्स

| समस्या | समाधान |
|------|-----|
| `Error: UPGRADE FAILED: another operation is in progress` | प्रतीक्षा करें या `--force` का उपयोग करें (खतरनाक) |
| टेम्प्लेट रेंडर नहीं हो रहे | लोकली `helm template .` का उपयोग करें |
| ImagePullBackOff | टैग, रजिस्ट्री ऑथ चेक करें |
| रिलीज़ नहीं मिल रहा | `helm ls --all --all-namespaces` |
| CRDs लागू नहीं हो रहे | `crds/` फोल्डर जोड़ें और अलग से लागू करें |

---

## उदाहरण: Helm के साथ NGINX डिप्लॉय करें

```bash
# रिपॉजिटरी जोड़ें
helm repo add bitnami https://charts.bitnami.com/bitnami

# इंस्टॉल करें
helm install web-server bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=LoadBalancer

# अपग्रेड करें
helm upgrade web-server bitnami/nginx --set replicaCount=5

# रोलबैक करें
helm rollback web-server 1
```

---

## संसाधन

- [आधिकारिक Helm डॉक्स](https://helm.sh/docs/)
- [Helm हब (चार्ट रिपॉजिटरी)](https://hub.helm.sh/)
- [Artifact हब (आधुनिक चार्ट खोज)](https://artifacthub.io/)
- [Helm बेस्ट प्रैक्टिसेज़](https://helm.sh/docs/topics/charts/#chart-best-practices)

[Helm आधिकारिक साइट](https://helm.sh)  
[Bitnami चार्ट्स](https://github.com/bitnami/charts)  
[Jenkins X में Helm](https://www.jenkins-x.io/docs/)