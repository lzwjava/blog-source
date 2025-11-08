---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de IBM MQ en WebSphere
translated: true
type: note
---

### Configuración de Colas de Mensajes en IBM WebSphere Application Server (Usando IBM MQ como Proveedor)

IBM WebSphere Application Server (WAS) admite la cola de mensajes a través de la integración de Java Message Service (JMS) con IBM MQ (anteriormente WebSphere MQ). La configuración se realiza normalmente a través de la **Consola de Soluciones Integradas de WebSphere** (la interfaz administrativa), accesible en `https://su-servidor:9043/ibm/console` (puerto seguro por defecto; ajústelo según sea necesario). Esta guía se centra en el perfil completo tradicional de WAS (por ejemplo, versión 9.0+), pero los pasos son similares para WebSphere Liberty con ajustes menores.

#### Prerrequisitos
- IBM MQ debe estar instalado, en ejecución y ser accesible (por ejemplo, el gestor de colas iniciado).
- El servidor WAS está iniciado y tiene acceso de administrador a la consola.
- Descargue e instale las bibliotecas cliente JMS de IBM MQ (por ejemplo, `com.ibm.mq.allclient.jar`) en las bibliotecas compartidas de WAS si aún no están presentes (bajo **Entorno > Bibliotecas Compartidas**).
- Asegúrese de que el proveedor de mensajería WebSphere MQ esté configurado (bajo **Recursos > JMS > Proveedores JMS**). Si no, cree uno con detalles como host, puerto (por defecto 1414) y nombre del gestor de colas.

Después de la configuración, guarde los cambios (botón **Guardar** en la parte superior) y reinicie el servidor de aplicaciones para que surtan efecto.

#### Paso 1: Crear una Fábrica de Conexiones de Cola JMS
La fábrica de conexiones establece conexiones con el gestor de colas de IBM MQ.

1. Inicie sesión en la Consola de Administración de WAS.
2. En el panel de navegación, expanda **Recursos > JMS > Fábricas de conexión de cola**.
3. Seleccione el **Ámbito** apropiado (por ejemplo, Celda, Nodo, Servidor) del menú desplegable y haga clic en **Aplicar**.
4. Haga clic en **Nuevo**.
5. Seleccione **Proveedor de mensajería WebSphere MQ** y haga clic en **Aceptar**.
6. En la siguiente pantalla:
   - **Nombre**: Introduzca un nombre descriptivo (por ejemplo, `MyMQQueueConnectionFactory`).
   - **Nombre JNDI**: Introduzca un enlace JNDI (por ejemplo, `jms/MyQueueConnectionFactory`).
   - Haga clic en **Siguiente**.
7. Introduzca los detalles de la conexión:
   - **Gestor de colas**: Nombre de su gestor de colas de IBM MQ (por ejemplo, `QM1`).
   - **Nombre del host**: Nombre de host o IP del servidor IBM MQ.
   - **Puerto**: Puerto del listener (por defecto: 1414).
   - **Tipo de transporte**: CHANNEL (para modo cliente) o BINDINGS (para modo embebido).
   - **Canal**: Nombre del canal por defecto (por ejemplo, `SYSTEM.DEF.SVRCONN`).
   - **ID de usuario** y **Contraseña**: Credenciales para la autenticación de MQ (si se requieren).
   - Haga clic en **Siguiente**.
8. Revise el resumen y haga clic en **Finalizar**.
9. Seleccione la nueva fábrica, vaya a **Propiedades adicionales > Grupo de conexiones** (opcional) y ajuste configuraciones como **Conexiones máximas** (por ejemplo, basado en la carga esperada).
10. Haga clic en **Probar conexión** para verificar.

#### Paso 2: Crear un Destino de Cola JMS
Esto define el endpoint de cola real para enviar/recibir mensajes.

1. En el panel de navegación, expanda **Recursos > JMS > Colas**.
2. Seleccione el **Ámbito** apropiado (que coincida con la fábrica de conexiones) y haga clic en **Aplicar**.
3. Haga clic en **Nuevo**.
4. Seleccione **Proveedor de mensajería WebSphere MQ** y haga clic en **Aceptar**.
5. Especifique las propiedades:
   - **Nombre**: Nombre descriptivo (por ejemplo, `MyRequestQueue`).
   - **Nombre JNDI**: Enlace JNDI (por ejemplo, `jms/MyRequestQueue`).
   - **Nombre de cola base**: Nombre exacto de la cola en IBM MQ (por ejemplo, `REQUEST.QUEUE`; debe existir o crearse en MQ).
   - **Cliente objetivo**: JMS (para aplicaciones JMS) o MQ (para aplicaciones MQ nativas).
   - **Modo de destino objetivo**: Una sola vez (por defecto para confiabilidad).
   - Haga clic en **Aceptar**.
6. (Opcional) Bajo **Propiedades adicionales**, configure ajustes de persistencia, expiración o prioridad.
7. Guarde la configuración.

#### Paso 3: (Opcional) Crear una Especificación de Activación para Message-Driven Beans (MDBs)
Si utiliza MDBs para consumir mensajes de forma asíncrona:

1. En el panel de navegación, expanda **Recursos > JMS > Especificaciones de activación**.
2. Seleccione el **Ámbito** y haga clic en **Nuevo**.
3. Seleccione **Proveedor de mensajería WebSphere MQ** y haga clic en **Aceptar**.
4. Introduzca:
   - **Nombre**: por ejemplo, `MyQueueActivationSpec`.
   - **Nombre JNDI**: por ejemplo, `jms/MyQueueActivation`.
   - **Tipo de destino**: Cola.
   - **Nombre JNDI de destino**: El JNDI de su cola (por ejemplo, `jms/MyRequestQueue`).
   - **Nombre JNDI de la fábrica de conexiones**: El JNDI de su fábrica de conexiones (por ejemplo, `jms/MyQueueConnectionFactory`).
   - Selector de mensajes (opcional): Selector JMS para filtrar mensajes.
5. Bajo **Propiedades adicionales > Servicio de escucha de mensajes > Puertos de escucha**, cree un puerto si es necesario:
   - **Nombre**: por ejemplo, `MyListenerPort`.
   - **JNDI de fábrica de conexiones**: Como arriba.
   - **JNDI de destino**: Como arriba.
   - **Componente**: El descriptor de despliegue de su MDB.
6. Haga clic en **Aceptar** y guarde.

#### Paso 4: Verificar y Probar
- **Probar en la Consola**: Use la opción **Probar conexión** en las fábricas y especificaciones.
- **Desplegar una Aplicación**: Cree una aplicación cliente JMS simple o una aplicación MDB, despliéguela y envíe/probar mensajes mediante las herramientas de IBM MQ (por ejemplo, MQ Explorer).
- **Monitoreo**: Bajo **Monitoreo y Ajuste > Visor de Rendimiento** o **Solución de Problemas > Registros**, busque errores relacionados con JMS.
- Problemas Comunes:
  - Fallos de conexión: Verifique el firewall, el estado del canal MQ (`DISPLAY CHANNEL`) y las credenciales.
  - Errores de búsqueda JNDI: Asegúrese de que los enlaces sean correctos y que la aplicación use el ámbito correcto.
  - Persistencia: Alinee los ajustes de durabilidad entre WAS y MQ.

Para alternativas de línea de comandos (scripting wsadmin), consulte la documentación de IBM. Ajuste según su versión (por ejemplo, WAS 9.0.5+ admite JMS 2.0).

#### Referencias
- [Configuración de recursos JMS en WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [Configuración de colas del proveedor de mensajería WebSphere MQ](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [Creación de una fábrica de conexiones de cola del proveedor de mensajería WebSphere MQ](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [Configurar un destino de cola JMS para WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)