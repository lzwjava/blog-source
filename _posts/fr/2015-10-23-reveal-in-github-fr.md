---
audio: false
generated: false
image: false
lang: fr
layout: post
title: 'Un Plugin Xcode : Révéler-sur-GitHub'
translated: true
type: post
---

Voici le README.md du projet GitHub [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub).

---

# Reveal-In-GitHub

Un plugin Xcode conçu pour une navigation fluide vers les fonctionnalités principales de GitHub directement depuis votre dépôt actuel. En un seul clic, accédez facilement à l'historique GitHub, à la fonction Blame, aux demandes de pull, aux issues et aux notifications, le tout en quelques secondes.

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

Mon entreprise utilise GitHub. J'ouvre GitHub très souvent. Parfois, je suis en train de modifier quelque chose dans Xcode et je ne comprends pas certains codes, donc je vais sur GitHub pour les blâmer. Parfois, je cherche les derniers commits concernant un fichier pour m'aider à comprendre comment le code évolue. Donc je me demande s'il existe un outil pour m'aider à ouvrir rapidement GitHub depuis Xcode. Donc j'ai écrit ce plugin. Lorsqu'on modifie un fichier source dans Xcode, il est facile de savoir sur quel dépôt GitHub on travaille et quel fichier on édite. Cela a du sens de sauter rapidement au fichier sur GitHub, de sauter rapidement pour blâmer la ligne que l'on édite actuellement sur GitHub, de sauter rapidement aux issues ou aux PR du dépôt actuel sur lequel on travaille dans Xcode.

## Éléments de menu

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

Il comporte six éléments de menu :

 Menu Title     | Raccourci              | Modèle d'URL GitHub (Lorsque je modifie LZAlbumManager.m Ligne 40)
----------------|-----------------------|----------------------------------
 Paramètres	    |⌃⇧⌘S |
 Dépôt           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 Fichier rapide     |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Liste historique   |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blâme          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 Notifications  |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

Les raccourcis sont soigneusement conçus. Ils n'entrent pas en conflits avec les raccourcis par défaut de Xcode. Le modèle de raccourci est ⌃⇧⌘ (Ctrl+Shift+Command), plus la première lettre du titre du menu.

## Personnaliser

Parfois, vous voudrez peut-être sauter rapidement à la wiki. Voici comment procéder, ouvrez les paramètres :

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

Par exemple,

Fichier rapide, le modèle et l'URL réelle :

```
           {git_remote_url}       /blob/{commit}/          {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

Le {commit} est le dernier hash de commit de la branche actuelle. C'est mieux que d'utiliser la branche. Car le HEAD de la branche peut changer. Donc le code en #L40-L43 peut également changer.

Donc si vous voulez ajouter un raccourci à la wiki du dépôt actuel, il suffit d'ajouter un élément de menu et de définir le modèle sur ` {git_remote_url}/wiki`.

Dans les paramètres, `Clear Default Repos` dit si vous avez plusieurs remotes Git, lorsque vous déclenchez pour la première fois, il vous demandera d'en choisir un :

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

Ensuite, le plugin se souvient de votre choix. Donc quand vous déclenchez le menu à nouveau, il ouvrira ce dépôt distant comme par défaut. Le bouton `Clear Default Repos` effacera ce paramètre, vous demandera de sélectionner à nouveau.

## Installer

Recommandé d'installer avec [Alcatraz](http://alcatraz.io/),

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

Ou

1. Clonez ce dépôt.
2. Ouvrez `Reveal-In-GitHub.xcodeproj`, et compilez-le.
3. Reveal-In-GitHub.xcplugin devrait être situé à `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. Redémarrez Xcode
5. Ouvrez n'importe quel projet GitHub et appuyez sur ⌃⇧⌘B (Ctrl+Shift+Command+B) pour blâmer le code.

## 安装

推荐使用 [Alcatraz](http://alcatraz.io/)，可参考巧神的一遍[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)。安装好后，按照上图搜索 `Reveal In GitHub`，点击 `Install` 即可。

如果不使用这个工具的话，那么也只需三步：

* 克隆该项目到本地。
* 打开 xcodeproj，点击 Build 构建。这会在目录`~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` 生成 Reveal-In-GitHub.xcplugin 文件。
* 重启 Xcode，打开任意一个放在 GitHub 上的项目。按下 `Ctrl+Shift+Command+B` 即可。

## Crédits

Lors du développement, j'ai trouvé un autre plugin [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) qui fait quelque chose de similaire. J'ai appris certaines techniques de celui-ci. Merci pour cela.

## Licence

MIT