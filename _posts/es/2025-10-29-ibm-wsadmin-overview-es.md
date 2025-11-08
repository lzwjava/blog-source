---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de la Herramienta wsadmin de IBM WebSphere
translated: true
type: note
---

### Resumen de wsadmin en IBM WebSphere Application Server (WAS)

La herramienta `wsadmin` es una interfaz de scripting por línea de comandos para administrar WebSphere Application Server. Permite automatizar tareas como gestionar servidores, desplegar aplicaciones, configurar recursos y monitorizar operaciones en tiempo de ejecución. Los scripts se pueden escribir en Jython (basado en Python) o JACL (basado en Tcl), siendo Jython el más utilizado comúnmente debido a su legibilidad.

- **`wsadmin.bat`**: Se utiliza en sistemas Windows.
- **`wsadmin.sh`**: Se utiliza en sistemas Unix/Linux/AIX.

Ambas herramientas se encuentran en el directorio `bin` de un perfil de WebSphere (por ejemplo, `<WAS_HOME>/profiles/<ProfileName>/bin/`) o en la instalación base (`<WAS_HOME>/bin/`). Se recomienda ejecutarlas desde el directorio `bin` del perfil para asegurar el entorno correcto.

#### Iniciar wsadmin de forma interactiva
Esto inicia un shell donde puedes introducir comandos directamente.

**Sintaxis:**
```
wsadmin[.bat|.sh] [opciones]
```

**Ejemplo básico (Windows):**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**Ejemplo básico (Unix/Linux):**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`: Especifica Jython (usa `-lang jacl` para JACL).
- `-user` y `-password`: Requeridos si la seguridad global está activada (omítelos si está desactivada).
- Si se omiten, se conecta al servidor local usando el conector SOAP por defecto en el puerto 8879 (o RMI en el 2809).

Una vez en el prompt de wsadmin (por ejemplo, `wsadmin>`), puedes ejecutar comandos usando objetos de scripting:
- **AdminConfig**: Para cambios de configuración (por ejemplo, crear recursos).
- **AdminControl**: Para operaciones en tiempo de ejecución (por ejemplo, iniciar/detener servidores).
- **AdminApp**: Para el despliegue/actualización de aplicaciones.
- **AdminTask**: Para tareas de alto nivel (por ejemplo, sincronizar nodos).
- **Help**: Para la ayuda integrada (por ejemplo, `Help.help()`).

**Comandos de ejemplo en el Shell:**
- Listar todos los servidores: `print AdminConfig.list('Server')`
- Iniciar un servidor: `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- Guardar cambios: `AdminConfig.save()`
- Salir: `quit`

#### Ejecutar un archivo de script
Usa la opción `-f` para ejecutar un script Jython (.py o .jy) o JACL (.jacl) de forma no interactiva.

**Script de ejemplo (deployApp.py):**
```python
# Conectar y desplegar una aplicación
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**Ejecutar en Windows:**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**Ejecutar en Unix/Linux:**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### Ejecutar un solo comando
Usa la opción `-c` para comandos únicos (útil en archivos por lotes o automatización).

**Ejemplo (fragmento de archivo por lotes de Windows):**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**Ejemplo (fragmento de script de shell de Unix):**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### Opciones clave

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `-conntype` | Tipo de conector: `SOAP` (por defecto, puerto 8879) o `RMI` (puerto 2809). | `-conntype RMI` |
| `-host` | Host remoto al que conectarse. | `-host myhost.example.com` |
| `-port` | Puerto del conector. | `-port 8879` |
| `-tracefile` | Registrar la salida en un archivo. | `-tracefile wsadmin.log` |
| `-profile` | Ejecutar un script de perfil antes del script principal. | `-profile init.py` |
| `-c` | Ejecutar un solo comando (no interactivo). | `-c "AdminConfig.save()"` |
| `-f` | Ejecutar un archivo de script. | `-f myscript.py` |
| `-job` | Ejecutar un comando del job manager. | `-job deploy.xml` |

#### Consejos y mejores prácticas
- **Seguridad**: Si la seguridad global está desactivada, omite `-user` y `-password`. Para configuraciones seguras, usa credenciales cifradas o archivos de claves.
- **Modo Thin Client**: Para administración remota sin una instalación completa de WAS, usa `wsadmin -conntype NONE` con los JARs del thin client (por ejemplo, `com.ibm.ws.admin.client_*.jar`).
- **Rendimiento**: Para múltiples comandos, usa un solo script con `-f` en lugar de llamadas repetidas con `-c` para evitar la sobrecarga de la JVM.
- **Manejo de errores**: Siempre llama a `AdminConfig.save()` después de los cambios de configuración. Usa try-except en Jython para robustez.
- **Generar comandos**: En la Consola de Administración de WAS, realiza una acción y haz clic en "View administrative scripting command for last action" para obtener el comando equivalente de wsadmin.
- **Notas de versión**: El comportamiento es consistente en WAS 8.5+ y 9.0+, pero consulta la documentación de IBM para detalles específicos de versión (por ejemplo, Jython 2.7 en versiones más recientes).

Para un uso más avanzado, explora el objeto AdminTask para comandos simplificados como `AdminTask.importFile('path/to/file')`.

### Referencias
- [wsadmin scripting tool - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [Getting started with wsadmin scripting - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) Tutorial](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - Getting Started with wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN Tutorial – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)