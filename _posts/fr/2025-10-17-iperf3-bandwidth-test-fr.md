---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Outil de Test de Bande Passante Réseau iPerf3
translated: true
type: note
---

### Qu'est-ce qu'iPerf3 ?

iPerf3 est un outil en ligne de commande open-source conçu pour mesurer la bande passante et les performances du réseau. Il est couramment utilisé pour tester le débit maximal réalisable sur les réseaux IP en simulant du trafic entre deux points terminaux (l'un agissant comme un serveur et l'autre comme un client). Cela aide à diagnostiquer des problèmes comme la latence, la perte de paquets et les goulots d'étranglement dans les réseaux locaux ou étendus.

#### Principales fonctionnalités :
- **Protocoles supportés** : TCP, UDP et SCTP pour des scénarios de test flexibles.
- **Personnalisation** : Permet de régler des paramètres comme la taille des tampons, la durée des tests et le trafic bidirectionnel.
- **Sortie** : Fournit des statistiques détaillées sur la bande passante, le gigue et la perte de datagrammes.

#### Exemple d'utilisation basique :
Pour tester la bande passante entre deux machines :
1. Sur le serveur : `iperf3 -s` (démarre le serveur).
2. Sur le client : `iperf3 -c <IP_du_serveur>` (se connecte et exécute un test de 10 secondes par défaut).

C'est un outil léger, multiplateforme (fonctionne sur Linux, Windows, macOS) et largement utilisé par les administrateurs réseau, les développeurs et les professionnels de l'informatique pour le dépannage.

#### Historique :
iPerf3 est une réécriture complète de l'outil iPerf original, commencée en 2009 par ESnet (Energy Sciences Network) et première version publiée en 2014. La refonte visait une base de code plus petite et plus maintenable tout en améliorant la précision.

Pour plus de détails, consultez le site officiel ou le dépôt GitHub.

### Références
- [iPerf - The TCP, UDP and SCTP network bandwidth measurement tool](https://iperf.fr/)
- [iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool](https://github.com/esnet/iperf)
- [Iperf - Wikipedia](https://en.wikipedia.org/wiki/Iperf)