---
audio: false
generated: true
lang: es
layout: post
title: 'Xvfb: Servidor de Pantalla X11 sin Interfaz Gráfica'
translated: true
type: note
---

### ¿Qué es Xvfb?

Xvfb (X Virtual Framebuffer) es un servidor de pantalla X11 que ejecuta aplicaciones gráficas sin necesidad de una pantalla física o aceleración gráfica por hardware. Esencialmente, es un servidor X "sin cabeza" que simula una pantalla en la memoria, permitiendo que programas que requieren un entorno gráfico (como navegadores, pruebas de interfaz de usuario o herramientas de renderizado) se ejecuten en servidores o en entornos sin monitor, teclado o ratón.

Es comúnmente utilizado en pruebas automatizadas (por ejemplo, con Selenium para web scraping o pruebas de UI), pipelines de CI/CD, o cualquier escenario donde se necesite ejecutar aplicaciones basadas en X11 en segundo plano sin mostrar nada en pantalla.

### ¿Cómo funciona Xvfb?

1. **Creación de Pantalla Virtual**:
   - Cuando inicias Xvfb, crea una pantalla virtual (por ejemplo, `:99` u otro número de pantalla) que existe completamente en la RAM. Esta pantalla tiene una resolución, profundidad de color y otros parámetros que defines al lanzarla.
   - Comando de ejemplo: `Xvfb :99 -screen 0 1024x768x24` (inicia una pantalla virtual a una resolución de 1024x768 con color de 24 bits).

2. **Manejo de Operaciones Gráficas**:
   - Xvfb intercepta las peticiones del protocolo X11 de las aplicaciones (como dibujar ventanas, renderizar imágenes o manejar eventos).
   - En lugar de enviar la salida a una pantalla física, realiza todas las operaciones en un búfer de memoria (el "framebuffer"). Este búfer actúa como una pantalla virtual donde se escriben los píxeles pero nunca se muestran.
   - Soporta características básicas de X11 pero carece de aceleración por hardware, por lo que no es adecuado para gráficos de alto rendimiento como videojuegos—es más para renderizado simple o pruebas.

3. **Simulación de Eventos**:
   - Xvfb puede simular eventos de entrada (por ejemplo, de ratón/teclado) si es necesario, pero típicamente, las aplicaciones se ejecutan como si estuvieran en una pantalla real.
   - La salida no es visible, pero puedes capturar capturas de pantalla o volcar el framebuffer a archivos (usando herramientas como `xwd` o `import` de ImageMagick) para su verificación.

4. **Integración con Herramientas**:
   - Bibliotecas como pyvirtualdisplay (como en tu traza de error) encapsulan Xvfb para facilitar su inicio/detención desde código. Por ejemplo, en Python:
     ```python
     from pyvirtualdisplay import Display
     display = Display(visible=0, size=(1024, 768))
     display.start()
     # Ejecuta tu aplicación gráfica aquí
     display.stop()
     ```
   - Se ejecuta en segundo plano, y tu aplicación establece la variable de entorno `DISPLAY` (por ejemplo, `export DISPLAY=:99`) para apuntar al servidor virtual.

5. **Limitaciones**:
   - No hay interacción real con el hardware, por lo que no hay soporte para GPU o salida de video directa.
   - El uso de memoria puede crecer con resoluciones más grandes o sesiones de larga duración.
   - Es parte del proyecto X.org y está disponible en sistemas Linux/Unix; no es nativo de macOS o Windows (aunque existen alternativas como Xming para Windows).

Respecto al error que pegaste: Parece que Xvfb no está instalado en tu sistema (el `FileNotFoundError` para 'Xvfb'). En macOS (basado en tus rutas de Homebrew), puedes instalarlo mediante `brew install --cask xvfb` o similar, pero confirma que esté en tu PATH. pyvirtualdisplay depende de que esté disponible como un ejecutable.

[Página Man de Xvfb](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)  
[Wikipedia: Xvfb](https://en.wikipedia.org/wiki/Xvfb)  
[Cómo usar Xvfb para Pruebas Headless](https://www.browserstack.com/guide/what-is-xvfb)