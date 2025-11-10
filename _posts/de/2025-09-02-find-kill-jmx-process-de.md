---
audio: false
generated: true
image: false
lang: de
layout: post
title: JMX-Port-Prozess finden und beenden
translated: true
type: note
---

Verstanden — Sie möchten überprüfen, welches Java-Programm unter Windows einen **JMX-Remote-Agent** auf Port `9091` geöffnet hat und es gegebenenfalls beenden. So gehen Sie Schritt für Schritt vor:

---

### 1. Prozess finden, der Port 9091 verwendet

Öffnen Sie die **Eingabeaufforderung** (wenn möglich als Administrator) und führen Sie aus:

```cmd
netstat -ano | findstr :9091
```

Das zeigt etwa:

```
  TCP    0.0.0.0:9091    0.0.0.0:0    ABHÖREND    12345
```

* Die letzte Spalte (`12345` hier) ist die **PID (Prozess-ID)**.

---

### 2. Herausfinden, zu welchem Programm diese PID gehört

Ordnen Sie nun die PID dem tatsächlichen Programm zu:

```cmd
tasklist /FI "PID eq 12345"
```

Das zeigt etwa:

```
Image Name                     PID   Session Name        Mem Usage
========================= ======== ================ ============
java.exe                    12345 Console           200,000 K
```

Falls es sich um einen Java-Prozess handelt, können Sie noch mehr Details abrufen:

```cmd
wmic process where processid=12345 get CommandLine
```

Das gibt die **Kommandozeile** aus, mit der die JVM gestartet wurde – Sie sehen die JMX-Flags (`-Dcom.sun.management.jmxremote.port=9091`), was bestätigt, dass es sich um den JMX-Remote-Agent handelt.

---

### 3. Prozess beenden

Wenn Sie bestätigt haben, dass ein Stopp sicher ist, können Sie ihn beenden:

```cmd
taskkill /PID 12345 /F
```

* `/PID` gibt die Prozess-ID an.
* `/F` erzwingt die Beendigung.

---

### 4. Alternative mit PowerShell

Wenn Sie PowerShell bevorzugen, können Sie ausführen:

```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess
```

Um direkt zu beenden:

```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess -Force
```

---

🔎 Zusammenfassung:

1. `netstat -ano | findstr :9091` → PID ermitteln
2. `tasklist /FI "PID eq <PID>"` → Programm anzeigen
3. `wmic process where processid=<PID> get CommandLine` → JVM-Flags anzeigen
4. `taskkill /PID <PID> /F` → beenden

---

Möchten Sie, dass ich Ihnen auch zeige, wie Sie **mehrere JVMs gleichzeitig** auf JMX-Agent-Ports überprüfen können (um zu sehen, ob andere auf Ports wie 9090, 9999 usw. laufen)?