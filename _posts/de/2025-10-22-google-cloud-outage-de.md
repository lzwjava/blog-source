---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Großstörung der Google Cloud Platform
translated: true
type: note
---

### Überblick

Am 12. Juni 2025 erlebte die Google Cloud Platform (GCP) einen schwerwiegenden globalen Ausfall, der ungefähr 7,5 Stunden dauerte (von 10:51 PDT bis 18:18 PDT). Der Vorfall resultierte aus einem Fehler in einer neu eingeführten Funktion innerhalb von Googles Service Control-System, speziell im Zusammenhang mit Quotenrichtlinienprüfungen. Dies verursachte, dass eine ungültige automatisierte Quotenaktualisierung sich global verbreitete, was zu weit verbreiteten API-Ablehnungen und Task-Überlastungen führte, insbesondere in Regionen mit hohem Datenaufkommen wie us-central1 (Iowa). Der Ausfall unterbrach den Zugang zu zahlreichen GCP-Diensten, Google Workspace-Produkten und Drittanbieteranwendungen, die von der GCP-Infrastruktur abhängen, und führte zu über 1,4 Millionen Nutzerberichten auf Downdetector.

### Zeitlicher Ablauf
(Alle Zeiten in US/Pacific, PDT)

- **10:51 Uhr**: Der Ausfall beginnt mit vermehrten 503-Fehlern bei externen API-Anfragen über mehrere GCP- und Google Workspace-Produkte hinweg, was zu intermittierenden Zugriffsproblemen führt.
- **11:46 Uhr**: Die Technikteams bestätigen weitreichende Dienstbeeinträchtigungen; die Untersuchung läuft.
- **12:09 Uhr**: Gegenmaßnahmen beginnen; Wiederherstellung in den meisten Regionen außer us-central1.
- **12:41 Uhr**: Die Grundursache wird als ungültige Quotenrichtliniendaten identifiziert; eine Umgehung für Quotenprüfungen wird implementiert.
- **13:16 Uhr**: Vollständige Wiederherstellung der Infrastruktur in allen Regionen außer us-central1 und der Multi-Region US.
- **14:00 Uhr**: Anzeichen der Erholung in us-central1; vollständige Behebung innerhalb einer Stunde erwartet.
- **15:16 Uhr**: Die meisten GCP-Produkte sind wiederhergestellt, aber Restprobleme bestehen in Dataflow, Vertex AI und Personalized Service Health.
- **17:06 Uhr**: Dataflow und Personalized Service Health sind behoben; Probleme mit Vertex AI dauern an mit einem geplanten Ende um 22:00 Uhr.
- **18:27 Uhr**: Vertex AI ist in allen Regionen vollständig wiederhergestellt.
- **18:18 Uhr**: Der Vorfall wird offiziell für beendet erklärt, alle Dienste sind vollständig wiederhergestellt.

Die primäre Problembehebung dauerte etwa 3 Stunden, aber verbleibende Rückstände und Fehler verlängerten die Gesamtauswirkung auf 7,5 Stunden.

### Grundursache

Der Ausfall wurde durch einen Fehler in der Service Control-Funktion ausgelöst, die API-Quoten und -Richtlinien verwaltet. Ein automatisiertes System führte eine ungültige Quotenrichtlinie, die leere oder Null-Felder enthielt, in die Datenbank ein. Aufgrund der globalen Replikation (entworfen für nahezu sofortige Konsistenz) verbreiteten sich diese beschädigten Daten innerhalb von Sekunden weltweit. Wenn API-Anfragen auf die Quotenprüfung trafen, führte dies zu Nullzeiger-Ausnahmen und Ablehnungen (erhöhte 503- und 5xx-Fehler). In großen Regionen wie us-central1 verursachte der Zustrom fehlgeschlagener Anfragen schwere Task-Überlastungen und kaskadierende Fehler in abhängigen Diensten. Der neuen Funktion fehlte eine ausreichende Validierung für Randfälle wie leere Felder, und das System "fail-open"-Verhalten (das Fortsetzen von Anfragen während der Prüfungen) war nicht implementiert.

### Betroffene Dienste

Der Ausfall betraf eine breite Palette von Google-Produkten und externen Diensten, die auf GCP angewiesen sind. Kern-GCP- und Google Workspace-Dienste erlebten unterschiedlich starke Unterbrechungen, einschließlich API-Fehlern und UI-Zugriffsproblemen (Streaming- und IaaS-Ressourcen waren nicht betroffen).

#### Wichtige betroffene Google Cloud Produkte
- **Compute & Storage**: Google Compute Engine, Cloud Storage, Persistent Disk.
- **Datenbanken**: Cloud SQL, Cloud Spanner, Cloud Bigtable, Firestore.
- **Daten & Analytics**: BigQuery, Dataflow, Dataproc, Vertex AI (einschließlich Online Prediction und Feature Store).
- **Netzwerke & Sicherheit**: Cloud Load Balancing, Cloud NAT, Identity and Access Management (IAM), Cloud Security Command Center.
- **Developer Tools**: Cloud Build, Cloud Functions, Cloud Run, Artifact Registry.
- **AI/ML**: Vertex AI Search, Speech-to-Text, Document AI, Dialogflow.
- **Andere**: Apigee, Cloud Monitoring, Cloud Logging, Resource Manager API.

#### Wichtige betroffene Google Workspace Produkte
- Gmail, Google Drive, Google Docs, Google Meet, Google Calendar, Google Chat.

#### Betroffene Drittanbieterdienste
Viele Consumer- und Enterprise-Apps, die auf GCP gehostet oder teilweise darauf angewiesen sind, erlebten Ausfallzeiten:
- **Spotify**: Streaming- und App-Zugang für ~46.000 Nutzer unterbrochen.
- **Discord**: Probleme bei Sprach-Chats und Serververbindungen.
- **Fitbit**: Synchronisierung und App-Funktionalität gestoppt.
- **Andere**: OpenAI (ChatGPT), Shopify, Snapchat, Twitch, Cloudflare (kaskadierende DNS-Probleme), Anthropic, Replit, Microsoft 365 (teilweise), Etsy, Nest.

Der globale Maßstab verstärkte die Auswirkungen, da GCP einen bedeutenden Teil der Backend-Infrastruktur des Internets betreibt.

### Lösung

Googles Technikteams identifizierten schnell die ungültige Richtlinie und implementierten eine Umgehung für die Quotenprüfungen, die es API-Anfragen erlaubte, während der Krise ohne Validierung fortzufahren. Dies stellte die meisten Regionen bis 12:48 Uhr PDT wieder her. Für us-central1 wurden gezielte Überlastungs-Minderungen angewendet, gefolgt von manueller Beseitigung von Rückständen in betroffenen Diensten wie Dataflow und Vertex AI. Die Überwachung bestätigte die vollständige Wiederherstellung bis 18:18 Uhr PDT. Es gab keinen Datenverlust, aber einige Dienste erlebten vorübergehende Verzögerungen.

### Auswirkungen

- **Umfang**: Über 1,4 Millionen Downdetector-Berichte, die die Echtzeit-Störung global hervorhoben.
- **Wirtschaftlich**: Milliarden an potenziell verlorener Produktivität für Unternehmen; Spotify allein berichtete von Nutzerfrustration während der Hauptverkehrszeiten.
- **Ruf**: Unterstrich die Risiken der Cloud-Konzentration, mit Forderungen nach besseren Multi-Cloud-Strategien.

### Erkenntnisse und Präventivmaßnahmen

Google veröffentlichte einen detaillierten Post-Mortem-Bericht mit Schwerpunkt auf Resilienz:
- **Architekturänderungen**: Modularisierung von Service Control, um Fehler zu isolieren und "Fail-Open"-Modi zu ermöglichen.
- **Datenvalidierung**: Inkrementelle Verbreitung globaler Änderungen mit Vorabvalidierung; erweiterte Tests für ungültige Eingaben.
- **Bereitstellungssicherungen**: Verpflichtende Feature Flags für kritische Updates; verbesserte statische Analyse und Fehlerbehandlung.
- **Monitoring & Kommunikation**: Sicherstellen, dass Ausfall-Erkennungstools unabhängig operational bleiben; schnellere automatisierte Kundenbenachrichtigungen.
- **Weitergehend**: Randomisierte Backoff-Zeiten in der Wiederholungslogik, um Überlastungskaskaden zu verhindern.

Diese Schritte zielen darauf ab, ähnliche Vorfälle zu verhindern, mit laufenden Audits der Quotensysteme.

[Google Cloud Incident Report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)
[ThousandEyes Outage Analysis](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)
[Ookla Downdetector Report](https://www.ookla.com/articles/google-cloud-outage-june-2025)
[ByteByteGo Breakdown](https://blog.bytebytego.com/p/how-the-google-cloud-outage-crashed)
[Medium Root Cause Explanation](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-a-single-google-cloud-bug-caused-global-internet-outage-on-june-12-2025-652a83ad9e68)