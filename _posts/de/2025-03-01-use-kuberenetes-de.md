---
audio: false
generated: true
lang: de
layout: post
title: So verwenden Sie Kubernetes
translated: true
type: note
---

Kubernetes (oft als K8s abgekürzt) ist eine Open-Source-Plattform zur Automatisierung der Bereitstellung, Skalierung und Verwaltung von containerisierten Anwendungen. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur effektiven Nutzung von Kubernetes.

---

### 1. **Einrichten eines Kubernetes-Clusters**
Bevor Sie Anwendungen bereitstellen können, benötigen Sie einen Kubernetes-Cluster – eine Gruppe von Maschinen (Nodes), die Ihre containerisierten Workloads ausführen und von einer Control Plane verwaltet werden.

- **Für die lokale Entwicklung:**
  - Verwenden Sie [Minikube](https://minikube.sigs.k8s.io/docs/start/) oder [Docker Desktop](https://www.docker.com/products/docker-desktop), um einen Single-Node-Cluster auf Ihrem lokalen Rechner einzurichten.
  - Beispiel mit Minikube:
    ```bash
    minikube start
    ```

- **Für die Produktion:**
  - Verwenden Sie Managed Services wie Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS) oder Azure Kubernetes Service (AKS).
  - Alternativ können Sie einen Cluster manuell mit [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) einrichten.
  - Beispiel mit einem Managed Service (z.B. GKE):
    ```bash
    gcloud container clusters create my-cluster
    ```

---

### 2. **Erstellen eines Docker-Images Ihrer Anwendung**
Kubernetes verwaltet containerisierte Anwendungen, typischerweise unter Verwendung von Docker-Containern.

- Schreiben Sie eine `Dockerfile`, um die Umgebung Ihrer Anwendung zu definieren. Beispiel:
  ```dockerfile
  FROM node:16
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

- Bauen Sie das Docker-Image:
  ```bash
  docker build -t your-image-name:latest .
  ```

- Pushen Sie das Image in eine Container Registry (z.B. Docker Hub):
  ```bash
  docker push your-image-name:latest
  ```

---

### 3. **Definieren von Kubernetes-Objekten**
Kubernetes verwendet YAML-Dateien, um Ressourcen wie Pods, Services und Deployments zu definieren.

- **Pod:** Die kleinste bereitstellbare Einheit, die einen oder mehrere Container enthält.
- **Service:** Macht Ihre Anwendung im Netzwerk verfügbar.
- **Deployment:** Verwaltet Pods, stellt die gewünschte Anzahl laufender Instanzen sicher und behandelt Updates.

Beispiel einer `Deployment`-YAML-Datei (`my-app-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # Anzahl der Pod-Instanzen
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

### 4. **Bereitstellen der Anwendung**
Verwenden Sie das Kommandozeilen-Tool `kubectl`, um mit Ihrem Cluster zu interagieren und Ihre Anwendung bereitzustellen.

- Wenden Sie die YAML-Datei auf den Cluster an:
  ```bash
  kubectl apply -f my-app-deployment.yaml
  ```

- Überprüfen Sie die Bereitstellung:
  ```bash
  kubectl get deployments
  kubectl get pods
  ```

---

### 5. **Verwalten der Anwendung**
`kubectl` bietet Befehle zum Überwachen und Verwalten Ihrer Anwendung:

- **Anwendung skalieren:**
  ```bash
  kubectl scale deployment my-app --replicas=5
  ```

- **Pod-Status überprüfen:**
  ```bash
  kubectl get pods
  ```

- **Logs anzeigen:**
  ```bash
  kubectl logs <pod-name>
  ```

- **Auf einen Container zugreifen:**
  ```bash
  kubectl exec -it <pod-name> -- /bin/bash
  ```

---

### Wichtige Konzepte für die weitere Erkundung
- **Namespaces:** Organisieren Sie Ressourcen und verwalten Sie den Zugriff (z.B. `kubectl create namespace my-namespace`).
- **ConfigMaps:** Speichern Sie Konfigurationsdaten getrennt von der Anwendung.
- **Secrets:** Verwalten Sie sensible Informationen wie Passwörter.
- **Ingress:** Machen Sie Services extern über einen einzelnen Einstiegspunkt verfügbar.

---

### Tipps für den Einstieg
Kubernetes ist ein leistungsstarkes, aber komplexes System. Beginnen Sie mit diesen Grundlagen – Einrichten eines Clusters, Bereitstellen einer einfachen Anwendung und Nutzung von `kubectl` – und erkunden Sie dann fortgeschrittene Funktionen nach Bedarf. Für praktische Übungen probieren Sie Tutorials wie die [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) auf der offiziellen Website.

Mit diesem Fundament sind Sie in der Lage, Kubernetes effektiv zum Bereitstellen und Verwalten containerisierter Anwendungen zu nutzen!