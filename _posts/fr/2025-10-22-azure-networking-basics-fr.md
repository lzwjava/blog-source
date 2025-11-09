---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principes de base de la mise en réseau virtuelle Azure
translated: true
type: note
---

### Notions de base sur les réseaux virtuels Azure

Azure fournit un environnement de mise en réseau évolutif et sécurisé grâce à son service **Réseau Virtuel (VNet)**, qui est l'équivalent fondamental d'AWS VPC. Il crée un espace privé et isolé dans le cloud Azure pour vos ressources telles que les machines virtuelles, les App Services ou les clusters Kubernetes. Ci-dessous, j'expliquerai les composants clés (réseau virtuel, passerelles, sous-réseaux, etc.) avec leurs similitudes et différences par rapport à AWS, structurés de manière similaire pour une comparaison facile.

#### Réseau Virtuel (VNet)
- **Ce que c'est** : Le réseau isolé fondamental dans Azure, couvrant une région et permettant aux ressources de communiquer en privé. Vous définissez son espace d'adressage avec des blocs CIDR (par exemple, 10.0.0.0/16).
- **Fonctionnalités clés** :
  - Accès Internet sortant par défaut pour les ressources (contrairement à AWS, où il est optionnel).
  - Prend en charge IPv4 et IPv6 ; isolé par défaut.
  - Aucun coût pour le VNet lui-même — payez pour les ressources attachées comme les passerelles.
- **Similaire à AWS VPC** : Les deux sont des clouds privés pour l'isolation des ressources, la mise à l'échelle et la connectivité. Les VNets Azure s'étendent automatiquement sur les zones de disponibilité (AZ) ; les VPC AWS nécessitent une configuration explicite des AZ.
- **Pourquoi l'utiliser ?** : Communication intra-ressources sécurisée, accès Internet et liaisons locales. Chaque abonnement Azure y a accès, mais vous créez des VNets personnalisés pour le contrôle.
- **Exemple** : Comme AWS VPC, c'est votre "domaine privé" dans le cloud — vous fixez les limites, mais Azure gère certains paramètres par défaut comme l'accès Internet sortant.

#### Sous-réseaux
- **Ce que c'est** : Des divisions de l'espace d'adressage d'un VNet, où les ressources sont déployées. Chaque sous-réseau est limité au VNet et peut s'étendre sur toutes les AZ d'une région.
- **Types** :
  - **Sous-réseau public** : Les ressources peuvent avoir des IP publiques pour un accès Internet entrant/sortant (via Azure Load Balancer ou des points de terminaison publics).
  - **Sous-réseau privé** : Aucun accès public direct ; idéal pour les bases de données ou les applications internes.
- **Fonctionnalités clés** :
  - Défini par CIDR (par exemple, 10.0.1.0/24).
  - Plusieurs par VNet pour la segmentation ; le trafic entre eux peut être filtré.
- **Similaire aux sous-réseaux AWS** : Les deux segmentent les réseaux pour la sécurité et l'organisation. L'extension automatique sur les AZ d'Azure simplifie la haute disponibilité ; AWS associe les sous-réseaux à des AZ spécifiques.
- **Pourquoi les utiliser ?** : Isole les charges de travail — par exemple, les frontends dans des sous-réseaux publics, les backends dans des sous-réseaux privés.
- **Exemple** : Les sous-réseaux sont des "quartiers" dans votre ville VNet : les publics avec un accès à la rue (Internet), les privés derrière des murs.

#### Passerelles
Les passerelles dans Azure gèrent la connectivité externe, mais avec certaines différences par défaut par rapport à AWS.

- **Équivalent Internet Gateway** :
  - **Ce que c'est** : Pas d'IGW direct ; l'accès Internet sortant est activé par défaut pour les ressources VNet. L'accès entrant nécessite une IP publique ou un Load Balancer.
  - **Comment ça marche** : Le trafic est acheminé via les routes système d'Azure (0.0.0.0/0 vers Internet). Utilisez des IP publiques pour un accès bidirectionnel.
  - **Similaire à AWS IGW** : Les deux permettent un accès Internet public, mais Azure est plus "toujours actif" pour le sortant ; AWS nécessite un attachement et des routes explicites.
  - **Pourquoi l'utiliser ?** : Exposition publique simple pour les applications web. Gratuit pour le routage de base.

- **Passerelle NAT** :
  - **Ce que c'est** : Un service managé dans un sous-réseau public pour un accès Internet sortant uniquement depuis des sous-réseaux privés (par exemple, mises à jour de machines virtuelles).
  - **Comment ça marche** : Partage une IP Élastique pour la traduction ; haute disponibilité sur plusieurs AZ.
  - **Similaire à AWS NAT Gateway** : Les deux fournissent un accès sortant sécurisé sans exposition entrante. Celui d'Azure est plus intégré et évolutif par défaut.
  - **Pourquoi l'utiliser ?** : Protège les ressources privées tout en permettant un accès unidirectionnel. Coûte ~0,045 $/heure + données.

- **Autres passerelles** :
  - **Passerelle VPN** : Pour les VPN site-à-site ou point-à-site vers des réseaux locaux (comme AWS VGW).
  - **Passerelle ExpressRoute** : Liaisons privées à haut débit vers des réseaux locaux (comme AWS Direct Connect).

#### Autres Composants Associés ("Etc.")
- **Tables de routage** : Contrôlent le flux de trafic des sous-réseaux (par exemple, vers Internet ou des VNets appairés). Des paramètres par défaut système existent ; les personnalisées les remplacent pour des routes spécifiques. Similaires aux tables de routage AWS, mais Azure propage dynamiquement les routes BGP depuis les réseaux locaux.
- **Groupes de sécurité réseau (NSG)** : Pare-feux avec état pour les sous-réseaux ou les ressources, avec des règles par IP/port/protocole. Comme un mélange des Groupes de Sécurité AWS (au niveau de l'instance, avec état) et des NACL (au niveau du sous-réseau, mais ceux d'Azure sont avec état). Utilisez les Groupes de sécurité d'application pour un étiquetage logique.
- **Appairage VNet** : Relie des VNets (mêmes/différentes régions/comptes) pour un trafic privé, comme l'appairage VPC AWS.
- **Points de terminaison de service/Liaison privée** : Accès privé sécurisé aux services Azure (par exemple, Stockage) sans Internet, similaire aux VPC Endpoints AWS.
- **Appliances virtuelles réseau** : Pare-feux ou routeurs basés sur des machines virtuelles dans le VNet, similaires à AWS Network Firewall.

#### Comment Tout Cela S'Assemble
1. Créez un VNet avec un CIDR.
2. Ajoutez des sous-réseaux (publics/privés) couvrant les AZ.
3. Les ressources obtiennent un accès Internet sortant par défaut ; ajoutez des IP publiques/Load Balancers pour l'accès entrant.
4. Utilisez une passerelle NAT pour le trafic sortant privé.
5. Appliquez des tables de routage et des NSG pour le contrôle du trafic.
6. Appairez des VNets ou ajoutez des passerelles pour des configurations hybrides.

Le modèle d'Azure met l'accent sur les paramètres par défaut (par exemple, l'Internet sortant) pour une configuration plus rapide, tandis qu'AWS offre des options d'adhésion plus granulaires. Les deux priorisent la sécurité et la résilience.

Pour une mise en pratique, essayez l'assistant VNet du portail Azure.

[Aperçu du réseau virtuel Azure](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)