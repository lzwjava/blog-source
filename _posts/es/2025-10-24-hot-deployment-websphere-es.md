---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Implementación en Caliente en WebSphere WAS
translated: true
type: note
---

### Comprensión de Hot Deployment y Hotswap en WebSphere Application Server (WAS)

Hot deployment (también conocido como hot reloading o hot swapping) es una técnica de desarrollo que permite actualizar e implementar cambios en tu aplicación—como código, configuración o recursos—sin requerir un reinicio completo del servidor de aplicaciones. Esto es particularmente valioso durante ciclos de desarrollo iterativos, donde los cambios frecuentes de código (por ejemplo, corregir errores, ajustar lógica o actualizar elementos de la UI) se verían ralentizados por los largos tiempos de inicio del servidor, especialmente en entornos empresariales como IBM WebSphere Application Server (WAS). Reiniciar una instancia de WAS puede tomar minutos o incluso más para aplicaciones grandes, interrumpiendo los flujos de trabajo y las pruebas.

El fragmento que proporcionaste se centra en estrategias prácticas para lograr iteraciones más rápidas en WAS, enfatizando los despliegues WAR "explotados" y herramientas para un hot swapping mejorado. Lo desglosaré paso a paso, explicando los conceptos, cómo funcionan, sus limitaciones y consejos de implementación.

#### 1. Desplegar como un WAR "Explotado" (Despliegue Desempaquetado)
Un archivo WAR (Web Application Archive) es esencialmente un paquete comprimido que contiene los recursos de tu aplicación web: JSPs, servlets, clases Java, archivos estáticos (HTML/CSS/JS), librerías (JARs) y archivos de configuración (por ejemplo, web.xml). Por defecto, los WARs se despliegan como archivos **empaquetados** (comprimidos), que WAS trata como inmutables—cualquier cambio requiere reempaquetar y redesplegar todo el archivo.

Un **WAR explotado** se refiere a descomprimir (deszippear) el archivo WAR en una estructura de directorios antes del despliegue. Esto permite modificar archivos o subdirectorios individuales directamente en el sistema de archivos del servidor sin tocar todo el archivo.

**Por qué permite iteraciones más rápidas:**
- **Actualizaciones a nivel de archivo:** Puedes editar un único archivo JSP o clase Java, y WAS puede detectar y recargar solo ese componente.
- **Sin reempaquetar:** Evita la sobrecarga de comprimir/descomprimir WARs grandes repetidamente.
- **Sinergia con hot reloading:** Facilita que el servidor monitoree y actualice los archivos modificados.

**Cómo desplegar un WAR explotado en WAS:**
- **Usando la Consola de Administración:**
  1. Inicia sesión en la Consola de Soluciones Integradas de WAS (típicamente en `http://localhost:9060/ibm/console`).
  2. Navega a **Applications > New Application > New Enterprise Application**.
  3. En lugar de seleccionar un archivo WAR empaquetado, apunta al directorio raíz de tu WAR descomprimido (por ejemplo, `/ruta/a/miapp.war/`—nota la barra diagonal final para indicar que es un directorio).
  4. Completa el asistente de despliegue, asegurándote de que "Deploy Web services" y otras opciones coincidan con tu aplicación.
- **Usando wsadmin (herramienta de scripting):**
  ```bash
  wsadmin.sh -c "AdminApp.install('/ruta/a/miapp', '[ -MapWebModToVH [[miapp .* default_host.* virtual_host ]]]')"
  ```
  Reemplaza `/ruta/a/miapp` con tu directorio explotado.
- **Servidores de desarrollo (por ejemplo, Liberty Profile):** Para pruebas más ligeras, usa Open Liberty (una variante de WAS) con `server start` y coloca tu aplicación explotada en la carpeta `dropins` para un despliegue automático.

**Mejores prácticas:**
- Usa una herramienta de control de código fuente (por ejemplo, Git) para sincronizar cambios desde tu IDE al directorio explotado.
- Monitorea el espacio en disco, ya que los despliegues explotados consumen más almacenamiento.
- En producción, usa WARs empaquetados por seguridad y consistencia—el hot deployment es principalmente para desarrollo/pruebas.

Una vez desplegado de forma explotada, los mecanismos incorporados de WAS pueden activarse para la recarga parcial en caliente.

#### 2. Soporte Nativo de Hot-Reload en WAS
WAS proporciona soporte nativo para la recarga en caliente de ciertos componentes sin un reinicio completo, pero es limitado. Esto depende del mecanismo de **sondeo de archivos** del servidor, donde WAS escanea periódicamente el directorio de despliegue explotado en busca de cambios (configurable mediante argumentos JVM como `-DwasStatusCheckInterval=5` para comprobaciones cada 5 segundos).

**Qué soporta WAS fuera de la caja:**
- **JSPs (JavaServer Pages):**
  - Los JSPs se compilan dinámicamente en servlets en el primer acceso. Si modificas un archivo JSP en un WAR explotado, WAS puede detectar el cambio, recompilarlo y recargar el servlet.
  - **Cómo funciona:** Establece `reloadInterval` en `ibm-web-ext.xmi` (bajo WEB-INF) a un valor bajo (por ejemplo, 1 segundo) para comprobaciones frecuentes. O usa la configuración global en **Servers > Server Types > WebSphere application servers > [tu_servidor] > Java and Process Management > Process definition > Java Virtual Machine > Custom properties** con `com.ibm.ws.webcontainer.invokefilterscompatibility=true`.
  - **Limitaciones:** Solo funciona para JSPs que no han sido almacenados en caché agresivamente. Los JSPs complejos con includes o etiquetas pueden requerir un reinicio de módulo.
- **Algunas clases Java (servlets y EJBs):**
  - Para despliegues explotados, WAS puede recargar archivos de clase individuales si están en los directorios WEB-INF/classes o lib.
  - **Cómo funciona:** Habilita "Application reload" en el descriptor de despliegue o vía consola: **Applications > [tu_app] > Manage Modules > [módulo] > Reload behavior > Reload enabled**.
  - Esto activa una **recarga a nivel de módulo**, que es más rápida que un reinicio completo de la aplicación pero aún así descarga/recarga todo el módulo (por ejemplo, tu aplicación web).

**Limitaciones del soporte incorporado:**
- **No es un hotswap verdadero:** Los cambios en la lógica central de la aplicación (por ejemplo, modificar un método en una clase servlet en ejecución) no surtirán efecto sin descargar el classloader antiguo. Podrías ver `ClassNotFoundException` o código obsoleto.
- **Pérdida de estado:** Las sesiones, singletons o conexiones de base de datos pueden reiniciarse.
- **Específicos del JDK de IBM:** WAS a menudo usa el JDK de IBM, que tiene peculiaridades con la recarga de clases en comparación con OpenJDK/HotSpot.
- **Sin soporte para cambios estructurales:** Agregar nuevas clases, cambiar firmas de métodos o actualizar anotaciones requiere un reinicio.
- **Sobrecarga de rendimiento:** El sondeo frecuente puede tensionar los recursos en desarrollo.

Para ajustes básicos de UI (ediciones de JSP) o actualizaciones simples de clases, esto es suficiente y gratuito. Pero para un "hotswap completo"—donde puedes editar código en ejecución a mitad de camino sin ninguna recarga—necesitas herramientas de terceros.

#### 3. Soluciones de Hotswap Completo
Para lograr cambios de código perfectos (por ejemplo, editar el cuerpo de un método en un IDE con el depurador adjunto como Eclipse o IntelliJ, y ver que se aplica al instante), usa plugins que parcheen la carga de clases y la instrumentación de la JVM.

**Opción 1: JRebel (Plugin de Pago)**
- **Qué es:** Una herramienta comercial de Perforce (anteriormente ZeroTurnaround) que proporciona hotswap completo para aplicaciones Java. Instrumenta tu bytecode al inicio, permitiendo la recarga de clases, recursos e incluso cambios específicos del framework (por ejemplo, beans de Spring, entidades de Hibernate).
- **Por qué usarlo con WAS:**
  - Integración profunda con WAS, incluyendo soporte para WARs explotados, bundles OSGi y el JDK de IBM.
  - Maneja escenarios complejos como cambiar firmas de métodos o agregar campos (más allá de los límites estándar de hotswap JVMTI).
  - **Características:** Detección automática de cambios desde tu IDE; sin redespliegues manuales; preserva el estado de la aplicación.
- **Cómo configurarlo:**
  1. Descarga JRebel del sitio oficial e instálalo como un plugin de Eclipse/IntelliJ.
  2. Genera un archivo de configuración `rebel.xml` para tu proyecto (generado automáticamente o manual).
  3. Agrega argumentos JVM a tu servidor WAS: `-javaagent:/ruta/a/jrebel.jar` (ruta completa al JAR del agente).
  4. Inicia WAS en modo depuración (`-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000`).
  5. Conecta el depurador de tu IDE y edita el código—JRebel sincroniza los cambios en vivo.
- **Costo:** Basado en suscripción (~$400/usuario/año para individuos; licencias empresariales varían). Prueba gratuita disponible.
- **Pros:** Confiable, fácil de usar, excelente soporte para WAS.
- **Contras:** De pago; requiere configuración por proyecto.

**Opción 2: DCEVM + HotSwapAgent (Alternativa Gratuita)**
- **Qué es:** Un combo de código abierto para hotswapping avanzado.
  - **DCEVM (Dynamic Code Evolution VM):** Una JVM modificada que extiende JVMTI (Java Virtual Machine Tool Interface) de HotSpot para permitir redefiniciones de clase más agresivas (por ejemplo, agregar/eliminar métodos, cambiar jerarquías).
  - **HotSwapAgent:** Un agente que se basa en DCEVM, proporcionando integración con el IDE para la recarga automática de clases.
- **Por qué usarlo con WAS:**
  - Gratuito y potente para desarrollo, imitando las capacidades de JRebel.
  - Soporta cambios en el cuerpo de métodos, actualizaciones de recursos e incluso algunas recargas de frameworks (vía plugins).
- **Nota de compatibilidad con el JDK de IBM de WAS:**
  - WAS normalmente incluye el JDK J9 de IBM, que **no soporta DCEVM** de forma nativa (DCEVM es específico de HotSpot).
  - **Solución alternativa:** Cambia a OpenJDK/HotSpot para desarrollo (por ejemplo, vía anulación de `JAVA_HOME` en `setInitial.sh` o `jvm.options` de Liberty). Prueba exhaustivamente—la recolección de basura y las características de seguridad del JDK de IBM podrían diferir.
  - En producción, vuelve al JDK de IBM; esto es solo para desarrollo.
- **Cómo configurarlo:**
  1. **Instalar DCEVM:**
     - Descarga el JAR parcheador de DCEVM desde GitHub (por ejemplo, `dcevm-11.0.0+7-full.jar` para JDK 11+).
     - Ejecuta: `java -jar dcevm.jar /ruta/a/tu/jdk/jre/lib/server/jvm.dll server` (Windows) o equivalente para Linux (`libjvm.so`).
     - ¡Esto parchea el binario JVM de tu JDK—haz una copia de seguridad primero!
  2. **Instalar HotSwapAgent:**
     - Descarga `hotswap-agent.jar` desde GitHub.
     - Agrega a los argumentos JVM de WAS: `-XXaltjvm=dcevm -XX:+TraceClassLoading -javaagent:/ruta/a/hotswap-agent.jar=DCEVM` (más cualquier plugin, por ejemplo, `=hotswap-spring` para Spring).
  3. **Integración con el IDE:**
     - Instala el plugin HotSwapAgent para IntelliJ/Eclipse.
     - Inicia WAS con los argumentos de depuración como se indicó anteriormente.
     - Edita y guarda el código en el IDE—el agente recarga automáticamente.
  4. **Probar compatibilidad:**
     - Ejecuta una prueba de humo: Despliega un servlet simple, edita un método (por ejemplo, agrega una línea de log), accede al endpoint y verifica el cambio sin reiniciar.
     - Revisa los logs en busca de errores como `HotSwap failed: method limit reached` (DCEVM tiene límites en los cambios por clase).
- **Pros:** Gratuito, personalizable (vía plugins para Spring, CDI, etc.), soportado por la comunidad.
- **Contras:** La configuración es complicada; posible inestabilidad con JVMs no estándar; limitado a HotSpot (probar el cambio de JDK de IBM con cuidado); no tan pulido como JRebel.

#### Cuándo Usar Qué
- **WAR explotado + Recarga incorporada:** Para ajustes rápidos de JSP/archivos estáticos en desarrollo temprano.
- **JRebel:** Si el presupuesto lo permite y necesitas confiabilidad de nivel empresarial.
- **DCEVM + HotSwapAgent:** Para hotswap completo sin costo, pero asigna tiempo para pruebas de compatibilidad de JVM.

En resumen, estas técnicas transforman WAS de un servidor pesado en un entorno de desarrollo más ágil, reduciendo los tiempos de iteración de minutos a segundos. Comienza con WARs explotados para ganancias inmediatas, luego agrega herramientas según sea necesario. Si encuentras errores específicos, comparte más detalles para la resolución de problemas.

**Referencias:**  
[Documentación de JRebel para WebSphere](https://www.jrebel.com/products/jrebel/tutorials/deploy-jrebel-websphere)  
[Repositorio GitHub de DCEVM](https://github.com/dcevm/dcevm)  
[Repositorio GitHub de HotSwapAgent](https://github.com/HotswapProjects/HotswapAgent)  
[Centro de Conocimiento de IBM: Hot Deployment en WebSphere](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-hot-deployment)