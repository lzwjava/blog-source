---
audio: true
lang: es
layout: post
title: Configura tu Servidor Proxy
translated: true
---

* Para configurar un servidor, utiliza Outline Manager: [https://getoutline.org](https://getoutline.org).  
* Los proveedores de hosting recomendados incluyen DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr o Linode. Prefiere regiones en Singapur o Tokio. Evita la región de Hong Kong, ya que herramientas como ChatGPT y Claude están prohibidas allí.  
* Protocolos como Shadowsocks, VMess y Trojan pueden ser bloqueados fácilmente.  
* Usa Linode para una migración rápida del servidor.  
* Es posible que necesites un script para renovar automáticamente tu servidor todos los días.  
* Si el servidor proxy es bloqueado por el GFW o encuentra otros problemas, puedes usar una tarjeta SIM de China Telecom Macau para compartir datos móviles con tu portátil. Esto te permitirá configurar un nuevo servidor.  
* Para servicios en la nube como Google Cloud Platform, configurar un nuevo servidor requiere un servidor proxy existente. Sin embargo, proveedores como DigitalOcean o Vultr pueden configurarse directamente sin necesidad de un servidor proxy.
* Usa [Auto SS Config](https://github.com/lzwjava/auto-ss-config) para generar y subir URLs de suscripción de Shadowsocks o Clash.
* Utiliza la funcionalidad de snapshot en Digital Ocean. Si la IP del servidor es bloqueada, crea un nuevo droplet a partir del snapshot del servidor y ejecuta `install.sh` nuevamente.