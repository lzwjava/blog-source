---
audio: false
generated: true
lang: es
layout: post
title: Usando PopMenu en iOS
translated: true
---

Para usar `pod 'PopMenu', '2.4'` en tu proyecto de iOS, estás integrando la biblioteca PopMenu (versión 2.4) a través de CocoaPods, un popular gestor de dependencias para iOS. Esta biblioteca proporciona un menú de animación emergente inspirado en aplicaciones como Sina Weibo o NetEase. A continuación, se presentan los pasos para configurarlo y usarlo en tu proyecto:

---

### Paso 1: Instalar CocoaPods (si no está ya instalado)
Si no tienes CocoaPods instalado en tu sistema, instálalo primero:
1. Abre tu terminal.
2. Ejecuta este comando:
   ```bash
   sudo gem install cocoapods
   ```
3. Verifica la instalación:
   ```bash
   pod --version
   ```

---

### Paso 2: Configurar tu Podfile
1. Navega al directorio de tu proyecto de Xcode en el terminal:
   ```bash
   cd /ruta/a/tu/proyecto
   ```
2. Si aún no tienes un Podfile, créalo ejecutando:
   ```bash
   pod init
   ```
3. Abre el `Podfile` en un editor de texto (por ejemplo, `nano Podfile` o usa Xcode).
4. Añade las siguientes líneas para especificar el pod de PopMenu para tu objetivo:
   ```ruby
   platform :ios, '8.0'  # Ajusta la versión de iOS si es necesario
   target 'NombreDeTuApp' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - Reemplaza `NombreDeTuApp` con el nombre de tu objetivo de Xcode.
   - La línea `use_frameworks!` es requerida ya que PopMenu es probablemente una biblioteca basada en frameworks.

5. Guarda y cierra el Podfile.

---

### Paso 3: Instalar el Pod
1. En el terminal, ejecuta:
   ```bash
   pod install
   ```
2. Esto descarga e integra PopMenu versión 2.4 en tu proyecto. Espera hasta ver un mensaje como:
   ```
   Instalación de Pods completa! Hay X dependencias del Podfile y X pods totales instalados.
   ```
3. Cierra tu proyecto de Xcode si está abierto, luego abre el archivo `.xcworkspace` recién generado (por ejemplo, `NombreDeTuApp.xcworkspace`) en lugar del archivo `.xcodeproj`.

---

### Paso 4: Uso Básico en tu Código
PopMenu está escrito en Objective-C, por lo que deberás usarlo en consecuencia. Aquí tienes un ejemplo de cómo implementarlo en tu app:

1. **Importar la Biblioteca**:
   - En tu archivo Objective-C (por ejemplo, `ViewController.m`):
     ```objective-c
     #import "PopMenu.h"
     ```
   - Si estás usando Swift, crea un encabezado de puente:
     - Ve a `File > New > File > Header File` (por ejemplo, `NombreDeTuApp-Bridging-Header.h`).
     - Añade:
       ```objective-c
       #import "PopMenu.h"
       ```
     - En Xcode, establece el encabezado de puente bajo `Build Settings > Swift Compiler - General > Objective-C Bridging Header` a la ruta de tu archivo de encabezado (por ejemplo, `NombreDeTuApp/NombreDeTuApp-Bridging-Header.h`).

2. **Crear Elementos del Menú**:
   Define los elementos que deseas en el menú emergente. Cada elemento puede tener un título, icono y color de brillo.
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];

   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr"
                                               iconName:@"post_type_bubble_flickr"
                                              glowColor:[UIColor grayColor]
                                                  index:0];
   [items addObject:menuItem1];

   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter"
                                               iconName:@"post_type_bubble_twitter"
                                              glowColor:[UIColor blueColor]
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **Inicializar y Mostrar el Menú**:
   Crea una instancia de `PopMenu` y muéstrala en tu vista.
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // Opciones: kPopMenuAnimationTypeSina o kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // Número de elementos por fila
   [popMenu showMenuAtView:self.view];
   ```

4. **Manejar la Selección (Opcional)**:
   Puedes subclasificar o extender la funcionalidad para detectar toques, aunque la versión básica de PopMenu (circa 2.4) puede que no soporte un delegado de forma nativa. Verifica la documentación de la biblioteca en GitHub (`xhzengAIB/PopMenu`) para cualquier actualización o personalización.

---

### Paso 5: Ejecutar tu Proyecto
Compila y ejecuta tu proyecto (`Cmd + R`) en Xcode. Si los iconos (por ejemplo, `post_type_bubble_flickr`) son parte de tu catálogo de activos, asegúrate de que estén añadidos a tu proyecto. Si no, necesitarás obtenerlos o crearlos.

---

### Notas
- **Especificidad de Versión**: `pod 'PopMenu', '2.4'` te bloquea en la versión 2.4. Si deseas la última versión, usa `pod 'PopMenu'` sin un número de versión, pero esto podría introducir cambios de ruptura.
- **Compatibilidad**: Asegúrate de que el objetivo de implementación de tu proyecto sea al menos iOS 8.0 (o ajusta la `platform` en el Podfile).
- **Personalización**: PopMenu permite ajustes de tipo de animación y diseño (por ejemplo, `perRowItemCount`). Explora el código fuente para más opciones.
- **Solución de Problemas**: Si encuentras errores como “archivo no encontrado”, asegúrate de que tus Pods estén correctamente instalados y que estés utilizando el workspace.

¡Esto debería ayudarte a comenzar con PopMenu 2.4 en tu app de iOS! Déjame saber si necesitas más aclaraciones.