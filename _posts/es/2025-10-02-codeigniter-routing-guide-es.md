---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Enrutamiento de CodeIgniter
translated: true
type: note
---

### Descripción General del Enrutamiento en CodeIgniter

El sistema de enrutamiento de CodeIgniter te permite asignar URLs (URIs) a clases y métodos de controlador específicos, anulando el patrón de URL predeterminado de `example.com/controlador/metodo/id/`. Esto es útil para crear URLs amigables para SEO, manejar APIs RESTful o simplemente personalizar cómo se procesan las solicitudes.

El fragmento de código proviene del archivo de configuración `routes.php` de CodeIgniter. Define un array asociativo `$route` donde cada clave es un patrón de URI y el valor es una cadena (`controlador/metodo`) o un array que especifica comportamientos diferentes por método HTTP (por ejemplo, GET, POST). Esta configuración admite tanto el enrutamiento estándar como el enrutamiento específico por método.

Desglosaré **cómo se definen las rutas**, **cómo funcionan** y **cómo usarlas**, basándome en el comportamiento estándar de CodeIgniter y el ejemplo de tu código. Para obtener detalles completos, consulta la Guía del Usuario oficial de CodeIgniter sobre enrutamiento: https://codeigniter.com/userguide4/general/routing.html.

#### 1. **Cómo Definir Rutas**

Las rutas se definen en `application/config/routes.php` como un array. Añades entradas a `$route[]`. Aquí está la sintaxis:

- **Ruta Básica**: Asigna cualquier método HTTP a un controlador/método.
  ```
  $route['segmento_uri'] = 'controlador/metodo';
  ```
  - Ejemplo: `$route['login'] = 'users/login';` significa que cualquier solicitud a `/login` se dirige a `Users::login()`.

- **Ruta Específica por Método**: Para APIs RESTful, puedes especificar diferentes controladores/métodos por método HTTP (GET, POST, PUT, etc.). Esto utiliza un array.
  ```
  $route['segmento_uri'] = array(
      'METHOD1' => 'controlador/metodo1',
      'METHOD2' => 'controlador/metodo2'
  );
  ```
  - Ejemplo de tu código: `$route['self'] = array('POST' => 'users/update', 'GET' => 'users/self');` significa:
    - POST a `/self` → `Users::update()`.
    - GET a `/self` → `Users::self()`.

- **Comodines (Placeholders)**: Usa patrones similares a regex para capturar partes dinámicas de la URL (que se pasan como parámetros al método).
  - `(:any)`: Coincide con cualquier carácter (excepto barras) – por ejemplo, slugs o cadenas.
  - `(:num)` o `(\d+)`: Coincide solo con dígitos – para IDs.
  - Regex personalizado: Envuelve entre paréntesis, por ejemplo, `(foo|bar)` para coincidencias específicas.
  - Ejemplos de tu código:
    - `$route['users/(\d+)']['GET'] = 'users/one/$1';`: GET `/users/123` dirige a `Users::one(123)`.
    - `$route['lives/(\d+)/notify'] = 'lives/notifyLiveStart/$1';`: Cualquier método a `/lives/123/notify` dirige a `Lives::notifyLiveStart(123)`.

- **Rutas Reservadas**:
  - `$route['default_controller'] = 'welcome';`: El controlador cargado si no se proporciona URI (por ejemplo, URL raíz → controlador `Welcome`).
  - `$route['404_override'] = 'errors/page_missing';`: El controlador/método para rutas no coincidentes (404 personalizado).
  - `$route['translate_uri_dashes'] = FALSE;`: Si es TRUE, convierte los guiones en las URIs a guiones bajos para los nombres de controlador/método (por ejemplo, `mi-controlador` → `mi_controller`).

- **El Orden Importa**: Las rutas se comparan en el orden en que aparecen. Define rutas específicas (con comodines) antes que las generales para evitar conflictos.
- **Métodos HTTP**: Si no se especifica, una ruta se aplica a todos los métodos. Tu código utiliza arrays para especificidad, lo cual es ideal para APIs.

**Consejos para Definir Rutas en Tu Código**:
- Añade nuevas rutas al final, antes de `$route['translate_uri_dashes']`.
- Prueba con herramientas como Postman para las rutas de API y asegúrate de que se accede al controlador/método correcto.
- Para aplicaciones complejas, agrupa las rutas por sección (como has hecho con comentarios como `// users`).

#### 2. **Cómo Funcionan las Rutas**

El router de CodeIgniter procesa cada solicitud entrante en este orden:
1.  **Analizar la URI**: Divide la URL en segmentos (por ejemplo, `/users/123/edit` → segmentos: `users`, `123`, `edit`).
2.  **Comparar con las Rutas**: Comprueba el array `$route` de arriba a abajo. Busca primero coincidencias exactas, luego patrones con comodines.
    - Si encuentra una coincidencia, la asigna al controlador/método especificado, pasando las partes dinámicas (por ejemplo, `123`) como argumentos del método.
    - Si no hay coincidencia, recurre al patrón predeterminado (`Controller::method/id/`).
3.  **Cargar Controlador & Método**: CodeIgniter instancia el controlador, llama al método y pasa cualquier segmento de URI o grupos capturados.
4.  **Manejo Específico por Método**: Si la ruta es un array (como en tu código), comprueba el método HTTP (GET, POST, etc.) de la solicitud.
5.  **Respaldo (Fallback)**: Las solicitudes no coincidentes activan un 404, o el `$route['404_override']` si está configurado.

**Flujo de Ejemplo**:
- Solicitud: `POST https://example.com/lives`
- Coincide: `$route['lives']['POST'] = 'lives/create';`
- Resultado: Llama a `Lives::create()` sin argumentos.
- Si la solicitud fuera `GET https://example.com/lives/456`, coincidiría con `$route['lives/(\d+)']['GET'] = 'lives/one/$1';` → `Lives::one(456)`.

**Mecánica Clave**:
- **Parámetros Dinámicos**: Los grupos capturados (por ejemplo, `$1`) se pasan como argumentos al método. Asegúrate de que tu método del controlador los espere.
- **Seguridad**: Las rutas ayudan a prevenir el acceso directo a controladores sensibles al ofuscar las URLs.
- **Rendimiento**: Búsquedas simples en arrays; sin sobrecarga importante a menos que tengas cientos de rutas.

#### 3. **Cómo Usar las Rutas**

Usar rutas significa configurarlas como se describió anteriormente y luego aprovecharlas en tu aplicación (controladores, vistas, etc.).

- **En Controladores**: Asume que la ruta maneja el mapeo de la URL; escribe métodos que esperen las solicitudes enrutadas.
  - Ejemplo: Para `$route['login']['POST'] = 'users/login';`, crea un controlador `Users.php` con un método `login()` que maneje los datos POST (por ejemplo, mediante `$this->input->post()`).

- **Generar URLs**: Usa `site_url()` o `base_url()` de CodeIgniter con las claves de tus rutas para enlaces/botones.
  - Ejemplo: En una vista, `<a href="<?= site_url('login'); ?>">Iniciar Sesión</a>` apunta a la URL enrutada, pero tu código define a qué controlador llega.

- **Probar Rutas**:
  - Usa tu navegador web o herramientas de API (por ejemplo, Postman) para acceder a URLs como `/users/register`.
  - Revisa `application/logs/log-{date}.php` para ver errores si las rutas fallan.
  - Añade depuración: Restablece temporalmente `$route['404_override']` y usa var_dump en un controlador de prueba para ver los parámetros.

- **Uso RESTful (Como en Tu Código)**: Tus rutas están configuradas para una estructura tipo API. Por ejemplo:
  - Crear un recurso: Envía POST a `/lives` → Crea un evento en vivo.
  - Leer: GET `/lives/123` → Obtiene el evento en vivo #123.
  - Actualizar: POST `/lives/123` → Actualiza el evento en vivo #123.

- **Problemas Comunes y Consejos**:
  - **Duplicados**: Evita rutas superpuestas (por ejemplo, `lives` y `lives/(\d+)`); coloca las específicas primero.
  - **Métodos No Especificados**: Si una ruta es una cadena, funciona para todos los métodos HTTP. Usa arrays para precisión.
  - **Para Desarrollo**: Habilita el Profiler de CodeIgniter (`$this->output->enable_profiler(TRUE);`) en un controlador para depurar el enrutamiento.
  - **Control de Versiones**: Tu `routes.php` está en control de versiones – los cambios afectan el enrutamiento en vivo.
  - **Extensiones**: Si necesitas funciones avanzadas (por ejemplo, soporte de namespaces), considera CodeIgniter 4 o bibliotecas de terceros, ya que CI 3 (tu código) es más antiguo.

Si tienes preguntas específicas sobre una ruta en tu archivo (por ejemplo, por qué se usa `(\d+)` o cómo añadir una nueva), ¡proporciona más detalles! Para la configuración de CodeIgniter, asegúrate de que `CI_VERSION` esté definido en tu index.php.