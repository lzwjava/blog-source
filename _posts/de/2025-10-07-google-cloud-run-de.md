---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einführung in Google Cloud Run
translated: true
type: note
---

Cloud Run ist eine vollständig verwaltete, serverlose Compute-Plattform in GCP, auf der Sie zustandslose Container direkt auf der skalierbaren Infrastruktur von Google ausführen können. Sie wurde für Entwickler konzipiert, die Anwendungen bereitstellen möchten, ohne sich um zugrunde liegende Server, Bereitstellung oder Skalierung kümmern zu müssen. Egal, ob Sie Web-Apps, APIs, Microservices oder ereignisgesteuerte Workloads erstellen – Cloud Run übernimmt die Infrastruktur, damit Sie sich auf den Code konzentrieren können.

### Wichtige Funktionen
- **Serverlose Ausführung**: Stellen Sie containerisierten Code bereit (unterstützt jede Sprache oder Laufzeitumgebung), der automatisch von null auf Tausende von Instanzen skaliert, basierend auf eingehenden Anfragen oder Traffic.
- **Pay-Per-Use-Preismodell**: Abrechnung nur für die tatsächlich verbrauchten Ressourcen – pro Anfrage oder pro Instanzdauer – was es für variable Workloads kosteneffizient macht.
- **Integrierte Integrationen**: Funktioniert nahtlos mit anderen GCP-Diensten wie Cloud SQL für Datenbanken, Cloud Storage für Dateien, Pub/Sub für Messaging und mehr. Unterstützt auch VPC für privates Networking.
- **Bereitstellungsoptionen**:
  - Übertragen Sie ein vorgebautes Container-Image aus der Artifact Registry oder Docker Hub.
  - Stellen Sie direkt aus dem Quellcode mit Cloud Build bereit (unterstützt Sprachen wie Node.js, Python, Java, Go, .NET und Ruby).
  - Verwenden Sie Cloud Run Functions für einfachere, Function-as-a-Service-artige Bereitstellungen.
- **Sicherheit und Networking**: Dienste können öffentlich oder privat (erfordert Authentifizierung) sein, mit Unterstützung für HTTPS-Endpunkte und benutzerdefinierte Domains.
- **Zusätzliche Modi**: Neben anfragegesteuerten Diensten bietet es Jobs für Batch-Aufgaben (z. B. geplante Skripte oder Datenverarbeitung) und Worker Pools für langlebige, nicht-HTTP-Workloads.

Um zu beginnen, können Sie über die GCP Console, die gcloud CLI oder CI/CD-Pipelines bereitstellen. Bauen und deployen Sie zum Beispiel in wenigen Minuten einen einfachen "Hello World"-Container.

### Die Cloud Run Admin Console
Der Cloud Run-Bereich in der GCP Console bietet ein intuitives Dashboard zur Verwaltung Ihrer Bereitstellungen. Hier ist eine Aufschlüsselung basierend auf der von Ihnen geteilten Service-Ansicht:

- **Übersicht**: Die Hauptseite "Cloud Run > Services" listet alle Ihre bereitgestellten Dienste in einem Tabellenformat auf. Sie beginnt mit einem hilfreichen Empfehlungsbanner wie "Run your app on a fully managed platform", um Neulinge zu schnellen Starts zu ermutigen.

- **Tabellenspalten** (wie in Ihrem Ausschnitt gezeigt):
  - **Name**: Der eindeutige Bezeichner für jeden Dienst (z. B. "my-api").
  - **Bereitstellungstyp**: Zeigt an, wie er bereitgestellt wurde – z. B. "Container" für Images oder "Source" für codebasierte Bereitstellungen.
  - **Anfr./Sek.**: Metrik für Anfragen pro Sekunde in Echtzeit zur Überwachung der Verkehrslast.
  - **Region**: Die GCP-Region, in der der Dienst läuft (z. B. us-central1), was Latenz und Compliance beeinflusst.
  - **Authentifizierung**: Zeigt, ob der Dienst öffentlich (unauthentifiziert erlaubt) ist oder IAM-Authentifizierung erfordert.
  - **Ingress**: Steuert das Traffic-Routing – z. B. "All" für intern/extern oder eingeschränkt auf nur intern.
  - **Zuletzt bereitgestellt**: Zeitstempel der letzten Aktualisierung.
  - **Bereitgestellt von**: Der Benutzer oder Service-Account, der die Bereitstellung durchgeführt hat.

- **Filter und Aktionen**: Über der Tabelle können Sie nach jeder dieser Spalten filtern, um Ihre Liste einzugrenzen. Verwenden Sie die Schaltfläche "Create Service", um neue Dienste bereitzustellen, oder klicken Sie auf einen Dienstnamen, um Einstellungen wie CPU-/Speicherlimits, Umgebungsvariablen, Skalierungskonfigurationen oder Revisionen für Traffic-Splitting zu bearbeiten.

Diese Konsole erleichtert die Leistungsüberwachung, die Anzeige von Protokollen und die Iteration an Bereitstellungen, ohne den Browser zu verlassen. Für praktische Erkundungen navigieren Sie zu [console.cloud.google.com/run](https://console.cloud.google.com/run), nachdem Sie die API aktiviert haben.

[Was ist Cloud Run?](https://cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Cloud Run-Dokumentation](https://cloud.google.com/run/docs)