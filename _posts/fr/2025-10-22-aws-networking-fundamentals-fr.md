---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principes fondamentaux de la mise en réseau virtuel AWS
translated: true
type: note
---

### Notions de base de la mise en réseau virtuelle AWS

AWS fournit un environnement de mise en réseau flexible et isolé via son service **Virtual Private Cloud (VPC)**. Celui-ci agit comme votre propre section logiquement isolée du Cloud AWS, où vous pouvez lancer des ressources telles que des instances EC2, des bases de données RDS, et plus encore. Ci-dessous, je décompose les composants clés que vous avez mentionnés (réseau virtuel, passerelle, sous-réseaux) et quelques autres connexes ("etc.") en termes simples, avec la façon dont ils s'assemblent.

#### Réseau Virtuel (VPC - Virtual Private Cloud)
- **Ce que c'est** : Le fondement de la mise en réseau AWS. Un VPC est un réseau virtuel dédié à votre compte AWS, similaire à un réseau de centre de données traditionnel mais dans le cloud. Il s'étend sur une ou plusieurs Zones de Disponibilité (AZ) dans une région.
- **Caractéristiques clés** :
  - Vous définissez sa plage d'adresses IP en utilisant des blocs CIDR (par exemple, 10.0.0.0/16, qui permet ~65 000 adresses IP).
  - Il est isolé par défaut — aucun trafic n'entre ou ne sort sauf si vous le configurez.
  - Prend en charge IPv4 et IPv6.
- **Pourquoi l'utiliser ?** : Contrôle l'accès, la sécurité et la connectivité pour vos ressources. Chaque compte AWS obtient un VPC par défaut, mais vous pouvez en créer des personnalisés pour les environnements de production.
- **Exemple** : Considérez un VPC comme votre jardin privé dans le "quartier" AWS — vous décidez des clôtures, des portes et des chemins à l'intérieur.

#### Sous-réseaux
- **Ce que c'est** : Des subdivisions de la plage d'adresses IP d'un VPC. Chaque sous-réseau est lié à une seule Zone de Disponibilité et agit comme une zone segmentée au sein de votre réseau.
- **Types** :
  - **Sous-réseau public** : Les ressources ici peuvent accéder directement à Internet (via une passerelle Internet).
  - **Sous-réseau privé** : Isolé de l'accès direct à Internet ; utilisé pour des ressources sensibles comme les bases de données.
- **Caractéristiques clés** :
  - La taille est définie par CIDR (par exemple, 10.0.1.0/24 pour ~250 IP).
  - Vous pouvez avoir plusieurs sous-réseaux par AZ pour la haute disponibilité.
  - Les ressources (par exemple, les instances EC2) sont lancées dans un sous-réseau.
- **Pourquoi les utiliser ?** : Améliore la sécurité et la tolérance aux pannes — par exemple, placez les serveurs web dans des sous-réseaux publics et les serveurs d'applications dans des sous-réseaux privés.
- **Exemple** : Si votre VPC est une ville, les sous-réseaux sont des quartiers : les publics près de l'autoroute (Internet), les privés dans des communautés fermées.

#### Passerelles
Les passerelles connectent votre VPC au monde extérieur ou à d'autres réseaux. Il en existe plusieurs types :

- **Passerelle Internet (IGW)** :
  - **Ce que c'est** : Un composant hautement disponible qui s'attache à votre VPC, permettant une communication bidirectionnelle avec l'Internet public.
  - **Comment ça marche** : Achemine le trafic des sous-réseaux publics vers Internet (et vice versa). Nécessite des mises à jour des tables de routage pour diriger le trafic (par exemple, 0.0.0.0/0 → igw-xxxx).
  - **Pourquoi l'utiliser ?** : Pour les applications accessibles au public comme les sites web. C'est gratuit et s'adapte automatiquement.
  - **Exemple** : La porte d'entrée vers Internet — attachez-la, mettez à jour les routes, et vos ressources publiques peuvent naviguer ou être consultées.

- **Passerelle NAT (Network Address Translation)** :
  - **Ce que c'est** : Se trouve dans un sous-réseau public et permet aux ressources des sous-réseaux privés d'initier un trafic Internet sortant (par exemple, pour les mises à jour logicielles) sans les exposer au trafic entrant.
  - **Comment ça marche** : Traduit les IP privées en une IP publique élastique. Plus fiable que les instances NAT.
  - **Pourquoi l'utiliser ?** : Accès sortant sécurisé pour les ressources privées. Coûte ~0,045 $/heure + transfert de données.
  - **Exemple** : Une valve à sens unique — les serveurs privés peuvent "appeler" pour récupérer des paquets, mais personne ne peut frapper sans invitation.

- **Autres passerelles** (brièvement) :
  - **Passerelle Privée Virtuelle (VGW)** : Pour les connexions VPN à votre réseau sur site.
  - **Passerelle de Transit** : Connecte plusieurs VPC et réseaux sur site comme un hub.

#### Autres Composants Connexes ("Etc.")
- **Tables de Routage** : Définissent comment le trafic est acheminé au sein de votre VPC (par exemple, vers IGW, NAT, ou des connexions de peering). Chaque sous-réseau a une table de routage associée — considérez-la comme une carte de trafic.
- **ACL Réseau (Listes de Contrôle d'Accès)** : Pare-feux sans état au niveau du sous-réseau, contrôlant le trafic entrant/sortant par IP/protocole (par exemple, autoriser le port 80).
- **Groupes de Sécurité** : Pare-feux avec état au niveau de l'instance, agissant comme des videurs personnels pour EC2/RDS (par exemple, autoriser SSH depuis votre IP).
- **Peering VPC** : Connecte deux VPC (même dans différents comptes/régions) pour une communication privée, comme un tunnel direct.
- **Interfaces Réseau Élastiques (ENI)** : Cartes réseau virtuelles pour les instances, permettant plusieurs IPs ou attachements.

#### Comment Tout Cela S'Assemble
1. Créez un VPC avec un bloc CIDR.
2. Ajoutez des sous-réseaux (publics/privés) à travers les AZ.
3. Attachez une Passerelle Internet pour l'accès public.
4. Configurez les tables de routage pour diriger le trafic (par exemple, les sous-réseaux publics routent vers IGW).
5. Lancez des ressources dans les sous-réseaux et sécurisez-les avec des Groupes de Sécurité/NACL.
6. Pour le trafic sortant privé, ajoutez une Passerelle NAT.

Cette configuration assure l'évolutivité, la sécurité et la résilience. Pour une approche pratique, commencez par l'assistant VPC AWS dans la console — il configure automatiquement une installation de base.

Si vous avez besoin de diagrammes, d'exemples de code ou de détails sur une partie spécifique (par exemple, le peering), faites-le moi savoir !

**Références**:
- [Documentation AWS VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Guide des Sous-réseaux AWS](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [Aperçu des Passerelles AWS](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)