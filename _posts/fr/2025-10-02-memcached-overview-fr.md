---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Présentation du système de mise en cache mémoire Memcached
translated: true
type: note
---

### Qu'est-ce que Memcached ?

Memcached est un système de cache d'objets en mémoire distribué, open source et haute performance. Il est principalement utilisé pour accélérer les applications web dynamiques (comme celles construites avec des frameworks PHP tels que CodeIgniter) en mettant en cache les résultats de requêtes de base de données, les réponses d'API ou d'autres données coûteuses en calcul dans la RAM. Cela réduit la charge sur les bases de données et améliore les temps de réponse des applications. Ce n'est pas une base de données complète mais un simple magasin clé-valeur conçu pour le stockage temporaire de données.

### Comment fonctionne Memcached ?

Memcached fonctionne comme un démon (processus en arrière-plan) qui s'exécute sur un ou plusieurs serveurs, généralement démarré avec des commandes comme `memcached -p 11211 -m 64` (spécifiant le port et la limite de mémoire). Voici un aperçu simplifié :

1. **Stockage en Mémoire** : Il stocke les données sous forme de paires clé-valeur entièrement en RAM pour un accès rapide. Chaque valeur peut atteindre 1 Mo, et les clés sont des chaînes de caractères jusqu'à 250 caractères. Les données sont volatiles — si le serveur redémarre, les données en cache sont perdues.

2. **Modèle Client-Serveur** : Les applications (clients) se connectent à Memcached via les protocoles TCP ou UDP. L'extrait de configuration CodeIgniter fourni montre une configuration PHP se connectant à une instance Memcached locale :
   - **Nom d'hôte** : '127.0.0.1' (localhost, signifiant le même serveur que votre application).
   - **Port** : '11211' (port par défaut de Memcached).
   - **Poids** : '1' (définit la priorité du serveur dans un cluster ; des valeurs plus élevées signifient plus de charge).

3. **Opérations** :
   - Set : Stocker une paire clé-valeur avec un temps d'expiration optionnel (par exemple, `set app_name 0 3600 13\n"cached_data"` via telnet).
   - Get : Récupérer une valeur par sa clé.
   - Delete : Supprimer par clé.
   Il utilise un algorithme de hachage simple pour répartir les clés sur les serveurs dans une configuration en cluster (par exemple, le hachage cohérent pour gérer les ajouts/suppressions de serveurs).

4. **Éviction et Mise à l'échelle** : Si la mémoire est pleine, il utilise une politique LRU (Least Recently Used) pour évincer les anciennes données. La mise à l'échelle implique plusieurs instances de serveur, souvent auto-découvertes via des outils comme moxi ou un partitionnement externe.

Les performances culminent à des millions d'opérations par seconde, mais il est optimisé pour les charges de travail principalement en lecture. Des outils de surveillance comme memcached-top peuvent suivre l'utilisation.

### Comparaison avec Redis

Bien que Memcached et Redis soient tous deux des magasins de données clé-valeur en mémoire utilisés pour la mise en cache et l'accès rapide aux données, ils diffèrent par leurs fonctionnalités, leur architecture et leurs cas d'utilisation :

| Aspect          | Memcached                              | Redis                                                  |
|-----------------|----------------------------------------|--------------------------------------------------------|
| **Types de Données** | Chaînes simples (juste des clés/valeurs). | Prend en charge les chaînes, les hachages, les listes, les ensembles, les ensembles triés, les bitmaps, les hyperloglogs, et plus encore. Permet des structures de données complexes (par exemple, des objets JSON ou des compteurs). |
| **Persistence**| Aucune — les données sont en RAM pure ; perdues au redémarrage. | Persistence optionnelle (AOF ou instantanés RDB) sur disque, permettant la récupération des données. |
| **Éviction**   | LRU uniquement.                        | Évictions basées sur LRU, LFU (Least Frequently Used) ou TTL volatile. |
| **Opérations** | Set/get/delete/multiget basiques.      | Des milliers de commandes (par exemple, pub/sub, transactions, script Lua, requêtes géospatiales). Prend en charge les opérations atomiques comme l'incrémentation. |
| **Performances**| Légèrement plus rapide pour la lecture/écriture simple (les multigets aident). | Excellentes en général, mais légèrement plus de surcharge pour les structures complexes. Les benchmarks montrent que Memcached prend l'avantage pour la mise en cache pure dans des scénarios à faible complexité. |
| **Mise à l'échelle & Clustering** | Intégrée via le hachage cohérent ; pas de clustering natif (utiliser un partitionnement externe). | Prend en charge le clustering natif, la réplication (maître-esclave) et Redis Cluster pour le partitionnement automatique. |
| **Cas d'Utilisation** | Idéal pour la mise en cache d'applications web (par exemple, les caches de session ou de requêtes), comme dans les configurations CodeIgniter. Simple et léger. | Plus large : mise en cache, stockage de session, files d'attente de messages, analyses en temps réel, ou même comme alternative complète à une base de données. |
| **Efficacité Mémoire** | Efficace pour les données de taille fixe ; pas de compression. | Meilleur pour les grands ensembles de données avec des options de compression (Redis 5+). |
| **Protocole**   | Protocoles personnalisés binaires/textes. | RESP (Redis Serialization Protocol) avec une meilleure gestion des erreurs. |
| **Licence & Écosystème** | Open-source (BSD), largement utilisé dans les piles LAMP. | Open-source (BSD), communauté plus large avec des outils comme RedisInsight. |

En résumé, choisissez Memcached pour la simplicité et la vitesse dans la mise en cache basique (comme illustré dans votre configuration CodeIgniter). Optez pour Redis si vous avez besoin de persistance, de types de données avancés ou de fonctionnalités comme la messagerie pub/sub. Si vous migrez depuis Memcached, des projets comme redis-memcached offrent des couches de compatibilité, mais Redis remplace souvent Memcached en raison de sa polyvalence. Pour CodeIgniter spécifiquement, la configuration permet un échange transparent entre les pilotes.