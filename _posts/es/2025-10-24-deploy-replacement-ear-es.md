---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Despliegue de EAR de Reemplazo en WebSphere
translated: true
type: note
---

### Despliegue de un Nuevo Archivo EAR para Reemplazar uno Existente en IBM WebSphere Application Server (WAS)

Reemplazar un archivo EAR (Enterprise Archive) en IBM WAS es una tarea de despliegue estándar, pero es fundamental seguir las mejores prácticas para evitar tiempo de inactividad, discrepancias de configuración o errores en tiempo de ejecución. A continuación, detallaré los puntos clave que debes confirmar y verificar antes, durante y después del proceso de carga/despliegue. Esto asume que estás utilizando la Consola Administrativa de WAS (o scripts de wsadmin para automatización) y que trabajas en un entorno soportado (por ejemplo, WAS 8.5, 9.x o perfil Liberty).

#### 1. **Preparativos Previos al Despliegue (Confirma Esto Antes de la Carga)**
   - **Copia de Seguridad de la Aplicación Actual**:
     - Exporta el EAR existente desde la consola (Aplicaciones > Aplicaciones Empresariales > [Nombre de la App] > Exportar) o haz una copia de seguridad de toda la configuración usando el comando `backupConfig` mediante wsadmin.
     - ¿Por qué? Permite revertir los cambios si el nuevo EAR causa problemas. Confirma que la copia de seguridad esté completa y almacenada de forma segura.

   - **Verificaciones de Compatibilidad**:
     - Verifica que el nuevo EAR se haya construido para la versión correcta de WAS (por ejemplo, versión de Java, especificaciones EJB como Jakarta EE vs. Java EE).
     - Comprueba si hay características obsoletas en tu versión de WAS (por ejemplo, mediante la documentación de IBM Knowledge Center). Ejecuta `wsadmin` con `AdminConfig.validateAppDeployment` si es posible.
     - Confirma que el descriptor de despliegue del EAR (application.xml, ibm-application-ext.xmi) coincida con los módulos de tu servidor (WARs, JARs dentro del EAR).

   - **Dependencias de Entorno y Recursos**:
     - Revisa los recursos JNDI: Orígenes de datos, colas JMS, variables de entorno. Asegúrate de que cualquier recurso referenciado (por ejemplo, proveedores JDBC) esté configurado y en buen estado. Prueba las conexiones a través de la consola (Recursos > JDBC > Orígenes de datos).
     - Seguridad: Confirma que los roles de usuario, las restricciones de seguridad y los mapeos (por ejemplo, en ibm-application-bnd.xmi) estén alineados con tu realm (por ejemplo, LDAP, federado). Verifica si el nuevo EAR requiere nuevos realms personalizados o certificados.
     - Políticas de Classloader: Toma nota del modo de classloader WAR actual (PARENT_FIRST o PARENT_LAST) y las referencias a bibliotecas compartidas—asegúrate de que no haya conflictos con el nuevo EAR.
     - Clustering/Alta Disponibilidad: Si estás en un entorno en clúster, confirma que el nuevo EAR sea idéntico en todos los nodos y planifica despliegues progresivos para minimizar el tiempo de inactividad.

   - **Detalles Específicos de la Aplicación**:
     - Context Root y Hosts Virtuales: Confirma que el contexto raíz no entre en conflicto con otras aplicaciones (Aplicaciones > [Nombre de la App] > Context Root for Web Modules).
     - Puerto y Mapeo: Verifica los mapeos de servlets y cualquier patrón de URL.
     - Propiedades Personalizadas: Comprueba si hay propiedades personalizadas específicas de la aplicación establecidas en la consola—puede que sea necesario reaplicarlas después del despliegue.

   - **Pruebas del Nuevo EAR**:
     - Construye y prueba el EAR en un entorno de staging/desarrollo primero. Utiliza herramientas como Rational Application Developer o Eclipse con plugins de WAS para validar.
     - Escanea en busca de problemas conocidos: Utiliza la búsqueda de Fix Packs y APARs de IBM para tu versión de WAS.

#### 2. **Durante la Carga y el Despliegue**
   - **Detener la Aplicación Actual**:
     - En la consola: Aplicaciones > Aplicaciones Empresariales > [Nombre de la App] > Detener. Confirma que se haya detenido completamente (no hay sesiones activas si la afinidad de sesión está habilitada).
     - Guarda la configuración y sincroniza los nodos en una configuración en clúster (Administración del sistema > Nodos > Sincronizar).

   - **Cargar el Nuevo EAR**:
     - Navega a Aplicaciones > Nueva Aplicación > Nueva Aplicación Empresarial.
     - Carga el archivo EAR. Durante el asistente:
       - Selecciona "Reemplazar aplicación existente" si se solicita (o desinstala la anterior primero mediante Aplicaciones > [Nombre de la App] > Desinstalar).
       - Revisa las opciones de despliegue: Mapea módulos a servidores, clústeres objetivo y bibliotecas compartidas.
       - Confirma paso a paso en el asistente: Asignaciones de roles de seguridad, referencias de recursos e integridad de los metadatos.
     - Si usas wsadmin: Script con `AdminApp.update` o `installInteractive` para reemplazos. Ejemplo:
       ```
       wsadmin> AdminApp.update('AppName', '[-operation update -contenturi /path/to/new.ear]')
       ```
       Siempre valida con `AdminConfig.validateAppDeployment` antes de aplicar.

   - **Sincronización de la Configuración**:
     - Después de la carga, guarda la configuración maestra y sincroniza con los gestores de despliegue/nodos.
     - Comprueba si hay advertencias/errores en el resumen del despliegue—soluciona inmediatamente cualquier problema de enlace de módulos.

   - **Iniciar la Aplicación**:
     - Inicia mediante la consola y confirma que se inicializa sin errores (monitorea el SystemOut.log y SystemErr.log en el directorio de logs del perfil).

#### 3. **Verificación Posterior al Despliegue**
   - **Registros y Monitoreo**:
     - Monitorea los registros (por ejemplo, `tail -f profile/logs/server1/SystemOut.log`) en busca del éxito del despliegue, errores de enlace o excepciones de inicio.
     - Utiliza la opción de la consola Solución de problemas > Registros y Trazas para obtener trazas detalladas si es necesario. Confirma que no haya ClassNotFoundExceptions o NoSuchMethodErrors.

   - **Pruebas Funcionales**:
     - Prueba de humo: Accede a la aplicación a través de su URL y verifica las funciones principales (por ejemplo, inicio de sesión, llamadas API).
     - Prueba de carga si es crítica—comprueba si hay fugas de memoria o regresiones de rendimiento.
     - Integraciones con Base de Datos/Externas: Ejecuta consultas o llamadas para confirmar el flujo de datos.

   - **Plan de Reversión**:
     - Confirma que puedes redesplegar rápidamente el EAR del que se hizo copia de seguridad. Configura comprobaciones de salud (por ejemplo, mediante IBM Health Center o scripts personalizados).

#### Errores Comunes a Tener en Cuenta
- **Gestión de Sesiones**: Si la aplicación utiliza HTTPSession, vacía las sesiones activas antes de detenerla para evitar pérdida de datos.
- **Permisos de Archivos**: Asegúrate de que el archivo EAR tenga permisos de lectura para el usuario de WAS (por ejemplo, wasadmin).
- **Tamaño y Tiempo**: Los EARs grandes pueden tardar tiempo en desplegarse—planifica durante ventanas de mantenimiento.
- **Diferencias del Perfil Liberty**: Si usas WAS Liberty, los despliegues son mediante ediciones de server.xml o `install-feature`; confirma que las configuraciones XML coincidan.
- **Notas Específicas de Versión**: Para WAS 9+, verifica los cambios de microProfile o CDI. Consulta siempre la documentación de IBM para tu versión exacta.

Si proporcionas más detalles (por ejemplo, versión de WAS, configuración en clúster o errores específicos que hayas visto), puedo refinar estos consejos. Para orientación oficial, consulta el IBM Knowledge Center o el portal de soporte. ¡Avísame si hay algo más en lo que pueda ayudar!