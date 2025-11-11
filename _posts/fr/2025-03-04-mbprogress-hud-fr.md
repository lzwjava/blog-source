---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de MBProgressHUD sous iOS
translated: true
type: note
---

Il semble que vous demandiez comment utiliser la bibliothèque `MBProgressHUD` dans un projet iOS, spécifiquement la version `0.9.1`, via un Podfile dans CocoaPods. Laissez-moi vous guider à travers le processus étape par étape.

### Qu'est-ce que MBProgressHUD ?
`MBProgressHUD` est une bibliothèque tierce populaire pour iOS qui fournit un moyen simple d'afficher un HUD (Heads-Up Display) avec des indicateurs d'activité, des barres de progression ou des vues personnalisées, généralement utilisé pour afficher des états de chargement ou des messages brefs.

### Étapes pour utiliser `pod 'MBProgressHUD', '0.9.1'`

#### 1. **Installer CocoaPods (si ce n'est pas déjà fait)**
CocoaPods est un gestionnaire de dépendances pour les projets iOS. Si vous ne l'avez pas installé, exécutez cette commande dans votre terminal :
```bash
sudo gem install cocoapods
```

#### 2. **Configurer un Podfile**
- Naviguez vers le répertoire de votre projet Xcode dans le terminal :
  ```bash
  cd /chemin/vers/votre/projet
  ```
- Si vous n'avez pas déjà de Podfile, créez-en un en exécutant :
  ```bash
  pod init
  ```
- Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano Podfile` ou `open Podfile`).

#### 3. **Ajouter MBProgressHUD à votre Podfile**
Dans votre `Podfile`, ajoutez la ligne pour `MBProgressHUD` version `0.9.1` à l'intérieur du bloc target pour votre application. Cela devrait ressembler à ceci :
```ruby
platform :ios, '9.0'  # Spécifiez votre cible de déploiement

target 'NomDeVotreApp' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Remplacez `'NomDeVotreApp'` par le nom réel de votre cible Xcode.
- La ligne `platform :ios, '9.0'` définit la version iOS minimale ; ajustez-la en fonction des besoins de votre projet.

#### 4. **Installer le Pod**
- Sauvegardez le `Podfile` et exécutez cette commande dans le terminal :
  ```bash
  pod install
  ```
- Cela télécharge et intègre `MBProgressHUD` version `0.9.1` dans votre projet. Si l'opération réussit, vous verrez une sortie confirmant l'installation.

#### 5. **Ouvrir l'espace de travail (Workspace)**
- Après l'installation, fermez votre projet Xcode (s'il est ouvert) et ouvrez le fichier `.xcworkspace` nouvellement créé (par exemple, `NomDeVotreApp.xcworkspace`) au lieu du fichier `.xcodeproj`. CocoaPods génère cet espace de travail pour gérer les dépendances.

#### 6. **Utiliser MBProgressHUD dans votre code**
- **Swift** : Importez le module et utilisez-le dans votre code :
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // Afficher un HUD simple avec un indicateur de chargement
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Chargement..."
          
          // Le masquer après un certain temps (par exemple, 2 secondes)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C** : Importez l'en-tête et utilisez-le :
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // Afficher un HUD simple avec un indicateur de chargement
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Chargement...";
      
      // Le masquer après un certain temps (par exemple, 2 secondes)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Fonctionnalités courantes de MBProgressHUD**
- **HUD de base** : Comme montré ci-dessus, affichez un indicateur de rotation avec un texte optionnel.
- **Texte personnalisé uniquement** :
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Terminé !"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **Barre de progression** :
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // Progression à 50%
  ```

#### Notes
- **Version 0.9.1** : Il s'agit d'une ancienne version (publiée vers 2015). La dernière version en date de Mars 2025 est bien plus récente (par exemple, 1.2.0 ou supérieure). Pour utiliser la dernière version, écrivez simplement `pod 'MBProgressHUD'` sans numéro de version. Envisagez de mettre à jour sauf si vous avez spécifiquement besoin de la version 0.9.1 pour des raisons de compatibilité.
- **Documentation** : Consultez la [page GitHub de MBProgressHUD](https://github.com/jdg/MBProgressHUD) pour plus d'options et d'exemples. La version 0.9.1 pourrait avoir moins de fonctionnalités que les versions modernes.

N'hésitez pas à me demander si vous avez besoin d'aide pour résoudre un problème ou pour des exemples plus spécifiques !