---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vérification de la configuration et de l'utilisation du proxy APT
translated: true
type: note
---

### Vérifier si APT utilise un proxy

Pour confirmer si APT (le gestionnaire de paquets sur les systèmes basés sur Debian/Ubuntu) est configuré pour utiliser un proxy—et s'il est effectivement appliqué pendant les opérations—vous pouvez suivre ces étapes. Cela implique d'inspecter les fichiers de configuration et de tester la connectivité. Notez qu'APT ne journalise pas explicitement l'utilisation du proxy de manière simple, donc la "confirmation" signifie généralement vérifier les paramètres et observer le comportement lors d'un test.

#### 1. **Inspecter la configuration du proxy d'APT**
   Les paramètres de proxy d'APT sont stockés dans `/etc/apt/apt.conf` ou dans les fichiers de `/etc/apt/apt.conf.d/` (par exemple, `99proxy` ou similaire). Cherchez les lignes définissant `Acquire::http::Proxy` ou `Acquire::https::Proxy`.

   - **Commande pour vérifier toute configuration liée au proxy** :
     ```
     apt-config dump | grep -i proxy
     ```
     - **Ce que cela fait** : Affiche la configuration effective d'APT et filtre les entrées de proxy. Si vous voyez une sortie comme `Acquire::http::Proxy "http://proxy.example.com:8080/"`, c'est qu'il est configuré.
     - **Exemple de sortie si un proxy est défini** :
       ```
       Acquire::http::Proxy "http://username:password@proxy.example.com:8080";
       Acquire::https::Proxy "http://proxy.example.com:8080";
       ```

   - **Vérification manuelle des fichiers** :
     ```
     grep -r "Proxy" /etc/apt/apt.conf* /etc/apt/apt.conf.d/
     ```
     - **Ce que cela fait** : Recherche les mots-clés "Proxy" dans tous les fichiers de configuration d'APT.

   Si aucune ligne de proxy n'apparaît, APT n'en **utilise** pas (il se connecte directement).

#### 2. **Tester si le proxy est réellement utilisé**
   La configuration seule ne confirme pas l'utilisation—testez en simulant une opération APT qui récupère des données depuis les dépôts (ce qui passerait par le proxy s'il est configuré).

   - **Test basique : Exécuter une mise à jour** :
     ```
     sudo apt update
     ```
     - **Ce que cela fait** : Récupère les listes de paquets depuis les dépôts. Observez la sortie :
       - Un succès (par exemple, "Hit:1 http://archive.ubuntu.com ...") indique une connectivité, probablement via le proxy si configuré.
       - Des erreurs comme "Failed to fetch" ou un timeout suggèrent des problèmes de proxy (par exemple, mauvais identifiants ou proxy injoignable).
     - Pour plus de détails, ajoutez de la verbosité : `sudo apt update -o Debug::Acquire::http=true`.

   - **Test de téléchargement uniquement (aucun changement sur le système)** :
     ```
     sudo apt clean
     sudo apt -d --reinstall install hostname
     ```
     - **Ce que cela fait** : Vide le cache, puis simule la réinstallation du petit paquet intégré `hostname` sans l'installer réellement (le drapeau `-d` télécharge seulement). Vérifiez la sortie pour des récupérations réussies. Si cela fonctionne, le proxy a été utilisé (en supposant qu'il est configuré).

   - **Avancé : Tracer les appaux réseau (nécessite `strace`)** :
     Si vous voulez confirmer les connexions proxy pendant une exécution :
     ```
     sudo strace -e trace=connect sudo apt update 2>&1 | grep -i proxy
     ```
     - **Ce que cela fait** : Trace les appaux système pour les connexions réseau. Cherchez les connexions vers l'IP/port de votre proxy au lieu des serveurs de dépôt directs (par exemple, `archive.ubuntu.com`).

#### Problèmes courants et correctifs
- **Si le proxy nécessite une authentification** : Assurez-vous que la configuration utilise `http://username:password@proxyhost:port`.
- **Variables d'environnement** : APT ignore les proxies du shell (`$http_proxy`), donc comptez sur la configuration spécifique à APT.
- **Concernant votre commande `sudo apt --fix-broken install`** : Cela corrige les dépendances cassées en réinstallant les paquets. Si elle échoue (par exemple, erreurs réseau), exécutez-la après avoir confirmé le proxy avec les tests ci-dessus. Les problèmes de proxy se manifestent souvent par des échecs de récupération—corrigez d'abord la configuration, puis réessayez.

Si cela ne résout pas le problème, partagez la sortie d'erreur pour plus d'aide.

**Références** :
- [How to check if apt proxy configuration is correct? (Unix Stack Exchange)](https://unix.stackexchange.com/questions/49781/how-to-check-if-apt-proxy-configuration-is-correct)
- [How to Use APT with Proxy on Ubuntu and Debian (Linuxiac)](https://linuxiac.com/how-to-use-apt-with-proxy/)