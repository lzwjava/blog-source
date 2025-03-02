---
audio: false
generated: false
lang: fr
layout: post
title: L'application de Reconnaissance de Fleurs
translated: true
---

Ceci est le README.md du projet GitHub [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition).

---

### Application de Reconnaissance de Fleurs

C'est une application Android de reconnaissance de fleurs conçue pour aider les utilisateurs à identifier les fleurs en capturant des photos et en dessinant des cercles pour aider à la reconnaissance.

#### Fonctionnalités:
- **Capture de Photos** : Les utilisateurs peuvent prendre des photos de fleurs directement dans l'application.
- **Fonctionnalité de Dessin** : Possibilité de dessiner des cercles et des annotations sur les images de fleurs pour aider à la reconnaissance.
- **Authentication** : Authentification sécurisée des utilisateurs avec un écran de connexion.
- **Affichage des Résultats** : Afficher les résultats de reconnaissance dans une interface conviviale.
- **Design Matériel** : Mise en œuvre des principes de design matériel pour une expérience utilisateur moderne et intuitive.

#### Structure des Fichiers:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### Composants:
- **Activities** : Contient des classes pour gérer différentes activités de l'application telles que la connexion, la capture de photos et l'écran de démarrage.
- **Adapters** : Gère l'affichage des photos et des résultats de reconnaissance.
- **AVObject** : Représente les objets photo avec des métadonnées associées.
- **Drawing** : Classes liées au dessin de cercles et d'annotations sur les images de fleurs.
- **Fragments** : Fournit des composants UI pour afficher les résultats de reconnaissance et les indicateurs d'attente.
- **Material** : Possiblement lié à la mise en œuvre des directives de design matériel.
- **Services** : Gère les tâches en arrière-plan et la manipulation des données liées aux photos.
- **Utils** : Contient des classes utilitaires pour diverses tâches telles que la manipulation d'images et la journalisation.

#### Utilisation:
1. Cloner le dépôt.
2. Ouvrir le projet dans Android Studio.
3. Construire et exécuter l'application sur un appareil Android ou un émulateur.

#### Licence:
Ce projet est sous licence [MIT License](LICENSE).