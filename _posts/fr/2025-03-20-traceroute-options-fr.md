---
audio: false
generated: true
lang: fr
layout: post
title: Options de Traceroute
translated: true
type: note
---

Traceroute est un outil puissant pour diagnostiquer les chemins réseau, et bien que son utilisation de base soit simple, il offre des options avancées pour personnaliser son comportement. Ci-dessous, je vais décrire les options courantes et expliquer comment utiliser traceroute de manière avancée, en me concentrant sur des exemples pratiques. Les options exactes dépendent de votre système d'exploitation (par exemple, Windows utilise `tracert`, tandis que Linux/macOS utilisent `traceroute`), mais je couvrirai les plus universellement applicables.

### Utilisation de base
- **Linux/macOS** : `traceroute [destination]`
  - Exemple : `traceroute google.com`
- **Windows** : `tracert [destination]`
  - Exemple : `tracert google.com`

Cela affiche les sauts (routeurs) entre vous et la cible, ainsi que les temps aller-retour (RTT) pour chacun.

---

### Options courantes de Traceroute
Voici un aperçu des options principales, principalement pour la commande `traceroute` sur les systèmes de type Unix (Linux/macOS). La commande Windows `tracert` a moins d'options mais partage certains concepts.

1. **`-n` (Pas de résolution DNS)**  
   - Ignore la résolution des adresses IP en noms d'hôte, accélérant le processus et affichant les IP brutes.
   - Utilisation : `traceroute -n google.com`
   - Pourquoi : Utile lorsque la résolution DNS est lente ou si vous ne vous intéressez qu'aux IP.

2. **`-m [max_hops]` (Définir le nombre maximal de sauts)**  
   - Limite le nombre de sauts que traceroute vérifie avant d'abandonner (la valeur par défaut est souvent 30).
   - Utilisation : `traceroute -m 15 google.com`
   - Pourquoi : Évite les exécutions infinies si la cible est inaccessible ou très éloignée.

3. **`-q [nqueries]` (Nombre de requêtes par saut)**  
   - Définit le nombre de paquets envoyés par saut (la valeur par défaut est 3). Chaque requête affiche une valeur de latence.
   - Utilisation : `traceroute -q 1 google.com`
   - Pourquoi : Réduit l'encombrement de la sortie ou accélère le traçage ; augmentez-le pour obtenir des données de latence plus fiables.

4. **`-w [waittime]` (Temps d'attente par saut)**  
   - Définit combien de temps (en secondes) attendre une réponse avant de marquer un saut comme ayant expiré.
   - Utilisation : `traceroute -w 2 google.com`
   - Pourquoi : S'adapte aux réseaux lents ou réduit les délais sur les réseaux rapides.

5. **`-p [port]` (Spécifier le port, mode UDP)**  
   - Définit le port de destination pour le traceroute basé sur UDP (la valeur par défaut est souvent 33434+).
   - Utilisation : `traceroute -p 53 google.com`
   - Pourquoi : Cible des services spécifiques (par exemple, DNS sur le port 53) ou contourne les filtres bloquant l'ICMP.

6. **`-I` (Utiliser ICMP au lieu d'UDP)**  
   - Passe de l'UDP (par défaut sur de nombreux systèmes) aux paquets ICMP Echo Request.
   - Utilisation : `traceroute -I google.com`
   - Pourquoi : Certains réseaux bloquent l'UDP mais autorisent l'ICMP, améliorant la visibilité.

7. **`-T` (Mode TCP)**  
   - Utilise des paquets TCP au lieu d'UDP ou d'ICMP, souvent avec des paquets SYN.
   - Utilisation : `traceroute -T -p 80 google.com`
   - Pourquoi : Contourne les pare-feux qui bloquent l'ICMP/UDP ; idéal pour tracer vers les serveurs web (port 80 = HTTP).

8. **`-f [first_ttl]` (Commencer à un TTL spécifique)**  
   - Définit la valeur TTL initiale, ignorant les sauts précédents.
   - Utilisation : `traceroute -f 5 google.com`
   - Pourquoi : Se concentre sur une partie spécifique du chemin, par exemple au-delà de votre réseau local.

9. **`-g [gateway]` (Routage source lâche)**  
   - Force les paquets à passer par une passerelle spécifiée (si pris en charge par le réseau).
   - Utilisation : `traceroute -g 192.168.1.1 google.com`
   - Pourquoi : Teste des routes spécifiques ou contourne le routage par défaut.

10. **`-4` ou `-6` (Forcer IPv4 ou IPv6)**  
    - Restreint traceroute à IPv4 ou IPv6.
    - Utilisation : `traceroute -6 google.com`
    - Pourquoi : Garantit que vous testez un protocole spécifique, utile pour les réseaux double pile.

---

### Options de `tracert` sous Windows
Windows a moins d'options, mais voici les principales :
- **`-d`** : Pas de résolution DNS (comme `-n`).
- **`-h [max_hops]`** : Nombre maximal de sauts (comme `-m`).
- **`-w [timeout]`** : Temps d'attente en millisecondes (comme `-w`).
- Exemple : `tracert -d -h 20 google.com`

---

### Exemples d'utilisation avancée
Voici comment combiner les options pour des besoins spécifiques :

1. **Diagnostiquer une connexion lente**  
   - Objectif : Identifier où surviennent les pics de latence.
   - Commande : `traceroute -I -q 5 -w 1 google.com`
   - Pourquoi : ICMP pour la fiabilité, 5 requêtes pour de meilleures statistiques de latence, timeout d'1 seconde pour avancer rapidement.

2. **Contourner les restrictions d'un pare-feu**  
   - Objectif : Tracer vers un serveur web bloqué par des filtres ICMP.
   - Commande : `traceroute -T -p 443 google.com`
   - Pourquoi : TCP sur le port 443 (HTTPS) imite un trafic légitime, souvent autorisé à traverser les pare-feux.

3. **Tester au-delà de votre FAI**  
   - Objectif : Ignorer les sauts locaux pour se concentrer sur le routage externe.
   - Commande : `traceroute -f 3 -m 10 google.com`
   - Pourquoi : Commence au saut 3 (après votre routeur/FAI), limite à 10 sauts au total.

4. **Comparer les chemins IPv4 et IPv6**  
   - Objectif : Voir si le choix du protocole affecte le routage.
   - Commandes :
     - `traceroute -4 google.com`
     - `traceroute -6 google.com`
   - Pourquoi : Identifie les différences dans les chemins réseau ou les performances.

5. **Trace silencieuse et rapide pour les scripts**  
   - Objectif : Sortie rapide pour l'automatisation.
   - Commande : `traceroute -n -q 1 -w 1 google.com > output.txt`
   - Pourquoi : Pas de DNS, une requête, timeout court, redirigé vers un fichier.

---

### Conseils pour une utilisation avancée
- **Combiner avec d'autres outils** : Associez traceroute avec `ping` (pour la latence) ou `mtr` (traceroute en temps réel) pour une analyse plus approfondie.
- **Comprendre le contexte réseau** : Les pare-feux, la NAT ou les VPN peuvent masquer des sauts (affichant des astérisques `*`) — ajustez les protocoles (ICMP/TCP) pour vous adapter.
- **Privilèges root** : Sur les systèmes Unix, certaines options (par exemple, le mode TCP) peuvent nécessiter `sudo` pour l'accès aux sockets bruts : `sudo traceroute -T google.com`.

La puissance de traceroute réside dans sa flexibilité. En ajustant les options, vous pouvez l'adapter pour résoudre des problèmes réseau spécifiques, contourner des restrictions ou analyser le comportement du routage en détail. Faites-moi savoir si vous souhaitez approfondir un scénario particulier !