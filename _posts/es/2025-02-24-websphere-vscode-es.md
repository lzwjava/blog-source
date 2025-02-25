---
audio: false
lang: es
layout: post
title: Usando el servidor WebSphere Liberty en VSCode
translated: true
---

Para usar el servidor WebSphere Liberty en Visual Studio Code (VSCode), puedes aprovechar la extensión **Liberty Tools**, que admite tanto Open Liberty como WebSphere Liberty. Esta extensión te permite gestionar tu servidor Liberty, desplegar aplicaciones y depurar directamente desde VSCode, optimizando tu flujo de trabajo de desarrollo.

### Pasos para usar WebSphere Liberty en VSCode

#### 1. **Instalar la extensión Liberty Tools**
   - Abre VSCode y navega a la vista de Extensiones haciendo clic en el ícono de Extensiones en la barra de Actividad o presionando `Ctrl+Shift+X`.
   - Busca "Liberty Tools" en el Mercado de Extensiones.
   - Haz clic en "Instalar" para agregar la extensión a VSCode.
   - Recarga VSCode si se te solicita para habilitar la extensión.

#### 2. **Configurar los Prerrequisitos**
   - **Java**: Asegúrate de tener una versión compatible de Java instalada (se recomienda Java 8 o posterior). Liberty es un servidor basado en Java, por lo que Java es esencial para ejecutarlo.
   - **WebSphere Liberty**: Descarga e instala el entorno de ejecución de WebSphere Liberty si aún no lo has hecho. Puedes obtenerlo desde el [sitio web oficial de IBM](https://www.ibm.com/docs/en/was-liberty). Tómate nota del directorio de instalación, ya que lo necesitarás para configurar la extensión.

#### 3. **Configurar la extensión Liberty Tools**
   - Después de instalar la extensión, configúrala para que apunte a tu instalación de Liberty.
   - Abre la Paleta de Comandos en VSCode presionando `Ctrl+Shift+P`.
   - Escribe "Liberty: Add Liberty Runtime" y selecciona el comando.
   - Proporciona la ruta a tu directorio de instalación de Liberty (por ejemplo, `/opt/ibm/wlp`).
   - La extensión detectará el entorno de ejecución de Liberty y lo hará disponible para su uso dentro de VSCode.

#### 4. **Gestionar tu servidor Liberty**
   - Una vez configurado, puedes gestionar tu servidor Liberty directamente desde VSCode.
   - **Tablero de Liberty**: Accede a la vista del Tablero de Liberty en el panel Explorador o a través de la Paleta de Comandos. Este tablero enumera tus proyectos y servidores de Liberty.
   - **Iniciar/Detener el servidor**: Haz clic derecho en tu servidor en el tablero para iniciar, detener o reiniciarlo.
   - **Desplegar aplicaciones**: Para proyectos de Liberty (por ejemplo, proyectos Maven o Gradle con plugins de Liberty), haz clic derecho en el proyecto y selecciona "Deploy to Liberty" para desplegar aplicaciones.
   - **Modo de Desarrollo (Dev Mode)**: Para proyectos Maven o Gradle, inicia el servidor en modo dev, que detecta automáticamente los cambios de código, recompila y vuelve a desplegar la aplicación sin reiniciar el servidor. Esto es ideal para el desarrollo iterativo.

#### 5. **Depuración y Pruebas**
   - **Depuración**: Adjunta un depurador a tu servidor Liberty en ejecución directamente desde VSCode. Usa la opción "Debug" en el Tablero de Liberty o configura una configuración de depuración en la vista Ejecutar y Depurar de VSCode.
   - **Ejecutar pruebas**: Si tu proyecto incluye pruebas, ejecútalas desde el tablero y visualiza los resultados dentro de VSCode.

#### 6. **Características adicionales**
   - **Asistencia de configuración**: La extensión proporciona autocompletado de código, validación y descripciones emergentes para archivos de configuración de Liberty (por ejemplo, `server.xml`), simplificando la configuración del servidor.
   - **Soporte de lenguajes**: Admite Java, MicroProfile y APIs de Jakarta EE, mejorando tu experiencia de desarrollo.

### Beneficios clave
- **Integración sin fisuras**: Gestiona tu servidor Liberty sin salir de VSCode, mejorando la eficiencia.
- **Despliegue automático**: En modo dev, los cambios de código se detectan y despliegan automáticamente, ahorrando tiempo durante el desarrollo.
- **Soporte de depuración**: Adjunta fácilmente un depurador a tu servidor para solucionar problemas.
- **Ligero y eficiente**: Liberty Tools está diseñado para ser ligero, alineándose con el enfoque de Liberty en velocidad y eficiencia.

### Recursos adicionales
- Para obtener una guía detallada, consulta la [Documentación de Open Liberty](https://openliberty.io/docs/) y la [Documentación de Liberty Tools VSCode](https://openliberty.io/docs/latest/develop/liberty-tools.html).
- Si encuentras problemas, revisa la sección de solución de problemas de la extensión o busca ayuda en la comunidad en plataformas como Stack Overflow.

Siguiendo estos pasos, puedes usar WebSphere Liberty dentro de VSCode, aprovechando sus características para mejorar tu proceso de desarrollo.