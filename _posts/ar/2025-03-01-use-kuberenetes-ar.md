---
audio: false
lang: ar
layout: post
title: كيفية استخدام Kubernetes
translated: true
---

Kubernetes (يُختصر غالبًا باسم K8s) هو منصة مفتوحة المصدر لتأتمتة نشر وتوسيع وإدارة تطبيقات المحتوية. أدناه دليل خطوة بخطوة حول كيفية استخدام Kubernetes بشكل فعال.

---

### 1. **إعداد مجموعة Kubernetes**
قبل أن يمكنك نشر التطبيقات، تحتاج إلى مجموعة Kubernetes - مجموعة من الآلات (الأعمد) التي تعمل على حملات المحتويات الخاصة بك، والتي يتم إدارتها بواسطة لوحة تحكم.

- **للإنتاج المحلي:**
  - استخدم [Minikube](https://minikube.sigs.k8s.io/docs/start/) أو [Docker Desktop](https://www.docker.com/products/docker-desktop) لإعداد مجموعة واحدة من العقد على جهازك المحلي.
  - مثال باستخدام Minikube:
    ```bash
    minikube start
    ```

- **للإنتاج:**
  - استخدم خدمات إدارة مثل Google Kubernetes Engine (GKE)، Amazon Elastic Kubernetes Service (EKS)، أو Azure Kubernetes Service (AKS).
  - أو قم بإعداد مجموعة يدويًا باستخدام [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/).
  - مثال باستخدام خدمة إدارة (مثل GKE):
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **إنشاء صورة Docker لتطبيقك**
Kubernetes يدير تطبيقات المحتوية، عادةً باستخدام محتويات Docker.

- أكتب ملف `Dockerfile` لتحديد بيئة تطبيقك. مثال:
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- بناء الصورة Docker:
  ```bash
  docker build -t your-image-name:latest .
  ```

- دفع الصورة إلى سجل محتويات (مثل Docker Hub):
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **تعريف كائنات Kubernetes**
Kubernetes يستخدم ملفات YAML لتعريف الموارد مثل Pods، Services، و Deployments.

- **Pod:** الوحدة الأصغر التي يمكن نشرها، تحتوي على حاوية أو أكثر.
- **Service:** يعرض تطبيقك للشبكة.
- **Deployment:** يدير Pods، يضمن أن العدد المطلوب يعمل ويManage التحديثات.

مثال ملف YAML Deployment (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # عدد منInstances Pod
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
استخدم أداة السطر الأوامر `kubectl` للتفاعل مع مجموعة و نشر تطبيقك.

- تطبيق الملف YAML على المجموعة:
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- التحقق من النشر:
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **إدارة التطبيق**
`kubectl` يوفر الأوامر لمراقبة وإدارة تطبيقك:

- **توسيع التطبيق:**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **تحقق من حالة Pod:**
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

### مفاهيم رئيسية للدراسة
- **المساحات الاسمية:** تنظيم الموارد وإدارة الوصول (مثل `kubectl create namespace my-namespace`).
- **ConfigMaps:** تخزين بيانات التكوين بشكل منفصل عن التطبيق.
- **السر:** إدارة المعلومات الحساسة مثل كلمات المرور.
- **الدخل:** عرض الخدمات خارجيًا مع نقطة دخول واحدة.

---

### نصائح للبدء
Kubernetes هو نظام قوي ولكن معقد. ابدأ بهذه الأساسيات - إعداد مجموعة، نشر تطبيق بسيط، واستخدام `kubectl` - ثم استكشف الميزات المتقدمة حسب الحاجة. للحصول على الممارسة العملية، حاول الدروس مثل [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) على الموقع الرسمي.

مع هذه الأساسيات، ستكون قادرًا على استخدام Kubernetes لنشر وإدارة تطبيقات المحتوية بشكل فعال!