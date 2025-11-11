---
audio: false
generated: true
lang: hant
layout: post
title: Docker 與 Kubernetes 之比較
translated: true
type: note
---

Docker 與 Kubernetes 是容器生態系中相輔相成的技術，但它們的用途各不相同。讓我們剖析它們的差異與關聯。

---

### Docker：容器化平台
**功能**：Docker 是用於創建、運行和管理獨立容器的工具——這種輕量級隔離環境會將應用程式與其依賴項打包在一起。

#### 主要特性
1. **容器運行環境**：
   - Docker 使用運行環境（例如 `containerd` 或 `runc`）來執行基於 Linux 核心功能（如命名空間和 cgroups）的容器。
   - 它負責單一容器的生命週期：構建、啟動、停止等。

2. **映像管理**：
   - Docker 透過 `Dockerfile` 構建映像，其中定義了應用程式、函式庫和配置。
   - 映像儲存在 registry（如 Docker Hub）中，並以容器形式運行。

3. **單主機導向**：
   - Docker 擅長在單一機器上管理容器。您可以運行多個容器，但缺乏跨多主機的內建編排功能。

4. **命令行驅動**：
   - 透過 `docker build`、`docker run` 和 `docker ps` 等指令直接操作容器。

#### 使用場景
- 在筆記型電腦或伺服器上運行單一 Spring Boot 應用程式：
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```

#### 限制
- 無原生多主機支援。
- 缺乏自動擴展、自我修復或負載平衡功能。
- 手動管理大量容器會變得混亂。

---

### Kubernetes：容器編排系統
**功能**：Kubernetes（常簡稱為 K8s）是跨機器集群管理與編排多容器的平台，可自動化容器化應用的部署、擴展和運維。

#### 主要特性
1. **集群管理**：
   - Kubernetes 運行於節點集群（實體或虛擬機器）上。一個節點作為「控制平面」（管理集群），其他節點則為「工作節點」（運行容器）。

2. **編排功能**：
   - **排程**：根據資源與限制條件決定各容器運行的節點。
   - **擴展**：自動增減容器實例數量（例如根據 CPU 使用率）。
   - **自我修復**：重啟故障容器，在節點失效時重新調度，確保維持期望狀態。
   - **負載平衡**：將流量分發至多個容器實例。

3. **抽象層**：
   - 以「Pod」為最小單位——每個 Pod 可包含一或多個共享儲存與網路資源的容器（通常為一個）。
   - 透過宣告式 YAML 檔案進行管理（例如定義部署、服務）。

4. **多主機導向**：
   - 專為分散式系統設計，能跨多台機器協調容器。

5. **生態系**：
   - 包含服務發現、持久化儲存、密鑰管理與滾動更新等功能。

#### 使用場景
- 部署含 10 個服務的微服務應用程式，每個服務均運行於獨立容器中，分佈於 5 台伺服器，並具備自動擴展與容錯移轉：
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: myapp
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: myapp
    template:
      metadata:
        labels:
          app: myapp
      spec:
        containers:
        - name: myapp
          image: myapp:latest
          ports:
          - containerPort: 8080
  ```

#### 限制
- 學習曲線較陡峭。
- 對單機簡單單容器應用而言過於複雜。

---

### 關鍵差異

| 維度                 | Docker                              | Kubernetes                          |
|----------------------|-------------------------------------|-------------------------------------|
| **用途**             | 容器創建與運行環境                  | 容器編排                            |
| **範圍**             | 單一主機                            | 主機集群                            |
| **單位**             | 容器                                | Pod（一組 1+ 容器）                 |
| **擴展**             | 手動（例如多次執行 `docker run`）   | 自動（透過副本數）                  |
| **網路**             | 基礎功能（橋接、主機、覆蓋網路）    | 進階功能（服務、輸入）              |
| **自我修復**         | 無（需手動重啟）                    | 內建（重啟、重新調度）              |
| **管理方式**         | CLI 或 Docker Compose（小型設置）   | YAML 配置、`kubectl` CLI            |
| **依賴項**           | 獨立運行（需 Docker Engine）        | 需容器運行環境（如 Docker）         |

---

### 協作模式
- **Docker 作為運行環境**：Kubernetes 不直接運行容器——它依賴容器運行環境（如 Docker 或替代方案 `containerd`）來啟動和管理 Pod 中的獨立容器。
- **工作流程**：
  1. 構建 Docker 映像（`docker build -t myapp:latest .`）。
  2. 推送至 registry（`docker push myapp:latest`）。
  3. Kubernetes 根據 YAML 配置拉取映像並部署至集群（`kubectl apply -f deployment.yaml`）。

- **範例**：Kubernetes 可能使用 Docker 在不同節點上運行三個 `myapp:latest` 實例，並透過負載平衡服務暴露它們。

---

### 比喻
- **Docker**：在廚房烹飪單道菜色的廚師。您告訴廚師要做什麼（`Dockerfile`）以及如何上菜（`docker run`）。
- **Kubernetes**：餐廳經理統籌多間廚房（節點）中的多位廚師（Docker 實例）。經理確保菜色準時完成，在高峰時段增派人手，並替補生病的廚師。

---

### 適用場景
- **單獨使用 Docker**：適用於開發、測試或單機簡單應用（例如單一 Spring Boot 應用程式）。
- **使用 Kubernetes**：適用於需要高可用性、擴展能力與韌性的生產級分散式應用（例如微服務架構）。

---

這樣的說明是否讓區別更清晰？如果您想深入探討特定面向——例如設定 Kubernetes 或與 Docker Compose 的比較，請告訴我！