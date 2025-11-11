---
audio: false
generated: true
lang: de
layout: post
title: C-Programm zum Dekodieren eines TCP-Pakets
translated: true
type: note
---

Das Decodieren eines TCP-Pakets in C umfasst das Erfassen von rohen Netzwerkdaten (typischerweise mit Raw Sockets oder einem Packet Capture Mechanismus) und dann das schrittweise Parsen der Header: den Ethernet-Header (falls vorhanden), den IP-Header und schließlich den TCP-Header. Da TCP über IP läuft, müssen Sie zuerst den IP-Header extrahieren, um das TCP-Segment innerhalb des Pakets zu lokalisieren. Der Einfachheit halber gehe ich davon aus, dass wir mit IPv4 und einem Raw Socket arbeiten, der IP-Pakete erfasst (keine Ethernet-Schicht).

Hier ist ein C-Programm, das ein TCP-Paket mit einem Raw Socket erfasst, den IP-Header decodiert und dann den TCP-Header decodiert, um wichtige Felder wie Quell-/Zielports, Sequenznummer, Bestätigungsnummer, Flags und Fenstergröße anzuzeigen.

---

### C-Programm zum Decodieren eines TCP-Pakets

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // Für struct iphdr
#include <netinet/tcp.h>  // Für struct tcphdr

// TCP-Flags in menschenlesbarer Form ausgeben
void print_tcp_flags(struct tcphdr *tcp) {
    printf("Flags: ");
    if (tcp->syn) printf("SYN ");
    if (tcp->ack) printf("ACK ");
    if (tcp->fin) printf("FIN ");
    if (tcp->rst) printf("RST ");
    if (tcp->psh) printf("PSH ");
    if (tcp->urg) printf("URG ");
    printf("\n");
}

int main() {
    int sock_fd;
    char buffer[65535]; // Maximale IP-Paketgröße
    struct sockaddr_in source_addr, dest_addr;

    // Raw Socket erstellen, um TCP-Pakete zu erfassen
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("Socket-Erstellung fehlgeschlagen (als root ausführen?)");
        exit(EXIT_FAILURE);
    }

    printf("Lausche auf TCP-Pakete...\n");

    while (1) {
        // Rohes Paket empfangen
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Empfang fehlgeschlagen");
            continue;
        }

        // IP-Header (struct iphdr) befindet sich am Anfang des Pakets
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl ist in 32-Bit-Worten, umwandeln in Bytes

        // Prüfen, ob es sich um ein IPv4-Paket mit TCP-Protokoll handelt
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // TCP-Header folgt auf IP-Header
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // Quell- und Ziel-IP-Adressen extrahieren
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // TCP-Paketdetails decodieren und ausgeben
            printf("\n--- TCP-Paket ---\n");
            printf("Quell-IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("Ziel-IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("Quell-Port: %u\n", ntohs(tcp->source));
            printf("Ziel-Port: %u\n", ntohs(tcp->dest));
            printf("Sequenznummer: %u\n", ntohl(tcp->seq));
            printf("Bestätigungsnummer: %u\n", ntohl(tcp->ack_seq));
            printf("Data Offset: %d Bytes\n", tcp->doff * 4); // TCP-Headerlänge
            print_tcp_flags(tcp);
            printf("Fenstergröße: %u\n", ntohs(tcp->window));
            printf("Prüfsumme: 0x%04x\n", ntohs(tcp->check));
            printf("Urgent Pointer: %u\n", ntohs(tcp->urg_ptr));

            // Payload (Daten nach dem TCP-Header)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("Payload-Länge: %d Bytes\n", payload_len);
                printf("Payload (erste 16 Bytes): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("Kein Payload\n");
            }
        }
    }

    close(sock_fd); // In dieser Schleife unerreichbar, aber gute Praxis
    return 0;
}
```

---

### So funktioniert es

1.  **Socket-Einrichtung**:
    *   `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` erstellt einen Raw Socket, der alle TCP-Pakete erfasst, die für den Host bestimmt sind. Dies erfordert Root-Rechte (`sudo`).

2.  **Paket-Erfassung**:
    *   `recvfrom()` fängt das rohe IP-Paket ab, das den IP-Header, TCP-Header und Payload enthält.

3.  **IP-Header-Parsing**:
    *   `struct iphdr` definiert den IPv4-Header (aus `<netinet/ip.h>`).
    *   `ihl` (IP-Header-Länge) wird mit 4 multipliziert, um den Byte-Offset zu erhalten, da es in 32-Bit-Worten gemessen wird.
    *   Prüfen von `version == 4` und `protocol == IPPROTO_TCP`, um sicherzustellen, dass es sich um ein IPv4-TCP-Paket handelt.

4.  **TCP-Header-Parsing**:
    *   `struct tcphdr` (aus `<netinet/tcp.h>`) definiert den TCP-Header, der direkt auf den IP-Header folgt.
    *   Wichtige Felder:
        *   `source` und `dest`: Quell- und Ziel-Ports (konvertiert von Netzwerk- zu Host-Byte-Reihenfolge mit `ntohs`).
        *   `seq` und `ack_seq`: Sequenz- und Bestätigungsnummern (`ntohl` für 32-Bit-Konvertierung).
        *   `doff`: Data Offset (TCP-Header-Länge in Bytes, ebenfalls mit 4 multipliziert).
        *   `syn`, `ack`, `fin`, etc.: Flags, die den Pakettyp anzeigen.
        *   `window`: Fenstergröße des Empfängers.
        *   `check`: Prüfsumme (hier der Einfachheit halber nicht validiert).
        *   `urg_ptr`: Urgent Pointer (wird mit dem URG-Flag verwendet).

5.  **Payload-Extraktion**:
    *   Der Payload beginnt nach dem TCP-Header. Seine Länge wird berechnet als: `Gesamtbytes - IP-Header-Länge - TCP-Header-Länge`.
    *   Ein Ausschnitt des Payloads wird in Hex ausgegeben.

---

### Kompilierung und Verwendung
*   Kompilieren: `gcc tcp_decode.c -o tcp_decode`
*   Ausführen (als root): `sudo ./tcp_decode`
*   Beispielausgabe (wenn TCP-Datenverkehr vorhanden ist, z.B. beim Surfen im Web):
    ```
    Lausche auf TCP-Pakete...

    --- TCP-Paket ---
    Quell-IP: 192.168.1.100
    Ziel-IP: 93.184.216.34
    Quell-Port: 54321
    Ziel-Port: 80
    Sequenznummer: 123456789
    Bestätigungsnummer: 987654321
    Data Offset: 20 Bytes
    Flags: SYN
    Fenstergröße: 64240
    Prüfsumme: 0x1a2b
    Urgent Pointer: 0
    Kein Payload
    ```

---

### Wichtige Strukturen
*   **IP-Header (`struct iphdr`)**:
    ```c
    struct iphdr {
        unsigned int ihl:4;    // Headerlänge (in 32-Bit-Worten)
        unsigned int version:4;// IP-Version (4 für IPv4)
        uint8_t tos;           // Type of Service
        uint16_t tot_len;      // Gesamtlänge
        uint16_t id;           // Identifikation
        uint16_t frag_off;     // Fragment-Offset
        uint8_t ttl;           // Time to Live
        uint8_t protocol;      // Protokoll (6 für TCP)
        uint16_t check;        // Prüfsumme
        uint32_t saddr;        // Quelladresse
        uint32_t daddr;        // Zieladresse
    };
    ```

*   **TCP-Header (`struct tcphdr`)**:
    ```c
    struct tcphdr {
        uint16_t source;       // Quellport
        uint16_t dest;         // Zielport
        uint32_t seq;          // Sequenznummer
        uint32_t ack_seq;      // Bestätigungsnummer
        uint16_t doff:4;       // Data Offset (Headerlänge in 32-Bit-Worten)
        uint16_t res1:4;       // Reserviert
        uint16_t res2:2;       // Reserviert
        uint16_t urg:1;        // Urgent-Flag
        uint16_t ack:1;        // Acknowledgment-Flag
        uint16_t psh:1;        // Push-Flag
        uint16_t rst:1;        // Reset-Flag
        uint16_t syn:1;        // Synchronize-Flag
        uint16_t fin:1;        // Finish-Flag
        uint16_t window;       // Fenstergröße
        uint16_t check;        // Prüfsumme
        uint16_t urg_ptr;      // Urgent Pointer
    };
    ```

---

### Anmerkungen
*   **Root-Rechte**: Raw Sockets erfordern `sudo`, da sie direkt auf den Netzwerkstack zugreifen.
*   **Promiscuous Mode**: Dies erfasst nur Pakete, die für den Host bestimmt sind. Für den gesamten Datenverkehr (wie bei Wireshark) benötigen Sie `libpcap` oder einen anderen Ansatz (z.B. `PF_PACKET` Sockets mit Promiscuous Mode).
*   **Byte-Reihenfolge**: Die Netzwerk-Byte-Reihenfolge (Big-Endian) wird mit `ntohs` (16-Bit) und `ntohl` (32-Bit) in die Host-Byte-Reihenfolge konvertiert.
*   **Einschränkungen**: Dies validiert nicht die Prüfsumme und behandelt keine fragmentierten Pakete.

Lassen Sie mich wissen, wenn Sie dies weiter verfeinern möchten (z.B. durch Hinzufügen einer Prüfsummenvalidierung oder das Filtern bestimmter Ports)!