---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Libérer de l'Espace de Stockage Système sur macOS
translated: true
type: note
---

### Aperçu du nettoyage de l'espace de stockage système sur macOS

D'après les recommandations officielles d'Apple et les conseils d'experts, libérer de l'espace sur macOS (version 15.6.1 comme la vôtre) implique d'utiliser les outils intégrés pour optimiser le stockage, de vider en toute sécurité les caches amovibles et de supprimer les fichiers inutiles. Les Données système incluent souvent les caches, les fichiers temporaires et les journaux – dont une grande partie peut être supprimée manuellement ou automatiquement sans endommager votre Mac. Évitez de supprimer les fichiers système critiques, car cela pourrait provoquer une instabilité. Votre système indique environ 13 Gio disponibles sur 460 Gio au total, avec 45 % utilisés, concentrez-vous donc sur les caches, les téléchargements et les pièces jointes pour des gains rapides.[1][2][3]

### Utilisation des outils intégrés de gestion du stockage macOS
Apple propose des méthodes intégrées pour analyser et libérer de l'espace sans applications tierces.
1.  **Vérifier l'utilisation du stockage** : Allez dans le menu Pomme > Paramètres Système > Général > Stockage. Cela affiche une répartition par code couleur (ex. : Apps, Documents, Données système). Cliquez sur une catégorie pour obtenir des recommandations.[1]
2.  **Optimiser le stockage automatiquement** : Dans les paramètres de Stockage, activez "Optimiser le stockage" pour décharger les données d'applications inutilisées et gérer les pièces jointes. Activez également "Vider la Corbeille automatiquement" après 30 jours.[1]
3.  **Vider la Corbeille et les Téléchargements** : Les Données système incluent le contenu de la Corbeille – videz-la manuellement depuis le Finder. Vérifiez ~/Téléchargements pour les anciens fichiers et supprimez-les.[1][2]
4.  **Gérer les pièces jointes volumineuses** : Allez dans Paramètres de Stockage > Applications > Gérer > Mail > "Optimiser le stockage" pour télécharger les pièces jointes volumineuses des e-mails à la demande.[1]

Pour un nettoyage plus approfondi, utilisez l'onglet "Éléments précédents" dans Stockage pour examiner les sauvegardes récentes (comme les sauvegardes Time Machine) et les supprimer si elles sont inutiles.[2]

### Identifier et vider les fichiers cache amovibles
Les caches sont des fichiers temporaires qui accélèrent les applications mais peuvent accumuler des gigaoctets. Videz en toute sécurité les caches au niveau de l'utilisateur via le Finder ; évitez les caches au niveau du système, sauf indication du support Apple, pour éviter les problèmes. Les caches de votre Mac se trouvent dans les dossiers de la bibliothèque – vérifiez leur taille avec "Lire les informations" du Finder.

1.  **Répertoire cache utilisateur (Le plus sûr à vider)** :
    - Accédez via Finder > Aller > Aller au dossier, tapez `~/Library/Caches`, et appuyez sur Entrée.
    - Ce dossier contient les caches des applications (ex. : navigateurs, applications Office). Sélectionnez tous les dossiers à l'intérieur et supprimez-les. Ils sont généralement sûrs et se régénèrent.
    - Astuce : Vérifiez les sous-dossiers comme `com.apple.*` pour les caches des applications Apple, mais ignorez-les en cas de doute. Videz la Corbeille ensuite.[4][2]

2.  **Caches spécifiques aux applications** :
    - Navigateurs : Dans Safari, effacez l'historique/les caches via le menu Safari > Effacer l'historique. Pour Chrome/les apps Google : Allez dans Chrome > Paramètres > Confidentialité et sécurité > Effacer les données de navigation.
    - Xcode/Développeur : Si vous codez, effacez les données dérivées dans Xcode > Préférences > Locations > Derived Data.
    - Autres applications : Vérifiez les préférences de l'application pour les options de vidage du cache ou utilisez le Finder pour voir les sous-dossiers de `~/Library/Caches`.[2][3]

3.  **Caches système et de la bibliothèque (Procéder avec prudence)** :
    - `/Library/Caches` peut contenir des caches système – ne supprimez que des dossiers spécifiques comme les caches d'applications obsolètes, pas ceux du système central (ex. : évitez `com.apple.coreservices`).
    - Pour analyser les tailles en toute sécurité, utilisez le Terminal pour lister les gros caches : Ouvrez le Terminal et exécutez `du -sh /Library/Caches/* | sort -h`.
    - Dernier recours pour les caches système profonds : Redémarrez en mode Recovery (Commande+R au démarrage) et exécutez Utilitaire de disque > Premiers secours, puis redémarrez et utilisez les outils de Stockage.[2]

### Conseils supplémentaires pour un nettoyage manuel et sûr
-   **Supprimer les fichiers temporaires et les journaux** : Les Données système incluent les journaux dans `/private/var/log`. Utilisez des commandes Terminal comme `sudo rm -rf /private/var/log/asl/*.asl` pour les anciens journaux Apple (déconnectez-vous et reconnectez-vous d'abord). Pour les fichiers temporaires, supprimez ceux de `/tmp` via `sudo rm -rf /tmp/*` après vérification.[2]
-   **Décharger vers un stockage externe** : Déplacez les photos/vidéos vers iCloud ou un disque externe via Paramètres de Stockage > "Stocker dans iCloud".[1]
-   **Applications pour une analyse sûre** : Les outils tiers comme CleanMyMac (de MacPaw) ou OmniDiskSweeper analysent à la recherche des gros caches/fichiers – utilisez-les comme guide, mais sauvegardez toujours d'abord (ex. : via Time Machine).[3]
-   **Surveiller après le nettoyage** : Redémarrez après des suppressions importantes pour actualiser le système. Revérifiez l'utilisation du Stockage ; la suppression des caches régénérables ne devrait pas affecter les performances.[2]

Si les Données système restent élevées (ex. : 218 Go comme dans certains rapports), il peut s'agir de sauvegardes cachées ou de fichiers corrompus – le Support Apple suggère d'exécuter `tmutil thinlocalsnapshots / 10000000000 4` dans le Terminal pour le nettoyage de Time Machine.[5] Assurez-vous d'avoir des sauvegardes avant de procéder. Ces méthodes devraient récupérer un espace significatif sans risques sur les Mac Apple Silicon comme votre M2.[1][2][4]

Citations :
[1] https://support.apple.com/en-us/102624
[2] https://macpaw.com/how-to/clear-system-storage-mac
[3] https://nektony.com/how-to/clean-up-system-storage-on-mac?srsltid=AfmBOorJjQPPX59Jw3MM47n0NZ8DQlerYQAbkZdymj0rUZM0rtLZlw1s
[4] https://www.reddit.com/r/MacOS/comments/154rp99/how_to_do_i_clear_system_data_on_mac_os/
[5] https://discussions.apple.com/thread/255084458