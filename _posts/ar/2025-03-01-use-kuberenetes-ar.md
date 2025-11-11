---
audio: false
generated: true
lang: ar
layout: post
title: كيفية استخدام كوبرنيتس
translated: true
type: note
---

Kubernetes (يُختصر غالبًا كـ K8s) هو منصة مفتوحة المصدر لأتمتة نشر وتوسيع نطاق وتشغيل التطبيقات المعتمدة على الحاويات. فيما يلي دليل خطوة بخطوة حول كيفية استخدام Kubernetes بشكل فعال.

---

### 1. **إعداد مجموعة Kubernetes (Cluster)**
قبل أن تتمكن من نشر التطبيقات، تحتاج إلى مجموعة Kubernetes (Cluster) – وهي مجموعة من الآلات (العُقد) التي تشغّل عبء العمل المعتمد على الحاويات الخاص بك، وتديرها وحدة تحكم (control plane).

- **للتطوير المحلي:**
  - استخدم [Minikube](https://minikube.sigs.k8s.io/docs/start/) أو [Docker Desktop](https://www.docker.com/products/docker-desktop) لإعداد مجموعة عُقدة واحدة على جهازك المحلي.
  - مثال باستخدام Minikube:
    ```bash
    minikube start
    ```

- **لبيئة الإنتاج:**
  - استخدم الخدمات المُدارة مثل Google Kubernetes Engine (GKE) أو Amazon Elastic Kubernetes Service (EKS) أو Azure Kubernetes Service (AKS).
  - بدلاً من ذلك، يمكنك إعداد مجموعة يدويًا باستخدام [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/).
  - مثال باستخدام خدمة مُدارة (مثل GKE):
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **إنشاء صورة Docker لتطبيقك**
تدير Kubernetes التطبيقات المعتمدة على الحاويات، وعادةً ما تستخدم حاويات Docker.

- اكتب ملف `Dockerfile` لتعريف بيئة تطبيقك. مثال:
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- ابنِ صورة Docker:
  ```bash
  docker build -t your-image-name:latest .
  ```

- ادفع الصورة إلى سجل الحاويات (مثل Docker Hub):
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **تحديد كائنات Kubernetes**
يستخدم Kubernetes ملفات YAML لتحديد الموارد مثل Pods وServices وDeployments.

- **الـ Pod:** أصغر وحدة قابلة للنشر، تحتوي على حاوية واحدة أو أكثر.
- **الـ Service:** يعرّض تطبيقك للشبكة.
- **الـ Deployment:** يدير الـ Pods، ويضمن تشغيل العدد المطلوب ويتعامل مع التحديثات.

مثال لملف YAML لـ `Deployment` (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # عدد نسخ الـ Pod
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: your-image-name:latest
```

---

### 4. **نشر التطبيق**
استخدم أداة سطر الأوامر `kubectl` للتفاعل مع مجموعتك ونشر تطبيقك.

- طبق ملف YAML على المجموعة:
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- تحقق من النشر:
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **إدارة التطبيق**
توفر `kubectl` أوامر لمراقبة وإدارة تطبيقك:

- **غيّر حجم التطبيق:**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **تحقق من حالة الـ Pod:**
  ```bash
  kubectl get pods
  ```

- **عرض السجلات:**
  ```bash
  kubectl logs <pod-name>
  ```

- **الوصول إلى حاوية:**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### مفاهيم رئيسية لاستكشافها بشكل أعمق
- **النطاقات (Namespaces):** نظم الموارد وأدر الوصول (مثال: `kubectl create namespace my-namespace`).
- **ConfigMaps:** خزن بيانات التهيئة بشكل منفصل عن التطبيق.
- **الأسرار (Secrets):** أدر المعلومات الحساسة مثل كلمات المرور.
- **Ingress:** عرّض الخدمات خارجيًا من خلال نقطة دخول واحدة.

---

### نصائح للبدء
Kubernetes نظام قوي ولكنه معقد. ابدأ بهذه الأساسيات – إعداد مجموعة، ونشر تطبيق بسيط، واستخدام `kubectl` – ثم استكشف الميزات المتقدمة حسب الحاجة. للتدريب العملي، جرب برامج تعليمية مثل [أساسيات Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/) على الموقع الرسمي.

بهذه الأساسيات، ستتمكن من استخدام Kubernetes لنشر وإدارة التطبيقات المعتمدة على الحاويات بشكل فعال!