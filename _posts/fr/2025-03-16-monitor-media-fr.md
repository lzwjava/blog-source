---
audio: false
generated: true
lang: fr
layout: post
title: Surveiller la lecture multimédia sur Ubuntu via VLC
translated: true
type: note
---

Pour regarder des films sur votre moniteur en utilisant votre deuxième ordinateur portable (sous Ubuntu avec un serveur Nginx) sans trop de tracas, voici la meilleure approche basée sur ce que vous avez déjà. Vous souhaitez éviter d'acheter des appareils supplémentaires comme une Fire TV Stick ou un Apple TV, et bien qu'un câble HDMI long fonctionne, vous préféreriez ne pas avoir à interagir constamment avec l'ordinateur portable pour sélectionner et lire les vidéos. Mettons en place une solution simple et pratique en utilisant votre configuration existante.

Étant donné que vos films sont stockés sur votre ordinateur portable Ubuntu et qu'il exécute déjà un serveur Nginx, le moyen le plus simple est de connecter cet ordinateur portable directement à votre moniteur via HDMI et de rendre le contrôle de la lecture sans effort. Voici comment procéder :

### Solution : Connecter l'ordinateur portable au moniteur et utiliser VLC avec une télécommande

#### Ce dont vous aurez besoin
- **Câble HDMI** : Pour connecter votre ordinateur portable Ubuntu au moniteur.
- **Lecteur multimédia VLC** : Probablement déjà installé sur Ubuntu, ou facile à installer.
- **Smartphone ou un autre appareil** : Pour contrôler la lecture à distance via votre réseau domestique.

#### Étapes de configuration
1. **Connecter l'ordinateur portable au moniteur**
   - Branchez une extrémité d'un câble HDMI dans le port HDMI de votre ordinateur portable Ubuntu et l'autre dans l'entrée HDMI de votre moniteur.
   - Allumez le moniteur et sélectionnez la bonne entrée HDMI. L'affichage de l'ordinateur portable devrait maintenant apparaître sur le moniteur, y compris la vidéo et l'audio (si votre moniteur a des haut-parleurs ; sinon, utilisez les haut-parleurs de l'ordinateur portable ou connectez-en des externes).

2. **Installer VLC (s'il n'est pas déjà installé)**
   - Ouvrez un terminal sur votre ordinateur portable Ubuntu et exécutez :
     ```
     sudo apt update
     sudo apt install vlc
     ```
   - Cela garantit que VLC, un lecteur multimédia polyvalent, est prêt à l'emploi.

3. **Activer l'interface Web de VLC pour le contrôle à distance**
   - Ouvrez VLC sur votre ordinateur portable Ubuntu.
   - Allez dans **Outils > Préférences**.
   - En bas à gauche, cliquez sur **"Tout"** pour afficher les paramètres avancés.
   - Accédez à **Interface > Interfaces principales**, et cochez la case **"Web"** pour activer l'interface HTTP.
   - Allez dans **Interface > Interfaces principales > Lua**, et définissez un mot de passe (par exemple, "monmotdepasse") dans le champ **Lua HTTP Password**.
   - Cliquez sur **Sauvegarder**, puis redémarrez VLC.

4. **Charger vos films dans VLC**
   - Dans VLC, allez dans **Lecture > Liste de lecture**.
   - Glissez-déposez vos fichiers de films depuis leur dossier (où ils sont stockés sur l'ordinateur portable) dans la liste de lecture de VLC, ou utilisez **Média > Ouvrir un fichier** pour les ajouter un par un.
   - Sauvegardez la liste de lecture (par exemple, "Mes Films") via **Ctrl+Y** pour un accès rapide ultérieur.

5. **Trouver l'adresse IP de votre ordinateur portable**
   - Dans le terminal, tapez :
     ```
     ip addr show
     ```
   - Cherchez l'adresse IP sous votre connexion réseau (par exemple, `192.168.1.100` sous `wlan0` pour le Wi-Fi). C'est ainsi que votre téléphone se connectera à l'ordinateur portable.

6. **Contrôler la lecture depuis votre téléphone**
   - Assurez-vous que votre téléphone et votre ordinateur portable sont sur le même réseau Wi-Fi.
   - Ouvrez un navigateur web sur votre téléphone et entrez : `http://<ip-ordinateur-portable>:8080` (par exemple, `http://192.168.1.100:8080`).
   - Lorsque vous y êtes invité, laissez le nom d'utilisateur vide et entrez le mot de passe que vous avez défini (par exemple, "monmotdepasse").
   - Vous verrez l'interface web de VLC. Utilisez-la pour lire, mettre en pause, arrêter ou sélectionner le film suivant dans votre liste de lecture.

7. **Commencer à regarder**
   - Sur l'ordinateur portable, commencez à lire un film dans VLC (double-cliquez sur un élément dans la liste de lecture).
   - Passez VLC en mode plein écran (**Affichage > Plein écran** ou appuyez sur `F`).
   - Asseyez-vous et utilisez votre téléphone pour contrôler la lecture sans toucher à l'ordinateur portable.

#### Pourquoi cette solution vous convient
- **Aucun coût supplémentaire** : Utilise votre ordinateur portable, moniteur et téléphone existants—pas besoin d'acheter quoi que ce soit de nouveau.
- **Tracas minimes** : Après la configuration initiale, il vous suffit d'allumer l'ordinateur portable et le moniteur, d'ouvrir VLC et de tout contrôler depuis votre téléphone.
- **Lecture locale** : Puisque les films sont sur l'ordinateur portable connecté au moniteur, vous n'avez pas besoin de diffuser en streaming sur le réseau (bien que Nginx soit configuré, il n'est pas nécessaire ici). VLC lit les fichiers directement, garantissant des performances fluides.

#### Améliorations optionnelles
- **Contrôle sans fil** : Si vous avez une souris ou un clavier sans fil, vous pourriez les utiliser au lieu de votre téléphone, mais le téléphone est plus pratique à distance.
- **Démarrage automatique** : Pour simplifier encore plus, configurez VLC pour lancer votre liste de lecture automatiquement au démarrage de l'ordinateur portable :
  - Ajoutez VLC avec votre liste de lecture aux **Applications de démarrage** d'Ubuntu (cherchez "Applications de démarrage" dans Ubuntu, cliquez sur "Ajouter", et entrez : `vlc /chemin/vers/votre/liste.m3u`).
- **Vérification audio** : Si votre moniteur n'a pas de haut-parleurs, assurez-vous que l'audio passe par l'ordinateur portable ou connectez des haut-parleurs externes via la prise audio de l'ordinateur portable.

### Alternative : Utiliser Nginx et un navigateur (si préféré)
Si vous préférez utiliser le serveur Nginx :
- Configurez une page HTML simple dans votre répertoire Nginx (par exemple, `/var/www/html/films`) avec des liens vers vos fichiers de films (par exemple, `<a href="film1.mp4">Film 1</a>`).
- Connectez l'ordinateur portable au moniteur, ouvrez un navigateur et allez à `http://localhost/films`.
- Cliquez sur un lien pour lire un film dans le navigateur et utilisez le mode plein écran.
- Cependant, cela ne permet pas facilement un contrôle par téléphone, sauf si vous accédez à la même page depuis votre téléphone et effectuez un cast, ce qui pourrait nécessiter une configuration ou du matériel supplémentaire.

### Recommandation finale
La méthode VLC est la mieux adaptée. Elle est simple, tire parti de votre configuration actuelle et vous permet "d'allumer le moniteur, puis de regarder sans trop de tracas" en contrôlant tout depuis votre téléphone. Après l'avoir configurée une fois, vous n'aurez plus qu'à lancer VLC et utiliser votre téléphone pour choisir les films—simple et efficace