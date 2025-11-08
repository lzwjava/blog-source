---
audio: false
generated: false
image: true
lang: es
layout: post
title: Algunas Plataformas Globales en la Nube
translated: true
type: post
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/><img/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - Fallo](#google-cloud---fail)
* [Resumen](#outline)
* [Conclusión](#summary)

Recientemente probé algunas plataformas en la nube. Las utilicé para configurar mi propio servidor proxy. Antes, usaba un servidor proxy de terceros. Ese servidor es utilizado por muchos usuarios, por lo que a veces la velocidad es lenta. Intenté configurar el mío propio para solucionar este problema.

## Azure

Azure es una buena opción. Creé 3 máquinas virtuales aquí. Porque la plataforma me dio 200 dólares de crédito de forma gratuita. Mis máquinas están ubicadas en Qatar, Estados Unidos y Hong Kong. El tiempo de ping desde mi portátil en Guangzhou al servidor de Qatar es de 150ms. Ahora, los paquetes de ping al servidor de Estados Unidos se pierden en un 100%. Hace dos días, podía hacer ping con éxito. Y los paquetes de ping al servidor de Hong Kong también se pierden en un 100%. Los probé en mi cliente proxy de iOS y no se podían conectar. Necesito apagarlos. Aunque el costo es gratuito, un servidor perdido no me sirve de nada.

<div align="center"><img src="/assets/images/cloud/azure.png" /><img/></div>

Veamos la consola y la pestaña de red, arriba y abajo.

<div align="center"><img src="/assets/images/cloud/network.png" /><img/></div>

Mi configuración de red personalizada es sencilla. Simplemente dejo abiertos todos los puertos entre 1024 y 65535 para cualquier protocolo, ya que es mi servidor proxy. No tengo datos secretos ni programas dentro de él, así que sigo la sugerencia de la aplicación Outline para hacerlo.

## AWS Lightsail

Lightsail es un producto ligero de AWS. AWS tiene una gran cantidad de productos. Y a veces solo queremos crear algunas máquinas virtuales dentro de él. Por eso nos ofrecen AWS Lightsail.

<div align="center"><img src="/assets/images/cloud/lightsail.png" /><img/></div>

## Digital Ocean

Utilicé mucho Digital Ocean en plataformas en la nube en el extranjero, especialmente entre 2016 y 2018. Gastaba 5 dólares cada mes.

Creamos un droplet de la siguiente manera:

<div align="center"><img src="/assets/images/cloud/do.png" /><img/></div>

Este es mi historial de facturación:

<div align="center"><img src="/assets/images/cloud/bill.png" /><img/></div>

## Vultr

Usé Vultr desde 2018 hasta 2020.

<div align="center"><img src="/assets/images/cloud/vultr.png" /><img/></div>

## Google Cloud - Fallo

También quiero probar Google Cloud. Sin embargo, no tuve éxito. No admiten usuarios de China. Aunque podemos proporcionar información falsa como si fuéramos ciudadanos de otros países, no tenemos la tarjeta de crédito correspondiente para registrarnos con éxito.

<div align="center"><img src="/assets/images/cloud/google.png" /><img/></div>

## Esquema

Outline no es una plataforma en la nube. Es una herramienta de proxy. Como me ayuda a configurar mi servidor proxy, tengo que escribir un párrafo aparte para elogiarla. Es realmente útil. Puedes obtener más información buscándola en línea.

<div align="center"><img src="/assets/images/cloud/outline.png" /><img/></div>

## Resumen

El servidor más barato con la configuración más baja suele costar alrededor de 5 dólares al mes. Es suficiente para actuar como un servidor proxy para ser utilizado por unos pocos usuarios. Los servidores en Singapur, Hong Kong u otras áreas de Asia suelen estar conectados más rápido que los servidores en Estados Unidos o Europa. Y a veces, cuando acabas de configurar el servidor, funciona de maravilla. Sin embargo, cuando pasan unos días, funciona como un zombi. Así que, en cuanto a velocidad y estabilidad, solo puedes descubrir la verdad en tu uso diario.