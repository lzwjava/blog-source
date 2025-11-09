---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General del Sistema de Caché de CodeIgniter
translated: true
type: note
---

### Resumen de la Biblioteca de Caché de CodeIgniter

La clase `CI_Cache` de CodeIgniter es un sistema de caché flexible que proporciona una interfaz unificada para almacenar y recuperar datos a través de varios backends (como en memoria, basado en archivos o servicios externos). Extiende `CI_Driver_Library`, que carga los controladores dinámicamente. La clase abstrae las operaciones de caché, permitiendo a los desarrolladores cambiar de backend fácilmente mediante configuración sin cambiar el código de la aplicación. Todos los métodos delegan en el "adaptador" activo (una clase controlador), con soporte de respaldo para mayor confiabilidad.

El sistema enfatiza el rendimiento, la portabilidad y la tolerancia a fallos—por ejemplo, recurre por defecto a un controlador "dummy" (sin operación) si otros fallan, asegurando que la aplicación no se rompa debido a problemas de caché.

### Controladores y Adaptadores de Caché Soportados

La clase soporta varios controladores, definidos en `$valid_drivers`:
- **apc**: Utiliza APC (Alternative PHP Cache) de PHP para almacenamiento en memoria (rápido, integrado).
- **dummy**: Un marcador de posición que no hace nada (siempre retorna TRUE o FALSE); se utiliza como respaldo para desarrollo/pruebas.
- **file**: Almacena datos como archivos serializados en un directorio (especificado por `$_cache_path`), adecuado para sitios con poco tráfico.
- **memcached**: Interfaz con el servicio Memcached para caché en memoria distribuido (alto rendimiento, escalable).
- **redis**: Interfaz con Redis, otro almacén de clave-valor en memoria con características como pub/sub y operaciones atómicas.
- **wincache**: Específico de Windows para IIS (utiliza Microsoft WinCache).

Cada controlador es una clase separada (ej. `CI_Cache_memcached`) que implementa métodos como `get()`, `save()`, etc. La biblioteca carga el controlador dinámicamente basándose en el array `$config['adapter']` pasado al constructor.

### Inicialización y Configuración

- **Constructor**: Toma un array `$config` con claves para `adapter` (controlador principal), `backup` (controlador de respaldo) y `key_prefix` (cadena antepuesta a todas las claves de caché para namespacing/aislamiento).
  - Ejemplo de configuración: `array('adapter' => 'redis', 'backup' => 'file', 'key_prefix' => 'myapp_')`.
- **Lógica de Respaldo**: Después de la inicialización, verifica si el adaptador principal es compatible usando `is_supported($driver)` (que llama al método `is_supported()` del controlador, probando las extensiones o servicios de PHP requeridos).
  - Si el principal falla, cambia al controlador de respaldo. Si ambos fallan, registra un error y recurre por defecto a "dummy" (vía `log_message()`).
  - Esto asegura que la caché siempre tenga un adaptador funcional, evitando caídas.

La variable `$_cache_path` se establece para controladores basados en archivos, pero no se inicializa aquí—probablemente se maneja en la clase del controlador de archivos.

### Métodos Clave y Cómo Operan

Los métodos anteponen el `key_prefix` a los IDs para un alcance único (ej. `'myapp_user123'`) y delegan en el adaptador activo. Todas las operaciones retornan booleanos, arrays o datos mixtos en caso de éxito/fracaso.

- **get($id)**: Recupera datos en caché por ID.
  - Ejemplo: `$data = $cache->get('user_profile');` —llama al método `get()` del adaptador.
  - Si la clave existe y no ha expirado, retorna los datos; de lo contrario, retorna FALSE.
  - No hay aplicación directa de TTL aquí; es manejado por el controlador (ej., Redis o Memcached aplican TTL internamente).

- **save($id, $data, $ttl = 60, $raw = FALSE)**: Almacena datos con un tiempo de vida (TTL) en segundos.
  - Ejemplo: `$cache->save('user_profile', $profile_data, 3600);` —almacena con expiración de 1 hora.
  - La bandera `$raw` (falso por defecto) indica si los datos están serializados—los controladores manejan la serialización si es necesario (ej., los arrays/objetos se convierten en cadenas).
  - Retorna TRUE en caso de éxito, facilitando la lógica condicional (ej., generar y almacenar en caché si falla el guardado).

- **delete($id)**: Elimina un elemento específico de la caché.
  - Ejemplo: `$cache->delete('user_profile');` —eliminación permanente.

- **increment($id, $offset = 1)** y **decrement($id, $offset = 1)**: Operaciones atómicas para valores numéricos (útiles para contadores).
  - Ejemplo: `$new_counter = $cache->increment('hits', 5);` —incrementa en 5 si es soportado por el controlador (ej., Redis/Memcached son atómicos; los basados en archivos pueden simularlo).
  - No todos los controladores soportan raw/inc/dec (dummy siempre falla); retorna el nuevo valor o FALSE.

- **clean()**: Limpia todos los datos de la caché para el controlador actual.
  - Ejemplo: `$cache->clean();` —útil para purgar después de actualizaciones.
  - El tipo "user" se dirige a datos específicos del usuario, no a cachés del sistema.

- **cache_info($type = 'user')**: Retorna metadatos sobre la caché (ej., estadísticas del servidor, conteos de claves o rutas de archivos).
  - Ejemplo: `$info = $cache->cache_info();` —un array de detalles del controlador.

- **get_metadata($id)**: Obtiene detalles sobre un elemento específico en caché (ej., tiempo de expiración, tamaño).
  - Ejemplo: `$meta = $cache->get_metadata('key');` —ayuda a depurar u optimizar.

- **is_supported($driver)**: Verifica la disponibilidad del controlador (almacena en caché los resultados usando un array estático `$support` para evitar comprobaciones repetidas).

### Mecanismos Adicionales

- **Prefijo de Claves**: Se aplica automáticamente a todos los IDs (ej., para aislamiento de aplicaciones o multi-tenencia). Habilitado vía configuración para prevenir colisiones de claves entre entornos.
- **Registro**: Utiliza `log_message()` para mensajes de depuración/error (ej., respaldos), integrando con el sistema de registro de CodeIgniter.
- **Flexibilidad y Tolerancia a Fallos**: Al abstraer los backends, puedes cambiar de caché de archivos (económico, local) a Redis (rápido, distribuido) con cambios mínimos. El respaldo dummy significa que los fallos de caché no detienen la aplicación—los métodos simplemente retornan FALSE, permitiendo que el código proceda (ej., recuperar de la base de datos en su lugar).
- **Notas de Rendimiento**: Controladores como APC/Redis están en memoria (acceso rápido, submilisegundo). Los basados en archivos son más lentos debido a E/S de disco. Los TTL son generalmente obedecidos por los controladores excepto en raros casos específicos del controlador.

Este diseño hace que el almacenamiento en caché de CodeIgniter sea modular y confiable. Para detalles sobre controladores específicos, consulta los archivos del controlador (ej., `Cache_memcached.php`). Siempre consulta la documentación oficial de CodeIgniter para matices específicos de la versión, ya que este código es de una versión anterior (alrededor de 2.0-3.x). Si tienes en mente un método o controlador específico, ¡puedo profundizar más!