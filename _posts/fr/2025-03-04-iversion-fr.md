---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de iVersion dans iOS
translated: true
---

Pour utiliser le pod `iVersion` dans votre projet iOS, vous devez suivre ces étapes :

1. **Ouvrez votre projet dans Xcode** : Assurez-vous que votre projet Xcode est ouvert là où vous souhaitez ajouter le pod `iVersion`.

2. **Initialisez CocoaPods** : Si vous n'avez pas encore initialisé CocoaPods dans votre projet, ouvrez le Terminal, naviguez jusqu'à votre répertoire de projet et exécutez :
   ```bash
   pod init
   ```
   Cela créera un fichier `Podfile` dans votre répertoire de projet.

3. **Éditez le Podfile** : Ouvrez le `Podfile` dans un éditeur de texte ou Xcode. Ajoutez le pod `iVersion` à votre `Podfile` en incluant la ligne suivante dans la section cible :
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Installez le Pod** : Enregistrez le `Podfile` et retournez au Terminal. Exécutez la commande suivante pour installer le pod `iVersion` :
   ```bash
   pod install
   ```

5. **Ouvrez le fichier `.xcworkspace`** : Une fois l'installation terminée, fermez votre projet Xcode s'il est ouvert, puis ouvrez le fichier `.xcworkspace` nouvellement créé. Ce fichier se trouve généralement dans le même répertoire que votre fichier `.xcodeproj` d'origine.

6. **Importez iVersion** : Dans vos fichiers Swift ou Objective-C, importez le module `iVersion` pour commencer à l'utiliser :
   ```swift
   import iVersion
   ```

7. **Utilisez iVersion dans votre code** : Vous pouvez maintenant utiliser la bibliothèque `iVersion` dans votre projet. Par exemple, vous pouvez vérifier la version de l'application ou le numéro de build en utilisant les méthodes fournies par `iVersion`.

En suivant ces étapes, vous devriez pouvoir intégrer et utiliser le pod `iVersion` dans votre projet iOS.