---
audio: false
generated: false
lang: es
layout: post
title: Análisis de la Detección de VPN en ChatGPT para iOS
translated: true
---

Hoy descubrí que la aplicación de ChatGPT para iOS ahora permite iniciar sesión con una VPN en China. Anteriormente, mostraba un mensaje de bloqueo, como el que se muestra a continuación.

Sin embargo, hasta la fecha, funciona correctamente con una VPN.

Recuerdo que cuando se lanzó por primera vez la aplicación de ChatGPT para iOS, usarla con una VPN no era un problema. Más tarde, la detección de VPN se volvió más estricta, lo que dificultaba el inicio de sesión. Afortunadamente, parece que esta restricción se ha relajado recientemente.

Tras realizar más pruebas, descubrí que al usar una VPN de la región de Singapur de DigitalOcean, no podía acceder a la aplicación. Sin embargo, al usar VPNs de Taiwán o del Reino Unido (proporcionadas por https://zhs.cloud), funcionaba perfectamente.

Parece que la detección de VPN en ChatGPT para iOS se basa en direcciones IP específicas. Algunos proveedores de servicios en la nube o ciertas direcciones IP están bloqueadas, lo que podría explicar el comportamiento inconsistente dependiendo de la ubicación del servidor VPN.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }