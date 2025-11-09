---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: OpenAI-Infrastruktur und Azure-Abhängigkeit
translated: true
type: note
---

### Überblick über den Tech Stack von OpenAI

Die Infrastruktur von OpenAI ist stark für groß angelegte KI-Forschung, Training und Deployment optimiert und legt den Schwerpunkt auf Skalierbarkeit, Sicherheit und schnelles Experimentieren. Seit dem Wechsel von AWS Anfang 2017 wurde ein Großteil der Infrastruktur auf Basis von Microsoft Azure aufgebaut, das die grundlegende Cloud-Plattform für ihre Supercomputer und Workloads bereitstellt. Dieser Wechsel ermöglichte eine bessere Integration mit spezialisierter Hardware und Kosteneffizienz. Wichtige Elemente sind ein einheitliches Python-Monorepo für die Entwicklung, Kubernetes für die Orchestrierung und Streaming-Tools wie Apache Kafka. Im Folgenden werde ich die Infrastruktur nach Kategorien aufschlüsseln und dabei auf die Azure-Abhängigkeit und die Kubernetes-Spezifika eingehen.

#### Cloud-Infrastruktur: Starke Azure-Abhängigkeit
OpenAI nutzt Azure intensiv für seine Forschungs- und Produktionsumgebungen, einschließlich des Trainings von Frontier-Modellen wie der GPT-Serie. Dazu gehören:
- **Azure als Kernplattform**: Alle wichtigen Workloads laufen auf Azure, mit privat verknüpftem Speicher für sensible Daten (z.B. Modellgewichte), um die Internet-Exposition zu minimieren. Die Authentifizierung ist in Azure Entra ID für Identity Management integriert, was risikobasierte Zugriffskontrollen und Anomalieerkennung ermöglicht.
- **Warum so viel Azure?**: Ein durchgesickertes internes Dokument (vermutlich bezugnehmend auf ihren Sicherheitsarchitektur-Post von 2024) unterstreicht die Rolle von Azure beim Schutz geistigen Eigentums während des Trainings. Es unterstützt massive GPU-Cluster für KI-Experimente in den Bereichen Robotik, Gaming und mehr. Die Partnerschaft von OpenAI mit Microsoft gewährleistet niedrige Latenzzeiten für den Zugriff auf Modelle über den Azure OpenAI Service, aber intern ist Azure das Rückgrat für das benutzerdefinierte Supercomputing. Sie nutzen auch Hybridlösungen mit On-Premise-Rechenzentren für GPU-intensive Aufgaben und verwalten Control Planes (z.B. etcd) in Azure für Zuverlässigkeit und Backups.

Diese tiefe Integration bedeutet, dass der Stack von OpenAI nicht einfach portierbar ist – er ist auf die Leistung und Compliance von Azures Ökosystem zugeschnitten.

#### Orchestrierung und Skalierung: Kubernetes (AKS) mit Azure-Optimierungen
Kubernetes ist zentral für das Workload-Management, behandelt Batch-Scheduling, Container-Orchestrierung und Portabilität über Cluster hinweg. OpenAI führt Experimente auf Azure Kubernetes Service (AKS) durch und skaliert in den letzten Jahren auf über 7.500 Nodes (gegenüber 2.500 im Jahr 2017).
- **AKS-Zuverlässigkeit in Azures Ökosystem**: Wie Sie anmerkten, glänzt der Kubernetes-Dienst von Azure, wenn er vollständig in Azure-Produkte eingebettet ist. OpenAI wechselte zu Azure CNI (Container Network Interface) für das Networking, das speziell für Azures Cloud entwickelt wurde und hochperformante, großskalige Umgebungen handhabt, mit denen generische CNIs wie Flannel bei dieser Größe nicht zuverlässig mithalten können. Dies ermöglicht dynamische Skalierung ohne Engpässe, automatische Pod-Health-Checks und Failover während Ausfällen. Ohne die nativen Integrationen von Azure (z.B. für Blob Storage und Workload Identity) sinkt die Zuverlässigkeit aufgrund von Latenz, Authentifizierungsproblemen oder Kapazitätsengpässen. Ihr benutzerdefinierter Autoscaler fügt dynamisch Nodes hinzu oder entfernt sie, senkt so die Kosten für ungenutzte Ressourcen und ermöglicht gleichzeitig eine 10-fache Skalierung von Experimenten innerhalb von Tagen.
- **Sicherheitsebene**: Kubernetes erzwingt RBAC für Least-Privilege-Zugriff, Admission Controller für Container-Richtlinien und standardmäßig verweigerte Netzwerk-Ausgänge (mit Allowlists für genehmigte Pfade). Für Hochrisiko-Jobs setzen sie zusätzlich gVisor für eine extra Isolierung ein. Multi-Cluster-Failover hält Jobs während regionaler Probleme am Laufen.

#### Entwicklung und Code-Management: Monorepo-Ansatz
OpenAI pflegt ein einziges Python-Monorepo für die meisten Forschungs- und Entwicklungsarbeiten. Dies zentralisiert Code, Bibliotheken und Abhängigkeiten und ermöglicht es Teams, vertraute Python-Tools (z.B. NumPy, PyTorch) neben KI-spezifischen Pipelines zu verwenden. Es integriert sich nahtlos in ihre Stream-Verarbeitung und verringert so die Reibungspunkte für Experimente. CI/CD-Pipelines sind mit Multi-Party-Genehmigungen und IaC (Infrastructure as Code) für konsistente Deployments abgesichert.

#### Datenverarbeitung und Streaming
- **Apache Kafka**: Das Event-Backbone für Logs, Trainingsdaten und Ergebnisse. Es ist multi-primary für hohe Verfügbarkeit, mit benutzerdefinierten Connectoren (z.B. Union Streams zum Lesen, Prism Sink zum Schreiben) und Watchdogs, um sich an Topologieänderungen wie Failover anzupassen.
- **PyFlink auf Kubernetes**: Für GenAI-Stream-Verarbeitung, unter Verwendung des Flink Kubernetes Operators für Automatisierung. Es unterstützt DataStream/Table-APIs in Python, mit RocksDB für State und Azure Blob Storage für Checkpoints – gesichert über Workload Identity (keine langlebigen Schlüssel).

#### Monitoring und Kommunikation
- **Prometheus**: Für Debugging und Metriken.
- **gRPC**: Für die Kommunikation zwischen Diensten.

#### Entwicklung im Jahr 2025
Aktuelle Updates (z.B. vom OpenAI DevDay 2025) konzentrieren sich mehr auf Modell-APIs und Agent-Tools wie AgentKit, aber der Infrastruktur-Stack bleibt Azure-Kubernetes-zentriert. Sie haben Tools wie ihren Autoscaler open-source veröffentlicht, um Erkenntnisse zu teilen.

Dieser Stack priorisiert eine "Data Flywheel" für schnellere Iteration, opfert jedoch Portabilität für Azures Zuverlässigkeit im Hyperscale-Bereich. Wenn Sie etwas Ähnliches aufbauen, könnte der Start mit AKS + Kafka dies nachahmen, aber außerhalb von Azure sind Anpassungen zu erwarten.

[How OpenAI Uses Kubernetes And Apache Kafka for GenAI](https://blog.bytebytego.com/p/how-openai-uses-kubernetes-and-apache)  
[Securing Research Infrastructure for Advanced AI](https://openai.com/index/securing-research-infrastructure-for-advanced-ai/)  
[OpenAI Kubernetes Case Study](https://kubernetes.io/case-studies/openai/)  
[How OpenAI Scaled Kubernetes with Azure CNI](https://medium.com/@PlanB./how-openai-scaled-kubernetes-with-azure-cni-to-handle-7-500-nodes-591162d0efa5)