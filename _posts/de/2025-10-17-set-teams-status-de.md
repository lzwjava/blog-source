---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Festlegen des Team-Status mit PowerShell
translated: true
type: note
---

Nein, Microsoft Teams verfügt nicht über ein offizielles, eigenständiges Kommandozeilenprogramm (wie ein einfaches `teams --status offline` Executable) zum Festlegen Ihres Präsenzstatus. Die integrierten Slash-Befehle (z. B. `/away` oder `/offline`) funktionieren nur innerhalb der Teams-App-Oberfläche, nicht über ein Terminal.

Sie können dies jedoch über die Kommandozeile mit PowerShell und der Microsoft Graph API erreichen. Dies erfordert die Installation des Microsoft Graph PowerShell SDK, die Authentifizierung mit Ihrem Microsoft-Konto und die Ausführung eines Cmdlets, um Ihre Präsenz zu aktualisieren. Hier ist eine Schritt-für-Schritt-Anleitung:

### Voraussetzungen
1. Installieren Sie PowerShell (falls nicht bereits vorhanden; es ist in Windows 10+ integriert).
2. Öffnen Sie PowerShell als Administrator und installieren Sie das Modul:
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### Status festlegen
1. Stellen Sie eine Verbindung zu Microsoft Graph her (dies fordert zur Authentifizierung über den Browser auf):
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. Führen Sie das Cmdlet aus, um Ihren Status zu setzen. Ersetzen Sie `YourUserId` durch Ihre Microsoft Entra ID (Azure AD) Benutzer-ID (diese erhalten Sie über `Get-MgUser -UserId Ihre.Email@domain.com`). Häufige Statuswerte sind:
   - `Available` (Verfügbar)
   - `Away` (Abwesend)
   - `Busy` (Beschäftigt)
   - `DoNotDisturb` (Bitte nicht stören)
   - `Offline` (Anderen gegenüber als offline angezeigt)

   Beispiel, um auf offline zu setzen:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   Beispiel, um auf abwesend zu setzen:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. Um die Verbindung zu trennen, wenn Sie fertig sind:
   ```
   Disconnect-MgGraph
   ```

### Hinweise
- Dies aktualisiert Ihre Präsenz sofort, aber sie kann sich basierend auf Ihrer Aktivität zurücksetzen (z. B. löst Leerlaufzeit "Abwesend" aus).
- Für die Automatisierung (z. B. Skripte zum zeitgesteuerten Umschalten des Status) packen Sie die obigen Befehle in eine `.ps1`-Datei und führen Sie sie über den Task Scheduler aus.
- Wenn Sie auch eine benutzerdefinierte Statusnachricht festlegen möchten (z. B. "Mittagspause"), verwenden Sie `Set-MgUserPresenceStatusMessage`.
- Dies funktioniert für die private Nutzung, erfordert jedoch entsprechende Berechtigungen; Administratoren müssen möglicherweise den Graph API-Zugriff aktivieren.

Um Ihren Status während Leerlaufperioden auf "Verfügbar" zu halten (gängige Problemumgehung), existieren Skripte, die Aktivität simulieren (z. B. Umschalten der Num-Taste alle paar Minuten), aber dies sind keine echten Status-Setter.

Referenzen:  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)