---
audio: true
lang: fr
layout: post
title: Commandes Réseau Windows
translated: true
---

Plongeons dans quelques commandes de réseau Windows utiles que vous pouvez exécuter dans l'invite de commandes (CMD) pour dépanner, recueillir des informations ou gérer votre réseau. Je vais expliquer quelques-unes des plus populaires comme `getmac`, et en ajouter d'autres qui pourraient être utiles. Vous n'avez pas besoin d'être un expert en technologie—ce sont assez simples une fois que vous avez pris le coup.

Tout d'abord, pour utiliser ces commandes, ouvrez l'invite de commandes : appuyez sur `Windows Key + R`, tapez `cmd`, et appuyez sur Entrée. C'est assez simple, non ?

### 1. `getmac` - Trouver votre adresse MAC
La commande `getmac` affiche l'adresse de contrôle d'accès au support (MAC) de vos adaptateurs réseau—ces identifiants uniques pour votre appareil sur un réseau. Voici comment cela fonctionne :

- Tapez `getmac` et appuyez sur Entrée.
- Vous verrez une liste d'adresses MAC pour chaque adaptateur réseau (comme Ethernet ou Wi-Fi).
- Ajoutez le commutateur `-v` (`getmac -v`) pour le mode verbeux, qui donne des détails supplémentaires comme le nom de l'adaptateur et le type de transport (par exemple, Ethernet ou sans fil).

La sortie de l'exemple pourrait ressembler à ceci :
```
Physical Address    Transport Name
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
L'adresse "Physical Address" est votre MAC. Utile pour le dépannage réseau ou la configuration du filtrage MAC sur un routeur.

### 2. `ipconfig` - Vérifier votre configuration IP
C'est une commande de base pour les informations réseau :
- Tapez `ipconfig` et appuyez sur Entrée pour voir des détails de base comme votre adresse IP, le masque de sous-réseau et la passerelle par défaut.
- Utilisez `ipconfig /all` pour une analyse complète, y compris les serveurs DNS, le statut DHCP et—oui—votre adresse MAC à nouveau.

C'est idéal pour savoir si votre appareil est correctement connecté ou s'il y a un conflit d'IP.

### 3. `ping` - Tester la connectivité
Vous voulez vérifier si vous pouvez atteindre un autre appareil ou un site web ?
- Tapez `ping [adresse]` (par exemple, `ping google.com` ou `ping 8.8.8.8`).
- Il envoie quelques paquets et vous dit s'ils reviennent, ainsi que le temps que cela prend (en millisecondes).

Si vous obtenez "Request timed out," quelque chose bloque la connexion—ce pourrait être un pare-feu, un serveur mort ou votre propre réseau.

### 4. `tracert` - Tracer l'itinéraire
Court pour "trace route," cela montre le chemin que prennent vos données vers une destination :
- Tapez `tracert [adresse]` (par exemple, `tracert google.com`).
- Il liste chaque saut (routeur ou serveur) le long du chemin, avec les temps de réponse.

Pratique pour repérer où une connexion ralentit ou échoue.

### 5. `netstat` - Voir l'activité réseau
Celle-ci est pour vérifier ce qui se passe sur votre réseau en ce moment :
- Tapez `netstat -a` pour voir toutes les connexions actives et les ports à l'écoute.
- Ajoutez `-n` (`netstat -an`) pour afficher les adresses IP au lieu des noms d'hôtes—plus rapide et plus brut.

C'est comme une fenêtre sur ce que votre ordinateur dit—utile pour repérer une activité suspecte.

### 6. `nslookup` - Plonger dans le DNS
Si les sites web ne se chargent pas, cela vérifie la résolution du système de noms de domaine (DNS) :
- Tapez `nslookup [domaine]` (par exemple, `nslookup google.com`).
- Il retourne l'adresse IP liée à ce domaine, montrant si votre DNS fonctionne.

### Conseils pour faciliter les choses
- Exécutez CMD en tant qu'administrateur (clic droit sur l'invite de commandes > "Exécuter en tant qu'administrateur") si une commande nécessite des privilèges élevés.
- Combinez les commandes avec `|` (pipe) pour le filtrage—par exemple, `getmac | find "00-14"` pour rechercher une adresse MAC spécifique.
- Si vous êtes bloqué, tapez `[commande] /?` (par exemple, `ipconfig /?`) pour obtenir de l'aide sur cette commande.

Ce sont vos outils de base pour explorer un réseau Windows. Vous voulez vous concentrer sur un outil—comme `getmac`—ou essayer quelque chose de spécifique ? Faites-moi savoir ce que vous visez !