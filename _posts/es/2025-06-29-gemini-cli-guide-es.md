---
audio: false
generated: true
lang: es
layout: post
title: Instalar y usar Gemini CLI
translated: true
type: note
---

A continuación, se presenta una guía concisa para instalar, configurar y usar la **Google Gemini CLI**, un agente de IA de código abierto que integra las capacidades de Gemini en tu terminal para programación, automatización de tareas y más. Esta guía se basa en la información más reciente disponible al 29 de junio de 2025.

---

## **Guía de Google Gemini CLI**

### **¿Qué es Gemini CLI?**
Gemini CLI es una herramienta de línea de comandos de código abierto desarrollada por Google que lleva el poder del modelo Gemini 2.5 Pro (con una ventana de contexto de 1 millón de tokens) a tu terminal. Soporta programación, depuración, generación de contenido, automatización de tareas y tareas multimodales como generación de imágenes y video. Es gratis usarlo con una cuenta de Google y se integra con herramientas como Google Search y servidores Model Context Protocol (MCP).

---

### **Prerrequisitos**
- **Node.js**: Versión 18 o superior. Verifica con `node -v`. Instálalo desde [nodejs.org](https://nodejs.org) si es necesario.
- **Cuenta de Google**: Requerida para acceso gratuito a Gemini 2.5 Pro (60 solicitudes/minuto, 1,000 solicitudes/día).
- (Opcional) **API Key**: Para límites más altos o modelos específicos, genera una desde [Google AI Studio](https://aistudio.google.com).
- (Opcional) **Docker**: Para integración con servidores MCP (ej. herramientas de GitHub).

---

### **Instalación**
Hay dos formas de comenzar con Gemini CLI:

1. **Instalar Globalmente**:
   ```bash
   npm install -g @google/gemini-cli
   gemini
   ```
   Esto instala la CLI globalmente y la ejecuta con el comando `gemini`.

2. **Ejecutar Sin Instalar**:
   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```
   Esto ejecuta la CLI directamente sin instalación, ideal para pruebas.

---

### **Configuración**
1. **Iniciar la CLI**:
   - Ejecuta `gemini` en tu terminal.
   - En la primera ejecución, selecciona un tema (ej. ASCII, oscuro, claro) y presiona Enter.

2. **Autenticar**:
   - Elige **Iniciar sesión con Google** para acceso gratuito (recomendado para la mayoría de usuarios).
   - Se abrirá una ventana del navegador; inicia sesión con tu cuenta de Google.
   - Alternativamente, usa una API key:
     - Genera una key desde [Google AI Studio](https://aistudio.google.com).
     - Establécela como una variable de entorno:
       ```bash
       export GEMINI_API_KEY=TU_API_KEY
       ```
     - Esto es útil para límites más altos o uso empresarial.

3. **Navegar a Tu Proyecto**:
   - Ejecuta `gemini` en el directorio raíz de tu proyecto para proporcionar contexto para tareas relacionadas con código.

---

### **Uso Básico**
Gemini CLI opera en un entorno interactivo Read-Eval-Print Loop (REPL). Escribe comandos o prompts en lenguaje natural para interactuar con el modelo Gemini. Aquí hay algunas tareas comunes:

1. **Explicación de Código**:
   - Navega a una carpeta de proyecto y ejecuta:
     ```bash
     gemini
     ```
   - Prompt: `Explica la arquitectura de este proyecto` o `Describe la función principal en main.py`.
   - La CLI lee los archivos y proporciona una explicación estructurada.

2. **Generación de Código**:
   - Prompt: `Crea una aplicación simple de lista de tareas en HTML, CSS y JavaScript`.
   - La CLI genera el código y puede guardarlo en archivos si se lo solicitas.

3. **Depuración**:
   - Pega un mensaje de error o un stack trace y pregunta: `¿Qué está causando este error?`.
   - La CLI analiza el error y sugiere correcciones, potencialmente usando Google Search para contexto adicional.

4. **Gestión de Archivos**:
   - Prompt: `Organiza mis facturas PDF por mes de gasto`.
   - La CLI puede manipular archivos o convertir formatos (ej. imágenes a PNG).

5. **Integración con GitHub**:
   - Usa servidores MCP para tareas de GitHub (ej. listar issues):
     - Configura un servidor MCP de GitHub en `.gemini/settings.json` con un Personal Access Token (PAT).
     - Prompt: `Obtén todos los issues abiertos asignados a mí en el repositorio foo/bar`.
   - Ejecuta `/mcp` para listar los servidores MCP configurados y las herramientas.

6. **Tareas Multimodales**:
   - Genera medios con herramientas como Imagen o Veo:
     - Prompt: `Crea un video corto de las aventuras de un gato en Australia usando Veo`.

---

### **Características Clave**
- **Archivos de Contexto (GEMINI.md)**: Añade un archivo `GEMINI.md` en la raíz de tu proyecto para definir estilos de codificación, reglas del proyecto o preferencias (ej. "Usa async/await para JavaScript"). La CLI usa esto para respuestas personalizadas.
- **Herramientas Integradas**:
   - `/tools`: Lista las herramientas disponibles (ej. Google Search, operaciones de archivos).
   - `/compress`: Resume el contexto del chat para ahorrar tokens.
   - `/bug`: Reporta issues directamente al repositorio GitHub de Gemini CLI.
- **Modo No Interactivo**: Para scripting, canaliza comandos:
   ```bash
   echo "Escribe un script de Python" | gemini
   ```
- **Memoria de Conversación**: Guarda el historial de sesiones con `/save <etiqueta>` y reanuda con `/restore <etiqueta>`.
- **Configuración Personalizada**:
   - Edita `~/.gemini/settings.json` para configuraciones globales o `.gemini/settings.json` en un proyecto para configuraciones locales.
   - Ejemplo: Establecer servidores MCP o temas personalizados.

---

### **Consejos y Trucos**
- **Comienza con Planes**: Para tareas complejas, pide un plan primero: `Crea un plan de implementación detallado para un sistema de inicio de sesión`. Esto asegura una salida estructurada.
- **Usa Contexto Local**: Codifica detalles específicos del proyecto en `GEMINI.md` en lugar de depender de servidores MCP para respuestas más rápidas y confiables.
- **Depuración**: Habilita el registro detallado con `DEBUG=true gemini` para información detallada de solicitud/respuesta.
- **Revisa los Cambios**: Siempre revisa las modificaciones de archivos o comandos antes de aprobarlos (escribe `y` para confirmar).
- **Explora Herramientas**: Ejecuta `/tools` para descubrir capacidades integradas como búsqueda web o guardado de memoria.

---

### **Solución de Problemas**
- **Problemas de Autenticación**: Asegúrate de que tu cuenta de Google o API key sean válidas. Usa `/auth` para cambiar de método.
- **Límites de Tasa**: El nivel gratuito permite 60 solicitudes/minuto y 1,000/día. Para límites más altos, usa una API key o Vertex AI.
- **Errores**: Consulta la [Guía de Solución de Problemas](https://github.com/google-gemini/gemini-cli/docs/troubleshooting.md) en GitHub.
- **Respuestas Lentas**: La CLI está en vista previa y puede ser lenta con las llamadas a la API. Reporta comentarios en GitHub.

---

### **Uso Avanzado**
- **Integración con Servidores MCP**:
  - Configura un servidor MCP de GitHub para interacciones con repositorios:
    - Crea un PAT de GitHub con los scopes necesarios.
    - Añádelo a `.gemini/settings.json`:
      ```json
      {
        "mcpServers": [
          {
            "name": "github",
            "url": "http://localhost:8080",
            "type": "github"
          }
        ]
      }
      ```
    - Ejecuta un contenedor Docker para el servidor MCP (consulta la documentación de GitHub).
- **Scripting**: Automatiza tareas integrando Gemini CLI en scripts:
  ```bash
  gemini --non-interactive "Genera un script bash para respaldar mis archivos"
  ```
- **Prompts Multimodales**:
  - Ejemplo: `Describe esta imagen: ruta/a/la/imagen.jpg` (requiere un modelo con capacidad de visión como `gemini-pro-vision`).

---

### **Limitaciones**
- **Etapa de Vista Previa**: Gemini CLI está en pre-GA, con potencial de soporte limitado o bugs.
- **No Completamente de Código Abierto**: Solo la interfaz de la CLI tiene licencia Apache 2.0; el modelo Gemini es propietario.
- **Compartición de Cuota**: Los límites se comparten con Gemini Code Assist si se usa.
- **Precios Futuros**: Los precios posteriores a la vista previa no están claros; las características avanzadas pueden requerir pago.

---

### **Recursos**
- **GitHub Oficial**: [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Documentación**: [gemini-cli.click](https://gemini-cli.click) o documentación de GitHub
- **Anuncio en el Blog**: [blog.google](https://blog.google)
- **Comentarios**: Reporta bugs o sugerencias en GitHub.

---

### **Flujo de Trabajo de Ejemplo**
1. Instalar: `npm install -g @google/gemini-cli`
2. Ejecutar: `cd mi-proyecto && gemini`
3. Autenticar: Inicia sesión con Google.
4. Prompt: `Escribe un script de Python para una API REST con FastAPI`.
5. Revisa y guarda el código generado.
6. Usa `/tools` para explorar características adicionales como la integración con GitHub.

---

Gemini CLI es una herramienta poderosa para desarrolladores, que ofrece una integración de IA perfecta en la terminal. Comienza de forma simple, aprovecha `GEMINI.md` para el contexto y explora sus capacidades multimodales para aumentar la productividad. Para más ejemplos, consulta los [tutoriales de GitHub](https://github.com/google-gemini/gemini-cli/docs/cli/tutorials.md).

¡Si necesitas ejemplos específicos o tienes preguntas sobre una característica en particular, házmelo saber!