---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser PopMenu dans iOS
translated: true
---

Pour utiliser `pod 'PopMenu', '2.4'` dans votre projet iOS, vous intégrez la bibliothèque PopMenu (version 2.4) via CocoaPods, un gestionnaire de dépendances populaire pour iOS. Cette bibliothèque fournit un menu à animation pop-up inspiré d'applications comme Sina Weibo ou NetEase. Voici les étapes pour la configurer et l'utiliser dans votre projet :

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
   cd /path/to/your/project
   ```
2. Si vous n'avez pas encore de Podfile, créez-en un en exécutant :
   ```bash
   pod init
   ```
3. Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano Podfile` ou utilisez Xcode).
4. Ajoutez les lignes suivantes pour spécifier le pod PopMenu pour votre cible :
   ```ruby
   platform :ios, '8.0'  # Ajustez la version iOS si nécessaire
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - Remplacez `YourAppName` par le nom de votre cible Xcode.
   - La ligne `use_frameworks!` est requise puisque PopMenu est probablement une bibliothèque basée sur des frameworks.

5. Enregistrez et fermez le Podfile.

---

### Étape 3 : Installer le Pod
1. Dans le terminal, exécutez :
   ```bash
   pod install
   ```
2. Cela télécharge et intègre PopMenu version 2.4 dans votre projet. Attendez jusqu'à ce que vous voyiez un message comme :
   ```
   Installation des pods terminée ! Il y a X dépendances du Podfile et X pods installés au total.
   ```
3. Fermez votre projet Xcode s'il est ouvert, puis ouvrez le fichier `.xcworkspace` nouvellement généré (par exemple, `YourAppName.xcworkspace`) au lieu du fichier `.xcodeproj`.

---

### Étape 4 : Utilisation de base dans votre code
PopMenu est écrit en Objective-C, vous devrez donc l'utiliser en conséquence. Voici un exemple de la manière de l'implémenter dans votre application :

1. **Importer la bibliothèque** :
   - Dans votre fichier Objective-C (par exemple, `ViewController.m`) :
     ```objective-c
     #import "PopMenu.h"
     ```
   - Si vous utilisez Swift, créez un header de pontage :
     - Allez dans `File > New > File > Header File` (par exemple, `YourAppName-Bridging-Header.h`).
     - Ajoutez :
       ```objective-c
       #import "PopMenu.h"
       ```
     - Dans Xcode, définissez le header de pontage sous `Build Settings > Swift Compiler - General > Objective-C Bridging Header` au chemin de votre fichier header (par exemple, `YourAppName/YourAppName-Bridging-Header.h`).

2. **Créer des éléments de menu** :
   Définissez les éléments que vous souhaitez dans le menu pop-up. Chaque élément peut avoir un titre, une icône et une couleur de halo.
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
   Créez une instance de `PopMenu` et affichez-la dans votre vue.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // Options : kPopMenuAnimationTypeSina ou kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // Nombre d'éléments par ligne
   [popMenu showMenuAtView:self.view];
   ```

4. **Gérer la sélection (optionnel)** :
   Vous pouvez sous-classer ou étendre la fonctionnalité pour détecter les taps, bien que la version de base de PopMenu (circa 2.4) ne supporte peut-être pas un délégué de manière native. Vérifiez la documentation de la bibliothèque sur GitHub (`xhzengAIB/PopMenu`) pour toute mise à jour ou personnalisation.

---

### Étape 5 : Exécuter votre projet
Construisez et exécutez votre projet (`Cmd + R`) dans Xcode. Si les icônes (par exemple, `post_type_bubble_flickr`) font partie de votre catalogue d'assets, assurez-vous qu'elles sont ajoutées à votre projet. Sinon, vous devrez les obtenir ou les créer.

---

### Notes
- **Spécificité de la version** : `pod 'PopMenu', '2.4'` vous verrouille à la version 2.4. Si vous souhaitez la dernière version, utilisez `pod 'PopMenu'` sans numéro de version, mais cela pourrait introduire des changements cassants.
- **Compatibilité** : Assurez-vous que la cible de déploiement de votre projet est au moins iOS 8.0 (ou ajustez la `platform` dans le Podfile).
- **Personnalisation** : PopMenu permet des ajustements de type d'animation et de mise en page (par exemple, `perRowItemCount`). Explorez le code source pour plus d'options.
- **Dépannage** : Si vous rencontrez des erreurs comme « fichier non trouvé », assurez-vous que vos Pods sont correctement installés et que votre espace de travail est en cours d'utilisation.

Cela devrait vous permettre de démarrer avec PopMenu 2.4 dans votre application iOS ! Faites-le moi savoir si vous avez besoin de plus de clarifications.