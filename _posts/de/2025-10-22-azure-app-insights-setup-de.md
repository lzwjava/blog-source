---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einrichtungsleitfaden für Azure Application Insights
translated: true
type: note
---

## Was ist Azure Application Insights?

Azure Application Insights ist ein Application Performance Management (APM)-Dienst in Azure Monitor, der Sie bei der Überwachung von Live-Webanwendungen unterstützt. Er bietet Tools zum Erkennen von Problemen, zur Diagnose von Fehlern und zum Verständnis des Benutzerverhaltens durch Telemetriedaten wie Anforderungen, Abhängigkeiten, Ablaufverfolgungen, Metriken und Protokolle. Er wird nun von OpenTelemetry angetrieben, um eine breitere Kompatibilität zu gewährleisten.

## Voraussetzungen
- Ein aktives Azure-Abonnement.
- Berechtigungen zum Erstellen von Ressourcen in Azure (z. B. die Rolle „Besitzer“ oder „Mitwirkender“).
- Ihr Anwendungscode (unterstützt .NET, Java, Node.js, Python und mehr).

## Schritt 1: Erstellen einer Application Insights-Ressource
1. Melden Sie sich beim [Azure-Portal](https://portal.azure.com) an.
2. Klicken Sie im Menü oben links auf **Ressource erstellen**.
3. Suchen Sie nach „Application Insights“ und wählen Sie es in den Ergebnissen unter **Überwachung + Verwaltung** aus.
4. Füllen Sie die Details aus:
   - **Abonnement**: Wählen Sie Ihr Azure-Abonnement.
   - **Ressourcengruppe**: Wählen Sie eine bestehende Gruppe aus oder erstellen Sie eine neue.
   - **Name**: Geben Sie Ihrer Ressource einen eindeutigen Namen.
   - **Region**: Wählen Sie eine Region in der Nähe Ihrer Benutzer oder Ihrer App.
   - **Arbeitsbereich**: Verknüpfen Sie optional mit einem bestehenden Log Analytics-Arbeitsbereich; andernfalls wird automatisch ein neuer erstellt.
5. Überprüfen Sie die Angaben und klicken Sie auf **Erstellen**. Die Bereitstellung dauert einige Minuten.
6. Wechseln Sie nach der Erstellung zur Seite **Übersicht** Ihrer Ressource und kopieren Sie die **Verbindungszeichenfolge** (fahren Sie mit der Maus darüber und klicken Sie auf das Kopiersymbol). Diese identifiziert, wohin Ihre App Telemetriedaten sendet.

**Tipp**: Verwenden Sie separate Ressourcen für Dev-, Test- und Prod-Umgebungen, um eine Vermischung von Daten zu vermeiden.

## Schritt 2: Instrumentieren Sie Ihre Anwendung
Fügen Sie OpenTelemetry-Unterstützung hinzu, um automatisch Telemetriedaten zu sammeln (Anforderungen, Ausnahmen, Metriken usw.). Setzen Sie die Verbindungszeichenfolge über eine Umgebungsvariable namens `APPLICATIONINSIGHTS_CONNECTION_STRING` (empfohlen für die Produktion).

### Für .NET (ASP.NET Core)
1. Installieren Sie das NuGet-Paket:
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. In `Program.cs`:
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. Setzen Sie die Umgebungsvariable mit Ihrer Verbindungszeichenfolge und führen Sie die App aus.

### Für Java
1. Laden Sie die Azure Monitor OpenTelemetry Distro JAR herunter (z. B. `applicationinsights-agent-3.x.x.jar`).
2. Erstellen Sie eine Konfigurationsdatei `applicationinsights.json` im selben Verzeichnis:
   ```json
   {
     "connectionString": "Ihre Verbindungszeichenfolge hier"
   }
   ```
3. Führen Sie Ihre App mit dem Agent aus: `java -javaagent:applicationinsights-agent-3.x.x.jar -jar your-app.jar`.

### Für Node.js
1. Installieren Sie das Paket:
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. Konfigurieren Sie es in Ihrem App-Einstiegspunkt:
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. Setzen Sie die Umgebungsvariable und starten Sie Ihre App.

### Für Python
1. Installieren Sie das Paket:
   ```
   pip install azure-monitor-opentelemetry
   ```
2. In Ihrer App:
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="Ihre Verbindungszeichenfolge hier")
   ```
3. Führen Sie die App aus.

Für andere Sprachen oder Auto-Instrumentierung (z. B. für Azure App Service) lesen Sie die offizielle Dokumentation. Testen Sie zuerst lokal.

## Schritt 3: Anzeigen und Analysieren von Daten
1. Führen Sie Ihre instrumentierte App aus und generieren Sie etwas Aktivität (z. B. senden Sie Anforderungen).
2. Öffnen Sie im Azure-Portal Ihre Application Insights-Ressource.
3. Überprüfen Sie die Seite **Übersicht**: Sehen Sie sich Live-Metriken, Anforderungsanzahlen und Antwortzeiten an (Daten erscheinen nach ca. 1-2 Minuten).
4. Erkunden Sie die Funktionen:
   - **Live Metrics**: Echtzeit-Datenstrom für Produktions-Apps.
   - **Fehler**: Detaillierte Untersuchung von Ausnahmen und Ablaufverfolgungen.
   - **Leistung**: Analysieren Sie Abhängigkeiten und langsame Anforderungen.
   - **Nutzung**: Verfolgen Sie Benutzersitzungen und benutzerdefinierte Ereignisse.
   - **Warnungen**: Richten Sie Benachrichtigungen für Probleme ein (z. B. hohe Fehlerraten).
5. Fragen Sie Daten mit der Kusto Query Language (KQL) unter **Protokolle** für benutzerdefinierte Analysen ab.

## Best Practices
- Beginnen Sie mit grundlegender Telemetrie; fügen Sie bei Bedarf benutzerdefinierte Ereignisse/Metriken hinzu.
- Überwachen Sie die Kosten über die Seite **Nutzung und geschätzte Kosten** (Abrechnung erfolgt über Log Analytics).
- Für die Browserüberwachung fügen Sie das JavaScript SDK-Snippet zu Ihren Webseiten hinzu.

[Erstellen und Konfigurieren von Application Insights-Ressourcen](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[Aktivieren von OpenTelemetry in Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Application Insights-Übersicht](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)