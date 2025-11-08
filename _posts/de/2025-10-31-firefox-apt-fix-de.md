---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung des Firefox-APT-Repository-Fehlers
translated: true
type: note
---

Der Fehler, den Sie sehen, betrifft speziell das Mozilla Firefox APT-Repository (`https://packages.mozilla.org/apt`), bei dem der Abruf der `binary-all/Packages`-Indexdatei mit einem 400 Bad Request fehlschlägt. Dies ist ein bekanntes, intermittierendes Problem, das von anderen Ubuntu/Debian-Nutzern gemeldet wurde und oft mit Proxy-Konfigurationen zusammenhängt (Ihr lokaler Proxy unter `127.0.0.1:7890` deutet auf ein Tool wie Clash, V2Ray oder ähnliches hin, das HTTPS-Anfragen für APT verfälschen kann). Die gute Nachricht ist, dass APT den Fehler ignoriert und zwischengespeicherte/alte Indexe verwendet, sodass Systemupdates nicht blockiert werden – aber es kann verhindern, dass die neuesten Firefox-Deb-Pakete bezogen werden.

### Schnelle Lösungsansätze (in dieser Reihenfolge)
1.  **APT-Cache leeren** (dies behebt beschädigte oder veraltete Indexdateien und hat das Problem bei mehreren Nutzern gelöst):
    ```
    sudo apt clean
    sudo apt update
    ```

2.  **Proxy für APT temporär umgehen** (da der 400-Fehler oft von Proxy-Interferenz mit dem HTTPS des Repositories stammt):
    ```
    unset http_proxy https_proxy all_proxy
    sudo -E apt update
    ```
    - Führen Sie dies in derselben Terminal-Sitzung aus. Wenn es funktioniert, können Sie es dauerhaft machen, indem Sie die `unset`-Zeilen in Ihre `~/.bashrc` einfügen (oder direkt vor APT-Befehlen) oder die Proxy-App kurzzeitig deaktivieren.
    - Wenn Ihr Proxy systemweit gesetzt ist (z.B. in `/etc/environment`), bearbeiten Sie diese Datei, um APT auszuschließen, oder kommentieren Sie die Zeilen vorübergehend aus.

3.  **Proxy global für APT deaktivieren** (wenn der obige Ansatz funktioniert, Sie aber eine dauerhafte Lösung bevorzugen):
    ```
    echo 'Acquire::http::Proxy "";
    Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
    sudo apt update
    ```
    - Dies weist APT an, Proxys vollständig zu ignorieren. Sie können dies rückgängig machen, indem Sie `/etc/apt/apt.conf.d/99no-proxy` löschen.

### Falls Sie das neueste Firefox ohne das Repository benötigen
Wenn das Repository weiterhin fehlschlägt und Sie einfach ein aktualisiertes Firefox wollen:
-   **Zu Snap wechseln** (Ubuntus Standard, einfache Updates, kein Repository-Aufwand):
    ```
    sudo snap install firefox
    ```
-   **Oder Flatpak** (falls bevorzugt):
    ```
    sudo apt install flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.mozilla.firefox
    ```

### Prävention/Hinweise
-   Das Mozilla-Repository ist inoffiziell, um aktuellste Firefox-Debs zu beziehen – erwägen Sie, bei der Snap-Version von Ubuntu zu bleiben, es sei denn, Sie benötigen spezifisch das Deb-Paket.
-   Wenn nichts davon funktioniert, überprüfen Sie Ihre Proxy-Logs (z.B. Clash-Dashboard) auf abgelehnte Anfragen an `packages.mozilla.org` oder testen Sie ohne den Proxy.
-   Führen Sie `sudo apt update` erneut nach den Korrekturen aus, um zu überprüfen.

Wenn diese Schritte das Problem nicht lösen, teilen Sie bitte weitere Details wie Ihren Proxy-Setup oder den vollständigen Inhalt von `/etc/apt/sources.list.d/mozilla.list` für eine tiefergehende Fehlerbehebung mit.

[Ubuntu 23.10 - Update Problems](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt repository error](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)