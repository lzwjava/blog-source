---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben des Befehlsfehlers Suspend
translated: true
type: note
---

Der Fehler `sudo: suspend: command not found` zeigt an, dass der `suspend`-Befehl auf Ihrem System nicht verfügbar oder nicht installiert ist. Der `suspend`-Befehl wird typischerweise verwendet, um ein Linux-System in einen Suspend-Zustand (Ruhezustand) zu versetzen, ist aber möglicherweise nicht standardmäßig vorhanden oder hat je nach Distribution einen anderen Namen.

So können Sie das Problem beheben:

### 1. **Verwenden Sie den richtigen Befehl**
Auf vielen Linux-Distributionen lautet der Befehl zum Suspendieren des Systems nicht `suspend`, sondern einer der folgenden:

- **`systemctl suspend`**:
  Dies ist der Standardbefehl auf Systemen, die `systemd` verwenden (z.B. Ubuntu, Debian, Fedora, etc.).
  ```bash
  sudo systemctl suspend
  ```

- **`pm-suspend`**:
  Wenn Ihr System das Paket `pm-utils` verwendet, können Sie Folgendes verwenden:
  ```bash
  sudo pm-suspend
  ```
  Hinweis: Möglicherweise müssen Sie `pm-utils` installieren, falls es noch nicht vorhanden ist:
  ```bash
  sudo apt-get install pm-utils  # Für Debian/Ubuntu
  sudo dnf install pm-utils      # Für Fedora
  ```

- **`echo mem > /sys/power/state`**:
  Für einen Low-Level-Ansatz können Sie direkt in den System-Power-State schreiben:
  ```bash
  echo mem | sudo tee /sys/power/state
  ```
  Dies erfordert Root-Rechte und funktioniert möglicherweise nicht auf allen Systemen, abhängig von der Kernel-Konfiguration.

### 2. **Prüfen Sie, ob `systemd` verfügbar ist**
Da `systemctl suspend` die gebräuchlichste Methode auf modernen Linux-Distributionen ist, überprüfen Sie, ob `systemd` läuft:
```bash
pidof systemd
```
Wenn dies eine PID zurückgibt, verwendet Ihr System `systemd` und `systemctl suspend` sollte funktionieren. Wenn nicht, müssen Sie möglicherweise `pm-suspend` oder eine andere Methode verwenden.

### 3. **Installieren Sie fehlende Tools**
Wenn weder `systemctl` noch `pm-suspend` verfügbar ist, müssen Sie möglicherweise das entsprechende Paket installieren:
- Für Ubuntu/Debian:
  ```bash
  sudo apt-get update
  sudo apt-get install pm-utils
  ```
- Für Fedora:
  ```bash
  sudo dnf install pm-utils
  ```

### 4. **Berechtigungen überprüfen**
Stellen Sie sicher, dass Sie über ausreichende Berechtigungen verfügen. Der `sudo`-Befehl legt nahe, dass Sie versuchen, ihn als Administrator auszuführen, aber überprüfen Sie nochmals, ob Ihr Benutzer in der `sudoers`-Datei enthalten ist:
```bash
sudo -l
```
Wenn Ihnen die Berechtigungen fehlen, müssen Sie möglicherweise Ihren Systemadministrator kontaktieren.

### 5. **Alternative: Verwenden Sie die Desktop-Umgebung**
Wenn Sie eine grafische Desktop-Umgebung ausführen (z.B. GNOME, KDE), können Sie das System über die GUI suspendieren (z.B. durch Klicken auf das Powermenü und Auswahl von "Suspend"). Alternativ können Sie verwenden:
- Für GNOME:
  ```bash
  gnome-session-quit --power-off
  ```
- Für KDE:
  ```bash
  qdbus org.kde.ksmserver /KSMServer org.kde.KSMServerInterface.logout 0 1 0
  ```

### 6. **Hardware-Unterstützung überprüfen**
Einige Systeme unterstützen Suspend möglicherweise aufgrund von Hardware- oder Kernel-Problemen nicht. Prüfen Sie, ob Suspend unterstützt wird:
```bash
cat /sys/power/state
```
Wenn `mem` in der Ausgabe aufgeführt ist, wird Suspend unterstützt. Wenn nicht, müssen Sie möglicherweise die Hardware oder Kernel-Einstellungen troubleshooten.

### 7. **Wenn Sie speziell den `suspend`-Befehl benötigen**
Wenn Sie nach einem bestimmten `suspend`-Befehl suchen (z.B. Teil eines benutzerdefinierten Skripts oder Pakets), ist dieser möglicherweise nicht installiert. Suchen Sie danach:
```bash
sudo apt-cache search suspend
```
Oder prüfen Sie, ob er Teil eines anderen Pakets ist. Wenn Sie ein benutzerdefiniertes Skript oder einen Alias meinen, verifizieren Sie dessen Speicherort und stellen Sie sicher, dass es ausführbar ist:
```bash
which suspend
```

### Beispiel-Workflow
So suspendieren Sie Ihr System in einem typischen Ubuntu-Setup:
```bash
sudo systemctl suspend
```
Dies sollte Ihr System in einen stromsparenden Ruhezustand versetzen. Wenn Sie das System wieder aufwecken, müssen Sie Ihre Sitzung möglicherweise entsperren.

Wenn Sie weiterhin Probleme haben, teilen Sie mir bitte Ihre Linux-Distribution und weitere Details zu Ihrem Setup mit, damit ich maßgeschneiderteren Rat geben kann.

[Ubuntu-Dokumentation zur Power Management](https://help.ubuntu.com/stable/ubuntu-help/power-suspend.html)
[systemd suspend man page](https://www.freedesktop.org/software/systemd/man/systemctl.html)