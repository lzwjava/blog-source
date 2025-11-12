---
audio: false
generated: true
lang: es
layout: post
title: Funciones en la Interfaz Gráfica de Kong Insomnia
translated: true
type: note
---

Kong Insomnia proporciona una interfaz gráfica de usuario (GUI) robusta para simplificar el desarrollo de API. A continuación se presenta una guía detallada sobre cómo usar **params**, **body**, **auth**, **cookies**, **certificates**, **settings** y **proxy** dentro de la GUI de Insomnia.

---

#### 1. **Params (Parámetros de Consulta)**
Los parámetros de consulta se utilizan para añadir datos a la URL, típicamente para solicitudes GET.

- **Cómo Usar**:
  - Abre la **pestaña Debug** y selecciona o crea una solicitud (por ejemplo, GET).
  - Junto al campo URL, haz clic en la pestaña **Query**.
  - Añade pares clave-valor para tus parámetros de consulta. Por ejemplo, introducir `key` como "id" y `value` como "123" añadirá `?id=123` a tu URL.
  - Para usar variables de entorno, escribe `{{nombreDeVariable}}` en el campo de valor (por ejemplo, `{{userId}}`).
  - Activa o desactiva parámetros específicos alternando la casilla de verificación junto a cada par.

- **Ejemplo**:
  Para una URL como `https://api.example.com/users?id=123`, añade:
  - Clave: `id`
  - Valor: `123`
  Insomnia formateará automáticamente la URL con la cadena de consulta.

---

#### 2. **Body (Cuerpo)**
El cuerpo se utiliza para enviar datos con solicitudes como POST o PUT.

- **Cómo Usar**:
  - En la **pestaña Debug**, selecciona una solicitud (por ejemplo, POST o PUT).
  - Cambia a la pestaña **Body** debajo del campo URL.
  - Elige un tipo de cuerpo del menú desplegable:
    - **JSON**: Introduce datos JSON (por ejemplo, `{"name": "John", "age": 30}`).
    - **Form URL-Encoded**: Añade pares clave-valor, similar a los parámetros de consulta.
    - **Multipart Form**: Añade campos o sube archivos para formularios con archivos adjuntos.
    - **Raw**: Introduce texto plano u otros formatos (por ejemplo, XML).
  - Usa variables de entorno escribiendo `{{nombreDeVariable}}` dentro del contenido del cuerpo.

- **Ejemplo**:
  Para una solicitud POST enviando JSON:
  - Selecciona **JSON** del menú desplegable.
  - Introduce: `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia establecerá automáticamente la cabecera `Content-Type` a `application/json`.

---

#### 3. **Auth (Autenticación)**
La configuración de autenticación te permite incluir credenciales o tokens en tus solicitudes.

- **Cómo Usar**:
  - En la **pestaña Debug**, selecciona tu solicitud.
  - Ve a la pestaña **Auth**.
  - Elige un tipo de autenticación del menú desplegable:
    - **Basic Auth**: Introduce un nombre de usuario y contraseña.
    - **Bearer Token**: Pega tu token (por ejemplo, un JWT).
    - **OAuth 2.0**: Configura el ID de cliente, secreto y otros detalles para flujos OAuth.
    - **API Key**: Añade un par clave-valor (por ejemplo, Clave: `Authorization`, Valor: `tu-clave-de-api`).
  - Insomnia añade automáticamente los detalles de autenticación a las cabeceras de la solicitud.

- **Ejemplo**:
  Para un Token Bearer:
  - Selecciona **Bearer Token**.
  - Pega tu token (por ejemplo, `abc123xyz`).
  La cabecera de la solicitud incluirá: `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies (Cookies)**
Las cookies se gestionan automáticamente, pero se pueden ver o editar manualmente.

- **Cómo Usar**:
  - Insomnia almacena las cookies recibidas de las respuestas del servidor por espacio de trabajo.
  - Para gestionar cookies:
    - Ve a **Preferences** (Ctrl + , o Cmd + , en macOS).
    - Navega a **Data** > **Cookie Jar**.
    - Visualiza, edita o elimina cookies según sea necesario.
  - Las cookies persisten entre solicitudes en el mismo espacio de trabajo y se envían automáticamente con las solicitudes posteriores.

- **Consejo**:
  Si necesitas probar con cookies específicas, añádelas manualmente en el **Cookie Jar** para el dominio relevante.

---

#### 5. **Certificates (Certificados)**
Los certificados de cliente se utilizan para solicitudes HTTPS que requieren autenticación TLS mutua.

- **Cómo Usar**:
  - Ve a **Preferences** (Ctrl + , o Cmd + ,).
  - Selecciona la sección **Certificates**.
  - Haz clic en **Add Certificate**:
    - Proporciona el archivo de certificado (por ejemplo, `.pem`, `.crt`).
    - Añade el archivo de clave privada y una frase de contraseña opcional si es requerida.
    - Asocia el certificado con hosts específicos (por ejemplo, `api.example.com`).
  - Insomnia usará el certificado para las solicitudes a los hosts especificados.

- **Ejemplo**:
  Para `api.example.com` que requiere un certificado:
  - Sube `client.crt` y `client.key`.
  - Establece Host a `api.example.com`.
  Las solicitudes a este dominio incluirán el certificado.

---

#### 6. **Settings (Configuración)**
La configuración te permite personalizar el comportamiento de Insomnia.

- **Cómo Usar**:
  - Accede a través de **Preferences** (Ctrl + , o Cmd + ,).
  - Las opciones clave incluyen:
    - **Theme**: Cambia entre claro, oscuro o el predeterminado del sistema.
    - **Proxy**: Configura los ajustes de proxy (ver más abajo).
    - **Plugins**: Instala funcionalidad adicional (por ejemplo, formateadores de respuesta personalizados).
    - **Data**: Gestiona Local Vault para el almacenamiento seguro de datos sensibles como claves de API.

- **Consejo**:
  Usa el **Local Vault** para almacenar valores sensibles (por ejemplo, tokens) de forma segura en lugar de codificarlos directamente.

---

#### 7. **Proxy**
Los proxies enrutan tus solicitudes a través de un servidor especificado, útil para depuración o redes corporativas.

- **Cómo Usar**:
  - Ve a **Preferences** > **Proxy**.
  - Habilita el proxy e introduce los detalles del servidor proxy (por ejemplo, `http://proxy.example.com:8080`).
  - Para uso global, guárdalo aquí.
  - Para proxy por solicitud:
    - Haz clic en el icono de engranaje junto al nombre de la solicitud en la **pestaña Debug**.
    - Anula la configuración del proxy en la configuración específica de la solicitud.

- **Ejemplo**:
  Para enrutar solicitudes a través de un proxy corporativo:
  - Habilita el proxy en **Preferences**.
  - Establece Proxy URL a `http://proxy.example.com:8080`.
  Todas las solicitudes usarán ahora este proxy a menos que se anule.

---

### Resumen
Aquí tienes un resumen rápido de cómo usar estas funciones en la GUI de Insomnia:
- **Params**: Añade parámetros de consulta en la pestaña **Query** para solicitudes GET.
- **Body**: Envía datos con solicitudes POST/PUT a través de la pestaña **Body**, seleccionando el formato.
- **Auth**: Configura la autenticación en la pestaña **Auth** para solicitudes seguras.
- **Cookies**: Gestiona las cookies en **Preferences** > **Cookie Jar**.
- **Certificates**: Añade certificados de cliente en **Preferences** > **Certificates** para HTTPS.
- **Settings**: Personaliza Insomnia en **Preferences** (temas, plugins, etc.).
- **Proxy**: Configura proxies en **Preferences** o por solicitud.

Al aprovechar estas funciones, puedes probar y depurar APIs en Kong Insomnia de manera eficiente. ¡Experimenta con cada sección para adaptar tu flujo de trabajo!