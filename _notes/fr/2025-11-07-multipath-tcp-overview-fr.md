---
audio: false
generated: true
image: false
lang: fr
layout: post
model: moonshotai/kimi-k2-thinking
title: Aperçu du protocole TCP multipath
translated: true
---

Le MPTCP est une extension du protocole de couche transport qui modifie fondamentalement le fonctionnement des connexions réseau en permettant à une connexion logique unique d'utiliser simultanément plusieurs chemins physiques. Voici une analyse détaillée :

## **1. Le problème central : Les limitations du chemin unique**

Le TCP traditionnel restreint chaque connexion à un seul chemin réseau défini par un 5-uplet (IP source, port source, IP de destination, port de destination, protocole). Cela crée plusieurs limitations critiques :

- **Aucune agrégation d'interface** : Un appareil avec à la fois le Wi-Fi et le cellulaire ne peut utiliser qu'une seule interface à la fois
- **Point de défaillance unique** : Si le chemin choisi devient congestionné ou tombe en panne, la connexion entière est interrompue
- **Utilisation sous-optimale des ressources** : Les chemins alternatifs non congestionnés restent inactifs tandis qu'un chemin est saturé
- **Perturbation de la mobilité** : Changer de réseau (par exemple, du Wi-Fi à la 4G) nécessite de rétablir toutes les connexions

Les appareils modernes sont intrinsèquement multi-hébergés—les smartphones, ordinateurs portables et serveurs ont plusieurs interfaces réseau—mais le TCP ne peut pas tirer parti de cette diversité.

## **2. Comment fonctionne le MPTCP : L'architecture des sous-flux**

Le MPTCP (RFC 8684) n'est **pas** un nouveau protocole mais une extension rétrocompatible du TCP. Il fonctionne en créant des **sous-flux**—des connexions TCP indépendantes sur différents chemins—qui forment collectivement une connexion logique MPTCP.

### Processus d'établissement de la connexion :

1. **Poignée de main initiale** : Le client et le serveur négocient la capacité MPTCP pendant la poignée de main TCP standard en trois étapes
2. **Découverte des chemins** : Les pairs échangent les adresses IP supplémentaires qu'ils peuvent utiliser
3. **Création de sous-flux** : Des connexions TCP supplémentaires sont établies sur les interfaces/chemins disponibles
4. **Distribution des données** : Un **ordonnanceur** répartit le flux d'octets de l'application sur les sous-flux
5. **Réassemblage** : Le récepteur utilise des numéros de séquence au niveau de la connexion pour réorganiser les données provenant de multiples sous-flux dans la séquence originale

```
TCP traditionnel : Données App → Flux TCP unique → Un chemin
MPTCP : Données App → Ordonnanceur → Multiples sous-flux TCP → Chemins multiples → Réassemblage
```

Vous pouvez visualiser cela sur Linux avec `ss -M`, qui montre les sous-flux groupés sous une connexion MPTCP.

## **3. Mécanismes clés pour la performance**

### **Agrégation de bande passante**
Le MPTCP peut combiner le débit de tous les chemins disponibles. Un flux de 9 Mbps pourrait être divisé en trois sous-flux de 3 Mbps sur différentes interfaces, utilisant ainsi efficacement toute la capacité du réseau. Ceci est particulièrement puissant dans les centres de données où plusieurs liaisons physiques existent entre les serveurs.

### **Ordonnancement intelligent**
L'ordonnanceur surveille continuellement :
- La latence et la congestion du chemin
- Les taux de perte de paquets
- La bande passante disponible
- Le coût/priorité de la liaison

Il ajuste dynamiquement la quantité de données à envoyer sur chaque sous-flux, évitant de surcharger les chemins lents tout en utilisant pleinement les chemins rapides.

### **Contrôle de congestion couplé**
Le MPTCP utilise des algorithmes spécialisés (comme LIA, OLIA, BALIA) qui :
- Équilibrent la congestion sur les chemins
- Assurent l'équité avec les flux TCP réguliers
- Empêchent une seule connexion MPTCP d'affamer les autres trafics
- Réagissent de manière appropriée lorsqu'un chemin devient congestionné

## **4. Avantages : Résilience et débit**

### **Résilience améliorée**
- **Basculement automatique** : Si le Wi-Fi tombe, les sous-flux cellulaires maintiennent la connexion sans interruption de l'application
- **Redondance des chemins** : La perte de paquets sur un chemin ne rompt pas la connexion—le trafic est redirigé vers les sous-flux sains
- **Dégradation gracieuse** : Les défaillances partielles de chemin réduisent la bande passante mais ne provoquent pas de déconnexions
- **Temps de récupération** : Les simulations montrent que le MPTCP minimise les perturbations en déplaçant rapidement le trafic vers des chemins alternatifs

### **Débit amélioré**
- **Regroupement des ressources** : Utilise toutes les ressources réseau disponibles simultanément
- **Évitement de la congestion** : Contourne les goulots d'étranglement en utilisant des chemins alternatifs moins congestionnés
- **Équilibrage de charge** : Répartit le trafic pour empêcher qu'un seul chemin ne devienne un goulot d'étranglement

### **Mobilité transparente**
Apple utilise le MPTCP depuis iOS 7 pour Siri, permettant aux requêtes vocales de se poursuivre sans interruption lors du passage entre les réseaux Wi-Fi et cellulaires. La connexion persiste parce que les sous-flux sont ajoutés et supprimés dynamiquement au fur et à mesure que les interfaces deviennent disponibles ou indisponibles.

## **5. Cas d'utilisation réels**

- **Appareils mobiles** : Les smartphones changent de réseau de manière transparente
- **Centres de données** : Exploitent la diversité des chemins pour un débit plus élevé et une tolérance aux pannes
- **Systèmes IoT/M2M** : Maximisent l'utilisation des ressources dans les appareils à interfaces multiples
- **Réseaux hybrides** : Combinaison de réseaux fixes haut débit et mobiles pour des transferts de fichiers plus rapides
- **Services cloud** : Réseaux de diffusion de contenu et environnements d'entreprise nécessitant une haute disponibilité

## **6. Implémentation et adoption**

### **Support du système d'exploitation**
- **Linux** : Support complet du noyau avec le démon `mptcpd` (RHEL 9+, distributions modernes)
- **iOS** : Utilisé pour Siri et certaines applications depuis 2013
- **Android** : Support partiel dans les versions récentes
- **Windows** : Support natif limité

### **Transparence applicative**
Les applications nécessitent généralement **aucune modification**—la pile réseau du système d'exploitation gère le MPTCP de manière transparente. Seules des modifications mineures des options de socket peuvent être nécessaires pour les fonctionnalités avancées.

### **Statut du déploiement**
Le MPTCP est encore en maturation. Bien qu'Apple l'utilise en interne, la plupart des services Internet ne le supportent pas encore. L'adoption nécessite un support à la fois du client et du serveur, bien que le retour au TCP régulier soit automatique.

## **7. Compromis et défis**

### **Complexité**
- Machine à états de protocole plus complexe
- Support limité des middlebox—certains pare-feu/NAT peuvent bloquer les options MPTCP
- Le dépannage réseau devient plus difficile

### **Implications pour la sécurité**
- **Angles morts d'inspection** : Les pare-feu et systèmes IPS ont du mal à réassembler les flux divisés, créant des lacunes de sécurité
- **Occultation des modèles de trafic** : Bien que cela puisse améliorer la confidentialité, cela complique la surveillance de la sécurité
- **Produits Cisco** : De nombreuses fonctionnalités d'inspection ne supportent pas le MPTCP, nécessitant une configuration minutieuse

### **Considérations de performance**
- **Réorganisation des paquets** : Les latences différentes des chemins peuvent provoquer des arrivées désordonnées, nuisant potentiellement aux performances si elles ne sont pas gérées correctement
- **Blocage en tête de ligne** : Les sous-flux lents peuvent retarder la livraison globale si l'ordonnanceur n'est pas intelligent
- **Exigences de tampon** : Plus de mise en mémoire tampon nécessaire au niveau du récepteur pour réorganiser les paquets

### **Équité**
Le contrôle de congestion couplé du MPTCP doit soigneusement équilibrer l'agressivité multi-chemin avec l'équité envers les flux TCP à chemin unique sur les liaisons partagées.

## **8. Comparaison avec les technologies similaires**

- **Liaison agrégée/teaming** : Opère au niveau de la couche 2, nécessite typiquement le même support et n'aide pas les connexions TCP uniques
- **Multi-Path à Coût Égal (ECMP)** : Routage au niveau de la couche réseau qui divise les flux, mais ne peut pas diviser une connexion *unique*
- **SCTP** : Protocole de transport alternatif avec multi-hébergement mais mauvaise adoption et problèmes de traversée de NAT

L'avantage clé du MPTCP est de fonctionner dans l'écosystème TCP existant tout en fournissant un véritable multi-chemin au **niveau de la connexion**.

---

**Conclusion** : Le MPTCP transforme le modèle TCP rigide à chemin unique en une architecture flexible, résiliente et axée sur la performance en regroupant intelligemment de multiples ressources réseau. Bien que des défis subsistent concernant la maturité et la sécurité, il représente la solution la plus pratique pour tirer parti des terminaux multi-hébergés dans les réseaux modernes.