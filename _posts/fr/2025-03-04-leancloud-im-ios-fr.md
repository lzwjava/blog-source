---
audio: false
generated: true
lang: fr
layout: post
title: LeanCloud Realtime iOS SDK
translated: true
---

Pour utiliser `pod 'AVOSCloudIM', '3.1.6.2'` dans votre projet iOS avec CocoaPods, suivez ces étapes. Cela suppose que vous avez installé CocoaPods et que vous êtes familier avec le développement iOS de base en utilisant Xcode.

---

### Étape 1 : Configurer CocoaPods (si ce n'est pas déjà fait)
Si vous n’avez pas encore installé CocoaPods, installez-le via le terminal :
```bash
sudo gem install cocoapods
```
Vérifiez l’installation :
```bash
pod --version
```

---

### Étape 2 : Créer ou ouvrir votre projet Xcode
1. Ouvrez votre projet Xcode existant ou créez-en un nouveau dans Xcode.
2. Fermez Xcode pour l’instant (nous le rouvrirons plus tard avec l’espace de travail).

---

### Étape 3 : Initialiser un Podfile
1. Ouvrez votre terminal et accédez au répertoire racine de votre projet (là où se trouve le fichier `.xcodeproj`):
   ```bash
   cd /path/to/your/project
   ```
2. Si vous n’avez pas encore de Podfile, créez-en un en exécutant :
   ```bash
   pod init
   ```
   Cela génère un `Podfile` de base dans votre répertoire de projet.

---

### Étape 4 : Modifier le Podfile
1. Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano`, `vim`, ou tout éditeur de code comme VS Code) :
   ```bash
   open Podfile
   ```
2. Modifiez le `Podfile` pour inclure le pod `AVOSCloudIM` avec la version `3.1.6.2`. Voici un exemple de ce à quoi pourrait ressembler votre `Podfile` :
   ```ruby
   platform :ios, '9.0'  # Spécifiez la version iOS minimale (ajustez selon les besoins)
   use_frameworks!       # Optionnel : Utilisez ceci si votre projet utilise Swift ou des frameworks

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # Ajoutez cette ligne pour inclure AVOSCloudIM version 3.1.6.2
   end
   ```
   - Remplacez `'YourAppName'` par le nom réel de votre cible Xcode (généralement le nom de votre application).
   - La ligne `platform :ios, '9.0'` spécifie la version iOS minimale ; ajustez-la en fonction des exigences de votre projet.
   - `use_frameworks!` est nécessaire si votre projet utilise Swift ou si le pod nécessite des frameworks dynamiques.

3. Enregistrez et fermez le `Podfile`.

---

### Étape 5 : Installer le Pod
1. Dans le terminal, exécutez la commande suivante à partir du répertoire racine de votre projet :
   ```bash
   pod install
   ```
   - Cela télécharge et intègre la bibliothèque `AVOSCloudIM` (version 3.1.6.2) dans votre projet.
   - Si l’opération est réussie, vous verrez un message comme :
     ```
     Installation des pods terminée ! Il y a X dépendances à partir du Podfile et X pods installés au total.
     ```

2. Si vous rencontrez des erreurs (par exemple, pod non trouvé), assurez-vous que la version `3.1.6.2` est toujours disponible dans le dépôt CocoaPods. Les anciennes versions peuvent ne plus être prises en charge. Vous pouvez vérifier la dernière version sur [CocoaPods.org](https://cocoapods.org) sous `AVOSCloudIM` ou mettre à jour vers une version plus récente (par exemple, `pod 'AVOSCloudIM', '~> 12.3'`).

---

### Étape 6 : Ouvrir l’espace de travail
1. Après l’installation, un fichier `.xcworkspace` sera créé dans votre répertoire de projet (par exemple, `YourAppName.xcworkspace`).
2. Ouvrez ce fichier dans Xcode :
   ```bash
   open YourAppName.xcworkspace
   ```
   - À partir de maintenant, utilisez toujours le fichier `.xcworkspace` au lieu du fichier `.xcodeproj` pour travailler avec votre projet.

---

### Étape 7 : Importer et utiliser AVOSCloudIM dans votre code
1. Dans vos fichiers Swift ou Objective-C, importez le module `AVOSCloudIM` :
   - **Swift** :
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C** :
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. Commencez à utiliser les fonctionnalités de la bibliothèque. `AVOSCloudIM` fait partie du SDK LeanCloud, généralement utilisé pour la messagerie en temps réel. Référez-vous à la [documentation LeanCloud](https://leancloud.app/docs/) pour des exemples d’utilisation spécifiques, comme la configuration d’un client de chat :
   - Exemple (Swift) :
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connecté à LeanCloud IM !")
         } else {
             print("Erreur : \(error?.localizedDescription ?? "Inconnu")")
         }
     }
     ```

---

### Étape 8 : Configurer votre projet (si nécessaire)
- **Clé de l'application et initialisation** : Les SDK LeanCloud nécessitent souvent un ID d'application et une clé. Ajoutez ce code d’initialisation (par exemple, dans `AppDelegate` ):
  - **Swift** :
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - Remplacez `"yourAppID"` et `"yourAppKey"` par les identifiants de votre compte LeanCloud.
- **Autorisations** : Assurez-vous que votre application dispose des autorisations nécessaires (par exemple, accès à Internet) dans `Info.plist` :
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### Notes
- **Spécificité de la version** : L’utilisation de `pod 'AVOSCloudIM', '3.1.6.2'` vous verrouille à cette version exacte. Si vous souhaitez de la flexibilité pour les mises à jour mineures, utilisez `~>` (par exemple, `pod 'AVOSCloudIM', '~> 3.1.6'` permet les mises à jour comme 3.1.6.1 mais pas 3.2).
- **Dépannage** : Si `pod install` échoue, essayez :
  - Mettre à jour CocoaPods : `sudo gem install cocoapods`
  - Effacer le cache : `pod cache clean --all`
  - Exécuter `pod repo update` pour actualiser le dépôt de spécifications CocoaPods local.
- **SDK LeanCloud** : Comme `AVOSCloudIM` fait partie de LeanCloud, assurez-vous de suivre leur guide de configuration pour une configuration supplémentaire (par exemple, l’enregistrement sur leur plateforme).

---

C’est tout ! Vous avez maintenant intégré `AVOSCloudIM` version 3.1.6.2 dans votre projet iOS. Construisez et exécutez votre application dans Xcode pour la tester. Faites-moi savoir si vous avez besoin d’aide pour des fonctionnalités spécifiques de LeanCloud !