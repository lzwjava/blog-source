---
audio: false
generated: true
lang: es
layout: post
title: Corrección de Errores de Permisos de Archivos en macOS
translated: true
type: note
---

### Comprender el Error
Este mensaje de error suele aparecer en macOS cuando intentas mover, copiar, eliminar o manipular archivos/carpetas (por ejemplo, vaciar la Papelera o arrastrar elementos), pero el sistema encuentra problemas de permisos, archivos bloqueados o restricciones de solo lectura. El mensaje en sí proporciona la solución principal, pero a veces se necesitan pasos adicionales si el problema persiste, como usar comandos de Terminal, reparar permisos del disco o manejar archivos problemáticos.

### Soluciones Paso a Paso
Sigue estos pasos en orden, comenzando por el más simple. Estos asumen que estás en macOS (por ejemplo, Ventura, Sonoma o posterior). Asegúrate de haber iniciado sesión como usuario administrador.

1.  **Desbloquear Archivos y Ajustar Permisos (Como Sugiere el Error)**:
    *   Selecciona el archivo o carpeta problemático en el Finder.
    *   Haz clic derecho (o Control + clic) y elige **Obtener información** (o presiona Comando + I).
    *   En la ventana de información:
        *   En la sección **General**, desmarca la casilla **Bloqueado** si está seleccionada.
        *   Desplázate a la sección **Compartir y Permisos** en la parte inferior.
        *   Haz clic en el icono del candado en la esquina inferior derecha e ingresa tu contraseña de administrador para desbloquear los cambios.
        *   Para tu nombre de usuario (o "todos" si es necesario), establece el Privilegio en **Lectura y escritura**.
    *   Si hay múltiples elementos afectados, puedes seleccionarlos todos, obtener información y aplicar los cambios (mantén presionada la tecla Comando para seleccionar múltiples).
    *   Cierra la ventana y vuelve a intentar la operación (por ejemplo, eliminar o mover los archivos).

2.  **Si el Problema es con la Papelera (Escenario Común)**:
    *   Este error aparece a menudo al vaciar la Papelera si los archivos están bloqueados o tienen problemas de permisos.
    *   Primero, abre la Papelera, selecciona los elementos y aplica los pasos de "Obtener información" anteriores para desbloquear/ajustar los permisos.
    *   Si eso no funciona, fuerza el vaciado de la Papelera:
        *   Mantén presionada la tecla Opción mientras haces clic derecho en el icono de la Papelera en el Dock y selecciona **Vaciar Papelera**.
    *   Alternativa mediante Terminal (si falla la interfaz gráfica):
        *   Abre Terminal (desde Aplicaciones > Utilidades o la búsqueda de Spotlight).
        *   Escribe: `sudo rm -rf ~/.Trash/*` y presiona Enter.
        *   Ingresa tu contraseña de administrador (no se mostrará mientras escribes).
        *   Advertencia: Esto elimina permanentemente todo en la Papelera; úsalo con precaución, ya que no hay deshacer.

3.  **Reparar Permisos del Disco Usando Utilidad de Discos**:
    *   Abre **Utilidad de Discos** (desde Aplicaciones > Utilidades o Spotlight).
    *   Selecciona tu unidad principal (por ejemplo, Macintosh HD) en la barra lateral.
    *   Haz clic en **Primeros Auxilios** > **Ejecutar** (o **Reparar Permisos del Disco** en versiones anteriores de macOS).
    *   Deja que complete el proceso, luego reinicia tu Mac e inténtalo de nuevo.

4.  **Verificar Unidades Externas o Volúmenes de Red**:
    *   Si los archivos están en una unidad externa, USB o recurso compartido de red:
        *   Expulsa y vuelve a conectar la unidad.
        *   En Obtener información, asegúrate de que la casilla **Ignorar la propiedad en este volumen** esté marcada (en Compartir y Permisos).
    *   Para formatos de solo lectura (por ejemplo, unidades NTFS), es posible que necesites herramientas de terceros como Paragon NTFS para obtener acceso de escritura.

5.  **Soluciones Avanzadas con Terminal (Si los Permisos Son Persistentes)**:
    *   Para restablecer permisos en una carpeta/archivo específico:
        *   En Terminal: `sudo chmod -R 777 /ruta/a/la/carpeta` (reemplaza `/ruta/a/la/carpeta` con la ruta real; arrastra la carpeta a Terminal para que se complete automáticamente).
        *   Esto establece permisos completos de lectura, escritura y ejecución para todos; úsalo con moderación.
    *   Para desbloquear todos los archivos en un directorio: `sudo chflags -R nouchg /ruta/a/la/carpeta`.
    *   Reinicia en Modo Seguro (mantén presionada la tecla Shift durante el arranque) para borrar las cachés, luego inténtalo de nuevo.

6.  **Otra Solución de Problemas**:
    *   **Reinicia tu Mac**: Simple, pero a menudo resuelve fallos temporales.
    *   **Actualiza macOS**: Ve a Configuración del Sistema > General > Actualización de software.
    *   **Verifica Interferencia de Malware/Antivirus**: Ejecuta un análisis con Malwarebytes o similar.
    *   Si los archivos son de descargas o aplicaciones, asegúrate de que no estén en cuarentena: En Terminal, `xattr -d com.apple.quarantine /ruta/al/archivo`.
    *   Si nada funciona, inicia en Modo de Recuperación (Comando + R al arrancar), ejecuta Primeros Auxilios en el disco, o considera restablecer los permisos mediante Terminal en el Modo de Recuperación.

Si el error persiste después de estos pasos, proporciona más detalles como tu versión de macOS, qué operación estás intentando (por ejemplo, eliminar archivos específicos) y si es en la Papelera o en otro lugar.

### Referencias
[Soporte de Apple: Cambiar los permisos de archivos, carpetas o discos en la Mac](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)  
[Cómo Solucionar el Error "No se puede completar la operación" en Mac](https://www.macrumors.com/how-to/fix-operation-cant-be-completed-error-mac/)  
[Vaciar la Papelera Cuando Dice Que Los Archivos Están En Uso](https://apple.stackexchange.com/questions/52257/empty-trash-when-it-says-files-are-in-use)