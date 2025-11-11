---
audio: false
generated: true
lang: es
layout: post
title: Pruebas del Registro de NPM Usando Solicitudes HTTP sin Procesar
translated: true
type: note
---

Para probar tu registro de NPM usando peticiones HTTP directas con herramientas como `curl` o Insomnia, puedes verificar su funcionalidad comprobando la conectividad, la autenticación y la capacidad de servir datos de paquetes, todo sin depender del cliente de NPM. Dado que tu registro requiere un nombre de usuario y contraseña, necesitarás manejar la autenticación manualmente en tus peticiones. A continuación, se presenta una guía completa para probar tu registro usando peticiones HTTP directas, asumiendo que es un registro compatible con NPM (por ejemplo, Verdaccio, Nexus, o una implementación personalizada) que soporta autenticación basada en tokens o autenticación básica.

---

## Pasos para Probar el Registro con Peticiones HTTP Directas

### 1. Autenticar y Obtener un Token (si es Necesario)

La mayoría de los registros de NPM usan autenticación basada en tokens, lo que requiere que inicies sesión para obtener un token antes de hacer más peticiones. Algunos registros también pueden soportar autenticación básica directamente. Así es como puedes autenticarte usando `curl`:

#### Usando `curl` para Iniciar Sesión
Envía una petición PUT al endpoint de autenticación del registro para obtener un token:

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **Reemplaza**:
  - `<username>`: Tu nombre de usuario del registro.
  - `<password>`: Tu contraseña del registro.
  - `<registry-url>`: La URL completa de tu registro (por ejemplo, `https://my-registry.example.com`).
- **Respuesta Esperada**: Si es exitosa, obtendrás una respuesta JSON con un token:
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **Guarda el Token**: Copia el valor `your-auth-token` para usarlo en peticiones posteriores.

**Nota**: Si tu registro usa un endpoint o método de autenticación diferente (por ejemplo, autenticación básica o una API personalizada), consulta su documentación. Si soporta autenticación básica directamente, puedes omitir este paso e incluir `-u "<username>:<password>"` en las peticiones posteriores.

---

### 2. Hacer Ping al Registro

Prueba la conectividad básica al registro enviando una petición GET a su URL raíz o a un endpoint de ping.

#### Usando `curl` para Hacer Ping
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **Reemplaza**:
  - `your-auth-token`: El token del Paso 1.
  - `<registry-url>`: La URL de tu registro.
- **Respuesta Esperada**: Una respuesta exitosa (HTTP 200) podría devolver la página de inicio del registro o un mensaje de estado simple (por ejemplo, `{"db_name":"registry"}` para registros basados en CouchDB).
- **Alternativa**: Algunos registros ofrecen un endpoint `/-/ping`:
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**Si Usas Autenticación Básica**: Si tu registro no usa tokens y soporta autenticación básica:
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. Recuperar Metadatos del Paquete

Verifica que el registro puede servir metadatos de paquetes solicitando los detalles de un paquete específico.

#### Usando `curl` para Obtener Metadatos
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **Reemplaza**:
  - `<package-name>`: Un paquete que sepas que existe en tu registro (por ejemplo, `lodash` si hace proxy al registro público, o un paquete privado como `my-org-utils`).
- **Respuesta Esperada**: Un objeto JSON con los metadatos del paquete, incluyendo versiones, dependencias y URLs de los tarballs. Por ejemplo:
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<registry-url>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**Si Usas Autenticación Básica**:
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **Éxito**: Una respuesta 200 OK con metadatos confirma que el registro está sirviendo datos de paquetes correctamente.

---

### 4. Descargar un Tarball de un Paquete (Opcional)

Para probar completamente el registro, descarga un tarball de un paquete para asegurarte de que puede entregar los archivos reales del paquete.

#### Usando `curl` para Descargar un Tarball
1. Desde los metadatos del Paso 3, encuentra la URL `tarball` para una versión específica (por ejemplo, `<registry-url>/lodash/-/lodash-4.17.21.tgz`).
2. Descárgala:
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **Reemplaza**: `<tarball-url>` con la URL de los metadatos.
- **Bandera `-O`**: Guarda el archivo con su nombre original (por ejemplo, `lodash-4.17.21.tgz`).
- **Si Usas Autenticación Básica**:
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **Éxito**: El archivo se descarga exitosamente, y puedes extraerlo (por ejemplo, con `tar -xzf <nombre-de-archivo>`) para verificar su contenido.

---

## Pruebas con Insomnia

Si prefieres una herramienta GUI como Insomnia, sigue estos pasos:

### 1. Configurar la Autenticación
- Crea una nueva petición en Insomnia.
- Ve a la pestaña **Auth**:
  - **Bearer Token**: Si obtuviste un token en el Paso 1, selecciona "Bearer Token" y pega `your-auth-token`.
  - **Basic Auth**: Si el registro usa autenticación básica, selecciona "Basic Auth" e ingresa tu `<username>` y `<password>`.

### 2. Hacer Ping al Registro
- **Método**: GET
- **URL**: `<registry-url>` o `<registry-url>/-/ping`
- Haz clic en **Send**.
- **Respuesta Esperada**: Un estado 200 OK con un cuerpo de respuesta simple.

### 3. Recuperar Metadatos del Paquete
- **Método**: GET
- **URL**: `<registry-url>/<package-name>`
- Asegúrate de que la autenticación esté configurada en la pestaña Auth.
- Haz clic en **Send**.
- **Respuesta Esperada**: Un estado 200 OK con metadatos del paquete en JSON.

### 4. Descargar un Tarball
- **Método**: GET
- **URL**: La URL del tarball de los metadatos (por ejemplo, `<registry-url>/<package-name>/-/<package-name>-<version>.tgz`).
- Haz clic en **Send and Download** para guardar el archivo localmente.
- **Éxito**: El archivo se descarga, confirmando que el registro sirve paquetes.

---

## Resolución de Problemas

- **401 No Autorizado**:
  - Verifica tu token o credenciales.
  - Asegúrate de que el encabezado `Authorization` o la autenticación básica estén formateados correctamente.
- **404 No Encontrado**:
  - Verifica que el paquete exista en el registro.
  - Si estás probando paquetes públicos (por ejemplo, `lodash`), confirma que el registro haga proxy al registro público de NPM.
- **Errores de Conexión**:
  - Verifica nuevamente la `<registry-url>` (por ejemplo, incluye `https://` si es necesario).
  - Para registros HTTPS, si obtienes errores de SSL con `curl`, añade `-k` para omitir las comprobaciones de certificado (solo para pruebas).
- **Comportamiento Personalizado del Registro**:
  - Si estos pasos fallan, consulta la documentación de tu registro para obtener endpoints específicos o métodos de autenticación.

---

## Conclusión

Siguiendo estos pasos con `curl` o Insomnia, puedes probar las capacidades de conectividad, autenticación y servicio de paquetes de tu registro de NPM usando peticiones HTTP directas. Comienza autenticándote (si es requerido), luego haz ping al registro, recupera los metadatos de un paquete conocido y, opcionalmente, descarga un tarball. Este enfoque asegura que tu registro esté completamente operativo a nivel HTTP.