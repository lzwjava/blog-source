---
audio: false
generated: true
lang: es
layout: post
title: Llamadas al Sistema de Red
translated: true
type: note
---

En sistemas operativos como Linux/Unix, las llamadas al sistema de más bajo nivel para redes, particularmente para establecer una conexión TCP, provienen de la API Berkeley Sockets (a menudo llamada simplemente "sockets"). Estas llamadas al sistema interactúan directamente con la pila de red del kernel. Las más fundamentales para conexiones TCP son:

1.  **`socket()`** - Crea un nuevo socket.
2.  **`bind()`** - Asigna una dirección al socket (opcional para clientes).
3.  **`connect()`** - Inicia una conexión con un servidor remoto (para clientes).
4.  **`listen()`** - Marca el socket como uno que acepta conexiones (para servidores).
5.  **`accept()`** - Acepta una conexión entrante (para servidores).
6.  **`send()` / `recv()`** - Envía o recibe datos a través de la conexión.
7.  **`close()`** - Cierra el socket.

Estas son las llamadas al sistema básicas que usarías en el nivel más bajo, por debajo de cualquier biblioteca de alto nivel como `libcurl` o frameworks. Aquí hay un ejemplo simple en C que muestra tanto un cliente como un servidor TCP estableciendo una conexión.

---

### Ejemplo de Servidor TCP
Este código configura un servidor que escucha una conexión en el puerto 8080, la acepta y envía un mensaje.

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

    // Crear socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configurar la estructura de dirección del servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Enlazar a cualquier dirección
    server_addr.sin_port = htons(8080);       // Puerto 8080

    // Enlazar socket
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Escuchar conexiones
    if (listen(server_fd, 3) < 0) { // Permitir hasta 3 conexiones en cola
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // Aceptar conexión entrante
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // Enviar mensaje al cliente
    send(client_fd, message, strlen(message), 0);

    // Limpiar
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### Ejemplo de Cliente TCP
Este código se conecta al servidor en `127.0.0.1:8080` y lee el mensaje.

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

    // Crear socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configurar la estructura de dirección del servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = h