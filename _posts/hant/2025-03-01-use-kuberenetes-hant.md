---
audio: false
lang: hant
layout: post
title: 如何使用 Kubernetes
translated: true
---

Kubernetes（常縮寫為 K8s）是一個開源平台，用於自動化部署、擴展和操作容器化應用程序。以下是如何有效使用 Kubernetes 的分步指南。

---

### 1. **設置 Kubernetes 集群**
在部署應用程序之前，您需要一個 Kubernetes 集群——一組運行您的容器化工作負載的機器（節點），由控制平面管理。

- **用於本地開發：**
  - 使用 [Minikube](https://minikube.sigs.k8s.io/docs/start/) 或 [Docker Desktop](https://www.docker.com/products/docker-desktop) 在本地機器上設置單節點集群。
  - 使用 Minikube 的示例：
    ```bash
    minikube start
    ```

- **用於生產：**
  - 使用受管理服務，如 Google Kubernetes Engine (GKE)、Amazon Elastic Kubernetes Service (EKS) 或 Azure Kubernetes Service (AKS)。
  - 或者，使用 [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) 手動設置集群。
  - 使用受管理服務（例如 GKE）的示例：
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **創建應用程序的 Docker 映像**
Kubernetes 管理容器化應用程序，通常使用 Docker 容器。

- 編寫一個 `Dockerfile` 來定義應用程序的環境。示例：
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- 建立 Docker 映像：
  ```bash
  docker build -t your-image-name:latest .
  ```

- 將映像推送到容器註冊表（例如 Docker Hub）：
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **定義 Kubernetes 對象**
Kubernetes 使用 YAML 文件來定義資源，如 Pods、Services 和 Deployments。

- **Pod：** 最小可部署單位，包含一個或多個容器。
- **Service：** 將應用程序暴露給網絡。
- **Deployment：** 管理 Pods，確保運行所需數量並處理更新。

示例 `Deployment` YAML 文件 (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # Pod 實例數
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

### 4. **部署應用程序**
使用 `kubectl` 命令行工具與集群交互並部署應用程序。

- 將 YAML 文件應用到集群：
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- 驗證部署：
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **管理應用程序**
`kubectl` 提供命令來監控和管理應用程序：

- **擴展應用程序：**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **檢查 Pod 狀態：**
  ```bash
  kubectl get pods
  ```

- **查看日誌：**
  ```bash
  kubectl logs <pod-name>
  ```

- **訪問容器：**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### 需要進一步探索的關鍵概念
- **命名空間：** 組織資源並管理訪問（例如 `kubectl create namespace my-namespace`）。
- **ConfigMaps：** 將配置數據與應用程序分開存儲。
- **Secrets：** 管理敏感信息，如密碼。
- **Ingress：** 通過單一入口點將服務外部暴露。

---

### 入門技巧
Kubernetes 是一個強大但複雜的系統。從這些基礎開始——設置集群、部署簡單應用程序和使用 `kubectl`——然後根據需要探索高級功能。要進行實踐，請嘗試官方網站上的教程，如 [Kubernetes 基礎](https://kubernetes.io/docs/tutorials/kubernetes-basics/)。

有了這些基礎，您將能夠有效地使用 Kubernetes 部署和管理容器化應用程序！