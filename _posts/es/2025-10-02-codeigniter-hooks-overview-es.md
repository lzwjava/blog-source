---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General de los Hooks de CodeIgniter
translated: true
type: note
---

### ¿Qué son los Hooks en CodeIgniter?

Los Hooks en CodeIgniter son una forma de extender la funcionalidad del framework sin modificar sus archivos principales. Te permiten ejecutar código personalizado en puntos específicos del ciclo de ejecución, como antes o después de cargar controladores, anular la salida o el caché. Esto preserva la capacidad de actualización al separar tu código de la base de código oficial.

Los Hooks se definen en `application/config/hooks.php` y se habilitan en `application/config/config.php` estableciendo `$config['enable_hooks'] = TRUE;`.

### Habilitar Hooks

1. Abre `application/config/config.php`.
2. Establece la variable de configuración:
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   Esto le indica a CodeIgniter que verifique y ejecute el archivo de hooks.

### Definir Hooks

Los Hooks se configuran como un array de arrays en `application/config/hooks.php`. Cada array de hook especifica:
- `class`: (Requerido) El nombre de la clase (debe coincidir con el nombre del archivo).
- `function`: (Requerido) El nombre del método en la clase.
- `filename`: (Requerido) El nombre del archivo de la clase (sin .php).
- `filepath`: (Opcional) La ruta de la carpeta al archivo, por defecto es `application/hooks/`.
- `params`: (Opcional) Un array de parámetros para pasar al método.

Coloca tus clases de hook en `application/hooks/`.

### Puntos de Hook

CodeIgniter proporciona estos puntos predefinidos donde los hooks pueden ejecutarse:
- **pre_system**: Se ejecuta antes de que se cargue el sistema (nada más ha sido ejecutado aún).
- **pre_controller**: Se ejecuta justo antes de que se llame al controlador.
- **post_controller_constructor**: Se ejecuta después de que el controlador es instanciado pero antes de que se ejecuten sus métodos.
- **post_controller**: Se ejecuta después de que el controlador termina.
- **display_override**: Se ejecuta en lugar de enviar la salida al navegador (anula el método _display del controlador).
- **cache_override**: Se ejecuta en lugar de cargar el caché (anula el método _display del caché).
- **post_system**: Se ejecuta después de que la página web es enviada completamente al navegador.

### Ejemplo de Uso

Supongamos que quieres registrar cada petición antes de que se ejecute el controlador. Crea un hook para `pre_controller`.

1. Crea el archivo `application/hooks/my_hook.php`:
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // Ejemplo: Registrar en un archivo o base de datos
           log_message('info', 'Controller about to be called: ' . $this->uri->uri_string());
       }
   }
   ```

2. En `application/config/hooks.php`, agrega:
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // Opcional, por defecto es application/hooks/
       'params' => array() // Parámetros opcionales
   );
   ```

Ahora, cada vez que un controlador esté a punto de ejecutarse, se ejecutará `log_request`.

### Mejores Prácticas
- Usa los hooks con moderación; si es posible, extiende controladores o usa librerías en su lugar.
- Siempre prueba los hooks en un entorno de desarrollo para asegurarte de que no interfieran con la lógica principal.
- Para más detalles, consulta la guía oficial del usuario de CodeIgniter sobre hooks.