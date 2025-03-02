---
audio: false
generated: true
lang: es
layout: post
title: Usar Características en la Interfaz de Usuario de Kong Insomnia
translated: true
---

Kong Insomnia proporciona una interfaz gráfica de usuario (GUI) robusta para simplificar el desarrollo de APIs. A continuación se presenta una guía detallada sobre cómo usar **params**, **body**, **auth**, **cookies**, **certificados**, **configuraciones** y **proxy** dentro de la GUI de Insomnia.

---

#### 1. **Params (Parámetros de Consulta)**
Los parámetros de consulta se utilizan para adjuntar datos a la URL, generalmente para solicitudes GET.

- **Cómo Usar**:
  - Abre la pestaña **Debug** y selecciona o crea una solicitud (por ejemplo, GET).
  - Junto al campo de URL, haz clic en la pestaña **Query**.
  - Agrega pares clave-valor para tus parámetros de consulta. Por ejemplo, ingresar `key` como "id" y `value` como "123" adjuntará `?id=123` a tu URL.
  - Para usar variables de entorno, escribe `{{variableName}}` en el campo de valor (por ejemplo, `{{userId}}`).
  - Habilita o deshabilita parámetros específicos activando o desactivando la casilla de verificación junto a cada par.

- **Ejemplo**:
  Para una URL como `https://api.example.com/users?id=123`, agrega:
  - Clave: `id`
  - Valor: `123`
  Insomnia formateará automáticamente la URL con la cadena de consulta.

---

#### 2. **Body**
El cuerpo se utiliza para enviar datos con solicitudes como POST o PUT.

- **Cómo Usar**:
  - En la pestaña **Debug**, selecciona una solicitud (por ejemplo, POST o PUT).
  - Cambia a la pestaña **Body** debajo del campo de URL.
  - Elige un tipo de cuerpo del menú desplegable:
    - **JSON**: Ingresa datos JSON (por ejemplo, `{"name": "John", "age": 30}`).
    - **Form URL-Encoded**: Agrega pares clave-valor, similar a los parámetros de consulta.
    - **Multipart Form**: Agrega campos o carga archivos para formularios con adjuntos de archivos.
    - **Raw**: Ingresa texto plano u otros formatos (por ejemplo, XML).
  - Usa variables de entorno escribiendo `{{variableName}}` dentro del contenido del cuerpo.

- **Ejemplo**:
  Para una solicitud POST enviando JSON:
  - Selecciona **JSON** del menú desplegable.
  - Ingresa: `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia establecerá automáticamente el encabezado `Content-Type` a `application/json`.

---

#### 3. **Auth (Autenticación)**
Las configuraciones de autenticación te permiten incluir credenciales o tokens en tus solicitudes.

- **Cómo Usar**:
  - En la pestaña **Debug**, selecciona tu solicitud.
  - Ve a la pestaña **Auth**.
  - Elige un tipo de autenticación del menú desplegable:
    - **Basic Auth**: Ingresa un nombre de usuario y una contraseña.
    - **Bearer Token**: Pega tu token (por ejemplo, un JWT).
    - **OAuth 2.0**: Configura el ID del cliente, el secreto y otros detalles para flujos de OAuth.
    - **API Key**: Agrega un par clave-valor (por ejemplo, Clave: `Authorization`, Valor: `your-api-key`).
  - Insomnia agrega automáticamente los detalles de autenticación a los encabezados de la solicitud.

- **Ejemplo**:
  Para un Bearer Token:
  - Selecciona **Bearer Token**.
  - Pega tu token (por ejemplo, `abc123xyz`).
  El encabezado de la solicitud incluirá: `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies**
Las cookies se gestionan automáticamente pero pueden verse o editarse manualmente.

- **Cómo Usar**:
  - Insomnia almacena las cookies recibidas de las respuestas del servidor por espacio de trabajo.
  - Para gestionar cookies:
    - Ve a **Preferences** (Ctrl + , o Cmd + , en macOS).
    - Navega a **Data** > **Cookie Jar**.
    - Ve, edita o elimina cookies según sea necesario.
  - Las cookies persisten a través de las solicitudes en el mismo espacio de trabajo y se envían automáticamente con las solicitudes posteriores.

- **Consejo**:
  Si necesitas probar con cookies específicas, agrégalas manualmente en el **Cookie Jar** para el dominio relevante.

---

#### 5. **Certificados**
Los certificados del cliente se utilizan para solicitudes HTTPS que requieren autenticación TLS mutua.

- **Cómo Usar**:
  - Ve a **Preferences** (Ctrl + , o Cmd + ,).
  - Selecciona la sección **Certificates**.
  - Haz clic en **Add Certificate**:
    - Proporciona el archivo de certificado (por ejemplo, `.pem`, `.crt`).
    - Agrega el archivo de clave privada y una contraseña opcional si es necesario.
    - Asocia el certificado con hosts específicos (por ejemplo, `api.example.com`).
  - Insomnia utilizará el certificado para solicitudes a los hosts especificados.

- **Ejemplo**:
  Para `api.example.com` que requiere un certificado:
  - Sube `client.crt` y `client.key`.
  - Establece el Host en `api.example.com`.
  Las solicitudes a este dominio incluirán el certificado.

---

#### 6. **Configuraciones**
Las configuraciones te permiten personalizar el comportamiento de Insomnia.

- **Cómo Usar**:
  - Accede a través de **Preferences** (Ctrl + , o Cmd + ,).
  - Opciones clave incluyen:
    - **Tema**: Cambia entre claro, oscuro o predeterminado del sistema.
    - **Proxy**: Configura los ajustes del proxy (ver a continuación).
    - **Plugins**: Instala funcionalidad adicional (por ejemplo, formatos de respuesta personalizados).
    - **Data**: Gestiona el Local Vault para el almacenamiento seguro de datos sensibles como claves API.

- **Consejo**:
  Usa el **Local Vault** para almacenar valores sensibles (por ejemplo, tokens) de manera segura en lugar de codificarlos.

---

#### 7. **Proxy**
Los proxies enrutan tus solicitudes a través de un servidor especificado, útil para la depuración o redes corporativas.

- **Cómo Usar**:
  - Ve a **Preferences** > **Proxy**.
  - Habilita el proxy e ingresa los detalles del servidor proxy (por ejemplo, `http://proxy.example.com:8080`).
  - Para uso global, guárdalo aquí.
  - Para proxy por solicitud:
    - Haz clic en el icono de engranaje junto al nombre de la solicitud en la pestaña **Debug**.
    - Anula la configuración del proxy en la configuración específica de la solicitud.

- **Ejemplo**:
  Para enrutar solicitudes a través de un proxy corporativo:
  - Habilita el proxy en **Preferences**.
  - Establece la URL del Proxy en `http://proxy.example.com:8080`.
  Todas las solicitudes ahora usarán este proxy a menos que se anule.

---

### Resumen
Aquí tienes un rápido repaso de cómo usar estas características en la GUI de Insomnia:
- **Params**: Agrega parámetros de consulta en la pestaña **Query** para solicitudes GET.
- **Body**: Envía datos con solicitudes POST/PUT a través de la pestaña **Body**, seleccionando el formato.
- **Auth**: Configura la autenticación en la pestaña **Auth** para solicitudes seguras.
- **Cookies**: Gestiona cookies en **Preferences** > **Cookie Jar**.
- **Certificados**: Agrega certificados del cliente en **Preferences** > **Certificates** para HTTPS.
- **Configuraciones**: Personaliza Insomnia en **Preferences** (temas, plugins, etc.).
- **Proxy**: Configura proxies en **Preferences** o por solicitud.

Al aprovechar estas características, puedes probar y depurar APIs en Kong Insomnia de manera eficiente. ¡Experimenta con cada sección para adaptar tu flujo de trabajo!