---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General de la Configuración de la Base de Datos de CodeIgniter
translated: true
type: note
---

### Resumen de la Configuración de Base de Datos de CodeIgniter

Este archivo PHP es un script de configuración para la conectividad de base de datos de CodeIgniter. Define ajustes de conexión para varios grupos de base de datos (por ejemplo, 'default', 'lzwjava', 'leo66', 'testing'), permitiendo que la aplicación cambie entre ellos según el entorno (desarrollo, testing, producción). La variable `$active_group` determina qué grupo de conexión se utiliza por defecto.

Componentes clave:
- **$query_builder**: Se establece en `TRUE` para habilitar la carga de la clase Query Builder, que proporciona una forma orientada a objetos para construir consultas SQL.
- **$db[][]**: Un array asociativo donde cada sub-array (por ejemplo, 'default') contiene opciones de configuración detalladas para una conexión de base de datos.

El `$active_group` se establece dinámicamente basado en la constante `ENVIRONMENT` (por ejemplo, mediante una sentencia switch), asegurando diferentes ajustes para distintas etapas de despliegue. A continuación, explicaré cada opción de configuración en detalle, basándome en la documentación de CodeIgniter y el uso estándar. Tenga en cuenta que los valores sensibles reales (como credenciales) se omiten aquí por seguridad; en la práctica, estos deben almacenarse de forma segura, por ejemplo, mediante variables de entorno.

### Opciones de Configuración Detalladas

Cada grupo de base de datos es un array con las siguientes claves. La mayoría son ajustes sencillos, pero algunos (como `encrypt`) admiten sub-opciones para características avanzadas.

- **dsn** (string): El nombre completo de la fuente de datos (DSN) que describe la conexión. Esta es una alternativa a especificar hostname, username, etc., por separado. Es útil para configuraciones complejas como ODBC. Si se proporciona, anula los campos individuales de host/credenciales. Formato de ejemplo: `'dsn' => 'mysql:host=tuhost;dbname=tubasededatos'`.

- **hostname** (string): La dirección del servidor de base de datos (por ejemplo, 'localhost' o una IP como '127.0.0.1'). Identifica dónde se ejecuta la base de datos, permitiendo conexiones a través de TCP/IP o sockets.

- **username** (string): El nombre de la cuenta utilizada para autenticarse con el servidor de base de datos. Debe coincidir con un usuario válido en el sistema de gestión de base de datos.

- **password** (string): La clave secreta asociada con el nombre de usuario para la autenticación. Siempre almacene esto de forma segura para prevenir su exposición.

- **database** (string): El nombre específico de la base de datos a la que desea conectarse en el servidor. Todas las consultas se dirigirán a esta base de datos a menos que se especifique lo contrario.

- **dbdriver** (string): Especifica el controlador de base de datos a usar (por ejemplo, 'mysqli' para MySQL). Los controladores comunes incluyen 'cubrid', 'ibase', 'mssql', 'mysql', 'mysqli', 'oci8', 'odbc', 'pdo', 'postgre', 'sqlite', 'sqlite3', y 'sqlsrv'. 'mysqli' es una opción moderna y segura para MySQL.

- **dbprefix** (string): Un prefijo opcional añadido a los nombres de las tablas cuando se usa el Query Builder de CodeIgniter (por ejemplo, si se establece en 'prefix_', 'mitabla' se convierte en 'prefix_mitabla'). Esto ayuda a poner nombres a las tablas en hosting compartido o aplicaciones multi-tenant.

- **pconnect** (boolean): Habilita conexiones persistentes (`TRUE`) o conexiones regulares (`FALSE`). Las conexiones persistentes reutilizan el mismo enlace, mejorando el rendimiento para aplicaciones de alta carga, pero pueden agotar los recursos del servidor si se usan en exceso.

- **db_debug** (boolean): Controla si los errores de base de datos se muestran (`TRUE`) para depuración. Desactive (`FALSE`) en producción para evitar filtrar detalles sensibles de error a los usuarios.

- **cache_on** (boolean): Habilita (`TRUE`) o deshabilita (`FALSE`) el cacheo de consultas. Cuando está habilitado, los resultados se almacenan para acelerar consultas repetidas.

- **cachedir** (string): Ruta del directorio donde se almacenan los resultados de consultas cacheadas. Debe tener permisos de escritura para el servidor web. Combinado con `cache_on`, esto reduce la carga de la base de datos.

- **char_set** (string): La codificación de caracteres para la comunicación con la base de datos (por ejemplo, 'utf8mb4' para soporte Unicode moderno). Asegura la integridad de los datos para aplicaciones multi-idioma.

- **dbcollat** (string): La collation para ordenar y comparar caracteres (por ejemplo, 'utf8mb4_unicode_ci' para Unicode que no distingue entre mayúsculas y minúsculas). Funciona como un respaldo para PHP/MySQL antiguos; se ignora en otros casos.

- **swap_pre** (string): Un prefijo de tabla para reemplazar `dbprefix` dinámicamente. Útil para intercambiar prefijos en aplicaciones existentes sin renombrar tablas.

- **encrypt** (boolean o array): Para soporte de encriptación. Para 'mysql' (obsoleto), 'sqlsrv', y 'pdo/sqlsrv', use `TRUE`/`FALSE` para habilitar/deshabilitar SSL. Para 'mysqli' y 'pdo/mysql', use un array con sub-opciones SSL:
  - 'ssl_key': Ruta al archivo de clave privada (por ejemplo, para certificados de cliente).
  - 'ssl_cert': Ruta al archivo de certificado de clave pública.
  - 'ssl_ca': Ruta al archivo de la autoridad certificadora (valida el certificado del servidor).
  - 'ssl_capath': Ruta a un directorio de certificados CA confiables en formato PEM.
  - 'ssl_cipher': Lista separada por dos puntos de cifrados permitidos (por ejemplo, 'AES128-SHA').
  - 'ssl_verify': Solo para 'mysqli'; `TRUE` para verificar certificados del servidor, `FALSE` para omitir (menos seguro; usar para certificados auto-firmados).

- **compress** (boolean): Habilita la compresión del lado del cliente para conexiones MySQL, reduciendo el tráfico de red (solo MySQL; ignorado por otros controladores).

- **stricton** (boolean): Fuerza conexiones en 'Modo Estricto' (`TRUE`), que aplica reglas SQL estrictas para detectar errores temprano (por ejemplo, tipos de datos no válidos). Útil durante el desarrollo.

- **ssl_options** (array): Opciones de configuración SSL avanzadas para controladores como 'pdo'. Permite ajustar finamente parámetros de encriptación no cubiertos por `encrypt`.

- **failover** (array): Array de conexión de respaldo para conmutación automática si la conexión principal falla. Cada elemento refleja la configuración principal (por ejemplo, hostname/puerto alternativo). Ejemplo: `array(array('hostname' => 'hostderespaldo', ...))`.

- **save_queries** (boolean): Guarda las consultas ejecutadas en memoria para depuración (`TRUE`). Proporciona acceso a métodos como `$this->db->last_query()` pero puede aumentar el uso de memoria; desactive (`FALSE`) en producción para ahorrar recursos.

### Grupos de Base de Datos y Cambio de Entorno

- **default**: El array de configuración base, que sirve como plantilla. Está configurado con valores por defecto de 'producción' (por ejemplo, sin depuración, ajustes seguros).
- **lzwjava**: Hereda de la base pero anula el nombre de usuario a un valor diferente (contraseña en blanco, lo que implica sin autenticación o por defecto).
- **leo66**: Hereda los ajustes base pero cambia el hostname al bucle local, username/password a los valores por defecto, y añade un puerto (3306, estándar para MySQL).
- **testing**: Un grupo dedicado para entornos de prueba; hereda la configuración base.

La sentencia `switch` activa el grupo apropiado basado en `ENVIRONMENT`:
- Desarrollo: Usa 'lzwjava'.
- Testing: Usa 'testing'.
- Producción: Usa 'default'.

Esta configuración promueve la flexibilidad para el desarrollo local, testing y despliegues en vivo. Siempre sanie las entradas para prevenir inyección SQL, y considere mover las credenciales a variables de entorno por seguridad. Para la documentación completa, consulte la Guía de Usuario oficial de CodeIgniter sobre conexiones de base de datos. Si tiene una opción o grupo específico para aclarar, ¡avíseme!