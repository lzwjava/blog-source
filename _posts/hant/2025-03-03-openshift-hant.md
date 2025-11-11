---
audio: false
generated: true
lang: hant
layout: post
title: OpenShift 指南
translated: true
type: note
---

OpenShift 是一個功能強大的平台，能簡化在雲端環境中建置、部署及管理應用程式的流程。由 Red Hat 開發，它運用領先的開源容器協調系統 Kubernetes 的能力，為開發者與組織提供穩定且可擴展的解決方案。無論您是希望簡化工作流程的開發者，還是尋求可靠雲端平台的企業，OpenShift 都能提供符合需求的工具與功能。

在本篇網誌中，我們將探討 OpenShift 的定義、關鍵功能、入門方法以及有效使用技巧。同時也會涵蓋最佳實踐與實際應用案例，助您深入了解其潛力。現在就開始吧！

---

## OpenShift 簡介

OpenShift 是一個平台即服務（PaaS），旨在讓應用程式開發與部署流程無縫銜接。建基於 Kubernetes 之上，它透過專為企業級容器管理打造的附加工具，延伸了核心協調能力。OpenShift 讓開發者能專注於編寫程式碼，同時自動化處理部署、擴展及維護的複雜性。

該平台支援多種程式語言、框架及資料庫，適用於各類應用程式。它還在本地、公有及混合雲基礎架構間提供一致的環境，為現代軟體開發帶來靈活性與可擴展性。

---

## OpenShift 的關鍵功能

OpenShift 憑藉其豐富功能組合，在容器化應用程式管理方面表現卓越。以下是一些重點功能：

- **容器管理**：以 Kubernetes 為核心，自動化跨集群的容器部署、擴展與操作。
- **開發者工具**：整合持續整合與持續部署（CI/CD）工具（如 Jenkins），簡化開發流程。
- **多語言支援**：使用您偏好的框架，以 Java、Node.js、Python、Ruby 等語言建置應用程式。
- **安全性**：內建角色型存取控制（RBAC）、網路政策及映像掃描等功能，確保應用程式安全無虞。
- **可擴展性**：水平擴展（增加實例）或垂直擴展（增加資源）以滿足需求。
- **監控與記錄**：透過 Prometheus、Grafana、Elasticsearch 及 Kibana 等工具，深入掌握應用程式效能與記錄。

這些功能使 OpenShift 成為管理從開發到生產整個應用程式生命週期的一站式解決方案。

---

## 如何開始使用 OpenShift

開始使用 OpenShift 非常簡單。請遵循以下步驟設定環境並部署您的第一個應用程式。

### 步驟 1：註冊或安裝 OpenShift
- **雲端選項**：於 [Red Hat OpenShift Online](https://www.openshift.com/products/online/) 註冊免費帳戶，在雲端使用 OpenShift。
- **本地選項**：安裝 [Minishift](https://docs.okd.io/latest/minishift/getting-started/installing.html)，在本地運行單節點 OpenShift 集群以供開發使用。

### 步驟 2：安裝 OpenShift CLI
OpenShift 命令行介面（CLI）`oc` 讓您能從終端機與平台互動。請從 [官方 OpenShift CLI 頁面](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html) 下載，並依照您的作業系統安裝說明進行操作。

### 步驟 3：登入並建立專案
- 使用 CLI 登入您的 OpenShift 集群：
  ```bash
  oc login <cluster-url> --token=<your-token>
  ```
  請將 `<cluster-url>` 和 `<your-token>` 替換為您的 OpenShift 實例提供的詳細資訊。
- 建立新專案以組織您的應用程式：
  ```bash
  oc new-project my-first-project
  ```

### 步驟 4：部署應用程式
使用 `oc new-app` 指令部署範例應用程式，例如 Node.js 應用：
```bash
oc new-app nodejs~https://github.com/sclorg/nodejs-ex.git
```
這會利用 OpenShift 的 Source-to-Image（S2I）功能，直接從 Git 儲存庫建置並部署應用程式。

### 步驟 5：公開應用程式
透過建立路由，讓您的應用程式可透過 URL 存取：
```bash
oc expose svc/nodejs-ex
```
執行 `oc get route` 以取得 URL，並在瀏覽器中訪問該網址，即可看到您的應用程式正式上線！

---

## 深入使用 OpenShift

設定完成 OpenShift 後，您可運用其功能有效管理應用程式。以下介紹一些核心功能的運用方式。

### 部署應用程式
OpenShift 提供多種部署應用的靈活性：
- **Source-to-Image（S2I）**：自動從原始碼建置並部署。例如：
  ```bash
  oc new-app python~https://github.com/example/python-app.git
  ```
- **Docker 映像**：部署預先建置的映像：
  ```bash
  oc new-app my-image:latest
  ```
- **範本**：部署常見服務如 MySQL：
  ```bash
  oc new-app --template=mysql-persistent
  ```

### 管理容器
使用 CLI 或網頁控制台管理容器生命週期：
- **開始建置**：`oc start-build <buildconfig>`
- **擴展應用**：`oc scale --replicas=3 dc/<deploymentconfig>`
- **檢視記錄**：`oc logs <pod-name>`

### 擴展應用程式
輕鬆調整應用程式的容量。擴展至三個實例：
```bash
oc scale --replicas=3 dc/my-app
```
OpenShift 會自動在這些複本間進行負載平衡。

### 監控與記錄
透過內建工具掌握應用程式狀態：
- **Prometheus**：監控 CPU 與記憶體使用率等指標。
- **Grafana**：視覺化效能數據。
- **Elasticsearch 與 Kibana**：集中管理與分析記錄。
透過 OpenShift 網頁控制台存取這些工具，即時掌握洞察資訊。

---

## 使用 OpenShift 的最佳實踐

為充分發揮 OpenShift 的潛力，請遵循以下最佳實踐：

- **透過 CI/CD 自動化**：使用 OpenShift 內建的 Jenkins 或整合您偏好的 CI/CD 工具，以簡化工作流程。
- **以範本標準化**：建立可重複使用的範本，確保部署一致性。
- **優先考慮安全性**：實施 RBAC、掃描映像漏洞，並使用網路政策。
- **優化資源**：透過 Prometheus 監控使用情況，調整資源限制以平衡效能與成本。
- **以標籤組織**：為資源添加標籤（例如 `app=my-app`），便於管理。

這些實踐能確保您的應用程式安全、高效且可擴展。

---

## OpenShift 的應用案例

OpenShift 在多種情境下表現卓越：
- **微服務**：透過內建服務發現與負載平衡，管理與擴展微服務。
- **DevOps**：藉由 CI/CD 與自動化工具，銜接開發與維運。
- **混合雲**：無縫部署應用程式至本地與雲端環境。
- **舊系統現代化**：將舊有應用程式容器化，提升可攜性與可擴展性。

這些案例彰顯了 OpenShift 在現代軟體開發中的多元應用性。

---

## 結語

對於希望簡化應用程式開發與管理的開發者及組織而言，OpenShift 是一項革命性的解決方案。憑藉其 Kubernetes 基礎、豐富的功能組合以及對多元工作流程的支援，它讓您能輕鬆建置、部署及擴展應用程式。無論您是在本地使用 Minishift 進行實驗，還是在雲端運行生產工作負載，OpenShift 都能滿足需求。

準備開始使用了嗎？探索 [官方 OpenShift 文件](https://docs.openshift.com/) 或依照上述步驟部署您的第一個應用程式。有了 OpenShift，從程式碼到生產的旅程將比以往更加順暢！