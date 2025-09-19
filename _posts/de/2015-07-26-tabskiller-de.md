---
audio: false
generated: false
image: false
lang: de
layout: post
title: Das TabiTöter
translated: true
---

Dies ist die README.md des GitHub-Projekts [https://github.com/lzwjava/TabsKiller](https://github.com/lzwjava/TabsKiller).

---

# TabsKiller

Ein Chrome-Plugin, das automatisch die ältesten Tabs schließt, wenn Ihr Browser mit zu vielen Tabs überlastet ist. Verabschieden Sie sich für immer von einem unordentlichen Browser-Erlebnis!

一个神奇的 Chrome 插件，当打开网页过多的时候，会自动关掉最老的网页，让浏览器保持清爽！

![xxqq20160114-1 2x](https://cloud.githubusercontent.com/assets/5022872/12328379/25a749c2-bb16-11e5-8400-6e5c67027a61.png)

=>

![qq20160114-2 2x](https://cloud.githubusercontent.com/assets/5022872/12328400/3906a1ca-bb16-11e5-853c-0da4ce65cd6a.png)

# Plugin

![qq20151003-2 2x](https://cloud.githubusercontent.com/assets/5022872/10262499/b39deb34-69fc-11e5-93b8-35bf10cedaaa.jpg)

# Funktionen

1. Schließt automatisch die ältesten Tabs, wenn die Anzahl der Tabs eine festgelegte Grenze überschreitet.
2. Passen Sie die maximale Anzahl der Tabs (x) nach Ihren Vorlieben an.
3. Schließen Sie bestimmte URL-Muster ein, um sicherzustellen, dass Tabs, die diesen Mustern entsprechen, offen bleiben, auch wenn zu viele Tabs geöffnet sind.

# 特性

1. 会自动关掉最老的网页，当打开的网页超过一定数量的时候。
2. 可以设置最大的标签数量。
3. 可以设置锁定规则，使得满足这个规则的网页不被关闭。

## Geschichte

Normalerweise öffne ich viele Tabs in Chrome. Daher drücke ich oft Strg + W, um viele davon zu schließen. Wiederholen und wiederholen. Daher möchte ich eine Erweiterung schreiben, um mein Problem zu lösen. Dann habe ich die Erweiterung „Tab Wrangler“ gefunden, die Tabs schließt, wenn sie x Minuten inaktiv sind. Ich habe davon gelernt und eine Erweiterung erstellt, um die ältesten Tabs zu schließen, wenn mehr als x Tabs geöffnet sind. Und einige Tabs, deren URL einige Muster entsprechen, gesperrt. Es hilft mir sehr. Ich muss mich nicht mehr um Tabs kümmern. Tabs werden niemals zu viel. Es erleichtert mein Leben. Ich hoffe, dir gefällt es.

## Demo

![killer](https://cloud.githubusercontent.com/assets/5022872/10262518/cd196a60-69fd-11e5-93bf-0589d65eeb19.gif)

## Installieren

Bitte gehen Sie zum Chrome-Store: https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/ oder installieren Sie manuell:

Gehen Sie zuerst zu `chrome://extensions`, wählen Sie dann den Entwicklermodus aus und laden Sie die entpackte Erweiterung. Fertig.

![chrome](https://cloud.githubusercontent.com/assets/5022872/10262586/ddc451b0-6a00-11e5-8b10-da16c9658221.jpg)

Mehr Details finden Sie in der Chrome-Start-Tutorial [Anleitung](https://developer.chrome.com/extensions/getstarted#unpacked).

中文：

请前往 Chrome 商店 https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/ ，或手动安装：

点击右边的 Download ZIP 下载源代码及解压，然后打开 `chrome://extensions`(复制粘贴到浏览器地址栏并打开)，选择`开发者模式`，然后点击`加载已解压的扩展程序`，像上面的图一样。接下来会弹出一个文件选择框，选择刚刚下载的源代码目录。这样就安装了这个插件了。