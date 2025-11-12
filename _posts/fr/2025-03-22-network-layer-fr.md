---
audio: false
generated: true
lang: fr
layout: post
title: Couche réseau
translated: true
type: note
---

D'accord, plongeons dans un tutoriel détaillé sur la couche réseau, spécifiquement adapté pour le cours de Technologie des Réseaux Informatiques du système d'examen en autodidacte chinois (自考). Ce chapitre est crucial pour comprendre comment les données voyagent à travers les réseaux.

## Tutoriel sur la Couche Réseau

La couche réseau est la troisième couche du modèle OSI et du modèle TCP/IP. Sa responsabilité principale est de faciliter le mouvement des paquets de données d'un hôte source vers un hôte de destination à travers un ou plusieurs réseaux. Considérez-la comme le service postal de l'internet – elle détermine le meilleur itinéraire et assure que votre "colis" (paquet de données) arrive à la bonne adresse.

Voici une répartition des sujets clés de ce chapitre :

### 1. Fonctions de la Couche Réseau

La couche réseau remplit trois fonctions principales :

#### a) Adressage Logique

* **Objectif :** Identifier de manière unique chaque hôte sur un réseau. Ceci est différent de l'adresse physique (adresse MAC) qui identifie un appareil au sein d'un réseau local. Les adresses logiques sont hiérarchiques et permettent un routage efficace.
* **Concept Clé :** Les adresses IP (adresses de protocole Internet) sont la forme principale d'adressage logique utilisée dans la couche réseau.
* **Analogie :** Pensez à votre adresse personnelle. C'est une adresse logique qui aide le service postal à trouver votre maison spécifique dans une ville et un pays, indépendamment de l'emplacement physique du bureau de poste.

#### b) Routage

* **Objectif :** Déterminer le meilleur chemin qu'un paquet de données doit emprunter pour aller de la source à la destination. Cela implique de sélectionner une séquence d'appareils réseau (routeurs) que le paquet va traverser.
* **Concept Clé :** Les algorithmes de routage sont utilisés par les routeurs pour construire et maintenir des tables de routage, qui contiennent des informations sur les meilleurs chemins vers différents réseaux.
* **Analogie :** Imaginez planifier un voyage en voiture. Vous consultez une carte ou utilisez un GPS pour déterminer le meilleur itinéraire vers votre destination, en tenant compte de facteurs comme la distance et le trafic. Les routeurs font quelque chose de similaire pour les paquets de données.

#### c) Forwarding (Acheminement)

* **Objectif :** Le processus réel de déplacement d'un paquet de données d'un port d'entrée d'un routeur vers le port de sortie approprié, basé sur la décision de routage.
* **Concept Clé :** Lorsqu'un routeur reçoit un paquet, il examine l'adresse IP de destination et consulte sa table de routage pour déterminer le saut suivant (un autre routeur ou l'hôte de destination).
* **Analogie :** Une fois que vous avez planifié votre itinéraire, l'acheminement, c'est comme conduire réellement votre voiture le long de cet itinéraire, passant d'un point à un autre.

### 2. Adressage IP

Les adresses IP sont fondamentales pour la couche réseau. Il existe deux versions principales : IPv4 et IPv6.

#### a) Structure IPv4

* **Format :** Une adresse numérique de 32 bits écrite en notation décimale pointée (par exemple, 192.168.1.10). Elle est divisée en quatre octets de 8 bits.
* **Classes d'Adresses (Historique) :** Bien que largement obsolètes maintenant en raison du CIDR, la compréhension des classes historiques (A, B, C, D, E) peut être utile pour les connaissances fondamentales.
    * **Classe A :** Grands réseaux (premier octet 1-126).
    * **Classe B :** Réseaux de taille moyenne (premier octet 128-191).
    * **Classe C :** Petits réseaux (premier octet 192-223).
    * **Classe D :** Adresses de multidiffusion (multicast) (premier octet 224-239).
    * **Classe E :** Réservée à un usage expérimental (premier octet 240-255).
* **ID de Réseau et ID d'Hôte :** Une adresse IPv4 se compose d'un ID de réseau (identifie le réseau) et d'un ID d'hôte (identifie un appareil spécifique dans ce réseau). La division entre ces IDs dépend de la classe d'adresse (ou du masque de sous-réseau en CIDR).
* **Adresses IPv4 Spéciales :**
    * **0.0.0.0 :** Représente le réseau courant.
    * **127.0.0.1 (Adresse de Loopback) :** Utilisée pour tester la pile réseau de la machine locale.
    * **Adresses IP Privées :** Plages réservées à un usage dans les réseaux privés (par exemple, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Ces adresses ne sont pas routables sur l'internet public.
    * **Adresses IP Publiques :** Adresses routables sur l'internet public.

#### b) Structure IPv6

* **Format :** Une adresse numérique de 128 bits écrite en format hexadécimal, regroupée en huit segments de 16 bits séparés par des deux-points (par exemple, 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
* **Avantages par rapport à IPv4 :** Espace d'adressage plus large (résout l'épuisement des adresses IPv4), sécurité améliorée (IPsec est souvent intégré), format d'en-tête simplifié, meilleure prise en charge des appareils mobiles.
* **Représentation des Adresses :**
    * **Zéros Non Significatifs :** Les zéros non significatifs dans un segment peuvent être omis (par exemple, 0000 peut être écrit 0).
    * **Double Deux-Points :** Un seul double deux-points (::) peut être utilisé pour représenter un ou plusieurs segments consécutifs de zéros. Cela ne peut être utilisé qu'une seule fois dans une adresse.
* **Types d'Adresses IPv6 :**
    * **Unicast :** Identifie une seule interface.
    * **Multicast :** Identifie un groupe d'interfaces.
    * **Anycast :** Identifie un ensemble d'interfaces, les paquets étant livrés à l'interface la plus proche de l'ensemble.
* **Adresses Link-Local (fe80::/10) :** Utilisées pour la communication au sein d'un seul lien réseau.
* **Adresses Globales Unicast :** Adresses routables globalement sur internet.

#### c) Subnetting (Sous-réseautage)

* **Objectif :** Diviser un réseau plus large en sous-réseaux (subnets) plus petits et plus gérables. Cela aide à organiser les réseaux, améliorer la sécurité et optimiser les performances du réseau.
* **Mécanisme :** Le sous-réseautage est réalisé en empruntant des bits de la partie hôte d'une adresse IP et en les utilisant pour créer des ID de sous-réseau. Cela se fait à l'aide d'un **masque de sous-réseau**.
* **Masque de Sous-Réseau :** Un nombre de 32 bits (pour IPv4) qui identifie les parties réseau et sous-réseau d'une adresse IP. Il a une séquence contiguë de 1 pour les bits réseau et sous-réseau, suivie d'une séquence contiguë de 0 pour les bits hôte.
* **Notation CIDR (Classless Inter-Domain Routing) :** Une manière plus flexible de représenter les préfixes de réseau en utilisant une barre oblique suivie du nombre de bits réseau (par exemple, 192.168.1.0/24 indique que les 24 premiers bits représentent le réseau). C'est la méthode standard utilisée aujourd'hui.
* **Calcul de Sous-Réseautage (IPv4) :**
    1.  Déterminer le nombre de sous-réseaux nécessaires.
    2.  Déterminer le nombre d'hôtes nécessaires par sous-réseau.
    3.  Calculer le nombre de bits requis pour les sous-réseaux et les hôtes.
    4.  Déterminer le masque de sous-réseau.
    5.  Identifier les adresses de sous-réseau valides, les adresses de diffusion (broadcast) et les plages d'hôtes utilisables pour chaque sous-réseau.
* **Sous-réseautage en IPv6 :** Bien que le concept de sous-réseautage existe en IPv6, le vaste espace d'adressage le rend moins axé sur la conservation des adresses et davantage sur l'organisation du réseau. Les sous-réseaux IPv6 ont généralement une taille fixe (/64).

### 3. Algorithmes de Routage

Les algorithmes de routage sont utilisés par les routeurs pour déterminer le meilleur chemin pour les paquets de données. Ils peuvent être classés en :

#### a) Routage Statique vs Dynamique

* **Routage Statique :**
    * Les tables de routage sont configurées manuellement par l'administrateur réseau.
    * Simple à mettre en œuvre pour les petits réseaux stables.
    * Non adaptable aux changements ou pannes du réseau.
    * Adapté à des scénarios spécifiques comme la connexion à un seul réseau distant.
* **Routage Dynamique :**
    * Les routeurs apprennent automatiquement la topologie du réseau et mettent à jour leurs tables de routage en échangeant des informations avec d'autres routeurs.
    * Plus complexe à configurer initialement mais très adaptable aux changements et pannes du réseau.
    * Évolutif pour les réseaux plus grands et plus complexes.

#### b) Routage à Vecteur de Distance

* **Principe :** Chaque routeur maintient une table de routage qui liste la meilleure distance connue (par exemple, le nombre de sauts) et la direction (routeur du prochain saut) vers chaque réseau de destination.
* **Échange d'Informations :** Les routeurs échangent périodiquement leurs tables de routage entières avec leurs voisins directement connectés.
* **Exemple d'Algorithme :** L'algorithme de **Bellman-Ford** est un algorithme courant utilisé dans les protocoles de routage à vecteur de distance.
* **Protocoles :** RIP (Routing Information Protocol) est un exemple bien connu de protocole de routage à vecteur de distance.
* **Limitations :** Peut souffrir d'une convergence lente (prend du temps pour que le réseau s'adapte aux changements) et du problème du "compte à l'infini" (des boucles de routage peuvent se produire).

#### c) Routage à État de Lien

* **Principe :** Chaque routeur maintient une carte complète de la topologie du réseau. Il connaît tous les routeurs et les liens entre eux, ainsi que le coût de chaque lien.
* **Échange d'Informations :** Les routeurs échangent des informations sur l'état de leurs liens directement connectés avec tous les autres routeurs du réseau. Cette information est appelée LSA (Link State Advertisement).
* **Exemple d'Algorithme :** L'**algorithme de Dijkstra** (Shortest Path First - SPF) est utilisé par chaque routeur pour calculer le chemin le plus court vers toutes les autres destinations basé sur les informations d'état de lien collectées.
* **Protocoles :** OSPF (Open Shortest Path First) et IS-IS (Intermediate System to Intermediate System) sont des protocoles de routage à état de lien populaires.
* **Avantages :** Convergence plus rapide, moins sujet aux boucles de routage par rapport au routage à vecteur de distance.

### 4. Protocoles

Plusieurs protocoles clés opèrent au niveau de la couche réseau :

#### a) IP (Internet Protocol)

* **Protocole de Base :** Le protocole fondamental responsable de l'adressage et du routage des paquets à travers les réseaux.
* **Sans Connexion et Non Fiable :** IP fournit un service sans connexion (aucun établissement de connexion préalable) et est non fiable (aucune garantie de livraison). La détection d'erreur est effectuée, mais la récupération d'erreur est de la responsabilité des protocoles de couches supérieures (comme TCP).
* **Format des Paquets :** IP définit la structure des paquets IP (datagrammes), y compris les adresses IP source et de destination, les informations d'en-tête (par exemple, time-to-live - TTL) et la charge utile (données des couches supérieures).

#### b) ICMP (Internet Control Message Protocol)

* **Objectif :** Utilisé pour envoyer des messages d'erreur et des messages de contrôle/d'information entre les appareils réseau.
* **Fonctionnalité :** Les messages ICMP sont utilisés pour signaler des erreurs (par exemple, destination inaccessible, temps dépassé), demander des informations (par exemple, demande/réponse d'écho utilisée par la commande `ping`) et effectuer d'autres diagnostics réseau.
* **Exemples :** L'utilitaire `ping` utilise les demandes et réponses d'écho ICMP pour tester la connectivité réseau. `traceroute` (ou `tracert` sur Windows) utilise les messages ICMP "time exceeded" pour tracer le chemin d'un paquet.

#### c) ARP (Address Resolution Protocol)

* **Objectif :** Utilisé pour résoudre une adresse logique (adresse IP) en une adresse physique (adresse MAC) au sein du même segment de réseau local.
* **Processus :** Lorsqu'un hôte doit envoyer un paquet à un autre hôte sur le même réseau, il connaît l'adresse IP de destination mais a besoin de l'adresse MAC de destination pour encadrer le paquet au niveau de la couche de liaison de données. L'hôte émetteur diffuse une requête ARP contenant l'adresse IP de destination. L'hôte avec cette adresse IP répond avec une réponse ARP contenant son adresse MAC.
* **Cache ARP :** Les hôtes maintiennent un cache ARP pour stocker les mappages adresse IP vers adresse MAC récemment résolus afin d'éviter d'envoyer des requêtes ARP pour chaque communication.

### 5. Appareils Réseau

La couche réseau implique principalement deux types clés d'appareils réseau :

#### a) Routeurs

* **Fonction Principale :** Acheminer les paquets de données entre différents réseaux en fonction de leurs adresses IP de destination.
* **Caractéristiques Clés :**
    * Maintiennent des tables de routage pour déterminer le meilleur chemin pour les paquets.
    * Connectent différents segments de réseau (peuvent être des technologies réseau différentes).
    * Effectuent l'acheminement des paquets basé sur les décisions de routage.
    * Peuvent mettre en œuvre des fonctionnalités de sécurité comme des pare-feu et des listes de contrôle d'accès (ACL).

#### b) Passerelles (Gateways)

* **Terme Plus Large :** Une passerelle est un appareil qui agit comme point d'entrée vers un autre réseau. Il peut s'agir d'un routeur, d'un pare-feu ou d'un autre type d'appareil.
* **Passerelle Par Défaut :** Dans le contexte du réseau IP, la passerelle par défaut est un routeur sur le réseau local qu'un hôte utilise pour envoyer le trafic vers des destinations en dehors de son propre réseau.
* **Conversion de Protocole :** Les passerelles peuvent également effectuer une conversion de protocole entre différentes architectures ou protocoles réseau, bien que cela soit moins courant pour le routage IP simple.

## Points Clés à Retenir pour l'Examen en Autodidacte

* **Comprendre les fonctions de base :** Adressage logique (adresses IP), routage (sélection du chemin) et forwarding (mouvement des paquets).
* **Maîtriser l'adressage IP :** Être capable d'expliquer la structure des adresses IPv4 et IPv6, comprendre les concepts de sous-réseautage et les calculs (surtout pour IPv4), et connaître les différents types d'adresses IP.
* **Différencier les algorithmes de routage :** Comprendre les différences entre le routage statique et dynamique, et être capable d'expliquer les principes de base des algorithmes de routage à vecteur de distance et à état de lien. Connaître les protocoles courants associés à chacun.
* **Connaître les protocoles clés de la Couche Réseau :** Comprendre l'objectif et le fonctionnement de base de IP, ICMP et ARP.
* **Identifier le rôle des appareils réseau :** Comprendre clairement la fonction des routeurs et des passerelles dans la couche réseau.

## Pratique et Révision

* **Travailler sur des exemples :** Pratiquez les calculs de sous-réseautage pour IPv4.
* **Comparer et contraster :** Créez des tableaux pour comparer les différents algorithmes de routage et les versions d'adresses IP.
* **Relier à des scénarios réels :** Réfléchissez à la manière dont ces concepts s'appliquent à votre propre utilisation d'internet et à vos configurations réseau.
* **Révisez les examens antérieurs :** Comprenez les types de questions typiquement posées sur ce sujet dans l'examen en autodidacte chinois.

En comprenant parfaitement ces concepts, vous construirez une base solide dans la couche réseau, ce qui est essentiel pour des études plus poussées en réseaux informatiques. Bonne chance dans vos études !