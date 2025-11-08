---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Resumen de Actualizaciones de la Extensión GitHub Copilot
translated: true
type: note
---

### Extensión GitHub Copilot para VS Code (Versión 1.388.0)

La versión 1.388.0 de la extensión GitHub Copilot se lanzó el 24 de octubre de 2025. Esta parece ser una actualización menor centrada en mejoras de estabilidad y compatibilidad, particularmente con la última versión de VS Code (1.105). Las notas de la versión específicas no se detallan públicamente en el marketplace o en el blog de GitHub, pero los informes de los usuarios indican correcciones para problemas como inserciones de código no deseadas durante la generación en línea y finalizaciones de etiquetas adicionales al abortar sugerencias. Se integra perfectamente con las funciones recientes de Copilot, incluidos los modos de agente mejorados y las selecciones de modelos.

#### Actualizaciones Clave en los Últimos 6 Meses (Mayo–Octubre 2025)
Las principales mejoras de GitHub Copilot generalmente se anuncian junto con los lanzamientos mensuales de VS Code. Aquí hay un resumen de las actualizaciones significativas para la extensión y las funciones relacionadas durante este período:

- **Octubre 2025 (VS Code 1.105 / Extensión ~1.388)**:
  - Integración de OpenAI Codex ahora disponible en VS Code Insiders para suscriptores de Copilot Pro+, permitiendo síntesis de código avanzada directamente en el editor.
  - Nueva interfaz de "control de misión" para asignar, dirigir y rastrear tareas del agente de codificación de Copilot entre sesiones.
  - La vista Sesiones de Agente se expandió para admitir la CLI de GitHub Copilot para gestionar agentes locales y basados en la nube.

- **Septiembre 2025 (VS Code 1.104 / Extensión ~1.38x)**:
  - Implementación del modelo experimental GitHub Copilot-SWE para VS Code Insiders, optimizado para edición de código, refactorización y pequeñas transformaciones. Está centrado en tareas y funciona en cualquier modo Chat; se recomiendan instrucciones detalladas para obtener los mejores resultados.
  - Chat en línea mejorado para errores de terminal, con mejores explicaciones y correcciones.

- **Agosto 2025 (VS Code 1.103 / Extensión ~1.37x)**:
  - Sugerencias de mensajes de commit mejoradas con conciencia del contexto multilínea e integración con @workspace para generar estructuras de proyecto completas.
  - Mejoras en el chat en línea ligero para interacciones más rápidas sin abrir vistas completas.

- **Julio 2025 (VS Code 1.102 / Extensión ~1.36x)**:
  - Mejor coordinación de ediciones multiarchivo mediante instrucciones únicas, analizando la estructura del proyecto para cambios consistentes.
  - Modelos más antiguos obsoletos (variantes seleccionadas de Claude, OpenAI y Gemini) en favor de opciones más nuevas y rápidas como GPT-4.1.

- **Junio 2025 (VS Code 1.101 / Extensión ~1.35x)**:
  - Introducción de archivos de instrucciones y prompts para personalizar el comportamiento de Copilot con pautas reutilizables y conocimiento organizacional.
  - Integración expandida de GitHub Pull Requests: Asigna PRs/issues a Copilot directamente desde las vistas de VS Code, con nueva consulta "Copilot on My Behalf" para seguimiento.

- **Mayo 2025 (VS Code 1.100 / Extensión ~1.34x)**:
  - Soporte del Model Context Protocol (MCP) añadido al modo agente, permitiendo claves API personalizadas para modelos de terceros.
  - Ediciones de agente más rápidas impulsadas por OpenAI GPT-4.1 y Anthropic Claude Sonnet, especialmente para archivos grandes.
  - Mejoras en la búsqueda de repositorios para descubrimiento semántico de código y sugerencias en toda la base de código.

Estas actualizaciones enfatizan los flujos de trabajo de agentes, el rendimiento del modelo y la integración perfecta con el ecosistema de VS Code. Para la historia completa de la extensión, consulta el VS Code Marketplace. Los anuncios importantes a menudo se vinculan con los ciclos mensuales de VS Code.

[GitHub Copilot in VS Code gets upgraded](https://github.blog/changelog/2025-10-28-github-copilot-in-visual-studio-code-gets-upgraded/)  
[Copilot-SWE model rolling out to Visual Studio Code Insiders](https://github.blog/changelog/2025-09-22-copilot-swe-model-rolling-out-to-visual-studio-code-insiders/)  
[GitHub Copilot in VS Code April release (v1.100)](https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/)  
[GitHub Copilot in VS Code March release (v1.99)](https://github.blog/changelog/2025-04-03-github-copilot-in-vs-code-march-release-v1-99/)  
[September 2025 (version 1.105) - Visual Studio Code](https://code.visualstudio.com/updates)  
[GitHub Copilot Marketplace Page](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)