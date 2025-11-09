---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 AKS 中配置微服務通訊
translated: true
type: note
---

### 在 Azure Kubernetes Service (AKS) 中配置微服務間的通訊

在 Azure Kubernetes Service (AKS) 中，微服務通常以 **Pods** 的形式部署，並由 **Deployments** 管理。要讓它們能夠互相通訊（例如服務 A 呼叫服務 B），您需要使用 **Kubernetes Services** 來抽象化 Pods 的動態 IP 並提供穩定的端點。這是透過內部網路實現的，利用了 Kubernetes 內建的 DNS 解析功能。以下是如何配置和實現此功能的逐步指南。

#### 1. **將您的微服務部署為 Deployments**
   每個微服務在一個 Pod（或一組用於擴展的 Pods）中運行。使用 Deployment 來管理它們。

   簡單微服務 Deployment 的 YAML 範例 (`service-a-deployment.yaml`)：
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # 或您的自訂命名空間
   spec:
     replicas: 3  # 按需擴展
     selector:
       matchLabels:
         app: service-a
     template:
       metadata:
         labels:
           app: service-a
       spec:
         containers:
         - name: service-a
           image: your-registry/service-a:latest  # 例如，ACR 或 Docker Hub 映像
           ports:
           - containerPort: 8080  # 您的應用程式監聽的端口
   ```

   應用它：
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   對其他服務（例如 `service-b`）重複此步驟。

#### 2. **使用 Services 公開微服務**
   為每個微服務建立一個 **ClusterIP Service**。此類型僅用於內部通訊（不暴露到叢集外部）。它會對流量進行負載平衡，並提供 DNS 名稱。

   服務 A 的 YAML 範例 (`service-a-service.yaml`)：
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # 與 Deployment 標籤匹配
     ports:
     - protocol: TCP
       port: 80  # 服務端口（呼叫者使用的端口）
       targetPort: 8080  # Pod 的容器端口
     type: ClusterIP  # 僅限內部
   ```

   應用它：
   ```
   kubectl apply -f service-a-service.yaml
   ```

   對服務 B 執行相同操作。現在，Pods 可以透過 Service 的 DNS 名稱互相訪問。

#### 3. **微服務如何互相呼叫**
   - **基於 DNS 的服務發現**：Kubernetes DNS 會自動解析 Service 名稱。從服務 A 中的 Pod，使用以下方式呼叫服務 B：
     - `<service-name>.<namespace>.svc.cluster.local`（完整限定名稱，例如 `service-b.default.svc.cluster.local`）。
     - 或者，如果在同一命名空間中，只需使用 `<service-name>`（例如 `service-b`）。
   - **HTTP/gRPC 呼叫**：在您的應用程式程式碼中，向 `http://service-b:80/endpoint` 發出請求。Kubernetes 會處理負載平衡和故障轉移。
     - Python 範例（使用 requests）：
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - 對於 gRPC，使用相同的主機名稱和 gRPC 端口。
   - **端口映射**：服務端口（例如 80）映射到 Pod 的目標端口（例如 8080）。無需硬編碼 Pod IPs——它們在重啟時會改變。

   從 Pod 測試連線：
   ```
   kubectl exec -it <pod-name-in-service-a> -- curl http://service-b:80/health
   ```

#### 4. **進階配置選項**
   - **命名空間**：將服務部署在不同的命名空間中以實現隔離。使用完整 DNS（例如 `service-b.other-ns.svc.cluster.local`）。
   - **網路策略**：使用 Calico 或 Azure CNI 策略來保護通訊，允許/拒絕服務之間的流量。
     允許服務 A 呼叫服務 B 的策略範例：
     ```yaml
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: allow-service-a-to-b
     spec:
       podSelector:
         matchLabels:
           app: service-b
       policyTypes:
       - Ingress
       ingress:
       - from:
         - podSelector:
             matchLabels:
               app: service-a
         ports:
         - protocol: TCP
           port: 80
     ```
   - **服務網格（例如 Istio 或 Linkerd）**：在生產環境中，添加網格以實現可觀測性、mTLS 和流量管理。透過 Helm 在 AKS 上安裝，然後將邊車代理注入到 Pods 中。
   - **外部存取（如果需要）**：使用 **LoadBalancer** 或 **Ingress** Services 進行出站呼叫，但內部通訊請堅持使用 ClusterIP。

#### 5. **最佳實踐**
   - 使用 **環境變數** 或 **ConfigMaps** 將 Service DNS 名稱動態注入到應用程式中。
   - 使用 Azure Monitor for AKS 監控服務間流量。
   - 根據 CPU/記憶體使用情況，使用 Horizontal Pod Autoscaler (HPA) 進行水平擴展。
   - 對於 Azure 特定的整合，請使用 Azure Container Registry (ACR) 儲存映像，並使用 Azure AD 進行身份驗證。

此設定確保了可靠、可擴展的通訊，而無需緊密耦合。從基本的 Services 開始，然後根據需要添加安全/網格層。

[AKS 網路概述](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Kubernetes Services 文件](https://kubernetes.io/docs/concepts/services-networking/service/)  
[AKS 微服務教學](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)