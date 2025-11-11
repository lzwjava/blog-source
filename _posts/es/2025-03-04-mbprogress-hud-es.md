---
audio: false
generated: true
lang: es
layout: post
title: Uso de MBProgressHUD en iOS
translated: true
type: note
---

Parece que estás preguntando sobre cómo usar la librería `MBProgressHUD` en un proyecto de iOS, específicamente la versión `0.9.1`, a través de un Podfile en CocoaPods. Permíteme guiarte a través del proceso paso a paso.

### ¿Qué es MBProgressHUD?
`MBProgressHUD` es una librería de terceros popular para iOS que proporciona una manera fácil de mostrar un HUD (Heads-Up Display) con indicadores de actividad, barras de progreso o vistas personalizadas, típicamente usado para mostrar estados de carga o mensajes breves.

### Pasos para Usar `pod 'MBProgressHUD', '0.9.1'`

#### 1. **Instalar CocoaPods (si aún no está instalado)**
CocoaPods es un gestor de dependencias para proyectos de iOS. Si no lo tienes instalado, ejecuta este comando en tu terminal:
```bash
sudo gem install cocoapods
```

#### 2. **Configurar un Podfile**
- Navega al directorio de tu proyecto de Xcode en la terminal:
  ```bash
  cd /ruta/a/tu/proyecto
  ```
- Si aún no tienes un Podfile, crea uno ejecutando:
  ```bash
  pod init
  ```
- Abre el `Podfile` en un editor de texto (por ejemplo, `nano Podfile` o `open Podfile`).

#### 3. **Agregar MBProgressHUD a Tu Podfile**
En tu `Podfile`, agrega la línea para `MBProgressHUD` versión `0.9.1` dentro del bloque target para tu aplicación. Debería verse algo así:
```ruby
platform :ios, '9.0'  # Especifica tu deployment target

target 'TuNombreDeApp' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- Reemplaza `'TuNombreDeApp'` con el nombre real de tu target de Xcode.
- La línea `platform :ios, '9.0'` establece la versión mínima de iOS; ajústala según las necesidades de tu proyecto.

#### 4. **Instalar el Pod**
- Guarda el `Podfile` y ejecuta este comando en la terminal:
  ```bash
  pod install
  ```
- Esto descarga e integra `MBProgressHUD` versión `0.9.1` en tu proyecto. Si es exitoso, verás una salida confirmando la instalación.

#### 5. **Abrir el Workspace**
- Después de la instalación, cierra tu proyecto de Xcode (si está abierto) y abre el archivo `.xcworkspace` recién creado (por ejemplo, `TuNombreDeApp.xcworkspace`) en lugar del archivo `.xcodeproj`. CocoaPods genera este workspace para gestionar las dependencias.

#### 6. **Usar MBProgressHUD en Tu Código**
- **Swift**: Importa el módulo y úsalo en tu código:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // Mostrar un HUD simple con un indicador de carga
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Cargando..."
          
          // Ocultarlo después de un tiempo (ej. 2 segundos)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: Importa el header y úsalo:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // Mostrar un HUD simple con un indicador de carga
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Cargando...";
      
      // Ocultarlo después de un tiempo (ej. 2 segundos)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **Características Comunes de MBProgressHUD**
- **HUD Básico**: Como se mostró arriba, muestra un indicador giratorio con texto opcional.
- **Solo Texto Personalizado**:
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
- **Versión 0.9.1**: Esta es una versión antigua (publicada alrededor de 2015). La última versión a partir de marzo de 2025 es mucho más nueva (ej. 1.2.0 o superior). Para usar la más reciente, simplemente escribe `pod 'MBProgressHUD'` sin un número de versión. Considera actualizar a menos que necesites específicamente la 0.9.1 por compatibilidad.
- **Documentación**: Consulta la [página de GitHub de MBProgressHUD](https://github.com/jdg/MBProgressHUD) para más opciones y ejemplos. La versión 0.9.1 podría tener menos características que las versiones modernas.

¡Avísame si necesitas ayuda para solucionar problemas o ejemplos más específicos!