---
audio: false
generated: true
lang: de
layout: post
title: Docker vs. Kubernetes
translated: true
type: note
---

Docker und Kubernetes sind komplementäre Technologien im Container-Ökosystem, erfüllen jedoch unterschiedliche Zwecke. Lassen Sie uns ihre Unterschiede und ihre Beziehung zueinander aufschlüsseln.

---

### Docker: Containerisierungsplattform
**Was es tut**: Docker ist ein Tool zum Erstellen, Ausführen und Verwalten einzelner Container – leichtgewichtige, isolierte Umgebungen, die eine Anwendung mit ihren Abhängigkeiten verpacken.

#### Hauptmerkmale
1. **Container-Runtime**:
   - Docker verwendet eine Runtime (z.B. `containerd` oder `runc`), um Container basierend auf Linux-Kernel-Funktionen wie Namespaces und Cgroups auszuführen.
   - Sie ist für den Lebenszyklus eines einzelnen Containers verantwortlich: Bauen, Starten, Stoppen usw.

2. **Image-Management**:
   - Docker erstellt Images aus einem `Dockerfile`, das die App, Bibliotheken und Konfigurationen definiert.
   - Images werden in Registries (z.B. Docker Hub) gespeichert und als Container ausgeführt.

3. **Single-Host-Fokus**:
   - Docker ist hervorragend darin, Container auf einem einzelnen Rechner zu verwalten. Sie können mehrere Container ausführen, aber die Orchestrierung über mehrere Hosts hinweg ist nicht eingebaut.

4. **CLI-gesteuert**:
   - Befehle wie `docker build`, `docker run` und `docker ps` ermöglichen die direkte Interaktion mit Containern.

#### Anwendungsfall
- Ausführung einer einzelnen Spring Boot App auf Ihrem Laptop oder einem Server:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```

#### Einschränkungen
- Keine native Multi-Host-Unterstützung.
- Keine automatische Skalierung, Selbstheilung oder Lastverteilung.
- Die manuelle Verwaltung vieler Container wird unübersichtlich.

---

### Kubernetes: Container-Orchestrierungssystem
**Was es tut**: Kubernetes (oft als K8s abgekürzt) ist eine Plattform zur Verwaltung und Orchestrierung mehrerer Container über einen Cluster von Maschinen hinweg. Es automatisiert die Bereitstellung, Skalierung und den Betrieb von containerisierten Anwendungen.

#### Hauptmerkmale
1. **Cluster-Management**:
   - Kubernetes läuft auf einem Cluster von Knoten (physischen oder virtuellen Maschinen). Ein Knoten ist die "Control Plane" (verwaltet den Cluster), die anderen sind "Worker Nodes" (führen Container aus).

2. **Orchestrierung**:
   - **Scheduling**: Entscheidet, welcher Knoten welchen Container basierend auf Ressourcen und Einschränkungen ausführt.
   - **Skalierung**: Erhöht oder verringert automatisch die Anzahl der Container-Instanzen (z.B. basierend auf CPU-Auslastung).
   - **Selbstheilung**: Startet fehlgeschlagene Container neu, plant sie neu ein, wenn ein Knoten ausfällt, und stellt sicher, dass der gewünschte Zustand erhalten bleibt.
   - **Lastverteilung**: Verteilt den Datenverkehr auf mehrere Container-Instanzen.

3. **Abstraktionsschicht**:
   - Verwendet "Pods" als kleinste Einheit – ein Pod kann einen oder mehrere Container enthalten (normalerweise einen), die sich Speicher- und Netzwerkressourcen teilen.
   - Wird über deklarative YAML-Dateien verwaltet (z.B. Definition von Deployments, Services).

4. **Multi-Host-Fokus**:
   - Entwickelt für verteilte Systeme, koordiniert Container über viele Maschinen hinweg.

5. **Ökosystem**:
   - Enthält Funktionen wie Service Discovery, persistenten Speicher, Secrets Management und Rolling Updates.

#### Anwendungsfall
- Bereitstellung einer Microservices-App mit 10 Diensten, jeder in seinem eigenen Container, verteilt über 5 Server, mit automatischer Skalierung und Failover:
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

#### Einschränkungen
- Steilere Lernkurve.
- Overkill für einfache, Single-Container-Apps auf einer Maschine.

---

### Hauptunterschiede

| Aspekt                | Docker                              | Kubernetes                          |
|-----------------------|-------------------------------------|-------------------------------------|
| **Zweck**             | Container-Erstellung und Runtime    | Container-Orchestrierung            |
| **Umfang**            | Einzelner Host                      | Cluster von Hosts                   |
| **Einheit**           | Container                           | Pod (Gruppe von 1+ Containern)      |
| **Skalierung**        | Manuell (z.B. `docker run` mehrmals) | Automatisch (via Replicas)          |
| **Netzwerke**         | Einfach (Bridge, Host, Overlay)     | Erweitert (Services, Ingress)       |
| **Selbstheilung**     | Keine (manueller Neustart)          | Eingebaut (Neustarts, Neuscheduling)|
| **Verwaltung**        | CLI oder Docker Compose für kleine Setups | YAML-Konfigs, `kubectl` CLI         |
| **Abhängigkeiten**    | Standalone (benötigt Docker Engine) | Benötigt eine Container-Runtime (z.B. Docker) |

---

### Wie sie zusammenarbeiten
- **Docker als Runtime**: Kubernetes führt Container nicht direkt aus – es verlässt sich auf eine Container-Runtime wie Docker (oder Alternativen wie `containerd`), um einzelne Container innerhalb von Pods zu starten und zu verwalten.
- **Workflow**:
  1. Sie bauen ein Docker-Image (`docker build -t myapp:latest .`).
  2. Sie schieben es in eine Registry (`docker push myapp:latest`).
  3. Kubernetes pullt das Image und deployt es im Cluster basierend auf Ihrer YAML-Konfiguration (`kubectl apply -f deployment.yaml`).

- **Beispiel**: Kubernetes könnte Docker verwenden, um drei Instanzen von `myapp:latest` auf verschiedenen Knoten auszuführen und sie über einen load-balanced Service verfügbar zu machen.

---

### Analogie
- **Docker**: Ein Koch, der ein einzelnes Gericht in einer Küche zubereitet. Sie sagen dem Koch, was er machen soll (`Dockerfile`) und wie er es servieren soll (`docker run`).
- **Kubernetes**: Ein Restaurantmanager, der mehrere Köche (Docker-Instanzen) in vielen Küchen (Knoten) überwacht. Der Manager stellt sicher, dass die Gerichte pünktlich zubereitet werden, bei starkem Andrang Personal aufstockt und einen kranken Koch ersetzt.

---

### Wann verwendet man was?
- **Nur Docker**: Für Entwicklung, Tests oder einfache Apps auf einer Maschine (z.B. eine einzelne Spring Boot App).
- **Kubernetes**: Für Produktionsreife, verteilte Anwendungen, die hohe Verfügbarkeit, Skalierung und Resilienz benötigen (z.B. eine Microservices-Architektur).

---

Klärt dies den Unterschied? Lassen Sie mich wissen, wenn Sie einen bestimmten Aspekt vertiefen möchten – wie die Einrichtung von Kubernetes oder ein Vergleich mit Docker Compose!