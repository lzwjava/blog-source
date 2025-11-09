---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Desarrollo WebSphere con Eclipse
translated: true
type: note
---

### Desarrollo con IBM WebSphere Application Server (WAS) en Eclipse

IBM WebSphere Application Server (WAS) es un servidor de aplicaciones Java EE, y Eclipse sirve como un excelente IDE para desarrollar, ensamblar y desplegar aplicaciones en él. La herramienta principal para esta integración son las **IBM WebSphere Application Server Developer Tools for Eclipse** (a menudo abreviadas como WDT). Este plugin proporciona capacidades de gestión de servidores, creación de proyectos, despliegue y depuración directamente dentro de Eclipse. Es compatible tanto con WAS tradicional (por ejemplo, v8.5 y v9.x) como con el perfil ligero Liberty.

#### Plugin Requerido
- **IBM WebSphere Application Server Developer Tools for Eclipse**: Este es el plugin esencial. Elija la versión que coincida con su runtime de WAS (por ejemplo, herramientas V8.5x o V9.x). Está disponible de forma gratuita en el Eclipse Marketplace y es compatible con versiones recientes de Eclipse como 2024-06 o 2025-03.

No se requieren estrictamente otros plugins, pero para un desarrollo completo de Java EE, asegúrese de que su instalación de Eclipse incluya la Web Tools Platform (WTP), que es estándar en el paquete Eclipse IDE for Java EE Developers.

#### Prerrequisitos
- Eclipse IDE for Java EE Developers (se recomienda la versión 2023-09 o posterior para compatibilidad).
- Runtime de IBM WAS instalado localmente (tradicional o Liberty) para pruebas y despliegue.
- Acceso a Internet para la instalación desde el Marketplace (o descargar los archivos sin conexión).

#### Pasos de Instalación
Puede instalar WDT a través del Eclipse Marketplace (método más fácil), el sitio de actualización o archivos descargados. Reinicie Eclipse después de la instalación.

1. **A través del Eclipse Marketplace** (Recomendado):
   - Abra Eclipse y vaya a **Help > Eclipse Marketplace**.
   - Busque "IBM WebSphere Application Server Developer Tools".
   - Seleccione la versión apropiada (por ejemplo, para V9.x o V8.5x).
   - Haga clic en **Install** y siga las instrucciones. Acepte las licencias y reinicie Eclipse cuando termine.

2. **A través del Sitio de Actualización**:
   - Vaya a **Help > Install New Software**.
   - Haga clic en **Add** e ingrese la URL del sitio de actualización (por ejemplo, `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` para versiones recientes—consulte la documentación de IBM para la más actual).
   - Seleccione las características de WDT (por ejemplo, WebSphere Application Server V9.x Developer Tools) e instálelas.

3. **Desde Archivos Descargados** (Opción Sin Conexión):
   - Descargue el archivo ZIP desde el [sitio para desarrolladores de IBM](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) (por ejemplo, `wdt-update-site_<version>.zip`).
   - Extráigalo en una carpeta local.
   - En Eclipse, vaya a **Help > Install New Software > Add > Archive** y seleccione el `site.xml` del sitio extraído.
   - Seleccione e instale las características deseadas, luego reinicie.

Después de la instalación, verifique yendo a **Window > Show View > Servers**—WAS debería aparecer como una opción de tipo de servidor.

#### Pasos Básicos para Desarrollar y Desplegar Aplicaciones WAS
Una vez instalado, puede crear, construir y ejecutar aplicaciones Java EE destinadas a WAS.

1. **Crear un Nuevo Proyecto**:
   - Vaya a **File > New > Project**.
   - Seleccione **Web > Dynamic Web Project** (para aplicaciones web) o **Java EE > Enterprise Application Project** (para EARs completos).
   - En el asistente de proyectos, establezca el runtime de destino en su instalación local de WAS (si no está en la lista, agréguelo mediante **Window > Preferences > Server > Runtime Environments > Add > WebSphere**).
   - Configure las facetas para la versión de Java EE (por ejemplo, 7 u 8) que coincida con su WAS.

2. **Configurar el Servidor**:
   - Abra la vista **Servers** (**Window > Show View > Servers**).
   - Haga clic derecho en la vista y seleccione **New > Server**.
   - Elija **WebSphere Application Server** (tradicional o Liberty) y apunte al directorio de su instalación local de WAS.
   - Finalice e inicie el servidor (clic derecho > Start).

3. **Desarrolle Su Aplicación**:
   - Agregue clases Java, JSPs, servlets, EJBs, etc., en su proyecto.
   - Utilice los editores de Eclipse para configuraciones XML (por ejemplo, web.xml, ibm-web-bnd.xml para enlaces específicos de WAS).
   - Construya el proyecto (**Project > Build Project**).

4. **Desplegar y Ejecutar**:
   - Haga clic derecho en su proyecto > **Run As > Run on Server** (seleccione su servidor WAS).
   - Eclipse publica la aplicación (auto-publicación para modo de desarrollo) e inicia el servidor.
   - Depure estableciendo puntos de interrupción y ejecutando en modo Debug.
   - Para despliegue en caliente (actualizaciones rápidas sin reiniciar), habilite "Publish server changes immediately" en la configuración del servidor.

5. **Consejos Avanzados**:
   - Utilice el perfil Liberty para pruebas locales más rápidas—está incluido en WDT y simula el comportamiento de WAS tradicional.
   - Para OSGi o microservicios, cree OSGi Bundle Projects a través del plugin.
   - Monitoree los registros en la vista **Console** durante el tiempo de ejecución.

Si encuentra problemas (por ejemplo, errores de compatibilidad), consulte la página de problemas conocidos de IBM o asegúrese de que sus versiones de Eclipse y WAS estén alineadas.

#### Referencias
- [IBM WebSphere Application Server Developer Tools Overview](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace: V9.x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace: V8.5x Tools](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [Installation Guide from IBM Docs](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)