---
audio: false
generated: false
lang: fr
layout: post
title: Mode Développeur d'iOS et ideviceinstaller
translated: true
---

## Mode Développeur

J'ai été développeur iOS pendant un certain temps. Mais ma carrière s'est orientée vers d'autres technologies. Cependant, il est toujours très utile d'appliquer les connaissances en développement iOS, même si je ne suis plus un développeur iOS professionnel aujourd'hui.

Récemment, j'ai voulu partager les applications que j'avais installées. Mais si je prenais des captures d'écran de toutes les applications depuis l'écran d'accueil ou depuis la liste des applications dans les paramètres, cela serait un vrai désordre. J'avais donc besoin de trouver un moyen de visualiser toutes les applications installées.

Voici les étapes pour afficher toutes les applications installées à l'aide de Xcode :

1. Connectez votre iPhone à votre Mac via USB
2. Ouvrez Xcode
3. Allez dans Window → Devices and Simulators (ou appuyez sur Shift + Cmd + 2)
4. Sélectionnez votre iPhone dans la barre latérale gauche
5. Dans le panneau principal, faites défiler jusqu'à la section "Installed Apps"

Il possède d'autres fonctions utiles :

1. Prendre des captures d'écran
2. Ouvrir les journaux récents
3. Ouvrir la console

## xcrun

`xcrun` est un outil en ligne de commande fourni par Apple qui permet de localiser et d'invoquer des outils de développement inclus dans les SDK d'Xcode. Il est particulièrement utile pour exécuter des commandes spécifiques à un SDK ou à une version d'Xcode sans avoir à spécifier manuellement le chemin complet de l'outil.

### Utilisation de base

Pour utiliser `xcrun`, vous pouvez simplement taper `xcrun` suivi de la commande que vous souhaitez exécuter. Par exemple :

```bash
xcrun clang -o mon_programme mon_programme.c
```

Dans cet exemple, `xcrun` localise automatiquement le compilateur `clang` inclus dans Xcode et l'utilise pour compiler le fichier `mon_programme.c`.

### Sélection d'un SDK spécifique

Vous pouvez également spécifier un SDK particulier à utiliser avec l'option `-sdk`. Par exemple, pour utiliser le SDK iOS :

```bash
xcrun --sdk iphoneos clang -o mon_programme mon_programme.c
```

### Liste des outils disponibles

Pour voir une liste des outils disponibles que vous pouvez invoquer avec `xcrun`, vous pouvez utiliser la commande suivante :

```bash
xcrun --find
```

Cela affichera une liste des outils de développement disponibles dans le chemin actuel de Xcode.

### Conclusion

`xcrun` est un outil puissant pour les développeurs travaillant avec Xcode, car il simplifie l'accès et l'utilisation des outils de développement sans avoir à se soucier des chemins d'accès spécifiques. Que vous soyez en train de compiler du code, de signer des applications ou de gérer des SDK, `xcrun` peut vous faire gagner du temps et des efforts.

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Utilisation de la journalisation détaillée.
2024-12-03 16:24:18.579+0800  Activation des services d'image disque développeur.
2024-12-03 16:24:18.637+0800  Acquisition d'une assertion d'utilisation.
Applications installées :
  - 0 éléments
```

Commande terminée, a pris 0.120 secondes
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