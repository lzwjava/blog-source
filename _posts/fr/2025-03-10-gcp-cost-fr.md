---
audio: false
generated: true
lang: fr
layout: post
title: Estimation des coûts GCP pour le VPN à Taipei
translated: true
type: note
---

Pour estimer le coût d'utilisation d'un serveur situé à Taipei comme VPN avec Google Cloud, en considérant que vous habitez à Guangzhou et que vous prévoyez 50 Go de données réseau par mois en utilisant une instance E2 micro, nous devons décomposer les coûts en plusieurs composantes : l'instance de machine virtuelle (VM), le trafic sortant du réseau et le stockage sur disque persistant. Voici un calcul détaillé basé sur les tarifs de Google Cloud pour la région asia-east1 (Taipei), où votre serveur sera hébergé.

### 1. Coût de l'Instance VM (E2 Micro à Taipei)
L'E2 micro est un type de machine à cœurs partagés avec 0,25 vCPU et 1 Go de mémoire. Selon les tarifs de Google Cloud pour Compute Engine dans la région asia-east1 :
- **Tarif horaire pour E2 micro** : 0,0084 $ par heure.
- **Heures dans un mois** : En supposant qu'un mois typique compte 730 heures (une approximation standard basée sur 365 jours ÷ 12 mois ≈ 30,42 jours × 24 heures).
- **Coût mensuel** :  
  0,0084 $/heure × 730 heures ≈ 6,132 $.

Ainsi, faire fonctionner l'instance E2 micro en continu pendant un mois coûte approximativement **6,13 $**.

### 2. Coût du Trafic Sortant du Réseau
Puisque vous utilisez le serveur de Taipei comme VPN depuis Guangzhou, votre configuration implique l'exécution d'un serveur VPN (par exemple, OpenVPN) sur l'instance E2 micro, et non le service Cloud VPN de Google Cloud. Vos 50 Go de données réseau mensuelles représentent le trafic total traité par le VPN. Voici comment le trafic circule :
- **De votre appareil à Guangzhou vers le serveur VPN** : Il s'agit d'un trafic entrant vers Google Cloud (gratuit).
- **Du serveur VPN vers Internet** : Il s'agit d'un trafic sortant (facturé).
- **D'Internet vers le serveur VPN** : Il s'agit d'un trafic entrant (gratuit).
- **Du serveur VPN vers votre appareil** : Il s'agit d'un trafic sortant (facturé).

Si vos 50 Go désignent le trafic total du tunnel VPN (données envoyées depuis votre appareil plus les données reçues en retour), le trafic sortant facturé par Google Cloud inclut :
- Les données envoyées du serveur VPN vers Internet.
- Les données envoyées du serveur VPN vers votre appareil.

En supposant que les 50 Go représentent le total des données transférées (par exemple, vous envoyez des requêtes et recevez des réponses, comme lors de la navigation ou du streaming), le trafic sortant total est d'environ 50 Go. Cela simplifie l'estimation, car la répartition exacte entre les données envoyées et reçues dépend de l'utilisation (par exemple, le streaming implique plus de données reçues, tandis que les téléversements impliquent plus de données envoyées). Pour une utilisation générale d'Internet, nous considérerons les 50 Go comme le trafic sortant total.

Google Cloud facture la sortie Internet en fonction de la région source (asia-east1 pour Taipei) :
- **Tranche tarifaire** : Pour l'Asie (à l'exclusion de la Chine, de l'Inde, de l'Indonésie et des Philippines), le tarif est de 0,12 $ par Gio pour les premiers 1 To de trafic sortant mensuel.
- **Conversion** : Google Cloud utilise les Gio (1 Gio = 1024³ octets), tandis que vous avez spécifié 50 Go (1 Go = 1000³ octets). Précision, 1 Go ≈ 0,931 Gio, donc 50 Go ≈ 46,55 Gio. Cependant, pour des raisons de simplicité et selon la pratique courante pour les estimations approximatives, nous approximerons 50 Go ≈ 50 Gio, la différence étant mineure pour de petits volumes.
- **Coût du trafic sortant** :  
  50 Gio × 0,12 $/Gio = 6,00 $.

Ainsi, le coût du trafic sortant du réseau est d'environ **6,00 $** par mois.

### 3. Coût du Disque Persistant
L'instance E2 micro nécessite un disque de démarrage. Bien que le niveau gratuit de Google Cloud offre 30 Go de stockage sur disque persistant standard dans certaines régions des États-Unis, Taipei (asia-east1) n'est pas incluse, vous aurez donc des frais :
- **Taille du disque** : En supposant un disque persistant standard typique de 30 Go (vous pourriez utiliser moins, comme 10 Go, mais 30 Go est courant pour une VM de base).
- **Tarification** : 0,040 $ par Go et par mois dans asia-east1 pour un disque persistant standard.
- **Coût mensuel** :  
  30 Go × 0,040 $/Go = 1,20 $.

Le disque persistant ajoute **1,20 $** par mois.

### 4. Adresse IP Externe
Votre serveur VPN a besoin d'une adresse IP externe pour être accessible depuis Guangzhou. Pour les VM Compute Engine :
- Si l'IP est attachée à une VM en cours d'exécution, il n'y a pas de frais supplémentaires.
- Si elle est réservée mais inutilisée, il y a de petits frais (non applicable ici puisque la VM fonctionne en continu).

Puisque votre E2 micro utilisera l'adresse IP externe, ce coût est **inclus dans le prix de la VM**.

### Coût Total Estimé
En additionnant toutes les composantes :
- **Instance VM** : 6,13 $
- **Trafic sortant** : 6,00 $
- **Disque persistant** : 1,20 $
- **Adresse IP externe** : 0,00 $ (incluse)

**Total** : 6,13 $ + 6,00 $ + 1,20 $ = **13,33 $ par mois**.

### Notes Supplémentaires
- **Trafic entrant** : Gratuit, donc les données entrant dans la VM (de votre part ou d'Internet) n'engendrent aucun coût.
- **Aucun niveau gratuit** : Le niveau gratuit E2 micro s'applique uniquement à des régions spécifiques des États-Unis (pas Taipei), et les 1 Go de trafic sortant gratuit proviennent d'Amérique du Nord (pas d'Asie), en excluant les destinations en Chine, donc cela ne s'applique pas ici.
- **Hypothèses d'utilisation** : Les 13,33 $ supposent que les 50 Go représentent le trafic sortant total. S'il s'agit uniquement des données envoyées ou reçues, ajustez le coût du trafic sortant proportionnellement (par exemple, si 50 Go sont des données reçues, le trafic sortant vers vous est de 6,00 $, mais le trafic sortant vers Internet pourrait être moindre).
- **Pas de Cloud VPN** : Puisque vous exécutez votre propre logiciel VPN (par exemple, OpenVPN), il n'y a pas de frais supplémentaires pour la passerelle ou le tunnel Cloud VPN.

### Réponse Finale
Le coût estimé pour l'utilisation d'un serveur à Taipei (asia-east1) comme VPN sur Google Cloud avec une instance E2 micro, 50 Go de données réseau mensuelles et un disque de 30 Go est d'environ **13,33 $ par mois**. Cela inclut l'instance VM (6,13 $), le trafic sortant vers Internet et votre appareil (6,00 $), et le disque persistant (1,20 $).