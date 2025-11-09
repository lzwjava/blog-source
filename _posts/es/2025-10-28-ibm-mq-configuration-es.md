---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de IBM MQ WebSphere Application Server
translated: true
type: note
---

### Requisitos Previos
Antes de configurar IBM MQ (anteriormente WebSphere MQ) en IBM WebSphere Application Server (WAS), asegúrese de lo siguiente:
- IBM MQ está instalado en un servidor dedicado (o en el mismo que WAS para el modo de enlaces locales).
- Se ha creado un gestor de colas en IBM MQ (por ejemplo, usando `crtmqm QMNAME`).
- Se han creado las colas necesarias en el gestor de colas (por ejemplo, usando MQ Explorer o `runmqsc`).
- Las bibliotecas cliente de IBM MQ (archivos JAR como `com.ibm.mq.allclient.jar`, `com.ibm.mqjms.jar`) están disponibles. Si WAS está en una máquina remota a MQ, instale el cliente de IBM MQ en la máquina de WAS.
- Añada el usuario del proceso de WAS al grupo `mqm` para los permisos.
- Para usuarios no root en sistemas tipo Unix, use `setmqaut` para otorgar permisos.

### Configuración Paso a Paso
La configuración implica configurar el proveedor JMS, las fábricas de conexión y los destinos en la Consola Administrativa de WAS. Esto asume una conexión en modo distribuido (cliente) sobre TCP/IP; ajústelo para el modo de enlaces si es local.

1.  **Acceder a la Consola Administrativa de WAS**:
    - Inicie el servidor WAS.
    - Abra un navegador y vaya a `https://localhost:9043/ibm/console` (reemplace con su host/puerto).
    - Inicie sesión con las credenciales de administrador.

2.  **Configurar el Proveedor JMS de IBM MQ**:
    - Vaya a **Recursos > JMS > Proveedores**.
    - Haga clic en **Nuevo**.
    - Seleccione **Proveedor de mensajería WebSphere MQ**.
    - Complete los detalles:
        - **Nombre**: por ejemplo, `MQProvider`.
        - **Descripción**: Opcional.
        - **Ruta de clase**: Ruta a los archivos JAR de MQ (por ejemplo, `/opt/mqm/java/lib/*` o cópielos en `<WAS_HOME>/lib/ext`).
        - **Ruta de biblioteca nativa**: Requerido para el modo de enlaces (ruta a las bibliotecas de MQ, por ejemplo, `/opt/mqm/lib64`).
        - **Nombre de fábrica de contexto inicial externo**: `com.ibm.mq.jms.context.WMQInitialContextFactory` (para modo cliente).
        - **URL del proveedor de contexto externo**: por ejemplo, `host:1414/CHANNEL` (host = IP del servidor MQ, 1414 = puerto por defecto, CHANNEL = por ejemplo, `SYSTEM.DEF.SVRCONN`).
    - Guarde la configuración.

3.  **Crear una Fábrica de Conexión de Cola**:
    - Vaya a **Recursos > JMS > Fábricas de conexión de cola** (ámbito a su servidor o celda).
    - Haga clic en **Nuevo**.
    - Seleccione el proveedor creado en el Paso 2.
    - Complete:
        - **Nombre**: por ejemplo, `MQQueueCF`.
        - **Nombre JNDI**: por ejemplo, `jms/MQQueueCF`.
        - **Gestor de colas**: El nombre de su gestor de colas de MQ (por ejemplo, `QM1`).
        - **Host**: Nombre de host o IP del servidor MQ.
        - **Puerto**: 1414 (por defecto).
        - **Canal**: por ejemplo, `SYSTEM.DEF.SVRCONN`.
        - **Tipo de transporte**: `CLIENT` (para TCP/IP) o `BINDINGS` (local).
        - **Credenciales de seguridad**: ID de usuario y contraseña si es requerido.
    - Propiedades avanzadas opcionales: Establezca los tamaños del grupo de conexiones (por ejemplo, conexiones máximas según su carga).
    - Guarde.

4.  **Crear Destinos de Cola**:
    - Vaya a **Recursos > JMS > Colas**.
    - Haga clic en **Nuevo**.
    - Seleccione el proveedor.
    - Para cada cola:
        - **Nombre**: por ejemplo, `MyQueue`.
        - **Nombre JNDI**: por ejemplo, `jms/MyQueue`.
        - **Nombre de la cola**: Nombre exacto de la cola en MQ (por ejemplo, `MY.LOCAL.QUEUE`).
        - **Gestor de colas**: El mismo de arriba.
        - **Tipo de cliente objetivo**: `MQ` o `JMS`.
    - Guarde. Repita para temas si usa pub/sub.

5.  **(Opcional) Configurar el Servidor WebSphere MQ para el Modo de Enlaces**:
    - Si usa enlaces locales, vaya a **Servidores > Tipos de servidor > Servidores WebSphere MQ**.
    - Haga clic en **Nuevo**.
    - Establezca **Nombre**, **Nombre del gestor de colas**.
    - Especifique **Instalaciones de MQ** (ruta a la instalación de MQ).
    - Guarde y reinicie el servidor.

6.  **Configurar el Adaptador de Recursos JCA (para MDBs)**:
    - Vaya a **Recursos > Adaptadores de recursos > Fábricas de conexiones J2C**.
    - Si usa el RA MQ incorporado, asegúrese de que esté desplegado (WAS incluye `wmq.jmsra.rar`).
    - Establezca propiedades como conexiones máximas (por ejemplo, 10-50 según la carga).

7.  **Probar la Configuración**:
    - Despliegue una aplicación JMS de ejemplo o use el ejemplo JMS de WAS.
    - Revise los registros en busca de errores (por ejemplo, conexión rechazada en el puerto 1414).
    - Verifique en MQ: Use MQ Explorer para monitorizar las profundidades de las colas y los canales.

8.  **Seguridad y Configuración Avanzada**:
    - Habilite SSL: Configure almacenes de claves en WAS y MQ (canal con `SSLCIPH`).
    - Establezca autenticación: Use grupos de usuarios de MQ o IDs de usuario alternativos.
    - Para clústeres: Sincronice las configuraciones a través de los nodos.

### Consejos para la Resolución de Problemas
- **ClassNotFoundException**: Asegúrese de que los JARs de MQ estén en el classpath.
- **Fallos de conexión**: Compruebe el firewall en el puerto 1414, el estado del canal (`DISPLAY CHSTATUS(*)` en runmqsc).
- **Problemas con el modo de enlaces**: Verifique las bibliotecas nativas y que el usuario esté en el grupo `mqm`.
- Reinicie WAS después de los cambios.

Para detalles específicos de la versión (por ejemplo, WAS 9.x con MQ 9.x), consulte la documentación oficial de IBM.

[Usar WebSphere Application Server con IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configurar WebSphere Application Server para usar con IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Crear una definición de servidor WebSphere MQ](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)