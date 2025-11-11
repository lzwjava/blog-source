---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de PopMenu dans iOS
translated: true
type: note
---

Pour utiliser `pod 'PopMenu', '2.4'` dans votre projet iOS, vous intégrez la bibliothèque PopMenu (version 2.4) via CocoaPods, un gestionnaire de dépendances populaire pour iOS. Cette bibliothèque fournit un menu animé contextuel inspiré par des applications comme Sina Weibo ou NetEase. Voici les étapes pour la configurer et l'utiliser dans votre projet :

---

### Étape 1 : Installer CocoaPods (si ce n'est pas déjà fait)
Si vous n'avez pas CocoaPods installé sur votre système, installez-le d'abord :
1. Ouvrez votre terminal.
2. Exécutez cette commande :
   ```bash
   sudo gem install cocoapods
   ```
3. Vérifiez l'installation :
   ```bash
   pod --version
   ```

---

### Étape 2 : Configurer votre Podfile
1. Accédez au répertoire de votre projet Xcode dans le terminal :
   ```bash
   cd /chemin/vers/votre/projet
   ```
2. Si vous n'avez pas déjà de Podfile, créez-en un en exécutant :
   ```bash
   pod init
   ```
3. Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano Podfile` ou utilisez Xcode).
4. Ajoutez les lignes suivantes pour spécifier le pod PopMenu pour votre cible :
   ```ruby
   platform :ios, '8.0'  # Ajustez la version iOS si nécessaire
   target 'NomDeVotreApp' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - Remplacez `NomDeVotreApp` par le nom de votre cible Xcode.
   - La ligne `use_frameworks!` est nécessaire car PopMenu est probablement une bibliothèque basée sur des frameworks.

5. Enregistrez et fermez le Podfile.

---

### Étape 3 : Installer le Pod
1. Dans le terminal, exécutez :
   ```bash
   pod install
   ```
2. Cela télécharge et intègre PopMenu version 2.4 dans votre projet. Attendez jusqu'à voir un message comme :
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. Fermez votre projet Xcode s'il est ouvert, puis ouvrez le fichier `.xcworkspace` nouvellement généré (par exemple, `NomDeVotreApp.xcworkspace`) au lieu du fichier `.xcodeproj`.

---

### Étape 4 : Utilisation de base dans votre code
PopMenu est écrit en Objective-C, vous devrez donc l'utiliser en conséquence. Voici un exemple de mise en œuvre dans votre application :

1. **Importer la bibliothèque** :
   - Dans votre fichier Objective-C (par exemple, `ViewController.m`) :
     ```objective-c
     #import "PopMenu.h"
     ```
   - Si vous utilisez Swift, créez un bridging header :
     - Allez dans `File > New > File > Header File` (par exemple, `NomDeVotreApp-Bridging-Header.h`).
     - Ajoutez :
       ```objective-c
       #import "PopMenu.h"
       ```
     - Dans Xcode, définissez le bridging header sous `Build Settings > Swift Compiler - General > Objective-C Bridging Header` sur le chemin de votre fichier d'en-tête (par exemple, `NomDeVotreApp/NomDeVotreApp-Bridging-Header.h`).

2. **Créer les éléments du menu** :
   Définissez les éléments que vous voulez dans le menu contextuel. Chaque élément peut avoir un titre, une icône et une couleur de lueur.
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];
   
   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr" 
                                               iconName:@"post_type_bubble_flickr" 
                                              glowColor:[UIColor grayColor] 
                                                  index:0];
   [items addObject:menuItem1];
   
   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter" 
                                               iconName:@"post_type_bubble_twitter" 
                                              glowColor:[UIColor blueColor] 
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **Initialiser et afficher le menu** :
   Créez une instance `PopMenu` et affichez-la dans votre vue.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // Options : kPopMenuAnimationTypeSina ou kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // Nombre d'éléments par ligne
   [popMenu showMenuAtView:self.view];
   ```

4. **Gérer la sélection (Optionnel)** :
   Vous pouvez sous-classer ou étendre la fonctionnalité pour détecter les taps, bien que la version de base de PopMenu (circa 2.4) ne prenne peut-être pas en charge nativement un délégué. Vérifiez la documentation de la bibliothèque sur GitHub (`xhzengAIB/PopMenu`) pour toute mise à jour ou personnalisation.

---

### Étape 5 : Exécuter votre projet
Compilez et exécutez votre projet (`Cmd + R`) dans Xcode. Si les icônes (par exemple, `post_type_bubble_flickr`) font partie de votre catalogue d'assets, assurez-vous qu'elles sont ajoutées à votre projet. Sinon, vous devrez les sourcer ou les créer.

---

### Notes
- **Spécificité de version** : `pod 'PopMenu', '2.4'` vous verrouille sur la version 2.4. Si vous voulez la dernière version, utilisez `pod 'PopMenu'` sans numéro de version, mais cela pourrait introduire des changements cassants.
- **Compatibilité** : Assurez-vous que la cible de déploiement de votre projet est au moins iOS 8.0 (ou ajustez la `platform` dans le Podfile).
- **Personnalisation** : PopMenu permet des ajustements du type d'animation et de la mise en page (par exemple, `perRowItemCount`). Explorez le code source pour plus d'options.
- **Dépannage** : Si vous rencontrez des erreurs comme "file not found", assurez-vous que vos Pods sont correctement installés et que votre workspace est utilisé.

Cela devrait vous permettre de démarrer avec PopMenu 2.4 dans votre application iOS ! Faites-moi savoir si vous avez besoin de précisions supplémentaires.