---
audio: false
generated: true
lang: de
layout: post
title: 'PowerShell: Verwendung von Get-NetTCPConnection'
translated: true
type: note
---

Das `Get-NetTCPConnection`-Cmdlet in PowerShell ruft Informationen über TCP-Verbindungen auf einem Windows-System ab. Es ist Teil des `NetTCPIP`-Moduls, das unter Windows 8/Windows Server 2012 und höher verfügbar ist. Nachfolgend finden Sie eine kurze Anleitung zur Verwendung:

### Grundlegende Verwendung
Führen Sie `Get-NetTCPConnection` aus, um alle aktiven TCP-Verbindungen aufzulisten:

```powershell
Get-NetTCPConnection
```

Dies liefert Details wie LocalAddress, LocalPort, RemoteAddress, RemotePort, State und OwningProcess.

### Häufig verwendete Parameter
- **-State**: Filtert nach Verbindungsstatus (z.B. Established, Listening, TimeWait).
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**: Filtert nach lokaler Portnummer.
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**: Filtert nach remote IP-Adresse.
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**: Filtert nach remote Port.
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**: Filtert nach der Prozess-ID (PID), der die Verbindung besitzt.
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### Filter kombinieren
Sie können Parameter für spezifischere Ergebnisse kombinieren:
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### Bestimmte Eigenschaften anzeigen
Verwenden Sie `Select-Object`, um nur gewünschte Eigenschaften anzuzeigen:
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Prozessdetails ermitteln
Um den Prozess hinter einer Verbindung zu identifizieren, kombinieren Sie es mit `Get-Process`:
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### Ausgabe sortieren und formatieren
Sortieren Sie Ergebnisse (z.B. nach LocalPort) und formatieren Sie sie als Tabelle:
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Praktische Beispiele
1. **Alle lauschenden Verbindungen auflisten:**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **Verbindungen zu einem bestimmten Remote-Server finden:**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **Überprüfen, welcher Prozess einen bestimmten Port verwendet:**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### Hinweise
- **Adminrechte**: Einige Details (z.B. OwningProcess für Systemprozesse) erfordern möglicherweise das Ausführen von PowerShell als Administrator.
- **IPv4/IPv6**: Das Cmdlet verarbeitet sowohl IPv4- als auch IPv6-Verbindungen.
- **Ergebnisse exportieren**: Speichern Sie die Ausgabe mit `Export-Csv` in einer Datei:
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

Für weitere Details führen Sie aus:
```powershell
Get-Help Get-NetTCPConnection -Full
```

Wenn Sie spezifische Beispiele benötigen oder einen bestimmten Anwendungsfall haben, lassen Sie es mich wissen!