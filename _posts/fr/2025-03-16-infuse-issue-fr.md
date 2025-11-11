---
audio: false
generated: true
lang: fr
layout: post
title: Un Problème d’Infuse
translated: true
type: note
---

L'erreur « Failed to open input stream in demuxing stream » dans Infuse indique généralement que l'application ne peut pas accéder ou traiter correctement le fichier vidéo que vous essayez de lire en streaming. Étant donné que vous diffusez des fichiers `.mkv` depuis votre serveur Nginx (par exemple, `http://192.168.1.27/movies/yourfile.mkv`) et que cela fonctionne avec VLC mais pas avec Infuse, le problème peut provenir de problèmes de réseau, de la compatibilité du fichier ou de particularités spécifiques à Infuse. Voici comment résoudre le problème :

### 1. Vérifier la connectivité réseau
Infuse génère souvent cette erreur en raison d'interruptions ou de mauvaises configurations du réseau.
- **Tester l'accessibilité** : Depuis votre iPad (ou l'endroit où Infuse est exécuté), assurez-vous que l'URL fonctionne :
  - Ouvrez Safari et allez à `http://192.168.1.27/movies/`. Vous devriez voir la liste des fichiers.
  - Appuyez sur `yourfile.mkv` — il se peut qu'il ne se lance pas, mais confirmez que le lien est accessible.
- **Ping le serveur** : Sur votre iPad, utilisez une application comme **Network Ping Lite** (gratuite sur l'App Store) pour ping `192.168.1.27`. Si cela échoue, vérifiez votre Wi-Fi ou le pare-feu du serveur.
- **Vérification du pare-feu** : Sur votre serveur Ubuntu :
  ```bash
  sudo ufw status
  ```
  Assurez-vous que le port 80 est ouvert (`80/tcp ALLOW`). Sinon :
  ```bash
  sudo ufw allow 80
  sudo systemctl restart nginx
  ```

### 2. Redémarrer Infuse et l'appareil
Des problèmes temporaires peuvent causer cette erreur.
- **Fermer Infuse** : Appuyez deux fois sur le bouton Home (ou faites un swipe vers le haut sur les iPad plus récents) et faites glisser Infuse pour le fermer.
- **Rouvrir** : Lancez Infuse et réessayez le streaming.
- **Redémarrer l'iPad** : Maintenez le bouton d'alimentation enfoncé, faites glisser pour éteindre, puis redémarrez. Testez à nouveau.

### 3. Vérifier la compatibilité du fichier
Bien qu'Infuse prenne en charge `.mkv`, l'erreur peut être liée aux codecs ou à la structure du fichier.
- **Tester un autre fichier** : Téléchargez un petit fichier `.mkv` fonctionnel (par exemple, encodé avec une vidéo H.264 et un audio AAC) dans `/var/www/movies/` :
  ```bash
  sudo mv /path/to/testfile.mkv /var/www/movies/
  sudo chown www-data:www-data /var/www/movies/testfile.mkv
  sudo chmod 644 /var/www/movies/testfile.mkv
  ```
  Essayez de diffuser `http://192.168.1.27/movies/testfile.mkv` dans Infuse.
- **Vérification des codecs** : Puisque VLC le lit, le fichier est probablement diffusable, mais Infuse pourrait avoir des difficultés avec des codecs rares (par exemple, VP9, Opus). Utilisez VLC sur votre Mac pour inspecter :
  - Ouvrez le `.mkv`, appuyez sur `Cmd + I` (Outils > Informations sur les codecs) et notez les codecs vidéo/audio.
  - S'il ne s'agit pas de H.264/AAC, réencodez avec HandBrake (gratuit, handbrake.fr) :
    - Chargez le `.mkv`, sélectionnez la vidéo "H.264 (x264)" et l'audio "AAC", puis convertissez.

### 4. Ajuster la configuration Nginx
Infuse pourrait avoir besoin d'en-têtes ou de paramètres spécifiques pour un streaming fluide.
- **Mettre à jour la configuration** : Modifiez votre fichier Nginx (par exemple, `/etc/nginx/sites-enabled/default`) :
  ```nginx
  server {
      listen 80;
      server_name 192.168.1.27 localhost;

      location /movies/ {
          alias /var/www/movies/;
          autoindex on;
          add_header Accept-Ranges bytes;  # Assure le fonctionnement des requêtes de plage
          add_header Content-Disposition "inline";  # Aide au streaming
      }
  }
  ```
- **Recharger** :
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```
- **Pourquoi** : `Accept-Ranges` garantit qu'Infuse peut demander des parties du fichier (essentiel pour le streaming).

### 5. Soumettre un rapport de diagnostic
Les développeurs d'Infuse le suggèrent pour les problèmes persistants.
- **Étapes** :
  1. Dans Infuse, allez dans **Paramètres > Général**.
  2. Appuyez sur **Soumettre un rapport de diagnostic**.
  3. Notez le code qu'il vous donne.
  4. Visitez le [Forum Communautaire de Firecore](https://community.firecore.com/), postez le code et décrivez votre configuration (Nginx, `.mkv`, streaming HTTP).
- **Pourquoi** : Ils peuvent identifier s'il s'agit d'un bogue ou d'un problème de configuration.

### 6. Solution alternative
Si Infuse continue d'échouer :
- **Utiliser VLC** : Restez avec VLC for Mobile sur votre iPad (car il fonctionne de manière fiable).
- **Changer d'application** : Essayez **nPlayer** ou **PlayerXtreme** (App Store) avec la même URL.

### Cause probable
Puisque VLC le diffuse correctement, il s'agit probablement d'un hoquet réseau ou de la gestion plus stricte du flux HTTP par Infuse. L'ajustement Nginx (étape 4) et un fichier test (étape 3) résolvent souvent ce problème. Sinon, le rapport de diagnostic clarifiera la situation.

Faites-moi savoir ce que vous observez après avoir essayé ces solutions — en particulier toute erreur dans les logs ou le code de diagnostic !