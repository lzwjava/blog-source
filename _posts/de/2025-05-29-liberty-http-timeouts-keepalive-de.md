---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Konfiguration von Liberty-HTTP-Zeitüberschreitungen und Keep-Alive
translated: true
type: note
---

### Konfiguration der Keep-Alive-Einstellungen

WebSphere Liberty Profile verwaltet HTTP-Keep-Alive-Verbindungen über das `<httpEndpoint>`-Element in der `server.xml`. Dieses Element steuert persistente Verbindungen, um Latenz und Overhead zu reduzieren.

- **keepAlive**: Aktiviert oder deaktiviert Keep-Alive. Auf `true` (Standard) setzen, um mehrere Anfragen über eine einzelne Verbindung zu erlauben.
- **keepAliveTimeout**: Definiert, wie lange (in Sekunden) der Server wartet, bevor er eine inaktive Keep-Alive-Verbindung schließt. Standard sind 30 Sekunden.

Zur Konfiguration fügen Sie das `<httpEndpoint>`-Element unter dem `<server>`-Hauptelement in der `server.xml` hinzu oder ändern es. Beispiel:

```xml
<server>
    <!-- Andere Konfigurationen -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        keepAlive="true"
        keepAliveTimeout="60"/>
</server>
```

Starten Sie den Server neu, damit die Änderungen wirksam werden. TCP-Level-Keep-Alives können bei Bedarf über `<tcpOptions>` angepasst werden, aber HTTP-Keep-Alive ist für Web-Traffic üblicher.

### Konfiguration der Timeout-Einstellungen

Timeouts in Libertys `server.xml` beziehen sich primär auf Verbindungs-Timeouts unter `<httpEndpoint>` und steuern, wie lange der Server auf Operationen wartet. Diese gelten für die HTTP-Kommunikation.

- **connectionTimeout**: Maximale Zeit (in Sekunden) zum Aufbau einer neuen Verbindung. Standard sind 60 Sekunden.
- **readTimeout**: Maximale Zeit (in Sekunden), um auf eingehende Daten während einer Anfrage zu warten. Standard sind 60 Sekunden.
- **writeTimeout**: Maximale Zeit (in Sekunden), um auf das Senden ausgehender Daten zu warten. Standard sind 60 Sekunden.

Sitzungsspezifische Timeouts (z.B. für Web-App-Sitzungen) werden in der `web.xml` oder über `<sessionManager>` in der `server.xml` konfiguriert, nicht direkt in `<httpEndpoint>`.

Beispielkonfiguration in `server.xml`:

```xml
<server>
    <!-- Andere Konfigurationen -->
    <httpEndpoint id="defaultHttpEndpoint" host="*"
        connectionTimeout="30"
        readTimeout="120"
        writeTimeout="120"/>
</server>
```

Passen Sie die Werte basierend auf den Anforderungen Ihrer Anwendung an, z.B. höhere Timeouts für langsame Netzwerke oder langlaufende Anfragen. Überwachen Sie die Logs auf Timeout-bezogene Fehler und starten Sie den Server nach Änderungen neu. Weitere Details finden Sie in der [IBM Liberty Dokumentation zu HTTP-Endpunkten](https://www.ibm.com/docs/en/was-liberty/23.0.0?topic=configuration-http-endpoint-running-liberty).