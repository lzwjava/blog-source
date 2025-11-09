---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Transferencia de Medios a Disco Externo
translated: true
type: note
---

### Mover fotos y videos a un disco portátil en macOS

Según la información de tu sistema, tienes un sistema macOS 15.6.1 con un disco portátil montado en `/Volumes/Untitled` (capacidad total 2.0 TB, 1.5 TB disponibles). Mover fotos y videos implica transferir archivos desde el almacenamiento de tu Mac (por ejemplo, en `~/Pictures` para fotos o `~/Movies` para videos) al disco externo. Esto se puede hacer mediante la interfaz gráfica (Finder) o herramientas de línea de comandos como Terminal, dependiendo de tu preferencia. A continuación cubriré ambos métodos, asumiendo que estás moviendo archivos y no la biblioteca completa de la aplicación Fotos (si eso es necesario, primero expórtalos desde la aplicación Fotos).

**Notas importantes:**
- **Haz una copia de seguridad primero:** Asegúrate de tener copias de seguridad de tus archivos para evitar pérdida de datos en caso de errores.
- **Permisos:** Es posible que necesites permisos de administrador para ciertas acciones. Ejecuta los comandos de Terminal como administrador si se te solicita.
- **Verificar espacio:** Confirma que el tamaño de los archivos no exceda el espacio disponible en el disco portátil (1.5 TB en tu caso).
- **Ubicaciones de archivos:** Las rutas predeterminadas son `~/Pictures` para fotos y `~/Movies` para videos. Si están en otros directorios (por ejemplo, Descargas), ajústalo en consecuencia.
- **Desmontar de forma segura:** Después de mover, desmonta el disco mediante Finder > Expulsar o `diskutil unmount /Volumes/Untitled` para evitar corrupción.

#### 1. Usar Finder (Método gráfico - Ideal para principiantes)
Esta es la forma más simple para la mayoría de usuarios. Implica arrastrar y soltar mediante el administrador de archivos de macOS.

1. **Localizar el disco portátil y los archivos:**
   - Abre Finder (haz clic en el icono de la cara sonriente en el Dock).
   - En la barra lateral, en "Ubicaciones", verás "Untitled" (tu disco portátil). Haz clic en él para explorar su contenido.
   - Abre una ventana separada de Finder (Comando + N) y navega a donde estén almacenados tus fotos/videos (por ejemplo, tu carpeta de Imágenes o Películas).

2. **Mover los archivos:**
   - Selecciona las fotos/videos que quieras mover (mantén presionada la tecla Comando para selección múltiple).
   - Arrástralos desde su ubicación actual a la ventana del disco portátil (por ejemplo, crea primero una carpeta como "PhotosBackup" en el disco para organizarte).
   - Para mover (reubicar permanentemente, liberando espacio en tu Mac), mantén presionada la tecla Opción mientras arrastras. Para copiar (duplicar), simplemente arrastra normalmente.
     - Alternativamente, haz clic derecho en los archivos seleccionados > "Mover a la Papelera" después de copiar para "moverlos" efectivamente eliminando los originales después de la copia.
   - Si te organizas, crea carpetas en el disco (clic derecho > Nueva carpeta) como "Photos" y "Videos".

3. **Verificar y expulsar:**
   - Abre el disco portátil en Finder y confirma que los archivos estén allí.
   - Arrastra el icono del disco a la Papelera (o clic derecho > Expulsar) para desmontar de forma segura antes de desconectarlo.

Este método preserva los metadatos (por ejemplo, fechas de creación) y maneja archivos grandes de manera eficiente.

#### 2. Usar Terminal (Método de línea de comandos - Eficiente para operaciones masivas)
Si prefieres el uso de scripts o manejar mediante comandos (como se muestra en tus scripts de Python), usa Terminal para mayor precisión. Esto es útil para movimientos automatizados o recursivos.

1. **Navegar a tus archivos y al disco:**
   - Abre Terminal (Aplicaciones > Utilidades > Terminal).
   - Verifica tu directorio actual: Ejecuta `pwd` y navega según sea necesario (por ejemplo, `cd ~/Pictures` para acceder a las fotos).
   - Confirma que el disco esté montado: Ejecuta `ls /Volumes` para ver "Untitled". Tu disco ya está montado según la salida proporcionada.

2. **Mover los archivos:**
   - Para **mover** archivos (reubicar permanentemente, eliminando de la ubicación original):
     - Para archivos individuales: `mv /ruta/a/photo.jpg /Volumes/Untitled/Photos/`
     - Para directorios (por ejemplo, carpeta completa de Fotos): `mv ~/Pictures/PhotosLibrary /Volumes/Untitled/`
     - Ejemplo de movimiento completo: `mv ~/Pictures/* /Volumes/Untitled/Photos/` (mueve todos los contenidos desde Imágenes a una nueva carpeta en el disco; añade opciones como `-v` para salida detallada).
   - Para **copiar** en su lugar (duplicar sin eliminar originales): Usa `cp` con `-r` para directorios recursivos.
     - Ejemplo: `cp -r ~/Pictures/PhotosLibrary /Volumes/Untitled/Photos/` (copia recursivamente; ideal para copias de seguridad donde quieres mantener los originales).
   - Para videos en Películas: `cp -r ~/Movies/Videos/ /Volumes/Untitled/Videos/`
   - Para manejar archivos ocultos o permisos: Añade `sudo` si es necesario (por ejemplo, `sudo mv ~/Pictures/photo.jpg /Volumes/Untitled/`).
   - Por seguridad, previsualiza lo que vas a mover: `ls -la ~/Pictures` para listar archivos.

3. **Verificar y desmontar:**
   - Verifica el disco: `ls /Volumes/Untitled` para confirmar las transferencias.
   - Desmonta de forma segura: `diskutil unmount /Volumes/Untitled` y luego desconecta físicamente el disco.

**Consejos avanzados:**
- **Usar Rsync para sincronización:** Para copias de seguridad incrementales (solo archivos nuevos/cambiados), `rsync -av ~/Pictures /Volumes/Untitled/Photos` (instala rsync si no está presente, pero viene integrado en macOS).
- **Automatización:** Adapta esto en tus scripts de Python (por ejemplo, usando `subprocess` para ejecutar comandos `cp` o `mv` basados en la salida de `list_portable_disks.py`).
- **Específico para MacBook:** En tu MacBook Air M2 (Modelo Mac14,2), las transferencias deberían ser rápidas vía USB-C. Monitorea la batería/temperatura (por ejemplo, mediante el Monitor de Actividad) si es necesario.

Si encuentras problemas (por ejemplo, errores de permisos), proporciona más detalles como rutas exactas de archivos o mensajes de error para un consejo más específico. Este proceso debería funcionar de manera confiable en tu configuración.