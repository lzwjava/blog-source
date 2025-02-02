---
audio: false
lang: fr
layout: post
title: TabsKiller
translated: true
---

Voici le README.md du projet Github [https://github.com/lzwjava/TabsKiller](https://github.com/lzwjava/TabsKiller).

---

# TabsKiller

Découvrez un plugin Chrome qui ferme automatiquement les onglets les plus anciens lorsque votre navigateur est encombré de trop d'onglets. Faites vos adieux à l'expérience de navigation désordonnée pour toujours !

一個神奇的 Chrome 插件，当打开网页过多的时候，会自动关掉最老的网页，让浏览器保持清爽！

![xxqq20160114-1 2x](https://cloud.githubusercontent.com/assets/5022872/12328379/25a749c2-bb16-11e5-8400-6e5c67027a61.png)

=>

![qq20160114-2 2x](https://cloud.githubusercontent.com/assets/5022872/12328400/3906a1ca-bb16-11e5-853c-0da4ce65cd6a.png)

# Plugin

![qq20151003-2 2x](https://cloud.githubusercontent.com/assets/5022872/10262499/b39deb34-69fc-11e5-93b8-35bf10cedaaa.jpg)

# Fonctionnalités

1. Ferme automatiquement les onglets les plus anciens lorsque le nombre d'onglets dépasse une limite définie.
2. Personnalisez le nombre maximum d'onglets (x) selon vos préférences.
3. Verrouillez des modèles d'URL spécifiques pour vous assurer que les onglets correspondant à ces modèles restent ouverts, même lorsqu'il y a trop d'onglets ouverts.

# 特性

1. 会自动关掉最老的网页，当打开的网页超过一定数量的时候。
2. 可以设置最大的标签数量。
3. 可以设置锁定规则，使得满足这个规则的网页不被关闭。

## Story

Je ouvre généralement de nombreux onglets dans Chrome. Donc, je presse Ctrl + W pour les fermer beaucoup en une fois. Répète et répète. Alors je veux écrire une extension pour résoudre mon problème. Ensuite, j'ai trouvé l'extension "Tab Wrangler" qui ferme les onglets lorsqu'ils ne sont pas actifs pendant x minutes. J'ai appris de celle-ci et j'ai fait une extension pour fermer les onglets les plus anciens lorsqu'il y a plus de x onglets. Et verrouillez certains onglets dont l'URL correspond à certains modèles. Cela m'aide beaucoup. Je n'ai juste plus à m'occuper des onglets. Les onglets ne deviennent jamais trop nombreux. Cela facilite ma vie. J'espère que vous l'aimerez aussi.

## Démo

![killer](https://cloud.githubusercontent.com/assets/5022872/10262518/cd196a60-69fd-11e5-93bf-0589d65eeb19.gif)

## Installation

Veuillez aller sur le Chrome Store [https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/](https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/) ,
ou installer manuellement :

Tout d'abord, allez à `chrome://extensions`, puis sélectionnez le mode développeur, puis chargez l'extension décompressée. C'est fait.

![chrome](https://cloud.githubusercontent.com/assets/5022872/10262586/ddc451b0-6a00-11e5-8b10-da16c9658221.jpg)

Plus de détails peuvent être trouvés dans le tutoriel Get Started de Chrome [tutorial](https://developer.chrome.com/extensions/getstarted#unpacked).

中文：

请前往 Chrome 商店 https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/ ，或手动安装：

点击右边的 Download ZIP 下载源代码及解压，然后打开 `chrome://extensions`(复制粘贴到浏览器地址栏并打开)，选择`开发者模式`，然后点击`加载已解压的扩展程序`，像上面的图一样。接下来会弹出一个文件选择框，选择刚刚下载的源代码目录。这样就安装了这个插件了。