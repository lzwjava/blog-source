---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Mode Développeur d’iOS et ideviceinstaller
translated: true
---

## Mode Développeur

J'ai été développeur iOS pendant un certain temps. Mais mon orientation professionnelle s'est déplacée vers d'autres technologies. Cependant, il est toujours très utile d'appliquer les connaissances en développement iOS même si je ne suis plus un développeur iOS professionnel aujourd'hui.

Récemment, je voulais partager mes applications installées. Mais si je prenais des captures d'écran de toutes les applications depuis l'écran d'accueil ou depuis la liste des applications dans les paramètres, ce serait un désordre. J'ai donc dû trouver un moyen de voir toutes les applications installées.

Voici les étapes pour voir toutes les applications installées en utilisant Xcode :

1. Connectez votre iPhone à votre Mac via USB
2. Ouvrez Xcode
3. Allez dans Fenêtre → Appareils et Simulateurs (ou appuyez sur Maj + Cmd + 2)
4. Sélectionnez votre iPhone dans la barre latérale de gauche
5. Dans le panneau principal, faites défiler vers le bas jusqu'à la section "Applications Installées"

Il possède d'autres fonctions utiles :

1. Prendre des captures d'écran
2. Ouvrir les logs récents
3. Ouvrir la console

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
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

## Saisie par Glissement Rapide

*2024.12.01*

Si vous voulez saisir "threads" sur iOS, il vous suffit de tracer rapidement une ligne couvrant les positions des lettres "threads" pour obtenir le résultat. Voyons comment cela fonctionne.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la balise vidéo.
</video>

Je l'ai découvert par hasard. Lorsque mon doigt touche rapidement la zone de saisie, une ligne apparaît. Je ne savais pas ce que cela signifiait. Après quelques expériences, j'ai fait cette découverte.