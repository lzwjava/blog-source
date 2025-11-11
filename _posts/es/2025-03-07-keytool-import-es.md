---
audio: false
generated: true
lang: es
layout: post
title: Importar Certificados con Keytool
translated: true
type: note
---

Para abordar tu consulta sobre el uso del comando `keytool -importcert` para importar un certificado al archivo `jre/lib/security/cacerts` y encontrar un error de "password verification failed" con una `java.security.UnrecoverableException`, desglosemos esto paso a paso para entender el problema, cómo solucionarlo y cuál podría ser la contraseña posible.

### Entendiendo el Problema

La utilidad `keytool` es una herramienta de línea de comandos incluida en el Java Development Kit (JDK) utilizada para gestionar almacenes de claves (keystores). Un almacén de claves es un archivo que almacena claves criptográficas y certificados, a menudo para proteger comunicaciones de red como SSL/TLS. El archivo `cacerts`, ubicado en `jre/lib/security`, es un almacén de claves específico que viene con el Java Runtime Environment (JRE). Contiene una colección de certificados raíz confiables de Autoridades de Certificación (CA) conocidas, que las aplicaciones Java utilizan por defecto para verificar conexiones seguras.

Cuando ejecutas el comando `keytool -importcert` para agregar un nuevo certificado al archivo `cacerts`, necesitas proporcionar la contraseña correcta para el almacén de claves. El mensaje de error que estás viendo—"password verification failed" seguido de `java.security.UnrecoverableException`—indica que la contraseña que proporcionaste (o no proporcionaste correctamente) no coincide con la contraseña del almacén de claves. Esta excepción típicamente surge cuando la contraseña proporcionada es incorrecta, impidiendo que `keytool` acceda o modifique el almacén de claves.

### El Comando en Cuestión

El comando que probablemente estás usando se parece a esto:

```
keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
```

- `-file mycert.crt`: Especifica el archivo de certificado que deseas importar.
- `-keystore /path/to/jre/lib/security/cacerts`: Apunta al almacén de claves `cacerts`.
- `-alias myalias`: Asigna un nombre único (alias) al certificado en el almacén de claves.

Cuando ejecutas este comando, `keytool` te solicita que ingreses la contraseña del almacén de claves. Si la contraseña que ingresas es incorrecta, obtienes el error que describes.

### Identificando la Contraseña Posible

Para el archivo `cacerts` en una instalación estándar de JRE (como las de Oracle u OpenJDK), la **contraseña por defecto** es **"changeit"**. Este es un valor por defecto bien documentado en todas las versiones y distribuciones de Java. El nombre "changeit" sirve como recordatorio de que los administradores podrían querer cambiarlo por razones de seguridad, pero en la mayoría de las instalaciones estándar y no modificadas, permanece sin cambios.

Dado que tu comando falla con un error de verificación de contraseña, el problema más probable es que:
1. No ingresaste "changeit" correctamente (por ejemplo, un error tipográfico o caso incorrecto—las contraseñas distinguen entre mayúsculas y minúsculas).
2. La solicitud de contraseña no se manejó correctamente.
3. En tu entorno específico, la contraseña por defecto ha sido cambiada (aunque esto es menos común para `cacerts` a menos que sea modificado explícitamente por un administrador del sistema).

Dado que tu consulta no indica una configuración personalizada, asumamos una instalación estándar de JRE donde "changeit" debería aplicarse.

### Cómo Solucionar el Problema

Aquí se explica cómo puedes resolver el problema:

1.  **Asegurar la Entrada Correcta de la Contraseña en el Prompt**
    Ejecuta el comando nuevamente:

    ```
    keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias
    ```

    Cuando se te solicite la contraseña, escribe cuidadosamente **"changeit"** (todo en minúsculas, sin espacios) y presiona Enter. Verifica dos veces que no haya errores tipográficos o problemas de distribución del teclado.

2.  **Especificar la Contraseña en la Línea de Comandos**
    Para evitar problemas con el prompt interactivo (por ejemplo, en scripts o mal comportamiento de la terminal), puedes incluir la contraseña directamente usando la opción `-storepass`:

    ```
    keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
    ```

    Esto pasa explícitamente "changeit" como la contraseña, evitando el prompt. Si esto funciona sin errores, el problema probablemente estaba en cómo se ingresó la contraseña anteriormente.

3.  **Verificar Permisos**
    Dado que `cacerts` reside en el directorio JRE (por ejemplo, `/usr/lib/jvm/java-11-openjdk/lib/security/cacerts` en Linux o una ruta similar en Windows), asegúrate de tener permisos de escritura. Ejecuta el comando con privilegios administrativos si es necesario:
    - En Linux/Mac: `sudo keytool ...`
    - En Windows: Ejecuta el símbolo del sistema como Administrador.

    Sin embargo, dado que tu error es sobre verificación de contraseña, no sobre acceso al archivo, es probable que este no sea el problema central—pero es bueno confirmarlo.

4.  **Verificar la Contraseña**
    Si "changeit" sigue fallando, es posible que la contraseña haya sido cambiada en tu entorno. Para probar la contraseña sin modificar el almacén de claves, intenta listar su contenido:

    ```
    keytool -list -keystore /path/to/jre/lib/security/cacerts
    ```

    Ingresa "changeit" cuando se te solicite. Si lista los certificados, la contraseña es correcta. Si obtienes el mismo error, la contraseña es diferente a la predeterminada.

### ¿Qué Pasa Si "changeit" No Es la Contraseña?

Si "changeit" no funciona, considera estas posibilidades:
- **Contraseña Personalizada**: En casos raros, un administrador del sistema podría haber cambiado la contraseña de `cacerts`. Necesitarías consultar la documentación de tu sistema o al administrador para obtenerla. No hay forma de recuperar directamente una contraseña de almacén de claves perdida; si es realmente desconocida, es posible que necesites reemplazar el archivo `cacerts` con una copia nueva de una instalación JRE nueva (lo que lo restablece a "changeit").
- **Valores Predeterminados Específicos del Entorno**: Algunas distribuciones de Java no estándar (por ejemplo, IBM JDK) podrían usar un valor predeterminado diferente, pero esto es poco común, y tu consulta sugiere una configuración típica.

Sin contexto adicional, "changeit" sigue siendo la contraseña más probable en un JRE estándar.

### Resolución Final

Para solucionar tu problema:
- Usa este comando, asumiendo un JRE estándar:

  ```
  keytool -importcert -file mycert.crt -keystore /path/to/jre/lib/security/cacerts -alias myalias -storepass changeit
  ```

- Si falla, verifica la contraseña con el comando `-list` o consulta con tu administrador del sistema.

La **contraseña posible** en este escenario, basada en las convenciones estándar de Java, es **"changeit"**. Esto debería resolver la `java.security.UnrecoverableException` si se ingresa correctamente y si el archivo `cacerts` no ha sido personalizado.