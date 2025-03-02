---
audio: false
generated: false
lang: es
layout: post
title: Opciones USB de Pixel
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel ofrece varias opciones de USB, y una característica particularmente interesante es su capacidad para funcionar como una cámara web. En macOS, QuickTime puede acceder a la cámara web de Android como una fuente de video, proporcionando una solución simple y efectiva.

Para configurar esto:

1. Navega a "Acerca del teléfono" en los ajustes y toca "Número de compilación" siete veces para habilitar el Modo de Desarrollador.  
2. Abre "Opciones de desarrollador" y habilita la "Depuración USB".  
3. Conecta tu Pixel a tu computadora mediante USB y ejecuta el siguiente comando en una terminal para verificar la conexión:  
   ```bash
   adb devices
   ```