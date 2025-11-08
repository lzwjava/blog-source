---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Modos de Chat Personalizados para GitHub Copilot
translated: true
type: note
---

### ¿Qué es chatmode.md?

En la extensión GitHub Copilot para Visual Studio Code (VS Code), los archivos `chatmode.md` se utilizan para definir **modos de chat personalizados**. Estos te permiten configurar Copilot Chat para que adopte comportamientos o personalidades específicas para tareas como planificación, revisiones de seguridad o implementación de código. Cada modo puede especificar instrucciones, herramientas disponibles (por ejemplo, búsqueda, fetch o acceso a repositorios de GitHub) e incluso el modelo de IA a utilizar. Esta característica está en vista previa a partir de VS Code 1.101 y ayuda a adaptar las respuestas para mantener la coherencia en tu flujo de trabajo.

Los modos personalizados se almacenan como archivos Markdown con la extensión `.chatmode.md`, ya sea en tu espacio de trabajo (para compartir en equipo) o en tu perfil de usuario (para reutilización personal).

### ¿Por qué usar modos de chat personalizados?
- **Respuestas Adaptadas**: Hacer cumplir pautas, como generar planes sin editar código.
- **Control de Herramientas**: Limitar las herramientas a solo lectura para planificación o habilitar la edición para implementación.
- **Eficiencia**: Reutilizar configuraciones para roles comunes (por ejemplo, arquitecto, revisor).

### Cómo crear un archivo chatmode.md

1. Abre la **vista de Chat** en VS Code:
   - Haz clic en el icono de Copilot Chat en la barra de título, o usa `Ctrl+Alt+I` (Windows/Linux) / `Cmd+Option+I` (macOS).

2. En la vista de Chat, haz clic en **Configure Chat > Modes**, y luego selecciona **Create new custom chat mode file**. Alternativamente, abre la Paleta de comandos (`Ctrl+Mayús+P` / `Cmd+Mayús+P`) y ejecuta **Chat: New Mode File**.

3. Elige una ubicación:
   - **Espacio de trabajo**: Se guarda en `.github/chatmodes/` por defecto (compartible con tu equipo). Personaliza las carpetas mediante la configuración `chat.modeFilesLocations`.
   - **Perfil de usuario**: Se guarda en la carpeta de tu perfil para sincronizar entre dispositivos.

4. Nombra el archivo (por ejemplo, `planning.chatmode.md`) y edítalo en VS Code.

Para gestionar modos existentes, usa **Configure Chat > Modes** o el comando **Chat: Configure Chat Modes**.

### Estructura del archivo y sintaxis

Un archivo `.chatmode.md` utiliza Markdown con un frontmatter YAML opcional para los metadatos. Aquí está la estructura básica:

- **Frontmatter YAML** (encerrado entre líneas `---`, opcional):
  - `description`: Texto breve que se muestra en el marcador de posición de entrada de chat y en el hover del desplegable.
  - `tools`: Array de nombres de herramientas (por ejemplo, `['fetch', 'search']`). Usa herramientas integradas como `githubRepo` o herramientas de extensión; configúralas mediante **Configure Tools**.
  - `model`: Modelo de IA (por ejemplo, `"Claude Sonnet 4"`). Por defecto, utiliza el modelo seleccionado por ti.

- **Cuerpo**: Instrucciones en Markdown para la IA, incluyendo prompts, pautas o enlaces a archivos externos.

Prioridad de las herramientas: Archivo de prompt > Modo referenciado > Herramientas del modo por defecto.

### Ejemplo de archivo chatmode.md

Esto crea un modo "Planning" para generar planes de implementación sin realizar cambios de código:

```
---
description: Genera un plan de implementación para nuevas características o para refactorizar código existente.
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# Instrucciones del modo Planning

Estás en modo de planificación. Tu tarea es generar un plan de implementación para una nueva característica o para refactorizar código existente. No realices ninguna edición de código, solo genera un plan.

El plan consiste en un documento Markdown con estas secciones:

* **Descripción general**: Breve descripción de la característica o refactorización.
* **Requisitos**: Lista de requisitos.
* **Pasos de implementación**: Pasos detallados para implementar.
* **Pruebas**: Lista de pruebas para verificar.
```

Guarda el archivo y aparecerá en el desplegable de modos de chat.

### Cómo usar un modo de chat personalizado

1. Abre la **vista de Chat** (como se indicó anteriormente).

2. En el desplegable en la parte superior de la vista de Chat (junto al selector de modo), elige tu modo personalizado (por ejemplo, "Planning").

3. La `description` del modo aparece como un marcador de posición en el cuadro de entrada. Escribe tu prompt (por ejemplo, "Planifica una característica de autenticación de usuario").

4. Copilot responde siguiendo las instrucciones y herramientas del modo. Cambia de modo en cualquier momento a través del desplegable; los modos integrados (Ask, Edit, Agent) permanecen disponibles.

Para más ejemplos, consulta las contribuciones de la comunidad en el [repositorio Awesome Copilot](https://github.com/github/awesome-copilot/tree/main).

### Referencias
- [Modos de chat personalizados en VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [Empezar con el chat en VS Code](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)