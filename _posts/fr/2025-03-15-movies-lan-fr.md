---
audio: false
generated: true
lang: fr
layout: post
title: Films en streaming sur réseau local
translated: true
type: note
---

Pour accéder aux films téléchargés sur votre ordinateur portable avec qBittorrent depuis votre iPad, les deux appareils étant sur le même réseau local (LAN), vous avez plusieurs options. Vous avez spécifiquement demandé à propos de l'utilisation d'un logiciel NAS ou de la configuration d'un serveur média Nginx, je vais donc aborder ces points et fournir une approche recommandée basée sur la facilité d'utilisation et les fonctionnalités.

---

### Option 1 : Utilisation d'un logiciel NAS (Recommandé : Plex Media Server)
NAS signifie Network Attached Storage, ce qui se réfère typiquement à un appareil qui stocke et partage des fichiers sur un réseau. Cependant, puisque vous utilisez votre ordinateur portable pour télécharger des films, vous pouvez installer un logiciel pour le transformer en un appareil similaire à un NAS. Un choix populaire et convivial est **Plex Media Server**, qui agit à la fois comme une solution de partage de fichiers et un serveur média avec des fonctionnalités supplémentaires comme organiser vos films et les diffuser de manière transparente.

#### Étapes pour configurer Plex :
1. **Installez Plex Media Server sur votre ordinateur portable :**
   - Téléchargez Plex Media Server depuis [plex.tv](https://www.plex.tv) et installez-le sur votre ordinateur portable (disponible pour Windows, macOS ou Linux).
   - Suivez l'assistant de configuration pour créer un compte (optionnel pour une utilisation locale) et configurer le serveur.

2. **Ajoutez votre dossier de films :**
   - Pendant la configuration, indiquez à Plex le dossier où qBittorrent enregistre vos films téléchargés. Cela ajoute les films à votre bibliothèque Plex, et Plex peut récupérer automatiquement les métadonnées (comme les affiches et les descriptions).

3. **Installez Plex sur votre iPad :**
   - Téléchargez l'application Plex gratuite depuis l'App Store sur votre iPad.

4. **Accédez à vos films :**
   - Assurez-vous que votre ordinateur portable et votre iPad sont sur le même réseau Wi-Fi.
   - Ouvrez l'application Plex sur votre iPad — elle devrait détecter automatiquement le serveur Plex fonctionnant sur votre ordinateur portable.
   - Parcourez votre bibliothèque de films et appuyez sur un film pour le lire. L'application Plex diffuse la vidéo directement depuis votre ordinateur portable.

#### Avantages :
- **Convivial :** Offre une interface soignée avec des illustrations et des détails sur les films.
- **Transcodage :** Si un format de film n'est pas pris en charge nativement par votre iPad, Plex peut le convertir à la volée (cela peut nécessiter des ressources suffisantes sur l'ordinateur portable).
- **Aucune expertise technique nécessaire :** La configuration est simple avec un processus guidé.

#### Considérations :
- La version gratuite de Plex est suffisante pour la diffusion en local dans votre LAN.
- Votre ordinateur portable doit rester allumé et connecté au réseau pendant que vous regardez des films.

---

### Option 2 : Partage de fichiers simple (sans logiciel supplémentaire)
Si vous préférez une solution légère sans installer de logiciel supplémentaire, vous pouvez partager le dossier de films directement depuis votre ordinateur portable en utilisant les fonctionnalités de partage de fichiers intégrées à votre système d'exploitation. Cela utilise le protocole SMB (Server Message Block), qui est pris en charge par l'application Fichiers de l'iPad.

#### Étapes pour configurer le partage de fichiers :
1. **Partagez le dossier sur votre ordinateur portable :**
   - **Windows :** Faites un clic droit sur le dossier où qBittorrent enregistre les films, sélectionnez "Propriétés", allez dans l'onglet "Partage" et cliquez sur "Partager". Choisissez de le partager avec "Tout le monde" ou des utilisateurs spécifiques et définissez les autorisations.
   - **macOS :** Ouvrez Préférences Système > Général > Partage, activez "Partage de fichiers" et ajoutez le dossier de films, en définissant les autorisations si nécessaire.
   - **Linux :** Installez et configurez Samba, puis partagez le dossier (nécessite une configuration en ligne de commande).

2. **Trouvez l'adresse IP de votre ordinateur portable :**
   - Sur votre ordinateur portable, ouvrez une invite de commande ou un terminal et tapez `ipconfig` (Windows) ou `ifconfig`/`ip addr` (Linux/macOS) pour trouver l'adresse IP (par exemple, 192.168.1.100).

3. **Connectez-vous depuis votre iPad :**
   - Ouvrez l'application **Fichiers** sur votre iPad.
   - Appuyez sur les trois points (...) dans le coin supérieur droit et sélectionnez "Se connecter au serveur".
   - Entrez `smb://<adresse-ip-ordinateur>` (par exemple, `smb://192.168.1.100`) et appuyez sur "Se connecter". Fournissez les identifiants si demandé (par exemple, le nom d'utilisateur et le mot de passe de votre ordinateur portable).
   - Naviguez jusqu'au dossier partagé.

4. **Lisez les films :**
   - Appuyez sur un fichier de film pour l'ouvrir dans le lecteur par défaut de l'application Fichiers, ou utilisez une application tierce comme **VLC for Mobile** (disponible sur l'App Store) pour une prise en charge plus large des formats.

#### Avantages :
- **Simple :** Aucun logiciel supplémentaire requis au-delà de ce qui est déjà sur votre ordinateur portable.
- **Configuration rapide :** Fonctionne avec votre système existant.

#### Considérations :
- La navigation dans les fichiers est moins intuitive qu'avec Plex — vous verrez une structure de dossiers basique.
- La lecture dépend du support du format du film par l'iPad (par exemple, MP4 avec H.264 fonctionne bien nativement ; VLC peut gérer plus de formats).
- Votre ordinateur portable doit être allumé et connecté au LAN.

---

### Option 3 : Configuration d'un serveur média Nginx
Nginx est un serveur web léger qui peut servir des fichiers via HTTP. Vous pouvez le configurer sur votre ordinateur portable pour rendre votre dossier de films accessible via un navigateur web ou un lecteur média sur votre iPad.

#### Étapes pour configurer Nginx :
1. **Installez Nginx sur votre ordinateur portable :**
   - Téléchargez et installez Nginx (disponible pour Windows, macOS ou Linux) depuis [nginx.org](https://nginx.org) ou via un gestionnaire de paquets (par exemple, `sudo apt install nginx` sur Ubuntu).

2. **Configurez Nginx :**
   - Modifiez le fichier de configuration de Nginx (par exemple, `/etc/nginx/nginx.conf` sur Linux ou un emplacement similaire) :
     ```
     server {
         listen 80;
         server_name localhost;
         location /movies {
             root /chemin/vers/votre/dossier/films;
             autoindex on; # Active le listage des répertoires
         }
     }
     ```
   - Remplacez `/chemin/vers/votre/dossier/films` par le chemin réel où qBittorrent enregistre les films.

3. **Démarrez Nginx :**
   - Exécutez `nginx` (Windows) ou `sudo systemctl start nginx` (Linux) pour lancer le serveur.

4. **Accédez depuis votre iPad :**
   - Ouvrez Safari ou un autre navigateur sur votre iPad.
   - Entrez `http://<adresse-ip-ordinateur>/movies` (par exemple, `http://192.168.1.100/movies`).
   - Vous verrez une liste de fichiers de films. Appuyez sur un pour le lire dans le navigateur, ou copiez le lien et ouvrez-le dans un lecteur média comme VLC.

#### Avantages :
- **Léger :** Utilise moins de ressources que Plex.
- **Personnalisable :** Vous pouvez ajuster les paramètres Nginx selon vos besoins.

#### Considérations :
- **Configuration technique :** Nécessite de modifier des fichiers de configuration et quelques connaissances en serveur.
- **Expérience basique :** Aucune interface élaborée — juste une liste de fichiers dans le navigateur.
- **Lecture :** Dépend du support du format du film par le navigateur ou l'application ; aucun transcodage n'est disponible.

---

### Recommandation
Compte tenu de vos options, je recommande **d'utiliser Plex Media Server** comme solution de "logiciel NAS". Voici pourquoi :
- **Facilité d'utilisation :** Plex est plus simple à configurer que Nginx et offre une bien meilleure expérience que le simple partage de fichiers.
- **Fonctionnalités :** Il organise vos films, prend en charge le transcodage si nécessaire et offre une application dédiée pour l'iPad pour une diffusion transparente.
- **Concentré sur le LAN :** Fonctionne parfaitement au sein de votre réseau local, comme vous l'avez spécifié.

Si vous voulez éviter d'installer un logiciel, la méthode de **partage de fichiers** est une alternative solide — partagez simplement le dossier et utilisez l'application Fichiers avec VLC sur votre iPad. Cependant, **Nginx** est excessif pour ce cas d'usage sauf si vous êtes à l'aise avec la configuration de serveur et préférez une configuration minimale.

#### Réponse finale
Pour la meilleure expérience, installez Plex Media Server sur votre ordinateur portable, ajoutez votre dossier de téléchargement qBittorrent, et utilisez l'application Plex sur votre iPad pour regarder vos films sur votre LAN. Alternativement, pour une approche plus simple, partagez le dossier via SMB et accédez-y avec l'application Fichiers et VLC sur votre iPad.