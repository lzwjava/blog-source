---
audio: false
generated: true
lang: fr
layout: post
title: Kit de développement LeanCloud pour iOS
translated: true
type: note
---

Pour utiliser `pod 'AVOSCloud', '3.1.6.2'` dans un projet iOS, vous faites référence à l'intégration du SDK AVOSCloud (probablement le SDK LeanCloud pour les services cloud) via CocoaPods, un gestionnaire de dépendances pour les projets iOS. Voici un guide étape par étape pour le configurer :

---

### Prérequis
1. **Installer CocoaPods** : Si vous n'avez pas CocoaPods d'installé, installez-le d'abord en exécutant cette commande dans votre terminal :
   ```bash
   sudo gem install cocoapods
   ```
2. **Projet Xcode** : Assurez-vous d'avoir un projet iOS existant dans Xcode.

---

### Étapes pour utiliser `pod 'AVOSCloud', '3.1.6.2'`

1. **Naviguer vers le répertoire de votre projet** :
   Ouvrez votre terminal et allez dans le répertoire contenant votre fichier `.xcodeproj` :
   ```bash
   cd /chemin/vers/votre/projet
   ```

2. **Initialiser un Podfile** (si vous n'en avez pas déjà un) :
   Exécutez la commande suivante pour créer un `Podfile` :
   ```bash
   pod init
   ```

3. **Modifier le Podfile** :
   Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano Podfile` ou `open Podfile`) et ajoutez le pod `AVOSCloud` avec la version spécifique `3.1.6.2`. Votre `Podfile` devrait ressembler à ceci :
   ```ruby
   platform :ios, '9.0'  # Spécifiez la version iOS minimale (ajustez si nécessaire)

   target 'NomDeVotreApp' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # Ajoutez cette ligne pour le SDK AVOSCloud
   end
   ```
   - Remplacez `'NomDeVotreApp'` par le nom réel de votre cible Xcode.
   - `use_frameworks!` est requis si vous utilisez Swift ou des frameworks dynamiques.

4. **Installer le Pod** :
   Sauvegardez le `Podfile`, puis exécutez cette commande dans le terminal pour installer la version spécifiée d'AVOSCloud :
   ```bash
   pod install
   ```
   - Cela téléchargera la version `3.1.6.2` du SDK AVOSCloud et configurera votre projet avec un fichier `.xcworkspace`.

5. **Ouvrir l'espace de travail (Workspace)** :
   Après l'installation, fermez votre `.xcodeproj` s'il est ouvert, et ouvrez le nouveau fichier `.xcworkspace` créé :
   ```bash
   open NomDeVotreApp.xcworkspace
   ```

6. **Importer et utiliser AVOSCloud dans votre code** :
   - En Objective-C :
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)exemple {
         [AVOSCloud setApplicationId:@"votre_app_id" clientKey:@"votre_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Bonjour" forKey:@"message"];
         [testObject save];
     }
     ```
   - En Swift :
     ```swift
     import AVOSCloud

     func exemple() {
         AVOSCloud.setApplicationId("votre_app_id", clientKey: "votre_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Bonjour"
         try? testObject.save()
     }
     ```
   - Remplacez `"votre_app_id"` et `"votre_client_key"` par les identifiants de votre application LeanCloud obtenus depuis leur tableau de bord.

7. **Configurer les identifiants de l'application** :
   - Inscrivez-vous sur [LeanCloud](https://leancloud.app) (ou le fournisseur de service AVOSCloud pertinent).
   - Récupérez votre `App ID` et votre `Client Key` dans les paramètres de votre application et définissez-les dans votre code (comme montré ci-dessus).

8. **Compiler et exécuter** :
   Compilez votre projet dans Xcode (`Cmd + B`) pour vous assurer que tout est configuré correctement. S'il y a des erreurs, vérifiez la syntaxe de votre Podfile ou votre connexion réseau.

---

### Notes
- **Version spécifique** : En spécifiant `'3.1.6.2'`, vous verrouillez le SDK à cette version exacte. Celle-ci pourrait être obsolète au 03 mars 2025. Pour utiliser la dernière version, écrivez simplement `pod 'AVOSCloud'` sans numéro de version.
- **Compatibilité** : Assurez-vous que la version `3.1.6.2` supporte votre cible de déploiement iOS (par exemple, iOS 9.0 ou supérieur). Consultez la [documentation LeanCloud](https://leancloud.app/docs) pour plus de détails.
- **Mise à jour de Pod** : Si vous devez mettre à jour CocoaPods ou résoudre un problème, exécutez :
  ```bash
  pod update
  ```
- **Dépannage** : Si `pod install` échoue, essayez :
  ```bash
  pod repo update
  pod install --verbose
  ```

---

Faites-moi savoir si vous avez besoin d'aide pour une partie spécifique, comme l'intégration d'une fonctionnalité (par exemple, les notifications push, la messagerie en temps réel) d'AVOSCloud !