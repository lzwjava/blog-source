---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Navigationsleitfaden für die IBM WebSphere-Administrationskonsole
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) Administrationskonsole: Linker Navigationsbereich

Die linke Ansicht in der IBM WebSphere Application Server (WAS) Administrationskonsole (auch bekannt als Integrated Solutions Console) ist ein hierarchischer Navigationsbaum, der Konfigurations- und Verwaltungsaufgaben organisiert. Sie bietet schnellen Zugriff auf wichtige Bereiche zur Administration der Serverumgebung, Anwendungen und Ressourcen. Die genaue Struktur kann je nach WAS-Version (z.B. 8.5, 9.0) und Edition (Base vs. Network Deployment) leicht variieren, aber die Kernkategorien der obersten Ebene sind konsistent.

Nachfolgend finden Sie eine Liste der wichtigsten Hauptabschnitte im Navigationsbaum mit kurzen Beschreibungen ihrer Hauptaufgaben. Unterabschnitte sind für detailliertere Aufgaben erweiterbar (mit +/- Symbolen).

#### Hauptabschnitte der obersten Ebene
- **Applications**  
  Wird zum Bereitstellen, Installieren, Aktualisieren, Starten/Stoppen und Verwalten von Anwendungen (z.B. EAR/WAR-Dateien) verwendet.  
  *Wichtige Unterabschnitte*: Enterprise Applications, WebSphere Enterprise Applications, Web Modules, Shared Libraries.  
  *Häufige Aufgaben*: Neue Apps installieren, Module Servern zuordnen, Class Loader konfigurieren.

- **Resources**  
  Konfiguriert gemeinsame Ressourcen wie Datenbanken, Messaging und Verbindungspools, die Anwendungen nutzen können.  
  *Wichtige Unterabschnitte*: JDBC (Data Sources/Providers), JMS (Queues/Topics), JavaMail Sessions, URL Providers.  
  *Häufige Aufgaben*: JDBC Data Sources einrichten, JMS Connection Factories erstellen.

- **Services**  
  Verwaltet serverweite Dienste wie Sicherheit, Messaging und Kommunikationsprotokolle.  
  *Wichtige Unterabschnitte*: Security (globale Sicherheit, Benutzer/Gruppen, Authentifizierung), Mail Providers, Ports, ORB Service, Transaction Service.  
  *Häufige Aufgaben*: SSL aktivieren, Benutzerverzeichnisse konfigurieren, Portzuweisungen anpassen.

- **Servers**  
  Verwaltet Serverinstanzen, Clustering und Web-Server-Definitionen.  
  *Wichtige Unterabschnitte*: Server Types (WebSphere application servers, WebSphere proxy servers), Clusters, Web Servers.  
  *Häufige Aufgaben*: Server starten/stoppen, JVM-Einstellungen konfigurieren, Cluster für Hochverfügbarkeit erstellen.

- **System Administration**  
  Verwaltet die Gesamttopologie, einschließlich Nodes, Cells und Konsoleneinstellungen.  
  *Wichtige Unterabschnitte*: Nodes, Cells, Deployment Manager, Console Preferences.  
  *Häufige Aufgaben*: Nodes synchronisieren, Deployment Manager verwalten, Konsolen-Themen/Bereiche festlegen.

- **Environment**  
  Definiert umgebungsspezifische Variablen und Aliase.  
  *Wichtige Unterabschnitte*: WebSphere Variables, Hosts Aliases.  
  *Häufige Aufgaben*: Systemvariablen für Pfade oder Eigenschaften setzen.

- **Monitor and Tuning**  
  Überwacht die Leistung und optimiert das Laufzeitverhalten.  
  *Wichtige Unterabschnitte*: Performance Monitoring Infrastructure (PMI), Custom Services, Logging and Tracing.  
  *Häufige Aufgaben*: Metriken aktivieren, Thread-Pools anpassen, Request-Metriken einsehen.

- **Troubleshooting**  
  Bietet Zugang zu Diagnosetools und Protokollen.  
  *Wichtige Unterabschnitte*: Logs and Trace, First Steps.  
  *Häufige Aufgaben*: Protokolle herunterladen, Trace Specifications aktivieren.

#### Zusätzliche Hinweise
- **Bereichsauswahl (Scope Selection)**: Oben auf vielen Seiten können Sie die Sichtbarkeit nach Bereich (Cell, Node, Server) filtern.
- **Guided Activities**: Erscheint manchmal als oberster oder kontextbezogener Abschnitt für Assistenten (z.B. zum Absichern der Umgebung).
- Zugriff auf die Konsole: Typischerweise über `https://<Host>:<Port>/ibm/console` (Standardport 9060 für Admin, 9043 für Secure).
- Für versionsspezifische Details (z.B. WAS 9.0) konsultieren Sie die offizielle IBM-Dokumentation, da in Updates kleinere UI-Änderungen auftreten können.

[WebSphere Administrative Console - 101](https://www.ibm.com/community/101/websphere/administrative-console/)  
[Introduction: Administrative Console (WAS 9.0.5)](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=administration-introduction-administrative-console)  
[WebSphere Application Server V7: Administration Consoles (Redpaper)](https://www.redbooks.ibm.com/redpapers/pdfs/redp4573.pdf)