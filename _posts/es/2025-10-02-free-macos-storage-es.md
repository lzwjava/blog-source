---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Liberar Almacenamiento del Sistema en macOS
translated: true
type: note
---

### Descripción general de la limpieza del espacio de almacenamiento del sistema en macOS

Basándose en la guía oficial de Apple y las recomendaciones de expertos, liberar espacio en macOS (versión 15.6.1 como la suya) implica el uso de herramientas integradas para optimizar el almacenamiento, borrar de forma segura las cachés removibles y eliminar archivos innecesarios. Los Datos del Sistema a menudo incluyen cachés, archivos temporales y registros (logs), gran parte de los cuales se pueden borrar manual o automáticamente sin dañar su Mac. Evite eliminar archivos críticos del sistema, ya que esto podría causar inestabilidad. Su sistema muestra aproximadamente 13 GiB disponibles de un total de 460 GiB, con un 45% usado, así que concéntrese en las cachés, descargas y archivos adjuntos para obtener ganancias rápidas.[1][2][3]

### Uso de las herramientas integradas de gestión de almacenamiento de macOS
Apple proporciona formas integradas de analizar y liberar espacio sin aplicaciones de terceros.
1.  **Verificar el uso de almacenamiento**: Vaya al menú Apple > Configuración del Sistema > General > Almacenamiento. Esto muestra un desglose codificado por colores (por ejemplo, Aplicaciones, Documentos, Datos del Sistema). Haga clic en cualquier categoría para ver recomendaciones.[1]
2.  **Optimizar el almacenamiento automáticamente**: En la configuración de Almacenamiento, active "Optimizar almacenamiento" para descargar datos de aplicaciones no utilizados y gestionar archivos adjuntos. También, active "Vaciar la Papelera automáticamente" después de 30 días.[1]
3.  **Vaciar la Papelera y la carpeta Descargas**: Los Datos del Sistema incluyen el contenido de la Papelera—vacíela manualmente desde el Finder. Revise ~/Downloads en busca de archivos antiguos y elimínelos.[1][2]
4.  **Gestionar archivos adjuntos grandes**: Vaya a Configuración de Almacenamiento > Aplicaciones > Gestionar > Correo > "Optimizar almacenamiento" para descargar archivos adjuntos de correo electrónico grandes bajo demanda.[1]

Para una limpieza más profunda, use la pestaña "Elementos anteriores" en Almacenamiento para revisar copias de seguridad recientes (como las de Time Machine) y eliminarlas si no son necesarias.[2]

### Identificación y eliminación de archivos de caché removibles
Las cachés son archivos temporales que aceleran las aplicaciones pero pueden acumular gigabytes. Borre de forma segura las cachés a nivel de usuario mediante el Finder; evite las cachés a nivel del sistema a menos que lo indique el soporte de Apple para evitar problemas. Las cachés de su Mac están en las carpetas de la biblioteca (library)—verifique los tamaños con "Obtener información" del Finder.

1.  **Directorio de Caché de Usuario (Más seguro de borrar)**:
    - Navegue a Finder > Ir > Ir a la carpeta, escriba `~/Library/Caches` y presione Enter.
    - Esta carpeta contiene las cachés de las aplicaciones (por ejemplo, para navegadores, aplicaciones de Office). Seleccione todas las carpetas internas y elimínelas. En su mayoría son seguras y se regeneran.
    - Consejo: Revise las subcarpetas como `com.apple.*` para las cachés de las aplicaciones de Apple, pero omítalas si no está seguro. Vacíe la Papelera después.[4][2]

2.  **Cachés específicas de aplicaciones**:
    - Navegadores: En Safari, borre el historial/cachés mediante el menú Safari > Borrar historial. Para Chrome/aplicaciones de Google: Vaya a Chrome > Configuración > Privacidad y seguridad > Borrar datos de navegación.
    - Xcode/Desarrollador: Si programa, borre los datos derivados (derived data) en Xcode > Preferencias > Locations > Derived Data.
    - Otras aplicaciones: Revise las preferencias de la aplicación para encontrar opciones de borrado de caché o use el Finder para ver las subcarpetas de `~/Library/Caches`.[2][3]

3.  **Cachés del Sistema y de la Biblioteca (Proceder con Precaución)**:
    - `/Library/Caches` puede contener cachés del sistema—elimine solo carpetas específicas como cachés de aplicaciones obsoletas aquí, no las del sistema central (por ejemplo, evite `com.apple.coreservices`).
    - Para analizar tamaños de forma segura, use Terminal para listar las cachés grandes: Abra Terminal y ejecute `du -sh /Library/Caches/* | sort -h`.
    - Último recurso para cachés profundas del sistema: Reinicie en Modo de Recuperación (Comando+R al arrancar) y ejecute Utilidad de Discos > Primeros Auxilios, luego reinicie normalmente y use las herramientas de Almacenamiento.[2]

### Consejos adicionales para una limpieza manual y segura
-   **Eliminar archivos temporales y de registro (logs)**: Los Datos del Sistema incluyen registros (logs) en `/private/var/log`. Use comandos de Terminal como `sudo rm -rf /private/var/log/asl/*.asl` para registros antiguos de Apple (cierre y vuelva a iniciar sesión primero). Para archivos temporales, elimine de `/tmp` mediante `sudo rm -rf /tmp/*` después de verificarlos.[2]
-   **Descargar a almacenamiento externo**: Mueva fotos/videos a iCloud o a una unidad externa mediante Configuración de Almacenamiento > "Almacenar en iCloud".[1]
-   **Aplicaciones para análisis seguro**: Herramientas de terceros como CleanMyMac (de MacPaw) u OmniDiskSweeper escanean en busca de cachés/archivos grandes—úselas como guía, pero siempre haga una copia de seguridad primero (por ejemplo, mediante Time Machine).[3]
-   **Monitorear después de la limpieza**: Reinicie después de eliminaciones importantes para actualizar. Verifique nuevamente el uso de Almacenamiento; la eliminación de cachés regenerables no debería afectar el rendimiento.[2]

Si los Datos del Sistema permanecen altos (por ejemplo, 218 GB como en algunos informes), podrían ser copias de seguridad ocultas o archivos corruptos—el Soporte de Apple sugiere ejecutar `tmutil thinlocalsnapshots / 10000000000 4` en Terminal para la limpieza de Time Machine.[5] Asegúrese de tener copias de seguridad antes de proceder. Estos métodos deberían recuperar un espacio significativo sin riesgos en Macs con Apple Silicon como su M2.[1][2][4]

Citas:
[1] https://support.apple.com/en-us/102624
[2] https://macpaw.com/how-to/clear-system-storage-mac
[3] https://nektony.com/how-to/clean-up-system-storage-on-mac?srsltid=AfmBOorJjQPPX59Jw3MM47n0NZ8DQlerYQAbkZdymj0rUZM0rtLZlw1s
[4] https://www.reddit.com/r/MacOS/comments/154rp99/how_to_do_i_clear_system_data_on_mac_os/
[5] https://discussions.apple.com/thread/255084458