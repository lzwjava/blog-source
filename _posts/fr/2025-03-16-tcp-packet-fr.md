---
audio: false
generated: true
lang: fr
layout: post
title: Programme C pour Décoder un Paquet TCP
translated: true
type: note
---

Décoder un paquet TCP en C implique de capturer des données réseau brutes (généralement en utilisant des sockets bruts ou un mécanisme de capture de paquets) puis d'analyser les en-têtes étape par étape : l'en-tête Ethernet (si présent), l'en-tête IP, et enfin l'en-tête TCP. Comme TCP fonctionne au-dessus d'IP, vous devrez d'abord extraire l'en-tête IP pour localiser le segment TCP dans le paquet. Pour simplifier, je suppose que nous travaillons avec IPv4 et un socket brut capturant des paquets IP (pas de couche Ethernet).

Voici un programme en C qui capture un paquet TCP en utilisant un socket brut, décode l'en-tête IP, puis décode l'en-tête TCP pour afficher les champs clés tels que les ports source/destination, le numéro de séquence, le numéro d'acquittement, les drapeaux et la taille de la fenêtre.

---

### Programme C pour décoder un paquet TCP

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // Pour struct iphdr
#include <netinet/tcp.h>  // Pour struct tcphdr

// Afficher les drapeaux TCP sous forme lisible
void print_tcp_flags(struct tcphdr *tcp) {
    printf("Drapeaux : ");
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
    char buffer[65535]; // Taille maximale d'un paquet IP
    struct sockaddr_in source_addr, dest_addr;

    // Créer un socket brut pour capturer les paquets TCP
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("Échec de la création du socket (exécuter en root ?)");
        exit(EXIT_FAILURE);
    }

    printf("Écoute des paquets TCP...\n");

    while (1) {
        // Recevoir le paquet brut
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Échec de la réception");
            continue;
        }

        // L'en-tête IP (struct iphdr) est au début du paquet
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl est en mots de 32 bits, convertir en octets

        // Vérifier s'il s'agit d'un paquet IPv4 avec le protocole TCP
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // L'en-tête TCP suit l'en-tête IP
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // Extraire les adresses IP source et destination
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // Décoder et afficher les détails du paquet TCP
            printf("\n--- Paquet TCP ---\n");
            printf("IP Source : %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("IP Destination : %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("Port Source : %u\n", ntohs(tcp->source));
            printf("Port Destination : %u\n", ntohs(tcp->dest));
            printf("Numéro de Séquence : %u\n", ntohl(tcp->seq));
            printf("Numéro d'Acquittement : %u\n", ntohl(tcp->ack_seq));
            printf("Décalage des Données : %d octets\n", tcp->doff * 4); // Longueur de l'en-tête TCP
            print_tcp_flags(tcp);
            printf("Taille de la Fenêtre : %u\n", ntohs(tcp->window));
            printf("Somme de Contrôle : 0x%04x\n", ntohs(tcp->check));
            printf("Pointeur Urgent : %u\n", ntohs(tcp->urg_ptr));

            // Payload (données après l'en-tête TCP)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("Longueur du Payload : %d octets\n", payload_len);
                printf("Payload (16 premiers octets) : ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("Aucun payload\n");
            }
        }
    }

    close(sock_fd); // Inaccessible dans cette boucle, mais bonne pratique
    return 0;
}
```

---

### Fonctionnement

1. **Configuration du Socket** :
   - `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` crée un socket brut qui capture tous les paquets TCP destinés à l'hôte. Cela nécessite les privilèges root (`sudo`).

2. **Capture de Paquet** :
   - `recvfrom()` récupère le paquet IP brut, qui inclut l'en-tête IP, l'en-tête TCP et le payload.

3. **Analyse de l'En-tête IP** :
   - `struct iphdr` définit l'en-tête IPv4 (de `<netinet/ip.h>`).
   - `ihl` (longueur de l'en-tête IP) est multiplié par 4 pour obtenir le décalage en octets, car il est mesuré en mots de 32 bits.
   - Vérifier `version == 4` et `protocol == IPPROTO_TCP` pour s'assurer qu'il s'agit d'un paquet TCP IPv4.

4. **Analyse de l'En-tête TCP** :
   - `struct tcphdr` (de `<netinet/tcp.h>`) définit l'en-tête TCP, commençant juste après l'en-tête IP.
   - Champs clés :
     - `source` et `dest` : Ports source et destination (convertis de l'ordre des octets du réseau vers celui de l'hôte avec `ntohs`).
     - `seq` et `ack_seq` : Numéros de séquence et d'acquittement (`ntohl` pour la conversion 32 bits).
     - `doff` : Décalage des données (longueur de l'en-tête TCP en octets, également multiplié par 4).
     - `syn`, `ack`, `fin`, etc. : Drapeaux indiquant le type de paquet.
     - `window` : Taille de la fenêtre du récepteur.
     - `check` : Somme de contrôle (non validée ici par souci de simplicité).
     - `urg_ptr` : Pointeur urgent (utilisé avec le drapeau URG).

5. **Extraction du Payload** :
   - Le payload commence après l'en-tête TCP. Sa longueur est calculée comme suit : `octets totaux - longueur en-tête IP - longueur en-tête TCP`.
   - Un extrait du payload est affiché en hexadécimal.

---

### Compilation et Utilisation
- Compiler : `gcc tcp_decode.c -o tcp_decode`
- Exécuter (en root) : `sudo ./tcp_decode`
- Exemple de sortie (lorsqu'il y a du trafic TCP, par exemple en naviguant sur le web) :
  ```
  Écoute des paquets TCP...

  --- Paquet TCP ---
  IP Source : 192.168.1.100
  IP Destination : 93.184.216.34
  Port Source : 54321
  Port Destination : 80
  Numéro de Séquence : 123456789
  Numéro d'Acquittement : 987654321
  Décalage des Données : 20 octets
  Drapeaux : SYN
  Taille de la Fenêtre : 64240
  Somme de Contrôle : 0x1a2b
  Pointeur Urgent : 0
  Aucun payload
  ```

---

### Structures Clés
- **En-tête IP (`struct iphdr`)** :
  ```c
  struct iphdr {
      unsigned int ihl:4;    // Longueur de l'en-tête (en mots de 32 bits)
      unsigned int version:4;// Version IP (4 pour IPv4)
      uint8_t tos;           // Type de service
      uint16_t tot_len;      // Longueur totale
      uint16_t id;           // Identification
      uint16_t frag_off;     // Décalage du fragment
      uint8_t ttl;           // Time to live
      uint8_t protocol;      // Protocole (6 pour TCP)
      uint16_t check;        // Somme de contrôle
      uint32_t saddr;        // Adresse source
      uint32_t daddr;        // Adresse de destination
  };
  ```

- **En-tête TCP (`struct tcphdr`)** :
  ```c
  struct tcphdr {
      uint16_t source;       // Port source
      uint16_t dest;         // Port destination
      uint32_t seq;          // Numéro de séquence
      uint32_t ack_seq;      // Numéro d'acquittement
      uint16_t doff:4;       // Décalage des données (longueur de l'en-tête en mots de 32 bits)
      uint16_t res1:4;       // Réservé
      uint16_t res2:2;       // Réservé
      uint16_t urg:1;        // Drapeau Urgent
      uint16_t ack:1;        // Drapeau d'Acquittement
      uint16_t psh:1;        // Drapeau Push
      uint16_t rst:1;        // Drapeau Reset
      uint16_t syn:1;        // Drapeau de Synchronisation
      uint16_t fin:1;        // Drapeau de Fin
      uint16_t window;       // Taille de la fenêtre
      uint16_t check;        // Somme de contrôle
      uint16_t urg_ptr;      // Pointeur urgent
  };
  ```

---

### Notes
- **Privilèges Root** : Les sockets bruts nécessitent `sudo` car ils accèdent directement à la pile réseau.
- **Mode Promiscuous** : Ceci capture uniquement les paquets destinés à l'hôte. Pour tout le trafic (comme Wireshark), vous auriez besoin de `libpcap` ou d'une approche différente (par exemple, des sockets `PF_PACKET` avec mode promiscuous).
- **Ordre des Octets** : L'ordre des octets du réseau (big-endian) est converti en ordre des octets de l'hôte en utilisant `ntohs` (16 bits) et `ntohl` (32 bits).
- **Limitations** : Ce programme ne valide pas la somme de contrôle et ne gère pas les paquets fragmentés.

Faites-moi savoir si vous souhaitez affiner ceci davantage (par exemple, ajouter la validation de la somme de contrôle ou filtrer des ports spécifiques) !