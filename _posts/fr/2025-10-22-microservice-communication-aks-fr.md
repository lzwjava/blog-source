---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration de la communication entre microservices dans AKS
translated: true
type: note
---

### Configuration de la communication entre microservices dans Azure Kubernetes Service (AKS)

Dans Azure Kubernetes Service (AKS), les microservices sont généralement déployés en tant que **Pods** gérés par des **Deployments**. Pour leur permettre de communiquer entre eux (par exemple, Service A appelant Service B), vous utilisez des **Services Kubernetes** pour abstraire les IP dynamiques des Pods et fournir des points de terminaison stables. Ceci est réalisé via un réseau interne, en tirant parti de la résolution DNS intégrée de Kubernetes. Voici un guide étape par étape pour configurer et mettre en œuvre cela.

#### 1. **Déployez vos microservices en tant que Deployments**
   Chaque microservice s'exécute dans un Pod (ou un ensemble de Pods pour la mise à l'échelle). Utilisez un Deployment pour les gérer.

   Exemple de YAML pour un Deployment de microservice simple (`service-a-deployment.yaml`) :
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # Ou votre namespace personnalisé
   spec:
     replicas: 3  # Mettez à l'échelle selon les besoins
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
           image: your-registry/service-a:latest  # Par exemple, une image ACR ou Docker Hub
           ports:
           - containerPort: 8080  # Port sur lequel votre application écoute
   ```

   Appliquez-le :
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   Répétez l'opération pour les autres services (par exemple, `service-b`).

#### 2. **Exposez les microservices avec des Services**
   Créez un **Service ClusterIP** pour chaque microservice. Ce type est réservé à la communication interne uniquement (non exposé à l'extérieur du cluster). Il répartit la charge du trafic vers les Pods et fournit un nom DNS.

   Exemple de YAML pour le Service A (`service-a-service.yaml`) :
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # Correspond aux labels du Deployment
     ports:
     - protocol: TCP
       port: 80  # Port du Service (utilisé par les appelants)
       targetPort: 8080  # Port du conteneur du Pod
     type: ClusterIP  # Interne uniquement
   ```

   Appliquez-le :
   ```
   kubectl apply -f service-a-service.yaml
   ```

   Faites de même pour le Service B. Maintenant, les Pods peuvent s'atteindre mutuellement via le nom DNS du Service.

#### 3. **Comment les microservices s'appellent mutuellement**
   - **Découverte basée sur DNS** : Le DNS de Kubernetes résout automatiquement les noms de Service. Depuis un Pod dans le Service A, appelez le Service B en utilisant :
     - `<nom-du-service>.<namespace>.svc.cluster.local` (nom qualifié complet, par exemple `service-b.default.svc.cluster.local`).
     - Ou simplement `<nom-du-service>` s'ils sont dans le même namespace (par exemple `service-b`).
   - **Appels HTTP/gRPC** : Dans le code de votre application, faites des requêtes vers `http://service-b:80/endpoint`. Kubernetes gère la répartition de charge et la tolérance de panne.
     - Exemple en Python (en utilisant requests) :
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - Pour gRPC, utilisez le même nom d'hôte avec le port gRPC.
   - **Mappage de ports** : Le port du Service (par exemple, 80) mappe vers le port cible du Pod (par exemple, 8080). Inutile de coder en dur les IP des Pods—elles changent lors des redémarrages.

   Testez la connectivité depuis un Pod :
   ```
   kubectl exec -it <nom-du-pod-dans-service-a> -- curl http://service-b:80/health
   ```

#### 4. **Options de configuration avancées**
   - **Namespaces** : Déployez les services dans différents namespaces pour l'isolation. Utilisez le DNS complet (par exemple, `service-b.other-ns.svc.cluster.local`).
   - **Network Policies** : Sécurisez la communication avec les politiques Calico ou Azure CNI pour autoriser/refuser le trafic entre les services.
     Exemple de politique autorisant le Service A à appeler le Service B :
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
   - **Service Mesh (par exemple, Istio ou Linkerd)** : Pour la production, ajoutez un mesh pour l'observabilité, mTLS et la gestion du trafic. Installez via Helm sur AKS, puis injectez des proxies sidecar dans les Pods.
   - **Accès externe (si nécessaire)** : Utilisez les Services **LoadBalancer** ou **Ingress** pour les appels sortants, mais utilisez ClusterIP pour la communication interne.

#### 5. **Bonnes pratiques**
   - Utilisez des **variables d'environnement** ou des **ConfigMaps** pour injecter dynamiquement les noms DNS des Services dans les applications.
   - Surveillez avec Azure Monitor for AKS pour suivre le trafic inter-services.
   - Mettez à l'échelle horizontalement avec Horizontal Pod Autoscaler (HPA) basé sur le CPU/la mémoire.
   - Pour les intégrations spécifiques à Azure, utilisez Azure Container Registry (ACR) pour les images et Azure AD pour l'authentification.

Cette configuration garantit une communication fiable et évolutive sans couplage fort. Commencez avec des Services basiques, puis ajoutez la sécurité/le mesh selon les besoins.

[Vue d'ensemble de la mise en réseau AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Documentation sur les Services Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/)  
[Tutoriel sur les microservices AKS](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)