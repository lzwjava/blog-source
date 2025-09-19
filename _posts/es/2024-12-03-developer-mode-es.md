---
audio: false
generated: false
image: false
lang: es
layout: post
title: Modo Desarrollador de iOS e ideviceinstaller
translated: true
---

## Modo Desarrollador

Durante un tiempo fui desarrollador de iOS. Sin embargo, mi enfoque profesional ha cambiado a otras tecnologías. Aun así, sigue siendo muy útil aplicar conocimientos de desarrollo en iOS aunque ya no sea un desarrollador profesional en esta área.

Recientemente, quise compartir las aplicaciones que tengo instaladas. Pero si tomaba capturas de pantalla de todas las apps desde la pantalla de inicio o desde la lista de aplicaciones en ajustes, sería un desorden. Así que necesitaba encontrar una forma de ver todas las aplicaciones instaladas.

Estos son los pasos para ver todas las aplicaciones instaladas usando Xcode:

1. Conecta tu iPhone a tu Mac mediante USB
2. Abre Xcode
3. Ve a Window → Devices and Simulators (o presiona Shift + Cmd + 2)
4. Selecciona tu iPhone en la barra lateral izquierda
5. En el panel principal, desplázate hacia abajo hasta la sección "Installed Apps"

También tiene otras funciones útiles:

1. Tomar capturas de pantalla
2. Abrir registros recientes
3. Abrir la consola

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
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

## Escritura por Deslizamiento Rápido

*2024.12.01*

Si quieres escribir "threads" en iOS, solo necesitas dibujar rápidamente una línea que cubra las posiciones de las letras de "threads" para obtener el resultado. Veamos cómo funciona.

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Lo descubrí por accidente. Cuando mi dedo toca rápidamente el área de entrada, aparece una línea. No sabía qué significaba. Después de algunos experimentos, hice el descubrimiento anterior.