---
audio: false
generated: true
lang: fr
layout: post
title: Programme C pour Décoder un Paquet UDP
translated: true
type: note
---

Voici un exemple de décodage d'un paquet UDP en C. Ce code montre comment recevoir un paquet UDP et extraire ses composants clés :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// Structure d'en-tête UDP
struct udp_header {
    uint16_t source_port;      // Port source
    uint16_t dest_port;       // Port de destination
    uint16_t length;          // Longueur du paquet UDP (en-tête + données)
    uint16_t checksum;        // Checksum
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // En supposant un en-tête IP de 20 octets (sans options)
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nEn-tête UDP\n");
    printf("Port source : %u\n", ntohs(udp->source_port));
    printf("Port de destination : %u\n", ntohs(udp->dest_port));
    printf("Longueur : %u\n", ntohs(udp->length));
    printf("Checksum : 0x%04x\n", ntohs(udp->checksum));
    
    // Calcul de la longueur des données et du pointeur
    int udp_header_size = 8;  // L'en-tête UDP fait 8 octets
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("Données : ");
    for(int i = 0; i < data_length && i < 20; i++) {  // Affiche maximum 20 premiers octets
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // Taille maximale d'un paquet UDP
    
    // Création de la socket UDP
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Échec de création de la socket");
        return 1;
    }
    
    // Initialisation de l'adresse du serveur
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // Port d'exemple
    
    // Liaison de la socket
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Échec de la liaison");
        close(sockfd);
        return 1;
    }
    
    printf("En écoute des paquets UDP sur le port 12345...\n");
    
    while (1) {
        socklen_t client_len = sizeof(client_addr);
        int received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0,
                                    (struct sockaddr*)&client_addr, &client_len);
                                    
        if (received_bytes < 0) {
            perror("Échec de réception");
            continue;
        }
        
        decode_udp_packet(buffer, received_bytes);
    }
    
    close(sockfd);
    return 0;
}
```

Ce code effectue les opérations suivantes :

1. Définit une structure `udp_header` qui correspond au format d'en-tête des paquets UDP :
   - Port source (16 bits)
   - Port de destination (16 bits)
   - Longueur (16 bits)
   - Checksum (16 bits)

2. Crée une socket UDP et la lie au port 12345 (vous pouvez changer ce numéro de port).

3. La fonction `decode_udp_packet` :
   - Prend un tampon de paquet brut en entrée
   - Suppose qu'un en-tête IP de 20 octets précède l'en-tête UDP (Note : cela peut varier si des options IP sont présentes)
   - Extrait et convertit les champs d'en-tête de l'ordre des octets du réseau (big-endian) vers l'ordre des octets de l'hôte en utilisant `ntohs`
   - Affiche les informations de l'en-tête
   - Extrait et affiche les données de charge utile

Pour compiler et exécuter :
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # Nécessite sudo à cause de l'utilisation de socket brute
```

Notes importantes :
1. Ceci est un exemple basique - les applications réelles pourraient nécessiter :
   - Vérification d'erreur pour la taille des paquets
   - Gestion des options d'en-tête IP (longueur variable)
   - Vérification du checksum
   - Traitement des données plus sophistiqué

2. Pour le tester, vous pouvez :
   - Envoyer des paquets UDP en utilisant netcat : `echo "test" | nc -u 127.0.0.1 12345`
   - Utiliser un outil de génération de paquets

3. Le code suppose que le paquet inclut un en-tête IP. Si vous travaillez avec des données UDP brutes, supprimez le décalage +20.

4. Pour une utilisation en production, ajoutez plus de gestion d'erreurs et utilisez éventuellement `struct udphdr` de `<netinet/udp.h>` au lieu d'une structure personnalisée.

Souhaitez-vous que j'explique une partie spécifique plus en détail ou que je montre une variante de ce code ?