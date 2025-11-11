---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de qBittorrent pour le Partage et la Gestion Automatique des
  Fichiers
translated: true
type: note
---

Il semble que vous souhaitiez configurer qBittorrent pour continuer à partager (seeder) vos torrents tout en déplaçant automatiquement les fichiers `.mkv` terminés vers `/var/www/movies` pour les servir sur un serveur. Je vais vous guider à travers les étapes pour y parvenir, en supposant que vous utilisez qBittorrent sur un système où `/var/www/movies` est un répertoire valide (par exemple, un serveur Linux avec un serveur web comme Apache ou Nginx). Voici comment procéder :

---

### Guide étape par étape

#### 1. **Comprendre la gestion des fichiers de qBittorrent**
   - qBittorrent peut déplacer les fichiers automatiquement après la fin du téléchargement tout en continuant à les partager, à condition d'utiliser correctement ses fonctions intégrées "Définir l'emplacement" ou "Déplacer". Déplacer les fichiers manuellement en dehors de qBittorrent (par exemple, via l'explorateur de fichiers) interrompra le partage sauf si vous redirigez qBittorrent vers le nouvel emplacement.

#### 2. **Configurer les paramètres de qBittorrent**
   - Ouvrez qBittorrent.
   - Allez dans **Outils > Options** (ou appuyez sur `Alt + O`).

   ##### a) **Définir l'emplacement de téléchargement par défaut**
   - Sous l'onglet **Téléchargements** :
     - Définissez **Chemin de sauvegarde par défaut** sur un répertoire temporaire où les fichiers seront téléchargés initialement (par exemple, `/home/user/downloads` ou là où vous avez de l'espace). C'est ici que qBittorrent stockera les fichiers pendant le téléchargement et le partage jusqu'à ce qu'ils soient déplacés.
     - Assurez-vous que **Garder les fichiers incomplets dans** est défini sur le même répertoire ou un répertoire différent si vous préférez (optionnel).

   ##### b) **Activer le déplacement automatique des fichiers**
   - Descendez jusqu'à **Quand le torrent se termine** :
     - Cochez la case pour **Déplacer automatiquement les téléchargements terminés vers**.
     - Définissez le chemin sur `/var/www/movies`. Cela indique à qBittorrent de déplacer les fichiers `.mkv` vers `/var/www/movies` une fois le téléchargement terminé.
   - Important : qBittorrent continuera à partager depuis le nouvel emplacement (`/var/www/movies`) après le déplacement, vous n'avez donc pas à vous soucier de perdre la capacité de partage.

   ##### c) **Optionnel : Filtrer pour les fichiers .mkv**
   - Si vous souhaitez que seuls les fichiers `.mkv` soient déplacés vers `/var/www/movies` (et non d'autres types de fichiers comme `.txt` ou `.nfo`), vous pouvez utiliser la fonction **Exécuter un programme externe** de qBittorrent (voir l'étape 3 ci-dessous) au lieu de l'option de déplacement automatique.

   ##### d) **Limites de partage**
   - Sous l'onglet **BitTorrent** ou **Téléchargements** :
     - Définissez les limites de partage si vous le souhaitez (par exemple, partager jusqu'à un certain ratio ou un certain temps). Pour un partage illimité, définissez **Ratio** et **Temps** sur `0` ou décochez les limites.
     - Cela garantit que qBittorrent continue à uploader vos seeds indéfiniment depuis `/var/www/movies`.

   - Cliquez sur **Appliquer** puis **OK** pour sauvegarder les paramètres.

#### 3. **Alternative : Utiliser "Exécuter un programme externe" pour plus de contrôle**
   - Si vous avez besoin de plus de personnalisation (par exemple, ne déplacer que les fichiers `.mkv` et laisser les autres en partage depuis l'emplacement d'origine), utilisez cette méthode :
     - Dans **Options > Téléchargements**, descendez jusqu'à **Exécuter un programme externe**.
     - Cochez **Exécuter un programme externe à la fin du torrent**.
     - Entrez une commande comme :
       ```
       mv "%F"/*.mkv /var/www/movies/
       ```
       - `%F` est un espace réservé de qBittorrent pour le chemin du dossier de contenu. Cette commande ne déplace que les fichiers `.mkv` vers `/var/www/movies`.
     - Note : qBittorrent continuera à partager les fichiers `.mkv` depuis `/var/www/movies` après le déplacement, mais les autres fichiers (par exemple, `.torrent`, `.nfo`) resteront à l'emplacement d'origine et continueront à être partagés depuis là, sauf si vous ajustez davantage.

#### 4. **Vérifier les permissions**
   - Assurez-vous que qBittorrent a les permissions d'écriture sur `/var/www/movies` :
     - Sur Linux, exécutez :
       ```
       sudo chown -R <utilisateur-qbittorrent>:<groupe-qbittorrent> /var/www/movies
       sudo chmod -R 775 /var/www/movies
       ```
       Remplacez `<utilisateur-qbittorrent>` et `<groupe-qbittorrent>` par l'utilisateur et le groupe sous lesquels qBittorrent s'exécute (par exemple, votre nom d'utilisateur ou `qbittorrent` s'il s'agit d'un service).
   - Sans les permissions appropriées, qBittorrent ne pourra pas déplacer les fichiers vers ce répertoire.

#### 5. **Tester la configuration**
   - Ajoutez un torrent avec des fichiers `.mkv` à qBittorrent.
   - Attendez qu'il termine le téléchargement.
   - Vérifiez que :
     - Les fichiers `.mkv` sont déplacés vers `/var/www/movies`.
     - Le statut du torrent dans qBittorrent passe à **Partage (Seeding)**, et la vitesse d'upload indique qu'il partage toujours les fichiers.
   - Visitez `/var/www/movies` pour confirmer que les fichiers sont là et accessibles (par exemple, via votre serveur web à l'adresse `http://<adresse-ip-du-serveur>/movies`).

#### 6. **Déplacer manuellement les fichiers existants (si nécessaire)**
   - Pour les torrents que vous avez déjà téléchargés et que vous souhaitez déplacer vers `/var/www/movies` sans interrompre le partage :
     - Dans qBittorrent, faites un clic droit sur le torrent.
     - Sélectionnez **Définir l'emplacement**.
     - Choisissez `/var/www/movies` et laissez qBittorrent déplacer les fichiers.
     - Après le déplacement, qBittorrent reprendra le partage depuis le nouvel emplacement.

#### 7. **Optimiser les paramètres d'upload**
   - Pour maximiser le partage :
     - Allez dans **Options > Vitesse** :
       - Définissez **Upload** sur `0` (illimité) ou une valeur élevée (par exemple, 80 % de votre vitesse d'upload maximale).
     - Allez dans **Options > Connexion** :
       - Assurez-vous que **Activer le transfert de port UPnP / NAT-PMP** est coché (si votre routeur le supporte) ou transférez manuellement un port pour une meilleure connectivité.
       - Augmentez le **Nombre maximum global de slots d'upload** (par exemple, à 50 ou 100) pour permettre à plus de pairs de se connecter.

---

### Notes importantes
- **Continuité du partage** : Tant que vous laissez qBittorrent gérer le déplacement des fichiers (via le déplacement automatique ou "Définir l'emplacement"), il mettra à jour son suivi interne et continuera à partager depuis `/var/www/movies`.
- **Accès au serveur web** : Assurez-vous que votre serveur web (par exemple, Apache/Nginx) est configuré pour servir les fichiers depuis `/var/www/movies`. Cela dépasse le cadre de qBittorrent mais est essentiel pour votre objectif de serveur.
- **Stockage** : Assurez-vous que `/var/www/movies` a assez d'espace pour vos fichiers.

Si vous rencontrez des problèmes (par exemple, les fichiers ne se déplacent pas ou le partage s'arrête), faites-moi part des détails de votre configuration (OS, version de qBittorrent, etc.), et j'affinerai la solution !