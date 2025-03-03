---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de MBProgressHUD dans iOS
translated: true
---

On dirait que vous demandez comment utiliser la bibliothèque `MBProgressHUD` dans un projet iOS, spécifiquement la version `0.9.1`, via un Podfile dans CocoaPods. Laissez-moi vous guider à travers le processus étape par étape.

### Qu'est-ce que MBProgressHUD ?
`MBProgressHUD` est une bibliothèque tierce populaire pour iOS qui fournit un moyen facile d'afficher un HUD (Heads-Up Display) avec des indicateurs d'activité, des barres de progression ou des vues personnalisées, généralement utilisées pour montrer des états de chargement ou des messages brefs.

### Étapes pour utiliser `pod 'MBProgressHUD', '0.9.1'`

#### 1. **Installer CocoaPods (si ce n'est pas déjà installé)**
CocoaPods est un gestionnaire de dépendances pour les projets iOS. Si vous ne l'avez pas installé, exécutez cette commande dans votre terminal :
```bash
sudo gem install cocoapods
```

#### 2. **Configurer un Podfile**
- Accédez au répertoire de votre projet Xcode dans le terminal :
  ```bash
  cd /path/to/your/project
  ```
- Si vous n'avez pas encore de Podfile, créez-en un en exécutant :
  ```bash
  pod init
  ```
- Ouvrez le `Podfile` dans un éditeur de texte (par exemple, `nano Podfile` ou `open Podfile`).

#### 3. **Ajouter MBProgressHUD à votre Podfile**
Dans votre `Podfile`, ajoutez la ligne pour `MBProgressHUD` version `0.9.1` dans le bloc cible pour votre application. Cela devrait ressembler à ceci :
```ruby
platform :ios, '9.0'  # Spécifiez votre cible de déploiement

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Remplacez `'YourAppName'` par le nom réel de votre cible Xcode.
- La ligne `platform :ios, '9.0'` définit la version iOS minimale ; ajustez-la en fonction des besoins de votre projet.

#### 4. **Installer le Pod**
- Enregistrez le `Podfile` et exécutez cette commande dans le terminal :
  ```bash
  pod install
  ```
- Cela télécharge et intègre `MBProgressHUD` version `0.9.1` dans votre projet. Si l'installation est réussie, vous verrez une sortie confirmant l'installation.

#### 5. **Ouvrir l'espace de travail**
- Après l'installation, fermez votre projet Xcode (s'il est ouvert) et ouvrez le fichier `.xcworkspace` nouvellement créé (par exemple, `YourAppName.xcworkspace`) au lieu du fichier `.xcodeproj`. CocoaPods génère cet espace de travail pour gérer les dépendances.

#### 6. **Utiliser MBProgressHUD dans votre code**
- **Swift** : Importez le module et utilisez-le dans votre code :
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // Afficher un HUD simple avec un indicateur de chargement
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Chargement..."

          // Masquez-le après un certain temps (par exemple, 2 secondes)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C** : Importez l'en-tête et utilisez-le :
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

      // Masquez-le après un certain temps (par exemple, 2 secondes)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Fonctionnalités courantes de MBProgressHUD**
- **HUD de base** : Comme montré ci-dessus, afficher un indicateur de rotation avec du texte optionnel.
- **Texte personnalisé uniquement** :
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Terminé !"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **Barre de progression** :
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50 % de progression
  ```

#### Notes
- **Version 0.9.1** : Il s'agit d'une version plus ancienne (publiée vers 2015). La dernière version à partir de mars 2025 est beaucoup plus récente (par exemple, 1.2.0 ou supérieure). Pour utiliser la dernière, écrivez simplement `pod 'MBProgressHUD'` sans numéro de version. Pensez à mettre à jour sauf si vous avez spécifiquement besoin de 0.9.1 pour la compatibilité.
- **Documentation** : Consultez la [page GitHub de MBProgressHUD](https://github.com/jdg/MBProgressHUD) pour plus d'options et d'exemples. La version 0.9.1 pourrait avoir moins de fonctionnalités que les versions modernes.

Faites-moi savoir si vous avez besoin d'aide pour le dépannage ou des exemples plus spécifiques !