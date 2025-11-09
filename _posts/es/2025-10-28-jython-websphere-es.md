---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Jython en WebSphere Application Server
translated: true
type: note
---

### Uso de Jython en IBM WebSphere Application Server

Nota: "jPython" se refiere a Jython, una implementación de Python que se ejecuta en la Máquina Virtual de Java (JVM). Se utiliza comúnmente en WebSphere para scripting administrativo y también puede integrarse en aplicaciones desplegadas. WebSphere Application Server (WAS) incluye Jython (normalmente versión 2.1 o posterior, dependiendo de la versión de WAS) en `<WAS_HOME>/optionalLibraries/jython`, por lo que generalmente no se necesita una instalación por separado. A continuación, cubriré los dos casos de uso principales: tareas administrativas y uso en tiempo de ejecución en aplicaciones.

#### 1. Scripting Administrativo con wsadmin
La forma más común de usar Jython en WebSphere es para tareas de administración del servidor como desplegar aplicaciones, iniciar/detener servidores, configurar recursos y listar aplicaciones instaladas. Esto se hace mediante la herramienta `wsadmin`, que admite Jython como el lenguaje de scripting preferido (sobre el obsoleto Jacl).

**Prerrequisitos:**
- Asegúrese de que el servidor WebSphere esté en ejecución.
- Localice `wsadmin` en `<WAS_HOME>/bin/wsadmin.sh` (Linux/Unix) o `wsadmin.bat` (Windows).
- Jython viene preinstalado; para funciones más nuevas (por ejemplo, sintaxis de Python 2.5+), es posible que necesite actualizar mediante un classpath personalizado (consulte las notas avanzadas a continuación).

**Pasos Básicos para Ejecutar un Script de Jython:**
1. Cree un archivo de script Jython (por ejemplo, `example.py`) con su código. Utilice los objetos AdminConfig, AdminControl y AdminApp para operaciones específicas de WebSphere.
   
   Script de ejemplo para listar todas las aplicaciones instaladas (`listApps.py`):
   ```
   # List all applications
   apps = AdminApp.list()
   print("Installed Applications:")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # Optional: Save config changes
   ```

2. Ejecute el script usando `wsadmin`:
   - Conectarse vía SOAP (predeterminado para remoto):  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <hostname> -port <soap_port> -user <admin_user> -password <admin_pass>
     ```
   - Para local (sin host/puerto):  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - Ejemplo de salida: Lista aplicaciones como `DefaultApplication`.

3. Para modo interactivo (REPL):  
   ```
   wsadmin.sh -lang jython
   ```
   Luego escriba comandos de Jython directamente, por ejemplo, `print AdminApp.list()`.

**Ejemplos Comunes:**
- **Desplegar un EAR/WAR:** Crear `deployApp.py`:
  ```
  appName = 'MyApp'
  earPath = '/path/to/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('Deployed ' + appName)
  ```
  Ejecutar: `wsadmin.sh -lang jython -f deployApp.py`.

- **Iniciar/Detener Servidor:**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # Or 'stop'
  ```

- **Especificar Versión de Jython (si es necesario):** Para Jython 2.1 explícitamente:  
  `wsadmin.sh -usejython21 true -f script.py`. Para versiones personalizadas, agregue al classpath: `-wsadmin_classpath /path/to/jython.jar`.

**Consejos:**
- Use `AdminConfig.help('object_type')` para obtener ayuda sobre comandos.
- Los scripts se pueden automatizar en CI/CD (por ejemplo, Jenkins) llamando a `wsadmin` en archivos por lotes.
- Para cliente ligero (sin instalación completa de WAS): Descargue los jars cliente de IBM y configure el classpath.

#### 2. Uso de Jython en Aplicaciones Desplegadas
Para ejecutar código Jython dentro de una aplicación Java (por ejemplo, servlet o EJB) que se ejecuta en WebSphere, incluya el runtime de Jython (jython.jar) en el classpath de la aplicación. Esto permite incrustar scripts de Python o usar Jython como un motor de scripting. Descargue el jython.jar más reciente del sitio oficial de Jython si la versión incluida está desactualizada.

Hay dos métodos principales: **Classpath** (a nivel de servidor) o **Biblioteca Compartida** (reutilizable entre aplicaciones).

**Método 1: Classpath (Adición Directa a la JVM)**
1. Guarde `jython.jar` en una ruta accesible en el host de WebSphere (por ejemplo, `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`).
2. Inicie sesión en la Consola de Administración de WebSphere.
3. Navegue a **Servers > Server Types > WebSphere application servers > [Su Servidor]**.
4. Vaya a **Java and Process Management > Process definition > Java Virtual Machine > Classpath**.
5. Agregue la ruta completa a `jython.jar` (por ejemplo, `/opt/.../jython.jar`).
6. En **Generic JVM arguments**, agregue la ruta de Python:  
   `-Dpython.path=/opt/.../jython.jar/Lib` (apunta a la biblioteca estándar de Jython).
7. Haga clic en **OK**, guarde la configuración y reinicie el servidor.
8. Sincronice los nodos si está en un entorno clusterizado (vía **System administration > Nodes > Synchronize**).
9. En su código Java, use `org.python.util.PythonInterpreter` para ejecutar scripts de Jython:
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hello from Jython in WebSphere!')");
   ```

**Método 2: Biblioteca Compartida (Recomendado para Múltiples Aplicaciones)**
1. Coloque `jython.jar` en un directorio compartido (por ejemplo, `/shared/libs/jython.jar`).
2. En la Consola de Administración: **Environment > Shared libraries > [Ámbito: Server o Cell] > New**.
3. Ingrese un nombre (por ejemplo, `JythonLib`), marque **Use a native library directory**, y establezca **Classpath** en `/shared/libs/jython.jar`.
4. Guarde.
5. Para una aplicación específica: **Applications > Application Types > WebSphere enterprise applications > [Su App] > Reference shared libraries**.
6. En **Shared library references**, haga clic en **Add**, seleccione `JythonLib`, y establezca **Classpath** para que coincida.
7. Guarde, actualice la aplicación (reinicie si es necesario) y sincronice los nodos.
8. Haga referencia en el código como en el método Classpath.

**Consejos para Aplicaciones:**
- Para aplicaciones Jython basadas en servlets, use PyServlet (incluido en Jython) para manejadores Python.
- Pruebe en un entorno de desarrollo; monitoree los registros para detectar problemas de classpath.
- Si usa una versión más nueva de Jython (por ejemplo, 2.7), asegúrese de la compatibilidad con Java 8+.

#### Notas Avanzadas
- **Compatibilidad de Versiones:** WAS 9.x usa Jython 2.7+. Para actualizaciones, reemplace el jar incluido pero pruebe exhaustivamente.
- **Manejo de Errores:** En scripts, use `try: ... except Exception as e: print(e)`.
- **Soporte para IDE:** Use IBM Rational Application Developer (RAD) o Eclipse con plugins de WebSphere para depurar scripts Jython/wsadmin.
- **Recursos:** Para tutoriales completos, consulte el libro *WebSphere Application Server Administration Using Jython* o la documentación de wsadmin de IBM.

Si esto no coincide con su escenario exacto (por ejemplo, versión específica de WAS o caso de uso), proporcione más detalles para un consejo personalizado.

**Referencias:**  
- [Using wsadmin scripting with Jython (IBM Docs)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [Deploying Jython on WebSphere (Oracle Guide)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [WebSphere Jython Integration (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [Jython Wiki on WebSphere](https://wiki.python.org/jython/WebSphere)  
- [Deploy App with Jython Example](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)