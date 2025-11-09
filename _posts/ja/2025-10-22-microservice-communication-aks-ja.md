---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AKSにおけるマイクロサービス通信の構成
translated: true
type: note
---

### Azure Kubernetes Service（AKS）でのマイクロサービス間通信の設定

Azure Kubernetes Service（AKS）では、マイクロサービスは通常、**Deployments**によって管理される**Pods**としてデプロイされます。これらが互いに通信できるようにするためには（例：Service AがService Bを呼び出す）、**Kubernetes Services**を使用してPodsの動的IPアドレスを抽象化し、安定したエンドポイントを提供します。これは、Kubernetesの組み込みDNS解決を活用した内部ネットワーキングを通じて行われます。以下に、これを設定および実装するためのステップバイステップガイドを示します。

#### 1. **マイクロサービスをDeploymentsとしてデプロイする**
   各マイクロサービスはPod（またはスケーリングのための一連のPods）で実行されます。これらを管理するためにDeploymentを使用します。

   シンプルなマイクロサービスDeploymentのYAML例（`service-a-deployment.yaml`）:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # またはカスタムネームスペース
   spec:
     replicas: 3  # 必要に応じてスケール
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
           image: your-registry/service-a:latest  # 例: ACRまたはDocker Hubイメージ
           ports:
           - containerPort: 8080  # アプリがリッスンするポート
   ```

   適用コマンド:
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   他のサービス（例: `service-b`）についても同様に繰り返します。

#### 2. **Servicesを使用してマイクロサービスを公開する**
   各マイクロサービスに対して**ClusterIP Service**を作成します。このタイプは内部通信専用です（クラスター外部には公開されません）。これはトラフィックをPodsに負荷分散し、DNS名を提供します。

   Service AのYAML例（`service-a-service.yaml`）:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # Deploymentのラベルと一致
     ports:
     - protocol: TCP
       port: 80  # サービスポート（呼び出し元が使用するポート）
       targetPort: 8080  # Podのコンテナポート
     type: ClusterIP  # 内部専用
   ```

   適用コマンド:
   ```
   kubectl apply -f service-a-service.yaml
   ```

   Service Bに対しても同様に行います。これで、PodsはServiceのDNS名を介して互いに到達できるようになります。

#### 3. **マイクロサービスが互いに呼び出す方法**
   - **DNSベースのサービスディスカバリー**: Kubernetes DNSがService名を自動的に解決します。Service A内のPodからは、以下を使用してService Bを呼び出せます:
     - `<service-name>.<namespace>.svc.cluster.local`（完全修飾名、例: `service-b.default.svc.cluster.local`）。
     - または、同じネームスペース内であれば単に`<service-name>`（例: `service-b`）。
   - **HTTP/gRPC呼び出し**: アプリコード内で、`http://service-b:80/endpoint` に対してリクエストを行います。Kubernetesが負荷分散とフェイルオーバーを処理します。
     - Pythonでの例（requestsを使用）:
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - gRPCの場合、同じホスト名でgRPCポートを使用します。
   - **ポートマッピング**: サービスポート（例: 80）はPodのターゲットポート（例: 8080）にマッピングされます。PodのIPアドレスは再起動時に変更されるため、ハードコーディングする必要はありません。

   Podから接続性をテスト:
   ```
   kubectl exec -it <service-a内のpod-name> -- curl http://service-b:80/health
   ```

#### 4. **高度な設定オプション**
   - **ネームスペース**: サービスを異なるネームスペースにデプロイして分離します。完全なDNS名（例: `service-b.other-ns.svc.cluster.local`）を使用します。
   - **ネットワークポリシー**: CalicoまたはAzure CNIポリシーを使用して通信を保護し、サービス間のトラフィックを許可/拒否します。
     Service AからService Bへの呼び出しを許可するポリシーの例:
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
   - **サービスメッシュ（例: IstioまたはLinkerd）**: 本番環境では、メッシュを追加して、観測性、mTLS、トラフィック管理を実現します。AKS上でHelm経由でインストールし、サイドカープロキシをPodsにインジェクトします。
   - **外部アクセス（必要な場合）**: アウトバウンド呼び出しには**LoadBalancer**または**Ingress** Servicesを使用しますが、内部通信にはClusterIPを使用します。

#### 5. **ベストプラクティス**
   - サービスDNS名をアプリに動的に注入するために、**環境変数**または**ConfigMaps**を使用します。
   - サービス間トラフィックを追跡するために、Azure Monitor for AKSで監視します。
   - CPU/メモリに基づいてHorizontal Pod Autoscaler（HPA）で水平スケーリングします。
   - Azure固有の統合には、イメージ用にAzure Container Registry（ACR）を、認証用にAzure ADを使用します。

このセットアップにより、密結合なしで信頼性が高くスケーラブルな通信が保証されます。基本的なServicesから始め、必要に応じてセキュリティ/メッシュを追加していきます。

[AKS ネットワーキングの概要](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Kubernetes Services ドキュメント](https://kubernetes.io/docs/concepts/services-networking/service/)  
[AKS マイクロサービス チュートリアル](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)