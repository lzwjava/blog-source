---
audio: false
generated: false
lang: es
layout: post
title: Usando WebSphere Liberty con Eclipse
translated: true
---

Para usar las herramientas del complemento de WebSphere en Eclipse e integrarlas para trabajar con WebSphere Liberty, puedes elegir entre dos opciones principales: **IBM Liberty Developer Tools** y **Liberty Tools**. Ambos están disponibles a través del Eclipse Marketplace y proporcionan características para construir, desplegar y gestionar aplicaciones en WebSphere Liberty, un servidor ligero, listo para producción para aplicaciones Java EE y nativas de la nube. A continuación se presenta una guía detallada sobre cómo usar e integrar estas herramientas.

---

### **Descripción General de las Herramientas**
- **IBM Liberty Developer Tools**: Un complemento tradicional proporcionado por IBM para gestionar servidores Liberty dentro de Eclipse. Permite crear y gestionar servidores Liberty, desplegar aplicaciones y depurar directamente desde el IDE. Esta herramienta es ideal para un flujo de trabajo centrado en el servidor o para proyectos que no utilizan Maven o Gradle.
- **Liberty Tools**: Una alternativa de próxima generación, de código abierto, enfocada en proyectos de Maven y Gradle. Ofrece una experiencia más integrada con las herramientas de construcción, detección automática de proyectos Liberty y soporte para el modo de desarrollo de Liberty (modo dev). Esta herramienta es más adecuada para flujos de trabajo modernos y centrados en herramientas de construcción.

Ambas herramientas agilizan el desarrollo para WebSphere Liberty, pero difieren en su enfoque. Elige la que mejor se adapte a tu tipo de proyecto y preferencias de desarrollo.

---

### **Instalación**
1. **Instalar Eclipse**:
   - Usa una versión compatible, como **Eclipse for Enterprise Java and Web Developers**.
   - Asegúrate de que tu versión de Eclipse soporte el complemento que elijas (verifica la compatibilidad en la lista del marketplace).

2. **Instalar el Complemento**:
   - Abre Eclipse y ve a **Help > Eclipse Marketplace**.
   - Busca:
     - "IBM Liberty Developer Tools" para el conjunto de herramientas tradicional de IBM, o
     - "Liberty Tools" para la alternativa de código abierto.
   - Instala el complemento deseado siguiendo las indicaciones.

---

### **Configuración del Entorno de Ejecución de Liberty**
- **Descargar Liberty**:
  - Si aún no lo has hecho, descarga el entorno de ejecución de WebSphere Liberty desde el [sitio web oficial de IBM](https://www.ibm.com/docs/en/was-liberty).
  - Asegúrate de que la versión de Liberty sea compatible con el complemento que instalaste.

- **Configurar el Entorno de Ejecución en Eclipse**:
  - Para **IBM Liberty Developer Tools**:
    - Ve a **Window > Preferences > Server > Runtime Environments**.
    - Haz clic en "Add," selecciona "Liberty Server" y especifica la ruta a tu directorio de instalación de Liberty.
  - Para **Liberty Tools**:
    - No se necesita una configuración explícita del entorno de ejecución. Liberty Tools detectan proyectos Liberty a través de las configuraciones de Maven o Gradle, así que asegúrate de que tu proyecto esté configurado correctamente (ver más abajo).

---

### **Integración con tu Proyecto**
El proceso de integración difiere ligeramente entre las dos herramientas. Sigue los pasos a continuación según el complemento que instalaste.

#### **Para IBM Liberty Developer Tools**
1. **Crear un Servidor Liberty**:
   - Abre la vista **Servers** (**Window > Show View > Servers**).
   - Haz clic derecho en la vista Servers y selecciona **New > Server**.
   - Elige "Liberty Server" de la lista y sigue el asistente para configurar el servidor, incluyendo especificar la ruta a tu instalación de Liberty.

2. **Agregar tu Proyecto**:
   - Haz clic derecho en el servidor en la vista Servers y selecciona **Add and Remove...**.
   - Selecciona tu proyecto y muévelo al lado "Configured".

3. **Iniciar el Servidor**:
   - Haz clic derecho en el servidor y elige **Start** o **Debug** para ejecutar tu aplicación.
   - Accede a tu aplicación en la URL especificada (predeterminada: `http://localhost:9080/<context-root>`).

#### **Para Liberty Tools (Proyectos Maven/Gradle)**
1. **Asegurar la Configuración del Proyecto**:
   - Tu proyecto debe incluir el complemento de Liberty necesario:
     - Para Maven: Agrega el `liberty-maven-plugin` a tu `pom.xml`.
     - Para Gradle: Agrega el `liberty-gradle-plugin` a tu `build.gradle`.
   - El archivo de configuración `server.xml` debe estar en la ubicación estándar:
     - Para Maven: `src/main/liberty/config`.
     - Para Gradle: Ajusta según la estructura de tu proyecto.

2. **Usar el Panel de Liberty**:
   - Haz clic en el icono de Liberty en la barra de herramientas de Eclipse para abrir el **Liberty Dashboard**.
   - Liberty Tools detectan automáticamente y listan tus proyectos Liberty en el panel.
   - Haz clic derecho en tu proyecto en el panel para acceder a comandos como:
     - "Start in dev mode" (redeploy automáticamente cambios sin reiniciar el servidor).
     - "Run tests."
     - "View test reports."

3. **Acceder a tu Aplicación**:
   - Una vez que el servidor esté en funcionamiento, accede a tu aplicación en la URL especificada (predeterminada: `http://localhost:9080/<context-root>`).
   - En modo dev, realiza cambios en tu código y Liberty los redeployará automáticamente.

---

### **Características Clave**
Ambas herramientas ofrecen características potentes para mejorar la productividad:

- **Gestión del Servidor**:
  - Inicia, detén y depura servidores Liberty directamente desde Eclipse.
- **Despliegue de Aplicaciones**:
  - Despliega y redeploy aplicaciones fácilmente.
- **Asistencia de Configuración**:
  - Ambas herramientas proporcionan autocompletado de código, validación y descripciones emergentes para archivos de configuración de Liberty (por ejemplo, `server.xml`).
- **Modo de Desarrollo**:
  - Detecta y redeploy automáticamente cambios de código sin reiniciar el servidor (especialmente con Liberty Tools en modo dev).
- **Depuración**:
  - Adjunta el depurador de Eclipse al servidor Liberty para solucionar problemas.

---

### **Consideraciones y Posibles Problemas**
- **Compatibilidad de Versiones**:
  - Asegúrate de que tus versiones de Eclipse, el complemento y el entorno de ejecución de Liberty sean compatibles. Consulta la documentación para requisitos específicos.
- **Configuración del Proyecto**:
  - Para Liberty Tools, tu proyecto debe ser un proyecto Maven o Gradle correctamente configurado con el complemento de Liberty incluido.
  - Asegúrate de que `server.xml` esté en la ubicación esperada para que las herramientas reconozcan tu proyecto.
- **Configuración de Red**:
  - Asegúrate de que los puertos predeterminados de Liberty (por ejemplo, 9080 para HTTP, 9443 para HTTPS) estén abiertos y no bloqueados por firewalls.
- **Compatibilidad de Java**:
  - Liberty es un servidor basado en Java, así que asegúrate de tener una versión de Java compatible instalada para tu entorno de ejecución de Liberty.

---

### **Inicio Rápido con Liberty Tools (Maven/Gradle)**
Si estás utilizando Maven o Gradle, Liberty Tools ofrece una experiencia más fluida. Aquí tienes una guía paso a paso:

1. Instala **Eclipse for Enterprise Java and Web Developers**.
2. Ve a **Help > Eclipse Marketplace**, busca "Liberty Tools" e instala el complemento.
3. Crea o importa un proyecto Maven/Gradle configurado para Liberty:
   - Puedes usar el [Open Liberty Starter](https://openliberty.io/start/) para generar un proyecto de muestra.
4. Asegúrate de que tu proyecto tenga el `liberty-maven-plugin` (para Maven) o `liberty-gradle-plugin` (para Gradle) configurado.
5. Abre el **Liberty Dashboard** haciendo clic en el icono de Liberty en la barra de herramientas.
6. Tu proyecto debería aparecer en el panel. Haz clic derecho en él y selecciona "Start in dev mode."
7. Accede a tu aplicación en la URL especificada (predeterminada: `http://localhost:9080/<context-root>`).
8. Realiza cambios en tu código; el modo dev de Liberty los redeployará automáticamente.
9. Usa el panel para ejecutar pruebas o ver informes de pruebas según sea necesario.

---

### **Elegir entre las Herramientas**
- **IBM Liberty Developer Tools**:
  - Ideal para un enfoque de gestión de servidores tradicional o para proyectos que no utilizan Maven o Gradle.
  - Ofrece una vista Servers para gestionar servidores Liberty explícitamente.
- **Liberty Tools**:
  - Más adecuado para proyectos Maven o Gradle, con una integración más estrecha con estos sistemas de construcción.
  - Proporciona un panel Liberty para la gestión centrada en el proyecto y soporte para el modo dev.
  - De código abierto, permitiendo contribuciones y actualizaciones de la comunidad.

Ambas herramientas están disponibles desde el Eclipse Marketplace, así que puedes probar ambas y elegir la que mejor se adapte a tu flujo de trabajo.

---

En resumen, usar las herramientas del complemento de WebSphere en Eclipse implica instalar el complemento adecuado, configurar el entorno de ejecución de Liberty y configurar tu proyecto para trabajar con Liberty. Ya elijas IBM Liberty Developer Tools o Liberty Tools, ambas proporcionan características robustas para agilizar el desarrollo para WebSphere Liberty dentro del IDE de Eclipse.