---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter Migraciones Gestión del Esquema de Base de Datos
translated: true
type: note
---

### ¿Qué son las Migraciones de CodeIgniter?

Las migraciones de CodeIgniter (CI) son una función que ayuda a gestionar los cambios en el esquema de la base de datos de manera controlada por versiones, similar a herramientas como Flyway o Liquibase. Te permiten escribir scripts PHP que definen alteraciones de la base de datos (por ejemplo, crear tablas, agregar columnas o modificar datos), y luego ejecutarlos en secuencia para mantener tu esquema actualizado en todos los entornos. Esto previene errores manuales con SQL y permite revertir cambios.

Las migraciones funcionan mediante:
- Almacenar archivos de migración en un directorio (por defecto: `application/migrations/`).
- Rastrear "versiones" en una tabla de la base de datos para saber qué migraciones se han aplicado.
- Ejecutar scripts hacia adelante (up) o hacia atrás (down) según tus necesidades.

El archivo de configuración que compartiste (`migration.php`) controla cómo se comportan las migraciones. Utiliza arrays de PHP para establecer opciones. A continuación, explicaré las configuraciones clave con ejemplos.

### Configuraciones Clave

| Configuración | Valor en Tu Código | Explicación | Cómo Funciona |
|---------|---------------------|-------------|-------------|
| `migration_enabled` | `FALSE` | Habilita o deshabilita las migraciones globalmente. Cuando es `FALSE`, no puedes ejecutar migraciones (por seguridad, ya que modifican la BD). | CI verifica esto antes de ejecutar cualquier comando de migración. Establécelo en `TRUE` durante el desarrollo, y luego vuelve a `FALSE` en producción. Ejemplo: Si está habilitado, ejecutar mediante `$this->migration->current()` en un controlador. |
| `migration_type` | `'timestamp'` | Estilo de nomenclatura de archivos: `'sequential'` (ej., `001_add_blog.php`) o `'timestamp'` (ej., `20121031104401_add_blog.php`). Se recomienda Timestamp para un mejor control de versiones. | Los archivos se cargan en orden cronológico. Timestamp utiliza el formato `AAAAMMDDHHMMSS` (ej., `20121031104401` para el 31 de Oct de 2012, 10:44:01). |
| `migration_table` | `'migrations'` | Nombre de la tabla de la BD que rastrea las migraciones aplicadas. Requerido. | CI crea esta tabla si no existe. Almacena la última versión de migración aplicada. Borrar o actualizar esta tabla reinicia el historial de migraciones. |
| `migration_auto_latest` | `FALSE` | Si es `TRUE` y `migration_enabled` es `TRUE`, ejecuta automáticamente las migraciones a la última versión cuando se carga la librería Migration (ej., al cargar la página). | Útil en entornos de desarrollo para sincronizar esquemas automáticamente. Establécelo en `FALSE` para ejecutar migraciones manualmente y tener más control (más seguro en prod). |
| `migration_version` | `0` | La versión/objetivo a la que migrar. Se establece con el prefijo del nombre de archivo (ej., `20121031104401`). `0` significa que no se han aplicado migraciones. | Ejecutar `$this->migration->version(20121031104401)` migra hasta ese punto. Se usa para reversiones específicas—los números negativos deshacen migraciones. |
| `migration_path` | `APPPATH.'migrations/'` | Directorio donde se almacenan los archivos de migración. `APPPATH` es una constante de CI que apunta a `application/`. | CI escanea esta carpeta en busca de archivos PHP que coincidan con la convención de nomenclatura. Debe tener permisos de escritura para el servidor web. Son posibles rutas personalizadas como `BASEPATH.'custom/migrations/'`. |

### Cómo Usar las Migraciones (Paso a Paso)

1. **Habilitar Migraciones**: Establece temporalmente `$config['migration_enabled'] = TRUE;` en el archivo de configuración.

2. **Crear un Archivo de Migración**: Agrega un archivo PHP en `application/migrations/` con un nombre como `20121031104401_add_blog.php`. Dentro, usa la clase Migration de CI:
   ```php
   defined('BASEPATH') OR exit('No direct script access allowed');

   class Migration_Add_blog extends CI_Migration {
       public function up() {
           $this->dbforge->add_field('id');
           $this->dbforge->create_table('blogs');
       }

       public function down() {
           $this->dbforge->drop_table('blogs');
       }
   }
   ```
   - `up()` aplica los cambios (ej., crear tabla).
   - `down()` los revierte (ej., eliminar tabla).

3. **Ejecutar Migraciones**:
   - Carga la librería: `$this->load->library('migration');`
   - A la última: `$this->migration->current();`
   - A una específica: `$this->migration->version('20121031104401');`
   - Desde la línea de comandos (si CLI está habilitado): `php index.php migrate current`

4. **Comandos Comunes**:
   - `$this->migration->latest()`: Alias para `current()`.
   - `$this->migration->find_migratables()`: Lista los archivos disponibles.
   Los errores se registran en los archivos de log de CI o lanzan excepciones.

5. **Mejores Prácticas**:
   - Mantén las migraciones idempotentes (que sean seguras de volver a ejecutar).
   - Prueba primero en desarrollo; evita habilitar la migración automática en producción para prevenir cambios accidentales en el esquema.
   - Usa transacciones si tu BD las soporta para cambios atómicos.
   - Deshabilita después de usar: Vuelve a establecer en `FALSE` por seguridad.

Si encuentras problemas (ej., permisos en la ruta), revisa los logs o la documentación de CI en [codeigniter.com/user_guide/libraries/migration.html](https://codeigniter.com/user_guide/libraries/migration.html). ¡Especifica tu versión de CI para un consejo más específico!