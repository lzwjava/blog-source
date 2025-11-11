---
audio: false
generated: true
lang: de
layout: post
title: Installieren von .deb-Paketen unter Ubuntu
translated: true
type: note
---

Wenn Sie eine `.deb`-Datei auf Ihrem Ubuntu-System heruntergeladen haben und diese installieren möchten, gibt es einige einfache Methoden. Im Folgenden erkläre ich den empfohlenen Weg über das Terminal sowie eine grafische Option, falls Sie eine Point-and-Click-Lösung bevorzugen.

### **Methode 1: Installation über das Terminal (Empfohlen)**
Der einfachste und zuverlässigste Weg, eine `.deb`-Datei in Ubuntu zu installieren, ist die Verwendung des `apt`-Befehls. Dieser installiert nicht nur das Paket, sondern löst auch automatisch alle erforderlichen Abhängigkeiten. So geht's:

1. **Öffnen Sie das Terminal**: Drücken Sie `Strg + Alt + T` oder suchen Sie nach "Terminal" im Anwendungsmenü.
2. **Navigieren Sie zum Speicherort der Datei** (optional): Wenn sich Ihre `.deb`-Datei in einem bestimmten Ordner befindet (z. B. im Downloads-Ordner), wechseln Sie dorthin mit dem `cd`-Befehl. Beispiel:
   ```bash
   cd ~/Downloads
   ```
   Wenn Sie das Verzeichnis nicht wechseln möchten, können Sie im nächsten Schritt den vollständigen Pfad zur Datei angeben.
3. **Führen Sie den Installationsbefehl aus**: Verwenden Sie den folgenden Befehl und ersetzen Sie `package_name.deb` durch den tatsächlichen Namen Ihrer `.deb`-Datei:
   ```bash
   sudo apt install ./package_name.deb
   ```
   - Wenn sich die Datei in einem anderen Verzeichnis befindet, geben Sie den vollständigen Pfad an, zum Beispiel:
     ```bash
     sudo apt install /home/benutzername/Downloads/package_name.deb
     ```
   - Das `./` vor dem Dateinamen weist `apt` an, nach einer lokalen Datei zu suchen und nicht nach einem Paket in den Repositories.
4. **Geben Sie Ihr Passwort ein**: Wenn Sie dazu aufgefordert werden, geben Sie Ihr Benutzerpasswort ein und drücken Sie die Eingabetaste. Der `sudo`-Befehl benötigt Administratorrechte.
5. **Warten Sie auf die Installation**: `apt` installiert die `.deb`-Datei und lädt alle notwendigen Abhängigkeiten aus den Ubuntu-Repositories herunter. Falls Probleme auftreten (z. B. fehlende Abhängigkeiten, die nicht in den Repositories gefunden werden), werden Sie benachrichtigt.

Diese Methode funktioniert ab Ubuntu 16.04, da sie eine Funktion von `apt` verwendet, die in Version 1.1 eingeführt wurde. Sie wird empfohlen, weil sie Einfachheit mit Abhängigkeitsverwaltung kombiniert.

### **Methode 2: Installation über die grafische Oberfläche**
Wenn Sie das Terminal nicht verwenden möchten, können Sie auch die grafischen Tools von Ubuntu für `.deb`-Dateien nutzen:
1. **Suchen Sie die Datei**: Öffnen Sie Ihren Dateimanager (z. B. Nautilus) und navigieren Sie zu dem Ordner, der die `.deb`-Datei enthält (wahrscheinlich Downloads).
2. **Doppelklicken Sie auf die Datei**: Dadurch sollte die Datei automatisch im Ubuntu Software Center (oder einer ähnlichen App, abhängig von Ihrer Ubuntu-Version) geöffnet werden.
3. **Klicken Sie auf "Installieren"**: Klicken Sie im Fenster des Software Centers auf die Schaltfläche "Installieren". Sie werden möglicherweise aufgefordert, Ihr Passwort einzugeben.
4. **Warten Sie auf den Abschluss**: Die Installation wird durchgeführt und Sie erhalten eine Bestätigung, sobald sie abgeschlossen ist.

Diese Methode ist benutzerfreundlich, erfordert jedoch eine Desktop-Umgebung und bietet möglicherweise keine detaillierten Rückmeldungen, falls etwas schiefgeht.

### **Wichtige Hinweise**
- **Vertrauenswürdige Quellen**: Installieren Sie `.deb`-Dateien nur aus Quellen, denen Sie vertrauen, da sie potenziell schädlichen Code enthalten und Ihr System gefährden könnten.
- **Installation überprüfen**: Nach der Installation können Sie überprüfen, ob die Software installiert wurde, indem Sie ausführen:
  ```bash
  dpkg -l | grep package_name
  ```
  (Ersetzen Sie `package_name` durch den Namen der Software, nicht den vollständigen `.deb`-Dateinamen.)
- **Abhängigkeitsprobleme**: Wenn `apt` die Abhängigkeiten nicht auflösen kann, müssen Sie diese möglicherweise manuell suchen und installieren oder eine andere, mit Ihrem System kompatible Version der `.deb`-Datei verwenden.

### **Beispiel**
Angenommen, Sie haben eine Datei namens `vscode.deb` in Ihren Downloads-Ordner heruntergeladen. Öffnen Sie ein Terminal und führen Sie aus:
```bash
sudo apt install ~/Downloads/vscode.deb
```
Dies installiert Visual Studio Code (oder was auch immer das Paket enthält) zusammen mit seinen Abhängigkeiten.

Das war's! Sie haben Ihre `.deb`-Datei nun auf Ubuntu installiert. Lassen Sie es mich wissen, wenn Sie auf Probleme stoßen!