---
audio: false
generated: true
lang: es
layout: post
title: Enrutador Mesh
translated: true
---

## TP-Link AX3000 - TL-XDR 3050

Comencé a usar un router de malla en 2023. Compré un sistema TP-Link AX3000 que consta de dos routers de malla: una unidad principal y una unidad satélite. Me costó alrededor de 484 CNY en ese momento, pero ahora solo cuesta 395 CNY en JD.com.

Inicialmente usé este sistema en mi casa grande, pero luego lo trasladé a la casa de mis padres.

## ZTE AC1200

Durante algunos días del Festival de Primavera de 2025, mi familia se quedó en mi casa grande y experimentó nuevamente una mala calidad de la red WiFi. Para solucionar esto, compré otro router de malla, el ZTE AC1200, que cuesta alrededor de 108 CNY.

Productos similares disponibles en Walmart incluyen el TP-Link WiFi Mesh Router, el Eero Dual Band Mesh Router y el NetGear Nighthawk AX3000. Los precios de la mayoría de estos productos oscilan entre 50 USD y 200 USD.

Para el router de malla ZTE AC1200, simplemente podía comprar uno y usar el modo puente, permitiendo que reciba una señal WiFi y luego emita su propia señal WiFi. Funciona perfectamente. Originalmente, la dirección de dominio del router era 192.168.5.1. Después de habilitar el modo puente, esta dirección IP ya no es accesible. En su lugar, 192.168.1.1 te redirigirá al router principal en tu red doméstica. En este punto, puedes acceder al centro de control del router navegando a http://zte.home.

Si puedes acceder al router principal, puedes ver los dispositivos conectados y sus direcciones IP. Luego, puedes intentar acceder a cada dispositivo para determinar cuál es el sub-router. En mi caso, era 192.168.1.23, que es la dirección del router de malla ZTE AC1200.

Para los teléfonos móviles, que movemos por la casa, es mejor usar el canal de 2.4 GHz ya que es más estable. Para las laptops o computadoras de escritorio, que normalmente usamos en nuestros dormitorios o estudios, es mejor usar el canal de 5 GHz ya que es más rápido.

Después de usarlo durante varios días, encuentro que es un poco deficiente. La velocidad o la señal es peor que la del TL-XDR 3050.

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*Fuente: JD.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*Fuente: Walmart.com*{: .caption }

## Alimentación de 12V para Routers

Un cable elevador de voltaje USB puede usarse para alimentar routers utilizando un banco de energía.

Sin embargo, en algunos casos, el cable elevador de un banco de energía puede no ser capaz de configurar el router correctamente. El router puede reiniciarse continuamente.

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*Fuente: JD.com*{: .caption }

## Dos Formas de Ayudar a un Sub-Router a Encontrar el Router Principal

A veces, un sub-router no puede encontrar fácilmente el router principal cuando la señal es débil.

Si tenemos que colocar el sub-router lejos del router principal, me pregunto si es más rápido conectarlo primero en una ubicación cercana y luego moverlo más lejos, en lugar de intentar conectarlo cuando ya está en la ubicación lejana.

Mantener una conexión mientras están cerca permite que se comuniquen entre sí. He encontrado que este método es más efectivo.