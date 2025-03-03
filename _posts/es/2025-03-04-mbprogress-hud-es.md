---
audio: false
generated: true
lang: es
layout: post
title: Usando MBProgressHUD en iOS
translated: true
---

Parece que estás preguntando cómo usar la biblioteca `MBProgressHUD` en un proyecto de iOS, específicamente la versión `0.9.1`, a través de un Podfile en CocoaPods. Déjame guiarte a través del proceso paso a paso.

### ¿Qué es MBProgressHUD?
`MBProgressHUD` es una popular biblioteca de terceros para iOS que proporciona una manera fácil de mostrar una HUD (Heads-Up Display) con indicadores de actividad, barras de progreso o vistas personalizadas, generalmente utilizadas para mostrar estados de carga o mensajes breves.

### Pasos para usar `pod 'MBProgressHUD', '0.9.1'`

#### 1. **Instalar CocoaPods (si no está instalado)**
CocoaPods es un gestor de dependencias para proyectos de iOS. Si no lo tienes instalado, ejecuta este comando en tu terminal:
```bash
sudo gem install cocoapods
```

#### 2. **Configurar un Podfile**
- Navega al directorio de tu proyecto de Xcode en la terminal:
  ```bash
  cd /ruta/a/tu/proyecto
  ```
- Si aún no tienes un Podfile, créalo ejecutando:
  ```bash
  pod init
  ```
- Abre el `Podfile` en un editor de texto (por ejemplo, `nano Podfile` o `open Podfile`).

#### 3. **Agregar MBProgressHUD a tu Podfile**
En tu `Podfile`, agrega la línea para `MBProgressHUD` versión `0.9.1` dentro del bloque de destino para tu app. Debería verse algo así:
```ruby
platform :ios, '9.0'  # Especifica tu objetivo de implementación

target 'NombreDeTuApp' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Reemplaza `'NombreDeTuApp'` con el nombre real de tu destino de Xcode.
- La línea `platform :ios, '9.0'` establece la versión mínima de iOS; ajústala según las necesidades de tu proyecto.

#### 4. **Instalar el Pod**
- Guarda el `Podfile` y ejecuta este comando en la terminal:
  ```bash
  pod install
  ```
- Esto descarga e integra `MBProgressHUD` versión `0.9.1` en tu proyecto. Si es exitoso, verás una salida confirmando la instalación.

#### 5. **Abrir el Workspace**
- Después de la instalación, cierra tu proyecto de Xcode (si está abierto) y abre el nuevo archivo `.xcworkspace` creado (por ejemplo, `NombreDeTuApp.xcworkspace`) en lugar del archivo `.xcodeproj`. CocoaPods genera este workspace para gestionar las dependencias.

#### 6. **Usar MBProgressHUD en tu Código**
- **Swift**: Importa el módulo y úsalo en tu código:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // Muestra una HUD simple con un indicador de carga
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Cargando..."

          // Ocúltalo después de algún tiempo (por ejemplo, 2 segundos)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: Importa el encabezado y úsalo:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // Muestra una HUD simple con un indicador de carga
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Cargando...";

      // Ocúltalo después de algún tiempo (por ejemplo, 2 segundos)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Características Comunes de MBProgressHUD**
- **HUD Básica**: Como se mostró anteriormente, muestra un indicador giratorio con texto opcional.
- **Texto Personalizado Solo**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "¡Hecho!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **Barra de Progreso**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% de progreso
  ```

#### Notas
- **Versión 0.9.1**: Esta es una versión antigua (publicada alrededor de 2015). La versión más reciente hasta marzo de 2025 es mucho más nueva (por ejemplo, 1.2.0 o superior). Para usar la más reciente, simplemente escribe `pod 'MBProgressHUD'` sin un número de versión. Considera actualizar a menos que necesites específicamente la 0.9.1 por compatibilidad.
- **Documentación**: Consulta la [página de GitHub de MBProgressHUD](https://github.com/jdg/MBProgressHUD) para más opciones y ejemplos. La versión 0.9.1 puede tener menos características que los lanzamientos modernos.

Hazme saber si necesitas ayuda para solucionar problemas o ejemplos más específicos.