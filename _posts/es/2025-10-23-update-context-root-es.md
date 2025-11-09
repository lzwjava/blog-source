---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Actualización de la Ruta de Contexto de WebSphere
translated: true
type: note
---

### Actualización de la raíz de contexto web en IBM WebSphere Application Server (WAS)

La raíz de contexto web define la ruta URL base para su aplicación web (por ejemplo, `/miapp`). En IBM WebSphere Application Server, puede actualizarla durante el despliegue inicial o para una aplicación existente a través de la Consola Administrativa. A continuación, se detallan los pasos para una aplicación existente. Asegúrese de tener acceso administrativo a la consola de WAS.

#### Prerrequisitos
- Acceso a la Consola Administrativa de WebSphere (normalmente en `https://su-servidor:9043/ibm/console`).
- La aplicación debe estar instalada y detenida (recomendado) antes de realizar cambios para evitar conflictos.

#### Pasos para actualizar la raíz de contexto
1. **Iniciar sesión en la Consola Administrativa**:
   - Abra un navegador web y navegue a la URL de la consola de WAS.
   - Ingrese sus credenciales de administrador.

2. **Navegar a la Aplicación**:
   - En el panel de navegación izquierdo, expanda **Applications** > **Application Types** > **WebSphere enterprise applications**.
   - Ubique y seleccione su aplicación desplegada de la lista.

3. **Acceder a la configuración de la raíz de contexto**:
   - En la página de detalles de la aplicación, desplácese hacia abajo hasta la sección **Web Module Properties**.
   - Haga clic en **Context root for web modules**.

4. **Editar la raíz de contexto**:
   - En la tabla que aparece, encuentre el módulo web (por ejemplo, el nombre de su archivo WAR).
   - Actualice el campo **Context root** con el nuevo valor (por ejemplo, cambie de `/appantigua` a `/appnueva`). Evite las barras iniciales si no son necesarias, pero inclúyalas para rutas como `/miapp`.
   - Haga clic en **OK** para guardar los cambios.

5. **Guardar y sincronizar la configuración**:
   - Haga clic en **Save** en la consola (o en **Save directly to the master configuration** si se le solicita).
   - Si se encuentra en un entorno de despliegue en clúster o de red:
     - Vaya a **System administration** > **Nodes**.
     - Seleccione todos los nodos relevantes y haga clic en **Full Resynchronize**.

6. **Reiniciar la aplicación**:
   - Regrese a **Applications** > **WebSphere enterprise applications**.
   - Seleccione su aplicación y haga clic en **Stop**, luego en **Start**.
   - Alternativamente, reinicie el servidor completo a través de **Servers** > **Server Types** > **WebSphere application servers** > seleccione el servidor > **Restart**.

7. **Verificar el cambio**:
   - Acceda a la URL de la aplicación en un navegador (por ejemplo, `http://su-servidor:9080/appnueva`).
   - Revise los registros del servidor (por ejemplo, `SystemOut.log`) en busca de errores relacionados con el despliegue.

#### Notas adicionales
- **Durante el despliegue inicial**: Si despliega una aplicación nueva, especifique la raíz de contexto en el paso **Select installation options** bajo **Context root** para cada módulo web.
- **Archivos EAR**: Para aplicaciones empaquetadas en un EAR, asegúrese de que el `application.xml` no codifique de forma rígida la raíz de contexto; las anulaciones en la consola tienen prioridad.
- **Problemas comunes**:
  - Es posible que los cambios no se apliquen si la aplicación está en ejecución—siempre deténgala primero.
  - En WebSphere Liberty u Open Liberty, utilice configuraciones del `server.xml` en su lugar.
  - Para hosts virtuales o plugins, actualice la configuración del plugin del servidor web después de los cambios.
- Si la aplicación utiliza seguridad o bibliotecas compartidas, realice pruebas exhaustivas después de la actualización.

Para más detalles, consulte la documentación oficial de IBM o las guías de la comunidad.

#### Referencias
- [Configuración de la raíz de contexto para módulos web](https://www.ibm.com/docs/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/uweb_contextroot.html)
- [IBM WebSphere - Raíz de contexto de una aplicación](https://www.freekb.net/Article?id=1647)
- [El cambio de la raíz de contexto en WebSphere 8.5 no se aplica al archivo WAR](https://stackoverflow.com/questions/24472790/websphere-8-5-context-root-change-not-applying-to-war-file)