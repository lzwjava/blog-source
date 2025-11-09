---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Configuración de API REST de CodeIgniter
translated: true
type: note
---

A continuación, proporcionaré una guía clara y paso a paso para comprender y utilizar el archivo de configuración de la API REST de CodeIgniter que compartiste (`application/config/rest.php`). Este archivo configura el comportamiento de la biblioteca REST_Controller (una biblioteca PHP popular para construir APIs RESTful en CodeIgniter), como la biblioteca REST de Phil Sturgeon (ahora mantenida como parte del framework CodeIgniter en algunas versiones).

Explicaré:
- Qué hace la biblioteca y los requisitos previos clave.
- Cómo configurarla y usarla.
- Opciones clave de configuración de tu archivo (con ejemplos).
- Un ejemplo de uso simple.
- Consejos para errores comunes y seguridad.

Si tu pregunta es específicamente sobre un aspecto (por ejemplo, autenticación o límites), ¡no dudes en aclararlo para obtener un consejo más dirigido!

### 1. **Requisitos Previos y Configuración**
   - **¿Qué es?** Esta es la biblioteca REST_Controller para CodeIgniter (un framework PHP). Te permite construir APIs RESTful (por ejemplo, endpoints que responden en JSON/XML en solicitudes GET/POST) extendiendo tus controladores desde `REST_Controller`. Tu archivo de configuración controla ajustes globales como autenticación, formatos de respuesta, límite de tasa y seguridad.

   - **Requisitos:**
     - CodeIgniter 3.x (o versión compatible; esta configuración es para versiones antiguas alrededor de la 3.x).
     - Instala la biblioteca REST_Controller si aún no está en tu instalación de CodeIgniter (puedes descargarla de GitHub: `chriskacerguis/codeigniter-restserver`). Coloca los archivos de la biblioteca en `application/libraries/` y cárgala automáticamente en `application/config/autoload.php`:
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - Configuración de la base de datos (opcional; necesaria para funciones como claves API, registro o límites). Ejecuta los esquemas SQL proporcionados en los comentarios de la configuración (por ejemplo, para tablas como `keys`, `logs`, `access`, `limits`).
     - Habilita URLs amigables en CodeIgniter (`application/config/routes.php`) para endpoints de API limpios como `/api/users`.
     - Tu archivo de configuración `rest.php` debe colocarse en `application/config/` y cargarse automáticamente en `application/config/autoload.php`:
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **Pasos Básicos de Instalación:**
     1. Descarga y descomprime CodeIgniter.
     2. Agrega los archivos de la biblioteca REST_Controller.
     3. Copia tu `rest.php` proporcionado a `application/config/`.
     4. Configura las rutas en `routes.php` (por ejemplo, `$route['api/(:any)'] = 'api/$1';` para mapear `/api/users` a un controlador).
     5. Crea controladores de API (ver ejemplo a continuación).
     6. Prueba con una herramienta como Postman o curl.

### 2. **Opciones Clave de Configuración**
Resumiré los ajustes principales de tu archivo de configuración, agrupados por propósito. Estos controlan el comportamiento global. Puedes modificarlos para adaptarlos a tus necesidades (por ejemplo, habilitar HTTPS o cambiar formatos predeterminados).

- **Protocolo y Salida:**
  - `$config['force_https'] = FALSE;`: Fuerza que todas las llamadas a la API usen HTTPS. Establece en `TRUE` para seguridad en producción.
  - `$config['rest_default_format'] = 'json';`: Formato de respuesta predeterminado (opciones: json, xml, csv, etc.). Las solicitudes pueden anularlo mediante URL (por ejemplo, `/api/users.format=xml`).
  - `$config['rest_supported_formats']`: Lista de formatos permitidos. Elimina los no deseados por seguridad.
  - `$config['rest_ignore_http_accept'] = FALSE;`: Ignora las cabeceras HTTP Accept del cliente para acelerar las respuestas (útil si siempre usas `$this->rest_format` en el código).

- **Autenticación (Seguridad):**
  - `$config['rest_auth'] = FALSE;`: Modo principal de autenticación. Opciones:
    - `FALSE`: No se requiere autenticación.
    - `'basic'`: Autenticación HTTP Basic (usuario/contraseña en cabeceras base64).
    - `'digest'`: Autenticación digest más segura.
    - `'session'`: Verifica una variable de sesión PHP.
  - `$config['auth_source'] = 'ldap';`: Dónde verificar las credenciales (por ejemplo, array de configuración, LDAP, biblioteca personalizada).
  - `$config['rest_valid_logins'] = ['admin' => '1234'];`: Array simple de usuario/contraseña (ignorado si se usa LDAP).
  - `$config['auth_override_class_method']`: Anula la autenticación para controladores/métodos específicos (por ejemplo, `'users' => 'view' => 'basic'`).
  - `$config['auth_library_class/function']`: Si usas una biblioteca personalizada, especifica la clase/método para la validación.
  - Controles de IP:
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']`: Filtrado de IP base en tu API.
    - Útil para restringir el acceso (por ejemplo, lista blanca de las IPs de tu aplicación).

- **Claves API (Capa de Seguridad Opcional):**
  - `$config['rest_enable_keys'] = FALSE;`: Habilita la verificación de claves API (almacenadas en la tabla de BD `keys`). Los clientes deben enviar claves en las cabeceras (por ejemplo, `X-API-KEY`).
  - `$config['rest_key_column/name/length']`: Personaliza los campos de la clave y el nombre de la cabecera.
  - Combínalo con `$config['rest_enable_access']` para restringir claves a controladores/métodos específicos.

- **Registro y Límites:**
  - `$config['rest_enable_logging/limits'] = FALSE;`: Habilita el registro en BD de las solicitudes (URI, parámetros, etc.) o la limitación de tasa (por ejemplo, X llamadas por hora por clave).
  - Tablas: `logs`, `limits` (ejecuta el SQL en los comentarios para crearlas).
  - `$config['rest_limits_method']`: Cómo aplicar los límites (por clave API, URL, etc.).
  - Personaliza por método en los controladores (por ejemplo, `$this->method['get']['limit'] = 100;`).

- **Otros:**
  - `$config['rest_ajax_only'] = FALSE;`: Restringe solo a solicitudes AJAX (de lo contrario, devuelve error 505).
  - `$config['rest_language'] = 'english';`: Idioma para los mensajes de error.

Para modificar: Edita `rest.php` y reinicia tu aplicación. ¡Prueba los cambios cuidadosamente!

### 3. **Cómo Usarlo: Uso Paso a Paso**
Una vez configurado, crea endpoints de API construyendo controladores que extiendan `REST_Controller`. Aquí hay un proceso de alto nivel:

1. **Crea un Controlador:**
   - En `application/controllers/`, crea `Api.php` (o por ejemplo, `Users.php` para un recurso específico):
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // Opcional: Establece autenticación, límites por método
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 solicitudes/hora
         }

         // GET /api
         public function index_get() {
             $data = ['message' => 'Bienvenido a la API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // Obtiene datos POST
             if (empty($data['name'])) {
                 $this->response(['error' => 'Nombre requerido'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // Procesa (por ejemplo, inserta en la BD)
             $this->response(['message' => 'Usuario creado'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // Obtiene datos PUT
             // Actualiza el usuario con $id
             $this->response(['message' => 'Usuario actualizado'], REST_Controller::HTTP_OK);
         }

         // etc. para DELETE
     }
     ```

2. **Envía Solicitudes:**
   - Usa cualquier cliente HTTP:
     - GET: `curl http://tudominio.com/api` → Devuelve JSON {"message": "Bienvenido a la API", "status": "success"}
     - POST: `curl -X POST http://tudominio.com/api/users -d "name=John"` → Crea un usuario.
   - Incluye cabeceras si usas autenticación/claves (por ejemplo, `Authorization: Basic base64(usuario:pass)` o `X-API-KEY: tuclave`).

3. **Prueba y Depura:**
   - Revisa los registros de CodeIgniter para ver errores.
   - Si la autenticación falla, asegúrate de que las credenciales estén establecidas correctamente.
   - Para límites/registro, consulta tus tablas de BD.

### 4. **Consejos Comunes y Mejores Prácticas**
- **Seguridad:** Usa siempre HTTPS en producción (`force_https = TRUE`). Habilita claves si se expone a clientes externos. Sanitiza las entradas para prevenir inyección SQL.
- **Errores:** Las respuestas incluyen campos `status` y `error` (personalizables en la configuración). Usa el perfilador de CodeIgniter para depurar.
- **Rendimiento:** Si el registro/límites están habilitados, tu BD manejará las consultas—monitorea el rendimiento lento.
- **Actualización:** Esta configuración es para versiones antiguas de CodeIgniter. Para CI 4, usa sus recursos de API integrados (esta configuración puede necesitar ajustes).
- **Solución de Problemas:**
  - "¿Sin respuesta?" Verifica rutas, carga automática y rutas de biblioteca.
  - ¿Problemas de autenticación? Verifica `$auth_source` y las credenciales.
  - ¿Errores de formato? Asegúrate de que tu formato esté en `rest_supported_formats`.
- **Recursos:** Documentación en codeigniter-restserver.org. Para migración a CI4, consulta la documentación oficial.

Si esto no responde a tu pregunta exacta o necesitas código para un caso de uso específico (por ejemplo, habilitar OAuth), ¡proporciona más detalles!