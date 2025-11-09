---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de test de serveur Web Apache Bench
translated: true
type: note
---

### Qu'est-ce que Apache Bench (ab) ?

Apache Bench (ab) est un outil en ligne de commande simple inclus avec Apache HTTP Server pour évaluer les performances des serveurs web. Il envoie un nombre spécifié de requêtes HTTP à une URL et mesure des métriques comme le nombre de requêtes par seconde, le temps par requête, les débits de transfert et les taux d'erreur. Il est excellent pour des tests de charge rapides mais est limité pour des scénarios complexes (par exemple, pas de support HTTPS par défaut ou de script avancé — envisagez des outils comme JMeter pour ceux-ci).

### Installation

ab est fourni avec Apache HTTP Server. Voici comment l'installer :

- **Sur Ubuntu/Debian (Linux)** :
  ```
  sudo apt update
  sudo apt install apache2-utils
  ```

- **Sur macOS (via Homebrew)** :
  ```
  brew install httpd
  ```

- **Sur Windows** :
  Téléchargez Apache HTTP Server depuis le site officiel et ajoutez son répertoire `bin` à votre PATH.

- **Vérifier l'installation** :
  Exécutez `ab -V` pour vérifier la version.

### Utilisation de base

La syntaxe de commande principale est :
```
ab [options] URL
```

- **Format de l'URL** : Doit être une URL HTTP complète, par exemple `http://example.com/`. (Pour HTTPS, utilisez un wrapper comme `openssl s_client` ou passez à des outils comme `wrk`.)

Options clés :
- `-n <requests>` : Nombre de requêtes à effectuer (par défaut : 1). Commencez par 100–1000 pour les tests.
- `-c <concurrency>` : Nombre de requêtes multiples à effectuer simultanément (par défaut : 1). Gardez-le bas (par exemple, 10–50) pour ne pas submerger votre serveur.
- `-t <seconds>` : Exécuter pendant une durée spécifiée au lieu d'un nombre de requêtes.
- `-k` : Activer HTTP Keep-Alive (réutilise les connexions).
- `-H "Header: Value"` : Ajouter des en-têtes personnalisés (par exemple, pour l'authentification).
- `-p <file>` : Données POST à partir d'un fichier.
- `-T <content-type>` : Type de contenu pour les requêtes POST.
- `-l` : Accepter des longueurs de document variables (pour le contenu dynamique).

### Exemple pas à pas

1. **Tester une requête GET simple** :
   Simuler 100 requêtes avec 10 utilisateurs concurrents contre un serveur local :
   ```
   ab -n 100 -c 10 http://localhost:8080/
   ```
   Exemple de sortie :
   ```
   Server Software:        Apache/2.4.41
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /
   Document Length:        1234 bytes

   Concurrency Level:      10
   Time taken for tests:   1.234 seconds
   Complete requests:      100
   Failed requests:        0
   Requests per second:    81.03 [#/sec] (mean)
   Time per request:       123.456 [ms] (mean)
   ```

2. **Tester avec des données POST** (par exemple, soumission de formulaire) :
   Créez un fichier `postdata.txt` avec votre charge utile (par exemple, `key=value`).
   ```
   ab -n 50 -c 5 -p postdata.txt -T application/x-www-form-urlencoded http://example.com/api/endpoint
   ```

3. **Exécuter pendant une durée** :
   ```
   ab -n 10000 -c 20 -t 30 http://example.com/  # Jusqu'à 10k requêtes ou 30 secondes
   ```

### Interprétation des résultats

- **Requêtes par seconde** : Plus c'est élevé, mieux c'est (débit).
- **Temps par requête** : Plus c'est bas, mieux c'est (latence).
- **Débit de transfert** : Efficacité de la bande passante.
- Surveillez les "Failed requests" ou "Non-2xx responses" pour détecter des problèmes.
- Exécutez plusieurs fois et moyennez les résultats, car la mise en cache/le réseau peuvent fausser les exécutions uniques.

### Conseils et limitations

- **Exécutez depuis une machine séparée** : Ne testez pas contre localhost si possible, pour simuler un trafic réel.
- **Préchauffage** : Envoyez d'abord quelques requêtes pour amorcer les caches.
- **Montée en charge** : Pour des charges plus élevées, utilisez des outils comme `wrk`, `siege` ou Locust.
- **HTTPS** : ab ne le supporte pas nativement ; utilisez `ab -n 100 -c 10 http://example.com/` avec un proxy ou des alternatives.
- **Erreurs** : Si vous voyez "socket: Too many open files", augmentez la limite de descripteurs de fichiers de votre OS (par exemple, `ulimit -n 4096`).

Pour plus de détails, consultez la page de manuel (`man ab`) ou la documentation officielle.

[Documentation Apache Bench](https://httpd.apache.org/docs/2.4/programs/ab.html)