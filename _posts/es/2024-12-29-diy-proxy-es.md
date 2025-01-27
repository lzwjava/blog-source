---
audio: true
lang: es
layout: post
title: Configura tu Servidor Proxy
translated: true
---

* Para configurar un servidor, utiliza Outline Manager: [https://getoutline.org](https://getoutline.org).  

* Los proveedores de hosting recomendados incluyen DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr o Linode. Prefiere regiones en Singapur o Tokio. Evita la región de Hong Kong, ya que herramientas como ChatGPT y Claude están prohibidas allí.  

* Si no te importa que ChatGPT y Claude estén prohibidos en Hong Kong, sigue siendo una opción viable. Puedes usar herramientas como Deepseek, Mistral, Grok y la API de Gemini con servidores en Hong Kong. Usa el pensamiento inverso; otros pueden evitar los servidores de Hong Kong, lo que los deja menos congestionados.  

* Considera la ubicación y la distancia del servidor. Para aquellos en Guangzhou, Hong Kong es una buena opción para alojar un servidor proxy. Usa Speedtest para medir la velocidad de la red.  

* Protocolos como Shadowsocks, VMess y Trojan pueden ser fácilmente bloqueados.  

* Usa Linode para una migración rápida de servidores.  

* Es posible que necesites un script para renovar automáticamente tu servidor todos los días.  

* Si el servidor proxy es bloqueado por el GFW o encuentra otros problemas, puedes usar una tarjeta SIM de China Telecom Macau para compartir datos móviles con tu laptop. Esto te permitirá configurar un nuevo servidor.  

* Para servicios en la nube como Google Cloud Platform, configurar un nuevo servidor requiere un servidor proxy existente. Sin embargo, proveedores como DigitalOcean o Vultr pueden configurarse directamente sin necesidad de un servidor proxy.  

* Usa [Auto SS Config](https://github.com/lzwjava/auto-ss-config) para generar y subir URLs de suscripción de Shadowsocks o Clash.  

* Usa la funcionalidad de instantáneas en Digital Ocean. Si la IP del servidor es bloqueada, crea un nuevo droplet a partir de la instantánea del servidor y ejecuta `install.sh` nuevamente.  

* Usa la funcionalidad de IP reservada en Digital Ocean. Si la IP del servidor es bloqueada, asigna una nueva IP reservada.  

* Usamos Outline Manager para configurar nuestros propios servidores porque es rápido y nos permite disfrutar del servidor por nosotros mismos. Los nodos de los proveedores de VPN suelen ser poco confiables. Nuestros servidores también pueden tener problemas, pero tenemos un conocimiento mucho más detallado de la situación. También podemos elegir diferentes proveedores de la nube. Además, sabemos si estamos usando China Telecom o China Mobile, y si estamos usando Wi-Fi doméstico o datos móviles.  

* Probablemente no sea útil instalar OpenWrt en un router para configurar un proxy. El principal problema es que el GFW puede bloquear fácilmente la dirección IP de tu servidor proxy. Es mejor usar un método de suscripción, como con Clash, para cambiar fácilmente la configuración en tu router.