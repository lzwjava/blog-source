---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Programmation Linux TCP/IP en C
translated: true
type: note
---

### Protocoles TCP/IP sous Linux : Aperçu et utilisation en C

Sous Linux, les protocoles TCP (Transmission Control Protocol) et IP (Internet Protocol) sont des protocoles de mise en réseau centraux implémentés **dans le noyau** dans le cadre de la pile TCP/IP Linux. Cette pile gère les détails de bas niveau tels que le routage des paquets, le contrôle de congestion et la gestion des connexions. Les applications en espace utilisateur (par exemple, vos programmes en C) interagissent avec cette pile via **l'API Berkeley sockets** (également appelée sockets POSIX), qui fournit un moyen standardisé de créer des connexions réseau.

Vous n'avez pas besoin d'implémenter TCP/IP vous-même — le noyau s'en charge. Au lieu de cela, vous utilisez l'API sockets pour "parler" au noyau. Cette API est **intégrée à la bibliothèque standard C (glibc)** sous Linux, il n'y a donc pas de "bibliothèque TCP/IP" séparée à installer ou à lier. Tout est fourni par `libc` (GNU C Library).

#### Bibliothèques et en-têtes clés
- **Bibliothèque principale** : `libc` (glibc). Toutes les fonctions de socket sont incluses ici. Liez votre programme avec elle implicitement (c'est généralement automatique avec `gcc`).
  - Emplacement : Typiquement `/lib/x86_64-linux-gnu/libc.so.6` (ou similaire, selon votre architecture et distribution). Vous pouvez le trouver avec `ldd /bin/ls` ou `locate libc.so`.
- **En-têtes** (pour les déclarations) : Ils font partie des en-têtes de développement Linux.
  - `<sys/socket.h>` : Fonctions de socket principales (par exemple, `socket()`, `bind()`, `connect()`).
  - `<netinet/in.h>` : Structures d'adresse Internet (par exemple, `struct sockaddr_in` pour IPv4).
  - `<arpa/inet.h>` : Fonctions de conversion d'adresse (par exemple, `inet_addr()`).
  - `<sys/types.h>` : Types de base (souvent inclus indirectement).
  - Emplacement : Habituellement `/usr/include/` (par exemple, `/usr/include/sys/socket.h`). Installez les en-têtes de développement s'ils manquent (par exemple, `sudo apt install libc6-dev` sur les systèmes basés sur Debian).

Aucun drapeau supplémentaire comme `-lsocket` n'est nécessaire sous Linux (contrairement à certains anciens systèmes Unix). Compilez simplement avec `gcc votre_programme.c -o votre_programme`.

#### Exemple de base : Client TCP simple en C
Voici un client TCP minimal qui se connecte à un serveur (par exemple, le port 80 sur example.com). Cela démontre l'utilisation de l'API sockets.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // For close()

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // Créer un socket TCP (AF_INET pour IPv4, SOCK_STREAM pour TCP)
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // Ordre des octets host-to-network
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // IP pour example.com

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
    printf("Response: %s\n", buffer);

    close(sockfd);
    return 0;
}
```

- Compilation : `gcc -o tcp_client tcp_client.c`
- Exécution : `./tcp_client`

Pour un serveur, vous utiliseriez `bind()`, `listen()`, et `accept()` au lieu de `connect()`.

#### Où en apprendre davantage
- **Pages de manuel** : Exécutez `man socket` ou `man 7 ip` sur votre système Linux pour une documentation détaillée.
- **Côté noyau** : Si vous pensiez à l'implémentation au niveau du noyau, vérifiez le code source dans `/usr/src/linux/net/ipv4/` (TCP) ou `/usr/src/linux/net/ipv6/` (pour IPv6). Installez les en-têtes du noyau avec `sudo apt install linux-headers-$(uname -r)`.
- Ressources :
  - [Socket Programming in C (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [Programming Linux Sockets with TCP/IP (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

Si ce n'est pas ce que vous vouliez dire (par exemple, modules du noyau ou autre chose), fournissez plus de détails !