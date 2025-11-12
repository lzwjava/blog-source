---
audio: false
generated: true
lang: fr
layout: post
title: Application Console
translated: true
type: note
---

Pour résoudre l'erreur « Failed to open input stream in demuxing stream » dans Infuse, une application Mac, et consulter des journaux plus détaillés, vous pouvez utiliser des outils disponibles sur votre Mac. La requête mentionne un « outil iOS ou Xcode », mais comme elle spécifie Infuse comme une application Mac, il est probable que vous souhaitiez utiliser Xcode ou des outils macOS associés pour inspecter les journaux de la version Mac d'Infuse. Voici des instructions étape par étape pour vous aider à accéder à ces journaux.

### Pour Infuse sur Mac (Méthode principale : Application Console)
Étant donné qu'Infuse est identifiée comme une application Mac dans votre requête, le moyen le plus direct de consulter ses journaux est d'utiliser l'application **Console**, qui est intégrée à macOS et conçue pour afficher les journaux système et des applications.

1. **Ouvrir l'application Console** :
   - Lancez l'application **Console**, située dans **Applications** > **Utilitaires** > **Console**, ou recherchez-la via Spotlight (Cmd + Espace, puis tapez "Console").

2. **Filtrer les journaux pour Infuse** :
   - Dans l'application Console, utilisez la barre de recherche en haut à droite.
   - Tapez "Infuse" ou le nom du processus de l'application (probablement "Infuse" ou similaire) pour filtrer les journaux liés à l'application.

3. **Reproduire l'erreur** :
   - Avec l'application Console ouverte et le filtre actif, lisez la vidéo dans Infuse qui déclenche l'erreur « Failed to open input stream in demuxing stream ».
   - Cela garantit que les journaux pertinents sont capturés en temps réel.

4. **Analyser les journaux** :
   - Recherchez les messages d'erreur, les avertissements ou les sorties détaillées qui pourraient expliquer pourquoi le flux d'entrée n'a pas pu être ouvert pendant le demuxing (le processus de séparation des flux audio et vidéo).
   - Des mots-clés comme "error", "fail" ou "demux" peuvent aider à identifier le problème.

### Si vous faisiez référence à la version iOS d'Infuse (Utilisation de Xcode)
Si vous souhaitiez déboguer la version iOS d'Infuse (malgré la requête indiquant "application Mac"), vous pouvez utiliser **Xcode**, l'outil de développement d'Apple, pour accéder aux journaux d'un appareil iOS. Voici comment :

1. **Connecter votre appareil iOS** :
   - Branchez votre iPhone ou iPad à votre Mac à l'aide d'un câble USB.

2. **Ouvrir Xcode** :
   - Lancez **Xcode** sur votre Mac. Si vous ne l'avez pas installé, téléchargez-le depuis le Mac App Store.

3. **Accéder aux Périphériques et Simulateurs** :
   - Dans Xcode, allez dans **Window** > **Devices and Simulators** depuis la barre de menu.

4. **Sélectionner votre appareil** :
   - Dans la fenêtre qui s'ouvre, trouvez votre appareil iOS connecté dans la barre latérale de gauche et cliquez dessus.

5. **Voir les journaux** :
   - Cliquez sur **Open Console** ou **View Device Logs** (l'option peut varier selon la version de Xcode).
   - Cela ouvre une visionneuse de journaux affichant toute l'activité de votre appareil.

6. **Filtrer pour Infuse** :
   - Utilisez l'option de recherche ou de filtre dans la visionneuse de journaux pour affiner les entrées en tapant "Infuse" ou l'identifiant du bundle de l'application (par exemple, `com.firecore.Infuse` s'il est connu).
   - Reproduisez l'erreur sur votre appareil iOS pendant que la console est ouverte pour capturer les journaux pertinents.

### Options supplémentaires
- **Vérifier les rapports de plantage** :
  - **Mac** : Si Infuse plante, vérifiez `~/Library/Logs/DiagnosticReports` ou `/Library/Logs/DiagnosticReports` pour les journaux de plantage nommés avec "Infuse" et un horodatage.
  - **iOS** : Dans la fenêtre **Devices and Simulators** de Xcode, les journaux de plantage pour Infuse peuvent apparaître dans les journaux de votre appareil.

- **Activer la journalisation de débogage dans Infuse** :
  - Certaines applications, y compris Infuse, peuvent offrir un mode débogage ou une option de journalisation verbeuse. Ouvrez les paramètres ou préférences d'Infuse sur votre Mac (ou appareil iOS) pour voir si une telle fonctionnalité existe. Si elle est activée, cela pourrait générer des journaux plus détaillés consultables via les méthodes ci-dessus.

- **Alternative pour iOS (Application Console)** :
  - Connectez votre appareil iOS à votre Mac, ouvrez l'application **Console**, et sélectionnez votre appareil dans la barre latérale de gauche. Filtrez les journaux par "Infuse" pour voir la sortie en temps réel sans avoir besoin de Xcode.

### Notes
- L'erreur « Failed to open input stream in demuxing stream » suggère un problème avec le fichier média ou le flux réseau qu'Infuse tente de traiter. Les journaux pourraient révéler s'il s'agit d'une corruption de fichier, d'une incompatibilité de codec ou d'un problème de connexion.
- Comme Infuse est une application tierce, le débogage avancé (par exemple, attacher Xcode au processus) est improbable sans un accès développeur, donc l'application Console (pour Mac) ou les journaux de l'appareil (pour iOS) sont vos meilleures options.

En suivant ces étapes, vous serez en mesure de collecter plus de journaux pour diagnostiquer l'erreur dans Infuse, que ce soit sur Mac ou iOS. Si le problème persiste, envisagez de consulter la documentation d'assistance ou les forums d'Infuse pour des conseils de journalisation spécifiques à l'application.