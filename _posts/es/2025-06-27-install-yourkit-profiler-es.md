---
audio: false
generated: true
lang: es
layout: post
title: Instalación de YourKit Java Profiler en Ubuntu
translated: true
type: note
---

Para instalar YourKit Java Profiler en Ubuntu, siga estos pasos basados en la información disponible del sitio web de YourKit:

1. **Descargar el Profiler**:
   - Visite la página de descarga de YourKit Java Profiler en [https://www.yourkit.com/java/profiler/download/](https://www.yourkit.com/java/profiler/download/).
   - Seleccione la versión para Linux de YourKit Java Profiler 2025.3, que es compatible con Java 8 hasta Java 24 y con Linux (incluyendo Ubuntu) en arquitecturas como arm32, arm64, ppc64le, x64 y x86. Asegúrese de que su sistema cumple con los [requisitos del sistema](https://www.yourkit.com/docs/java/system-requirements/) para garantizar la compatibilidad.

2. **Descargar el Archivo**:
   - Descargue el archivo `.zip` para Linux (por ejemplo, `YourKit-JavaProfiler-2025.3-<build>.zip`). El enlace de descarga está disponible en la página de descarga de YourKit.

3. **Descomprimir el Archivo**:
   - Abra una terminal y navegue al directorio donde se encuentra el archivo descargado (por ejemplo, `~/Downloads`).
   - Descomprima el archivo usando el siguiente comando:
     ```bash
     unzip YourKit-JavaProfiler-2025.3-<build>.zip -d /opt/yourkit
     ```
     Reemplace `<build>` con el número de compilación real del archivo descargado. Este comando extrae el profiler en `/opt/yourkit`. Puede elegir otro directorio si lo prefiere.

4. **Ejecutar el Profiler**:
   - Navegue al directorio extraído:
     ```bash
     cd /opt/yourkit
     ```
   - Ejecute el profiler usando el script proporcionado:
     ```bash
     ./bin/profiler.sh
     ```
     Esto inicia la interfaz de usuario de YourKit Java Profiler.

5. **Opcional: Instalación Automatizada con Clave de Licencia**:
   - Si tiene una clave de licencia y desea automatizar la instalación, puede usar opciones de línea de comandos para aceptar el EULA y aplicar la clave de licencia. Por ejemplo:
     ```bash
     ./bin/profiler.sh -accept-eula -license-key=<key>
     ```
     Reemplace `<key>` con su clave de licencia real. Esto es útil para configuraciones automatizadas o mediante scripts.

6. **Integrar con el Entorno de Desarrollo (Opcional)**:
   - Si utiliza un IDE como Eclipse, IntelliJ IDEA o NetBeans, YourKit proporciona plugins para una integración perfecta. Para Eclipse, por ejemplo:
     - Abra Eclipse y vaya a **Help > Install New Software**.
     - Agregue el repositorio del plugin de YourKit: `https://www.yourkit.com/download/yjp2025_3_for_eclipse/`.
     - Seleccione el plugin YourKit Java Profiler, siga las indicaciones de instalación y reinicie Eclipse si es necesario.
     - Alternativamente, use el archivo offline en `<Directorio de Instalación del Profiler>/lib/eclipse-plugin/yjp2025_3_for_eclipse.zip`.
   - Después de la instalación, la acción "Profile" aparecerá en la barra de herramientas, menú principal o menús contextuales de Eclipse para facilitar el profiling.

7. **Verificar la Instalación**:
   - Una vez que el profiler esté en ejecución, la pantalla de bienvenida le permitirá monitorear aplicaciones Java locales, conectarse a aplicaciones remotas o abrir snapshots existentes. También puede cargar una aplicación de demostración para explorar las características del profiler.

8. **Notas Adicionales**:
   - Si encuentra problemas, asegúrese de que Java (versión 8 o superior) esté instalado en su sistema, ya que YourKit Java Profiler requiere una JVM compatible. Puede verificar su versión de Java con:
     ```bash
     java -version
     ```
   - Para remote profiling, asegúrese de que el acceso SSH esté configurado si va a perfilar aplicaciones en servidores remotos.
   - YourKit ofrece una prueba gratuita de 15 días, por lo que inicialmente no se requiere clave de licencia. Para proyectos de código abierto no comerciales, puede contactar a ventas de YourKit para obtener una licencia gratuita.
   - Si el profiler no se inicia (por ejemplo, debido a espacios en el directorio de instalación), mueva la carpeta extraída a una ruta sin espacios, como `/opt/yourkit`.

Para obtener más ayuda, consulte la [documentación de YourKit](https://www.yourkit.com/docs/java/) o contacte a su soporte a través del [sitio web de YourKit](https://www.yourkit.com/support/).

¡Avíseme si necesita ayuda con algún paso específico!