---
audio: false
generated: false
image: true
lang: es
layout: post
title: Pixel USB, Herramientas de desarrollo de iOS, Escritura deslizable
translated: true
---

### Tabla de Contenidos

1. [Opciones USB de Pixel](#pixels-usb-options)
   - Usar Pixel como webcam
   - Habilitar Modo Desarrollador en los ajustes
   - Activar Depuración USB para la conexión
   - Verificar conexión con comando ADB

2. [Modo Desarrollador de iOS y ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - Ver aplicaciones instaladas a través de Xcode
   - Usar Xcode para capturas de pantalla y registros
   - Listar aplicaciones con el comando xcrun
   - Instalar y usar la herramienta ideviceinstaller

3. [Escritura rápida por deslizamiento](#quick-swipe-typing)
   - Introducir palabras deslizando sobre las letras
   - Función descubierta por accidente
   - La línea aparece durante el toque rápido


<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel ofrece varias opciones USB, y una característica particularmente interesante es su capacidad para funcionar como webcam. En macOS, QuickTime puede acceder a la webcam de Android como fuente de video, proporcionando una solución sencilla y efectiva.

Para configurarlo:

1. Ve a "Acerca del teléfono" en los ajustes y toca "Número de compilación" siete veces para habilitar el Modo Desarrollador.
2. Abre "Opciones de desarrollador" y habilita la "Depuración USB".
3. Conecta tu Pixel a tu computadora mediante USB y ejecuta el siguiente comando en un terminal para verificar la conexión:
   ```bash
   adb devices
   ```

---

## Modo Desarrollador de iOS y ideviceinstaller

*2024.12.03*

## Modo Desarrollador

Fui desarrollador de iOS durante algún tiempo. Pero mi enfoque profesional ha cambiado a otras tecnologías. Sin embargo, sigue siendo muy útil aplicar el conocimiento de desarrollo de iOS, aunque ahora no sea un desarrollador profesional de iOS.

Recientemente, quería compartir mis aplicaciones instaladas. Pero si tomaba capturas de pantalla de todas las aplicaciones desde la pantalla de inicio o desde la lista de aplicaciones en los ajustes, sería un desorden. Así que necesitaba encontrar una manera de ver todas las aplicaciones instaladas.

Aquí están los pasos para ver todas las aplicaciones instaladas usando Xcode:

1. Conecta tu iPhone a tu Mac vía USB
2. Abre Xcode
3. Ve a Ventana → Dispositivos y Simuladores (o presiona Shift + Cmd + 2)
4. Selecciona tu iPhone de la barra lateral izquierda
5. En el panel principal, desplázate hasta la sección "Installed Apps"

Tiene otras funciones útiles:

1. Tomar capturas de pantalla
2. Abrir registros recientes
3. Abrir la consola

## xcrun

```bash
(base) lzwjava@192 Descargas % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Utilizando registro detallado.
2024-12-03 16:24:18.579+0800  Habilitando servicios de imagen de disco de desarrollador.
2024-12-03 16:24:18.637+0800  Afirmación de uso adquirida.
Aplicaciones instaladas:
  - 0 elementos

Comando completado, tardó 0.120 segundos
```


## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Descargas % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

---

## Escritura rápida por deslizamiento

*2024.12.01*

Si quieres escribir "threads" en iOS, solo necesitas dibujar rápidamente una línea para cubrir las posiciones de las letras "threads" para obtener el resultado. Veamos cómo funciona.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Descubrí esto accidentalmente. Cuando mi dedo toca rápidamente el área de entrada, mostrará una línea. No sé qué significa eso. Después de algunos experimentos, hice el descubrimiento anterior.