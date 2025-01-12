---
lang: hant
layout: post
title: 在Azure上构建可扩展的应用程序
---

*这篇博客文章是在ChatGPT-4o的协助下完成的。*

---

### 目錄
- [簡介](#簡介)
- [開始使用 Azure 訂閱](#開始使用-azure-訂閱)
- [使用 Azure Kubernetes 服務 (AKS) 部署應用程式](#使用-azure-kubernetes-服務-aks-部署應用程式)
  - [建立與管理 AKS 叢集](#建立與管理-aks-叢集)
  - [部署應用程式](#部署應用程式)
- [從 Pods 取得日誌](#從-pods-取得日誌)
- [使用 Azure Application Insights 進行監控與診斷](#使用-azure-application-insights-進行監控與診斷)
- [利用 Azure 虛擬機器 (VMs)](#利用-azure-虛擬機器-vms)
- [使用 Azure Event Hubs 進行即時資料擷取](#使用-azure-event-hubs-進行即時資料擷取)
- [使用 Azure API 管理服務管理 API](#使用-azure-api-管理服務管理-api)
- [利用 Azure SQL 資料庫](#利用-azure-sql-資料庫)
- [使用 Kusto 查詢語言 (KQL) 查詢日誌](#使用-kusto-查詢語言-kql-查詢日誌)
- [設定警報以進行主動監控](#設定警報以進行主動監控)
- [結論](#結論)

### 引言

在云计算的世界中，微软Azure作为一个强大的平台脱颖而出，用于构建、部署和管理应用程序。在我们最近的项目中，我们利用了多项Azure服务，包括Azure订阅、Azure Kubernetes服务（AKS）、Application Insights、虚拟机（VMs）、事件中心、API管理服务和SQL数据库，以创建一个可扩展且受监控的应用程序基础设施。这篇博客文章概述了我们的方法、使用的工具、最佳实践以及管理集群、获取日志和查询日志的详细步骤。

### Azure 订阅入门指南

Azure订阅是您访问Azure服务的门户。它作为一个容器，承载着您的所有资源，例如虚拟机、数据库和Kubernetes集群。

1. 设置Azure订阅：
   - 注册：如果您还没有Azure账户，请先在[Azure门户](https://portal.azure.com/)注册。
   - 创建订阅：导航至“订阅”部分并创建一个新订阅。这将是您的计费和管理容器。

2. 资源组织：
   - 资源组：根据资源的生命周期和管理标准将其组织到资源组中。
   - 标签：使用标签来添加额外的元数据，以便更轻松地进行资源管理和计费。

### 使用Azure Kubernetes服务（AKS）部署应用程序

Azure Kubernetes Service（AKS）是一项托管的Kubernetes服务，它简化了容器化应用程序的部署、管理和扩展。

#### 创建和管理AKS集群

1. 在Azure门户中创建AKS集群：
   - 设置：在Azure门户中搜索AKS并创建一个新的Kubernetes集群。
   - 配置：选择集群规模，配置节点池，并设置网络。
   - 认证：使用Azure Active Directory（AAD）进行安全的访问控制。
   - 监控：在设置过程中启用监控和日志记录。

2. 使用 Azure CLI 创建 AKS 集群：
   ```sh
   az aks create \
     --resource-group myResourceGroup \
     --name myAKSCluster \
     --node-count 3 \
     --enable-addons monitoring \
     --generate-ssh-keys
   ```

3. 管理您的AKS集群：
   - 擴展集群：
     ```sh
     az aks scale \
       --resource-group myResourceGroup \
       --name myAKSCluster \
       --node-count 5
     ```
   - 升級集群：
     ```sh
     az aks upgrade \
       --resource-group myResourceGroup \
       --name myAKSCluster \
       --kubernetes-version 1.21.2
     ```

#### 部署应用程序

1. 使用Kubernetes清单：为您的部署、服务和其他Kubernetes对象编写YAML文件。
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: myapp
   spec:
     replicas: 2
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
           image: myregistry.azurecr.io/myapp:latest
           ports:
           - containerPort: 80
   ```

2. 使用 kubectl 部署：
   ```sh
   kubectl apply -f myapp-deployment.yaml
   ```

3. Helm Charts: 使用 Helm 來管理 Kubernetes 應用程序及版本控制。
   ```sh
   helm install myapp ./mychart
   ```

### 从 Pod 中获取日志

1. 附加到Pod並獲取日誌：
   ```sh
   kubectl logs <pod名稱>
   ```
   - 若要實時流式傳輸日誌：
     ```sh
     kubectl logs <pod名稱> -f
     ```

2. 使用边车（Sidecar）进行日志记录：
   - 在您的Pod规范中创建一个日志记录边车容器，以便将日志发送到集中式日志服务。

```yaml
spec:
  containers:
  - name: myapp
    image: myregistry.azurecr.io/myapp:latest
    ...
  - name: log-shipper
    image: log-shipper:latest
    ...
```

### 使用 Azure Application Insights 进行监控与诊断

Application Insights 为您的应用程序提供了强大的监控和诊断功能。

1. 设置应用洞察：
   - 集成：将应用洞察SDK添加到您的应用程序代码中。
   - 检测密钥：使用来自应用洞察资源的检测密钥配置您的应用程序。

2. 跟踪性能：
   - 指标：监控响应时间、故障率和应用程序依赖关系。
   - 实时指标流：查看实时性能指标，获取即时洞察。

3. 诊断与故障排除：
   - 应用地图：可视化依赖关系，识别性能瓶颈。
   - 事务诊断：利用分布式追踪技术，跨服务追踪请求路径。

### 利用Azure虚拟机（VMs）

Azure 虚拟机提供了运行非容器化自定义应用程序和服务的灵活性。

1. 配置虚拟机：
   - 创建虚拟机：在Azure门户中，创建新的虚拟机，并选择合适的大小和操作系统。
   - 网络配置：设置虚拟网络、子网和安全组以控制流量。

2. 配置虚拟机：
   - 软件安装：安装所需的软件和依赖项。
   - 安全：定期应用补丁和更新，配置防火墙，并使用网络安全组（NSGs）。

3. 管理虚拟机：
   - 备份与恢复：使用 Azure 备份服务进行虚拟机备份。
   - 监控：利用 Azure Monitor 监控虚拟机性能。

### 使用Azure事件中心实现实时数据摄取

Azure Event Hubs 是一个大数据流处理平台和事件摄取服务，能够每秒接收和处理数百万个事件。

1. 设置事件中心：
   - 创建事件中心命名空间：在Azure门户中，创建一个事件中心命名空间来容纳您的事件中心。
   - 创建事件中心：在命名空间内，创建一个或多个事件中心以捕获您的数据流。

2. 数据摄取：
   - 生产者：配置您的应用程序或服务，使用多种语言（如.NET、Java、Python）提供的SDK将事件发送到事件中心。
   - 分区：利用分区来扩展事件处理能力，确保高吞吐量和并行处理。

3. 处理事件：
   - 消费者：使用消费者组来读取和处理事件。Azure 提供了多种处理选项，包括 Azure 流分析、Azure 函数以及使用事件中心 SDK 进行自定义处理。

4. 监控事件中心：
   - 指标：通过Azure门户监控吞吐量、延迟和事件处理指标。
   - 警报：设置警报以通知您任何问题，例如高延迟或消息丢失。

### 使用Azure API管理服务管理API

Azure API 管理服务提供了一种方法，为现有的后端服务创建一致且现代化的 API 网关。

1. 设置API管理：
   - 创建API管理服务：在Azure门户中搜索API管理并创建新服务。
   - 配置API：从OpenAPI规范、Azure函数或其他后端定义并导入API。

2. 保护API：
   - 认证与授权：采用OAuth2、JWT验证及其他机制来确保API的安全性。
   - 速率限制与流量控制：实施策略以防止API被滥用。

3. 监控与分析：
   - API洞察：追踪使用情况，监控性能，并分析日志。
   - 开发者门户：为开发者提供一个发现和使用API的门户平台。

4. 管理生命周期：
   - 版本控制与修订：无缝管理API的不同版本和修订。
   - 策略管理：应用策略以实现请求的转换、验证和路由。

以及相应的回复。

### 利用Azure SQL数据库

Azure SQL数据库是一种完全托管的关系型数据库，具备内置智能、高可用性和可扩展性。

1. 设置Azure SQL数据库：
   - 创建SQL数据库：在Azure门户中，导航至SQL数据库并创建一个新数据库。
   - 配置数据库：设置数据库大小、性能层级，并配置网络设置。

2. 连接到SQL数据库：
   - 连接字符串：使用提供的连接字符串将您的应用程序连接到SQL数据库。
   - 防火墙规则：配置防火墙规则以允许来自您的应用程序或本地机器的访问。

3. 管理数据库：
   - 备份与恢复：利用自动备份和时间点恢复功能来保护您的数据。
   - 扩展：根据性能需求，灵活扩展或缩减数据库规模。

4. 监控与性能调优：
   - 查询性能洞察：监控并优化查询性能。
   - 自动调优：启用自动调优功能以提升性能。

### 使用Kusto查询语言（KQL）查询日志

Kusto查询语言（KQL）用于查询Azure Monitor日志，为您的日志数据提供强大的洞察力。

1. 基本KQL查詢：
   ```kql
   // 從特定表格中檢索記錄
   LogTableName
   | where TimeGenerated > ago(1h)
   | project TimeGenerated, Level, Message
   ```

2. 過濾與彙總數據：
   ```kql
   LogTableName
   | where TimeGenerated > ago(1h) and Level == "Error"
   | summarize Count=count() by bin(TimeGenerated, 5m)
   ```

3. 連接表格：
   ```kql
   Table1
   | join kind=inner (Table2) on $left.UserId == $right.UserId
   | project Table1.TimeGenerated, Table1.Message, Table2.AdditionalInfo
   ```

4. 基于查询创建警报：
   - 在 Azure 门户中，导航到 Log Analytics 工作区。
   - 点击 `日志` 并输入您的 KQL 查询。
   - 点击 `新建警报规则`，根据查询结果创建警报。

### 设置警报以实现主动监控

Azure 警报帮助您及时了解资源的健康状况和性能。

1. 创建告警：
   - 指标告警：基于CPU使用率、内存使用率和响应时间等指标设置告警。
   - 日志告警：使用KQL（Kusto查询语言）基于日志搜索查询创建告警。

2. 配置操作：
   - 操作组：定义操作组以指定谁将收到通知以及通过何种方式（电子邮件、短信、网络钩子）。
   - 集成：与ITSM工具（如ServiceNow）集成，实现自动化的事件管理。

3. 响应警报：
   - 仪表板：设置Azure仪表板，以提供警报的集中视图。
   - 自动化：利用Azure自动化功能，自动响应特定警报。

### 结论

在本节中，我们探讨了多个关键点，旨在为读者提供一个全面的理解框架。首先，我们回顾了相关背景信息，明确了研究的重要性和必要性。接着，我们详细分析了主要问题和挑战，指出了当前领域内的不足之处。随后，我们提出了一系列解决方案和建议，这些方案不仅具有理论上的创新性，还具备实际操作的可行性。最后，我们总结了研究成果，并展望了未来的研究方向和应用前景。

通过这一系列的探讨，我们希望能够为相关领域的研究者和实践者提供有价值的参考和启示。同时，我们也认识到，任何研究都有其局限性，未来的工作需要在现有基础上进一步深化和拓展。我们期待更多的学者和实践者能够加入到这一领域的研究中来，共同推动知识的进步和实际应用的发展。

总之，本研究不仅丰富了理论体系，也为实际问题的解决提供了新的思路和方法。我们相信，随着研究的不断深入，这一领域将会取得更加丰硕的成果，为社会的发展做出更大的贡献。

通过利用Azure订阅、AKS（Azure Kubernetes服务）、Application Insights（应用洞察）、虚拟机、事件中心、API管理服务和SQL数据库，我们构建了一个可扩展、健壮且受监控的应用程序基础设施。Azure提供的一整套工具确保了我们可以高效地部署、管理和监控我们的应用程序。这一配置不仅提升了我们的应用性能，还为我们提供了主动维护和优化资源所需的洞察力。