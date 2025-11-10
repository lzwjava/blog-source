---
audio: false
generated: true
lang: es
layout: post
title: Herramientas de edición de código con IA
translated: true
type: note
---

### Visual Studio Code (VS Code) con GitHub Copilot
VS Code, potenciado por GitHub Copilot (una extensión de IA), permite seleccionar código (como una función) y usar IA para corregirlo, editarlo o refactorizarlo. Las características clave incluyen:
- **Chat en línea**: Selecciona el código, presiona `Ctrl+I` (Windows/Linux) o `Cmd+I` (Mac) e ingresa un comando como "arregla este error" o "refactoriza para usar async/await". Copilot sugiere ediciones directamente en el editor.
- **Corregir errores**: Para errores del compilador (subrayados rojos), coloca el cursor sobre él y selecciona "Corregir usando Copilot" para obtener soluciones generadas por IA.
- **Vista de Chat**: Abre el Chat de Copilot (`Ctrl+Alt+I`), selecciona código y pide que lo explique, edite o genere pruebas. Puede manejar ediciones multiarchivo en modo agente.
- **Menú de Acciones**: Haz clic derecho en el código seleccionado para acceder a acciones de IA como explicar, renombrar o revisar.

Copilot es gratuito con límites o de pago para uso ilimitado.

### Editor de Código Cursor AI
Cursor es un editor de código centrado en la IA, bifurcado desde VS Code, diseñado específicamente para la edición asistida por IA. Se destaca en la selección y modificación de código con IA:
- **Editar con Ctrl+K**: Selecciona una función o bloque de código, presiona `Ctrl+K` (o `Cmd+K` en Mac) y describe los cambios (ej. "optimiza esta función para rendimiento"). Cursor genera diferencias (diffs) que puedes previsualizar y aplicar.
- **Modo Compositor**: Para ediciones complejas en múltiples archivos, usa la interfaz del Compositor para solicitar cambios multiarchivo, revisar diferencias e iterar.
- **Modo Agente**: Presiona `Ctrl+I`, instruye tareas más amplias (ej. "corrige los errores en este módulo") y este planifica, edita y ejecuta comandos de forma autónoma manteniéndote informado.
- **Sugerencias para la Siguiente Edición**: La IA predice y sugiere ediciones de seguimiento basadas en tus cambios.

Cursor es gratuito para funciones básicas, con un plan Pro para modelos avanzados. Importa extensiones de VS Code sin problemas.

### IntelliJ IDEA con JetBrains AI Assistant
IntelliJ IDEA (y otros IDEs de JetBrains) tiene un plugin integrado de AI Assistant que permite seleccionar código y usar IA para correcciones o ediciones:
- **Menú de Acciones de IA**: Selecciona código, presiona `Alt+Enter` o haz clic derecho, elige "AI Actions" > opciones como "Suggest Refactoring," "Find Problems," o "Fix with AI." Analiza el contexto y sugiere cambios en un visor de diferencias (diff).
- **Comando en línea**: Escribe un comando directamente en el editor (ej. "refactoriza esta función"), presiona `Tab`, y la IA genera/edita código en línea.
- **Corrección de Errores**: Para errores resaltados, selecciona "Fix with AI" para obtener sugerencias conscientes del contexto.
- **Generación/Refactorización de Código**: Invócalo mediante el menú para explicar código, añadir anotaciones de tipo o regenerar secciones.

AI Assistant requiere una licencia de JetBrains AI (prueba gratuita disponible) y está potenciado por modelos como Mellum para completados.

Todas estas herramientas integran la IA profundamente, pero Cursor es la más centrada en IA, VS Code/Copilot es flexible y ampliamente usado, y la IA de IntelliJ está adaptada para flujos de trabajo empresariales o con mucho código Java. Elige según tu ecosistema preferido.

Referencias:  
[GitHub Copilot en VS Code](https://code.visualstudio.com/docs/copilot/overview)  
[Empezar con GitHub Copilot en VS Code](https://code.visualstudio.com/docs/copilot/getting-started)  
[Características | Cursor - El Editor de Código con IA](https://cursor.com/en/features)  
[Cursor AI: Una Guía Con 10 Ejemplos Prácticos](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Usar IA en el editor | Documentación de IntelliJ IDEA](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)  
[AI Assistant en IDEs de JetBrains | Documentación de IntelliJ IDEA](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html)  
[Usar comandos de IA para explicar y refactorizar tu código | Documentación de IntelliJ IDEA](https://www.jetbrains.com/help/idea/use-prompts-to-explain-and-refactor-your-code.html)