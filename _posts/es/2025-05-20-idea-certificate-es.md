---
audio: false
generated: true
lang: es
layout: post
title: Manejo de certificados no confiables en IntelliJ IDEA
translated: true
type: note
---

El cuadro de diálogo "Certificado del servidor no confiable" en IntelliJ IDEA suele aparecer cuando el IDE encuentra certificados SSL que no son confiables para su almacén de claves, como certificados corporativos personalizados o autofirmados. Dado que ya importaste el almacén de claves de tu corporación en `/lib/cacerts` pero aún ves el aviso, el problema podría deberse a que IntelliJ no está usando ese almacén de claves o a certificados adicionales que provocan el diálogo. Aquí te explicamos cómo solucionarlo y potencialmente detener los avisos:

### Opción 1: Configurar IntelliJ para Aceptar Certificados No Confiables Automáticamente
Habilitar esta opción le indica a IntelliJ que omita el diálogo para certificados no confiables, pero ten cuidado, ya que reduce la seguridad al aceptar todos los certificados, exponiéndote potencialmente a ataques de tipo "man-in-the-middle".

- **Windows/Linux**:
  1. Ve a `File > Settings > Tools > Server Certificates`.
  2. Marca la casilla para **"Accept non-trusted certificates automatically"**.
  3. Haz clic en **Apply** y **OK**.
- **macOS**:
  1. Ve a `IntelliJ IDEA > Preferences > Tools > Server Certificates`.
  2. Marca **"Accept non-trusted certificates automatically"**.
  3. Haz clic en **Apply** y **OK**.

**Nota**: Esto no se recomienda a menos que te encuentres en una red confiable y aislada (por ejemplo, un entorno corporativo air-gapped), ya que puede hacer que tu IDE sea vulnerable a conexiones no verificadas.

### Opción 2: Verificar y Corregir la Configuración del Almacén de Claves
Dado que importaste el almacén de claves corporativo en `/lib/cacerts`, asegúrate de que IntelliJ lo esté usando correctamente. El problema podría ser que IntelliJ todavía esté haciendo referencia a su propio almacén de confianza o al archivo cacerts incorrecto.

1. **Verifica la Ruta del Almacén de Claves**:
   - IntelliJ a menudo usa su propio almacén de confianza en `~/.IntelliJIdea<version>/system/tasks/cacerts` o el almacén de confianza de JetBrains Runtime (JBR) en `<IntelliJ Installation>/jbr/lib/security/cacerts`.
   - Si modificaste `/lib/cacerts` en el directorio de IntelliJ, confirma que sea la ruta correcta para tu versión del IDE. Para instalaciones de JetBrains Toolbox, la ruta podría ser diferente (por ejemplo, `~/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/<version>/jbr/lib/security/cacerts` en Windows).
   - Usa el comando `keytool` para verificar que el certificado esté en el archivo cacerts:
     ```bash
     keytool -list -keystore <ruta-al-cacerts> -storepass changeit
     ```
     Asegúrate de que tu certificado de CA corporativo esté listado.

2. **Dirige IntelliJ al Almacén de Claves Personalizado**:
   - Si el certificado se importó correctamente pero IntelliJ aún muestra el aviso, es posible que no esté usando el cacerts modificado. Agrega una opción de VM personalizada para especificar el almacén de confianza:
     1. Ve a `Help > Edit Custom VM Options`.
     2. Agrega:
        ```
        -Djavax.net.ssl.trustStore=<ruta-al-cacerts>
        -Djavax.net.ssl.trustStorePassword=changeit
        ```
        Reemplaza `<ruta-al-cacerts>` con la ruta completa a tu archivo `cacerts` modificado.
     3. Reinicia IntelliJ IDEA.

3. **Reimporta el Certificado**:
   - Si la importación del certificado fue incompleta o incorrecta, reimpórtalo:
     ```bash
     keytool -import -trustcacerts -file <archivo-certificado>.cer -alias <alias> -keystore <ruta-al-cacerts> -storepass changeit
     ```
     Reemplaza `<archivo-certificado>.cer` con tu certificado de CA corporativo y `<ruta-al-cacerts>` con la ruta correcta del archivo cacerts.

### Opción 3: Agregar Certificados mediante la Configuración de Certificados de Servidor de IntelliJ
En lugar de modificar manualmente el archivo cacerts, puedes agregar certificados a través de la interfaz de usuario de IntelliJ, que los almacena en su almacén de confianza interno:

1. Ve a `File > Settings > Tools > Server Certificates` (o `IntelliJ IDEA > Preferences` en macOS).
2. Haz clic en el botón **"+"** para agregar un nuevo certificado.
3. Navega hasta tu archivo de certificado de CA corporativo (en formato `.cer` o `.pem`) e impórtalo.
4. Reinicia IntelliJ para asegurarte de que el certificado sea reconocido.

### Opción 4: Verificar Interferencia de Proxy o Antivirus
Los entornos corporativos a menudo usan proxies o software antivirus (por ejemplo, Zscaler, Forcepoint) que realizan inspección SSL de tipo "man-in-the-middle", generando nuevos certificados dinámicamente. Esto puede causar avisos repetidos si los certificados cambian con frecuencia (por ejemplo, diariamente, como con McAfee Endpoint Security).

- **Importa el Certificado de CA del Proxy/Antivirus**:
  - Obtén el certificado de CA raíz de tu software de proxy o antivirus (pregunta a tu equipo de TI).
  - Impórtalo al almacén de confianza de IntelliJ a través de `Settings > Tools > Server Certificates` o en el archivo cacerts usando el comando `keytool` mencionado anteriormente.
- **Deshabilita la Inspección SSL (si es posible)**:
  - Si tu proxy lo permite, configúralo para omitir la inspección SSL para los dominios relacionados con IntelliJ (por ejemplo, `plugins.jetbrains.com`, `repo.maven.apache.org`).

### Opción 5: Depurar e Identificar Certificados Problemáticos
Si el problema persiste, identifica qué servidor o certificado está causando el aviso:

1. Habilita el registro SSL detallado:
   - Ve a `Help > Edit Custom VM Options` y agrega:
     ```
     -Djavax.net.debug=ssl:handshake:verbose
     ```
   - Reinicia IntelliJ y revisa el archivo `idea.log` (ubicado en `~/.IntelliJIdea<version>/system/log/`) en busca de errores SSL, como `PKIX path building failed`. Esto mostrará el servidor o certificado problemático.

2. Verifica si hay plugins o integraciones específicas:
   - Los plugins como Maven, Gradle o sistemas de control de versiones (por ejemplo, Git, SVN) pueden conectarse a servidores con certificados diferentes. Deshabilita los plugins temporalmente para aislar el problema.
   - Para Maven, asegúrate de que el JDK configurado en `File > Settings > Build, Execution, Deployment > Build Tools > Maven > Runner` use el cacerts actualizado.

### Notas Adicionales
- **Advertencia de Seguridad**: Aceptar certificados no confiables automáticamente es conveniente pero arriesgado en redes no aisladas. Usa esto solo en entornos confiables.
- **Sincronización de la Hora del Sistema**: Asegúrate de que el reloj de tu sistema esté sincronizado, ya que una desincronización puede causar problemas de validación de certificados.
- **JetBrains Runtime (JBR)**: IntelliJ se ejecuta en su propio JBR, que puede no usar el almacén de confianza de Java del sistema. Los cambios en `$JAVA_HOME/lib/security/cacerts` del sistema no afectarán a IntelliJ a menos que se configuren explícitamente.
- **Avisos Persistentes**: Si los avisos persisten después de importar el certificado, podría deberse a un plugin o servicio (por ejemplo, JFrog, SonarQube) que use un almacén de confianza diferente. Revisa la configuración del plugin o contacta a tu equipo de TI para obtener la cadena de certificados completa.

### Enfoque Recomendado
1. Prueba primero la **Opción 3** (agregar certificados mediante la interfaz de usuario de IntelliJ), ya que es la más segura y directa.
2. Si falla, verifica la ruta y configuración del almacén de claves con la **Opción 2**.
3. Usa la **Opción 1** (aceptar automáticamente) solo como último recurso en un entorno confiable.
4. Si el problema involucra un proxy o antivirus, trabaja con tu equipo de TI para obtener e importar los certificados de CA correctos.

Si aún enfrentas problemas, comparte detalles sobre el certificado (por ejemplo, emisor, dominio) o cualquier mensaje de error del archivo `idea.log`, y puedo ayudarte a reducirlo aún más.