---
audio: false
generated: true
lang: de
layout: post
title: Leitfaden für PowerShell-Befehle
translated: true
type: note
---

## Einführung in PowerShell
PowerShell ist ein Framework zur Aufgabenautomatisierung und Konfigurationsverwaltung von Microsoft, bestehend aus einer Befehlszeilen-Shell und einer Skriptsprache. Es basiert auf dem .NET Framework (und .NET Core in neueren Versionen) und ermöglicht Administratoren die Ausführung komplexer Aufgaben über Windows-, Linux- und macOS-Systeme hinweg.

PowerShell-Befehle, bekannt als **Cmdlets** (ausgesprochen "Command-lets"), folgen einer `Verb-Noun`-Namenskonvention (z.B. `Get-Process`, `Set-Item`). Dieser Leitfaden behandelt wesentliche Cmdlets, kategorisiert nach Funktionalität, mit Beispielen zur Veranschaulichung ihrer Verwendung.

---

## 1. Grundlegende PowerShell-Konzepte
Bevor wir uns mit Befehlen befassen, ist das Verständnis wichtiger Konzepte entscheidend:
- **Cmdlets**: Leichtgewichtige Befehle, die spezifische Funktionen ausführen.
- **Pipelines**: Ermöglichen, dass die Ausgabe eines Cmdlets als Eingabe an einen anderen Befehl weitergegeben wird, unter Verwendung des `|`-Operators.
- **Module**: Sammlungen von Cmdlets, Skripten und Funktionen, die die PowerShell-Funktionalität erweitern.
- **Provider**: Schnittstellen für den Zugriff auf Datenspeicher (z.B. Dateisystem, Registry), als wären sie Laufwerke.
- **Objekte**: PowerShell arbeitet mit Objekten, nicht mit Klartext, und ermöglicht so die strukturierte Datenmanipulation.

---

## 2. Wesentliche Cmdlets nach Kategorien

### 2.1 Systeminformationen
Diese Cmdlets rufen Informationen über das System, Prozesse und Dienste ab.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Get-ComputerInfo` | Ruft Details zur Systemhardware und -software ab. | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | Listet laufende Prozesse auf. | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | Zeigt die Dienste auf dem System an. | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | Listet installierte Windows-Updates auf. | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**Beispiel**: Alle laufenden Prozesse nach CPU-Auslastung sortiert auflisten.
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 Datei- und Verzeichnisverwaltung
PowerShell behandelt das Dateisystem als Provider und ermöglicht eine ähnliche Navigation wie bei einem Laufwerk.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Get-Item` | Ruft Dateien oder Verzeichnisse ab. | `Get-Item C:\Users\*.txt` |
| `Set-Item` | Modifiziert Elementeigenschaften (z.B. Dateiattribute). | `Set-Item -Path C:\test.txt -Value "Neuer Inhalt"` |
| `New-Item` | Erstellt eine neue Datei oder ein neues Verzeichnis. | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | Löscht Dateien oder Verzeichnisse. | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | Kopiert Dateien oder Verzeichnisse. | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | Verschiebt Dateien oder Verzeichnisse. | `Move-Item C:\Docs\Report.txt C:\Archive` |

**Beispiel**: Ein Verzeichnis und eine Datei erstellen und dann an einen anderen Ort kopieren.
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 Systemverwaltung
Cmdlets zum Verwalten von Systemeinstellungen, Diensten und Benutzern.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Start-Service` | Startet einen Dienst. | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | Stoppt einen Dienst. | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | Startet das System neu. | `Restart-Computer -Force` |
| `Get-EventLog` | Ruft Einträge aus dem Ereignisprotokoll ab. | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | Legt die Skriptausführungsrichtlinie fest. | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**Beispiel**: Den Status des Windows Update-Dienstes prüfen und ihn starten, falls er gestoppt ist.
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 Netzwerkverwaltung
Cmdlets für Netzwerkkonfiguration und -diagnose.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Test-Connection` | Pingt einen Remote-Host an. | `Test-Connection google.com` |
| `Get-NetAdapter` | Listet Netzwerkadapter auf. | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | Ruft IP-Adresskonfigurationen ab. | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | Löst DNS-Namen auf. | `Resolve-DnsName www.google.com` |

**Beispiel**: Einen Server anpingen und seine DNS-Auflösung prüfen.
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 Benutzer- und Gruppenverwaltung
Cmdlets zum Verwalten lokaler Benutzer und Gruppen.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `New-LocalUser` | Erstellt ein lokales Benutzerkonto. | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | Löscht ein lokales Benutzerkonto. | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | Listet lokale Gruppen auf. | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | Fügt einen Benutzer zu einer lokalen Gruppe hinzu. | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**Beispiel**: Einen neuen lokalen Benutzer erstellen und ihn zur Gruppe "Administratoren" hinzufügen.
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Testkonto"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 Skripterstellung und Automatisierung
PowerShell glänzt bei der Skripterstellung für die Automatisierung.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Write-Output` | Gibt Daten an die Pipeline aus. | `Write-Output "Hallo, Welt!"` |
| `ForEach-Object` | Durchläuft Elemente in einer Pipeline. | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | Filtert Objekte basierend auf Bedingungen. | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | Führt Befehle auf lokalen oder Remote-Computern aus. | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | Erstellt eine geplante Aufgabe. | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**Beispiel**: Ein Skript erstellen, um laufende Prozesse in einer Datei zu protokollieren.
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 Modulverwaltung
Module erweitern die PowerShell-Funktionalität.

| Cmdlet | Beschreibung | Beispiel |
|--------|-------------|---------|
| `Get-Module` | Listet verfügbare oder importierte Module auf. | `Get-Module -ListAvailable` |
| `Import-Module` | Importiert ein Modul. | `Import-Module ActiveDirectory` |
| `Install-Module` | Installiert ein Modul aus einem Repository. | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | Sucht nach Modulen in einem Repository. | `Find-Module -Name *Azure*` |

**Beispiel**: Das PSWindowsUpdate-Modul installieren und importieren, um Windows-Updates zu verwalten.
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. Arbeiten mit Pipelines
Die Pipeline (`|`) ermöglicht das Verketten von Cmdlets, um Daten sequentiell zu verarbeiten. Zum Beispiel:
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
Dieser Befehl:
1. Ruft alle Prozesse ab.
2. Filtert jene heraus, die mehr als 100 MB Arbeitsspeicher verwenden.
3. Sortiert sie nach Speichernutzung in absteigender Reihenfolge.
4. Wählt die Top-5-Prozesse aus und zeigt deren Namen und Speichernutzung an.

---

## 4. Variablen, Schleifen und Bedingungen
PowerShell unterstützt Skriptkonstrukte für die Automatisierung.

### Variablen
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "Log-Pfad ist $path"
```

### Schleifen
- **ForEach-Object**:
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **For-Schleife**:
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Iteration $i" }
```

### Bedingungen
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update wird ausgeführt."
} else {
    Write-Output "Windows Update ist gestoppt."
}
```

---

## 5. Fehlerbehandlung
Verwenden Sie `Try`, `Catch` und `Finally` für robuste Skripte.
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Fehler: $($_.Exception.Message)"
}
Finally {
    Write-Output "Vorgang abgeschlossen."
}
```

---

## 6. Remote-Verwaltung
PowerShell unterstützt die Remote-Administration mit `Invoke-Command` und `Enter-PSSession`.

**Beispiel**: Einen Befehl auf einem Remote-Computer ausführen.
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**Beispiel**: Eine interaktive Remote-Sitzung starten.
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. Praktisches Skriptbeispiel
Nachfolgend ein Beispielskript zur Überwachung des Festplattenspeichers, das eine Warnung ausgibt, wenn die Nutzung 80 % überschreitet.

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Warnung: Disk $($disk.Number) ist zu $("{0:N2}" -f (100 - $freeSpacePercent))% belegt."
    }
}
```

---

## 8. Tipps für eine effektive PowerShell-Nutzung
- **Verwenden Sie Aliase für Geschwindigkeit**: Gebräuchliche Aliase wie `dir` (`Get-ChildItem`), `ls` (`Get-ChildItem`) oder `gci` (`Get-ChildItem`) sparen Zeit in interaktiven Sitzungen.
- **Get-Help**: Verwenden Sie `Get-Help <Cmdlet>` für eine detaillierte Dokumentation (z.B. `Get-Help Get-Process -Full`).
- **Update-Help**: Halten Sie Hilfedateien mit `Update-Help` aktuell.
- **Profile**: Passen Sie Ihre PowerShell-Umgebung an, indem Sie `$PROFILE` bearbeiten (z.B. `notepad $PROFILE`).
- **Tab-Vervollständigung**: Drücken Sie `Tab`, um Cmdlets, Parameter und Pfade automatisch zu vervollständigen.
- **Ausführliche Ausgabe verwenden**: Fügen Sie Cmdlets `-Verbose` hinzu, um detaillierte Ausführungsinformationen zu erhalten.

---

## 9. Zusätzliche Ressourcen
- **Offizielle Dokumentation**: [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell Gallery**: [PowerShell Gallery](https://www.powershellgallery.com/) für Module.
- **Community**: Prüfen Sie Beiträge auf X oder in Foren wie Stack Overflow für Echtzeit-Tipps und Skripte.
- **Lernmaterial**: Bücher wie *PowerShell in Depth* oder *Learn PowerShell in a Month of Lunches*.

---

PowerShell ist eine leistungsstarke Skriptsprache und Befehlszeilen-Shell, die von Microsoft entwickelt wurde. Sie wird häufig für die Aufgabenautomatisierung und Konfigurationsverwaltung verwendet. Hier sind einige häufig verwendete PowerShell-Befehle neben `Get-NetTCPConnection`:

1.  **Get-Process**: Ruft Informationen über die Prozesse ab, die auf dem lokalen Computer oder einem Remotecomputer ausgeführt werden.
2.  **Get-Service**: Ruft die Dienste auf einem lokalen oder Remotecomputer ab.
3.  **Get-EventLog**: Ruft Ereignisse aus Ereignisprotokollen ab, einschließlich Anwendungs-, Sicherheits- und Systemprotokollen.
4.  **Get-ChildItem**: Ruft die Elemente und untergeordneten Elemente an einem oder mehreren angegebenen Speicherorten ab (ähnlich wie `dir` in der Eingabeaufforderung).
5.  **Get-Content**: Ruft den Inhalt des Elements am angegebenen Speicherort ab (ähnlich wie `type` in der Eingabeaufforderung).
6.  **Set-ExecutionPolicy**: Ändert die Benutzereinstellung für die PowerShell-Ausführungsrichtlinie.
7.  **Invoke-Command**: Führt Befehle auf lokalen und Remotecomputern aus.
8.  **New-Item**: Erstellt ein neues Element, z.B. eine Datei oder ein Verzeichnis.
9.  **Remove-Item**: Löscht die angegebenen Elemente.
10. **Copy-Item**: Kopiert ein Element von einem Speicherort an einen anderen.
11. **Move-Item**: Verschiebt ein Element von einem Speicherort an einen anderen.
12. **Rename-Item**: Benennt ein Element in einem PowerShell-Provider-Namespace um.
13. **Get-Help**: Zeigt Informationen zu PowerShell-Befehlen und Konzepten an.
14. **Select-Object**: Wählt bestimmte Eigenschaften eines Objekts oder einer Gruppe von Objekten aus.
15. **Where-Object**: Wählt Objekte aus einer Sammlung basierend auf ihren Eigenschaftswerten aus.
16. **Sort-Object**: Sortiert Objekte nach Eigenschaftswerten.
17. **Export-Csv**: Konvertiert Objekte in eine Reihe von CSV-Zeichenfolgen und speichert die Zeichenfolgen in einer Datei.
18. **Import-Csv**: Importiert eine CSV-Datei und konvertiert sie in Objekte.
19. **Start-Process**: Startet einen oder mehrere Prozesse auf dem lokalen Computer.
20. **Stop-Process**: Stoppt einen oder mehrere laufende Prozesse.

Diese Befehle sind nur einige Beispiele für das, was Sie mit PowerShell tun können. Die Sprache ist hochgradig erweiterbar, und Sie können benutzerdefinierte Cmdlets und Skripte erstellen, um komplexe Aufgaben zu automatisieren.