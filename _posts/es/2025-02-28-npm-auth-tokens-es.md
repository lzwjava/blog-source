---
audio: false
generated: true
lang: es
layout: post
title: Uso de Tokens de Autenticación con URLs del Registro de npm
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar un token de autenticación con una URL de registro de npm, lo configures en el archivo `.npmrc`, asociando el token con la URL del registro.
- La investigación sugiere que la forma estándar es agregar `//registry.url.com/:_authToken=tu_token` en el archivo `.npmrc`, donde `registry.url.com` es la URL del registro y `tu_token` es tu token de autenticación.
- La evidencia se inclina por usar el archivo `.npmrc` para la autenticación, ya que incluir el token directamente en la URL (como en la petición HTTP) no es estándar para npm y puede no funcionar.

### Respuesta Directa

#### Descripción General
Para usar un token de autenticación con una URL de registro de npm, normalmente lo configuras en un archivo especial llamado `.npmrc`. Este archivo le indica a la herramienta de línea de comandos de npm cómo autenticarse cuando accede a registros de paquetes específicos, como el registro público de npm o uno privado. Aquí te mostramos cómo hacerlo paso a paso, manteniéndolo simple para principiantes.

#### Pasos para Configurar
1.  **Encuentra la URL del Registro**: Decide qué registro quieres usar, como `registry.npmjs.org` para el registro público de npm o una URL como `privateregistry.com` para uno privado.
2.  **Obtén Tu Token de Autenticación**: Consigue el token de autenticación del proveedor del registro, que podría ser un token de acceso personal u otro tipo proporcionado por tu organización.
3.  **Edita el Archivo `.npmrc`**: Abre o crea el archivo `.npmrc`. Este archivo puede estar en la carpeta de tu proyecto para configuraciones específicas del proyecto o en tu directorio de usuario (como `~/.npmrc` en sistemas Unix) para configuraciones de todo el usuario.
    - Agrega una línea como esta: `//registry.url.com/:_authToken=tu_token`. Reemplaza `registry.url.com` con la URL de tu registro y `tu_token` con tu token real.
    - Por ejemplo, para el registro público de npm, podría verse así: `//registry.npmjs.org/:_authToken=abc123`.
4.  **Asegura el Archivo**: Asegúrate de que el archivo `.npmrc` solo sea legible y escribible por ti para mantener tu token seguro. En sistemas Unix, puedes establecer los permisos con `chmod 600 ~/.npmrc`.
5.  **Verifica que Funcione**: Intenta ejecutar un comando de npm, como `npm install`, para ver si puede acceder al registro sin problemas.

#### Detalle Inesperado
Aunque podrías pensar que puedes poner el token de autenticación directamente en la URL (como `https://registry.url.com?token=tu_token`), esta no es la forma estándar para npm. En su lugar, npm usa el archivo `.npmrc` para manejar la autenticación detrás de escena, haciéndolo más seguro y fácil de gestionar.

Para más detalles, consulta la documentación oficial de npm sobre la configuración del archivo `.npmrc` [aquí](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Nota de Estudio: Exploración Detallada del Uso de Tokens de Autenticación con URLs de Registro de npm

Esta sección proporciona un análisis exhaustivo de cómo usar tokens de autenticación con URLs de registro de npm, ampliando la respuesta directa con contexto adicional, detalles técnicos y ejemplos. Su objetivo es cubrir todos los aspectos discutidos en la investigación, asegurando una comprensión completa para usuarios con distintos niveles de experiencia.

#### Introducción a npm y Autenticación
Node Package Manager (npm) es una herramienta crucial para los desarrolladores de JavaScript, que gestiona paquetes y dependencias. Interactúa con registros de paquetes, como el registro público en [registry.npmjs.org](https://registry.npmjs.org), y registros privados alojados por organizaciones. A menudo se requiere autenticación para registros privados o acciones específicas como publicar paquetes, y esto normalmente se maneja a través de tokens de autenticación almacenados en archivos de configuración.

El archivo `.npmrc` es central para la configuración de npm, permitiendo personalizar ajustes como URLs de registro, métodos de autenticación y más. Puede existir en múltiples ubicaciones, como por proyecto (en la raíz del proyecto), por usuario (en el directorio de usuario, ej., `~/.npmrc`) o globalmente (ej., `/etc/npmrc`). Este archivo usa un formato INI, donde las claves y los valores definen cómo se comporta npm, incluyendo cómo se autentica con los registros.

#### Configuración de Tokens de Autenticación en `.npmrc`
Para usar un token de autenticación con una URL de registro específica, configuras el archivo `.npmrc` para asociar el token con ese registro. El formato estándar es:

```
registry.url.com/:_authToken=tu_token
```

Aquí, `registry.url.com` es la URL base del registro (ej., `registry.npmjs.org` para el registro público o `privateregistry.com` para uno privado), y `tu_token` es el token de autenticación proporcionado por el registro. La clave `:_authToken` indica que esta es una autenticación basada en token, que npm usa para establecer la cabecera `Authorization` como `Bearer tu_token` al hacer peticiones HTTP al registro.

Por ejemplo, si tienes un token `abc123` para el registro público de npm, tu entrada en `.npmrc` sería:

```
registry.npmjs.org/:_authToken=abc123
```

Esta configuración asegura que cualquier comando de npm que interactúe con `registry.npmjs.org` incluirá el token para la autenticación, permitiendo el acceso a paquetes privados o capacidades de publicación, dependiendo del alcance del token.

#### Manejo de Paquetes con Scope
Para paquetes con scope (paquetes que comienzan con `@`, como `@mycompany/mypackage`), puedes especificar un registro diferente para ese scope. Primero, establece el registro para el scope:

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Luego, asocia el token de autenticación con ese registro:

```
mycompany.artifactory.com/:_authToken=tu_token
```

Esta configuración enruta todas las peticiones para paquetes `@mycompany` al registro privado especificado y usa el token proporcionado para la autenticación. Esto es particularmente útil en entornos empresariales donde las organizaciones alojan sus propios registros npm para paquetes internos.

#### Ubicación y Seguridad de `.npmrc`
El archivo `.npmrc` puede ubicarse en varios lugares, cada uno sirviendo para diferentes propósitos:
-   **Por proyecto**: Ubicado en la raíz del proyecto (ej., junto a `package.json`). Esto es ideal para configuraciones específicas del proyecto y anula las configuraciones globales.
-   **Por usuario**: Ubicado en el directorio de usuario del usuario (ej., `~/.npmrc` en Unix, `C:\Users\<NombreDeUsuario>\.npmrc` en Windows). Esto afecta a todas las operaciones de npm para ese usuario.
-   **Global**: Ubicado en `/etc/npmrc` o especificado por el parámetro `globalconfig`, típicamente usado para ajustes de todo el sistema.

Dado que `.npmrc` puede contener información sensible como tokens de autenticación, la seguridad es crucial. El archivo debe ser legible y escribible solo por el usuario para prevenir acceso no autorizado. En sistemas Unix, puedes asegurar esto con el comando `chmod 600 ~/.npmrc`, estableciendo permisos de lectura/escritura solo para el propietario.

#### Métodos Alternativos de Autenticación
Si bien la autenticación basada en token es común, npm también soporta autenticación básica, donde puedes incluir nombre de usuario y contraseña en el archivo `.npmrc`:

```
registry.url.com/:username=tu_usuario
registry.url.com/:_password=tu_contraseña
```

Sin embargo, por razones de seguridad, se prefiere la autenticación basada en token, ya que los tokens pueden ser revocados y tienen permisos con alcance, reduciendo el riesgo en comparación con almacenar contraseñas en texto plano.

#### Inclusión Directa en la URL: ¿Es Posible?
La pregunta menciona "usar auth o authtoken en la url del registro de npm", lo que podría sugerir incluir el token directamente en la URL, como `https://registry.url.com?token=tu_token`. Sin embargo, la investigación indica que esta no es la práctica estándar para npm. La documentación de la API del registro de npm y recursos relacionados, como [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), enfatizan el uso del archivo `.npmrc` para la autenticación, con el token pasado en la cabecera `Authorization` como `Bearer tu_token`.

Intentar incluir el token en la URL como un parámetro de consulta no está soportado por el registro estándar de npm y puede no funcionar, ya que la autenticación se maneja a nivel de cabecera HTTP. Algunos registros privados podrían soportar autenticación personalizada basada en URL, pero esto no está documentado para el registro oficial de npm. Por ejemplo, la autenticación básica permite URLs como `https://usuario:contraseña@registry.url.com`, pero esto está obsoleto y es inseguro en comparación con los métodos basados en token.

#### Ejemplos Prácticos y Casos de Uso
Para ilustrar, considera estos escenarios:

-   **Registro Público con Token**: Si necesitas publicar en el registro público de npm y tienes un token, agrega:
    ```
    registry.npmjs.org/:_authToken=abc123
    ```
    Luego, ejecuta `npm publish` para subir tu paquete, y npm usará el token para la autenticación.

-   **Registro Privado para Paquetes con Scope**: Para una empresa que usa un registro privado en `https://company.registry.com` para paquetes `@company`, configura:
    ```
    @company:registry=https://company.registry.com/
    company.registry.com/:_authToken=def456
    ```
    Ahora, instalar `@company/mypackage` se autenticará con el registro privado usando el token.

-   **Integración CI/CD**: En entornos de integración continua, almacena el token como una variable de entorno (ej., `NPM_TOKEN`) y úsalo en el archivo `.npmrc` dinámicamente:
    ```
    registry.npmjs.org/:_authToken=${NPM_TOKEN}
    ```
    Este enfoque, detallado en [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/), asegura que los tokens no estén codificados y sean seguros.

#### Resolución de Problemas y Mejores Prácticas
Si la autenticación falla, verifica:
-   La URL del registro es correcta y accesible.
-   El token es válido y tiene los permisos necesarios (ej., lectura para instalación, escritura para publicación).
-   El archivo `.npmrc` está en la ubicación correcta y tiene los permisos adecuados.

Las mejores prácticas incluyen:
-   Nunca comprometer (commit) `.npmrc` con tokens al control de versiones; agrégalo a `.gitignore`.
-   Usar variables de entorno para tokens en pipelines CI/CD para mejorar la seguridad.
-   Rotar tokens regularmente y revocar los no utilizados para minimizar el riesgo.

#### Análisis Comparativo de Métodos de Autenticación
Para proporcionar una visión general estructurada, aquí hay una tabla que compara la autenticación basada en token y la autenticación básica en npm:

| **Método**               | **Configuración en `.npmrc`**                                                              | **Seguridad**                          | **Caso de Uso**                     |
|--------------------------|-------------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------|
| Basada en Token (Preferida) | `registry.url.com/:_authToken=tu_token`                                                  | Alta (revocable, con alcance)          | Registros privados, CI/CD            |
| Autenticación Básica     | `registry.url.com/:username=tu_usuario`<br>`registry.url.com/:_password=tu_contraseña` | Baja (contraseña en texto plano)       | Sistemas legacy, registro público    |

Esta tabla resalta por qué se recomienda la autenticación basada en token, especialmente para flujos de trabajo modernos.

#### Conclusión
Usar un token de autenticación con una URL de registro de npm implica principalmente configurar el archivo `.npmrc` para asociar el token con el registro. Este enfoque es estándar, seguro y ampliamente soportado, asegurando que npm pueda autenticar peticiones sin exponer tokens en las URLs. Si bien incluir tokens directamente en las URLs no es estándar para npm y puede no funcionar, el método `.npmrc` proporciona una solución robusta para las interacciones con registros tanto públicos como privados.

Para más lectura, consulta la documentación oficial de npm sobre [configurar npmrc](https://docs.npmjs.com/configuring-npm/npmrc) y [autenticación de registro](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Citas Clave
-   [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
-   [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
-   [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
-   [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
-   [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
-   [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)