---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Correctif d'Authentification Localhost Safari
translated: true
type: note
---

Ce problème survient parce que Safari sur macOS applique des politiques de sécurité plus strictes que Chrome pour les URLs localhost. Spécifiquement, Safari nécessite un contexte HTTPS sécurisé pour autoriser les cookies persistants et les sessions d'authentification, empêchant ainsi les boucles de déconnexion potentielles ou les ré-authentifications à chaque visite pour des applications comme LibreChat fonctionnant en HTTP. Chrome est plus permissif avec HTTP sur localhost, ce qui explique pourquoi l'authentification persiste dans Chrome mais pas dans Safari.[1][2][3]

### Facteurs Gouvernants
- **Politiques des Navigateurs** : Les navigateurs modernes comme Safari exigent HTTPS pour localhost afin d'éviter les avertissements de contenu mixte et les insécurités de session.
- **Comportement de LibreChat** : LibreChat utilise des cookies sécurisés ou des jetons basés sur le localStorage pour l'authentification, qui se rompent en HTTP dans Safari en raison de sa gestion plus stricte des origines non sécurisées.

### Solutions (Classées par Facilité et Efficacité)
1. **Configurer HTTPS pour Localhost (Recommandé)** :
   - La documentation et le blog de LibreChat recommandent cette approche pour prévenir les déconnexions induites par HTTP.[1]
   - Utilisez `mkcert` (un outil gratuit) pour générer et approuver des certificats SSL locaux pour localhost :
     - Installez `mkcert` via `brew install mkcert` ou téléchargez-le depuis GitHub.
     - Exécutez `mkcert -install` pour installer l'autorité de certification racine.
     - Créez les certificats : `mkcert localhost 127.0.0.1`.
     - Configurez LibreChat (par exemple, via les variables d'environnement Docker ou la configuration) pour utiliser ces certificats : Ajoutez `HTTPS=true`, `SSL_CRT_FILE=/chemin/vers/localhost.pem`, et `SSL_KEY_FILE=/chemin/vers/localhost-key.pem` dans votre fichier `.env` ou l'environnement.
     - Redémarrez LibreChat et accédez-y via `https://localhost:3080`.
     - Safari le traitera maintenant comme sécurisé, permettant des connexions transparentes.

2. **Alternative : Utiliser 127.0.0.1 au lieu de localhost** :
   - Safari se comporte parfois différemment avec `localhost` (en raison de la résolution IPv6 ou DNS). Essayez d'accéder à `http://127.0.0.1:3080` – cela a résolu des problèmes de connexion similaires dans certains cas, bien que cela ne corrige pas nécessairement entièrement la persistance de l'authentification.[4][4][5]

3. **Effacer les Données du Site Web Safari pour localhost** :
   - Allez dans Safari > Préférences > Confidentialité > Gérer les données des sites Web > Recherchez "localhost" > Supprimez toute entrée.
   - Cela force Safari à cesser d'appliquer les mises à niveau HTTPS ou les contextes non sécurisés en cache.[3][2]
   - Redémarrez Safari et testez ; si LibreChat le prend en charge, l'authentification devrait être maintenue.

Si aucune de ces solutions ne fonctionne, vérifiez les journaux de LibreChat pour les erreurs d'authentification, assurez-vous que votre `.env` n'a pas de drapeaux conflictuels (par exemple, `ALLOW_ANONYMOUS=true` désactive entièrement l'authentification si souhaité), et confirmez que vous n'êtes pas en mode de navigation privée de Safari, qui bloque le stockage persistant.[6][7] Si le problème persiste, fournissez votre version de LibreChat et la configuration de votre fichier .env pour un dépannage plus approfondi.

Citations :
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354