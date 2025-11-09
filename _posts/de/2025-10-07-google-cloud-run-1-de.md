---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Google Cloud Run Überblick
translated: true
type: note
---

### Was ist Google Cloud Run?

Google Cloud Run ist eine vollständig verwaltete, serverlose Plattform auf der Google Cloud Platform (GCP), die für das Ausführen containerisierter Anwendungen konzipiert ist. Sie ermöglicht es Entwicklern, Code bereitzustellen und zu skalieren, ohne sich um die zugrunde liegende Infrastruktur kümmern zu müssen, da sie die Bereitstellung, Skalierung und Wartung automatisch handhabt. Sie unterstützt zustandslose HTTP/HTTPS-Anfragen, ereignisgesteuerte Workloads und skaliert auf null Instanzen herunter, wenn sie im Leerlauf ist, was sie sehr kosteneffizient macht.

### Wichtige Funktionen und Eigenschaften
- **Container-basierte Bereitstellung**: Führen Sie jede Sprache oder jedes Framework in einem Standard-Container (z.B. Docker) aus, mit integrierter Unterstützung für HTTP/gRPC-Dienste, Hintergrundjobs und asynchrone Verarbeitung.
- **Automatische Skalierung und Bezahlung nach Nutzung**: Skaliert von null auf Tausende von Instanzen basierend auf dem Datenverkehr; Sie zahlen nur für die tatsächliche Nutzung (CPU, Arbeitsspeicher und Anfragen).
- **Integrationen**: Funktioniert nahtlos mit anderen GCP-Diensten wie Cloud Build (für CI/CD), Cloud SQL (Datenbanken), Pub/Sub (Messaging), Artifact Registry (Container-Speicher) und AI-Tools für GPU-beschleunigte Aufgaben.
- **Sicherheit und Netzwerke**: Integrierte Authentifizierung (IAM), VPC-Konnektivität und Binary Authorization für sichere Bereitstellungen.
- **Free Tier**: Bis zu 2 Millionen Anfragen pro Monat kostenlos.

### Typische Anwendungsszenarien
Cloud Run ist ideal für moderne, ereignisgesteuerte Anwendungen, bei denen Flexibilität und geringer Overhead entscheidend sind. Häufige Beispiele sind:
- **Webanwendungen und APIs**: Hosten von zustandslosen Microservices, RESTful APIs oder vollständigen Web-Apps (z.B. ein Node.js-Backend, das dynamische Inhalte aus einer Datenbank bereitstellt). Es glänzt bei E-Commerce-Webseiten oder Mobile-Backends, die variablen Datenverkehr verarbeiten.
- **Batch-Jobs und Datenverarbeitung**: Ausführen von geplanten Aufgaben wie ETL-Pipelines (Extract, Transform, Load) oder Bild-/Video-Verarbeitungs-Warteschlangen, die durch Cloud Scheduler oder Pub/Sub ausgelöst werden.
- **AI/ML-Workloads**: Hosten von Large Language Models (LLMs) wie Llama 3.1 oder Gemma 2 für Echtzeit-Inferenz, z.B. für Chatbots, Bilderkennung oder Videotranskodierung. Die GPU-Unterstützung macht es für rechenintensive Aufgaben geeignet.
- **Serverless-Migrationen**: Der Wechsel von VMs oder Kubernetes (z.B. über Knative), um Kosten zu senken – Unternehmen wie die Telegraph Media Group berichteten von 90 % Einsparungen bei Kosten und Kohlenstoffemissionen nach der Migration.

Im Wesentlichen ist es ideal für Entwickler, die Kubernetes-ähnliche Leistung ohne den operativen Aufwand wünschen, besonders für burstartige oder unvorhersehbare Workloads.

[Cloud Run-Dokumentation](https://cloud.google.com/run)