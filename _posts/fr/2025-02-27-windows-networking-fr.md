---
audio: false
generated: true
lang: fr
layout: post
title: Commandes de mise en réseau Windows
translated: true
type: note
---

Plongeons dans quelques commandes de réseau Windows utiles que vous pouvez exécuter dans l'invite de commandes (CMD) pour dépanner, collecter des informations ou gérer votre réseau. Je vais expliquer quelques-unes des plus populaires comme `getmac`, et j'ajouterai d'autres qui pourraient être utiles. Pas besoin d'être un expert en informatique — elles sont assez simples une fois qu'on les a comprises.

Pour commencer, ouvrez l'invite de commandes : appuyez sur `Touche Windows + R`, tapez `cmd`, et appuyez sur Entrée. Facile, n'est-ce pas ?

### 1. `getmac` - Trouvez votre adresse MAC
La commande `getmac` affiche l'adresse de contrôle d'accès au support (MAC) de vos cartes réseau — ces identifiants uniques pour votre appareil sur un réseau. Voici comment elle fonctionne :

- Tapez `getmac` et appuyez sur Entrée.
- Vous verrez une liste d'adresses MAC pour chaque carte réseau (comme Ethernet ou Wi-Fi).
- Ajoutez l'option `-v` (`getmac -v`) pour le mode verbeux, qui donne des détails supplémentaires comme le nom de la carte et le type de transport (par exemple, Ethernet ou Wireless).

Un exemple de résultat peut ressembler à ceci :
```
Adresse physique      Nom du transport
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
L'« Adresse physique » est votre MAC. Utile pour le dépannage réseau ou la configuration du filtrage MAC sur un routeur.

### 2. `ipconfig` - Vérifiez votre configuration IP
C'est une commande incontournable pour les informations réseau :
- Tapez `ipconfig` et appuyez sur Entrée pour voir les détails de base comme votre adresse IP, le masque de sous-réseau et la passerelle par défaut.
- Utilisez `ipconfig /all` pour une analyse complète, incluant les serveurs DNS, l'état DHCP et — oui — encore votre adresse MAC.

C'est idéal pour déterminer si votre appareil est correctement connecté ou s'il y a un conflit d'adresse IP.

### 3. `ping` - Testez la connectivité
Vous voulez vérifier si vous pouvez joindre un autre appareil ou un site web ?
- Tapez `ping [adresse]` (par exemple, `ping google.com` ou `ping 8.8.8.8`).
- Il envoie quelques paquets et vous dit s'ils reviennent, ainsi que le temps que cela a pris (en millisecondes).

Si vous obtenez « Délai d’attente de la demande dépassé », quelque chose bloque la connexion — cela peut être un pare-feu, un serveur hors service ou votre propre réseau.

### 4. `tracert` - Tracez l'itinéraire
Abréviation de "trace route", cette commande montre le chemin que vos données prennent pour atteindre une destination :
- Tapez `tracert [adresse]` (par exemple, `tracert google.com`).
- Elle liste chaque saut (routeur ou serveur) le long du chemin, avec les temps de réponse.

Pratique pour repérer où une connexion ralentit ou échoue.

### 5. `netstat` - Voir l'activité réseau
Celle-ci permet de vérifier ce qui se passe sur votre réseau en ce moment :
- Tapez `netstat -a` pour voir toutes les connexions actives et les ports en écoute.
- Ajoutez `-n` (`netstat -an`) pour afficher les adresses IP au lieu des noms d'hôte — plus rapide et plus brut.

C'est comme une fenêtre sur ce à quoi votre ordinateur parle — utile pour repérer une activité suspecte.

### 6. `nslookup` - Creusez dans le DNS
Si les sites web ne se chargent pas, cette commande vérifie la résolution du système de noms de domaine (DNS) :
- Tapez `nslookup [domaine]` (par exemple, `nslookup google.com`).
- Elle retourne l'adresse IP liée à ce domaine, montrant si votre DNS fonctionne.

### Astuces pour que tout se passe mieux
- Exécutez CMD en tant qu'Administrateur (clic droit sur Invite de commandes > « Exécuter en tant qu'administrateur ») si une commande nécessite des privilèges élevés.
- Combinez les commandes avec `|` (pipe) pour filtrer — par exemple, `getmac | find "00-14"` pour rechercher une MAC spécifique.
- Si vous êtes bloqué, tapez `[commande] /?` (par exemple, `ipconfig /?`) pour obtenir de l'aide sur cette commande.

Ce sont vos outils de base pour explorer un réseau Windows. Vous voulez vous concentrer sur une — comme `getmac` — ou essayer quelque chose de spécifique ? Faites-moi savoir ce que vous visez !