---
audio: false
lang: fr
layout: post
title: 'Un Plugin Xcode : Révéler dans GitHub'
translated: true
---

# Reveal-In-GitHub

Un plugin Xcode conçu pour une navigation sans faille vers les fonctionnalités clés de GitHub au sein de votre dépôt actuel. Avec un simple clic, accédez facilement à l'historique de GitHub, à Blame, aux demandes de tirage, aux problèmes et aux notifications, le tout en quelques secondes.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

Mon entreprise travaille sur GitHub. J'ouvre GitHub très souvent. Parfois, je suis en train d'éditer dans Xcode et je ne comprends pas certains codes, alors je vais sur GitHub pour blâmer. Parfois, je trouve les derniers commits concernant un fichier pour m'aider à comprendre comment le code évolue. Je me suis donc demandé s'il existait un outil pour m'aider à ouvrir rapidement GitHub depuis Xcode. J'ai donc écrit ce plugin. Lorsque vous éditez un fichier source dans Xcode, il est facile de savoir quel dépôt GitHub vous utilisez et quel fichier vous éditez. Cela a donc du sens de sauter rapidement au fichier sur GitHub, de sauter rapidement pour blâmer la ligne en cours d'édition sur GitHub, de sauter rapidement aux problèmes ou aux demandes de tirage du dépôt actuel sur lequel vous travaillez dans Xcode.

## Éléments du menu

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

Il dispose de six éléments de menu :

 Menu Title     | Raccourci              | Modèle d'URL GitHub (Lorsque j'édite LZAlbumManager.m Ligne 40)                |
----------------|-----------------------|----------------------------------
 Paramètres	    |⌃⇧⌘S |
 Dépôt           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Problèmes         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Fichier Rapide     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Liste Historique   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blâme          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

Les raccourcis sont soigneusement conçus. Ils ne conflictueront pas avec les raccourcis par défaut de Xcode. Le modèle de raccourci est ⌃⇧⌘ (Ctrl+Shift+Command), plus le premier caractère du titre du menu.

## Personnaliser

Parfois, vous pourriez vouloir sauter rapidement à Wiki. Voici comment, ouvrez les paramètres :

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

Par exemple,

Fichier Rapide, le modèle et l'URL réelle :

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}    
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

L'élément {commit} est le dernier hash de commit de la branche actuelle. C'est mieux que d'utiliser une branche. Parce que le HEAD de la branche peut être changé. Donc, le code dans #L40-L43 peut aussi être changé.

Donc, si vous voulez ajouter un raccourci à la Wiki du dépôt actuel, ajoutez simplement un élément de menu et définissez le modèle sur `{git_remote_url}/wiki`.

Dans les paramètres, `Clear Default Repos` dit si vous avez plusieurs dépôts distants, la première fois que vous déclenchez, il vous demandera d'en choisir un :

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

Ensuite, le plugin se souvient de votre choix. Donc, quand vous déclenchez le menu à nouveau, il ouvrira ce dépôt distant comme par défaut. Le bouton `Clear Default Repos` effacera ce paramètre, vous demandera de sélectionner à nouveau.

## Installer

Recommandé d'installer avec [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

Ou

1. Cloner ce dépôt.
2. Ouvrir `Reveal-In-GitHub.xcodeproj`, et le construire.
3. Reveal-In-GitHub.xcplugin doit se situer à `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. Redémarrer Xcode
5. Ouvrir n'importe quel projet GitHub et appuyez sur ⌃⇧⌘B (Ctrl+Shift+Command+B) pour blâmer le code.

## 安装

推荐使用 [Alcatraz](http://alcatraz.io/)，可参考巧神的一遍[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)。安装好后，按照上图搜索 `Reveal In GitHub`，点击 `Install` 即可。

如果不使用这个工具的话，那么也只需三步：

* 克隆该项目到本地。
* 打开 xcodeproj，点击 Build 构建。这会在目录`~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` 生成 Reveal-In-GitHub.xcplugin 文件。
* 重启 Xcode，打开任意一个放在 GitHub 上的项目。按下 `Ctrl+Shift+Command+B` 即可。

## Crédit

Au cours de son développement, j'ai trouvé un autre plugin [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) qui fait quelque chose de similaire. J'ai appris certaines techniques de celui-ci. Merci pour cela.

## Licence

MIT