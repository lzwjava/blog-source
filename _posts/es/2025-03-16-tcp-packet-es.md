---
audio: false
generated: true
lang: es
layout: post
title: Programa en C para Decodificar un Paquete TCP
translated: true
type: note
---

Decodificar un paquete TCP en C implica capturar datos de red en bruto (normalmente usando sockets raw o un mecanismo de captura de paquetes) y luego analizar las cabeceras paso a paso: la cabecera Ethernet (si está presente), la cabecera IP y finalmente la cabecera TCP. Dado que TCP funciona sobre IP, necesitarás extraer primero la cabecera IP para localizar el segmento TCP dentro del paquete. Por simplicidad, asumiré que estamos trabajando con IPv4 y un socket raw que captura paquetes IP (sin capa Ethernet).

Aquí tienes un programa en C que captura un paquete TCP usando un socket raw, decodifica la cabecera IP y luego decodifica la cabecera TCP para mostrar campos clave como puertos de origen/destino, número de secuencia, número de acuse de recibo, flags y tamaño de ventana.

---

### Programa en C para Decodificar un Paquete TCP

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // For struct iphdr
#include <netinet/tcp.h>  // For struct tcphdr

// Imprimir flags TCP en forma legible
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
    char buffer[65535]; // Tamaño máximo de paquete IP
    struct sockaddr_in source_addr, dest_addr;

    // Crear socket raw para capturar paquetes TCP
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("Error en la creación del socket (¿ejecutar como root?)");
        exit(EXIT_FAILURE);
    }

    printf("Escuchando paquetes TCP...\n");

    while (1) {
        // Recibir paquete raw
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Error en la recepción");
            continue;
        }

        // La cabecera IP (struct iphdr) está al inicio del paquete
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl está en palabras de 32-bit, convertir a bytes

        // Verificar si es un paquete IPv4 con protocolo TCP
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // La cabecera TCP sigue a la cabecera IP
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // Extraer direcciones IP de origen y destino
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // Decodificar e imprimir detalles del paquete TCP
            printf("\n--- Paquete TCP ---\n");
            printf("IP Origen: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("IP Destino: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("Puerto Origen: %u\n", ntohs(tcp->source));
            printf("Puerto Destino: %u\n", ntohs(tcp->dest));
            printf("Número de Secuencia: %u\n", ntohl(tcp->seq));
            printf("Número de Acuse de Recibo: %u\n", ntohl(tcp->ack_seq));
            printf("Desplazamiento de Datos: %d bytes\n", tcp->doff * 4); // Longitud de la cabecera TCP
            print_tcp_flags(tcp);
            printf("Tamaño de Ventana: %u\n", ntohs(tcp->window));
            printf("Checksum: 0x%04x\n", ntohs(tcp->check));
            printf("Puntero Urgente: %u\n", ntohs(tcp->urg_ptr));

            // Payload (datos después de la cabecera TCP)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("Longitud del Payload: %d bytes\n", payload_len);
                printf("Payload (primeros 16 bytes): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("Sin payload\n");
            }
        }
    }

    close(sock_fd); // Inalcanzable en este bucle, pero buena práctica
    return 0;
}
```

---

### Cómo Funciona

1. **Configuración del Socket**:
   - `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` crea un socket raw que captura todos los paquetes TCP destinados al host. Esto requiere privilegios de root (`sudo`).

2. **Captura de Paquetes**:
   - `recvfrom()` captura el paquete IP en bruto, que incluye la cabecera IP, la cabecera TCP y el payload.

3. **Análisis de la Cabecera IP**:
   - `struct iphdr` define la cabecera IPv4 (desde `<netinet/ip.h>`).
   - `ihl` (longitud de la cabecera IP) se multiplica por 4 para obtener el desplazamiento en bytes, ya que se mide en palabras de 32 bits.
   - Se verifica `version == 4` y `protocol == IPPROTO_TCP` para asegurarse de que es un paquete TCP IPv4.

4. **Análisis de la Cabecera TCP**:
   - `struct tcphdr` (desde `<netinet/tcp.h>`) define la cabecera TCP, comenzando justo después de la cabecera IP.
   - Campos clave:
     - `source` y `dest`: Puertos de origen y destino (convertidos del orden de bytes de red al del host con `ntohs`).
     - `seq` y `ack_seq`: Números de secuencia y de acuse de recibo (`ntohl` para conversión de 32 bits).
     - `doff`: Desplazamiento de datos (longitud de la cabecera TCP en bytes, también multiplicada por 4).
     - `syn`, `ack`, `fin`, etc.: Flags que indican el tipo de paquete.
     - `window`: Tamaño de la ventana del receptor.
     - `check`: Checksum (no se valida aquí por simplicidad).
     - `urg_ptr`: Puntero urgente (se usa con el flag URG).

5. **Extracción del Payload**:
   - El payload comienza después de la cabecera TCP. Su longitud se calcula como: `bytes totales - longitud cabecera IP - longitud cabecera TCP`.
   - Se imprime un fragmento del payload en hexadecimal.

---

### Compilación y Uso
- Compilar: `gcc tcp_decode.c -o tcp_decode`
- Ejecutar (como root): `sudo ./tcp_decode`
- Salida de ejemplo (cuando hay tráfico TCP, por ejemplo, navegando por la web):
  ```
  Escuchando paquetes TCP...

  --- Paquete TCP ---
  IP Origen: 192.168.1.100
  IP Destino: 93.184.216.34
  Puerto Origen: 54321
  Puerto Destino: 80
  Número de Secuencia: 123456789
  Número de Acuse de Recibo: 987654321
  Desplazamiento de Datos: 20 bytes
  Flags: SYN
  Tamaño de Ventana: 64240
  Checksum: 0x1a2b
  Puntero Urgente: 0
  Sin payload
  ```

---

### Estructuras Clave
- **Cabecera IP (`struct iphdr`)**:
  ```c
  struct iphdr {
      unsigned int ihl:4;    // Longitud de la cabecera (en palabras de 32-bit)
      unsigned int version:4;// Versión IP (4 para IPv4)
      uint8_t tos;           // Tipo de servicio
      uint16_t tot_len;      // Longitud total
      uint16_t id;           // Identificación
      uint16_t frag_off;     // Desplazamiento del fragmento
      uint8_t ttl;           // Tiempo de vida
      uint8_t protocol;      // Protocolo (6 para TCP)
      uint16_t check;        // Checksum
      uint32_t saddr;        // Dirección de origen
      uint32_t daddr;        // Dirección de destino
  };
  ```

- **Cabecera TCP (`struct tcphdr`)**:
  ```c
  struct tcphdr {
      uint16_t source;       // Puerto origen
      uint16_t dest;         // Puerto destino
      uint32_t seq;          // Número de secuencia
      uint32_t ack_seq;      // Número de acuse de recibo
      uint16_t doff:4;       // Desplazamiento de datos (longitud de cabecera en palabras de 32-bit)
      uint16_t res1:4;       // Reservado
      uint16_t res2:2;       // Reservado
      uint16_t urg:1;        // Flag urgente
      uint16_t ack:1;        // Flag de acuse de recibo
      uint16_t psh:1;        // Flag push
      uint16_t rst:1;        // Flag reset
      uint16_t syn:1;        // Flag de sincronización
      uint16_t fin:1;        // Flag de finalización
      uint16_t window;       // Tamaño de ventana
      uint16_t check;        // Checksum
      uint16_t urg_ptr;      // Puntero urgente
  };
  ```

---

### Notas
- **Privilegios de Root**: Los sockets raw requieren `sudo` porque acceden directamente a la pila de red.
- **Modo Promiscuo**: Esto captura solo los paquetes destinados al host. Para todo el tráfico (como Wireshark), necesitarías `libpcap` o un enfoque diferente (por ejemplo, sockets `PF_PACKET` con modo promiscuo).
- **Orden de Bytes**: El orden de bytes de red (big-endian) se convierte al orden de bytes del host usando `ntohs` (16-bit) y `ntohl` (32-bit).
- **Limitaciones**: Esto no valida el checksum ni maneja paquetes fragmentados.

¡Avísame si quieres refinar esto más (por ejemplo, añadir validación de checksum o filtrar puertos específicos)!