---
audio: false
generated: true
lang: es
layout: post
title: Uso de iVersion en iOS
translated: true
type: note
---

Para usar el pod `iVersion` en tu proyecto de iOS, debes seguir estos pasos:

1. **Abre tu proyecto en Xcode**: Asegúrate de tener tu proyecto de Xcode abierto donde deseas agregar el pod `iVersion`.

2. **Inicializa CocoaPods**: Si aún no has inicializado CocoaPods en tu proyecto, abre la Terminal, navega al directorio de tu proyecto y ejecuta:
   ```bash
   pod init
   ```
   Esto creará un `Podfile` en tu directorio de proyecto.

3. **Edita el Podfile**: Abre el `Podfile` en un editor de texto o en Xcode. Agrega el pod `iVersion` a tu `Podfile` incluyendo la siguiente línea dentro de la sección del target:
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Instala el Pod**: Guarda el `Podfile` y regresa a la Terminal. Ejecuta el siguiente comando para instalar el pod `iVersion`:
   ```bash
   pod install
   ```

5. **Abre el archivo `.xcworkspace`**: Una vez que la instalación se complete, cierra tu proyecto de Xcode si está abierto, y luego abre el archivo `.xcworkspace` recién creado. Este archivo generalmente se encuentra en el mismo directorio que tu archivo `.xcodeproj` original.

6. **Importa iVersion**: En tus archivos Swift u Objective-C, importa el módulo `iVersion` para comenzar a usarlo:
   ```swift
   import iVersion
   ```

7. **Usa iVersion en tu código**: Ahora puedes usar la librería `iVersion` en tu proyecto. Por ejemplo, puedes verificar la versión de la aplicación o el número de compilación usando los métodos proporcionados por `iVersion`.

Siguiendo estos pasos, deberías poder integrar y usar exitosamente el pod `iVersion` en tu proyecto de iOS.