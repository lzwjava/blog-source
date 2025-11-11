---
audio: false
generated: true
lang: fr
layout: post
title: Diffusion de Fichiers MKV sur iPad avec VLC Mobile et d'Autres Applications
translated: true
type: note
---

Pour diffuser vos fichiers `.mkv` depuis votre serveur Nginx (par exemple, `http://192.168.1.27/movies/`) sur votre iPad sans les télécharger entièrement, vous aurez besoin d'une application qui prend en charge la diffusion HTTP et la lecture des fichiers `.mkv`. iPadOS ne gère pas nativement les fichiers `.mkv` dans Safari ou l'application Fichiers, donc un lecteur multimédia tiers est la solution. Voici comment réaliser cette "magie" sur votre iPad :

### Applications Recommandées pour la Diffusion `.mkv` sur iPad
#### 1. VLC for Mobile (Gratuit, Meilleure Option)
VLC est disponible sur iPadOS et fonctionne de manière similaire à la version Mac, prenant en charge la diffusion HTTP avec des requêtes de plage.
- **Installer** :
  1. Ouvrez l'**App Store** sur votre iPad.
  2. Recherchez **VLC for Mobile**.
  3. Appuyez sur **Obtenir** (ou l'icône nuage si vous l'avez déjà installé), puis authentifiez-vous avec votre Apple ID si demandé.
- **Diffuser** :
  1. Ouvrez l'application **VLC**.
  2. Appuyez sur l'onglet **Network** (icône cône) en bas.
  3. Sélectionnez **Open Network Stream**.
  4. Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
  5. Appuyez sur **Open Network Stream** (ou le bouton de lecture).
- **Pourquoi ça marche** : VLC met le flux en mémoire tampon, vous permettant de lire et de naviguer sans télécharger le fichier entier.

#### 2. nPlayer (Payant, Option Premium)
nPlayer est un lecteur multimédia puissant avec une excellente prise en charge des fichiers `.mkv` et des capacités de diffusion.
- **Installer** :
  1. Ouvrez l'**App Store**.
  2. Recherchez **nPlayer** (coûte environ 8,99 $, mais il existe une version Lite gratuite avec des publicités).
  3. Appuyez sur **Obtenir** ou **Acheter**, puis installez.
- **Diffuser** :
  1. Ouvrez **nPlayer**.
  2. Appuyez sur l'icône **+** ou l'option **Network**.
  3. Sélectionnez **Add URL** ou **HTTP/HTTPS**.
  4. Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
  5. Appuyez sur **Play**.
- **Pourquoi ça marche** : Prend en charge les codecs avancés et une diffusion fluide ; excellente interface utilisateur pour iPad.

#### 3. Infuse (Gratuit avec Achats In-App)
Infuse est un autre choix populaire pour diffuser et lire des fichiers `.mkv`, avec une interface élégante.
- **Installer** :
  1. Ouvrez l'**App Store**.
  2. Recherchez **Infuse**.
  3. Appuyez sur **Obtenir** (la version gratuite fonctionne pour la diffusion de base ; la mise à niveau Pro est optionnelle).
- **Diffuser** :
  1. Ouvrez **Infuse**.
  2. Appuyez sur **Add Files** > **Via URL**.
  3. Entrez `http://192.168.1.27/movies/votre_fichier.mkv`.
  4. Appuyez sur **Add** ou **Play**.
- **Pourquoi ça marche** : Diffuse via HTTP et gère bien les fichiers `.mkv` ; les fonctionnalités Pro (comme AirPlay) sont optionnelles.

### Étapes pour Commencer
1. **Connectez-vous au Même Réseau** :
   - Assurez-vous que votre iPad est sur le même réseau Wi-Fi que votre serveur Nginx (par exemple, `192.168.1.x`).
   - Testez la connectivité : Ouvrez Safari sur votre iPad et allez à `http://192.168.1.27/movies/`. Vous devriez voir la liste des fichiers (même si Safari ne peut pas lire les `.mkv`).

2. **Choisissez une Application** :
   - **VLC** est gratuit et fiable — commencez par là.
   - Installez-le depuis l'App Store comme décrit.

3. **Entrez l'URL** :
   - Utilisez l'URL exacte de votre fichier `.mkv` (par exemple, `http://192.168.1.27/movies/votre_fichier.mkv`).
   - Vous pouvez copier le lien depuis la liste des fichiers dans Safari et le coller dans l'application.

4. **Lisez et Profitez** :
   - L'application diffusera la vidéo. Vous pouvez mettre en pause, naviguer ou ajuster la lecture sans télécharger le fichier entier.

### Dépannage
- **La Connexion Échoue** : Si l'iPad ne peut pas atteindre `192.168.1.27`, assurez-vous que le pare-feu du serveur autorise le port 80 (`sudo ufw allow 80`) et que l'iPad est sur le même LAN.
- **Mise en Mémoire Tampon** : Un Wi-Fi lent peut causer des retards — rapprochez-vous du routeur ou vérifiez la vitesse de votre réseau.
- **Problèmes de Codec** : Si le fichier `.mkv` ne lit pas, il utilise peut-être un codec non pris en charge (par exemple, VP9). VLC gère la plupart, mais vous pourriez le ré-encoder avec HandBrake en H.264/AAC pour une compatibilité plus large.
- **Faute de Frappe dans l'URL** : Vérifiez l'adresse IP et le chemin — `http://192.168.1.27/movies/votre_fichier.mkv` doit correspondre à votre configuration.

### Bonus : Parcourir et Sélectionner
Puisque `autoindex on;` vous donne un listing de répertoire :
- Ouvrez Safari sur votre iPad, allez à `http://192.168.1.27/movies/`, appuyez sur un lien de fichier, puis copiez l'URL.
- Collez-la dans VLC/nPlayer/Infuse pour la diffusion.

Avec **VLC for Mobile**, vous aurez cette "magie" sur votre iPad en un rien de temps — en diffusant vos fichiers `.mkv` sans effort ! Faites-moi savoir si vous avez besoin d'aide pour le configurer.