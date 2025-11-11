---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Nginx
translated: true
type: note
---

Utiliser `server_name 0.0.0.0` dans votre configuration Nginx n'est pas la bonne approche, car `server_name` est destiné à correspondre à des noms de domaine ou des noms d'hôte, pas à des adresses IP. De plus, `0.0.0.0` est une adresse spéciale qui signifie "écouter sur toutes les interfaces", ce qui est géré par la directive `listen`, pas par `server_name`. Étant donné que l'adresse IP de votre ordinateur portable (le serveur) change dynamiquement, vous avez besoin d'une solution qui s'adapte à cela. Voici les étapes pour corriger votre configuration Nginx et gérer efficacement le problème d'IP dynamique.

### Problème
L'adresse IP de votre ordinateur portable (par exemple, `192.168.1.27`) change à cause du DHCP, mais vous voulez que votre serveur Nginx serve de manière fiable les fichiers vidéo, quel que soit l'adresse IP. Coder en dur l'IP dans la directive `server_name` ou la configuration du client pose problème lorsque l'IP change.

### Solution
Pour que votre serveur Nginx fonctionne de manière transparente malgré l'IP changeante, vous pouvez utiliser une ou plusieurs des approches suivantes :

#### 1. Utiliser un DNS Dynamique (DDNS) ou un Nom d'Hôte Local
Au lieu de dépendre de l'adresse IP, utilisez un nom d'hôte pour votre serveur. Cela peut être réalisé en :
- **Utilisant le nom d'hôte de l'ordinateur portable** : La plupart des systèmes d'exploitation attribuent un nom d'hôte par défaut (par exemple, `mylaptop.local` sur macOS ou `mylaptop` sur Linux/Windows). Vous pouvez l'utiliser dans votre `server_name` Nginx et accéder au serveur via le nom d'hôte.
- **Configurant un DNS local ou mDNS** : Utilisez un service comme Avahi (pour Linux) ou Bonjour (pour macOS/Windows) pour résoudre le nom d'hôte de l'ordinateur portable localement (par exemple, `mylaptop.local`).
- **Utilisant un service DDNS** : Si vous avez besoin d'un accès depuis l'extérieur de votre réseau local, des services comme No-IP ou DynDNS peuvent assigner un nom de domaine (par exemple, `mymovies.ddns.net`) qui suit l'IP de votre ordinateur portable, même si elle change.

**Exemple de Configuration Nginx** :
```nginx
server {
    listen 80;
    server_name mylaptop.local; # Utilisez le nom d'hôte de l'ordinateur portable ou le nom DDNS
    root /chemin/vers/videos;
    location / {
        try_files $uri $uri/ /index.html; # Ajustez selon votre configuration
    }
}
```
- Remplacez `mylaptop.local` par le nom d'hôte réel de votre ordinateur portable ou le nom DDNS.
- Sur les clients, accédez au serveur via `http://mylaptop.local` au lieu de l'adresse IP.

**Comment Trouver le Nom d'Hôte de Votre Ordinateur Portable** :
- Linux/macOS : Exécutez `hostname` dans un terminal.
- Windows : Exécutez `hostname` dans l'invite de commandes ou vérifiez dans Paramètres > Système > À propos.
- Assurez-vous que votre réseau prend en charge mDNS (la plupart des routeurs domestiques le font via Bonjour/Avahi).

#### 2. Lier Nginx à Toutes les Interfaces
Si vous voulez que Nginx écoute sur toutes les adresses IP disponibles (utile lorsque l'IP change), configurez la directive `listen` pour utiliser `0.0.0.0` ou omettez l'adresse entièrement (Nginx utilise par défaut toutes les interfaces).

**Exemple de Configuration Nginx** :
```nginx
server {
    listen 80; # Écoute sur toutes les interfaces (équivalent à 0.0.0.0:80)
    server_name _; # Correspond à tout nom d'hôte ou IP
    root /chemin/vers/videos;
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
- `listen 80` : Se lie à toutes les interfaces, donc le serveur répond aux requêtes sur n'importe quelle IP assignée à l'ordinateur portable.
- `server_name _` : Une valeur générique qui correspond à tout nom d'hôte ou IP utilisé pour accéder au serveur.
- Les clients peuvent accéder au serveur en utilisant n'importe quelle IP actuelle de l'ordinateur portable (par exemple, `http://192.168.1.27` ou `http://192.168.1.28`) ou le nom d'hôte.

#### 3. Assigner une IP Statique à l'Ordinateur Portable
Pour éviter que l'adresse IP ne change, configurez votre ordinateur portable pour utiliser une adresse IP statique dans votre réseau local (par exemple, `192.168.1.27`). Cela peut être fait via :
- **Les paramètres du routeur** : Réservez une IP pour l'adresse MAC de votre ordinateur portable dans les paramètres DHCP de votre routeur (souvent appelé "réservation DHCP").
- **Les paramètres réseau de l'ordinateur portable** : Définissez manuellement une IP statique en dehors de la plage DHCP (par exemple, `192.168.1.200`) dans la configuration réseau de votre ordinateur portable.

Une fois l'IP statique définie, mettez à jour votre configuration Nginx :
```nginx
server {
    listen 192.168.1.27:80; # Lier à l'IP statique
    server_name 192.168.1.27; # Optionnel, si les clients utilisent l'IP directement
    root /chemin/vers/videos;
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
- Les clients accèdent au serveur via `http://192.168.1.27`.

#### 4. Utiliser un Reverse Proxy ou un Load Balancer (Avancé)
Si vous avez plusieurs serveurs ou voulez une configuration plus robuste, vous pouvez configurer un reverse proxy (par exemple, une autre instance Nginx) sur un appareil avec une IP statique qui redirige les requêtes vers votre ordinateur portable. Le proxy peut utiliser le nom d'hôte de l'ordinateur portable ou résoudre dynamiquement son IP.

### Approche Recommandée
Pour la simplicité, je recommande **l'Option 1 (Utiliser le nom d'hôte de l'ordinateur portable)** ou **l'Option 2 (Lier à toutes les interfaces)** :
- **L'Option 1** est idéale si votre réseau prend en charge mDNS et que vous voulez une URL conviviale (par exemple, `http://mylaptop.local`). Elle nécessite une configuration minimale et fonctionne bien pour les réseaux locaux.
- **L'Option 2** est la meilleure si vous ne voulez pas dépendre des noms d'hôte et que vous êtes d'accord pour que les clients utilisent l'IP actuelle (que vous pouvez trouver via `ip addr` ou `ifconfig` sur l'ordinateur portable).

### Étapes de Mise en Œuvre
1. **Éditez la Configuration Nginx** :
   - Ouvrez votre fichier de configuration Nginx (par exemple, `/etc/nginx/sites-available/default` ou `/etc/nginx/conf.d/movies.conf`).
   - Appliquez l'une des configurations ci-dessus (par exemple, utilisez `server_name mylaptop.local` ou `server_name _` avec `listen 80`).
   - Sauvegardez le fichier.

2. **Testez la Configuration** :
   ```bash
   sudo nginx -t
   ```
   Assurez-vous qu'il n'y a pas d'erreurs de syntaxe.

3. **Rechargez Nginx** :
   ```bash
   sudo systemctl reload nginx
   ```
   Ou, si `systemctl` n'est pas disponible :
   ```bash
   sudo nginx -s reload
   ```

4. **Testez l'Accès** :
   - Depuis un appareil client, accédez au serveur en utilisant le nom d'hôte (par exemple, `http://mylaptop.local`) ou l'IP actuelle de l'ordinateur portable (par exemple, `http://192.168.1.27`).
   - Vérifiez que les fichiers vidéo sont servis correctement.

5. **Optionnel : Vérifiez l'IP de l'Ordinateur Portable** :
   Si vous avez besoin de trouver l'IP actuelle de l'ordinateur portable :
   - Linux/macOS : `ip addr show` ou `ifconfig`.
   - Windows : `ipconfig` dans l'invite de commandes.

### Conseils Supplémentaires
- **Pare-feu** : Assurez-vous que le pare-feu de l'ordinateur portable autorise le trafic HTTP sur le port 80 (ou 443 pour HTTPS). Par exemple, sur Linux avec `ufw` :
  ```bash
  sudo ufw allow 80/tcp
  ```
- **Permissions des Fichiers** : Vérifiez que Nginx a la permission de lire les fichiers vidéo :
  ```bash
  sudo chown -R www-data:www-data /chemin/vers/videos
  sudo chmod -R 755 /chemin/vers/videos
  ```
  (Ajustez `www-data` à l'utilisateur sous lequel Nginx s'exécute, par exemple, `nginx` sur certains systèmes.)
- **HTTPS (Optionnel)** : Pour la sécurité, envisagez de configurer HTTPS avec un certificat auto-signé ou Let’s Encrypt, surtout si vous accédez au serveur depuis l'extérieur de votre réseau local.
- **Débogage** : Si le serveur n'est pas accessible, vérifiez les journaux Nginx :
  ```bash
  sudo tail -f /var/log/nginx/error.log
  sudo tail -f /var/log/nginx/access.log
  ```

### Pourquoi `server_name 0.0.0.0` Ne Fonctionne Pas
- `server_name` est utilisé pour correspondre à l'en-tête `Host` dans les requêtes HTTP, pas pour spécifier l'interface d'écoute. Définir `server_name 0.0.0.0` s'attendrait à ce que les clients envoient un en-tête `Host: 0.0.0.0`, ce qu'ils ne feront pas.
- Pour écouter sur toutes les interfaces, utilisez `listen 0.0.0.0:80` (ou simplement `listen 80`), et pour correspondre à tout nom d'hôte, utilisez `server_name _`.

### Exemple de Configuration Finale (La Plus Simple)
Pour un serveur vidéo local qui fonctionne quel que soit le changement d'IP :
```nginx
server {
    listen 80;
    server_name _;
    root /chemin/vers/videos;
    location / {
        autoindex on; # Active le listing des répertoires pour une navigation facile
        try_files $uri $uri/ /index.html;
    }
}
```
- Sauvegardez, testez et rechargez Nginx comme décrit ci-dessus.
- Accédez via `http://<ip-ordinateur-portable>` ou `http://<nom-hôte-ordinateur-portable>`.

Cette configuration garantit que votre serveur vidéo reste accessible même lorsque l'IP de l'ordinateur portable change, sans dépendre d'une IP spécifique dans la configuration.

Si vous avez plus de détails (par exemple, votre configuration Nginx actuelle, OS, ou configuration réseau), je peux adapter la solution davantage. Faites-moi savoir !