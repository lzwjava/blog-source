---
audio: false
generated: true
lang: de
layout: post
title: Entwicklung eines Shadowsocks-Clients mit Netty
translated: true
type: note
---

Die Entwicklung eines Shadowsocks-Clients wie Clash oder des originalen Shadowsocks-Clients mit Netty erfordert ein Verständnis des Shadowsocks-Protokolls und die Nutzung von Nettys asynchronem, ereignisgesteuertem Netzwerk-Anwendungs-Framework. Hier ist eine Aufschlüsselung der Schritte und Schlüsselkonzepte:

**1. Verständnis des Shadowsocks-Protokolls**

Bevor man sich mit Netty beschäftigt, muss man das Shadowsocks-Protokoll gründlich verstehen. Auf einer hohen Ebene umfasst es:

*   **Verbindungsaufbau:** Ein Client initiiert eine Verbindung zu einem Shadowsocks-Server.
*   **Authentifizierung und Methoden-Aushandlung:** Der Client sendet die gewählte Verschlüsselungsmethode und das Passwort zur Authentifizierung an den Server.
*   **Adresskodierung:** Der Client sendet die Zieladresse (IP-Adresse und Port) des eigentlichen Zielservers in einem spezifischen kodierten Format.
*   **Datenweiterleitung:** Nach erfolgreicher Authentifizierung und Adresskodierung werden alle nachfolgenden, zwischen Client und Shadowsocks-Server ausgetauschten Daten, mit der vereinbarten Methode verschlüsselt/entschlüsselt.

**Schlüsselaspekte des Protokolls, die Sie implementieren müssen:**

*   **Umgang mit Methode und Passwort:** Speichern und Senden der gewählten Verschlüsselungsmethode (z.B. `aes-256-cfb`, `chacha20-ietf-poly1305`) und des Passworts.
*   **Adresskodierung:** Kodieren der Zieladresse in ein spezifisches Format (Typ-Byte, Adresse, Port). Das Typ-Byte gibt an, ob es sich um eine IPv4-Adresse (0x01), eine IPv6-Adresse (0x04) oder einen Hostnamen (0x03) handelt.
*   **Verschlüsselung und Entschlüsselung:** Implementierung der gewählten Verschlüsselungs- und Entschlüsselungsalgorithmen. Bibliotheken wie `PyCryptodome` (Python) oder `Bouncy Castle` (Java) können hierbei hilfreich sein.
*   **TCP-Weiterleitung:** Einrichten eines lokalen TCP-Servers, der auf Verbindungen von Anwendungen lauscht und den Datenverkehr durch den Shadowsocks-Tunnel leitet.

**2. Einrichten eines Netty-Projekts**

Zuerst müssen Sie die Netty-Abhängigkeit in Ihr Projekt einbinden (z.B. mit Maven oder Gradle für ein Java-Projekt).

**3. Kern-Netty-Komponenten für einen Proxy-Client**

Sie werden hauptsächlich die folgenden Netty-Komponenten verwenden:

*   **`Bootstrap`:** Wird verwendet, um die Client-seitige Anwendung zu konfigurieren und zu starten.
*   **`EventLoopGroup`:** Verwaltet die Event-Loops, die die I/O-Operationen für den Client handhaben. Typischerweise verwendet man `NioEventLoopGroup` für nicht-blockierende I/O.
*   **`Channel`:** Stellt eine Netzwerkverbindung dar.
*   **`ChannelPipeline`:** Eine Kette von `ChannelHandler`s, die eingehende und ausgehende Ereignisse und Daten verarbeiten.
*   **`ChannelHandler`:** Schnittstellen, die Sie implementieren, um spezifische Ereignisse und Datentransformationen zu handhaben. Sie werden benutzerdefinierte Handler für das Shadowsocks-Protokoll erstellen.
*   **`ByteBuf`:** Nettys Puffer für die Handhabung binärer Daten.

**4. Implementierung des Shadowsocks-Protokolls mit Netty-Handlern**

Sie müssen mehrere benutzerdefinierte `ChannelHandler`s innerhalb Ihrer `ChannelPipeline` erstellen, um die Shadowsocks-Logik zu implementieren. Hier ist eine mögliche Struktur:

*   **Lokaler Proxy-Server-Handler (`ChannelInboundHandlerAdapter`):**
    *   Dieser Handler läuft auf einem lokalen Server-Socket, mit dem sich Ihre Anwendungen verbinden (z.B. `localhost:1080`).
    *   Wenn eine neue Verbindung von einer lokalen Anwendung eingeht, wird dieser Handler:
        *   Eine Verbindung zum entfernten Shadowsocks-Server herstellen.
        *   Die initiale Verbindungsanfrage (Zieladresse) an den Shadowsocks-Server weiterleiten, nachdem sie gemäß dem Protokoll kodiert wurde.
        *   Den Datenfluss zwischen der lokalen Anwendung und dem Shadowsocks-Server verwalten.

*   **Shadowsocks-Client-Encoder (`ChannelOutboundHandlerAdapter`):**
    *   Dieser Handler ist für das Kodieren der Daten verantwortlich, die an den Shadowsocks-Server gesendet werden.
    *   Er wird:
        *   Die Zieladresse gemäß dem Shadowsocks-Protokoll kodieren (Typ, Adresse, Port).
        *   Die Daten mit der gewählten Verschlüsselungsmethode verschlüsseln.

*   **Shadowsocks-Client-Decoder (`ChannelInboundHandlerAdapter`):**
    *   Dieser Handler ist für das Dekodieren der vom Shadowsocks-Server empfangenen Daten verantwortlich.
    *   Er wird:
        *   Die empfangenen Daten entschlüsseln.

*   **Remote-Server-Weiterleitungs-Handler (`ChannelInboundHandlerAdapter`):**
    *   Dieser Handler wird aufgerufen, wenn Daten vom entfernten Shadowsocks-Server empfangen werden.
    *   Er leitet die entschlüsselten Daten zurück zur ursprünglichen lokalen Anwendung.

**5. Beispielstruktur der Netty-Pipeline**

Hier ist ein vereinfachtes Beispiel, wie Ihre `ChannelPipeline` für die Verbindung zum Shadowsocks-Server aussehen könnte:

```java
public class ShadowsocksClientInitializer extends ChannelInitializer<SocketChannel> {

    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClientInitializer(String serverAddress, int serverPort, String method, String password) {
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // Outbound-Handler (Daten, die zum Shadowsocks-Server gehen)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // Inbound-Handler (Daten, die vom Shadowsocks-Server kommen)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

Und für den lokalen Proxy-Server:

```java
public class LocalProxyInitializer extends ChannelInitializer<SocketChannel> {

    private final String shadowsocksServerAddress;
    private final int shadowsocksServerPort;
    private final String method;
    private final String password;

    public LocalProxyInitializer(String shadowsocksServerAddress, int shadowsocksServerPort, String method, String password) {
        this.shadowsocksServerAddress = shadowsocksServerAddress;
        this.shadowsocksServerPort = shadowsocksServerPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // Handler, um die Verbindung zum Shadowsocks-Server zu initiieren und Daten weiterzuleiten
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. Wichtige Implementierungsdetails**

*   **Implementierung der Verschlüsselung/Entschlüsselung:** Sie müssen die gewählten Verschlüsselungs- und Entschlüsselungsalgorithmen in Ihrem `ShadowsocksClientEncoder` und `ShadowsocksClientDecoder` implementieren. Dies wird wahrscheinlich die Verwendung externer Bibliotheken beinhalten. Seien Sie vorsichtig mit Schlüsselableitung und Initialisierungsvektoren, falls dies von der gewählten Methode verlangt wird.
*   **Adresskodierung in `LocalProxyHandler`:** Wenn der `LocalProxyHandler` die initiale Verbindungsanfrage von der lokalen Anwendung empfängt, muss er die Zieladresse und den Port extrahieren und sie in das Shadowsocks-Format kodieren, bevor sie an den Shadowsocks-Server gesendet werden.
*   **Verbinden mit dem Shadowsocks-Server in `LocalProxyHandler`:** Der `LocalProxyHandler` wird eine separate Netty-`Bootstrap`-Instanz verwenden, um eine Verbindung zum konfigurierten Shadowsocks-Server herzustellen.
*   **Datenweiterleitung:** Sobald die Verbindung zum Shadowsocks-Server hergestellt ist, müssen die Handler Daten effizient zwischen der Verbindung der lokalen Anwendung und der Verbindung des Shadowsocks-Servers weiterleiten. Sie müssen wahrscheinlich die `Channel`-Objekte für beide Verbindungen verwalten.
*   **Fehlerbehandlung:** Implementieren Sie eine ordnungsgemäße Fehlerbehandlung für Netzwerkprobleme, Protokollfehler und Verschlüsselungs-/Entschlüsselungsfehler.
*   **Nebenläufigkeit:** Netty handhabt Nebenläufigkeit effizient mit seinem Event-Loop-Modell. Stellen Sie sicher, dass Ihre Handler thread-sicher entworfen sind, wenn Sie Zustände teilen müssen.

**7. Starten des Proxy-Clients**

Sie müssen eine Hauptklasse erstellen, um sowohl den lokalen Proxy-Server (der auf lokale Verbindungen lauscht) zu starten als auch potenziell die Konfiguration zu handhaben.

```java
public class ShadowsocksClient {

    private final int localPort;
    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClient(int localPort, String serverAddress, int serverPort, String method, String password) {
        this.localPort = localPort;
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    public void run() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap b = new ServerBootstrap();
            b.group(bossGroup, workerGroup)
             .channel(NioServerSocketChannel.class)
             .childHandler(new LocalProxyInitializer(serverAddress, serverPort, method, password))
             .option(ChannelOption.SO_BACKLOG, 128)
             .childOption(ChannelOption.SO_KEEPALIVE, true);

            ChannelFuture f = b.bind(localPort).sync();
            System.out.println("Shadowsocks client started on port: " + localPort);
            f.channel().closeFuture().sync();
        } finally {
            workerGroup.shutdownGracefully();
            bossGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        // Ersetzen Sie dies mit Ihrer Konfiguration
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. Erweiterte Überlegungen (wie bei Clash)**

Um einen Client wie Clash zu bauen, müssten Sie erweiterte Funktionen berücksichtigen:

*   **Mehrere Proxy-Protokolle:** Clash unterstützt verschiedene Proxy-Protokolle (Shadowsocks, SOCKS5, HTTP). Sie müssten Handler für jedes Protokoll hinzufügen.
*   **Regelbasierte Weiterleitung:** Clash erlaubt es Ihnen, Regeln zu definieren, um Datenverkehr basierend auf Domain, IP-Adresse, GEOIP usw. zu routen. Dies würde die Implementierung einer Regel-Engine in Ihrem Client erfordern.
*   **Konfigurationsverwaltung:** Clash verwendet YAML-Konfigurationsdateien. Sie müssten eine Möglichkeit implementieren, solche Konfigurationen zu laden und zu parsen.
*   **DNS-Behandlung:** Clash fängt oft DNS-Anfragen ab und leitet sie durch den Proxy. Sie müssten DNS-Abfangen und -Weiterleitung implementieren.
*   **UDP-Unterstützung:** Shadowsocks unterstützt auch UDP-Weiterleitung. Sie müssten UDP-Handling mit Nettys UDP-Fähigkeiten implementieren.
*   **Plugins und Erweiterungen:** Clash hat ein Plugin-System. Die Implementierung eines solchen Systems würde die Komplexität erheblich erhöhen.

**Zusammenfassend lässt sich sagen, dass der Bau eines grundlegenden Shadowsocks-Clients mit Netty Folgendes beinhaltet:**

1.  Verständnis des Shadowsocks-Protokolls.
2.  Einrichten eines Netty-Projekts.
3.  Erstellen benutzerdefinierter `ChannelHandler`s für Kodieren, Dekodieren und Weiterleiten von Daten.
4.  Implementieren der Verschlüsselungs- und Entschlüsselungslogik.
5.  Starten eines lokalen Servers, um Verbindungen von Anwendungen zu akzeptieren.
6.  Verbinden mit dem entfernten Shadowsocks-Server.

Der Bau eines funktionsreicheren Clients wie Clash erfordert ein viel tieferes Verständnis von Netzwerken, Proxy-Protokollen und komplexerer Softwarearchitektur. Beginnen Sie mit einer grundlegenden Shadowsocks-Implementierung und fügen Sie schrittweise Funktionen nach Bedarf hinzu. Denken Sie daran, die offizielle Shadowsocks-Dokumentation und Netty-Beispiele für detailliertere Informationen zu konsultieren.