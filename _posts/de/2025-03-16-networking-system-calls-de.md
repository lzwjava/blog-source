---
audio: false
generated: true
lang: de
layout: post
title: Netzwerk Systemaufrufe
translated: true
type: note
---

In Betriebssystemen wie Linux/Unix stammen die niedrigsten Systemaufrufe für Netzwerkfunktionen, insbesondere für das Herstellen einer TCP-Verbindung, von der Berkeley Sockets API (oft einfach "Sockets" genannt). Diese Systemaufrufe interagieren direkt mit dem Netzwerkstack des Kernels. Die grundlegendsten für TCP-Verbindungen sind:

1.  **`socket()`** - Erzeugt einen neuen Socket.
2.  **`bind()`** - Weist dem Socket eine Adresse zu (optional für Clients).
3.  **`connect()`** - Initiiert eine Verbindung zu einem entfernten Server (für Clients).
4.  **`listen()`** - Markiert den Socket als verbindungsannehmend (für Server).
5.  **`accept()`** - Akzeptiert eine eingehende Verbindung (für Server).
6.  **`send()` / `recv()`** - Sendet oder empfängt Daten über die Verbindung.
7.  **`close()`** - Schließt den Socket.

Dies sind die rohen Systemaufrufe, die man auf der niedrigsten Ebene verwenden würde, unterhalb jeglicher höherer Bibliotheken wie `libcurl` oder Frameworks. Hier ist ein einfaches Beispiel in C, das sowohl einen TCP-Client als auch einen Server zeigt, die eine Verbindung herstellen.

---

### TCP-Server-Beispiel
Dieser Code richtet einen Server ein, der auf Port 8080 auf eine Verbindung wartet, diese annimmt und eine Nachricht sendet.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    char *message = "Hello from server!\n";

    // Socket erstellen
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Serveradressstruktur einrichten
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // An jede Adresse binden
    server_addr.sin_port = htons(8080);       // Port 8080

    // Socket binden
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Auf Verbindungen warten
    if (listen(server_fd, 3) < 0) { // Bis zu 3 Verbindungen in der Warteschlange erlauben
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // Eingehende Verbindung akzeptieren
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // Nachricht an Client senden
    send(client_fd, message, strlen(message), 0);

    // Aufräumen
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### TCP-Client-Beispiel
Dieser Code verbindet sich mit dem Server unter `127.0.0.1:8080` und liest die Nachricht.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock_fd;
    struct sockaddr_in server_addr;
    char buffer[1024] = {0};

    // Socket erstellen
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Serveradressstruktur einrichten
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // Port 8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // Localhost

    // Mit Server verbinden
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Connected to server\n");

    // Nachricht vom Server empfangen
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Server message: %s", buffer);

    // Aufräumen
    close(sock_fd);
    return 0;
}
```

---

### Erklärung der wichtigsten Systemaufrufe
-   **`socket(AF_INET, SOCK_STREAM, 0)`**: Erstellt einen TCP-Socket (`AF_INET` für IPv4, `SOCK_STREAM` für TCP).
-   **`bind()`**: Verknüpft den Socket mit einer lokalen Adresse und einem Port (Server-Seite).
-   **`listen()`**: Bereitet den Socket darauf vor, Verbindungen zu akzeptieren (Server-Seite).
-   **`accept()`**: Blockiert, bis ein Client eine Verbindung herstellt, und gibt dann einen neuen Socket für die Kommunikation zurück.
-   **`connect()`**: Initiiert einen TCP-Handshake mit dem Server (Client-Seite).
-   **`send()` / `recv()`**: Behandeln die Datenübertragung über die etablierte Verbindung.
-   **`close()`**: Beendet den Socket.

Dies ist die niedrigste Ebene für TCP-Netzwerkkommunikation im User Space. Darunter würde man sich mit Kernel-Interna befassen (z.B. dem TCP/IP-Stack selbst), auf die ohne das Schreiben von Kernel-Code nicht direkt über Systemaufrufe zugegriffen werden kann.

So kompilieren und ausführen:
1.  Speichern Sie den Server-Code als `server.c` und den Client-Code als `client.c`.
2.  Kompilieren: `gcc server.c -o server` und `gcc client.c -o client`.
3.  Führen Sie zuerst den Server aus: `./server`.
4.  Führen Sie in einem anderen Terminal den Client aus: `./client`.

Lassen Sie es mich wissen, wenn Sie mehr Details oder einen tieferen Einblick wünschen!