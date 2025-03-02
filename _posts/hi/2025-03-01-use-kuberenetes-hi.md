---
audio: false
generated: true
lang: hi
layout: post
title: Kubernetes Kaise Use Karein
translated: true
---

Kubernetes (कभी-कभी K8s के रूप में संक्षिप्त) एक ओपन-सोर्स प्लेटफॉर्म है जो कंटेनराइज्ड एप्लिकेशन की डिप्लॉयमेंट, स्केलिंग, और ऑपरेशन को ऑटोमेट करने के लिए है। नीचे एक कदम-दर-कदम गाइड है कि कैसे Kubernetes का उपयोग करने के लिए किया जा सकता है।

---

### 1. **एक Kubernetes क्लस्टर सेट अप करें**
आप एप्लिकेशन डिप्लॉय करने से पहले एक Kubernetes क्लस्टर की जरूरत है—एक मशीनों (नोड्स) का सेट जो आपके कंटेनराइज्ड वर्कलोड को चलाते हैं, जो एक कंट्रोल प्लेन द्वारा प्रबंधित होते हैं।

- **लोकल डेवलपमेंट के लिए:**
  - [Minikube](https://minikube.sigs.k8s.io/docs/start/) या [Docker Desktop](https://www.docker.com/products/docker-desktop) का उपयोग करके अपने लोकल मशीन पर एक एकल-नोड क्लस्टर सेट अप करें।
  - Minikube के साथ उदाहरण:
    ```bash
    minikube start
    ```

- **प्रोडक्शन के लिए:**
  - Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), या Azure Kubernetes Service (AKS) जैसे प्रबंधित सेवाओं का उपयोग करें।
  - या [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) के साथ एक क्लस्टर को मैन्युअल रूप से सेट अप करें।
  - एक प्रबंधित सेवा (उदाहरण के लिए, GKE) के साथ उदाहरण:
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **अपने एप्लिकेशन का एक Docker इमेज बनाएं**
Kubernetes कंटेनराइज्ड एप्लिकेशन को प्रबंधित करता है, आमतौर पर Docker कंटेनरों का उपयोग करके।

- एक `Dockerfile` लिखें ताकि आपका एप्लिकेशन का वातावरण परिभाषित हो सके। उदाहरण:
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- Docker इमेज बनाएं:
  ```bash
  docker build -t your-image-name:latest .
  ```

- इमेज को एक कंटेनर रजिस्ट्री (उदाहरण के लिए, Docker Hub) पर पुश करें:
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **Kubernetes ऑब्जेक्ट्स परिभाषित करें**
Kubernetes YAML फाइलों का उपयोग करके Pods, Services, और Deployments जैसे संसाधनों को परिभाषित करता है।

- **Pod:** सबसे छोटा डिप्लॉयमेंट इकाई, जिसमें एक या अधिक कंटेनर होते हैं।
- **Service:** आपका एप्लिकेशन को नेटवर्क पर प्रदर्शित करता है।
- **Deployment:** Pods को प्रबंधित करता है, सुनिश्चित करता है कि उचित संख्या चल रही है और अपडेट्स को संभालता है।

`Deployment` YAML फाइल का उदाहरण (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # Pod instances की संख्या
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
`kubectl` कमांड-लाइन टूल का उपयोग करके अपने क्लस्टर के साथ इंटरैक्ट करें और अपना एप्लिकेशन डिप्लॉय करें।

- YAML फाइल को क्लस्टर पर लागू करें:
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- डिप्लॉयमेंट की पुष्टि करें:
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **एप्लिकेशन प्रबंधित करें**
`kubectl` कमांड्स आपका एप्लिकेशन निगरानी और प्रबंधित करने के लिए प्रदान करता है:

- **एप्लिकेशन को स्केल करें:**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **Pod स्थिति देखें:**
  ```bash
  kubectl get pods
  ```

- **लॉग देखें:**
  ```bash
  kubectl logs <pod-name>
  ```

- **एक कंटेनर तक पहुंचें:**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### आगे की खोज के लिए मुख्य अवधारणाएँ
- **Namespaces:** संसाधनों को संगठित करें और एक्सेस प्रबंधित करें (उदाहरण के लिए, `kubectl create namespace my-namespace`).
- **ConfigMaps:** एप्लिकेशन से अलग रूप से कॉन्फ़िगरेशन डेटा स्टोर करें।
- **Secrets:** सेंसिटिव जानकारी जैसे पासवर्ड प्रबंधित करें।
- **Ingress:** एकल प्रवेश बिंदु के साथ सेवाओं को बाहरी रूप से प्रदर्शित करें।

---

### शुरू करने के लिए टिप्स
Kubernetes एक शक्तिशाली लेकिन जटिल प्रणाली है। इन बुनियादी चीजों से शुरू करें—एक क्लस्टर सेट अप करें, एक सरल एप्लिकेशन डिप्लॉय करें, और `kubectl` का उपयोग करें—फिर आवश्यकता के अनुसार उन्नत विशेषताओं की खोज करें। हाथों से अभ्यास के लिए, आधिकारिक साइट पर [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) जैसे ट्यूटोरियल्स की कोशिश करें।

इस आधार के साथ, आप Kubernetes का उपयोग करके कंटेनराइज्ड एप्लिकेशन को डिप्लॉय और प्रबंधित करने में सक्षम होंगे!