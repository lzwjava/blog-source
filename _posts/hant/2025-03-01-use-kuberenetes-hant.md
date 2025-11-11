---
audio: false
generated: true
lang: hant
layout: post
title: 如何使用 Kubernetes
translated: true
type: note
---

Kubernetes（常簡稱為 K8s）是一個開源平台，用於自動化部署、擴展及管理容器化應用程式。以下是如何有效使用 Kubernetes 的逐步指南。

---

### 1. **設定 Kubernetes 集群**
在部署應用程式之前，你需要一個 Kubernetes 集群——一組運行容器化工作負載的機器（節點），由控制平面管理。

- **本地開發用途：**
  - 使用 [Minikube](https://minikube.sigs.k8s.io/docs/start/) 或 [Docker Desktop](https://www.docker.com/products/docker-desktop) 在本地機器上設定單節點集群。
  - Minikube 範例：
    ```bash
    minikube start
    ```

- **生產環境用途：**
  - 使用託管服務，例如 Google Kubernetes Engine (GKE)、Amazon Elastic Kubernetes Service (EKS) 或 Azure Kubernetes Service (AKS)。
  - 或者，使用 [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) 手動設定集群。
  - 託管服務範例（例如 GKE）：
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **建立應用程式的 Docker 映像**
Kubernetes 管理容器化應用程式，通常使用 Docker 容器。

- 編寫 `Dockerfile` 以定義應用程式的環境。範例：
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

- 將映像推送至容器註冊表（例如 Docker Hub）：
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **定義 Kubernetes 物件**
Kubernetes 使用 YAML 檔案定義資源，例如 Pods、Services 和 Deployments。

- **Pod：** 最小的可部署單位，包含一個或多個容器。
- **Service：** 將應用程式暴露至網絡。
- **Deployment：** 管理 Pods，確保運行所需數量並處理更新。

範例 `Deployment` YAML 檔案 (`my-app-deployment.yaml`)：
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # Pod 實例數量
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

### 4. **部署應用程式**
使用 `kubectl` 命令列工具與集群互動並部署應用程式。

- 將 YAML 檔案應用至集群：
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- 驗證部署：
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **管理應用程式**
`kubectl` 提供命令以監控和管理應用程式：

- **擴展應用程式：**
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

- **存取容器：**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### 可進一步探索的關鍵概念
- **Namespaces：** 組織資源並管理存取（例如 `kubectl create namespace my-namespace`）。
- **ConfigMaps：** 將配置數據與應用程式分開儲存。
- **Secrets：** 管理敏感資訊，如密碼。
- **Ingress：** 透過單一入口點將服務暴露至外部。

---

### 入門提示
Kubernetes 是一個功能強大但複雜的系統。從這些基礎開始——設定集群、部署簡單應用程式及使用 `kubectl`——然後按需要探索進階功能。如需動手實踐，可嘗試官方網站的教程，例如 [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)。

有了這個基礎，你將能夠使用 Kubernetes 有效部署和管理容器化應用程式！