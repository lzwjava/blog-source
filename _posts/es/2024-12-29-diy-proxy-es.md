---
audio: true
lang: es
layout: post
title: Configurar tu servidor proxy
translated: true
---

* Para configurar un servidor, use Outline Manager: [https://getoutline.org](https://getoutline.org).

* Los proveedores de alojamiento recomendados incluyen DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr y Linode. Para un rendimiento óptimo, elija ubicaciones de servidores en Singapur o Tokio. Aunque Hong Kong también es una opción viable, tenga en cuenta que ciertas herramientas de IA como ChatGPT y Claude están restringidas en esa región.

* Todavía puede usar herramientas como Deepseek, Mistral, Grok y la API de Gemini (a través de Cursor) con servidores de Hong Kong. Usando el pensamiento inverso, dado que otros pueden evitar los servidores de Hong Kong, tienden a estar menos congestionados.

* Considere la ubicación del servidor y la distancia. Para aquellos en Guangzhou, Hong Kong es una buena opción para alojar un servidor proxy. Use Speedtest para medir la velocidad de la red.

* Si le importa la velocidad, la mejor opción, según mi conocimiento, es usar un servidor Aliyun Hong Kong con una IP elástica BGP (premium). La IP es elástica, lo que facilita la vinculación de una nueva si la IP actual es bloqueada. Además, esta conexión BGP (premium) está optimizada por Aliyun Cloud, proporcionando velocidades rápidas.

* Protocolos como Shadowsocks, VMess y Trojan pueden ser bloqueados fácilmente.

* Use Linode para una migración de servidor rápida.

* Es posible que necesite un script para renovar su servidor automáticamente todos los días.

* Si el servidor proxy es bloqueado por el GFW o encuentra otros problemas, puede usar una tarjeta SIM de China Telecom Macau para compartir datos celulares con su computadora portátil. Esto le permite configurar un nuevo servidor.

* Para servicios en la nube como Google Cloud Platform, la configuración de un nuevo servidor requiere un servidor proxy existente. Sin embargo, proveedores como DigitalOcean o Vultr se pueden configurar directamente sin necesidad de un servidor proxy.

* Use [Auto SS Config](https://github.com/lzwjava/auto-ss-config) para generar y cargar URLs de suscripción de Shadowsocks o Clash.

* Use la funcionalidad de instantánea en Digital Ocean. Si la IP del servidor es bloqueada, cree un nuevo droplet desde la instantánea del servidor y ejecute `install.sh` nuevamente.

* Use la funcionalidad de IP reservada en Digital Ocean. Si la IP del servidor es bloqueada, asigne una nueva IP reservada.

* Usamos Outline Manager para configurar nuestros propios servidores porque es rápido y nos permite disfrutar del servidor nosotros mismos. Los nodos del proveedor de VPN pueden ser a menudo poco confiables. Nuestros servidores también pueden tener problemas, pero tenemos un conocimiento mucho más detallado de la situación. También podemos elegir diferentes proveedores de la nube. Además, sabemos si estamos usando China Telecom o China Mobile, y si estamos usando Wi-Fi de casa o datos celulares.

* Probablemente no sea útil instalar OpenWrt en un enrutador para configurar un proxy. El problema principal es que el GFW puede bloquear fácilmente la dirección IP de su servidor proxy. Es mejor usar un método de suscripción, como con Clash, para cambiar fácilmente la configuración en su enrutador.