---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de Copilot para Modelos Personalizados
translated: true
type: note
---

Cuando seleccionas "modelos gestionados" en GitHub Copilot y aún ves GPT-4.1 como predeterminado, o no puedes usar los modelos Grok o Kimi de OpenRouter como se esperaba, hay algunas razones potenciales y pasos para solucionarlo. Aquí tienes un desglose del problema y cómo configurar Copilot para usar los modelos Grok o Kimi a través de OpenRouter:

### Por qué se sigue usando GPT-4.1
1.  **Configuración del Modelo Predeterminado**: GitHub Copilot utiliza GPT-4.1 como predeterminado para Copilot Chat, Ediciones y Modo Agente a menos que se cambie explícitamente. Incluso cuando seleccionas "modelos gestionados", el modelo predeterminado puede persistir si no has configurado completamente la integración con OpenRouter o seleccionado un modelo específico.
2.  **Uso del Modelo Específico del Contexto**: La "caja de corrección" (chat en línea o finalización de código) en Copilot podría no admitir el cambio a modelos personalizados como Grok o Kimi en ciertos contextos. Por ejemplo, el panel de Copilot Chat o las sugerencias en línea podrían usar el modelo predeterminado (GPT-4.1) a menos que cambies explícitamente a un modelo personalizado en la vista inmersiva o en el Modo Agente.
3.  **Limitaciones de la Integración con OpenRouter**: OpenRouter permite el acceso a modelos como Grok (creado por xAI) y Kimi (de Moonshot AI), pero la integración de Copilot con OpenRouter requiere una configuración específica, y es posible que no todos los modelos estén disponibles inmediatamente debido a limitaciones de la API o problemas de configuración. Por ejemplo, la API de OpenRouter puede no anunciar soporte para herramientas en todos los modelos, lo que puede impedir que el Modo Agente o ciertas funciones funcionen con Grok o Kimi.
4.  **Restricciones de Suscripción o Configuración**: Si estás usando un plan gratuito o una suscripción a Copilot que no sea Pro/Business, es posible que estés limitado a modelos predeterminados como GPT-4.1. Además, algunos modelos (por ejemplo, Grok o Kimi) pueden requerir configuraciones específicas o acceso premium a través de OpenRouter.

### Cómo usar los modelos Grok o Kimi en Copilot a través de OpenRouter
Para usar los modelos Grok o Kimi de OpenRouter en Copilot, particularmente para la "caja de corrección" (chat en línea o finalización de código), sigue estos pasos:

1.  **Configurar OpenRouter con Copilot**:
    *   **Obtener una Clave API de OpenRouter**: Regístrate en [openrouter.ai](https://openrouter.ai) y obtén una clave API. Asegúrate de tener créditos o un plan que admita el acceso a los modelos Grok (xAI) y Kimi (Moonshot AI K2).
    *   **Configurar OpenRouter en VS Code**:
        *   Abre Visual Studio Code (VS Code) y asegúrate de tener instalada la última extensión de GitHub Copilot (v1.100.2 o posterior).
        *   Ve al panel de control de Copilot en la Barra de Estado, o abre la Paleta de Comandos (`Ctrl+Shift+P` o `Command+Shift+P` en Mac) y escribe `GitHub Copilot: Manage Models`.
        *   Añade tu clave API de OpenRouter y configura el endpoint para incluir los modelos de OpenRouter. Es posible que necesites seguir la documentación de OpenRouter para integrarlo con la extensión de Copilot de VS Code.
    *   **Verificar la Disponibilidad del Modelo**: Después de añadir el endpoint de OpenRouter, revisa la sección "Manage Models" en Copilot. Modelos como `openrouter/xai/grok` o `openrouter/moonshotai/kimi-k2` deberían aparecer en el selector de modelos. Si no es así, asegúrate de que tu cuenta de OpenRouter tenga acceso a estos modelos y de que no haya restricciones (por ejemplo, limitaciones del plan gratuito).

2.  **Cambiar de Modelo para la Caja de Corrección**:
    *   **Para Chat en Línea (Caja de Corrección)**: La "caja de corrección" probablemente se refiere a la función de chat en línea o finalización de código de Copilot. Para cambiar el modelo para el chat en línea:
        *   Abre la interfaz de Copilot Chat en VS Code (a través del icono en la barra de título o la barra lateral).
        *   En la vista de chat, selecciona el menú desplegable `CURRENT-MODEL` (normalmente en la parte inferior derecha) y elige `openrouter/xai/grok` o `openrouter/moonshotai/kimi-k2` si están disponibles.
        *   Si el menú desplegable no muestra Grok o Kimi, podría deberse a que la API de OpenRouter no anuncia soporte para herramientas para estos modelos, lo que puede limitar su uso en ciertas funciones de Copilot como el Modo Agente o las correcciones en línea.
    *   **Para Finalización de Código**: Para cambiar el modelo para las finalizaciones de código (no solo el chat):
        *   Abre la Paleta de Comandos (`Ctrl+Shift+P` o `Command+Shift+P`) y escribe `GitHub Copilot: Change Completions Model`.
        *   Selecciona el modelo de OpenRouter deseado (por ejemplo, Grok o Kimi) de la lista. Ten en cuenta que es posible que no todos los modelos de OpenRouter admitan la finalización de código debido a la limitación actual de VS Code de admitir solo endpoints de Ollama para modelos personalizados, aunque OpenRouter puede funcionar con una solución alternativa de proxy.

3.  **Solución Alternativa para Modelos OpenRouter**:
    *   **Solución con Proxy**: Dado que la API de OpenRouter no siempre anuncia soporte para herramientas (requerido para el Modo Agente o funciones avanzadas), puedes usar un proxy como `litellm` para habilitar Grok o Kimi en Copilot. Edita el archivo `config.yaml` para incluir:
        ```yaml
        model_list:
          - model_name: grok
            litellm_params:
              model: openrouter/xai/grok
          - model_name: kimi-k2
            litellm_params:
              model: openrouter/moonshotai/kimi-k2
        ```
        *   Sigue las instrucciones de configuración de fuentes como [Bas codes](https://bas.codes) o [DEV Community](https://dev.to) para obtener pasos detallados sobre cómo configurar el proxy.
    *   **Reiniciar VS Code**: Después de configurar el proxy, reinicia VS Code para asegurarte de que los nuevos modelos estén disponibles en el selector de modelos.

4.  **Verificar Suscripción y Permisos**:
    *   **Suscripción a Copilot**: Asegúrate de tener una suscripción Copilot Pro o Business, ya que los usuarios de planes gratuitos pueden no tener la opción de añadir modelos personalizados.
    *   **Restricciones Empresariales**: Si estás usando una suscripción Copilot Business, tu organización debe habilitar el cambio de modelo. Consulta con tu administrador o consulta la documentación de GitHub sobre la gestión de políticas de Copilot.
    *   **Créditos de OpenRouter**: Verifica que tu cuenta de OpenRouter tenga créditos suficientes para acceder a modelos premium como Grok o Kimi, ya que estos pueden consumir más créditos que otros.

5.  **Solución de Problemas de la Caja de Corrección**:
    *   Si la caja de corrección sigue usando GPT-4.1, podría deberse a que la función de chat en línea está bloqueada al modelo predeterminado en ciertos contextos (por ejemplo, en una vista no inmersiva). Intenta cambiar a la vista inmersiva de Copilot Chat (`https://github.com/copilot`) para seleccionar Grok o Kimi explícitamente.
    *   Si Grok o Kimi no aparecen en el selector de modelos, verifica nuevamente la integración de OpenRouter en `Manage Models`. Es posible que necesites actualizar la lista de modelos o volver a añadir la clave API de OpenRouter.
    *   Si el problema persiste, prueba los modelos en el Modo Agente o en la interfaz de chat de Copilot primero para confirmar que funcionan, y luego intenta aplicarlos a las correcciones en línea.

6.  **Herramientas Alternativas**:
    *   Si la integración de OpenRouter con Copilot sigue siendo problemática, considera usar Grok directamente a través de [grok.com](https://grok.com) o las aplicaciones iOS/Android de Grok, que ofrecen acceso gratuito con cuotas de uso. Los modelos Kimi también se pueden probar a través de la interfaz de chat de OpenRouter para asegurarse de que son accesibles.
    *   Para una experiencia más fluida, podrías explorar otros IDE o herramientas como Cursor, de los que se ha informado que funcionan bien con el modelo Kimi K2 de OpenRouter.

### Notas Adicionales
*   **Rendimiento del Modelo**: Grok está optimizado para el razonamiento y la búsqueda de la verdad, lo que lo hace adecuado para tareas complejas de depuración o arquitectura, mientras que Kimi (K2) puede sobresalir en escenarios de codificación específicos. Prueba ambos para ver cuál funciona mejor para tu caso de uso.
*   **Comentarios de la Comunidad**: Algunos usuarios informan de problemas con los modelos de OpenRouter que no aparecen en el selector de modelos de Copilot, especialmente con cuentas de plan gratuito. Esto podría requerir un plan de pago de OpenRouter o una suscripción Copilot Pro para resolverse.
*   **Limitaciones Continuas**: Existe una discusión abierta sobre habilitar endpoints API personalizados directamente en Copilot (ver [microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518)). Hasta que esto se implemente, la solución alternativa del proxy es el método más confiable para usar Grok o Kimi.

### Citas
*   [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
*   [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)
*   [Openrouter - openrouter.ai](https://openrouter.ai/models)
*   [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
*   [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
*   [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
*   [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
*   [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)

Si encuentras errores específicos o necesitas más ayuda con la configuración, ¡proporciona más detalles (por ejemplo, mensajes de error, versión de VS Code o tipo de suscripción) y puedo adaptar la solución aún más!