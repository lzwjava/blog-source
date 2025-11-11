---
audio: false
generated: true
lang: es
layout: post
title: Uso de GitHub Copilot en Visual Studio Code
translated: true
type: note
---

GitHub Copilot es un asistente de codificación impulsado por IA desarrollado por GitHub y OpenAI, diseñado para mejorar la productividad de los desarrolladores en Visual Studio Code (VS Code). Ofrece finalizaciones de código conscientes del contexto, chat en lenguaje natural y capacidades avanzadas de edición. Esta guía te lleva a través de la configuración de Copilot, la exploración de sus características y la optimización de tu flujo de trabajo con consejos y mejores prácticas.

## 1. Introducción a GitHub Copilot
GitHub Copilot actúa como un programador en pareja con IA, ofreciendo sugerencias de código en tiempo real, respondiendo preguntas de codificación y automatizando tareas repetitivas. Está impulsado por grandes modelos de lenguaje entrenados con vastos conjuntos de datos de código público, lo que le permite admitir numerosos lenguajes de programación y frameworks, incluyendo Python, JavaScript, TypeScript, Ruby, Go, C# y C++.

Las características clave incluyen:
- **Finalizaciones de Código**: Sugiere fragmentos de código mientras escribes, desde líneas individuales hasta funciones completas.
- **Copilot Chat**: Permite consultas en lenguaje natural para explicar código, generar fragmentos o depurar problemas.
- **Modo Agente**: Automatiza tareas de codificación de varios pasos, como refactorizar o crear aplicaciones.
- **Instrucciones Personalizadas**: Adapta las sugerencias para que coincidan con tu estilo de codificación o los requisitos del proyecto.

## 2. Configuración de GitHub Copilot en VS Code

### Prerrequisitos
- **VS Code**: Descarga e instala Visual Studio Code desde el [sitio web oficial](https://code.visualstudio.com/). Asegúrate de tener una versión compatible (cualquier versión reciente admite Copilot).
- **Cuenta de GitHub**: Necesitas una cuenta de GitHub con acceso a Copilot. Las opciones incluyen:
  - **Copilot Gratuito**: Finalizaciones e interacciones de chat limitadas por mes.
  - **Copilot Pro/Pro+**: Planes de pago con límites más altos y características avanzadas.
  - **Acceso de Organización**: Si lo proporciona tu organización, consulta con tu administrador los detalles de acceso.
- **Conexión a Internet**: Copilot requiere una conexión activa para proporcionar sugerencias.

### Pasos de Instalación
1. **Abre VS Code**:
   Inicia Visual Studio Code en tu máquina.

2. **Instala la Extensión GitHub Copilot**:
   - Ve a la vista **Extensiones** (Ctrl+Shift+X o Cmd+Shift+X en macOS).
   - Busca "GitHub Copilot" en el Marketplace de Extensiones.
   - Haz clic en **Instalar** para la extensión oficial GitHub Copilot. Esto también instala automáticamente la extensión Copilot Chat.

3. **Inicia Sesión en GitHub**:
   - Después de la instalación, puede aparecer un aviso en la Barra de Estado de VS Code (esquina inferior derecha) para configurar Copilot.
   - Haz clic en el icono de Copilot y selecciona **Iniciar sesión** para autenticarte con tu cuenta de GitHub.
   - Si no aparece ningún aviso, abre la Paleta de Comandos (Ctrl+Shift+P o Cmd+Shift+P) y ejecuta el comando `GitHub Copilot: Sign in`.
   - Sigue el flujo de autenticación basado en el navegador, copiando el código proporcionado por VS Code en GitHub.

4. **Verifica la Activación**:
   - Una vez que hayas iniciado sesión, el icono de Copilot en la Barra de Estado debería volverse verde, indicando un estado activo.
   - Si no tienes una suscripción a Copilot, se te inscribirá en el plan Copilot Gratuito con uso mensual limitado.

5. **Opcional: Desactiva la Telemetría**:
   - Por defecto, Copilot recopila datos de telemetría. Para desactivarlo, ve a **Configuración** (Ctrl+, o Cmd+,), busca `telemetry.telemetryLevel` y establécelo en `off`. Alternativamente, ajusta la configuración específica de Copilot en `GitHub Copilot Settings`.

> **Nota**: Si tu organización ha desactivado Copilot Chat o restringido características, contacta a tu administrador. Para solución de problemas, consulta la [Guía de Solución de Problemas de GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting).[](https://code.visualstudio.com/docs/copilot/setup)

## 3. Características Principales de GitHub Copilot en VS Code

### 3.1 Finalizaciones de Código
Copilot sugiere código mientras escribes, desde líneas individuales hasta funciones o clases completas, basándose en el contexto de tu código y la estructura del archivo.
- **Cómo Funciona**:
  - Comienza a escribir en un lenguaje admitido (por ejemplo, JavaScript, Python, C#).
  - Copilot muestra sugerencias en texto "fantasma" atenuado.
  - Presiona **Tab** para aceptar una sugerencia o continúa escribiendo para ignorarla.
  - Usa **Alt+]** (siguiente) o **Alt+[** (anterior) para recorrer múltiples sugerencias.
- **Ejemplo**:
  ```javascript
  // Calcular el factorial de un número
  function factorial(n) {
  ```
  Copilot podría sugerir:
  ```javascript
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```
  Presiona **Tab** para aceptar la sugerencia.

- **Consejos**:
  - Usa nombres de funciones descriptivos o comentarios para guiar a Copilot (por ejemplo, `// Ordenar un array en orden ascendente`).
  - Para múltiples sugerencias, pasa el cursor sobre la sugerencia para abrir el Panel de Finalizaciones (Ctrl+Enter) y ver todas las opciones.

### 3.2 Copilot Chat
Copilot Chat te permite interactuar con Copilot usando lenguaje natural para hacer preguntas, generar código o depurar problemas.
- **Acceder al Chat**:
  - Abre la **Vista de Chat** desde la Barra de Actividad o usa **Ctrl+Alt+I** (Windows/Linux) o **Cmd+Ctrl+I** (macOS).
  - Alternativamente, usa **Chat en Línea** (Ctrl+I o Cmd+I) directamente en el editor para consultas específicas del contexto.
- **Casos de Uso**:
  - **Explicar Código**: Selecciona un bloque de código, abre el Chat en Línea y escribe `explica este código`.
  - **Generar Código**: Escribe `escribe una función en Python para invertir una cadena` en la Vista de Chat.
  - **Depuración**: Pega un mensaje de error en el Chat y pide una solución.
- **Ejemplo**:
  En la Vista de Chat, escribe:
  ```
  ¿Qué es la recursión?
  ```
  Copilot responde con una explicación detallada, a menudo incluyendo ejemplos de código en Markdown.

- **Comandos de Barra**:
  Usa comandos como `/explain`, `/doc`, `/fix`, `/tests` o `/optimize` para especificar tareas. Por ejemplo:
  ```
  /explain this function
  ```
  con una función seleccionada generará una explicación detallada.

### 3.3 Modo Agente (Vista Previa)
El Modo Agente permite a Copilot manejar de forma autónoma tareas de codificación de varios pasos, como crear aplicaciones, refactorizar código o escribir pruebas.
- **Cómo Usarlo**:
  - Abre la **Vista de Ediciones de Copilot** en VS Code Insiders o Stable (si está disponible).
  - Selecciona **Agente** del menú desplegable de modos.
  - Introduce un prompt, por ejemplo, `Crea un componente de formulario React con campos de nombre y email`.
  - Copilot analiza tu base de código, sugiere ediciones y puede ejecutar comandos de terminal o pruebas.
- **Capacidades**:
  - Genera código a través de múltiples archivos.
  - Monitorea errores e itera para solucionar problemas.
  - Integra nuevas bibliotecas o migra código a frameworks modernos.

> **Nota**: El Modo Agente es experimental y funciona mejor en repositorios pequeños. Comparte tus comentarios a través del repositorio de GitHub de VS Code.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 3.4 Instrucciones Personalizadas
Personaliza Copilot para que se alinee con tu estilo de codificación o los requisitos del proyecto.
- **Configuración**:
  - Crea un archivo `.github/copilot-instructions.md` en tu espacio de trabajo.
  - Añade instrucciones en Markdown, por ejemplo, `Usa snake_case para los nombres de variables en Python`.
  - Habilita las instrucciones personalizadas en **Configuración** > **GitHub** > **Copilot** > **Enable custom instructions** (VS Code 17.12 o posterior).
- **Ejemplo**:
  ```markdown
  # Instrucciones Personalizadas de Copilot
  - Usa camelCase para las variables en JavaScript.
  - Prefiere async/await sobre .then() para las promesas.
  ```
  Copilot adaptará las sugerencias a estas preferencias.

### 3.5 Contexto del Espacio de Trabajo con @workspace
Usa el comando `@workspace` para consultar toda tu base de código.
- **Ejemplo**:
  En la Vista de Chat, escribe:
  ```
  @workspace ¿Dónde está configurada la cadena de conexión a la base de datos?
  ```
  Copilot busca en tu espacio de trabajo y hace referencia a los archivos relevantes.

### 3.6 Sugerencias de Siguiente Edición (Vista Previa)
Copilot predice y sugiere la siguiente edición lógica basándose en tus cambios recientes.
- **Cómo Funciona**:
  - Mientras editas código, Copilot resalta las posibles siguientes ediciones.
  - Acepta las sugerencias con **Tab** o modifícalas a través del Chat en Línea.
- **Caso de Uso**: Ideal para refactorización iterativa o para completar cambios de código relacionados.

## 4. Consejos y Trucos para Optimizar el Uso de Copilot

### 4.1 Escribe Prompts Efectivos
- Sé específico: En lugar de `escribe una función`, prueba `escribe una función en Python para ordenar una lista de diccionarios por la clave 'edad'`.
- Proporciona contexto: Incluye detalles del framework o biblioteca (por ejemplo, `usa React hooks`).
- Usa comentarios: Escribe `// Genera un endpoint de API REST en Express` para guiar las finalizaciones.

### 4.2 Aprovecha el Contexto
- **Referencia Archivos/Símbolos**: Usa `#nombre_de_archivo`, `#carpeta` o `#símbolo` en los prompts del Chat para delimitar el contexto.
  ```
  /explain #src/utils.js
  ```
- **Arrastrar y Soltar**: Arrastra archivos o pestañas del editor al prompt del Chat para añadir contexto.
- **Adjuntar Imágenes**: En VS Code 17.14 Preview 1 o posterior, adjunta capturas de pantalla para ilustrar problemas (por ejemplo, errores de UI).

### 4.3 Usa Comandos de Barra
- `/doc**: Genera documentación para una función.
- `/fix**: Sugiere soluciones para errores.
- `/tests**: Crea pruebas unitarias para el código seleccionado.
- Ejemplo:
  ```
  /tests Genera pruebas Jest para esta función
  ```

### 4.4 Guarda y Reutiliza Prompts
- Crea un archivo `.prompt.md` en `.github/prompts/` para almacenar prompts reutilizables.
- Ejemplo:
  ```markdown
  # Prompt para Componente React
  Genera un componente funcional de React con estilos Tailwind CSS. Pregunta el nombre del componente y las props si no se proporcionan.
  ```
- Adjunta el prompt en el Chat para reutilizarlo en diferentes proyectos.

### 4.5 Elige el Modelo Correcto
- Copilot admite múltiples modelos de lenguaje (por ejemplo, GPT-4o, Claude Sonnet).
- Selecciona modelos en el menú desplegable de la Vista de Chat para una codificación más rápida o un razonamiento más profundo.
- Para tareas complejas, Claude Sonnet puede tener un mejor rendimiento en el Modo Agente.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 4.6 Indexa tu Espacio de Trabajo
- Habilita la indexación del espacio de trabajo para búsquedas de código más rápidas y precisas.
- Usa un índice remoto para repositorios de GitHub o un índice local para bases de código grandes.

## 5. Mejores Prácticas
- **Revisa las Sugerencias**: Verifica siempre las sugerencias de Copilot para asegurar su precisión y alineación con los estándares de tu proyecto.
- **Combina con IntelliCode**: En Visual Studio, Copilot complementa a IntelliCode para finalizaciones mejoradas.[](https://devblogs.microsoft.com/visualstudio/github-copilot-in-visual-studio-2022/)
- **Verifica la Seguridad**: Copilot puede sugerir código con vulnerabilidades. Revisa las sugerencias, especialmente en proyectos sensibles, y verifica las políticas de tu organización.[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Usa Nombres Significativos**: Los nombres descriptivos de variables y funciones mejoran la calidad de las sugerencias.
- **Itera con el Chat**: Refina los prompts si las sugerencias iniciales no son acertadas.
- **Monitorea los Límites de Uso**: Con Copilot Gratuito, realiza un seguimiento de tus finalizaciones e interacciones de chat mensuales a través de la configuración de la cuenta de GitHub o la insignia de Copilot en VS Code.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)

## 6. Solución de Problemas Comunes
- **Copilot Inactivo**: Asegúrate de haber iniciado sesión con una cuenta de GitHub que tenga acceso a Copilot. Actualiza las credenciales a través del menú desplegable de la Barra de Estado de Copilot.
- **Sin Sugerencias**: Verifica tu conexión a internet o cambia a un lenguaje admitido. Ajusta la configuración en **Herramientas** > **Opciones** > **GitHub Copilot**.
- **Funcionalidad Limitada**: Si alcanzas el límite de uso de Copilot Gratuito, volverás a las sugerencias de IntelliCode. Actualiza a un plan de pago o verifica tu estado.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)
- **Problemas de Red**: Consulta la [Guía de Solución de Problemas de GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting).

## 7. Casos de Uso Avanzados
- **Consultas a Bases de Datos**: Pide a Copilot que genere consultas SQL (por ejemplo, `Escribe una consulta SQL para unir dos tablas`).
- **Desarrollo de API**: Solicita código para endpoints de API (por ejemplo, `Crea una ruta en Flask para manejar solicitudes POST`).
- **Pruebas Unitarias**: Usa `/tests` para generar pruebas para frameworks como Jest o Pytest.
- **Refactorización**: Usa el Modo Agente para refactorizar código a través de archivos (por ejemplo, `Migra este código jQuery a React`).

## 8. Consideraciones de Privacidad y Seguridad
- **Uso de Datos**: Copilot transmite fragmentos de código a los servidores de GitHub en tiempo real para generar sugerencias, pero no los retiene (Copilot for Business descarta los fragmentos inmediatamente).[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Coincidencia con Código Público**: Copilot puede sugerir código que coincida con repositorios públicos de GitHub. Habilita la referencia de código para ver los detalles de la licencia.[](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)
- **Políticas Organizacionales**: Verifica si tu organización permite el uso de Copilot, ya que algunas desactivan el Chat o restringen las sugerencias.[](https://docs.github.com/en/copilot/quickstart)
- **Telemetría**: Desactiva la telemetría en la configuración de VS Code si lo deseas.[](https://code.visualstudio.com/docs/copilot/setup)

## 9. Recursos para Aprender Más
- [Documentación de GitHub Copilot](https://docs.github.com/en/copilot)
- [Inicio Rápido de Copilot en VS Code](https://code.visualstudio.com/docs/copilot/copilot-quickstart)
- [Tutorial de Copilot Chat](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [Serie de Copilot en VS Code en YouTube](https://www.youtube.com/playlist?list=PLj6YeMhvp2S6X0vF4TrRkpZ7GIqM3oPWp)
- [Preguntas Frecuentes de GitHub Copilot](https://docs.github.com/en/copilot/faq)

## 10. Conclusión
GitHub Copilot en VS Code es una herramienta poderosa que agiliza la codificación al proporcionar sugerencias inteligentes, responder preguntas y automatizar tareas complejas. Al configurarlo correctamente, aprovechar sus características y seguir las mejores prácticas, puedes aumentar significativamente tu productividad y concentrarte en tareas de codificación creativas. Experimenta con las capacidades de Copilot, personalízalo para tu flujo de trabajo y mantente atento a la seguridad y los límites de uso para aprovechar al máximo este programador en pareja con IA.