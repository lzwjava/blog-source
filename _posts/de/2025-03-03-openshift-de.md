---
audio: false
generated: true
lang: de
layout: post
title: OpenShift-Leitfaden
translated: true
type: note
---

OpenShift ist eine leistungsstarke Plattform, die den Prozess des Erstellens, Bereitstellens und Verwaltens von Anwendungen in einer Cloud-Umgebung vereinfacht. Entwickelt von Red Hat, nutzt es die Fähigkeiten von Kubernetes, dem führenden Open-Source-Container-Orchestrierungssystem, um eine robuste und skalierbare Lösung für Entwickler und Organisationen gleichermaßen zu bieten. Egal, ob Sie ein Entwickler sind, der seinen Workflow optimieren möchte, oder ein Unternehmen, das eine zuverlässige Cloud-Plattform sucht – OpenShift bietet die Werkzeuge und Funktionen, um Ihre Anforderungen zu erfüllen.

In diesem Blogbeitrag werden wir untersuchen, was OpenShift ist, seine Hauptfunktionen, wie Sie damit beginnen und es effektiv nutzen können. Wir werden auch Best Practices und reale Anwendungsfälle behandeln, um Ihnen zu helfen, sein Potenzial zu verstehen. Fangen wir an!

---

## Einführung in OpenShift

OpenShift ist eine Platform-as-a-Service (PaaS), die darauf ausgelegt ist, die Anwendungsentwicklung und -bereitstellung nahtlos zu gestalten. Auf Kubernetes aufbauend, erweitert es die Kern-Orchestrierungsfähigkeiten um zusätzliche Werkzeuge, die für Enterprise-grade Container Management maßgeschneidert sind. OpenShift ermöglicht es Entwicklern, sich auf das Schreiben von Code zu konzentrieren, während es die Komplexitäten der Bereitstellung, Skalierung und Wartung automatisiert.

Die Plattform unterstützt eine breite Palette von Programmiersprachen, Frameworks und Datenbanken, was sie für verschiedene Anwendungstypen vielseitig einsetzbar macht. Sie bietet außerdem eine konsistente Umgebung über On-Premises-, Public- und Hybrid-Cloud-Infrastrukturen hinweg und bietet so Flexibilität und Skalierbarkeit für die moderne Softwareentwicklung.

---

## Hauptfunktionen von OpenShift

OpenShift zeichnet sich durch seinen reichen Funktionsumfang aus, der die Verwaltung containerisierter Anwendungen vereinfacht. Hier sind einige Highlights:

- **Container Management**: Angetrieben von Kubernetes automatisiert OpenShift die Bereitstellung, Skalierung und den Betrieb von Containern über Cluster hinweg.
- **Developer Tools**: Integrierte Tools für Continuous Integration und Continuous Deployment (CI/CD), wie z.B. Jenkins, optimieren die Entwicklungspipeline.
- **Multi-Language Support**: Erstellen Sie Anwendungen in Sprachen wie Java, Node.js, Python, Ruby und mehr, mit Ihren bevorzugten Frameworks.
- **Sicherheit**: Integrierte Funktionen wie rollenbasierte Zugriffskontrolle (RBAC), Netzwerkrichtlinien und Image-Scanning stellen sicher, dass Ihre Anwendungen sicher bleiben.
- **Skalierbarkeit**: Skalieren Sie Anwendungen horizontal (mehr Instanzen) oder vertikal (mehr Ressourcen), um die Nachfrage zu bedienen.
- **Monitoring und Logging**: Tools wie Prometheus, Grafana, Elasticsearch und Kibana bieten Einblicke in die Anwendungsleistung und Logs.

Diese Funktionen machen OpenShift zu einer All-in-One-Lösung für die Verwaltung des gesamten Anwendungslebenszyklus, von der Entwicklung bis zur Produktion.

---

## Erste Schritte mit OpenShift

Die ersten Schritte mit OpenShift sind unkompliziert. Befolgen Sie diese Schritte, um Ihre Umgebung einzurichten und Ihre erste Anwendung bereitzustellen.

### Schritt 1: Für OpenShift anmelden oder es installieren
- **Cloud-Option**: Melden Sie sich für einen kostenlosen Account auf [Red Hat OpenShift Online](https://www.openshift.com/products/online/) an, um OpenShift in der Cloud zu nutzen.
- **Lokale Option**: Installieren Sie [Minishift](https://docs.okd.io/latest/minishift/getting-started/installing.html), um einen Single-Node-OpenShift-Cluster lokal für die Entwicklung auszuführen.

### Schritt 2: Die OpenShift-CLI installieren
Die OpenShift Command Line Interface (CLI), bekannt als `oc`, ermöglicht es Ihnen, mit der Plattform von Ihrem Terminal aus zu interagieren. Laden Sie sie von der [offiziellen OpenShift-CLI-Seite](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html) herunter und befolgen Sie die Installationsanweisungen für Ihr Betriebssystem.

### Schritt 3: Anmelden und ein Projekt erstellen
- Melden Sie sich bei Ihrem OpenShift-Cluster über die CLI an:
  ```bash
  oc login <cluster-url> --token=<your-token>
  ```
  Ersetzen Sie `<cluster-url>` und `<your-token>` durch die Details Ihrer OpenShift-Instanz.
- Erstellen Sie ein neues Projekt, um Ihre Anwendungen zu organisieren:
  ```bash
  oc new-project my-first-project
  ```

### Schritt 4: Eine Anwendung bereitstellen
Stellen Sie eine Beispielanwendung, wie z.B. eine Node.js-App, mit dem Befehl `oc new-app` bereit:
```bash
oc new-app nodejs~https://github.com/sclorg/nodejs-ex.git
```
Dies nutzt die Source-to-Image (S2I)-Funktion von OpenShift, um die App direkt aus dem Git-Repository zu bauen und bereitzustellen.

### Schritt 5: Die Anwendung verfügbar machen
Machen Sie Ihre Anwendung über eine URL zugänglich, indem Sie eine Route erstellen:
```bash
oc expose svc/nodejs-ex
```
Führen Sie `oc get route` aus, um die URL zu finden, und rufen Sie sie in Ihrem Browser auf, um Ihre Live-App zu sehen!

---

## OpenShift nutzen: Ein tieferer Einblick

Sobald Sie OpenShift eingerichtet haben, können Sie seine Funktionen nutzen, um Anwendungen effektiv zu verwalten. Hier erfahren Sie, wie Sie einige seiner Kernfunktionalitäten verwenden.

### Anwendungen bereitstellen
OpenShift bietet Flexibilität bei der Bereitstellung von Apps:
- **Source-to-Image (S2I)**: Baut und stellt automatisch aus Quellcode bereit. Zum Beispiel:
  ```bash
  oc new-app python~https://github.com/example/python-app.git
  ```
- **Docker Images**: Stellen vorgebaute Images bereit:
  ```bash
  oc new-app my-image:latest
  ```
- **Templates**: Stellen gängige Dienste wie MySQL bereit:
  ```bash
  oc new-app --template=mysql-persistent
  ```

### Container verwalten
Verwenden Sie die CLI oder die Web-Konsole, um Container-Lebenszyklen zu verwalten:
- **Build starten**: `oc start-build <buildconfig>`
- **App skalieren**: `oc scale --replicas=3 dc/<deploymentconfig>`
- **Logs anzeigen**: `oc logs <pod-name>`

### Anwendungen skalieren
Passen Sie die Kapazität Ihrer App leicht an. Um auf drei Instanzen zu skalieren:
```bash
oc scale --replicas=3 dc/my-app
```
OpenShift übernimmt automatisch den Lastausgleich über diese Replikate.

### Monitoring und Logging
Behalten Sie den Überblick über Ihre App mit integrierten Tools:
- **Prometheus**: Überwacht Metriken wie CPU- und Speichernutzung.
- **Grafana**: Visualisiert Leistungsdaten.
- **Elasticsearch und Kibana**: Zentralisieren und analysieren Logs.
Greifen Sie über die OpenShift-Web-Konsole in Echtzeit auf diese zu.

---

## Best Practices für die Nutzung von OpenShift

Um das Potenzial von OpenShift voll auszuschöpfen, befolgen Sie diese Best Practices:

- **Automatisieren mit CI/CD**: Nutzen Sie den integrierten Jenkins von OpenShift oder integrieren Sie Ihre bevorzugten CI/CD-Tools, um Workflows zu optimieren.
- **Standardisieren mit Templates**: Erstellen Sie wiederverwendbare Templates für konsistente Bereitstellungen.
- **Sicherheit priorisieren**: Implementieren Sie RBAC, scannen Sie Images auf Schwachstellen und verwenden Sie Netzwerkrichtlinien.
- **Ressourcen optimieren**: Überwachen Sie die Nutzung mit Prometheus und passen Sie Ressourcenlimits an, um Leistung und Kosten auszugleichen.
- **Mit Labels organisieren**: Versehen Sie Ressourcen mit Labels (z.B. `app=my-app`) für eine einfachere Verwaltung.

Diese Praktiken stellen sicher, dass Ihre Anwendungen sicher, effizient und skalierbar sind.

---

## Anwendungsfälle für OpenShift

OpenShift glänzt in einer Vielzahl von Szenarien:
- **Microservices**: Verwalten und skalieren Sie Microservices mit integriertem Service Discovery und Lastausgleich.
- **DevOps**: Überbrücken Sie Entwicklung und Betrieb mit CI/CD und Automatisierungstools.
- **Hybrid Cloud**: Stellen Sie Apps nahtlos über On-Premises- und Cloud-Umgebungen hinweg bereit.
- **Modernisierung von Legacy-Systemen**: Containerisieren Sie ältere Anwendungen für verbesserte Portabilität und Skalierbarkeit.

Diese Anwendungsfälle unterstreichen die Vielseitigkeit von OpenShift in der modernen Softwareentwicklung.

---

## Fazit

OpenShift ist ein Game-Changer für Entwickler und Organisationen, die die Anwendungsentwicklung und -verwaltung vereinfachen möchten. Mit seinem Kubernetes-Fundament, seinem robusten Funktionsumfang und seiner Unterstützung für diverse Workflows befähigt es Sie, Anwendungen mühelos zu erstellen, bereitzustellen und zu skalieren. Egal, ob Sie mit einem lokalen Minishift-Setup experimentieren oder Produktions-Workloads in der Cloud ausführen – OpenShift hat die passende Lösung.

Bereit zu beginnen? Erkunden Sie die [offizielle OpenShift-Dokumentation](https://docs.openshift.com/) oder stellen Sie Ihre erste App mit den oben beschriebenen Schritten bereit. Mit OpenShift ist der Weg vom Code zur Produktion reibungsloser denn je!