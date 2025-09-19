---
audio: false
generated: false
image: false
lang: es
layout: post
title: Configura tu servidor proxy
translated: true
---

Para configurar un servidor, usa el Administrador de Contornos: [https://getoutline.org](https://getoutline.org).

Los proveedores de alojamiento recomendados incluyen DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr y Linode. Para un rendimiento óptimo, elige ubicaciones de servidores en Singapur o Tokio. Aunque Hong Kong también es una opción viable, ten en cuenta que ciertas herramientas de IA como ChatGPT y Claude están restringidas en esa región.

Aún puedes usar herramientas como Deepseek, Mistral, Grok y la API de Gemini (a través de Cursor) con servidores en Hong Kong. Usando el pensamiento inverso, dado que otros pueden evitar los servidores de Hong Kong, tienden a estar menos congestionados.

Considera la ubicación del servidor y la distancia. Para aquellos en Guangzhou, Hong Kong es una buena opción para alojar un servidor proxy. Usa Speedtest para medir la velocidad de la red.

Para una velocidad óptima, recomiendo usar un servidor de Aliyun Hong Kong con una IP elástica BGP (premium). La característica de IP elástica permite un reemplazo rápido si la IP actual se bloquea. La conexión BGP (premium) optimizada de Aliyun Cloud asegura un rendimiento rápido. El servicio cuesta 3 CNY por 1 GB de tráfico.

Protocolos como Shadowsocks, VMess y Trojan pueden ser fácilmente bloqueados.

La característica de Transferencia de IP de Linode te permite migrar rápidamente tu servidor a una nueva ubicación, obteniendo así una nueva dirección IP.

Es posible que necesites un script para renovar automáticamente tu servidor todos los días.

Si el servidor proxy es bloqueado por el GFW o encuentra otros problemas, puedes usar una tarjeta SIM de China Telecom Macau para compartir datos celulares con tu laptop. Esto te permite configurar un nuevo servidor.

Para servicios en la nube como Google Cloud Platform, la configuración de un nuevo servidor requiere un servidor proxy existente. Sin embargo, proveedores como DigitalOcean o Vultr se pueden configurar directamente sin necesidad de un servidor proxy.

Usa [Auto SS Config](https://github.com/lzwjava/lzwjava.github.io/blob/main/scripts/auto-ss-config/upload_configs.py) para generar y subir URLs de suscripción de Shadowsocks o Clash.

Usa la funcionalidad de captura de instantáneas en Digital Ocean. Si la IP del servidor está bloqueada, crea un nuevo droplet desde la captura de instantáneas del servidor y ejecuta `install.sh` nuevamente.

Usa la funcionalidad de IP reservada en Digital Ocean. Si la IP del servidor está bloqueada, asigna una nueva IP reservada.

Usamos el Administrador de Contornos para configurar nuestros propios servidores porque es rápido y nos permite disfrutar del servidor nosotros mismos. Los nodos de los proveedores de VPN pueden ser a menudo poco confiables. Nuestros servidores también pueden tener problemas, pero tenemos un conocimiento mucho más detallado de la situación. También podemos elegir diferentes proveedores de la nube. Además, sabemos si estamos usando China Telecom o China Mobile, y si estamos usando Wi-Fi de casa o datos celulares.

Probablemente no sea útil instalar OpenWrt en un enrutador para configurar un proxy. El principal problema es que el GFW puede bloquear fácilmente la dirección IP de tu servidor proxy. Es mejor usar un método de suscripción, como con Clash, para cambiar fácilmente la configuración en tu enrutador.