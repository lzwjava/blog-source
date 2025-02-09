---
audio: true
lang: de
layout: post
title: SSH-Konfiguration
translated: true
---

Diese `ssh-config`-Datei konfiguriert das Verhalten des SSH-Clients.  Schauen wir uns jeden Teil genauer an:

- `Host * !192.*.*.*`: Dieser Abschnitt gilt für alle Hosts *außer* diejenigen, die dem Muster `192.*.*.*` entsprechen (typischerweise lokale Netzwerkadressen).
    - `ProxyCommand corkscrew localhost 7890 %h %p`: Dies ist der wichtigste Teil. Er weist SSH an, das Programm `corkscrew` zu verwenden, um eine Verbindung zum Zielhost herzustellen.
        - `corkscrew`: Ein Tool, mit dem Sie SSH-Verbindungen über HTTP- oder HTTPS-Proxies tunneln können.
        - `localhost 7890`: Gibt die Adresse (`localhost`) und den Port (`7890`) des Proxyservers an. Dies setzt voraus, dass ein Proxyserver auf Ihrem lokalen Rechner läuft, der auf Port 7890 lauscht (z. B. Shadowsocks, ein SOCKS-Proxy oder eine andere Tunneling-Lösung).
        - `%h`: Eine spezielle SSH-Variable, die in den Zielhostname expandiert, zu dem Sie eine Verbindung herstellen möchten.
        - `%p`: Eine weitere SSH-Variable, die in den Zielport expandiert (normalerweise 22 für SSH).
    - Zusammenfassend konfiguriert dieser `Host`-Block SSH so, dass für alle Verbindungen *außer* denjenigen zum lokalen Netzwerk der `corkscrew`-Proxy verwendet wird.

- `Host *`: Dieser Abschnitt gilt für *alle* Hosts.
    - `UseKeychain yes`: Unter macOS weist dies SSH an, SSH-Schlüssel in Ihrem Schlüsselbund zu speichern und abzurufen, sodass Sie nicht jedes Mal Ihr Passwort eingeben müssen.
    - `AddKeysToAgent yes`: Dies fügt Ihre SSH-Schlüssel automatisch dem SSH-Agent hinzu, sodass Sie sie nach jedem Neustart nicht manuell hinzufügen müssen.
    - `IdentityFile ~/.ssh/id_rsa`: Gibt den Pfad zu Ihrer privaten SSH-Schlüsseldatei an. `~/.ssh/id_rsa` ist der Standardpfad für den privaten RSA-Schlüssel.

**Im Wesentlichen konfiguriert diese Einstellung einen Proxy für alle SSH-Verbindungen außer denen im lokalen Netzwerk und konfiguriert die Schlüsselverwaltung für mehr Komfort.**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
