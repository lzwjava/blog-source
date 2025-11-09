---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Desactivar la Notificación de Sonido de Ghostty
translated: true
type: note
---

### ¿Qué es la "pestaña de notificación" de Ghostty?

En Ghostty (un emulador de terminal acelerado por GPU), la "pestaña de notificación" probablemente se refiere a la función de notificación de campana visual. Cuando un comando o aplicación en ejecución en el terminal envía un carácter de campana (`\a`) (por ejemplo, desde un proceso de larga duración o un error), Ghostty puede anteponer un emoji de campana (🔔) al título de la pestaña o ventana afectada. Esto sirve como una alerta sutil para llamar tu atención de vuelta a esa pestaña, especialmente si el terminal no está enfocado o estás trabajando en otra pestaña. Es parte del sistema de manejo de campanas de Ghostty, que tiene como objetivo proporcionar notificaciones no intrusivas sin depender únicamente de audio o ventanas emergentes del sistema.

Este comportamiento está habilitado por defecto bajo la configuración `bell-features`, específicamente la opción `title`. Está diseñado para ser útil para flujos de trabajo como la finalización de trabajos en segundo plano, pero puede percibirse como una "notificación" no deseada en la barra de pestañas.

### Cómo desactivarlo

Para cancelar o desactivar esta notificación de título por campana (y potencialmente otros comportamientos de campana), edita tu archivo de configuración de Ghostty. La ubicación predeterminada es `~/.config/ghostty/config` en Linux o `~/Library/Application Support/com.mitchellh.Ghostty/config` en macOS.

1.  Abre el archivo de configuración en tu editor preferido.
2.  Añade o modifica la siguiente línea para desactivar específicamente el emoji del título (manteniendo otras funciones de campana como las solicitudes de atención):
    ```
    bell-features = no-title
    ```
    - Esto elimina el 🔔 del título de la pestaña pero permite otros efectos de campana (por ejemplo, audio del sistema o resaltado de ventana).

3.  Para una desactivación más completa (sin emoji de título, sin solicitudes de atención, etc.), usa:
    ```
    bell-features = false
    ```
    - Esto desactiva todas las funciones de campana por completo.

4.  Guarda el archivo y recarga tu configuración en Ghostty:
    - Presiona `Cmd/Ctrl + Shift + ,` (o ejecuta `ghostty --reload-config` desde otra terminal).
    - Las nuevas ventanas/pestañas usarán la configuración actualizada; las existentes pueden necesitar un reinicio.

Si esta no es la notificación exacta a la que te refieres (por ejemplo, si es un mensaje emergente dentro de la aplicación como "Copiado al portapapeles" o notificaciones de escritorio de las aplicaciones), también puedes desactivar esas:
-   Para mensajes emergentes dentro de la aplicación (solo Linux GTK): `app-notifications = false`
-   Para notificaciones de escritorio de aplicaciones de terminal: `desktop-notifications = false`

Pruébalo ejecutando un comando que active una campana, como `echo -e '\a'`.

[Referencia de Configuración de Ghostty](https://ghostty.org/docs/config/reference)  
[Discusión sobre Funciones de Campana de Ghostty](https://github.com/ghostty-org/ghostty/discussions/3242)