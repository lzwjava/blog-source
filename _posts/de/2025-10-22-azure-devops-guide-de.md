---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Azure DevOps Essential Guide
translated: true
type: note
---

Azure DevOps ist eine umfassende Suite cloudbasierter Entwicklungstools von Microsoft, die Teams dabei unterstützt, Software effizient zu planen, zu entwickeln, zu testen und auszuliefern. Es integriert sich nahtlos mit anderen Microsoft-Diensten wie Azure und GitHub und unterstützt verschiedene Methodologien wie Agile, Scrum und DevOps-Praktiken. Dieser Leitfaden behandelt die Grundlagen: Was es ist, wichtige Komponenten, erste Schritte, Best Practices und Ressourcen für vertiefendes Lernen.

## Was ist Azure DevOps?
Azure DevOps bietet End-to-End-DevOps-Fähigkeiten und ermöglicht die Zusammenarbeit zwischen Entwicklung, Betrieb und Stakeholdern. Es ist plattformunabhängig und unterstützt mehrere Sprachen, Frameworks und Tools. Zu den wichtigsten Vorteilen gehören:
- **Skalierbarkeit**: Bewältigt Projekte jeder Größe, von kleinen Teams bis hin zu Unternehmen.
- **Integration**: Verbindet sich mit IDEs wie Visual Studio, GitHub, Slack und Jira.
- **Sicherheit**: Integrierte Compliance-Features wie rollenbasierte Zugriffssteuerung (RBAC) und Audit-Logs.
- **Preisgestaltung**: Kostenlos für bis zu 5 Benutzer; kostenpflichtige Pläne beginnen bei 6 $/Benutzer/Monat für zusätzliche Funktionen.

Stand 2025 hat sich Azure DevOps mit erweiterten KI-Integrationen (z. B. GitHub Copilot für Azure) und verbesserten Pipeline-Analysen weiterentwickelt.

## Wichtige Komponenten
Azure DevOps besteht aus fünf Kernservices, die jeweils über ein Webportal oder APIs zugänglich sind:

### 1. **Boards**
   - **Zweck**: Visuelle Planungs- und Nachverfolgungstools für Arbeitselemente.
   - **Funktionen**:
     - Kanban-Boards zur Visualisierung von Workflows.
     - Backlogs zum Priorisieren von Aufgaben.
     - Sprints für Agile-Iterationen.
     - Abfragen für benutzerdefinierte Berichte.
   - **Anwendungsfall**: Verfolgen Sie Fehler, Features und Aufgaben in Echtzeit.

### 2. **Repos**
   - **Zweck**: Zentralisierte Versionskontrolle für Code.
   - **Funktionen**:
     - Git- oder TFVC-Repositorys.
     - Branching-Strategien und Pull Requests.
     - Wiki-Integration für Dokumentation.
   - **Anwendungsfall**: Zusammenarbeit bei Code-Reviews und Pflege der Historie.

### 3. **Pipelines**
   - **Zweck**: CI/CD-Automatisierung (Continuous Integration/Continuous Deployment).
   - **Funktionen**:
     - YAML-basierte oder klassische Pipelines.
     - Multi-Stage-Builds, Tests und Deployments.
     - Integration mit Azure Artifacts für die Paketverwaltung.
     - Environments für Genehmigungen und Gates.
   - **Anwendungsfall**: Automatisieren Sie Builds für jeden Commit und deployen Sie in die Cloud oder On-Premises.

### 4. **Test Plans**
   - **Zweck**: Manuelles und exploratives Testen.
   - **Funktionen**:
     - Testfall-Management.
     - Live-Protokolle und Anhänge.
     - Integration mit automatisierten Tests aus Pipelines.
   - **Anwendungsfall**: Sicherstellen der Qualität vor der Veröffentlichung.

### 5. **Artifacts**
   - **Zweck**: Paketverwaltung und Behandlung von Abhängigkeiten.
   - **Funktionen**:
     - Universal Packages, NuGet-, npm- und Maven-Feeds.
     - Aufbewahrungsrichtlinien für Binärdateien.
   - **Anwendungsfall**: Teilen und Versionieren von Bibliotheken teamsübergreifend.

## Erste Schritte
Befolgen Sie diese Schritte, um Azure DevOps einzurichten:

1. **Konto erstellen**:
   - Gehen Sie zu [dev.azure.com](https://dev.azure.com) und registrieren Sie sich mit einem Microsoft-Konto (kostenloser Tarif verfügbar).
   - Erstellen Sie eine neue Organisation (z. B. "MyProjectOrg").

2. **Projekt einrichten**:
   - Klicken Sie in Ihrer Organisation auf "New Project".
   - Wählen Sie Sichtbarkeit (privat/öffentlich) und Versionskontrolle (Git/TFVC).
   - Fügen Sie Teammitglieder per E-Mail-Einladung hinzu.

3. **Repos konfigurieren**:
   - Klonen Sie das Standard-Repo: `git clone https://dev.azure.com/{org}/{project}/_git/{repo}`.
   - Übertragen Sie Ihren initialen Code: `git add . && git commit -m "Initial commit" && git push`.

4. **Eine einfache Pipeline erstellen**:
   - In Pipelines > New Pipeline > Repository auswählen > ASP.NET (oder Ihr Framework).
   - Verwenden Sie YAML für Einfachheit:
     ```yaml
     trigger:
     - main
     pool:
       vmImage: 'ubuntu-latest'
     steps:
     - task: DotNetCoreCLI@2
       inputs:
         command: 'build'
         projects: '**/*.csproj'
     ```
   - Speichern und Ausführen der Pipeline.

5. **Ein Board erstellen**:
   - Gehen Sie zu Boards > Sprints > New Query.
   - Definieren Sie Arbeitselementtypen (z. B. Epic > Feature > Task).

6. **Testen und Bereitstellen**:
   - Fügen Sie eine Testaufgabe in Ihrer Pipeline hinzu.
   - Richten Sie eine Release-Pipeline für das Deployment in Azure App Service ein.

Für praktische Tutorials beginnen Sie mit den offiziellen Schnellstarts.

## Best Practices
- **YAML-Pipelines übernehmen**: Sie sind versionskontrolliert und wiederverwendbar.
- **Branch-Richtlinien verwenden**: Erzwingen Sie Pull-Request-Genehmigungen und verknüpfte Arbeitselemente.
- **Security Scans implementieren**: Integrieren Sie Tools wie SonarQube oder Microsoft Defender.
- **Mit Analytics überwachen**: Verwenden Sie Dashboards für Velocity und Build-Erfolgsquoten.
- **Mit Erweiterungen skalieren**: Der Marketplace bietet 2.000+ Erweiterungen (z. B. Slack-Benachrichtigungen).
- **Hybrid-Support**: Für On-Premises verwenden Sie Azure DevOps Server (selbst gehostet).

Häufige Fallstricke: Übermäßige Anpassung am Anfang – beginnen Sie einfach und iterieren Sie.

## Fortgeschrittene Themen
- **Erweiterungen und Marketplace**: Passen Sie es mit Plugins für Tools wie Jenkins oder Terraform an.
- **KI/ML-Integration**: Verwenden Sie Azure ML für die Modellbereitstellung in Pipelines.
- **Multi-Team-Collaboration**: Nutzen Sie Areas und Iterations für große Organisationen.
- **Migration**: Tools zum Importieren von GitHub oder Jira.

## Referenzen
- [Azure DevOps-Dokumentation](https://learn.microsoft.com/en-us/azure/devops/)
- [Erste Schritte mit Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/get-started/what-is-azure-devops)
- [Azure DevOps-Preise](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
- [Best Practices für Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/)