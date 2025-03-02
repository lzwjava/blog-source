---
audio: false
generated: false
lang: es
layout: post
title: Modo Desarrollador de iOS e ideviceinstaller
translated: true
---

## Modo Desarrollador

En algún momento fui desarrollador de iOS durante un tiempo. Sin embargo, mi enfoque profesional se ha desplazado hacia otras tecnologías. Aun así, sigue siendo muy útil aplicar los conocimientos de desarrollo de iOS, aunque ahora no sea un desarrollador profesional de iOS.

Recientemente, quise compartir las aplicaciones que tengo instaladas. Pero si tomaba capturas de pantalla de todas las aplicaciones desde la pantalla de inicio o desde la lista de aplicaciones en los ajustes, sería un desastre. Así que necesitaba encontrar una manera de ver todas las aplicaciones instaladas.

Aquí están los pasos para ver todas las aplicaciones instaladas usando Xcode:

1. Conecta tu iPhone a tu Mac mediante un cable USB
2. Abre Xcode
3. Ve a Window → Devices and Simulators (o presiona Shift + Cmd + 2)
4. Selecciona tu iPhone en la barra lateral izquierda
5. En el panel principal, desplázate hacia abajo hasta la sección "Installed Apps" (Aplicaciones instaladas)

Tiene otras funciones útiles:

1. Tomar capturas de pantalla
2. Abrir registros recientes
3. Abrir la consola

## xcrun

`xcrun` es una herramienta de línea de comandos que forma parte de Xcode, el entorno de desarrollo integrado (IDE) de Apple. Su función principal es localizar y ejecutar herramientas de desarrollo, como compiladores, enrutadores y otras utilidades, independientemente de la versión de Xcode que esté instalada en el sistema. Esto permite a los desarrolladores trabajar con diferentes versiones de Xcode sin necesidad de modificar manualmente las rutas de las herramientas.

### Uso básico

El comando `xcrun` se utiliza de la siguiente manera:

```bash
xcrun <herramienta> [opciones]
```

Por ejemplo, para compilar un archivo fuente en C utilizando el compilador `clang`, puedes usar:

```bash
xcrun clang archivo.c -o archivo
```

### Ejemplos comunes

1. **Compilar código Swift:**

   ```bash
   xcrun swiftc archivo.swift -o ejecutable
   ```

2. **Ejecutar pruebas unitarias:**

   ```bash
   xcrun simctl list devices
   ```

3. **Crear un archivo IPA para distribución:**

   ```bash
   xcrun -sdk iphoneos PackageApplication -v MyApp.app -o MyApp.ipa
   ```

### Opciones útiles

- `--sdk`: Especifica el SDK que se utilizará. Por ejemplo, `iphoneos` para iOS o `macosx` para macOS.
  
  ```bash
  xcrun --sdk iphoneos clang archivo.c -o archivo
  ```

- `--show-sdk-path`: Muestra la ruta del SDK seleccionado.

  ```bash
  xcrun --sdk iphoneos --show-sdk-path
  ```

- `--find`: Encuentra la ruta de una herramienta específica.

  ```bash
  xcrun --find clang
  ```

### Consideraciones

- Asegúrate de tener Xcode instalado y configurado correctamente en tu sistema.
- `xcrun` es especialmente útil en entornos donde se manejan múltiples versiones de Xcode, ya que permite seleccionar la versión deseada sin conflictos.

En resumen, `xcrun` es una herramienta esencial para los desarrolladores que trabajan con Xcode, ya que simplifica la gestión y ejecución de diversas herramientas de desarrollo en diferentes versiones del entorno.

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Usando registro detallado.
2024-12-03 16:24:18.579+0800  Habilitando servicios de imagen de disco de desarrollador.
2024-12-03 16:24:18.637+0800  Adquirida la aserción de uso.
Aplicaciones instaladas:
  - 0 elementos
```

Comando completado, tomó 0.120 segundos
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