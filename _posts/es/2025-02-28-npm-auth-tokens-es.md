---
audio: false
generated: true
lang: es
layout: post
title: Usando Tokens de Autenticación con URLs del Registro de npm
translated: true
---

### Puntos Clave
- Parece probable que para usar un token de autenticación con una URL de registro de npm, se configure en el archivo `.npmrc`, asociando el token con la URL del registro.
- La investigación sugiere que la forma estándar es agregar `//registry.url.com/:_authToken=your_token` en el archivo `.npmrc`, donde `registry.url.com` es la URL del registro y `your_token` es su token de autenticación.
- La evidencia apunta a usar el archivo `.npmrc` para la autenticación, ya que incluir el token directamente en la URL (como en la solicitud HTTP) no es estándar para npm y puede que no funcione.

### Respuesta Directa

#### Descripción General
Para usar un token de autenticación con una URL de registro de npm, generalmente se configura en un archivo especial llamado `.npmrc`. Este archivo le indica a la herramienta de línea de comandos de npm cómo autenticarse al acceder a registros de paquetes específicos, como el registro público de npm o uno privado. Aquí te explicamos cómo hacerlo paso a paso, manteniéndolo simple para principiantes.

#### Pasos para Configurar
1. **Encontrar la URL del Registro**: Decide qué registro quieres usar, como `registry.npmjs.org` para el registro público de npm o una URL como `privateregistry.com` para uno privado.
2. **Obtener tu Token de Autenticación**: Obtén el token de autenticación del proveedor del registro, que podría ser un token de acceso personal o otro tipo proporcionado por tu organización.
3. **Editar el Archivo `.npmrc`**: Abre o crea el archivo `.npmrc`. Este archivo puede estar en la carpeta del proyecto para configuraciones específicas del proyecto o en tu directorio de inicio (como `~/.npmrc` en sistemas Unix) para configuraciones de usuario.
   - Agrega una línea como esta: `//registry.url.com/:_authToken=your_token`. Reemplaza `registry.url.com` con tu URL del registro y `your_token` con tu token real.
   - Por ejemplo, para el registro público de npm, podría verse así: `//registry.npmjs.org/:_authToken=abc123`.
4. **Seguridad del Archivo**: Asegúrate de que el archivo `.npmrc` sea solo legible y escribible por ti para mantener tu token seguro. En sistemas Unix, puedes establecer permisos con `chmod 600 ~/.npmrc`.
5. **Verificar que Funcione**: Intenta ejecutar un comando de npm, como `npm install`, para ver si puede acceder al registro sin problemas.

#### Detalle Inesperado
Aunque podrías pensar que puedes poner el token de autenticación directamente en la URL (como `https://registry.url.com?token=your_token`), esto no es la forma estándar para npm. En cambio, npm usa el archivo `.npmrc` para manejar la autenticación en segundo plano, haciéndolo más seguro y fácil de gestionar.

Para más detalles, consulta la documentación oficial de npm sobre la configuración del archivo `.npmrc` [aquí](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Nota de Encuesta: Exploración Detallada del Uso de Tokens de Autenticación con URLs de Registros de npm

Esta sección proporciona un análisis exhaustivo de cómo usar tokens de autenticación con URLs de registros de npm, ampliando la respuesta directa con contexto adicional, detalles técnicos y ejemplos. Se pretende cubrir todos los aspectos discutidos en la investigación, asegurando una comprensión completa para usuarios con diferentes niveles de experiencia.

#### Introducción a npm y Autenticación
El Administrador de Paquetes de Node (npm) es una herramienta crucial para los desarrolladores de JavaScript, gestionando paquetes y dependencias. Interactúa con registros de paquetes, como el registro público en [registry.npmjs.org](https://registry.npmjs.org), y registros privados alojados por organizaciones. La autenticación a menudo es necesaria para registros privados o acciones específicas como publicar paquetes, y esto generalmente se maneja a través de tokens de autenticación almacenados en archivos de configuración.

El archivo `.npmrc` es central en la configuración de npm, permitiendo la personalización de configuraciones como URLs de registros, métodos de autenticación y más. Puede existir en múltiples ubicaciones, como por proyecto (en la raíz del proyecto), por usuario (en el directorio de inicio, por ejemplo, `~/.npmrc`), o globalmente (por ejemplo, `/etc/npmrc`). Este archivo usa un formato INI, donde las claves y valores definen cómo se comporta npm, incluyendo cómo se autentica con los registros.

#### Configuración de Tokens de Autenticación en `.npmrc`
Para usar un token de autenticación con una URL de registro específica, configuras el archivo `.npmrc` para asociar el token con ese registro. El formato estándar es:

```
registry.url.com/:_authToken=your_token
```

Aquí, `registry.url.com` es la URL base del registro (por ejemplo, `registry.npmjs.org` para el registro público o `privateregistry.com` para uno privado), y `your_token` es el token de autenticación proporcionado por el registro. La clave `:_authToken` indica que esta es una autenticación basada en tokens, que npm usa para establecer el encabezado `Authorization` como `Bearer your_token` al hacer solicitudes HTTP al registro.

Por ejemplo, si tienes un token `abc123` para el registro público de npm, tu entrada en `.npmrc` sería:

```
registry.npmjs.org/:_authToken=abc123
```

Esta configuración asegura que cualquier comando de npm que interactúe con `registry.npmjs.org` incluya el token para la autenticación, permitiendo el acceso a paquetes privados o capacidades de publicación, dependiendo del alcance del token.

#### Manejo de Paquetes con Alcance
Para paquetes con alcance (paquetes que comienzan con `@`, como `@mycompany/mypackage`), puedes especificar un registro diferente para ese alcance. Primero, establece el registro para el alcance:

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Luego, asocia el token de autenticación con ese registro:

```
mycompany.artifactory.com/:_authToken=your_token
```

Esta configuración enruta todas las solicitudes para paquetes `@mycompany` al registro privado especificado y usa el token proporcionado para la autenticación. Esto es particularmente útil en entornos empresariales donde las organizaciones alojan sus propios registros de npm para paquetes internos.

#### Ubicación y Seguridad de `.npmrc`
El archivo `.npmrc` puede estar ubicado en varios lugares, cada uno sirviendo diferentes propósitos:
- **Por Proyecto**: Ubicado en la raíz del proyecto (por ejemplo, junto a `package.json`). Esto es ideal para configuraciones específicas del proyecto y anula las configuraciones globales.
- **Por Usuario**: Ubicado en el directorio de inicio del usuario (por ejemplo, `~/.npmrc` en Unix, `C:\Users\<NombreDeUsuario>\.npmrc` en Windows). Esto afecta todas las operaciones de npm para ese usuario.
- **Global**: Ubicado en `/etc/npmrc` o especificado por el parámetro `globalconfig`, generalmente utilizado para configuraciones del sistema.

Dado que `.npmrc` puede contener información sensible como tokens de autenticación, la seguridad es crucial. El archivo debe ser legible y escribible solo por el usuario para evitar acceso no autorizado. En sistemas Unix, puedes asegurarte de esto con el comando `chmod 600 ~/.npmrc`, estableciendo permisos de lectura/escritura solo para el propietario.

#### Métodos de Autenticación Alternativos
Aunque la autenticación basada en tokens es común, npm también soporta la autenticación básica, donde puedes incluir el nombre de usuario y la contraseña en el archivo `.npmrc`:

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

Sin embargo, por razones de seguridad, se prefiere la autenticación basada en tokens, ya que los tokens pueden ser revocados y tienen permisos con alcance, reduciendo el riesgo en comparación con almacenar contraseñas en texto plano.

#### Inclusión Directa en la URL: ¿Es Posible?
La pregunta menciona "usar auth o authtoken en la URL del registro de npm", lo que podría sugerir incluir el token directamente en la URL, como `https://registry.url.com?token=your_token`. Sin embargo, la investigación indica que esto no es la práctica estándar para npm. La documentación de la API del registro de npm y los recursos relacionados, como [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), enfatizan el uso del archivo `.npmrc` para la autenticación, con el token pasado en el encabezado `Authorization` como `Bearer your_token`.

Intentar incluir el token en la URL como un parámetro de consulta no es compatible con el registro de npm estándar y puede que no funcione, ya que la autenticación se maneja al nivel del encabezado HTTP. Algunos registros privados pueden soportar la autenticación basada en URL personalizada, pero esto no está documentado para el registro de npm oficial. Por ejemplo, la autenticación básica permite URLs como `https://username:password@registry.url.com`, pero esto está obsoleto e inseguro en comparación con los métodos basados en tokens.

#### Ejemplos Prácticos y Casos de Uso
Para ilustrar, considera estos escenarios:

- **Registro Público con Token**: Si necesitas publicar en el registro público de npm y tienes un token, agrega:
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  Luego, ejecuta `npm publish` para subir tu paquete, y npm usará el token para la autenticación.

- **Registro Privado para Paquetes con Alcance**: Para una empresa que usa un registro privado en `https://company.registry.com` para paquetes `@company`, configura:
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  Ahora, instalar `@company/mypackage` se autenticará con el registro privado usando el token.

- **Integración CI/CD**: En entornos de integración continua, almacena el token como una variable de entorno (por ejemplo, `NPM_TOKEN`) y úsalo en el archivo `.npmrc` dinámicamente:
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  Este enfoque, detallado en [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/), asegura que los tokens no estén codificados de manera rígida y sean seguros.

#### Solución de Problemas y Mejores Prácticas
Si la autenticación falla, verifica:
- La URL del registro es correcta y accesible.
- El token es válido y tiene los permisos necesarios (por ejemplo, lectura para la instalación, escritura para la publicación).
- El archivo `.npmrc` está en la ubicación correcta y tiene los permisos adecuados.

Las mejores prácticas incluyen:
- Nunca comites `.npmrc` con tokens en el control de versiones; agrégalo a `.gitignore`.
- Usa variables de entorno para tokens en flujos de trabajo CI/CD para mejorar la seguridad.
- Rota tokens regularmente y revoca los no utilizados para minimizar el riesgo.

#### Análisis Comparativo de Métodos de Autenticación
Para proporcionar una visión estructurada, aquí tienes una tabla comparando la autenticación basada en tokens y la autenticación básica en npm:

| **Método**          | **Configuración en `.npmrc`**                          | **Seguridad**                     | **Caso de Uso**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| Basada en Tokens (Preferida) | `registry.url.com/:_authToken=your_token`            | Alta (revocable, con alcance)         | Registros privados, CI/CD        |
| Autenticación Básica| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | Baja (contraseña en texto plano)         | Sistemas legados, registro público  |

Esta tabla destaca por qué la autenticación basada en tokens es recomendada, especialmente para flujos de trabajo modernos.

#### Conclusión
Usar un token de autenticación con una URL de registro de npm implica principalmente configurar el archivo `.npmrc` para asociar el token con el registro. Este enfoque es estándar, seguro y ampliamente soportado, asegurando que npm pueda autenticarse sin exponer tokens en URLs. Aunque incluir tokens directamente en URLs no es estándar para npm y puede que no funcione, el método `.npmrc` proporciona una solución robusta para interacciones tanto con registros públicos como privados.

Para lectura adicional, consulta la documentación oficial de npm sobre [configurar npmrc](https://docs.npmjs.com/configuring-npm/npmrc) y [autenticación de registros](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Citaciones Clave
- [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
- [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
- [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)