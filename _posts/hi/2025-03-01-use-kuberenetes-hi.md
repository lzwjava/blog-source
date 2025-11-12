---
audio: false
generated: true
lang: hi
layout: post
title: कुबेरनेटेस का उपयोग कैसे करें
translated: true
type: note
---

Kubernetes (जिसे अक्सर K8s कहा जाता है) कंटेनराइज्ड एप्लिकेशन के डिप्लॉयमेंट, स्केलिंग और ऑपरेशन को स्वचालित करने के लिए एक ओपन-सोर्स प्लेटफॉर्म है। नीचे Kubernetes का प्रभावी ढंग से उपयोग करने के तरीके पर एक चरण-दर-चरण मार्गदर्शिका दी गई है।

---

### 1. **Kubernetes क्लस्टर सेट अप करें**
एप्लिकेशन डिप्लॉय करने से पहले, आपको एक Kubernetes क्लस्टर की आवश्यकता होती है—मशीनों (नोड्स) का एक समूह जो आपके कंटेनराइज्ड वर्कलोड को चलाता है, जिसे एक कंट्रोल प्लेन द्वारा प्रबंधित किया जाता है।

- **लोकल डेवलपमेंट के लिए:**
  - अपने लोकल मशीन पर सिंगल-नोड क्लस्टर सेट अप करने के लिए [Minikube](https://minikube.sigs.k8s.io/docs/start/) या [Docker Desktop](https://www.docker.com/products/docker-desktop) का उपयोग करें।
  - Minikube के साथ उदाहरण:
    ```bash
    minikube start
    ```

- **प्रोडक्शन के लिए:**
  - Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), या Azure Kubernetes Service (AKS) जैसी मैनेज्ड सर्विसेज का उपयोग करें।
  - वैकल्पिक रूप से, [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) के साथ मैन्युअल रूप से एक क्लस्टर सेट अप करें।
  - मैनेज्ड सर्विस के साथ उदाहरण (जैसे, GKE):
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **अपने एप्लिकेशन की Docker इमेज बनाएं**
Kubernetes कंटेनराइज्ड एप्लिकेशन को मैनेज करता है, आमतौर पर Docker कंटेनर का उपयोग करते हुए।

- अपने एप्लिकेशन के एनवायरनमेंट को परिभाषित करने के लिए एक `Dockerfile` लिखें। उदाहरण:
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- Docker इमेज बिल्ड करें:
  ```bash
  docker build -t your-image-name:latest .
  ```

- इमेज को एक कंटेनर रजिस्ट्री (जैसे, Docker Hub) पर पुश करें:
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **Kubernetes ऑब्जेक्ट्स को परिभाषित करें**
Kubernetes, Pods, Services और Deployments जैसे रिसोर्सेज को परिभाषित करने के लिए YAML फाइलों का उपयोग करता है।

- **Pod:** सबसे छोटी डिप्लॉय करने योग्य इकाई, जिसमें एक या अधिक कंटेनर होते हैं।
- **Service:** आपके एप्लिकेशन को नेटवर्क पर एक्सपोज़ करता है।
- **Deployment:** Pods को मैनेज करता है, यह सुनिश्चित करता है कि वांछित संख्या चल रही हो और अपडेट को हैंडल करता है।

उदाहरण `Deployment` YAML फाइल (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # Pod इंस्टेंस की संख्या
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

### 4. **एप्लिकेशन डिप्लॉय करें**
अपने क्लस्टर के साथ इंटरैक्ट करने और अपना एप्लिकेशन डिप्लॉय करने के लिए `kubectl` कमांड-लाइन टूल का उपयोग करें।

- YAML फाइल को क्लस्टर पर अप्लाई करें:
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- डिप्लॉयमेंट को वेरिफाई करें:
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **एप्लिकेशन को मैनेज करें**
`kubectl` आपके एप्लिकेशन को मॉनिटर और मैनेज करने के लिए कमांड प्रदान करता है:

- **एप्लिकेशन को स्केल करें:**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **Pod स्टेटस चेक करें:**
  ```bash
  kubectl get pods
  ```

- **लॉग्स देखें:**
  ```bash
  kubectl logs <pod-name>
  ```

- **कंटेनर में एक्सेस करें:**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### आगे एक्सप्लोर करने के लिए मुख्य अवधारणाएं
- **Namespaces:** रिसोर्सेज को व्यवस्थित करें और एक्सेस मैनेज करें (जैसे, `kubectl create namespace my-namespace`)।
- **ConfigMaps:** एप्लिकेशन से अलग कॉन्फ़िगरेशन डेटा स्टोर करें।
- **Secrets:** पासवर्ड जैसी संवेदनशील जानकारी को मैनेज करें।
- **Ingress:** सिंगल एंट्री पॉइंट के साथ सर्विसेज को बाहरी रूप से एक्सपोज़ करें।

---

### शुरुआत करने के टिप्स
Kubernetes एक शक्तिशाली लेकिन जटिल सिस्टम है। इन बुनियादी बातों—क्लस्टर सेट अप करना, एक सरल एप्लिकेशन डिप्लॉय करना और `kubectl` का उपयोग करना—से शुरुआत करें, फिर आवश्यकतानुसार उन्नत सुविधाओं का पता लगाएं। हाथों-हाथ अभ्यास के लिए, आधिकारिक साइट पर [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) जैसे ट्यूटोरियल आज़माएं।

इस आधार के साथ, आप कंटेनराइज्ड एप्लिकेशन को प्रभावी ढंग से डिप्लॉय और मैनेज करने के लिए Kubernetes का उपयोग करने में सक्षम होंगे!