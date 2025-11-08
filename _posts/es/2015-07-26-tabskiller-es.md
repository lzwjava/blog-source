---
audio: false
generated: false
image: false
lang: es
layout: post
title: TabsKiller
translated: true
type: post
---

Este es el README.md del proyecto de GitHub [https://github.com/lzwjava/TabsKiller](https://github.com/lzwjava/TabsKiller).

---

# TabsKiller

¡Presentamos un complemento de Chrome que cierra automáticamente las pestañas más antiguas cuando tu navegador se llena de demasiadas pestañas! ¡Di adiós para siempre a una experiencia de navegador desordenada!

一个神奇的 Chrome 插件，当打开网页过多的时候，会自动关掉最老的网页，让浏览器保持清爽！

![xxqq20160114-1 2x](https://cloud.githubusercontent.com/assets/5022872/12328379/25a749c2-bb16-11e5-8400-6e5c67027a61.png)

=>

![qq20160114-2 2x](https://cloud.githubusercontent.com/assets/5022872/12328400/3906a1ca-bb16-11e5-853c-0da4ce65cd6a.png)

# Complemento

![qq20151003-2 2x](https://cloud.githubusercontent.com/assets/5022872/10262499/b39deb34-69fc-11e5-93b8-35bf10cedaaa.jpg)

# Características

1. Cierra automáticamente las pestañas más antiguas cuando el número de pestañas supera un límite establecido.
2. Personaliza el número máximo de pestañas (x) según tu preferencia.
3. Bloquea patrones de URL específicos para asegurarte de que las pestañas que coinciden con esos patrones permanezcan abiertas, incluso cuando hay demasiadas pestañas abiertas.

# 特性

1. 会自动关掉最老的网页，当打开的网页超过一定数量的时候。
2. 可以设置最大的标签数量。
3. 可以设置锁定规则，使得满足这个规则的网页不被关闭。

## Historia

Suelo abrir muchas pestañas en Chrome. Entonces, presiono Ctrl + W para cerrarlas muchas veces. Repetir y repetir. Así que quiero escribir una extensión para solucionar mi problema. Luego, encontré la extensión “Tab Wrangler” que cierra pestañas cuando no están activas durante x minutos. Aprendí de ella y creé una extensión para cerrar las pestañas más antiguas cuando hay más de x pestañas. Y bloquear algunas pestañas cuyas URL coinciden con algún patrón. Me ayuda mucho. Simplemente no necesito preocuparme por las pestañas. Las pestañas nunca se vuelven demasiado numerosas. Me facilita la vida. Espero que te guste.

## Demostración

![killer](https://cloud.githubusercontent.com/assets/5022872/10262518/cd196a60-69fd-11e5-93bf-0589d65eeb19.gif)

## Instalación

Por favor, ve a la tienda de Chrome: [https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf](https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf), o instala manualmente:

Primero, ve a `chrome://extensions`, selecciona el modo desarrollador y luego carga la extensión descomprimida. ¡Listo!

![chrome](https://cloud.githubusercontent.com/assets/5022872/10262586/ddc451b0-6a00-11e5-8b10-da16c9658221.jpg)

Más detalles se pueden encontrar en el tutorial de [inicio en Chrome](https://developer.chrome.com/extensions/getstarted#unpacked).

中文：

请前往 Chrome 商店 [https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf](https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf), 或手动安装：

点击右边的 Download ZIP 下载源代码及解压，然后打开 `chrome://extensions`(复制粘贴到浏览器地址栏并打开)，选择`开发者模式`，然后点击`加载已解压的扩展程序`，像上面的图一样。接下来会弹出一个文件选择框，选择刚刚下载的源代码目录。这样就安装了这个插件了。