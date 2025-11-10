---
audio: false
generated: true
image: false
lang: de
layout: post
model: google/gemini-2.5-flash
title: Beheben von Docker OverlayFS-Entfernungsfehlern
translated: true
type: note
---

Der Fehler, den Sie sehen, insbesondere die Zeile:
`Error response from daemon: container ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18: driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged: readdirent merged: bad message`
deutet auf ein **Problem mit dem Docker Storage Driver**, speziell **OverlayFS (overlay2)**, hin. Dies steht oft im Zusammenhang mit einem korrupten Dateisystemzustand auf Ihrem Host-Rechner. Dies passiert normalerweise, wenn der Docker-Daemon nicht auf die Dateien des Containers zugreifen oder diese ordnungsgemäß bereinigen kann.

Hier ist ein schrittweiser Ansatz zur Behebung des Problems, beginnend mit den am wenigsten invasiven Methoden.

-----

## 1. Container stoppen und gewaltsam entfernen

Der Container `chat-mongodb` konnte nicht entfernt werden. Sie müssen diesen spezifischen Container anvisieren.

### A. Erzwingen der Entfernung

Versuchen Sie, den Container erneut zu entfernen, diesmal jedoch mit dem Force-Flag (`-f`), um sicherzustellen, dass er nicht läuft und eine aggressivere Entfernung zu erzwingen:

```bash
docker rm -f chat-mongodb
```

oder verwenden Sie die Container-ID:

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
```

### B. Docker Compose Stack stoppen

Wenn der Container Teil eines größeren Stacks ist, den Sie abbauen möchten (was die `[+] Running 3/3`-Meldung nahelegt), versuchen Sie, die Dienste zuerst ordnungsgemäß zu stoppen, bevor Sie die Entfernung erneut versuchen:

```bash
docker compose stop
# Dann versuchen Sie den ursprünglichen Befehl erneut
# z.B. docker compose down
```

-----

## 2. Docker-Daemon neu starten

Ein einfacher Neustart des Docker-Dienstes kann oft vorübergehende Storage-Driver-Fehler und Lock-Dateien bereinigen.

### Für Linux-Systeme (mit systemd):

```bash
sudo systemctl restart docker
```

### Für Docker Desktop (macOS/Windows):

1.  Klicken Sie auf das **Docker-Symbol** in Ihrer Systemleiste / Menüleiste.
2.  Navigieren Sie zu **Troubleshoot** (oder **Settings** $\rightarrow$ **Daemon** $\rightarrow$ **Restart**).
3.  Klicken Sie auf **Restart**.

Versuchen Sie nach dem Neustart erneut, den Container zu entfernen.

-----

## 3. Manuelles Bereinigen des korrupten Verzeichnisses

**⚠️ WARNUNG:** Dieser Schritt beinhaltet die direkte Manipulation der internen Dateistruktur von Docker und sollte **nur als letzter Ausweg** und **während der Docker-Daemon GESTOPPT ist** durchgeführt werden. Eine falsche manuelle Löschung kann weitere Korruption verursachen.

Der Fehler verweist auf ein spezifisches Verzeichnis innerhalb des OverlayFS-Speichers: `/var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged`.

1.  **Docker-Daemon stoppen:**

    ```bash
    sudo systemctl stop docker
    ```

2.  **Problemverzeichnis manuell entfernen:**

    ```bash
    # Entfernen Sie nur das Verzeichnis, das in IHRER Fehlermeldung angezeigt wird
    sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f
    ```

    *Wenn Sie das exakte Verzeichnis nicht finden können, müssen Sie möglicherweise eine allgemeinere Bereinigung versuchen (siehe nächster Schritt).*

3.  **Docker-Daemon starten:**

    ```bash
    sudo systemctl start docker
    ```

4.  **Versuchen Sie erneut, den Container/Stack zu entfernen.**

-----

## 4. Nicht verwendete Daten bereinigen

Wenn die obigen Schritte fehlschlagen, können Sie die integrierten Bereinigungsbefehle von Docker verwenden. Dieser Befehl entfernt alle gestoppten Container, alle nicht verwendeten Netzwerke, alle ungenutzten Images und den Build-Cache.

```bash
docker system prune
```

**Hinweis:** Dieser Befehl fordert eine Bestätigung an und entfernt Daten, die Sie möglicherweise behalten möchten, wenn sie nicht aktiv verwendet werden (z.B. gestoppte Container). Verwenden Sie `-a`, um alle ungenutzten Images zu entfernen (nicht nur die ungenutzten ohne Tag).