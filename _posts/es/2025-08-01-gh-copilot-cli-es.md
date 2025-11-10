---
audio: false
generated: true
image: false
lang: es
layout: post
title: Integración de GitHub Copilot con la CLI
translated: true
type: note
---

No puedes invocar directamente GitHub Copilot como un plugin desde la línea de comandos usando una sintaxis como `code --plugin copilot "hi"` para obtener una respuesta. Sin embargo, GitHub Copilot sí ofrece integración con la línea de comandos a través de la CLI de GitHub con la extensión `gh copilot`, que proporciona una interfaz similar a un chat para sugerencias y explicaciones de comandos. Esto no es exactamente lo mismo que un plugin genérico invocado mediante el comando `code`, pero cumple un propósito similar para interacciones en la línea de comandos.

### Detalles sobre GitHub Copilot en la CLI
- **Requisitos**: Necesitas una suscripción a GitHub Copilot, la CLI de GitHub (`gh`) instalada y la extensión `gh-copilot` instalada. Las instrucciones de configuración están disponibles en el repositorio de la CLI de GitHub o en la documentación [Instalación de GitHub CLI](https://cli.github.com/) y [Instalación de GitHub Copilot en la CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).
- **Uso**: Una vez configurado, puedes usar comandos como:
  - `gh copilot suggest -t shell "hi"` para obtener una sugerencia de comando de shell.
  - `gh copilot explain "hi"` para obtener una explicación de un comando.
  - Ejemplo: Ejecutar `gh copilot suggest -t shell "say hello"` podría sugerir `echo "hello"` o un comando de texto a voz como `say "hello"` en macOS, dependiendo del contexto.
- **Limitaciones**: La interfaz de CLI está diseñada para tareas relacionadas con la línea de comandos (por ejemplo, comandos de shell, Git o CLI de GitHub) y no admite respuestas conversacionales genéricas como un chatbot. También solo admite prompts en inglés [Uso responsable de GitHub Copilot en la CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **Modo Interactivo**: Después de ejecutar un comando `suggest`, Copilot inicia una sesión interactiva donde puedes refinar la sugerencia, ejecutarla (se copia al portapapeles) o calificarla. Para la ejecución automática, necesitas configurar el alias `ghcs` [Usar GitHub Copilot en la línea de comandos](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line).[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### Por qué `code --plugin copilot "hi"` No Funciona
- **CLI de Visual Studio Code**: El comando `code` (para VS Code) admite opciones como `--install-extension` para instalar extensiones, pero no tiene un flag `--plugin` para invocar extensiones directamente con entrada como `"hi"`. Las extensiones como GitHub Copilot generalmente operan dentro del editor VS Code, proporcionando sugerencias en línea o interfaces de chat, no como herramientas CLI independientes [GitHub Copilot en VS Code](https://code.visualstudio.com/docs/copilot/overview).[](https://code.visualstudio.com/docs/copilot/overview)
- **Arquitectura de Copilot**: El plugin de GitHub Copilot para VS Code se comunica con un servidor de lenguaje y el backend de GitHub para completados de código y chat. No existe un mecanismo de API pública o CLI para pasar cadenas arbitrarias como `"hi"` directamente al plugin desde la línea de comandos y obtener una respuesta [¿Cómo invocar Github Copilot programáticamente?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **Alternativa para Entrada Genérica**: Si deseas enviar un prompt como `"hi"` a Copilot y obtener una respuesta, necesitarías usar Copilot Chat dentro de VS Code u otro IDE compatible, o explorar otras herramientas CLI de IA que admitan prompts conversacionales (por ejemplo, AI Shell de Microsoft para Azure CLI) [Usar Microsoft Copilot en Azure con AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### Solución Alternativa para Tu Objetivo
Si tu objetivo es invocar un asistente de IA como Copilot desde la línea de comandos con un prompt como `"hi"` y obtener una respuesta, puedes:
1. **Usar `gh copilot` para Tareas de Línea de Comandos**:
   - Instalar GitHub CLI y la extensión Copilot.
   - Ejecutar `gh copilot suggest -t shell "greet with hi"` para obtener un comando como `echo "hi"`.
   - Esto está limitado a contextos de línea de comandos, por lo que `"hi"` solo puede no producir una respuesta significativa a menos que se enmarque como una solicitud de comando.
2. **Usar Copilot Chat de VS Code**:
   - Abrir VS Code, usar la interfaz de Copilot Chat (accesible mediante `⌃⌘I` o el icono de chat) y escribir `"hi"` para obtener una respuesta conversacional.
   - Esto requiere interacción manual dentro del editor, no una invocación CLI [Hoja de referencia de GitHub Copilot en VS Code](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet).[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **Explorar Otras Herramientas CLI de IA**:
   - **AI Shell**: AI Shell de Microsoft permite prompts en lenguaje natural en la CLI para tareas relacionadas con Azure. Puedes instalarlo y probar prompts como `"hi"`, aunque está optimizado para comandos de Azure CLI y PowerShell [Usar Microsoft Copilot en Azure con AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli).[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **Scripts Personalizados**: Podrías escribir un script para interactuar con la API de un modelo de IA (por ejemplo, la API de OpenAI, si es accesible) para procesar prompts como `"hi"`. Sin embargo, la API de GitHub Copilot no está disponible públicamente para tal uso [¿Cómo invocar Github Copilot programáticamente?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **Simular el Comportamiento del Plugin**:
   - Crear un script de shell o un alias que canalice la entrada a `gh copilot suggest` u otra herramienta CLI de IA.
   - Ejemplo:
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     Esto sugeriría un comando como `echo "hi"` o similar.

### Invocación Programática
Si estás buscando invocar programáticamente una funcionalidad similar a Copilot (como implica tu ejemplo), ten en cuenta que:
- GitHub Copilot no expone una API pública para acceso programático directo. Algunos esfuerzos de la comunidad han reverse-engineered el servidor de lenguaje o usado proxies para capturar sugerencias, pero estos son complejos y arriesgados (por ejemplo, posibilidad de bloqueo de cuentas) [¿Cómo invocar Github Copilot programáticamente?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically).[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- Podrías explorar alternativas de código abierto u otros modelos de IA con integraciones CLI (por ejemplo, las herramientas CLI de Hugging Face o LLMs locales como LLaMA con wrappers personalizados).

### Conclusión
Si bien `code --plugin copilot "hi"` no es compatible, puedes lograr una funcionalidad similar usando `gh copilot` para tareas de línea de comandos o Copilot Chat en VS Code para prompts conversacionales. Para una experiencia genérica de IA en CLI, considera herramientas como AI Shell o scripts personalizados con otras APIs de IA. Siempre verifica las sugerencias, ya que las respuestas de Copilot en la CLI pueden contener errores o sesgos de los datos de entrenamiento [Uso responsable de GitHub Copilot en la CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli).[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

Si tienes un caso de uso específico (por ejemplo, IA conversacional vs. generación de comandos), ¡házmelo saber y puedo adaptar la solución aún más!