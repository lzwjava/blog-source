---
audio: false
generated: true
lang: es
layout: post
title: LeanCloud Realtime SDK para iOS
translated: true
---

Para usar `pod 'AVOSCloudIM', '3.1.6.2'` en tu proyecto de iOS con CocoaPods, sigue estos pasos. Esto asume que tienes CocoaPods instalado y estás familiarizado con el desarrollo básico de iOS usando Xcode.

---

### Paso 1: Configurar CocoaPods (si no se ha hecho ya)
Si aún no has instalado CocoaPods, instálalo a través de la terminal:
```bash
sudo gem install cocoapods
```
Verifica la instalación:
```bash
pod --version
```

---

### Paso 2: Crear o Abrir tu Proyecto de Xcode
1. Abre tu proyecto de Xcode existente o crea uno nuevo en Xcode.
2. Cierra Xcode por ahora (lo volveremos a abrir más tarde con el workspace).

---

### Paso 3: Inicializar un Podfile
1. Abre tu terminal y navega al directorio raíz de tu proyecto (donde se encuentra el archivo `.xcodeproj`):
   ```bash
   cd /ruta/a/tu/proyecto
   ```
2. Si aún no tienes un Podfile, crea uno ejecutando:
   ```bash
   pod init
   ```
   Esto genera un `Podfile` básico en tu directorio de proyecto.

---

### Paso 4: Editar el Podfile
1. Abre el `Podfile` en un editor de texto (por ejemplo, `nano`, `vim` o cualquier editor de código como VS Code):
   ```bash
   open Podfile
   ```
2. Modifica el `Podfile` para incluir el pod `AVOSCloudIM` con la versión `3.1.6.2`. Aquí tienes un ejemplo de cómo podría verse tu `Podfile`:
   ```ruby
   platform :ios, '9.0'  # Especifica la versión mínima de iOS (ajusta según sea necesario)
   use_frameworks!       # Opcional: Usa esto si tu proyecto usa Swift o frameworks

   target 'NombreDeTuApp' do
     pod 'AVOSCloudIM', '3.1.6.2'  # Agrega esta línea para incluir AVOSCloudIM versión 3.1.6.2
   end
   ```
   - Reemplaza `'NombreDeTuApp'` con el nombre real de tu objetivo de Xcode (generalmente el nombre de tu app).
   - La línea `platform :ios, '9.0'` especifica la versión mínima de iOS; ajústala según los requisitos de tu proyecto.
   - `use_frameworks!` es necesario si tu proyecto usa Swift o si el pod requiere frameworks dinámicos.

3. Guarda y cierra el `Podfile`.

---

### Paso 5: Instalar el Pod
1. En la terminal, ejecuta el siguiente comando desde el directorio raíz de tu proyecto:
   ```bash
   pod install
   ```
   - Esto descarga e integra la biblioteca `AVOSCloudIM` (versión 3.1.6.2) en tu proyecto.
   - Si es exitoso, verás una salida similar a:
     ```
     Instalación de pod completa! Hay X dependencias del Podfile y X pods totales instalados.
     ```

2. Si encuentras errores (por ejemplo, pod no encontrado), asegúrate de que la versión `3.1.6.2` aún esté disponible en el repositorio de CocoaPods. Las versiones antiguas pueden no ser compatibles. Puedes verificar la última versión en [CocoaPods.org](https://cocoapods.org) bajo `AVOSCloudIM` o actualizar a una versión más nueva (por ejemplo, `pod 'AVOSCloudIM', '~> 12.3'`).

---

### Paso 6: Abrir el Workspace
1. Después de la instalación, se creará un archivo `.xcworkspace` en tu directorio de proyecto (por ejemplo, `NombreDeTuApp.xcworkspace`).
2. Abre este archivo en Xcode:
   ```bash
   open NombreDeTuApp.xcworkspace
   ```
   - A partir de ahora, siempre usa el archivo `.xcworkspace` en lugar del archivo `.xcodeproj` para trabajar con tu proyecto.

---

### Paso 7: Importar y Usar AVOSCloudIM en tu Código
1. En tus archivos Swift o Objective-C, importa el módulo `AVOSCloudIM`:
   - **Swift**:
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**:
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. Comienza a usar las características de la biblioteca. `AVOSCloudIM` es parte del SDK de LeanCloud, generalmente utilizado para mensajería en tiempo real. Consulta la [documentación de LeanCloud](https://leancloud.app/docs/) para ejemplos específicos de uso, como configurar un cliente de chat:
   - Ejemplo (Swift):
     ```swift
     let client = AVIMClient(clientId: "tuClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Conectado a LeanCloud IM!")
         } else {
             print("Error: \(error?.localizedDescription ?? "Desconocido")")
         }
     }
     ```

---

### Paso 8: Configurar tu Proyecto (si es necesario)
- **App Key e Inicialización**: Los SDKs de LeanCloud a menudo requieren un ID y clave de app. Agrega este código de inicialización (por ejemplo, en `AppDelegate`):
  - **Swift**:
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("tuAppID", clientKey: "tuAppKey")
        return true
    }
    ```
  - Reemplaza `"tuAppID"` y `"tuAppKey"` con las credenciales de tu cuenta de LeanCloud.
- **Permisos**: Asegúrate de que tu app tenga los permisos necesarios (por ejemplo, acceso a internet) en `Info.plist`:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### Notas
- **Especificidad de Versión**: Usar `pod 'AVOSCloudIM', '3.1.6.2'` te bloquea en esa versión exacta. Si deseas flexibilidad para actualizaciones menores, usa `~>` (por ejemplo, `pod 'AVOSCloudIM', '~> 3.1.6'` permite actualizaciones como 3.1.6.1 pero no 3.2).
- **Solución de Problemas**: Si `pod install` falla, intenta:
  - Actualizar CocoaPods: `sudo gem install cocoapods`
  - Limpiar la caché: `pod cache clean --all`
  - Ejecutar `pod repo update` para actualizar el repositorio local de especificaciones de CocoaPods.
- **SDK de LeanCloud**: Dado que `AVOSCloudIM` es parte de LeanCloud, asegúrate de seguir su guía de configuración para configuraciones adicionales (por ejemplo, registrarte en su plataforma).

---

¡Listo! Ahora has integrado `AVOSCloudIM` versión 3.1.6.2 en tu proyecto de iOS. Compila y ejecuta tu app en Xcode para probarla. ¡Hazme saber si necesitas ayuda con características específicas de LeanCloud!