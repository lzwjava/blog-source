---
audio: false
generated: true
lang: es
layout: post
title: Instalación de Paquetes .deb en Ubuntu
translated: true
type: note
---

Si has descargado un archivo `.deb` en tu sistema Ubuntu y deseas instalarlo, existen algunos métodos sencillos para hacerlo. A continuación, explicaré el enfoque más recomendado usando la terminal, así como una opción gráfica si prefieres una solución de apuntar y hacer clic.

### **Método 1: Instalar mediante la Terminal (Recomendado)**
La forma más fácil y confiable de instalar un archivo `.deb` en Ubuntu es usando el comando `apt`, que no solo instala el paquete sino que también resuelve automáticamente cualquier dependencia requerida. Así es cómo se hace:

1. **Abre la Terminal**: Puedes hacerlo presionando `Ctrl + Alt + T` o buscando "Terminal" en el menú de aplicaciones.
2. **Navega a la Ubicación del Archivo** (opcional): Si tu archivo `.deb` está en una carpeta específica (por ejemplo, la carpeta Descargas), usa el comando `cd` para ir allí. Por ejemplo:
   ```bash
   cd ~/Downloads
   ```
   Si no deseas cambiar de directorio, puedes especificar la ruta completa al archivo en el siguiente paso.
3. **Ejecuta el Comando de Instalación**: Usa el siguiente comando, reemplazando `nombre_del_paquete.deb` con el nombre real de tu archivo `.deb`:
   ```bash
   sudo apt install ./nombre_del_paquete.deb
   ```
   - Si el archivo está en un directorio diferente, proporciona la ruta completa, así:
     ```bash
     sudo apt install /home/usuario/Downloads/nombre_del_paquete.deb
     ```
   - El `./` antes del nombre del archivo le indica a `apt` que busque un archivo local en lugar de un paquete en los repositorios.
4. **Ingresa tu Contraseña**: Cuando se te solicite, escribe tu contraseña de usuario y presiona Enter. El comando `sudo` requiere privilegios administrativos.
5. **Espera a que Finalice la Instalación**: `apt` instalará el archivo `.deb` y descargará las dependencias necesarias desde los repositorios de Ubuntu. Si hay problemas (por ejemplo, dependencias faltantes que no se encuentran en los repositorios), te lo hará saber.

Este método funciona en Ubuntu 16.04 y versiones posteriores, ya que utiliza una característica de `apt` introducida en la versión 1.1. Es recomendable porque combina simplicidad con gestión de dependencias.

### **Método 2: Instalar mediante la Interfaz Gráfica**
Si prefieres no usar la terminal, las herramientas gráficas de Ubuntu también pueden manejar archivos `.deb`:
1. **Localiza el Archivo**: Abre tu administrador de archivos (por ejemplo, Nautilus) y navega a la carpeta que contiene el archivo `.deb` (probablemente Descargas).
2. **Haz Doble Clic en el Archivo**: Esto debería abrir automáticamente el archivo con el Centro de Software de Ubuntu (o una aplicación similar, dependiendo de tu versión de Ubuntu).
3. **Haz Clic en Instalar**: En la ventana del Centro de Software, haz clic en el botón "Instalar". Es posible que se te solicite tu contraseña.
4. **Espera a que Finalice**: La instalación procederá y verás una confirmación una vez que esté lista.

Este método es fácil de usar pero requiere un entorno de escritorio y puede no proporcionar información detallada si algo sale mal.

### **Notas Importantes**
- **Fuentes Confiables**: Solo instala archivos `.deb` de fuentes en las que confíes, ya que potencialmente pueden dañar tu sistema si contienen código malicioso.
- **Verifica la Instalación**: Después de instalar, puedes verificar que el software esté instalado ejecutando:
  ```bash
  dpkg -l | grep nombre_del_paquete
  ```
  (Reemplaza `nombre_del_paquete` con el nombre del software, no con el nombre completo del archivo `.deb`).
- **Problemas de Dependencias**: Si `apt` no puede resolver las dependencias, es posible que necesites encontrarlas e instalarlas manualmente o usar una versión diferente del archivo `.deb` compatible con tu sistema.

### **Ejemplo**
Supongamos que descargaste un archivo llamado `vscode.deb` en tu carpeta de Descargas. Abre una terminal y ejecuta:
```bash
sudo apt install ~/Downloads/vscode.deb
```
Esto instalará Visual Studio Code (o lo que sea que contenga el paquete) junto con sus dependencias.

¡Eso es todo! Ahora tienes tu archivo `.deb` instalado en Ubuntu. ¡Avísame si tienes algún problema!