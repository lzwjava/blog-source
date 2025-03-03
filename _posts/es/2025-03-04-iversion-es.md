---
audio: false
generated: true
lang: es
layout: post
title: Usando iVersion en iOS
translated: true
---

Para usar el pod `iVersion` en tu proyecto de iOS, debes seguir estos pasos:

1. **Abrir tu proyecto en Xcode**: Asegúrate de tener tu proyecto de Xcode abierto donde quieras agregar el pod `iVersion`.

2. **Inicializar CocoaPods**: Si aún no has inicializado CocoaPods en tu proyecto, abre la Terminal, navega al directorio de tu proyecto y ejecuta:
   ```bash
   pod init
   ```
   Esto creará un archivo `Podfile` en el directorio de tu proyecto.

3. **Editar el Podfile**: Abre el `Podfile` en un editor de texto o en Xcode. Agrega el pod `iVersion` a tu `Podfile` incluyendo la siguiente línea dentro de la sección de destino:
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **Instalar el Pod**: Guarda el `Podfile` y vuelve a la Terminal. Ejecuta el siguiente comando para instalar el pod `iVersion`:
   ```bash
   pod install
   ```

5. **Abrir el archivo `.xcworkspace`**: Después de que la instalación esté completa, cierra tu proyecto de Xcode si está abierto, y luego abre el archivo `.xcworkspace` recién creado. Este archivo generalmente se encuentra en el mismo directorio que tu archivo original `.xcodeproj`.

6. **Importar iVersion**: En tus archivos Swift u Objective-C, importa el módulo `iVersion` para comenzar a usarlo:
   ```swift
   import iVersion
   ```

7. **Usar iVersion en tu código**: Ahora puedes usar la biblioteca `iVersion` en tu proyecto. Por ejemplo, puedes verificar la versión de la aplicación o el número de compilación utilizando los métodos proporcionados por `iVersion`.

Siguiendo estos pasos, deberías poder integrar y usar el pod `iVersion` en tu proyecto de iOS.