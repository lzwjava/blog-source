---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Flujo de Código de Dispositivo OAuth de GitHub
translated: true
type: note
---

### Resumen

Este código JavaScript implementa el flujo de Concesión de Autorización de Dispositivo OAuth 2.0 (también conocido como concesión de Código de Dispositivo) para autenticarse con GitHub y obtener un token de acceso. El flujo se utiliza típicamente para aplicaciones sin interfaz gráfica (por ejemplo, herramientas CLI o sistemas embebidos) donde el usuario no puede interactuar directamente con un navegador web para aprobar la autenticación.

En este caso específico, parece estar imitando peticiones del plugin GitHub Copilot (por ejemplo, para Neovim o Vim), usando encabezados que suplantan a un cliente Copilot para potencialmente integrarse o acceder al sistema de autenticación de GitHub. El objetivo es generar un token de acceso que podría usarse para llamadas a la API de GitHub que requieren autenticación de usuario, como leer información del usuario (según el `scope: "read:user"`).

El código se ejecuta como un script de Node.js, usando `fetch` para peticiones HTTP y `process` para variables de entorno. Asume que Node.js tiene `fetch` disponible (como en versiones más nuevas o mediante un polyfill). Si tiene éxito, sondea los servidores de GitHub hasta que el usuario autorice la solicitud o se agote el tiempo de espera.

**Notas importantes:**
- Este código requiere establecer una variable de entorno `MY_COPILOT_CLIENT_ID`, probablemente un ID de cliente de una App OAuth de GitHub registrada para GitHub Copilot.
- Maneja los errores mínimamente—por ejemplo, si falla la obtención (`fetch`), registra el error y continúa o sale.
- En cuanto a seguridad, almacenar o registrar tokens de acceso es riesgoso (otorgan acceso a la API). Este código imprime el objeto token completo directamente en la consola, lo que podría ser un problema de privacidad/seguridad en un uso real. Los tokens de acceso deben manejarse de forma segura (por ejemplo, almacenados cifrados y rotados).
- El flujo implica interacción del usuario: El usuario debe visitar una URL e introducir un código en el sitio de GitHub para autorizar.
- Este no es código de documentación "oficial" de GitHub; parece estar reverse-engineered del comportamiento de GitHub Copilot. Usa las APIs de manera responsable y de acuerdo con los términos de servicio de GitHub.

### Desglose Paso a Paso

#### 1. Verificación del Entorno
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID is not set");
  process.exit(1);
}
```
- Recupera `MY_COPILOT_CLIENT_ID` de las variables de entorno (por ejemplo, establecida via `export MY_COPILOT_CLIENT_ID=tu_client_id` en tu shell).
- Si no está establecida, registra un error y sale del script (código de proceso 1 indica fallo).
- Este ID de cliente proviene de una App OAuth de GitHub registrada (necesaria para los flujos OAuth).

#### 2. Configuración de Encabezados Comunes
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- Crea un objeto `Headers` con pares clave-valor para peticiones HTTP.
- Estos encabezados hacen que las peticiones parezcan ser del plugin GitHub Copilot para Vim (versión 1.16.0 para Neovim 0.6.1). Esto es probablemente para suplantar el user-agent y imitar las llamadas API de Copilot, lo que podría ser requerido o útil para que GitHub acepte las peticiones.
- `"accept": "application/json"`: Espera respuestas JSON.
- `"content-type": "application/json"`: Envía JSON en los cuerpos de las peticiones.
- `"accept-encoding"`: Permite compresión gzip/deflate para ahorrar ancho de banda.

#### 3. Función `getDeviceCode()`
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **Propósito**: Inicia el flujo de Código de Dispositivo solicitando un código de dispositivo a GitHub.
- Construye una carga útil JSON con:
  - `client_id`: El ID de cliente OAuth (para autenticación de tu app).
  - `scope`: `"read:user"`—limita el token a leer información básica del perfil de usuario (por ejemplo, nombre de usuario, email via API de GitHub). Este es un alcance mínimo.
- Realiza una petición POST a `https://github.com/login/device/code` (el endpoint de código de dispositivo OAuth de GitHub).
- Analiza la respuesta JSON (campos esperados: `device_code`, `user_code`, `verification_uri`, `expires_in`—no se muestran en el código, pero es estándar para este flujo).
- En error (por ejemplo, problemas de red), lo registra pero continúa (podría devolver `undefined`).
- Devuelve el objeto de datos JSON analizado de GitHub.

#### 4. Función `getAccessToken(deviceCode: string)`
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **Propósito**: Sonda a GitHub para intercambiar el código de dispositivo por un token de acceso una vez que el usuario lo autoriza.
- Toma el `device_code` del paso anterior.
- Construye JSON con:
  - `client_id`: El mismo que antes.
  - `device_code`: El código único que identifica este intento de autenticación/dispositivo.
  - `grant_type`: Especifica que es una concesión de Código de Dispositivo (URN estándar OAuth2).
- Realiza una petición POST a `https://github.com/login/oauth/access_token`.
- Devuelve la respuesta JSON analizada, que podría ser:
  - En éxito: `{ access_token: "...", token_type: "bearer", scope: "read:user" }`.
  - En pendiente/error: `{ error: "...", error_description: "..." }` (por ejemplo, "authorization_pending" o "slow_down").
- Los errores (por ejemplo, fallos de `fetch`) se registran pero no se manejan explícitamente, por lo que la función llamante debe verificar el valor de retorno.

#### 5. Ejecución Principal (Función Asíncrona Invocada Inmediatamente)
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`enter user code:\n${user_code}\n${verification_uri}`);
  console.info(`Expires in ${expires_in} seconds`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`access token:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **Flujo General**: Orquesta la concesión completa de Código de Dispositivo OAuth 2.0.
- Llama a `getDeviceCode()` y desestructura la respuesta en variables (asume que tiene éxito y tiene estas propiedades).
- Registra instrucciones para el usuario:
  - `user_code`: Un código alfanumérico corto (por ejemplo, "ABCD-EFGH").
  - `verification_uri`: Normalmente `https://github.com/login/device`, donde el usuario se autentica.
  - `expires_in`: Tiempo en segundos hasta que el código expira (por ejemplo, 900 para 15 minutos).
- El usuario debe visitar la URL, iniciar sesión en GitHub e introducir el código de usuario para autorizar la app.
- Entra en un bucle infinito para sondear por el token:
  - Espera 5 segundos entre intentos (intervalo de sondeo; GitHub recomienda slow_down para peticiones demasiado frecuentes).
  - Llama a `getAccessToken(device_code)`.
  - Si la respuesta tiene un `error`: Lo registra (por ejemplo, seguir esperando si es "authorization_pending").
  - Si tiene `access_token`: Registra el objeto token completo (formateado con sangría) y sale del bucle.
- **Casos Límite/Problemas**:
  - Si `getDeviceCode()` falla, la desestructuración podría dar error (el código no verifica esto).
  - No hay tiempo de espera del bucle—sigue sondeando indefinidamente a menos que se reciba el token de acceso o el script falle.
  - Registrar el token de acceso en la consola lo expone; en producción, deberías guardarlo de forma segura (por ejemplo, en un archivo o base de datos).

### Cómo Funciona de Extremo a Extremo
1. **Paso 1: Solicitar Código de Dispositivo** → El script obtiene un código temporal de GitHub.
2. **Paso 2: Autorización del Usuario** → El usuario visita GitHub e introduce el código para conceder permiso.
3. **Paso 3: Sondear por el Token** → El script sigue preguntando a GitHub hasta que se emite el token.
4. **Resultado**: Un token de acceso para el alcance especificado (por ejemplo, leer datos de usuario via API de GitHub).

Esta es una simulación de cómo podrían funcionar herramientas como GitHub CLI, adaptada para Copilot. Para la documentación oficial de OAuth de GitHub, consulta https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow. Si estás construyendo algo similar, asegúrate de cumplir con los estándares OAuth y las políticas de GitHub. Si tienes preguntas sobre modificar o ejecutar esto, ¡avísame!