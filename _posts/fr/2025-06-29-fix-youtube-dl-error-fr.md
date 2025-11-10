---
audio: false
generated: true
lang: fr
layout: post
title: Correction de l'Erreur de Vérification du Bot YouTube-dl
translated: true
type: note
---

L'erreur « Sign in to confirm you’re not a bot » de youtube-dl se produit généralement parce que YouTube bloque la requête, souvent en raison de restrictions d'adresse IP, de l'utilisation d'un VPN ou d'un manque d'authentification. Voici les étapes pour résoudre le problème, en commençant par les solutions les plus simples :

1. **Mettre à jour youtube-dl** :
   - L'erreur peut provenir d'une version obsolète de youtube-dl, car YouTube met fréquemment à jour ses systèmes. Mettez à jour vers la dernière version en exécutant :
     ```bash
     sudo youtube-dl -U
     ```
     ou, si vous l'avez installé via pip :
     ```bash
     pip install --upgrade youtube-dl
     ```
   - Après la mise à jour, réessayez la commande :
     ```bash
     youtube-dl https://www.youtube.com/watch?v=st3mUEub99E
     ```

2. **Passer à yt-dlp (Alternative Recommandée)** :
   - youtube-dl n'est plus activement maintenu, et yt-dlp, un fork de youtube-dl, est plus fiable face aux récents changements de YouTube. Installez yt-dlp :
     ```bash
     sudo pip install yt-dlp
     ```
     Puis utilisez :
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - yt-dlp gère mieux l'authentification et les restrictions d'adresse IP.

3. **Désactiver le VPN ou Changer de Serveur** :
   - Si vous utilisez un VPN, YouTube peut signaler votre adresse IP comme suspecte. Essayez de désactiver votre VPN ou de changer de serveur :
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Des utilisateurs ont signalé un succès après s'être déconnectés des VPNs ou après avoir changé de serveur.

4. **Utiliser des Cookies pour l'Authentification** :
   - YouTube peut exiger une authentification pour contourner la vérification de bot. Exportez les cookies depuis un navigateur où vous êtes connecté à YouTube :
     - Installez une extension de navigateur comme "Export Cookies" pour Firefox ou Chrome.
     - Connectez-vous à YouTube, exportez les cookies dans un fichier `cookies.txt`, et utilisez-le avec :
       ```bash
       youtube-dl --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
       ou pour yt-dlp :
       ```bash
       yt-dlp --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - Alternativement, utilisez `--cookies-from-browser firefox` (ou remplacez `firefox` par `chrome`, `edge`, etc.) pour extraire automatiquement les cookies :
       ```bash
       yt-dlp --cookies-from-browser firefox https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - Remarque : Évitez d'utiliser votre compte Google principal pour éviter un éventuel signalement. Utilisez un compte jetable si possible.

5. **Utiliser un Proxy** :
   - Si le problème persiste, votre adresse IP pourrait être bloquée (par exemple, si vous utilisez une IP de centre de données). Essayez un proxy résidentiel pour masquer votre adresse IP :
     ```bash
     youtube-dl --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
     ou pour yt-dlp :
     ```bash
     yt-dlp --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Les proxys résidentiels sont moins susceptibles d'être signalés que les proxys de centre de données.

6. **Effacer le Cache ou Essayer un Autre Réseau** :
   - Si vous avez récemment effacé les journaux ou les fichiers temporaires, assurez-vous que youtube-dl/yt-dlp ne dépend pas d'un cache corrompu. Effacez le cache :
     ```bash
     rm -rf ~/.cache/youtube-dl
     rm -rf ~/.cache/yt-dlp
     ```
   - Passez à un autre réseau (par exemple, un point d'accès mobile) pour tester si le problème est lié à l'adresse IP.

7. **Sortie Verbose pour le Débogage** :
   - Si les étapes ci-dessus échouent, exécutez la commande avec une sortie verbose pour un diagnostic plus approfondi :
     ```bash
     youtube-dl -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
     ou pour yt-dlp :
     ```bash
     yt-dlp -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - Partagez la sortie dans un forum pertinent (par exemple, les issues GitHub pour yt-dlp) pour une assistance communautaire.

**Notes** :
- La détection de bots par YouTube est devenue plus stricte, ciblant souvent les adresses IP de centres de données ou les requêtes non authentifiées.
- L'utilisation de cookies comporte un faible risque de signalement de compte, utilisez donc un compte secondaire.
- Si la vidéo est privée ou restreinte, assurez-vous que votre compte y a accès avant d'utiliser les cookies.
- Si rien de tout cela ne fonctionne, envisagez d'utiliser des interfaces alternatives comme Invidious ou NewPipe, bien qu'elles puissent avoir des limitations.

Essayez ces étapes dans l'ordre, en commençant par la mise à jour ou le passage à yt-dlp, car c'est le correctif le plus probable. Si le problème persiste, faites-moi part de la sortie verbose ou de tout détail spécifique (par exemple, utilisation d'un VPN, OS).