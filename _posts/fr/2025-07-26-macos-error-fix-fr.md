---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les erreurs de permissions de fichiers sur macOS
translated: true
type: note
---

### Comprendre l'erreur
Ce message d'erreur apparaît généralement sur macOS lorsque vous essayez de déplacer, copier, supprimer ou manipuler des fichiers/dossiers (par exemple, vider la Corbeille ou faire glisser des éléments), mais que le système rencontre des problèmes de permissions, des fichiers verrouillés ou des restrictions en lecture seule. Le message lui-même fournit la solution principale, mais des étapes supplémentaires sont parfois nécessaires si le problème persiste, comme l'utilisation de commandes Terminal, la réparation des permissions du disque ou la gestion de fichiers récalcitrants.

### Corrections étape par étape
Suivez ces étapes dans l'ordre, en commençant par la plus simple. Ces étapes supposent que vous êtes sur macOS (par exemple, Ventura, Sonoma ou une version ultérieure). Assurez-vous d'être connecté en tant qu'utilisateur administrateur.

1.  **Déverrouiller les fichiers et ajuster les permissions (comme suggéré dans l'erreur)** :
    *   Sélectionnez le fichier ou le dossier problématique dans le Finder.
    *   Faites un clic droit (ou Contrôle + clic) et choisissez **Lire les informations** (ou appuyez sur Commande + I).
    *   Dans la fenêtre Lire les informations :
        *   Dans la section **Général**, décochez la case **Verrouillé** si elle est sélectionnée.
        *   Faites défiler jusqu'à la section **Partage et permissions** en bas.
        *   Cliquez sur l'icône du cadenas dans le coin inférieur droit et entrez votre mot de passe administrateur pour déverrouiller les modifications.
        *   Pour votre nom d'utilisateur (ou "tout le monde" si nécessaire), définissez le Privilège sur **Lecture et écriture**.
    *   Si plusieurs éléments sont concernés, vous pouvez tous les sélectionner, ouvrir Lire les informations et appliquer les modifications (maintenez la touche Commande enfoncée pour en sélectionner plusieurs).
    *   Fermez la fenêtre et réessayez l'opération (par exemple, supprimez ou déplacez les fichiers).

2.  **Si le problème concerne la Corbeille (scénario courant)** :
    *   Cette erreur apparaît souvent lors du vidage de la Corbeille si des fichiers sont verrouillés ou ont des problèmes de permissions.
    *   Tout d'abord, ouvrez la Corbeille, sélectionnez les éléments et appliquez les étapes Lire les informations ci-dessus pour les déverrouiller/ajuster les permissions.
    *   Si cela ne fonctionne pas, forcez le vidage de la Corbeille :
        *   Maintenez la touche Option enfoncée tout en cliquant avec le bouton droit sur l'icône de la Corbeille dans le Dock et sélectionnez **Vider la Corbeille**.
    *   Alternative via Terminal (si l'interface graphique échoue) :
        *   Ouvrez Terminal (depuis Applications > Utilitaires ou la recherche Spotlight).
        *   Tapez : `sudo rm -rf ~/.Trash/*` et appuyez sur Entrée.
        *   Entrez votre mot de passe administrateur (il ne s'affichera pas pendant que vous tapez).
        *   Avertissement : Cela supprime définitivement tout le contenu de la Corbeille — utilisez cette commande avec prudence, car il n'y a pas d'annulation.

3.  **Réparer les permissions du disque à l'aide de l'Utilitaire de disque** :
    *   Ouvrez **Utilitaire de disque** (depuis Applications > Utilitaires ou la recherche Spotlight).
    *   Sélectionnez votre disque principal (par exemple, Macintosh HD) dans la barre latérale.
    *   Cliquez sur **Premiers secours** > **Exécuter** (ou **Réparer les permissions du disque** dans les anciennes versions de macOS).
    *   Laissez l'opération se terminer, puis redémarrez votre Mac et réessayez.

4.  **Vérifier les disques externes ou les volumes réseau** :
    *   Si les fichiers se trouvent sur un disque externe, une clé USB ou un partage réseau :
        *   Éjectez et reconnectez le lecteur.
        *   Dans Lire les informations, assurez-vous que la case **Ignorer la propriété de ce volume** est cochée (dans Partage et permissions).
    *   Pour les formats en lecture seule (par exemple, les lecteurs NTFS), vous pourriez avoir besoin d'outils tiers comme Paragon NTFS pour un accès en écriture.

5.  **Correctifs avancés via Terminal (si les permissions sont récalcitrantes)** :
    *   Pour réinitialiser les permissions sur un dossier/fichier spécifique :
        *   Dans Terminal : `sudo chmod -R 777 /chemin/vers/le/dossier` (remplacez `/chemin/vers/le/dossier` par le chemin réel ; faites glisser le dossier dans Terminal pour le remplir automatiquement).
        *   Cela définit les permissions complètes de lecture/écriture/exécution pour tout le monde — à utiliser avec parcimonie.
    *   Pour déverrouiller tous les fichiers d'un répertoire : `sudo chflags -R nouchg /chemin/vers/le/dossier`.
    *   Redémarrez en mode sans échec (maintenez la touche Majuscule enfoncée pendant le démarrage) pour effacer les caches, puis réessayez.

6.  **Autres dépannages** :
    *   **Redémarrez votre Mac** : Simple mais résout souvent des problèmes temporaires.
    *   **Mettez à jour macOS** : Allez dans Paramètres Système > Général > Mise à jour de logiciel.
    *   **Vérifiez les interférences de logiciels malveillants/antivirus** : Exécutez une analyse avec Malwarebytes ou un logiciel similaire.
    *   Si les fichiers proviennent de téléchargements ou d'applications, assurez-vous qu'ils ne sont pas mis en quarantaine : Dans Terminal, `xattr -d com.apple.quarantine /chemin/vers/le/fichier`.
    *   Si rien ne fonctionne, démarrez en mode de récupération (Commande + R au démarrage), exécutez Premiers secours sur le disque, ou envisagez de réinitialiser les permissions via Terminal en mode de récupération.

Si l'erreur persiste après ces étapes, fournissez plus de détails comme votre version de macOS, l'opération que vous essayez de réaliser (par exemple, supprimer des fichiers spécifiques) et si cela concerne la Corbeille ou un autre emplacement.

### Références
[Assistance Apple : Modifier les permissions de fichiers, de dossiers ou de disques sur Mac](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)
[Comment corriger l'erreur "L'opération n'a pas pu être achevée" sur Mac](https://www.macrumors.com/how-to/fix-operation-cant-be-completed-error-mac/)
[Vider la Corbeille lorsqu'un message indique que des fichiers sont utilisés](https://apple.stackexchange.com/questions/52257/empty-trash-when-it-says-files-are-in-use)