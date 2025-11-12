---
audio: false
generated: true
lang: es
layout: post
title: Instalar VLC Media Player en Ubuntu
translated: true
type: note
---

Para instalar VLC media player en tu sistema Ubuntu, puedes usar la terminal (línea de comandos) o el Centro de software de Ubuntu (interfaz gráfica). A continuación, se muestran instrucciones detalladas para ambos métodos.

---

### **Método 1: Instalar VLC usando la Terminal**

Este método es rápido y eficiente, especialmente si te sientes cómodo con la línea de comandos. Sigue estos pasos:

1. **Abre la Terminal**
   - Busca "Terminal" en el menú de aplicaciones de Ubuntu, o presiona `Ctrl + Alt + T` para abrirla.

2. **Actualiza la lista de paquetes**
   - Antes de instalar software, es una buena práctica asegurarse de que tu lista de paquetes esté actualizada. Ejecuta este comando:
     ```bash
     sudo apt update
     ```
   - Ingresa tu contraseña cuando se te solicite. Este comando actualiza la lista de paquetes de software disponibles.

3. **Instala VLC**
   - Una vez que la lista de paquetes esté actualizada, instala VLC ejecutando:
     ```bash
     sudo apt install vlc
     ```
   - Necesitarás ingresar tu contraseña nuevamente. El sistema puede pedirte que confirmes la instalación escribiendo `y` y presionando Enter. Esto descargará e instalará VLC junto con sus dependencias necesarias.

4. **Verifica la instalación**
   - Después de la instalación, verifica si VLC está instalado escribiendo:
     ```bash
     vlc
     ```
   - Esto debería iniciar el reproductor multimedia VLC. Si se abre, la instalación fue exitosa.
   - Alternativamente, puedes verificar la versión de VLC ejecutando:
     ```bash
     vlc --version
     ```
   - Esto mostrará algo como "VLC media player 3.0.11.1 Vetinari" (el número de versión puede variar).

5. **Opcional: Prueba VLC**
   - Para asegurarte de que VLC funciona correctamente, intenta reproducir un archivo multimedia. Por ejemplo, si tienes un archivo MP4 en tu escritorio, haz clic derecho sobre él y selecciona "Abrir con VLC media player". Si se reproduce, VLC está completamente funcional.

---

### **Método 2: Instalar VLC usando el Centro de software de Ubuntu**

Si prefieres una interfaz gráfica en lugar de la terminal, usa el Centro de software de Ubuntu:

1. **Abre el Centro de software de Ubuntu**
   - Busca "Ubuntu Software" en el menú de aplicaciones y haz clic para abrirlo.

2. **Busca VLC**
   - En el Centro de software, haz clic en el icono de búsqueda (generalmente una lupa) y escribe "VLC" en la barra de búsqueda.

3. **Instala VLC**
   - Encuentra "VLC media player" en los resultados de búsqueda, haz clic en él y luego haz clic en el botón "Instalar". Es posible que necesites ingresar tu contraseña para autorizar la instalación.

4. **Inicia VLC**
   - Una vez instalado, puedes iniciar VLC directamente desde el Centro de software haciendo clic en "Abrir" (si está disponible) o buscando "VLC" en el menú de aplicaciones.

---

### **Notas Adicionales**

- **Mantener VLC actualizado**
  - Si instalaste VLC usando la terminal, puedes mantenerlo actualizado ejecutando periódicamente:
    ```bash
    sudo apt update
    sudo apt upgrade
    ```
  - Esto actualiza VLC junto con otros paquetes del sistema. Si usaste el Centro de software, las actualizaciones generalmente se gestionan a través de la misma interfaz.

- **Plugins y códecs**
  - La instalación predeterminada de VLC a través de `sudo apt install vlc` incluye plugins esenciales (como `vlc-plugin-base`) y códecs, por lo que debería poder reproducir la mayoría de los formatos multimedia comunes (por ejemplo, MP4, AVI) listos para usar. Si encuentras problemas con tipos de archivo específicos, puedes instalar códecs adicionales más tarde, como `ubuntu-restricted-extras`, usando:
    ```bash
    sudo apt install ubuntu-restricted-extras
    ```

- **Instalación alternativa vía Snap**
  - VLC también está disponible como un paquete Snap. Si prefieres este método, ejecuta:
    ```bash
    sudo snap install vlc
    ```
  - Sin embargo, el método `apt` es recomendado para la mayoría de los usuarios ya que se integra bien con el sistema.

---

Siguiendo cualquiera de los métodos, tendrás VLC instalado y listo para usar en tu sistema Ubuntu. El método de terminal es más rápido para los usuarios de línea de comandos, mientras que el Centro de software es ideal para aquellos que prefieren un enfoque gráfico. ¡Disfruta de tu reproducción multimedia!

---

Para solucionar el error que estás encontrando al reproducir un archivo MKV en VLC en Ubuntu—específicamente el mensaje sobre los decodificadores faltantes MPEG-4 AAC y H.265—sigue los pasos a continuación. Este problema generalmente ocurre porque Ubuntu no incluye ciertos códecs propietarios por defecto debido a restricciones de licencia. Instalar paquetes de códecs adicionales debería resolver el problema.

---

### **Solución**

#### **Paso 1: Instalar el paquete `ubuntu-restricted-extras`**
Este paquete proporciona soporte para una variedad de códecs, incluidos MPEG-4 AAC (audio) y H.265 (HEVC) video, que probablemente faltan en tu instalación de VLC.

1. **Abre la Terminal**
   - Busca "Terminal" en el menú de aplicaciones de Ubuntu o presiona `Ctrl + Alt + T`.

2. **Actualiza la lista de paquetes**
   - Ejecuta este comando para asegurarte de que la lista de paquetes de tu sistema esté actualizada:
     ```bash
     sudo apt update
     ```

3. **Instala `ubuntu-restricted-extras`**
   - Ejecuta el siguiente comando:
     ```bash
     sudo apt install ubuntu-restricted-extras
     ```
   - Es posible que necesites ingresar tu contraseña. Durante la instalación, es posible que se te solicite aceptar el Acuerdo de Licencia de Usuario Final (EULA) para ciertos componentes—sigue las instrucciones en pantalla para aceptar y proceder.

4. **Reinicia VLC**
   - Cierra VLC si está abierto, luego ábrelo de nuevo e intenta reproducir el archivo MKV nuevamente.

---

#### **Paso 2: Instalar paquetes de códecs adicionales (si es necesario)**
Si el error persiste después del Paso 1, instala paquetes específicos que proporcionan soporte adicional para H.265 y otros códecs.

1. **Instala `libde265-0` y `libavcodec-extra`**
   - Ejecuta este comando para instalar bibliotecas para la decodificación H.265 y soporte de códecs extra:
     ```bash
     sudo apt install libde265-0 libavcodec-extra
     ```

2. **Reinicia VLC**
   - Cierra y vuelve a abrir VLC, luego intenta reproducir el archivo MKV nuevamente.

---

#### **Paso 3: Solución de problemas adicional (si es necesario)**
Si el problema aún no se resuelve, prueba estos pasos adicionales:

- **Verifica la versión de VLC**
  - Asegúrate de estar usando la última versión de VLC. Verifica tu versión actual con:
    ```bash
    vlc --version
    ```
  - Si está desactualizada, actualízala ejecutando:
    ```bash
    sudo apt update
    sudo apt upgrade vlc
    ```

- **Prueba con otro archivo MKV**
  - Reproduce un archivo MKV diferente para ver si el problema es específico de un archivo. Si otros archivos funcionan, el archivo problemático podría estar corrupto o usar una codificación no compatible.

- **Consulta los registros de VLC para más detalles**
  - Para una solución de problemas avanzada, ejecuta VLC desde la terminal con salida detallada:
    ```bash
    vlc --verbose 2
    ```
  - Intenta reproducir el archivo y busca mensajes de error detallados sobre los códecs faltantes.

---

### **Notas Adicionales**
- **Por qué sucede esto**: MKV es un formato contenedor que puede usar varios códecs como MPEG-4 AAC para audio y H.265 para video. La instalación predeterminada de VLC en Ubuntu podría carecer de estos debido a restricciones legales sobre software propietario.
- **Aceleración por hardware**: Si tu sistema admite la decodificación por hardware de H.265 (por ejemplo, a través de una GPU moderna), asegúrate de que tus controladores de gráficos estén actualizados. Sin embargo, este error sugiere un decodificador de software faltante, por lo que es probable que la aceleración por hardware no sea el problema principal.
- **Próximos pasos**: Si nada de lo anterior funciona, considera reinstalar VLC o buscar ayuda en los foros de Ubuntu o VLC con detalles sobre tu sistema y el archivo MKV específico.

---

Siguiendo estos pasos, deberías poder solucionar los errores de decodificadores faltantes y reproducir tus archivos MKV en VLC exitosamente. Comienza con el Paso 1, ya que es la solución más directa y probable.