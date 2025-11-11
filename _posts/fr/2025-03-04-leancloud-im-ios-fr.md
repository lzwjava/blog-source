---
audio: false
generated: true
lang: fr
layout: post
title: LeanCloud Realtime SDK iOS
translated: true
type: note
---

Pour utiliser `pod 'AVOSCloudIM', '3.1.6.2'` dans votre projet iOS avec CocoaPods, suivez ces étapes. Cela suppose que vous avez CocoaPods installé et que vous êtes familier avec le développement iOS de base en utilisant Xcode.

---

### Étape 1 : Configurer CocoaPods (si ce n'est pas déjà fait)
Si vous n'avez pas encore installé CocoaPods, installez-le via le terminal :
```bash
sudo gem install cocoapods
```
Vérifiez l'installation :
```bash
pod --version
```

---

### Étape 2 : Créer ou ouvrir votre projet Xcode
1. Ouvrez votre projet Xcode existant ou créez-en un nouveau dans Xcode.
2. Fermez Xcode pour l'instant (nous le rouvrirons plus tard avec l'espace de travail).

---

### Étape 3 : Initialiser un Podfile
1. Ouvrez votre terminal et naviguez vers le répertoire racine de votre projet (où se trouve le fichier `.xcodeproj`) :
   ```bash
   cd /chemin/vers/votre/projet
   ```
2. Si vous n'avez pas déjà de Podfile, créez-en un en exécutant :
   ```bash
   pod init
   ```
   Cela génère un `Podfile` de base dans votre répertoire de projet.

---

### Étape 4 : Modifier le Podfile
1. Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano`, `vim`, ou tout éditeur de code comme VS Code) :
   ```bash
   open Podfile
   ```
2. Modifiez le `Podfile` pour inclure le pod `AVOSCloudIM` avec la version `3.1.6.2`. Voici un exemple de ce à quoi votre `Podfile` pourrait ressembler :
   ```ruby
   platform :ios, '9.0'  # Spécifiez la version iOS minimale (ajustez si nécessaire)
   use_frameworks!       # Optionnel : Utilisez ceci si votre projet utilise Swift ou des frameworks

   target 'NomDeVotreApp' do
     pod 'AVOSCloudIM', '3.1.6.2'  # Ajoutez cette ligne pour inclure AVOSCloudIM version 3.1.6.2
   end
   ```
   - Remplacez `'NomDeVotreApp'` par le nom réel de votre cible Xcode (généralement le nom de votre application).
   - La ligne `platform :ios, '9.0'` spécifie la version iOS minimale ; ajustez-la en fonction des exigences de votre projet.
   - `use_frameworks!` est nécessaire si votre projet utilise Swift ou si le pod nécessite des frameworks dynamiques.

3. Enregistrez et fermez le `Podfile`.

---

### Étape 5 : Installer le Pod
1. Dans le terminal, exécutez la commande suivante depuis le répertoire racine de votre projet :
   ```bash
   pod install
   ```
   - Cela télécharge et intègre la bibliothèque `AVOSCloudIM` (version 3.1.6.2) dans votre projet.
   - Si l'opération réussit, vous verrez une sortie comme :  
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. Si vous rencontrez des erreurs (par exemple, pod introuvable), assurez-vous que la version `3.1.6.2` est toujours disponible dans le dépôt CocoaPods. Les versions plus anciennes pourraient ne plus être prises en charge. Vous pouvez vérifier la dernière version sur [CocoaPods.org](https://cocoapods.org) sous `AVOSCloudIM` ou passer à une version plus récente (par exemple, `pod 'AVOSCloudIM', '~> 12.3'`).

---

### Étape 6 : Ouvrir l'espace de travail
1. Après l'installation, un fichier `.xcworkspace` sera créé dans votre répertoire de projet (par exemple, `NomDeVotreApp.xcworkspace`).
2. Ouvrez ce fichier dans Xcode :
   ```bash
   open NomDeVotreApp.xcworkspace
   ```
   - Désormais, utilisez toujours le fichier `.xcworkspace` au lieu du fichier `.xcodeproj` pour travailler sur votre projet.

---

### Étape 7 : Importer et utiliser AVOSCloudIM dans votre code
1. Dans vos fichiers Swift ou Objective-C, importez le module `AVOSCloudIM` :
   - **Swift** :
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C** :
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. Commencez à utiliser les fonctionnalités de la bibliothèque. `AVOSCloudIM` fait partie du SDK LeanCloud, généralement utilisé pour la messagerie en temps réel. Reportez-vous à la [documentation LeanCloud](https://leancloud.app/docs/) pour des exemples d'utilisation spécifiques, tels que la configuration d'un client de discussion :
   - Exemple (Swift) :
     ```swift
     let client = AVIMClient(clientId: "votreClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connecté à LeanCloud IM!")
         } else {
             print("Erreur : \\(error?.localizedDescription ?? "Inconnue")")
         }
     }
     ```

---

### Étape 8 : Configurer votre projet (si nécessaire)
- **Clé d'application et initialisation** : Les SDK LeanCloud nécessitent souvent un ID d'application et une clé. Ajoutez ce code d'initialisation (par exemple, dans `AppDelegate`) :
  - **Swift** :
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("votreAppID", clientKey: "votreAppKey")
        return true
    }
    ```
  - Remplacez `"votreAppID"` et `"votreAppKey"` par les identifiants de votre compte LeanCloud.
- **Autorisations** : Assurez-vous que votre application dispose des autorisations nécessaires (par exemple, l'accès à Internet) dans `Info.plist` :
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### Notes
- **Spécificité de la version** : L'utilisation de `pod 'AVOSCloudIM', '3.1.6.2'` vous verrouille à cette version exacte. Si vous voulez de la flexibilité pour les mises à jour mineures, utilisez `~>` (par exemple, `pod 'AVOSCloudIM', '~> 3.1.6'` autorise les mises à jour comme 3.1.6.1 mais pas 3.2).
- **Dépannage** : Si `pod install` échoue, essayez :
  - Mettre à jour CocoaPods : `sudo gem install cocoapods`
  - Effacer le cache : `pod cache clean --all`
  - Exécuter `pod repo update` pour actualiser le dépôt spec local de CocoaPods.
- **SDK LeanCloud** : Étant donné qu'`AVOSCloudIM` fait partie de LeanCloud, assurez-vous de suivre leur guide de configuration pour toute configuration supplémentaire (par exemple, l'inscription sur leur plateforme).

---

C'est tout ! Vous avez maintenant intégré `AVOSCloudIM` version 3.1.6.2 dans votre projet iOS. Compilez et exécutez votre application dans Xcode pour la tester. Faites-moi savoir si vous avez besoin d'aide avec des fonctionnalités spécifiques de LeanCloud !