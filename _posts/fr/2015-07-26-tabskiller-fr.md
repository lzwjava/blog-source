---
audio: false
generated: false
lang: fr
layout: post
title: TabsFermeur
translated: true
---

Voici le README.md du projet GitHub [https://github.com/lzwjava/TabsKiller](https://github.com/lzwjava/TabsKiller).

---

# TabsKiller

Présentant un plugin Chrome qui ferme automatiquement les onglets les plus anciens lorsque votre navigateur est encombré de trop d'onglets. Dites adieu à une expérience de navigation désordonnée à jamais !

一个神奇的 Chrome 插件，当打开网页过多的时候，会自动关掉最老的网页，让浏览器保持清爽！

![xxqq20160114-1 2x](https://cloud.githubusercontent.com/assets/5022872/12328379/25a749c2-bb16-11e5-8400-6e5c67027a61.png)

=>

![qq20160114-2 2x](https://cloud.githubusercontent.com/assets/5022872/12328400/3906a1ca-bb16-11e5-853c-0da4ce65cd6a.png)

# Plugin

![qq20151003-2 2x](https://cloud.githubusercontent.com/assets/5022872/10262499/b39deb34-69fc-11e5-93b8-35bf10cedaaa.jpg)

# Fonctionnalités

1. Ferme automatiquement les onglets les plus anciens lorsque le nombre d'onglets dépasse une limite définie.
2. Personnalisez le nombre maximum d'onglets (x) selon vos préférences.
3. Verrouillez des motifs d'URL spécifiques pour vous assurer que les onglets correspondant à ces motifs restent ouverts, même lorsqu'il y a trop d'onglets ouverts.

# 特性

1. 会自动关掉最老的网页，当打开的网页超过一定数量的时候。
2. 可以设置最大的标签数量。
3. 可以设置锁定规则，使得满足这个规则的网页不被关闭。

## Histoire

J'ouvre généralement de nombreux onglets dans Chrome. Donc, j'appuie sur Ctrl + W pour les fermer beaucoup à la fois. Répéter et répéter. Donc, je veux écrire une extension pour résoudre mon problème. Ensuite, j'ai trouvé l'extension "Tab Wrangler" qui ferme les onglets lorsqu'ils ne sont pas actifs depuis x minutes. J'ai appris de celle-ci et j'ai fait une extension pour fermer les onglets les plus anciens lorsqu'il y a plus de x onglets. Et verrouiller certains onglets dont l'URL correspond à certains motifs. Cela m'a beaucoup aidé. Je n'ai plus besoin de m'occuper des onglets. Les onglets ne deviennent jamais trop nombreux. Cela facilite ma vie. J'espère que vous l'aimerez aussi.

## Démo

![killer](https://cloud.githubusercontent.com/assets/5022872/10262518/cd196a60-69fd-11e5-93bf-0589d65eeb19.gif)

## Installer

Veuillez vous rendre sur le [Chrome Store](https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/) ou installer manuellement :

Tout d'abord, allez sur `chrome://extensions`, puis sélectionnez le mode développeur, et ensuite chargez l'extension décompressée. C'est fait.

![chrome](https://cloud.githubusercontent.com/assets/5022872/10262586/ddc451b0-6a00-11e5-8b10-da16c9658221.jpg)

Plus de détails peuvent être trouvés dans le tutoriel [démarrage de Chrome](https://developer.chrome.com/extensions/getstarted#unpacked).

中文：

Veuillez vous rendre sur la boutique Chrome [https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/](https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/) ou installer manuellement :

Cliquez sur Télécharger ZIP en bas à droite pour télécharger le code source et le décompresser, puis ouvrez `chrome://extensions` (copiez-collez dans la barre d'adresse du navigateur et ouvrez), sélectionnez le mode développeur, puis cliquez sur Charger le dossier non compressé comme ci-dessus. Ensuite, une boîte de sélection de fichiers apparaîtra, sélectionnez le dossier de code source téléchargé précédemment. Ainsi, cet outil sera installé.