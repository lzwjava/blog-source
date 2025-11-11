---
audio: false
generated: true
lang: es
layout: post
title: Instalar el Cliente de Outline en Ubuntu
translated: true
type: note
---

Sí, puedes instalar el Outline Client en Ubuntu, ya que es una distribución de Linux basada en Debian, y el Outline Client se proporciona como un paquete Debian, que es compatible con Ubuntu. Hay dos métodos para instalarlo: el método recomendado que utiliza el repositorio y un método alternativo que consiste en descargar el paquete Debian directamente. A continuación, explicaré cómo hacerlo usando el método recomendado del repositorio, que es preferible porque se integra con el gestor de paquetes de Ubuntu, haciendo que las actualizaciones sean más fáciles de gestionar.

### Pasos para instalar Outline Client en Ubuntu (Método Recomendado)

Sigue estos pasos para instalar el Outline Client en tu sistema Ubuntu:

1. **Abre una Terminal**  
   Inicia la aplicación de terminal en tu sistema Ubuntu. Puedes hacerlo buscando "Terminal" en el menú de aplicaciones o presionando `Ctrl + Alt + T`.

2. **Instala la Clave del Repositorio de Outline**  
   Ejecuta el siguiente comando para descargar y añadir la clave de firma del repositorio a las claves confiables de tu sistema. Esto asegura que los paquetes del repositorio sean verificados para autenticidad:
   ```bash
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   ```

3. **Añade el Repositorio de Outline Client**  
   Añade el repositorio de Outline Client a la lista de fuentes de tu sistema ejecutando este comando. Esto le indica a Ubuntu dónde encontrar el paquete de Outline Client:
   ```bash
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
   - Nota: La parte `[arch=amd64]` especifica que esto es para sistemas de 64 bits. La mayoría de las instalaciones modernas de Ubuntu son de 64 bits, pero puedes confirmar la arquitectura de tu sistema ejecutando `uname -m`. Si el resultado es `x86_64`, estás usando un sistema de 64 bits y este comando funcionará tal cual.

4. **Actualiza la Lista de Paquetes**  
   Actualiza la lista de paquetes de tu sistema para incluir el repositorio de Outline recién añadido:
   ```bash
   sudo apt update
   ```

5. **Instala el Outline Client**  
   Instala la última versión del Outline Client con este comando:
   ```bash
   sudo apt install outline-client
   ```

### Después de la Instalación

- **Iniciar el Outline Client**: Después de la instalación, puedes encontrar el Outline Client en el menú de aplicaciones o iniciarlo desde la terminal escribiendo `outline-client`.
- **Mantenerlo Actualizado**: Para buscar e instalar actualizaciones, usa los comandos de actualización estándar de Ubuntu:
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
  Estos comandos actualizarán todos los paquetes instalados, incluido el Outline Client, ya que se gestiona a través del repositorio. Ten en cuenta que las actualizaciones automáticas dentro de la aplicación están deshabilitadas para el Outline Client en Linux a partir de la versión 1.15, por lo que confiar en el gestor de paquetes es la mejor manera de mantenerse actualizado.
- **Desinstalar**: Si necesitas eliminar el Outline Client, ejecuta:
  ```bash
  sudo apt purge outline-client
  ```

### ¿Por qué usar el método recomendado?

El método del repositorio es recomendado porque:
- Se integra con el gestor de paquetes `apt` de Ubuntu, permitiéndote actualizar el Outline Client junto con otros paquetes del sistema.
- No necesitas descargar e instalar manualmente nuevas versiones, a diferencia del método alternativo donde tendrías que repetir el proceso de descarga e instalación para cada actualización.

### Suposiciones y Requisitos

- **Versión de Ubuntu**: Las instrucciones no especifican una versión mínima de Ubuntu, pero dado que Ubuntu está basado en Debian y el paquete está dirigido a sistemas de 64 bits, cualquier versión reciente de Ubuntu de 64 bits debería funcionar. Para mayor seguridad, asegúrate de que tu sistema esté actualizado ejecutando `sudo apt update && sudo apt upgrade` antes de comenzar.
- **Arquitectura**: Estas instrucciones asumen un sistema de 64 bits (amd64). Si estás usando una arquitectura diferente (por ejemplo, 32 bits o ARM), este método no funcionará tal como se proporciona, y necesitarías buscar paquetes alternativos o contactar al soporte de Outline.

### Método Alternativo (Opcional)

Si prefieres no añadir un repositorio, puedes descargar e instalar el paquete Debian directamente:
1. Descarga el paquete:
   ```bash
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   ```
2. Instálalo:
   ```bash
   sudo apt install ./outline-client.deb
   ```
Sin embargo, necesitarás repetir este proceso manualmente para las actualizaciones, lo que es menos conveniente.

### Conclusión

Usando el método recomendado del repositorio, puedes instalar y mantener fácilmente el Outline Client en Ubuntu. Solo sigue los pasos anteriores, y lo tendrás funcionando con la capacidad de mantenerlo actualizado sin esfuerzo a través del gestor de paquetes de tu sistema.