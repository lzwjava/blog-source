---
audio: false
generated: true
image: false
lang: de
layout: post
model: google/gemini-2.5-flash
title: Behebung von Docker OverlayFS-Korruption auf macOS
translated: true
type: note
---

Der Fehler `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message`, den Sie sehen, weist auf eine tiefgreifende Beschädigung innerhalb des Docker-Speichermechanismus (OverlayFS) hin, die oft durch einen unterbrochenen Vorgang oder ein Problem mit dem Dateisystem des Host-Rechners verursacht wird.

Da Sie sich auf **macOS** befinden (wo Docker Desktop läuft), werden der Docker-Daemon und sein Speicher in einer dedizierten **Linux-Virtual Machine (VM)** verwaltet. Sie haben keinen direkten Zugriff auf `/var/lib/docker/overlay2` wie auf einem nativen Linux-System, was die Lösung einfacher und sicherer macht, indem Sie sich auf die Docker Desktop App selbst konzentrieren.

Hier ist die sicherste und effektivste Abfolge von Schritten, um dies unter macOS zu beheben:

-----

## 1. Container gewaltsam stoppen und entfernen

Der fehlgeschlagene Container ist `chat-mongodb` (ID: `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`). Versuchen Sie zunächst, ihn mit seinem Namen oder seiner ID gewaltsam zu entfernen.

1.  **Stoppen Sie den gesamten Stack** (um sicherzustellen, dass kein Hintergrundprozess eine Sperre hält):

    ```bash
    docker compose stop
    ```

2.  **Entfernen Sie den spezifischen Container gewaltsam** mit dem `-f` Flag:

    ```bash
    docker rm -f chat-mongodb
    # ODER mit der ID:
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **Versuchen Sie, Ihren ursprünglichen Befehl erneut auszuführen** (`docker compose down` oder gleichwertig). Wenn der Fehler weiterhin besteht, fahren Sie mit Schritt 2 fort.

-----

## 2. Docker Desktop neu starten

Ein einfacher Neustart beseitigt oft vorübergehende Sperrprobleme oder beschädigte Zustände innerhalb der internen VM.

### Option A: Über die Menüleiste (Empfohlen)

1.  Klicken Sie auf das **Docker-Wal-Symbol** in Ihrer macOS-Menüleiste.
2.  Wählen Sie **Restart**.

### Option B: Über das Terminal

Sie können die Anwendung gewaltsam beenden und wieder öffnen:

```bash
killall Docker && open /Applications/Docker.app
```

Warten Sie nach dem Neustart von Docker etwa 30 Sekunden, bis es vollständig gestartet ist, und versuchen Sie dann, Ihren ursprünglichen Befehl erneut auszuführen.

-----

## 3. Docker-Cache und ungenutzte Daten bereinigen (Prune)

Wenn der Neustart fehlschlägt, kann ein umfassender Bereinigungsbefehl oft tiefere Beschädigungsprobleme beheben, indem er ungenutzte oder "verwaiste" Komponenten entfernt, die mit dem Fehler in Verbindung stehen könnten.

**WARNUNG:** Dieser Befehl entfernt alle gestoppten Container, ungenutzten Netzwerke und verwaisten Images. Wenn Sie Container haben, die Sie gestoppt (aber nicht entfernt) aufbewahren möchten, sichern Sie diese oder überspringen Sie diesen Schritt.

Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
docker system prune -a --volumes
```

  * **`-a`** (all) entfernt alle ungenutzten Images (nicht nur verwaiste).
  * **`--volumes`** entfernt ungenutzte anonyme Volumes (die die Quelle der `overlay2`-Beschädigung sein könnten).

Sie werden zur Bestätigung aufgefordert. Geben Sie `y` ein und drücken Sie die Eingabetaste. Nachdem der Prune-Vorgang abgeschlossen ist, versuchen Sie, Ihren ursprünglichen Befehl erneut auszuführen.

-----

## 4. Docker Desktop auf Werkseinstellungen zurücksetzen

Dies ist der **letzte Ausweg**, da dabei **alle Ihre Container, Images und Volumes gelöscht werden** (einschließlich aller lokalen Daten, die Sie in nicht eingebundenen Volumes gespeichert haben). Er erzwingt einen komplett neuen Start der internen Docker-VM.

1.  Klicken Sie auf das **Docker-Wal-Symbol** in Ihrer macOS-Menüleiste.
2.  Gehen Sie zu **Settings (oder Preferences)** $\rightarrow$ **Troubleshoot**.
3.  Klicken Sie auf **Reset to factory settings...**

Nach dem Reset startet Docker mit einem sauberen Zustand neu, und Sie sollten in der Lage sein, Ihren `docker compose up`-Befehl auszuführen, um Ihre Umgebung neu aufzubauen.