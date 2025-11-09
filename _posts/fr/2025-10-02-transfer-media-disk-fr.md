---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Transfert de médias vers un disque externe
translated: true
type: note
---

### Transférer des photos et vidéos vers un disque portable sur macOS

D'après les informations de votre système, vous utilisez un système macOS 15.6.1 avec un disque portable monté sur `/Volumes/Untitled` (capacité totale de 2,0 To, 1,5 To disponible). Transférer des photos et des vidéos implique de déplacer des fichiers du stockage de votre Mac (par exemple, dans `~/Pictures` pour les photos ou `~/Movies` pour les vidéos) vers le disque externe. Cela peut être fait via l'interface graphique (Finder) ou des outils en ligne de commande comme le Terminal, selon votre préférence. Je vais détailler les deux méthodes ci-dessous, en supposant que vous déplacez des fichiers plutôt que l'intégralité de la bibliothèque de l'application Photos (si nécessaire, exportez-les d'abord depuis l'application Photos).

**Notes importantes :**
- **Sauvegarde préalable :** Assurez-vous d'avoir des sauvegardes de vos fichiers pour éviter toute perte de données en cas d'erreur.
- **Permissions :** Vous pourriez avoir besoin de permissions d'administrateur pour certaines actions. Exécutez les commandes Terminal en tant qu'admin si vous y êtes invité.
- **Vérification de l'espace :** Vérifiez que la taille des fichiers ne dépasse pas l'espace disponible sur le disque portable (1,5 To dans votre cas).
- **Emplacements des fichiers :** Les chemins par défaut sont `~/Pictures` pour les photos et `~/Movies` pour les vidéos. S'ils se trouvent dans d'autres répertoires (par exemple, Téléchargements), ajustez en conséquence.
- **Démontage sécurisé :** Après le transfert, démontez le disque via Finder > Éjecter ou `diskutil unmount /Volumes/Untitled` pour éviter toute corruption.

#### 1. Utilisation du Finder (Méthode graphique - Conviviale pour les débutants)
C'est la méthode la plus simple pour la plupart des utilisateurs. Elle implique un glisser-déposer via le gestionnaire de fichiers de macOS.

1. **Localisez le disque portable et les fichiers :**
   - Ouvrez le Finder (cliquez sur l'icône du smiley dans le Dock).
   - Dans la barre latérale, sous "Périphériques", vous verrez "Untitled" (votre disque portable). Cliquez dessus pour parcourir son contenu.
   - Ouvrez une autre fenêtre du Finder (Commande + N) et naviguez jusqu'à l'emplacement de stockage de vos photos/vidéos (par exemple, votre dossier Images ou Films).

2. **Déplacez les fichiers :**
   - Sélectionnez les photos/vidéos que vous souhaitez déplacer (maintenez la touche Commande enfoncée pour une sélection multiple).
   - Faites-les glisser de leur emplacement actuel vers la fenêtre du disque portable (par exemple, créez d'abord un dossier comme "SauvegardePhotos" sur le disque pour une meilleure organisation).
   - Pour *déplacer* (relocaliser définitivement, libérant de l'espace sur votre Mac), maintenez la touche Option enfoncée tout en faisant glisser. Pour *copier* (dupliquer), faites simplement glisser normalement.
     - Alternativement, faites un clic droit sur les fichiers sélectionnés > "Mettre à la corbeille" après la copie pour effectivement les "déplacer" en supprimant les originaux après copie.
   - Si vous organisez, créez des dossiers sur le disque (clic droit > Nouveau dossier) comme "Photos" et "Vidéos".

3. **Vérifiez et éjectez :**
   - Ouvrez le disque portable dans le Finder et confirmez que les fichiers s'y trouvent.
   - Faites glisser l'icône du disque vers la Corbeille (ou clic droit > Éjecter) pour le démonter en toute sécurité avant de le déconnecter.

Cette méthode préserve les métadonnées (par exemple, les dates de création) et gère efficacement les fichiers volumineux.

#### 2. Utilisation du Terminal (Méthode en ligne de commande - Efficace pour les opérations en lot)
Si vous préférez l'utilisation de scripts ou la gestion par commandes (comme montré dans vos scripts Python), utilisez le Terminal pour plus de précision. C'est utile pour les déplacements automatisés ou récursifs.

1. **Naviguez vers vos fichiers et le disque :**
   - Ouvrez le Terminal (Applications > Utilitaires > Terminal).
   - Vérifiez votre répertoire actuel : Exécutez `pwd` et naviguez si nécessaire (par exemple, `cd ~/Pictures` pour accéder aux photos).
   - Confirmez que le disque est monté : Exécutez `ls /Volumes` pour voir "Untitled". Votre disque est déjà monté d'après la sortie fournie.

2. **Déplacez les fichiers :**
   - Pour **déplacer** des fichiers (relocaliser définitivement, en les supprimant de l'emplacement d'origine) :
     - Pour des fichiers individuels : `mv /chemin/vers/photo.jpg /Volumes/Untitled/Photos/`
     - Pour des répertoires (par exemple, un dossier Photos entier) : `mv ~/Pictures/PhotosLibrary /Volumes/Untitled/`
     - Exemple de déplacement complet : `mv ~/Pictures/* /Volumes/Untitled/Photos/` (déplace tout le contenu de Pictures vers un nouveau dossier sur le disque ; ajoutez des options comme `-v` pour une sortie verbeuse).
   - Pour **copier** à la place (dupliquer sans supprimer les originaux) : Utilisez `cp` avec `-r` pour les répertoires récursifs.
     - Exemple : `cp -r ~/Pictures/PhotosLibrary /Volumes/Untitled/Photos/` (copie récursivement ; idéal pour les sauvegardes où vous souhaitez conserver les originaux).
   - Pour les vidéos dans Films : `cp -r ~/Movies/Videos/ /Volumes/Untitled/Videos/`
   - Pour gérer les fichiers cachés ou les permissions : Ajoutez `sudo` si nécessaire (par exemple, `sudo mv ~/Pictures/photo.jpg /Volumes/Untitled/`).
   - Par sécurité, prévisualisez ce que vous allez déplacer : `ls -la ~/Pictures` pour lister les fichiers.

3. **Vérifiez et démontez :**
   - Vérifiez le disque : `ls /Volumes/Untitled` pour confirmer les transferts.
   - Démontage sécurisé : `diskutil unmount /Volumes/Untitled` puis déconnectez physiquement le disque.

**Conseils avancés :**
- **Utilisez Rsync pour la synchronisation :** Pour les sauvegardes incrémentielles (uniquement les fichiers nouveaux/modifiés), `rsync -av ~/Pictures /Volumes/Untitled/Photos` (installez rsync s'il n'est pas présent, mais il est intégré à macOS).
- **Automatisation :** Adaptez cela dans vos scripts Python (par exemple, en utilisant `subprocess` pour exécuter des commandes `cp` ou `mv` basées sur la sortie de `list_portable_disks.py`).
- **Spécificités MacBook :** Sur votre MacBook Air M2 (Modèle Mac14,2), les transferts devraient être rapides via USB-C. Surveillez la batterie/la température (par exemple, via le Moniteur d'activité) si nécessaire.

Si vous rencontrez des problèmes (par exemple, des erreurs de permissions), fournissez plus de détails comme les chemins de fichiers exacts ou les messages d'erreur pour des conseils adaptés. Ce processus devrait fonctionner de manière fiable sur votre configuration.