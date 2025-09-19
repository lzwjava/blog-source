---
audio: true
generated: false
image: false
lang: de
layout: post
title: SSH-Konfiguration
translated: true
---

Diese `ssh-config`-Datei konfiguriert das Verhalten des SSH-Clients. Lassen Sie uns jeden Teil analysieren:

-   `Host * !192.*.*.*`: Dieser Abschnitt gilt für alle Hosts *außer* für diejenigen, die dem Muster `192.*.*.*` entsprechen (in der Regel lokale Netzwerkadressen).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: Dies ist der entscheidende Teil. Er weist SSH an, das Programm `corkscrew` zu verwenden, um eine Verbindung zum Zielhost herzustellen.
        -   `corkscrew`: Ein Werkzeug, das es ermöglicht, SSH-Verbindungen durch HTTP- oder HTTPS-Proxys zu tunneln.
        -   `localhost 7890`: Gibt die Adresse (`localhost`) und den Port (`7890`) des Proxy-Servers an. Dies setzt voraus, dass auf Ihrem lokalen Computer ein Proxy-Server läuft, der auf Port 7890 hört (z.B. Shadowsocks, ein SOCKS-Proxy oder eine andere Tunnellösung).
        -   `%h`: Eine spezielle SSH-Variable, die sich auf den Ziel-Hostnamen erweitert, den Sie zu verbinden versuchen.
        -   `%p`: Eine weitere SSH-Variable, die sich auf den Zielport (normalerweise 22 für SSH) erweitert.
    - Zusammengefasst konfiguriert dieser `Host`-Block SSH so, dass es den `corkscrew`-Proxy für alle Verbindungen *außer* für diejenigen zum lokalen Netzwerk verwendet.

-   `Host *`: Dieser Abschnitt gilt für *alle* Hosts.
    -   `UseKeychain yes`: Auf macOS weist dies SSH an, SSH-Schlüssel im Keychain zu speichern und abzurufen, sodass Sie Ihr Passwort nicht jedes Mal eingeben müssen.
    -   `AddKeysToAgent yes`: Dies fügt Ihre SSH-Schlüssel automatisch dem SSH-Agent hinzu, sodass Sie sie nach jedem Neustart nicht manuell hinzufügen müssen.
    -   `IdentityFile ~/.ssh/id_rsa`: Gibt den Pfad zu Ihrer privaten SSH-Schlüsseldatei an. `~/.ssh/id_rsa` ist der Standardort für den RSA-Private-Key.

**Im Wesentlichen richtet diese Konfiguration einen Proxy für alle SSH-Verbindungen ein, außer für diejenigen im lokalen Netzwerk, und konfiguriert die Schlüsselverwaltung für den Komfort.**

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```