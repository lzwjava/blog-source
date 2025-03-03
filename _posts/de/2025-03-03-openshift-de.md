---
audio: true
generated: true
lang: de
layout: post
title: OpenShift Leitfaden
translated: true
---

OpenShift ist eine leistungsstarke Plattform, die den Prozess des Bauens, Bereitstellens und Verwalten von Anwendungen in einer Cloud-Umgebung vereinfacht. Entwickelt von Red Hat, nutzt es die Fähigkeiten von Kubernetes, dem führenden Open-Source-Container-Orchestrierungssystem, um eine robuste und skalierbare Lösung für Entwickler und Organisationen gleichermaßen zu bieten. Ob Sie ein Entwickler sind, der Ihren Workflow optimieren möchte, oder ein Unternehmen, das nach einer zuverlässigen Cloud-Plattform sucht, OpenShift bietet die Tools und Funktionen, um Ihre Bedürfnisse zu erfüllen.

In diesem Blogbeitrag werden wir erkunden, was OpenShift ist, seine wichtigsten Funktionen, wie man beginnt und wie man es effektiv nutzt. Wir werden auch Best Practices und reale Anwendungsfälle behandeln, um Ihnen zu helfen, sein Potenzial zu verstehen. Lassen Sie uns eintauchen!

---

## Einführung in OpenShift

OpenShift ist eine Plattform-as-a-Service (PaaS), die entwickelt wurde, um die Anwendungsentwicklung und -bereitstellung nahtlos zu gestalten. Auf Kubernetes aufgebaut, erweitert es die Kernorchestrierungsfähigkeiten mit zusätzlichen Tools, die für die unternehmensgerechte Containerverwaltung zugeschnitten sind. OpenShift ermöglicht es Entwicklern, sich auf das Schreiben von Code zu konzentrieren, während die Komplexitäten der Bereitstellung, Skalierung und Wartung automatisiert werden.

Die Plattform unterstützt eine breite Palette von Programmiersprachen, Frameworks und Datenbanken, was sie vielseitig für verschiedene Anwendungstypen macht. Sie bietet auch eine konsistente Umgebung über On-Premises-, Public- und Hybrid-Cloud-Infrastrukturen hinweg, was Flexibilität und Skalierbarkeit für die moderne Softwareentwicklung bietet.

---

## Wichtige Funktionen von OpenShift

OpenShift hebt sich durch seinen reichen Satz an Funktionen hervor, die die Verwaltung von containerisierten Anwendungen vereinfachen. Hier sind einige Highlights:

- **Containerverwaltung**: Mit Kubernetes angetrieben, automatisiert OpenShift die Bereitstellung, Skalierung und den Betrieb von Containern über Cluster hinweg.
- **Entwicklertools**: Integrierte Tools für kontinuierliche Integration und kontinuierliche Bereitstellung (CI/CD), wie Jenkins, optimieren die Entwicklungs-Pipeline.
- **Mehrsprachige Unterstützung**: Entwickeln Sie Anwendungen in Sprachen wie Java, Node.js, Python, Ruby und mehr, unter Verwendung Ihrer bevorzugten Frameworks.
- **Sicherheit**: Integrierte Funktionen wie rollenbasierte Zugriffskontrolle (RBAC), Netzwerkrichtlinien und Bildscans stellen sicher, dass Ihre Anwendungen sicher bleiben.
- **Skalierbarkeit**: Skalieren Sie Anwendungen horizontal (mehr Instanzen) oder vertikal (mehr Ressourcen), um der Nachfrage gerecht zu werden.
- **Überwachung und Protokollierung**: Tools wie Prometheus, Grafana, Elasticsearch und Kibana bieten Einblicke in die Anwendungsleistung und Protokolle.

Diese Funktionen machen OpenShift zu einer All-in-One-Lösung für die Verwaltung des gesamten Anwendungslebenszyklus, von der Entwicklung bis zur Produktion.

---

## So beginnen Sie mit OpenShift

Mit OpenShift zu beginnen, ist einfach. Folgen Sie diesen Schritten, um Ihre Umgebung einzurichten und Ihre erste Anwendung zu bereitzustellen.

### Schritt 1: Registrieren oder OpenShift installieren
- **Cloud-Option**: Registrieren Sie sich für ein kostenloses Konto auf [Red Hat OpenShift Online](https://www.openshift.com/products/online/), um OpenShift in der Cloud zu nutzen.
- **Lokale Option**: Installieren Sie [Minishift](https://docs.okd.io/latest/minishift/getting-started/installing.html), um einen Single-Node-OpenShift-Cluster lokal für die Entwicklung auszuführen.

### Schritt 2: Installieren Sie die OpenShift-Befehlszeilenschnittstelle
Die OpenShift Command Line Interface (CLI), bekannt als `oc`, ermöglicht Ihnen die Interaktion mit der Plattform von Ihrem Terminal aus. Laden Sie es von der [offiziellen OpenShift CLI-Seite](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html) herunter und befolgen Sie die Installationsanweisungen für Ihr Betriebssystem.

### Schritt 3: Anmelden und Projekt erstellen
- Melden Sie sich bei Ihrem OpenShift-Cluster mit der CLI an:
  ```bash
  oc login <cluster-url> --token=<your-token>
  ```
  Ersetzen Sie `<cluster-url>` und `<your-token>` durch die Details, die von Ihrer OpenShift-Instanz bereitgestellt werden.
- Erstellen Sie ein neues Projekt, um Ihre Anwendungen zu organisieren:
  ```bash
  oc new-project my-first-project
  ```

### Schritt 4: Anwendung bereitstellen
Stellen Sie eine Beispielanwendung, wie eine Node.js-App, mit dem Befehl `oc new-app` bereit:
```bash
oc new-app nodejs~https://github.com/sclorg/nodejs-ex.git
```
Dies nutzt die Source-to-Image (S2I)-Funktion von OpenShift, um die App direkt aus dem Git-Repository zu erstellen und bereitzustellen.

### Schritt 5: Anwendung freigeben
Machen Sie Ihre Anwendung über eine URL zugänglich, indem Sie eine Route erstellen:
```bash
oc expose svc/nodejs-ex
```
Führen Sie `oc get route` aus, um die URL zu finden, und besuchen Sie sie in Ihrem Browser, um Ihre App live zu sehen!

---

## OpenShift: Ein tieferer Einblick

Sobald Sie OpenShift eingerichtet haben, können Sie seine Funktionen nutzen, um Anwendungen effektiv zu verwalten. Hier ist, wie Sie einige seiner Kernfunktionen nutzen können.

### Anwendungen bereitstellen
OpenShift bietet Flexibilität bei der Bereitstellung von Apps:
- **Source-to-Image (S2I)**: Baut und stellt automatisch aus dem Quellcode bereit. Zum Beispiel:
  ```bash
  oc new-app python~https://github.com/example/python-app.git
  ```
- **Docker-Bilder**: Stellen Sie vorgebaute Bilder bereit:
  ```bash
  oc new-app my-image:latest
  ```
- **Vorlagen**: Stellen Sie gemeinsame Dienste wie MySQL bereit:
  ```bash
  oc new-app --template=mysql-persistent
  ```

### Container verwalten
Verwenden Sie die CLI oder die Webkonsole, um den Lebenszyklus von Containern zu verwalten:
- **Build starten**: `oc start-build <buildconfig>`
- **App skalieren**: `oc scale --replicas=3 dc/<deploymentconfig>`
- **Protokolle anzeigen**: `oc logs <pod-name>`

### Anwendungen skalieren
Passen Sie die Kapazität Ihrer App einfach an. Um auf drei Instanzen zu skalieren:
```bash
oc scale --replicas=3 dc/my-app
```
OpenShift übernimmt das Lastausgleich über diese Replikate automatisch.

### Überwachung und Protokollierung
Behalten Sie Ihre App mit integrierten Tools im Auge:
- **Prometheus**: Überwacht Metriken wie CPU- und Speichernutzung.
- **Grafana**: Visualisiert Leistungsdaten.
- **Elasticsearch und Kibana**: Zentralisieren und analysieren Sie Protokolle.
Greifen Sie über die OpenShift-Webkonsole auf diese für Echtzeiteinblicke zu.

---

## Best Practices für die Nutzung von OpenShift

Um das Potenzial von OpenShift voll auszuschöpfen, befolgen Sie diese Best Practices:

- **Automatisieren Sie mit CI/CD**: Nutzen Sie das eingebaute Jenkins von OpenShift oder integrieren Sie Ihre bevorzugten CI/CD-Tools, um Workflows zu optimieren.
- **Standardisieren Sie mit Vorlagen**: Erstellen Sie wiederverwendbare Vorlagen für konsistente Bereitstellungen.
- **Sicherheit priorisieren**: Implementieren Sie RBAC, scannen Sie Bilder auf Schwachstellen und verwenden Sie Netzwerkrichtlinien.
- **Ressourcen optimieren**: Überwachen Sie die Nutzung mit Prometheus und passen Sie die Ressourcengrenzen an, um Leistung und Kosten auszugleichen.
- **Organisieren Sie mit Labels**: Markieren Sie Ressourcen mit Labels (z. B. `app=my-app`) für eine einfachere Verwaltung.

Diese Praktiken stellen sicher, dass Ihre Anwendungen sicher, effizient und skalierbar sind.

---

## Anwendungsfälle für OpenShift

OpenShift glänzt in einer Vielzahl von Szenarien:
- **Microservices**: Verwalten und skalieren Sie Microservices mit eingebauter Dienstentdeckung und Lastausgleich.
- **DevOps**: Brücken Sie Entwicklung und Betrieb mit CI/CD- und Automatisierungstools.
- **Hybrid Cloud**: Stellen Sie Apps nahtlos über On-Premises- und Cloud-Umgebungen bereit.
- **Legacy Modernisierung**: Containerisieren Sie ältere Anwendungen für verbesserte Portabilität und Skalierbarkeit.

Diese Anwendungsfälle unterstreichen die Vielseitigkeit von OpenShift in der modernen Softwareentwicklung.

---

## Fazit

OpenShift ist ein Game-Changer für Entwickler und Organisationen, die die Anwendungsentwicklung und -verwaltung vereinfachen möchten. Mit seiner Kubernetes-Grundlage, einem robusten Funktionssatz und der Unterstützung für vielfältige Workflows ermöglicht es Ihnen, Anwendungen einfach zu erstellen, bereitzustellen und zu skalieren. Ob Sie mit einer lokalen Minishift-Einrichtung experimentieren oder Produktionsaufgaben in der Cloud ausführen, OpenShift hat Sie abgedeckt.

Bereit, loszulegen? Erkunden Sie die [offizielle OpenShift-Dokumentation](https://docs.openshift.com/) oder stellen Sie Ihre erste App mit den obigen Schritten bereit. Mit OpenShift ist die Reise vom Code zur Produktion glatter denn je!