---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration der Microservice-Kommunikation in AKS
translated: true
type: note
---

### Konfiguration der Kommunikation zwischen Microservices in Azure Kubernetes Service (AKS)

In Azure Kubernetes Service (AKS) werden Microservices typischerweise als **Pods** bereitgestellt, die von **Deployments** verwaltet werden. Um ihre Kommunikation untereinander zu ermöglichen (z. B. wenn Service A Service B aufruft), werden **Kubernetes Services** verwendet, um die dynamischen IPs der Pods zu abstrahieren und stabile Endpunkte bereitzustellen. Dies geschieht über internes Networking unter Nutzung der integrierten DNS-Auflösung von Kubernetes. Hier ist eine Schritt-für-Schritt-Anleitung zur Konfiguration und Implementierung.

#### 1. **Bereitstellen Ihrer Microservices als Deployments**
   Jeder Microservice läuft in einem Pod (oder einer Gruppe von Pods zur Skalierung). Verwenden Sie ein Deployment, um sie zu verwalten.

   Beispiel-YAML für ein einfaches Microservice-Deployment (`service-a-deployment.yaml`):
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # Oder Ihren benutzerdefinierten Namespace
   spec:
     replicas: 3  # Nach Bedarf skalieren
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
           image: your-registry/service-a:latest  # Z.B. ACR oder Docker Hub Image
           ports:
           - containerPort: 8080  # Port, den Ihre App abhört
   ```

   Anwenden:
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   Wiederholen Sie dies für andere Services (z. B. `service-b`).

#### 2. **Microservices mit Services verfügbar machen**
   Erstellen Sie einen **ClusterIP Service** für jeden Microservice. Dieser Typ ist nur für interne Kommunikation gedacht (nicht außerhalb des Clusters verfügbar). Er lastverteilt den Traffic zu den Pods und stellt einen DNS-Namen bereit.

   Beispiel-YAML für Service A (`service-a-service.yaml`):
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # Stimmt mit den Deployment-Labels überein
     ports:
     - protocol: TCP
       port: 80  # Service-Port (den Aufrufer verwenden)
       targetPort: 8080  # Container-Port des Pods
     type: ClusterIP  # Nur intern
   ```

   Anwenden:
   ```
   kubectl apply -f service-a-service.yaml
   ```

   Machen Sie dasselbe für Service B. Jetzt können Pods sich gegenseitig über den DNS-Namen des Services erreichen.

#### 3. **Wie Microservices sich gegenseitig aufrufen**
   - **DNS-basierte Erkennung**: Das Kubernetes-DNS löst Servicenamen automatisch auf. Von einem Pod in Service A aus rufen Sie Service B auf mit:
     - `<service-name>.<namespace>.svc.cluster.local` (voll qualifiziert, z. B. `service-b.default.svc.cluster.local`).
     - Oder einfach `<service-name>`, wenn im selben Namespace (z. B. `service-b`).
   - **HTTP/gRPC-Aufrufe**: Machen Sie in Ihrem App-Code Anfragen an `http://service-b:80/endpoint`. Kubernetes übernimmt Lastverteilung und Failover.
     - Beispiel in Python (mit requests):
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - Für gRPC verwenden Sie denselben Hostnamen mit dem gRPC-Port.
   - **Port-Mapping**: Der Service-Port (z. B. 80) wird auf den Target-Port des Pods (z. B. 8080) gemappt. Es ist nicht nötig, Pod-IPs hartzucodieren – diese ändern sich bei Neustarts.

   Konnektivität von einem Pod testen:
   ```
   kubectl exec -it <pod-name-in-service-a> -- curl http://service-b:80/health
   ```

#### 4. **Erweiterte Konfigurationsoptionen**
   - **Namespaces**: Stellen Sie Services in verschiedenen Namespaces für Isolation bereit. Verwenden Sie den vollständigen DNS-Namen (z. B. `service-b.other-ns.svc.cluster.local`).
   - **Network Policies**: Sichern Sie die Kommunikation mit Calico- oder Azure-CNI-Richtlinien, um Traffic zwischen Services zu erlauben/zu verweigern.
     Beispielrichtlinie, die Aufrufe von Service A zu Service B erlaubt:
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
   - **Service Mesh (z. B. Istio oder Linkerd)**: Für Produktionsumgebungen fügen Sie ein Mesh für Observability, mTLS und Traffic-Management hinzu. Installieren Sie es via Helm auf AKS und injizieren Sie dann Sidecar-Proxys in die Pods.
   - **Externer Zugriff (falls benötigt)**: Verwenden Sie **LoadBalancer**- oder **Ingress**-Services für ausgehende Aufrufe, aber bleiben Sie für interne Aufrufe bei ClusterIP.

#### 5. **Best Practices**
   - Verwenden Sie **Umgebungsvariablen** oder **ConfigMaps**, um Service-DNS-Namen dynamisch in Apps zu injizieren.
   - Überwachen Sie mit Azure Monitor for AKS, um den Traffic zwischen Services zu verfolgen.
   - Skalieren Sie horizontal mit dem Horizontal Pod Autoscaler (HPA) basierend auf CPU/Arbeitsspeicher.
   - Für Azure-spezifische Integrationen verwenden Sie Azure Container Registry (ACR) für Images und Azure AD für die Authentifizierung.

Dieser Setup gewährleistet zuverlässige, skalierbare Kommunikation ohne enge Kopplung. Beginnen Sie mit einfachen Services und fügen Sie dann je nach Bedarf Sicherheit/Mesh hinzu.

[AKS Networking Overview](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Kubernetes Services Documentation](https://kubernetes.io/docs/concepts/services-networking/service/)  
[AKS Microservices Tutorial](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)