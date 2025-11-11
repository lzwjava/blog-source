---
audio: false
generated: true
lang: fr
layout: post
title: Appels système de mise en réseau
translated: true
type: note
---

Dans les systèmes d'exploitation comme Linux/Unix, les appels système de plus bas niveau pour la mise en réseau, en particulier pour établir une connexion TCP, proviennent de l'API Berkeley Sockets (souvent simplement appelée "sockets"). Ces appels système interagissent directement avec la pile réseau du noyau. Les plus fondamentaux pour les connexions TCP sont :

1. **`socket()`** - Crée un nouveau socket.
2. **`bind()`** - Assigne une adresse au socket (optionnel pour les clients).
3. **`connect()`** - Initie une connexion vers un serveur distant (pour les clients).
4. **`listen()`** - Marque le socket comme acceptant les connexions (pour les serveurs).
5. **`accept()`** - Accepte une connexion entrante (pour les serveurs).
6. **`send()` / `recv()`** - Envoie ou reçoit des données sur la connexion.
7. **`close()`** - Ferme le socket.

Ce sont les appels système bruts que vous utiliseriez au niveau le plus bas, en dessous de toute bibliothèque de plus haut niveau comme `libcurl` ou de tout framework. Voici un exemple simple en C montrant à la fois un client TCP et un serveur établissant une connexion.

---

### Exemple de Serveur TCP
Ce code configure un serveur qui écoute une connexion sur le port 8080, l'accepte et envoie un message.

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

    // Créer le socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Échec de la création du socket");
        exit(EXIT_FAILURE);
    }

    // Configurer la structure d'adresse du serveur
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Lier à n'importe quelle adresse
    server_addr.sin_port = htons(8080);       // Port 8080

    // Lier le socket
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Échec de la liaison");
        exit(EXIT_FAILURE);
    }

    // Écouter les connexions
    if (listen(server_fd, 3) < 0) { // Autoriser jusqu'à 3 connexions en file d'attente
        perror("Échec de l'écoute");
        exit(EXIT_FAILURE);
    }
    printf("Serveur en écoute sur le port 8080...\n");

    // Accepter la connexion entrante
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Échec de l'acceptation");
        exit(EXIT_FAILURE);
    }
    printf("Connexion acceptée\n");

    // Envoyer un message au client
    send(client_fd, message, strlen(message), 0);

    // Nettoyer
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### Exemple de Client TCP
Ce code se connecte au serveur à l'adresse `127.0.0.1:8080` et lit le message.

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

    // Créer le socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Échec de la création du socket");
        exit(EXIT_FAILURE);
    }

    // Configurer la structure d'adresse du serveur
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // Port 8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // Localhost

    // Se connecter au serveur
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Échec de la connexion");
        exit(EXIT_FAILURE);
    }
    printf("Connecté au serveur\n");

    // Recevoir le message du serveur
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Message du serveur: %s", buffer);

    // Nettoyer
    close(sock_fd);
    return 0;
}
```

---

### Explication des Appels Système Clés
- **`socket(AF_INET, SOCK_STREAM, 0)`** : Crée un socket TCP (`AF_INET` pour IPv4, `SOCK_STREAM` pour TCP).
- **`bind()`** : Associe le socket à une adresse et un port locaux (côté serveur).
- **`listen()`** : Prépare le socket à accepter les connexions (côté serveur).
- **`accept()`** : Se bloque jusqu'à ce qu'un client se connecte, puis retourne un nouveau socket pour la communication.
- **`connect()`** : Initie une poignée de main TCP avec le serveur (côté client).
- **`send()` / `recv()`** : Gèrent le transfert de données sur la connexion établie.
- **`close()`** : Termine le socket.

C'est le niveau le plus bas que l'on puisse atteindre pour la mise en réseau TCP dans l'espace utilisateur. En dessous, vous seriez confronté aux internes du noyau (par exemple, la pile TCP/IP elle-même), qui n'est pas directement accessible via des appels système sans écrire du code noyau.

Pour compiler et exécuter :
1. Sauvegardez le code du serveur dans `server.c` et le code du client dans `client.c`.
2. Compilez : `gcc server.c -o server` et `gcc client.c -o client`.
3. Exécutez d'abord le serveur : `./server`.
4. Dans un autre terminal, exécutez le client : `./client`.

Faites-moi savoir si vous voulez plus de détails ou une exploration plus approfondie !