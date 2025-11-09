---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de recursos JMS en WebSphere
translated: true
type: note
---

### Requisitos Previos
- Asegúrese de tener acceso administrativo a la Consola de Soluciones Integradas (admin console) de IBM WebSphere Application Server (WAS).
- El servidor debe estar en ejecución, y necesita decidir el ámbito (por ejemplo, celda, nodo, servidor) para los recursos.
- Esta guía se centra en el Proveedor de Mensajería Predeterminado (que utiliza Service Integration Bus o SIBus), que es el proveedor JMS integrado en WAS. Si utiliza WebSphere MQ, se requiere configuración adicional para el proveedor MQ.
- Reinicie el servidor después de cambios importantes si se le solicita.

### Paso 1: Crear un Bus de Integración de Servicios
El bus de integración de servicios actúa como la columna vertebral de mensajería para los recursos JMS.

1. Inicie sesión en la Consola de Soluciones Integradas de WebSphere.
2. Navegue a **Integración de servicios > Buses**.
3. Haga clic en **Nuevo**.
4. Ingrese un nombre único para el bus (por ejemplo, `MyJMSBus`).
5. Desactive la opción **Seguridad del bus** a menos que sea requerida.
6. Haga clic en **Siguiente**, luego en **Finalizar** para crear el bus.

### Paso 2: Agregar el Servidor como un Miembro del Bus
Esto permite que el servidor aloje motores de mensajería en el bus.

1. Seleccione el bus que creó (por ejemplo, `MyJMSBus`).
2. En **Propiedades adicionales**, haga clic en **Miembros del bus**.
3. Haga clic en **Agregar**.
4. En el asistente **Agregar un Nuevo Miembro del Bus**:
   - Seleccione **Motor de mensajería** como el tipo de miembro del bus.
   - Elija su servidor (por ejemplo, `server1`) de la lista.
   - Para el almacén de mensajes, seleccione **Almacén de archivos** (predeterminado para no agrupados) o **Almacén de datos** para persistencia en base de datos, y configure las propiedades si es necesario.
5. Haga clic en **Siguiente**, luego en **Finalizar**.
6. Reinicie WebSphere Application Server para activar el miembro del bus.

### Paso 3: Crear una Fábrica de Conexiones JMS
Se requiere una fábrica de conexiones para conectar clientes JMS al proveedor.

1. Navegue a **Recursos > JMS > Fábricas de conexiones**.
2. Seleccione el ámbito apropiado (por ejemplo, Ámbito del servidor para `server1`) y haga clic en **Nuevo**.
3. Seleccione **Proveedor de mensajería predeterminado** y haga clic en **Aceptar**.
4. Ingrese los detalles:
   - **Nombre**: por ejemplo, `MyJMSConnectionFactory`.
   - **Nombre JNDI**: por ejemplo, `jms/MyConnectionFactory`.
   - **Nombre del bus**: Seleccione `MyJMSBus` del menú desplegable.
   - Deje otros valores predeterminados (por ejemplo, Puntos finales del proveedor como auto-detectados).
5. Haga clic en **Aplicar**, luego en **Guardar** en la configuración maestra.

### Paso 4: Crear una Cola JMS
Esto define el destino de la cola para la mensajería punto a punto.

1. Navegue a **Recursos > JMS > Colas**.
2. Seleccione el ámbito apropiado y haga clic en **Nuevo**.
3. Seleccione **Proveedor de mensajería predeterminado** y haga clic en **Aceptar**.
4. Ingrese los detalles:
   - **Nombre**: por ejemplo, `MyJMSQueue`.
   - **Nombre JNDI**: por ejemplo, `jms/MyQueue`.
   - **Nombre del bus**: Seleccione `MyJMSBus`.
   - **Nombre de la cola**: Seleccione **Crear destino del bus de integración de servicios**, ingrese un identificador único (por ejemplo, `MyQueueDestination`) y seleccione el miembro del bus creado anteriormente.
   - **Nombre de cola base**: por ejemplo, `$MyJMSBus:MyQueueDestination` (generado automáticamente).
5. Configure propiedades adicionales si es necesario (por ejemplo, modo de entrega, caducidad).
6. Haga clic en **Aplicar**, luego en **Guardar** en la configuración maestra.

### Paso 5: (Opcional) Crear Especificaciones de Activación para Message-Driven Beans (MDBs)
Si utiliza MDBs para consumir de la cola, configure las especificaciones de activación.

1. Navegue a **Recursos > JMS > Especificaciones de activación**.
2. Seleccione el ámbito apropiado y haga clic en **Nuevo**.
3. Seleccione **Proveedor de mensajería predeterminado** y haga clic en **Aceptar**.
4. Ingrese los detalles:
   - **Nombre**: por ejemplo, `MyActivationSpec`.
   - **Nombre JNDI**: por ejemplo, `jms/activation/MyActivationSpec`.
   - **Nombre del bus**: Seleccione `MyJMSBus`.
   - **Tipo de destino**: Cola.
   - **Destino**: Ingrese el nombre JNDI de la cola (por ejemplo, `jms/MyQueue`).
5. Haga clic en **Aplicar**, luego en **Guardar** en la configuración maestra.

### Verificación y Pruebas
- Después de guardar, sincronice los nodos si está en un entorno agrupado.
- Reinicie el servidor.
- Utilice una aplicación cliente JMS para probar el envío/recepción de mensajes a través de los nombres JNDI.
- Monitoree a través de **Integración de servicios > Buses > [Su Bus] > Miembros del bus > [Su Miembro] > Motores de mensajería**.

Para configuraciones avanzadas (por ejemplo, seguridad, agrupamiento), consulte la documentación de IBM.

[Configuración de IBM WebSphere Application Server para Decision Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[Gestión de mensajería con el proveedor de mensajería predeterminado](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)