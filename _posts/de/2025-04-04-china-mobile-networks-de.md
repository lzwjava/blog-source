---
audio: false
generated: true
lang: de
layout: post
title: Warum Git-Operationen in chinesischen Mobilfunknetzen fehlschlagen
translated: true
type: note
---

Dies ist ein häufiges Problem bei der Verwendung bestimmter Mobilfunknetze in China, insbesondere mit Diensten wie Git, die auf bestimmten Ports und Protokollen angewiesen sind. Hier ist eine Aufschlüsselung, warum es passiert und wie man es beheben kann:

**Warum Git-Operationen in chinesischen Mobilfunknetzen fehlschlagen:**

*   **Port-Blockierung/Drosselung:**
    *   Mobilfunknetzbetreiber in China setzen manchmal Traffic Shaping oder Port-Blockierung ein, insbesondere für nicht standardmäßige Ports, die von Git verwendet werden (wie SSH-Port 22). Dies geschieht oft zur Verwaltung der Netzwerkbandbreite oder aus Sicherheitsgründen.
    *   Selbst wenn Port 22 nicht vollständig blockiert ist, könnte er stark gedrosselt werden, was zu extrem langsamen Verbindungen oder Timeouts führt, die als "hängende" Git-Operationen erscheinen.
*   **DNS-Probleme:**
    *   Während Sie auf Websites wie GitHub und Google zugreifen können, sind Git-Operationen auf die Auflösung bestimmter Hostnamen (z.B. `github.com`) über DNS angewiesen. Wenn die DNS-Auflösung langsam oder unzuverlässig ist, kann dies dazu führen, dass Git hängt.
*   **Paketverlust/Latenz:**
    *   Mobilfunknetze, insbesondere wenn sie als Hotspots genutzt werden, können eine höhere Latenz und Paketverluste im Vergleich zu kabelgebundenen Verbindungen aufweisen. Dies kann die von Git verwendete SSH-Verbindung unterbrechen und zu Fehlern führen.
*   **Firewall-Interferenz:**
    *   Chinas "Great Firewall" kann SSH-Verbindungen stören, selbst wenn sie nicht explizit blockiert sind. Die Deep Packet Inspection der Firewall kann manchmal Verbindungsinstabilität verursachen.
*   **MTU-Probleme:**
    *   Probleme mit der Maximum Transmission Unit (MTU) können Probleme bei der Datenübertragung verursachen, und Mobilfunknetze haben manchmal kleinere MTU-Werte als kabelgebundene Netze.

**Wie man Git-Push/Pull-Probleme in chinesischen Mobilfunknetzen behebt:**

1.  **Verwenden Sie HTTPS anstelle von SSH:**
    *   Git über HTTPS verwendet Port 443, der typischerweise für Webverkehr offen ist. Dies ist die zuverlässigste Problemumgehung.
    *   Um Ihr Git-Remote auf HTTPS umzustellen:
        *   Öffnen Sie Ihr Terminal.
        *   Navigieren Sie zu Ihrem Git-Repository.
        *   Führen Sie den folgenden Befehl aus und ersetzen Sie `your_username` und `your_repository` durch Ihre GitHub-Daten:
            ```bash
            git remote set-url origin https://github.com/your_username/your_repository.git
            ```
    *   Wenn Sie Benutzername und Passwort eingeben müssen, können Sie den Git Credential Helper verwenden oder ein Personal Access Token nutzen.
2.  **Verwenden Sie einen VPN:**
    *   Ein zuverlässiger VPN kann Netzwerkeinschränkungen umgehen und eine stabilere Verbindung bieten.
    *   Verbinden Sie sich mit einem VPN-Server außerhalb Chinas, bevor Sie Git-Operationen versuchen.
    *   Seien Sie sich bewusst, dass auch VPNs Instabilität und Geschwindigkeitsprobleme aufweisen können.
3.  **SSH-Port konfigurieren (falls SSH notwendig ist):**
    *   Wenn Sie SSH verwenden müssen, versuchen Sie, Git so zu konfigurieren, dass es einen anderen Port (z.B. 443) verwendet, der weniger blockiert werden könnte.
    *   Bearbeiten Sie Ihre `~/.ssh/config`-Datei:
        ```
        Host github.com
            Hostname ssh.github.com
            Port 443
            User git
        ```
    *   Ändern Sie dann Ihre Git-Remote-URL, um `ssh.github.com` zu verwenden:
        ```bash
        git remote set-url origin git@ssh.github.com:your_username/your_repository.git
        ```
4.  **MTU-Einstellungen überprüfen:**
    *   Wenn Sie MTU-Probleme vermuten, versuchen Sie, Ihre MTU-Größe zu reduzieren.
    *   Unter macOS können Sie den Befehl `networksetup` verwenden, um die MTU anzupassen.
    *   Das Ändern der MTU ist jedoch generell ein fortgeschrittener Schritt zur Problembehebung und sollte mit Vorsicht durchgeführt werden.
5.  **DNS-Einstellungen überprüfen:**
    *   Versuchen Sie, einen öffentlichen DNS-Server zu verwenden, wie Google DNS (8.8.8.8 und 8.8.4.4) oder Cloudflare DNS (1.1.1.1 und 1.0.0.1).
    *   Sie können die DNS-Einstellungen in Ihren macOS-Netzwerkeinstellungen konfigurieren.
6.  **Einen Git-Proxy verwenden:**
    *   Wenn Sie Zugriff auf einen Proxy-Server haben, können Sie Git so konfigurieren, dass er ihn verwendet.
    *   Setzen Sie die Git-Konfigurationsvariablen `http.proxy` und `https.proxy`:
        ```bash
        git config --global http.proxy http://proxy_address:proxy_port
        git config --global https.proxy https://proxy_address:proxy_port
        ```
    *   Wenn der Proxy eine Authentifizierung benötigt, können Sie Benutzername und Passwort in die Proxy-URL aufnehmen.
7.  **Versuchen Sie, SSH über Websockets zu verwenden:**
    *   Einige Tools und Dienste ermöglichen es, SSH-Datenverkehr über Websockets zu tunneln, was hilfreich sein kann, wenn Standard-SSH-Ports blockiert sind.
    *   Dies ist eine fortgeschrittene Technik und erfordert die Einrichtung eines Servers, der SSH über Websockets unterstützt.

**Wichtige Überlegungen:**

*   Die Bedingungen in Mobilfunknetzen können erheblich variieren, daher kann das, was an einem Ort oder zu einer Zeit funktioniert, an einem anderen Ort oder zu einer anderen Zeit möglicherweise nicht funktionieren.
*   Seien Sie sich der Nutzungsbedingungen Ihres Mobilfunknetzanbieters und möglicher Einschränkungen bei der Verwendung von VPNs oder anderen Problemumgehungen bewusst.
*   HTTPS ist generell die beste Lösung für die meisten Benutzer.