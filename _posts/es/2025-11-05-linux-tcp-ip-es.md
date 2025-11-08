---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Programación Linux TCP/IP en C
translated: true
type: note
---

### Protocolos TCP/IP en Linux: Descripción General y Uso en C

En Linux, el TCP (Protocolo de Control de Transmisión) y el IP (Protocolo de Internet) son protocolos de red centrales implementados **en el kernel** como parte de la pila TCP/IP de Linux. Esta pila maneja detalles de bajo nivel como el enrutamiento de paquetes, el control de congestión y la gestión de conexiones. Las aplicaciones en el espacio de usuario (por ejemplo, sus programas en C) interactúan con esta pila a través de la **API de sockets Berkeley** (también conocida como sockets POSIX), que proporciona una forma estandarizada de crear conexiones de red.

No necesita implementar TCP/IP usted mismo: el kernel lo hace. En su lugar, utiliza la API de sockets para "hablar" con el kernel. Esta API está **integrada en la biblioteca estándar de C (glibc)** en Linux, por lo que no hay una "biblioteca TCP/IP" separada que instalar o enlazar. Todo es proporcionado por `libc` (GNU C Library).

#### Bibliotecas y Cabeceras Clave
- **Biblioteca Principal**: `libc` (glibc). Todas las funciones de socket están incluidas aquí. Enlace su programa con ella implícitamente (generalmente es automático con `gcc`).
  - Ubicación: Típicamente `/lib/x86_64-linux-gnu/libc.so.6` (o similar, dependiendo de su arquitectura y distribución). Puede encontrarla con `ldd /bin/ls` o `locate libc.so`.
- **Cabeceras** (para declaraciones): Estas son parte de las cabeceras de desarrollo de Linux.
  - `<sys/socket.h>`: Funciones principales de socket (por ejemplo, `socket()`, `bind()`, `connect()`).
  - `<netinet/in.h>`: Estructuras de direcciones de Internet (por ejemplo, `struct sockaddr_in` para IPv4).
  - `<arpa/inet.h>`: Funciones de conversión de direcciones (por ejemplo, `inet_addr()`).
  - `<sys/types.h>`: Tipos básicos (a menudo incluidos indirectamente).
  - Ubicación: Usualmente `/usr/include/` (por ejemplo, `/usr/include/sys/socket.h`). Instale las cabeceras de desarrollo si faltan (por ejemplo, `sudo apt install libc6-dev` en sistemas basados en Debian).

No se necesitan banderas adicionales como `-lsocket` en Linux (a diferencia de algunos sistemas Unix antiguos). Simplemente compile con `gcc su_programa.c -o su_programa`.

#### Ejemplo Básico: Cliente TCP Simple en C
Aquí hay un cliente TCP mínimo que se conecta a un servidor (por ejemplo, puerto 80 en example.com). Esto demuestra el uso de la API de sockets.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // Para close()

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // Crear socket TCP (AF_INET para IPv4, SOCK_STREAM para TCP)
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // Orden de bytes host-a-red
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // IP para example.com

    if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(sockfd);
        return 1;
    }

    const char* msg = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
    send(sockfd, msg, strlen(msg), 0);

    char buffer[1024];
    int bytes = recv(sockfd, buffer, sizeof(buffer) - 1, 0);
    buffer[bytes] = '\0';
    printf("Respuesta: %s\n", buffer);

    close(sockfd);
    return 0;
}
```

- Compilar: `gcc -o tcp_client tcp_client.c`
- Ejecutar: `./tcp_client`

Para un servidor, usaría `bind()`, `listen()` y `accept()` en lugar de `connect()`.

#### Dónde Aprender Más
- **Páginas del Manual**: Ejecute `man socket` o `man 7 ip` en su sistema Linux para documentación detallada.
- **Lado del Kernel**: Si se refería a la implementación a nivel del kernel, consulte el código fuente en `/usr/src/linux/net/ipv4/` (TCP) o `/usr/src/linux/net/ipv6/` (para IPv6). Instale las cabeceras del kernel con `sudo apt install linux-headers-$(uname -r)`.
- Recursos:
  - [Programación de Sockets en C (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [Programación de Sockets Linux con TCP/IP (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

Si esto no es lo que quería decir (por ejemplo, módulos del kernel o algo más), ¡proporcione más detalles!