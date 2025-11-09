---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Vermeidung von Docker-Daemon-Proxy-Schleifen
translated: true
type: note
---

### Warum `"no-proxy": "localhost,127.0.0.1,.local"` in Docks `daemon.json` entscheidend ist

Wenn Sie den Docker-Daemon mit Proxy-Einstellungen wie `"http-proxy": "http://localhost:7890"` konfigurieren (üblich für lokale Tools wie Clash), wendet der Daemon diese Regeln standardmäßig auf **allen** ausgehenden Netzwerkverkehr an. Dies schließt Verbindungen zu externen Registries ein (z. B. `registry-1.docker.io` zum Pullen von Images wie `hello-world`).

Ohne die `no-proxy`-Direktive versucht der Docker-Daemon jedoch auch **lokale Verbindungen** – wie den anfänglichen TCP-Handshake zu Ihrem Proxy-Server selbst unter `localhost:7890` – über denselben Proxy zu routen. Dies erzeugt einen klassischen **Proxy-Loop**:

1.  Docker muss ein Image von `registry-1.docker.io` abrufen.
2.  Es versucht, eine Verbindung über den Proxy unter `localhost:7890` herzustellen.
3.  Um jedoch `localhost:7890` zu erreichen, greifen die Proxy-Einstellungen erneut, was Docker zwingt, sich... über den Proxy unter `localhost:7890` zu verbinden.
4.  Diese unendliche Rekursion scheitert auf TCP-Ebene, weil der Proxy keine Verbindung zu sich selbst proxyn kann (es führt zu einer selbstreferenziellen Schleife ohne Auflösung).
5.  Die Verbindung bricht unerwartet ab, was zu dem `proxyconnect tcp: EOF`-Fehler führt (EOF bedeutet "end of file" und signalisiert einen vorzeitigen Abschluss während der Proxy-Aushandlung/des Handshakes).

Durch das Hinzufügen von `"no-proxy": "localhost,127.0.0.1,.local"` wird dem Daemon explizit mitgeteilt, den Proxy für Datenverkehr zu **umgehen**, der für folgendes bestimmt ist:
-   `localhost` (der Loopback-Hostname Ihres Rechners),
-   `127.0.0.1` (IPv4-Loopback-Adresse),
-   `.local`-Domains (üblich für mDNS/lokale Netzwerkauflösung).

Dies ermöglicht es Docker, sich **direkt** mit dem Proxy-Server auf localhost zu verbinden, ohne sich selbst zu durchlaufen. Sobald die Verbindung hergestellt ist, kann der Proxy die externe Anfrage an die Docker-Registry ordnungsgemäß abwickeln (z. B. via HTTP CONNECT für HTTPS-Datenverkehr).

Kurz gesagt: Es verhindert, dass der Daemon "den Proxy proxt", stellt den lokalen Proxy-Zugriff sicher und leitet internetgebundenen Datenverkehr (wie Image-Pulls) weiterhin darüber.

Wenn Ihr Setup andere lokale Dienste umfasst (z. B. interne Registries oder lokal kommunizierende Container), kann das Erweitern von `no-proxy` um diese Domains/IPs ähnliche Probleme verhindern.

[Docker Daemon Proxy Configuration](https://docs.docker.com/engine/daemon/proxy/)  
[Docker Proxy Settings Forum Discussion](https://forums.docker.com/t/proxy-settings-for-the-docker-daemon/132089)  
[Docker Proxy Guide for Corporate Firewalls](https://www.datacamp.com/tutorial/docker-proxy)