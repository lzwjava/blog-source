---
audio: false
generated: true
lang: es
layout: post
title: Extensión Liberty Tools en Visual Studio Code
translated: true
type: note
---

A continuación se presenta un resumen de cómo puedes usar la extensión Liberty Tools en Visual Studio Code para trabajar con un servidor WebSphere Liberty:

---

### 1. Instalar la Extensión Liberty Tools
- **Buscar e Instalar:**  
  Abre la vista de Extensiones de VS Code, busca **"IBM WebSphere Liberty Tools"** e instálala.
- **Beneficios de la Extensión:**  
  Esta extensión integra la gestión del servidor, el despliegue de aplicaciones y la depuración en VS Code.

---

### 2. Preparar tu Servidor WebSphere Liberty
- **Instalar o Apuntar a un Runtime de Liberty:**  
  Si aún no tienes un servidor Liberty instalado, descárgalo e instálalo desde IBM. Si ya está instalado, ten a mano su directorio de instalación.
- **Garantizar la Compatibilidad:**  
  Verifica que la versión de tu runtime de Liberty sea compatible con la extensión.

---

### 3. Configurar tu Servidor Liberty en VS Code
- **Crear una Nueva Instancia del Servidor:**  
  Abre la Paleta de Comandos (`Ctrl+Shift+P` o `Cmd+Shift+P`) y ejecuta el comando:  
  `Liberty: Create Server`  
  Sigue las instrucciones para:
  - Seleccionar la carpeta de instalación del runtime.
  - Especificar el archivo de configuración del servidor (normalmente el `server.xml`).
- **Proyectos Existentes:**  
  Si ya tienes una aplicación basada en Liberty, abre el espacio de trabajo para que la extensión pueda detectar y ayudar a gestionar la configuración de tu servidor.

---

### 4. Añadir tu Aplicación
- **Desplegar la Aplicación:**  
  Puedes añadir tu aplicación al servidor ya sea:
  - Editando el `server.xml` para incluir el contexto y los detalles de despliegue de tu aplicación, o
  - Usando las opciones de la UI de la extensión (a menudo disponibles en la vista Liberty) para "Añadir Aplicación" o "Desplegar Aplicación".
- **Integración con Build:**  
  Si estás usando Maven o Gradle, la extensión también puede ofrecer tareas que construyan tu aplicación antes del despliegue.

---

### 5. Iniciar, Detener y Depurar el Servidor
- **Iniciar el Servidor:**  
  En la vista Liberty (normalmente disponible como un panel o vista de árbol dedicada en VS Code), haz clic derecho en tu servidor configurado y selecciona **"Start Server"**.  
  El panel de salida mostrará los logs de inicio y cualquier mensaje de configuración.
- **Detener el Servidor:**  
  De manera similar, haz clic derecho y elige **"Stop Server"** para apagar tu instancia.
- **Depuración:**  
  Si necesitas depurar tu aplicación:
  - Establece puntos de interrupción en tu código.
  - Usa la paleta de comandos para ejecutar **"Liberty: Debug Server"** (o usa las opciones de depuración proporcionadas en la vista Liberty) para conectar el depurador de VS Code a tu servidor en ejecución.
  - Tus puntos de interrupción deberían activarse ahora mientras tu aplicación procesa las solicitudes.

---

### 6. Características y Consejos Adicionales
- **Monitoreo de Logs en Tiempo Real:**  
  La extensión proporciona una forma de ver los logs del servidor Liberty en tiempo real, facilitando el diagnóstico de problemas.
- **Editar la Configuración del Servidor:**  
  Benefíciate de IntelliSense y sugerencias al editar tu `server.xml` directamente dentro de VS Code.
- **Integración de Tareas:**  
  Utiliza las tareas de VS Code si estás ejecuting builds o despliegues automatizados como parte de tu flujo de trabajo de desarrollo.
- **Soporte para Contenedores y Remoto:**  
  Dependiendo de tu configuración, también podrías configurar Liberty para que se ejecute dentro de contenedores o entornos remotos, con comandos adicionales disponibles en la extensión.

---

### Notas Finales
Usar la extensión Liberty Tools agiliza el proceso de desarrollar, desplegar y depurar tus aplicaciones de WebSphere Liberty directamente dentro de VS Code. Esta integración ayuda a reducir el cambio de contexto y acelera tu ciclo de desarrollo.

No dudes en consultar la documentación oficial de IBM sobre la extensión Liberty Tools para cualquier configuración avanzada o paso de resolución de problemas.