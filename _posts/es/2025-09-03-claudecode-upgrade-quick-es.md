---
audio: false
generated: true
image: false
lang: es
layout: post
title: Actualización Rápida de Código Claude Ahora
translated: true
type: note
---

Si estás buscando **actualizar Claude Code**, el agente de codificación de línea de comandos de Anthropic, aquí te explicamos cómo puedes hacerlo—y conseguir que las últimas capacidades, como los modos de aprendizaje y los subagentes personalizados, funcionen sin problemas.

---

### Cómo actualizar Claude Code

1.  **Verifica tu versión actual**
    Ejecuta:

    ```
    claude --version
    ```

    Esto te permite ver qué versión estás ejecutando actualmente.

2.  **Actualiza via npm**
    El método de actualización más simple es:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    Esto descarga la última versión desde npm.
    Usuarios en Reddit reportan que esto solucionó errores y mejoró la capacidad de respuesta. Uno escribió:

    > “Después de actualizar a la última versión (1.0.18), es como la noche y el día — se siente mucho más inteligente y con mejor capacidad de respuesta.”
    > ([Reddit][1], [Anthropic][2])

3.  **Alternativamente, usa el instalador nativo (Beta)**
    Si prefieres un binario independiente (en lugar de npm), prueba:

    ```
    curl -fsSL https://claude.ai/install.sh | bash -s latest
    ```

    (En Windows, usa la versión de PowerShell)
    ([Anthropic][3])

4.  **Verifica la actualización**
    Después de la instalación, reinicia tu terminal y ejecuta `claude --version` nuevamente para confirmar que la nueva versión está activa.

5.  **Solución de problemas de instalación**
    Si enfrentas problemas, intenta desinstalar primero:

    ```
    npm uninstall -g @anthropic-ai/claude-code
    npm install -g @anthropic-ai/claude-code
    ```

    Algunos usuarios encontraron que esta secuencia resolvió fallos en la actualización. ([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### ¿Qué hay de nuevo en las actualizaciones recientes?

#### Modos de Aprendizaje

Anthropic añadió recientemente dos nuevos estilos de aprendizaje dentro de Claude Code: **"Explicativo"** y **"Aprendizaje"**. Estos te ayudan a entender el razonamiento detrás del código generado en lugar de solo darte soluciones. Para activarlos:

1.  Asegúrate de haber actualizado Claude Code.
2.  Ejecuta `/output-styles` en tu sesión de Claude Code.
3.  Elige entre el estilo **Predeterminado**, **Explicativo** o **Aprendizaje**.
    Esta función se lanzó el **14 de agosto de 2025**. ([Tom's Guide][7])

#### Subagentes Personalizados

Claude Code ahora admite **subagentes**—asistentes de IA especializados para tareas específicas (por ejemplo, corrección de errores, refactorización, documentación). Puedes establecer diferentes prompts del sistema, permisos de herramientas y ventanas de contexto para cada uno.
Para configurar uno:

1.  Ejecuta `/agents`
2.  Elige "Crear nuevo agente" (a nivel de usuario o de proyecto)
3.  Define su comportamiento, las herramientas permitidas y guárdalo.
    Los subagentes ayudan a mantener tu flujo de trabajo más limpio, más enfocado y consciente del contexto. ([Anthropic][8])

---

### Resumen Rápido (Sin Tablas, Solo Pasos Claros)

*   **Para Actualizar**:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    o usa la instalación nativa con `curl | bash -s latest`.

*   **Habilitar Modos de Aprendizaje**:

    *   Actualiza
    *   Dentro de Claude Code: ejecuta `/output-styles` y elige tu modo.

*   **Crear Subagentes**:

    *   Dentro de Claude Code: ejecuta `/agents`
    *   Personaliza el acceso a herramientas, el prompt del sistema y el comportamiento.

---

### Reflexiones Finales

Actualizar Claude Code es sencillo—usa npm o el instalador nativo, verifica que estés en la última versión, y luego explora las nuevas funciones de **modos de aprendizaje** y **subagentes**. Estas adiciones cambian a Claude Code de ser solo un asistente de codificación hacia algo más parecido a un compañero de enseñanza y un colaborador agéntico en tu flujo de trabajo de desarrollo.

Si deseas ayuda para crear tu primer subagente o usar el modo de aprendizaje de manera efectiva, ¡estaré encantado de guiarte!

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "Don't forget to update your Claude CLI! It makes a huge ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Intelligent AI Solutions \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Quickstart - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Claude Code settings"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Claude Code overview"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic launches tool to connect AI systems directly to datasets"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Claude's new 'learning modes' take on ChatGPT's Study Mode - here's what they do"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Subagents"