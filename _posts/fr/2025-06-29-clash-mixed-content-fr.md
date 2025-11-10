---
audio: false
generated: true
lang: fr
layout: post
title: Corriger les erreurs de contenu mixte de Clash VPN
translated: true
type: note
---

Les messages d'erreur que vous rencontrez indiquent un problème de **contenu mixte** avec l'application VPN Clash, spécifiquement lorsque la page à l'adresse `https://clash.razord.top/` tente de charger des ressources depuis un point de terminaison non sécurisé `http://127.0.0.1:9090/` (par exemple, `http://127.0.0.1:9090/version`). Les navigateurs modernes bloquent ces requêtes car elles violent les politiques de sécurité en tentant de charger du contenu HTTP non sécurisé sur une page HTTPS sécurisée. De plus, il y a des erreurs CORS (Cross-Origin Resource Sharing) dues à des restrictions de contrôle d'accès. Voici un guide étape par étape pour résoudre ce problème.

---

### Pourquoi cela se produit
- **Erreur de Contenu Mixte** : La page web est servie via HTTPS, mais elle tente de récupérer des ressources (comme la vérification de version) depuis `http://127.0.0.1:9090`, qui est non sécurisé. Les navigateurs bloquent ces requêtes pour empêcher des vulnérabilités de sécurité potentielles, telles que les attaques de type "man-in-the-middle".
- **Erreur CORS** : Le navigateur bloque la requête vers `http://127.0.0.1:9090` en raison de la politique CORS, qui restreint les requêtes cross-origin à moins d'être explicitement autorisées par le serveur.
- **Contexte de Clash** : Clash (ou Clash for Windows) est une application proxy qui utilise probablement un serveur local (`127.0.0.1:9090`) pour son tableau de bord ou son API. Si ce serveur local ne prend pas en charge HTTPS ou n'est pas configuré correctement, il déclenche ces erreurs lorsqu'il est accessible via une page web HTTPS.

---

### Étapes pour résoudre le problème

#### 1. **Vérifier la configuration du Clash Core**
   - **Vérifier si le Clash Core est en cours d'exécution** : Assurez-vous que le service Clash core (le service backend) est en cours d'exécution sur votre machine et écoute sur `127.0.0.1:9090`. Vous pouvez le vérifier en :
     - Ouvrant un terminal ou une invite de commande.
     - Exécutant `curl http://127.0.0.1:9090/version` pour vérifier si le point de terminaison répond avec la version de Clash.
     - S'il ne répond pas, assurez-vous que le service Clash est actif. Redémarrez Clash for Windows ou le processus Clash core.
   - **Activer HTTPS pour le Clash Core** (si possible) :
     - Certaines versions de Clash (par exemple, Clash Premium ou Clash Meta) prennent en charge HTTPS pour l'API locale. Consultez la documentation de Clash ou le fichier de configuration (généralement `config.yaml`) pour une option permettant d'activer HTTPS pour le contrôleur externe (le point de terminaison de l'API).
     - Recherchez un paramètre comme `external-controller` ou `external-ui` dans le fichier de configuration. Par exemple :
       ```yaml
       external-controller: 127.0.0.1:9090
       external-ui: <chemin-vers-l-ui>
       ```
       Si HTTPS est pris en charge, vous devrez peut-être configurer un certificat pour le serveur local. Ceci est avancé et peut nécessiter la génération d'un certificat auto-signé (voir l'étape 4 ci-dessous).

#### 2. **Accéder au tableau de bord via HTTP (Solution temporaire)**
   - Si le tableau de bord Clash est accessible via HTTP (par exemple, `http://clash.razord.top/` au lieu de HTTPS), essayez de le charger sans HTTPS pour éviter les problèmes de contenu mixte :
     - Ouvrez votre navigateur et naviguez vers `http://clash.razord.top/`.
     - Remarque : Ceci n'est pas recommandé pour une utilisation en production, car HTTP n'est pas sécurisé. Utilisez ceci uniquement pour des tests ou si le tableau de bord n'est accessible que localement.
   - Si le tableau de bord nécessite HTTPS, passez aux étapes suivantes pour traiter la cause racine.

#### 3. **Mettre à jour les URL vers HTTPS**
   - L'erreur suggère que le tableau de bord Clash tente de récupérer des ressources depuis `http://127.0.0.1:9090`. Si vous avez accès au code source ou à la configuration du tableau de bord Clash :
     - Vérifiez le code frontend (par exemple, `index-5e90ca00.js` ou `vendor-827b5617.js`) pour les références codées en dur `http://127.0.0.1:9090`.
     - Mettez-les à jour vers `https://127.0.0.1:9090` si le Clash core prend en charge HTTPS, ou utilisez une URL relative (par exemple, `/version`) pour laisser le navigateur utiliser le même protocole que la page.
     - Si vous n'avez pas accès au code source, vous devrez peut-être configurer un proxy inverse (voir l'étape 4).

#### 4. **Configurer un proxy inverse avec HTTPS**
   - Pour résoudre le problème de contenu mixte, vous pouvez configurer un proxy inverse (par exemple, en utilisant Nginx ou Caddy) pour servir l'API Clash core (`http://127.0.0.1:9090`) via HTTPS. Cela permet au tableau de bord de communiquer avec le core de manière sécurisée.
   - **Étapes pour Nginx** :
     1. Installez Nginx sur votre système (s'il n'est pas déjà installé).
     2. Générez un certificat SSL auto-signé pour `127.0.0.1` :
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -subj "/CN=localhost"
        ```
     3. Configurez Nginx pour proxyfier les requêtes vers `http://127.0.0.1:9090` via HTTPS. Créez un fichier de configuration (par exemple, `/etc/nginx/sites-available/clash`) :
        ```nginx
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /chemin/vers/localhost.crt;
            ssl_certificate_key /chemin/vers/localhost.key;

            location / {
                proxy_pass http://127.0.0.1:9090;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
     4. Activez la configuration et redémarrez Nginx :
        ```bash
        sudo ln -s /etc/nginx/sites-available/clash /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl restart nginx
        ```
     5. Mettez à jour le tableau de bord Clash pour utiliser `https://localhost:443` au lieu de `http://127.0.0.1:9090` pour les requêtes API.
     6. Dans votre navigateur, acceptez le certificat auto-signé lorsque vous y êtes invité.

   - **Alternative avec Caddy** : Caddy est plus simple à configurer et gère automatiquement HTTPS :
     1. Installez Caddy.
     2. Créez un `Caddyfile` :
        ```caddy
        localhost:443 {
            reverse_proxy http://127.0.0.1:9090
        }
        ```
     3. Exécutez Caddy : `caddy run`.
     4. Mettez à jour le tableau de bord Clash pour utiliser `https://localhost:443`.

#### 5. **Contourner les restrictions CORS (Avancé)**
   - L'erreur CORS (`XMLHttpRequest cannot load http://127.0.0.1:9090/version due to access control checks`) indique que le serveur Clash core n'envoie pas les en-têtes CORS appropriés. Si vous contrôlez le Clash core :
     - Modifiez la configuration du Clash core pour inclure les en-têtes CORS, tels que :
       ```yaml
       external-controller: 127.0.0.1:9090
       allow-cors: true
       ```
       (Vérifiez la documentation de Clash pour la syntaxe exacte, car cela dépend de la version de Clash.)
     - Alternativement, la configuration du proxy inverse de l'étape 4 peut gérer CORS en ajoutant des en-têtes comme :
       ```nginx
       add_header Access-Control-Allow-Origin "https://clash.razord.top";
       add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
       add_header Access-Control-Allow-Headers "*";
       ```
   - Si vous ne contrôlez pas le core, vous pouvez utiliser une extension de navigateur pour contourner temporairement CORS (par exemple, "CORS Unblock" pour Chrome), mais ce n'est pas recommandé pour des raisons de sécurité.

#### 6. **Mettre à jour Clash ou passer à une version compatible**
   - Assurez-vous d'utiliser la dernière version de Clash for Windows ou Clash Verge, car les versions plus anciennes peuvent avoir des bogues ou manquer de prise en charge HTTPS pour le contrôleur externe.
   - Vérifiez le dépôt GitHub de Clash (`github.com/Dreamacro/clash` ou `github.com/Fndroid/clash_for_windows_pkg`) pour les mises à jour ou les problèmes signalés liés au contenu mixte ou à CORS.
   - Envisagez de passer à **Clash Verge** ou **Clash Meta**, qui peuvent avoir une meilleure prise en charge de HTTPS et des politiques de sécurité des navigateurs modernes.[](https://clashverge.net/en/tutorial-en/)

#### 7. **Autoriser le contenu non sécurisé dans le navigateur (Non recommandé)**
   - En dernier recours, vous pouvez autoriser le contenu non sécurisé dans votre navigateur pour `https://clash.razord.top/` :
     - **Chrome** :
       1. Cliquez sur l'icône de cadenas dans la barre d'adresse.
       2. Allez dans "Paramètres du site" > "Contenu non sécurisé" > Définissez sur "Autoriser".
     - **Firefox** :
       1. Cliquez sur l'icône de cadenas et allez dans "Paramètres de connexion".
       2. Désactivez "Bloquer le contenu dangereux et trompeur" temporairement.
     - **Avertissement** : Cela contourne les protections de sécurité et ne doit être utilisé que pour des tests locaux sur des réseaux de confiance.
   - Alternativement, lancez Chrome avec le drapeau `--disable-web-security` (uniquement pour le développement) :
     ```bash
     google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```

#### 8. **Vérifier les extensions conflictuelles ou le pare-feu**
   - Les extensions de navigateur (par exemple, les bloqueurs de publicités, les outils de confidentialité) ou les paramètres du pare-feu peuvent interférer avec le serveur local de Clash. Désactivez temporairement les extensions ou vérifiez votre pare-feu pour vous assurer que `127.0.0.1:9090` est accessible.[](https://vpncentral.com/reddit-blocked-by-network-security/)
   - Sur Windows, assurez-vous que l'application Clash a les permissions de pare-feu :
     - Allez dans Paramètres > Réseau et Internet > Pare-feu Windows > Autoriser une application via le pare-feu.
     - Ajoutez ou activez Clash for Windows.

#### 9. **Contacter le support ou la communauté Clash**
   - Si les étapes ci-dessus ne résolvent pas le problème, signalez-le sur la page des problèmes GitHub de Clash for Windows (`github.com/Fndroid/clash_for_windows_pkg/issues`) ou sur les forums de la communauté Clash. Fournissez des détails sur votre configuration, y compris :
     - La version de Clash.
     - Le système d'exploitation.
     - Le fichier de configuration (masquez les informations sensibles).
     - Le navigateur et sa version.
   - Vérifiez les problèmes similaires dans la communauté, car cette erreur peut être spécifique à certaines versions ou configurations de Clash.[](https://superuser.com/questions/1769163/could-not-switch-to-this-profile-proxy-0-filed-ws-opts-headershost-invalid-c)

---

### Approche recommandée
La solution la plus sécurisée et robuste est de **configurer un proxy inverse avec HTTPS** (étape 4) pour garantir que toutes les requêtes sont servies via HTTPS, résolvant à la fois les problèmes de contenu mixte et CORS. Si vous ne pouvez pas modifier le Clash core ou le tableau de bord, utiliser une version plus récente de Clash (par exemple, Clash Verge) ou accéder temporairement au tableau de bord via HTTP (étape 2) peuvent être des solutions de contournement plus rapides.

---

### Notes supplémentaires
- Si vous utilisez un tableau de bord Clash personnalisé ou un service tiers comme `clash.razord.top`, vérifiez qu'il est compatible avec votre version de Clash core.
- Sauvegardez toujours votre configuration Clash (`config.yaml`) avant d'apporter des modifications.
- Si le problème persiste, vous pouvez essayer de passer à d'autres clients proxy alternatifs comme v2rayN ou OpenVPN, qui peuvent avoir une meilleure prise en charge HTTPS pour les API locales.[](https://stackoverflow.com/questions/67822697/how-to-route-internet-traffic-via-clash-for-windows-ping-from-python-code-is)

N'hésitez pas à demander de l'aide pour des étapes spécifiques, comme la configuration de Nginx ou le débogage de la configuration Clash !