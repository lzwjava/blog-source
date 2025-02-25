---
audio: false
lang: es
layout: post
title: Comandos del servidor WebSphere Liberty
translated: true
---

Al gestionar un servidor WebSphere Liberty, se utilizan varios comandos con frecuencia para realizar tareas esenciales como crear, iniciar, detener y monitorear el servidor. A continuación se presenta una lista de los comandos más comúnmente utilizados, junto con una breve descripción de cada uno:

- **`./server create <server_name>`**
  Crea una nueva instancia del servidor con el nombre especificado. Este comando configura la estructura de directorios necesaria y los archivos de configuración predeterminados (por ejemplo, `server.xml`) para el servidor.

- **`./server start <server_name>`**
  Inicia el servidor en segundo plano. El servidor se ejecuta como un proceso en segundo plano y los registros se escriben en los archivos de registro del servidor.

- **`./server stop <server_name>`**
  Detiene una instancia del servidor en ejecución. Este comando detiene el servidor de manera ordenada.

- **`./server status <server_name>`**
  Verifica si el servidor especificado está en ejecución. Devuelve el estado actual (por ejemplo, iniciado o detenido).

- **`./server run <server_name>`**
  Inicia el servidor en primer plano. Esto es útil para la depuración o el monitoreo, ya que la salida del servidor se muestra directamente en la consola.

- **`./server package <server_name>`**
  Empaqueta el servidor, incluyendo su configuración y aplicaciones, en un archivo zip. Esto es útil para desplegar el servidor en otro entorno o para fines de respaldo.

- **`./server debug <server_name>`**
  Inicia el servidor en modo de depuración, permitiéndole adjuntar un depurador al proceso del servidor para solucionar problemas.

Estos comandos cubren las operaciones básicas necesarias para gestionar un servidor WebSphere Liberty de manera efectiva. Para tareas más avanzadas, como instalar características o gestionar la seguridad, están disponibles utilidades adicionales como `featureUtility` o `securityUtility`, aunque se utilizan menos frecuentemente en las operaciones diarias.