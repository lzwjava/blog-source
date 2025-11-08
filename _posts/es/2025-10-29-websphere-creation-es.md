---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Creación Correcta de WebSphere Application Server
translated: true
type: note
---

No, el comando `nodeName -name serverName admin create applciation server` (notando el error tipográfico en "applciation") no es correcto para crear un servidor de aplicaciones en IBM WebSphere Application Server (WAS) usando scripts de wsadmin.

### Sintaxis Correcta
El comando apropiado utiliza el método `AdminTask.createApplicationServer` en Jython (el lenguaje de script recomendado para wsadmin). Requiere:
- El **nombre del nodo** como primer argumento (una cadena de texto).
- Una **lista de opciones** como segundo argumento, incluyendo `-name` para el nombre del servidor.

**Ejemplo básico:**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- Reemplaza `'YourNodeName'` con el nodo real (por ejemplo, `ndnode1`).
- Reemplaza `'YourServerName'` con el nombre deseado para el servidor (por ejemplo, `appServer1`).
- Se pueden agregar parámetros opcionales a la lista, como `'-templateName', 'default'` para usar una plantilla de servidor predeterminada.

### Pasos para Ejecutarlo
1. Inicia wsadmin en modo Jython: `./wsadmin.sh -lang jython -user admin -password pass`.
2. Ejecuta el comando anterior.
3. Guarda la configuración: `AdminConfig.save()`.
4. Sal: `quit`.

Esto crea un servidor de aplicaciones básico en el nodo especificado. Para más opciones (por ejemplo, puertos, configuraciones JVM), consulta la documentación completa de AdminTask.

[Grupo de comandos ServerManagement para el objeto AdminTask](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[Creación de un servidor usando scripts](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)