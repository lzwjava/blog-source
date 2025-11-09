---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht zu Azure Monitor-Warnungen
translated: true
type: note
---

### Übersicht über Warnungen in Azure

Azure Monitor-Warnungen sind eine Funktion von Azure Monitor, die Sie proaktiv benachrichtigt, wenn bestimmte Bedingungen in Ihren Azure-Ressourcen erfüllt sind. Sie helfen Ihnen, Probleme zu erkennen und zu beheben, bevor sie Auswirkungen auf Benutzer haben. Sie funktionieren, indem sie Daten aus Metriken, Logs oder Aktivitätsprotokollen anhand vordefinierter Regeln auswerten. Wenn eine Bedingung ausgelöst wird (z. B. CPU-Auslastung über 80 %), wird eine Warnung ausgelöst, die Benachrichtigungen per E-Mail oder SMS senden oder automatisierte Aktionen wie das Ausführen eines Skripts auslösen kann.

Warnungen sind zustandsbehaftet (sie lösen sich automatisch auf, wenn das Problem behoben ist) oder zustandslos (sie werden wiederholt ausgelöst, bis sie manuell geschlossen werden), abhängig von Ihrer Konfiguration. Sie unterstützen die Überwachung über einzelne oder mehrere Ressourcen hinweg und werden basierend auf der Anzahl der überwachten Zeitreihen abgerechnet.

#### Arten von Warnungen
Azure Monitor unterstützt mehrere Warnungstypen, die auf verschiedene Datenquellen zugeschnitten sind:

| Warnungstyp              | Beschreibung | Am besten geeignet für |
|-------------------------|-------------|----------|
| **Metrikwarnungen**      | Werten numerische Metriken (z. B. CPU-Prozentsatz, Speicherplatz) in regelmäßigen Abständen aus. Unterstützt statische oder dynamische Schwellenwerte (KI-basiert). | Leistungsüberwachung von VMs, Datenbanken oder Apps. |
| **Log Search-Warnungen**  | Führen Abfragen auf Log Analytics-Daten aus, um Muster in Protokollen zu erkennen. | Komplexe Ereignisanalyse, z. B. Fehler-Spikes in Anwendungsprotokollen. |
| **Aktivitätsprotokoll-Warnungen**| Werden durch administrative oder operative Ereignisse ausgelöst (z. B. Erstellung/Löschung von Ressourcen). | Sicherheits- und Compliance-Überwachung. |
| **Smart Detection-Warnungen** | KI-gestützte Anomalieerkennung für Web-Apps über Application Insights. | Automatische Problemerkennung in Apps. |
| **Prometheus-Warnungen**  | Fragen Prometheus-Metriken in verwalteten Diensten wie AKS ab. | Container- und Kubernetes-Umgebungen. |

Für die meisten Anwendungsfälle sollten Sie mit Metrik- oder Log-Warnungen beginnen.

### Voraussetzungen
- Ein Azure-Abonnement mit aktiven, zu überwachenden Ressourcen.
- Berechtigungen: Die Rolle "Leser" auf der Zielressource, "Mitwirkender" auf der Ressourcengruppe für die Warnungsregel und "Leser" auf allen Aktionsgruppen.
- Vertrautheit mit dem Azure-Portal (portal.azure.com).

### Erstellen und Verwenden einer Metrikwarnungsregel (Schritt für Schritt)
Metrikwarnungen sind ein häufiger Ausgangspunkt. So erstellen Sie eine im Azure-Portal. Dieser Prozess dauert etwa 5-10 Minuten.

1. **Melden Sie sich beim Azure-Portal an**: Gehen Sie zu [portal.azure.com](https://portal.azure.com) und loggen Sie sich ein.

2. **Navigieren Sie zu "Warnungen"**:
   - Suchen Sie auf der Startseite nach **Monitor** und wählen Sie es aus.
   - Wählen Sie im linken Menü unter **Insights** den Punkt **Warnungen**.
   - Klicken Sie auf **+ Erstellen** > **Warnungsregel**.

   *Alternative*: Wählen Sie bei einer bestimmten Ressource (z. B. einer VM) im linken Menü **Warnungen** und dann **+ Erstellen** > **Warnungsregel**. Dies setzt den Bereich automatisch.

3. **Legen Sie den Bereich fest**:
   - Wählen Sie im Bereich **Ressource auswählen** Ihr Abonnement, den Ressourcentyp (z. B. "Virtual machines") und die spezifische Ressource aus.
   - Klicken Sie auf **Übernehmen**. (Für Multi-Ressourcen-Warnungen wählen Sie mehrere Ressourcen desselben Typs in einer Region aus.)

4. **Konfigurieren Sie die Bedingung**:
   - Klicken Sie auf der Registerkarte **Bedingung** auf **Signalname** und wählen Sie eine Metrik aus (z. B. "Percentage CPU" für eine VM).
     - Verwenden Sie **Alle Signale anzeigen**, um nach Typ zu filtern (z. B. Plattformmetriken).
   - Vorschau der Daten: Legen Sie einen Zeitraum fest (z. B. letzte 24 Stunden), um historische Werte zu sehen.
   - Legen Sie die **Warnungslogik** fest:
     - **Schwellenwert**: Statisch (z. B. > 80) oder Dynamisch (KI-angepasst basierend auf dem Verlauf).
     - **Operator**: Größer als, Kleiner als, etc.
     - **Aggregation**: Durchschnitt, Summe, Min, Max über den Auswertungszeitraum.
     - Für dynamisch: Wählen Sie die Empfindlichkeit (Niedrig/Mittel/Hoch).
   - (Optional) **Nach Dimensionen aufteilen**: Filtern Sie nach Attributen wie Instanzname für granulare Warnungen (z. B. pro VM in einem Set).
   - **Auswertung**: Überprüfen Sie alle 1-5 Minuten; schauen Sie 5-15 Minuten zurück.
   - Klicken Sie auf **Fertig**.

5. **Fügen Sie Aktionen hinzu (Optional, aber empfohlen)**:
   - Wählen Sie auf der Registerkarte **Aktionen** die Option **Aktionsgruppen hinzufügen**.
   - Wählen Sie eine bestehende Gruppe (für E-Mails/SMS) oder erstellen Sie eine:
     - Fügen Sie Empfänger hinzu (z. B. E-Mail der Administratoren).
     - Fügen Sie Aktionen wie Logic Apps für Automatisierung oder Webhooks für Integrationen hinzu.
   - Klicken Sie auf **Fertig**.

6. **Legen Sie Regeldetails fest**:
   - Auf der Registerkarte **Details**:
     - **Abonnement** und **Ressourcengruppe**: Automatisch ausgefüllt; bei Bedarf ändern.
     - **Schweregrad**: Sev 0 (Kritisch) bis Sev 4 (Ausführlich).
     - **Name der Warnungsregel**: z. B. "High CPU Alert - Prod VM".
     - **Beschreibung**: Optionale Notizen.
   - **Erweiterte Optionen**:
     - Regel bei Erstellung aktivieren.
     - Warnungen automatisch auflösen (macht sie zustandsbehaftet).
   - Fügen Sie bei Bedarf Tags für die Organisation hinzu.

7. **Überprüfen und Erstellen**:
   - Gehen Sie zu **Überprüfen + erstellen**.
   - Validieren Sie (beheben Sie ggf. Fehler, wie ungültige Schwellenwerte).
   - Klicken Sie auf **Erstellen**. Die Regel wird sofort aktiviert, wenn sie aktiviert ist.

Sobald erstellt, löst die Warnung aus, wenn die Bedingungen erfüllt sind, sendet Benachrichtigungen und aktualisiert ihren Status (z. B. von "Ausgelöst" zu "Gelöst").

#### Verwalten von Warnungen
- **Warnungen anzeigen**: Sehen Sie sich in Monitor > Warnungen aktive/ausgelöste Warnungen an. Filtern Sie nach Zeit, Schweregrad oder Ressource.
- **Eine Regel bearbeiten**: Gehen Sie zu Monitor > Warnungen > Warnungsregeln, wählen Sie die Regel aus und klicken Sie auf **Bearbeiten**.
- **Testen**: Verwenden Sie die Vorschau in Schritt 4 zur Simulation.
- **Skalieren**: Verwenden Sie für mehrere Ressourcen Azure CLI/PowerShell oder ARM-Vorlagen. Aktivieren Sie integrierte empfohlene Regeln über Ressourcen-Insights.

### Best Practices
- Fangen Sie einfach an: Anfangs eine Bedingung pro Regel.
- Verwenden Sie dynamische Schwellenwerte für verrauschte Metriken, um falsch-positive Meldungen zu reduzieren.
- Integrieren Sie Aktionsgruppen für automatisierte Abhilfemaßnahmen (z. B. Hochskalieren einer VM).
- Überwachen Sie die Kosten: Basierend auf überwachten Reihen (kostenlos für die Grundnutzung; Preise prüfen).
- Für Logs folgen Sie ähnlichen Schritten, wählen aber bei der Erstellung **Log-Warnungen** und schreiben eine KQL-Abfrage.

Für Log-Warnungen oder andere Typen ist der Prozess analog – ersetzen Sie einfach die Bedingung durch eine Abfrage.

[Übersicht über Azure Monitor-Warnungen](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)  
[Erstellen einer Metrikwarnungsregel](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule)  
[Erstellen einer Log-Warnungsregel](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-log-alert-rule)  
[Azure Monitor – Preise](https://azure.microsoft.com/en-us/pricing/details/monitor/)