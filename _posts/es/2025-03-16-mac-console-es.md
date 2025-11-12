---
audio: false
generated: true
lang: es
layout: post
title: Aplicación de Consola
translated: true
type: note
---

Para solucionar el error "Failed to open input stream in demuxing stream" en Infuse, una aplicación para Mac, y ver registros más detallados, puedes usar herramientas disponibles en tu Mac. Dado que la consulta menciona "iOS o Xcode tool" pero especifica Infuse como una aplicación para Mac, es probable que desees usar Xcode o herramientas relacionadas con macOS para inspeccionar los registros de la versión para Mac de Infuse. A continuación, se presentan instrucciones paso a paso para ayudarte a acceder a estos registros.

### Para Infuse en Mac (Método Principal: App Console)
Dado que Infuse se identifica como una aplicación para Mac en tu consulta, la forma más directa de ver sus registros es usando la aplicación **Console**, que está integrada en macOS y está diseñada para mostrar registros del sistema y de aplicaciones.

1. **Abrir la aplicación Console**:
   - Inicia la aplicación **Console**, que se encuentra en **Aplicaciones** > **Utilidades** > **Console**, o búscala usando Spotlight (Cmd + Espacio, luego escribe "Console").

2. **Filtrar registros para Infuse**:
   - En la aplicación Console, usa la barra de búsqueda en la parte superior derecha.
   - Escribe "Infuse" o el nombre del proceso de la aplicación (probablemente "Infuse" o similar) para filtrar los registros relacionados con la aplicación.

3. **Reproducir el Error**:
   - Con la aplicación Console abierta y el filtro activo, reproduce el video en Infuse que desencadena el error "Failed to open input stream in demuxing stream".
   - Esto asegura que los registros relevantes se capturen en tiempo real.

4. **Analizar los Registros**:
   - Busca mensajes de error, advertencias o salidas detalladas que puedan explicar por qué falló la apertura del flujo de entrada durante el demuxing (el proceso de separar las pistas de audio y video).
   - Palabras clave como "error", "fail" o "demux" pueden ayudar a identificar el problema.

### Si te referías a la versión iOS de Infuse (Usando Xcode)
Si tu intención era depurar la versión iOS de Infuse (a pesar de que la consulta dice "Mac app"), puedes usar **Xcode**, la herramienta de desarrollo de Apple, para acceder a los registros de un dispositivo iOS. Así es cómo:

1. **Conectar tu dispositivo iOS**:
   - Conecta tu iPhone o iPad a tu Mac usando un cable USB.

2. **Abrir Xcode**:
   - Inicia **Xcode** en tu Mac. Si no lo tienes instalado, descárgalo desde la Mac App Store.

3. **Acceder a Dispositivos y Simuladores**:
   - En Xcode, ve a **Window** > **Devices and Simulators** desde la barra de menús.

4. **Seleccionar tu Dispositivo**:
   - En la ventana que se abre, encuentra tu dispositivo iOS conectado en la barra lateral izquierda y haz clic en él.

5. **Ver Registros**:
   - Haz clic en **Open Console** o **View Device Logs** (la opción puede variar según la versión de Xcode).
   - Esto abre un visor de registros que muestra toda la actividad de tu dispositivo.

6. **Filtrar por Infuse**:
   - Usa la opción de búsqueda o filtro en el visor de registros para reducir las entradas escribiendo "Infuse" o el identificador del bundle de la aplicación (por ejemplo, `com.firecore.Infuse` si se conoce).
   - Reproduce el error en tu dispositivo iOS mientras la consola está abierta para capturar los registros relevantes.

### Opciones Adicionales
- **Buscar Informes de Fallos (Crash Reports)**:
  - **Mac**: Si Infuse falla, revisa `~/Library/Logs/DiagnosticReports` o `/Library/Logs/DiagnosticReports` en busca de informes de fallos con nombres que incluyan "Infuse" y una marca de tiempo.
  - **iOS**: En la ventana **Devices and Simulators** de Xcode, los informes de fallos para Infuse pueden aparecer en los registros de tu dispositivo.

- **Habilitar el Registro de Depuración (Debug Logging) en Infuse**:
  - Algunas aplicaciones, incluida Infuse, pueden ofrecer un modo de depuración o una opción de registro detallado. Abre la configuración o preferencias de Infuse en tu Mac (o dispositivo iOS) para ver si existe tal función. Si se habilita, esto podría generar registros más detallados que se pueden ver mediante los métodos anteriores.

- **Alternativa para iOS (App Console)**:
  - Conecta tu dispositivo iOS a tu Mac, abre la aplicación **Console** y selecciona tu dispositivo de la barra lateral izquierda. Filtra los registros por "Infuse" para ver la salida en tiempo real sin necesidad de Xcode.

### Notas
- El error "Failed to open input stream in demuxing stream" sugiere un problema con el archivo de medios o el stream de red que Infuse está intentando procesar. Los registros podrían revelar si se trata de una corrupción de archivo, una incompatibilidad de códec o un problema de conexión.
- Dado que Infuse es una aplicación de terceros, la depuración avanzada (por ejemplo, adjuntar Xcode al proceso) es poco probable sin acceso de desarrollador, por lo que la aplicación Console (para Mac) o los registros del dispositivo (para iOS) son tus mejores opciones.

Siguiendo estos pasos, podrás recopilar más registros para diagnosticar el error en Infuse, ya sea en Mac o iOS. Si el problema persiste, considera consultar la documentación de soporte o los foros de Infuse para obtener consejos específicos sobre el registro de la aplicación.