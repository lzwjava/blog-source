---
audio: false
generated: true
lang: fr
layout: post
title: Diffusion de Fichiers MKV depuis Nginx avec VLC
translated: true
type: note
---

Puisque vous avez un serveur Nginx qui sert des fichiers `.mkv` (par exemple, à l'adresse `http://192.168.1.27/movies/`) et que vous souhaitez les visualiser depuis un Mac sans télécharger le fichier entier, vous cherchez à **streamer** les vidéos. Nginx peut servir les fichiers d'une manière qui prend en charge les requêtes HTTP de plage (ce qu'il fait par défaut), permettant aux lecteurs multimédias de streamer plutôt que de télécharger complètement. Voici comment procéder, ainsi que des outils adaptés pour macOS.

### Prérequis
- Votre configuration Nginx (par exemple, `alias /var/www/movies/; autoindex on;`) fonctionne, et `http://192.168.1.27/movies/` liste les fichiers.
- Les fichiers `.mkv` sont accessibles via le réseau (testés depuis une autre machine).

### Outils pour Streamer les Fichiers `.mkv` sur macOS
Vous avez besoin d'un lecteur multimédia qui prend en charge le streaming via HTTP et gère bien les fichiers `.mkv`. Voici les meilleures options :

#### 1. VLC Media Player (Gratuit, Recommandé)
VLC est un lecteur polyvalent et open-source qui prend en charge le streaming des fichiers `.mkv` via HTTP sans télécharger le fichier entier (il utilise les requêtes de plage).
- **Installer** :
  - Téléchargez-le sur [videolan.org](https://www.videolan.org/vlc/).
  - Installez-le sur votre Mac.
- **Streamer** :
  1. Ouvrez VLC.
  2. Appuyez sur `Cmd + N` (ou allez dans `Fichier > Ouvrir un flux réseau`).
  3. Entrez l'URL, par exemple `http://192.168.1.27/movies/votre_fichier.mkv`.
  4. Cliquez sur `Ouvrir`.
- **Pourquoi ça marche** : VLC ne met en mémoire tampon que ce qui est nécessaire, vous permettant de naviguer et de lire sans télécharger le fichier entier.

#### 2. IINA (Gratuit, Natif macOS)
IINA est un lecteur moderne, spécifique à macOS, avec une excellente prise en charge des `.mkv` et des capacités de streaming.
- **Installer** :
  - Téléchargez-le sur [iina.io](https://iina.io/) ou `brew install iina` (avec Homebrew).
- **Streamer** :
  1. Ouvrez IINA.
  2. Appuyez sur `Cmd + U` (ou `Fichier > Ouvrir une URL`).
  3. Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
  4. Cliquez sur `OK`.
- **Pourquoi ça marche** : Léger, prend en charge le streaming HTTP et s'intègre parfaitement avec macOS.

#### 3. QuickTime Player (Intégré, Limité)
Le QuickTime Player par défaut de macOS peut streamer certains formats, mais la prise en charge des `.mkv` est variable sans codecs supplémentaires.
- **Essayez** :
  1. Ouvrez QuickTime Player.
  2. Appuyez sur `Cmd + U` (ou `Fichier > Ouvrir l'emplacement`).
  3. Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
  4. Cliquez sur `Ouvrir`.
- **Mise en garde** : Si cela ne fonctionne pas, installez Perian (un ancien pack de codecs) ou utilisez VLC/IINA à la place.

#### 4. Navigateur (Safari/Chrome, Le Plus Simple)
Les navigateurs modernes peuvent streamer directement les fichiers `.mkv` s'ils sont encodés avec des codecs pris en charge (par exemple, vidéo H.264, audio AAC).
- **Comment** :
  1. Ouvrez Safari ou Chrome sur votre Mac.
  2. Allez à `http://192.168.1.27/movies/`.
  3. Cliquez sur `votre_fichier.mkv`.
- **Pourquoi ça marche** : Les navigateurs utilisent les balises vidéo HTML5 et les requêtes de plage pour le streaming.
- **Limitation** : Si le `.mkv` utilise des codecs non pris en charge (par exemple, VP9, Opus), il ne se lira pas—reposez-vous sur VLC ou IINA.

### S'assurer que Nginx Prend en Charge le Streaming
Nginx gère les requêtes de plage par défaut, ce qui permet le streaming. Pour confirmer :
- Vérifiez que votre configuration ne désactive pas cela (par exemple, pas de `limit_rate` ou d'en-têtes personnalisés bloquant les plages).
- Testez avec VLC ou IINA—si vous pouvez naviguer (par exemple, sauter à 5 minutes), le streaming fonctionne.

### Flux de Travail Recommandé
1. **Utilisez VLC** (c'est le plus fiable) :
   - Installez VLC.
   - Ouvrez `http://192.168.1.27/movies/votre_fichier.mkv` via `Cmd + N`.
   - Lisez, mettez en pause ou naviguez selon les besoins.
2. **Navigation dans le Répertoire** :
   - Visitez `http://192.168.1.27/movies/` dans Safari/Chrome pour voir la liste des fichiers (grâce à `autoindex on;`).
   - Copiez l'URL de `votre_fichier.mkv` et collez-la dans VLC ou IINA.

### Dépannage
- **Problèmes de Mise en Mémoire Tampon** : Un réseau lent ou de gros fichiers `.mkv` peuvent causer des latences—assurez-vous que votre LAN est stable (par exemple, que le Wi-Fi ne coupe pas).
- **Erreurs de Codec** : Si VLC indique "format non supporté", le `.mkv` utilise peut-être des codecs rares—essayez de le ré-encoder avec HandBrake en H.264/AAC.
- **Connexion Refusée** : Revérifiez les paramètres du pare-feu sur le serveur (`sudo ufw allow 80` ou équivalent).

Avec VLC ou IINA, vous streamerez vos fichiers `.mkv` depuis votre Mac en un rien de temps sans les télécharger complètement. Faites-moi savoir si vous rencontrez des problèmes !

---

Installer VLC sur un Mac est simple. Voici un guide rapide pour le configurer afin que vous puissiez streamer vos fichiers `.mkv` depuis votre serveur Nginx :

### Méthode 1 : Téléchargement depuis le Site Officiel
1. **Visitez le Site Web de VLC** :
   - Ouvrez votre navigateur (par exemple, Safari ou Chrome).
   - Allez sur [https://www.videolan.org/vlc/](https://www.videolan.org/vlc/).

2. **Téléchargez VLC** :
   - Cliquez sur le bouton **Download VLC**. Il devrait automatiquement détecter votre macOS et proposer la version correcte (par exemple, VLC 3.0.20 à l'heure actuelle).
   - Vous obtiendrez un fichier `.dmg` (par exemple, `vlc-3.0.20.dmg`).

3. **Installez VLC** :
   - Ouvrez le fichier `.dmg` téléchargé (généralement dans votre dossier `Téléchargements`).
   - Faites glisser l'icône VLC vers le dossier **Applications** comme indiqué dans la fenêtre.
   - Fermez la fenêtre du `.dmg` et éjectez-le (clic droit sur l'icône du disque sur votre bureau ou dans le Finder et sélectionnez "Éjecter").

4. **Lancez VLC** :
   - Allez dans votre dossier **Applications** (par exemple, via le Finder ou Spotlight avec `Cmd + Espace`, puis tapez "Applications").
   - Double-cliquez sur **VLC**.
   - Si macOS le bloque ("développeur non identifié"), faites un clic droit sur VLC, sélectionnez **Ouvrir**, puis cliquez sur **Ouvrir** dans la boîte de dialogue.

5. **Streamer Votre Fichier** :
   - Ouvrez VLC.
   - Appuyez sur `Cmd + N` (ou `Fichier > Ouvrir un flux réseau`).
   - Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
   - Cliquez sur **Ouvrir**.

### Méthode 2 : Installation via Homebrew (Terminal)
Si vous préférez la ligne de commande et avez Homebrew installé :
1. **Installez Homebrew** (si pas déjà fait) :
   - Ouvrez le Terminal.
   - Exécutez :
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Suivez les instructions.

2. **Installez VLC** :
   - Dans le Terminal :
     ```bash
     brew install vlc
     ```

3. **Lancez VLC** :
   - Lancez-le depuis le Terminal avec :
     ```bash
     open -a VLC
     ```
   - Ou trouvez-le dans **Applications** sous le nom `VLC.app`.

4. **Streamer** :
   - Identique à ci-dessus : `Cmd + N`, entrez votre URL, et lisez.

### Vérifier l'Installation
- Une fois installé, VLC devrait apparaître dans votre dossier **Applications**.
- Testez-le d'abord avec un fichier local (glissez-déposez un `.mkv` dans VLC) pour vous assurer qu'il fonctionne, puis essayez de streamer `http://192.168.1.27/movies/votre_fichier.mkv`.

### Dépannage
- **Échec du Téléchargement** : Utilisez un lien miroir sur le site de VLC si le téléchargement principal est lent.
- **Alerte de Sécurité** : Si macOS le bloque, allez dans `Préférences Système > Sécurité et Confidentialité > Général` et cliquez sur **Ouvrir quand même**.
- **Ne Joue Pas** : Assurez-vous que l'URL est correcte et que votre serveur est accessible (`ping 192.168.1.27` depuis le Terminal).

C'est tout ! VLC devrait maintenant être prêt sur votre Mac pour streamer vos fichiers `.mkv`. Faites-moi savoir si vous avez besoin d'aide pour l'étape suivante !