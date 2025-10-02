---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Pixel USB, Outils de développement iOS, Balayage gestuel
translated: true
---

### Table des matières

1. [Options USB du Pixel](#pixels-usb-options)
   - Utiliser Pixel comme webcam
   - Activer le mode développeur dans les paramètres
   - Activer le débogage USB pour la connexion
   - Vérifier la connexion avec la commande ADB

2. [Mode développeur d'iOS et ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - Afficher les applications installées via Xcode
   - Utiliser Xcode pour les captures d'écran et les journaux
   - Lister les applications avec la commande xcrun
   - Installer et utiliser l'outil ideviceinstaller

3. [Saisie rapide par balayage](#quick-swipe-typing)
   - Saisir des mots en balayant les lettres
   - Fonction découverte par accident
   - Une ligne apparaît lors d'un toucher rapide


## Options USB du Pixel

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Le Pixel offre plusieurs options USB, et une fonctionnalité particulièrement intéressante est sa capacité à fonctionner comme une webcam. Sur macOS, QuickTime peut accéder à la webcam Android comme source vidéo, offrant une solution simple et efficace.

Pour configurer cela :

1. Naviguez vers "À propos du téléphone" dans les paramètres et appuyez sept fois sur "Numéro de build" pour activer le mode développeur.
2. Ouvrez "Options pour les développeurs" et activez le "Débogage USB".
3. Connectez votre Pixel à votre ordinateur via USB et exécutez la commande suivante dans un terminal pour vérifier la connexion :
   ```bash
   adb devices
   ```

---

## Mode développeur d'iOS et ideviceinstaller

*2024.12.03*

## Mode développeur

J'ai été développeur iOS pendant un certain temps. Mais l'orientation de ma carrière s'est déplacée vers d'autres technologies. Cependant, il est toujours très utile d'appliquer mes connaissances en développement iOS même si je ne suis plus un développeur iOS professionnel aujourd'hui.

Récemment, je voulais partager mes applications installées. Mais si je prenais des captures d'écran de toutes les applications depuis l'écran d'accueil ou depuis la liste des applications dans les paramètres, ce serait un désordre. J'avais donc besoin de trouver un moyen de voir toutes les applications installées.

Voici les étapes pour afficher toutes les applications installées à l'aide de Xcode :

1. Connectez votre iPhone à votre Mac via USB
2. Ouvrez Xcode
3. Allez dans Fenêtre → Périphériques et simulateurs (ou appuyez sur Maj + Cmd + 2)
4. Sélectionnez votre iPhone dans la barre latérale gauche
5. Dans le panneau principal, faites défiler jusqu'à la section "Applications installées"

Il a d'autres fonctions utiles :

1. Prendre des captures d'écran
2. Ouvrir les journaux récents
3. Ouvrir la console

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800 Enabling developer disk image services.
2024-12-03 16:24:18.637+0800 Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```


## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

---

## Saisie rapide par balayage

*2024.12.01*

Si vous voulez saisir "threads" dans iOS, il vous suffit de dessiner rapidement une ligne pour couvrir les positions des lettres "threads" pour obtenir le résultat. Voyons comment cela fonctionne.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

J'ai découvert cela par accident. Lorsque mon doigt touche rapidement la zone de saisie, une ligne apparaît. Je ne sais pas ce que cela signifie. Après quelques expériences, j'ai fait la découverte ci-dessus.