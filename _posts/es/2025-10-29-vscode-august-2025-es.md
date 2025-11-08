---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Actualización de Visual Studio Code de agosto de 2025
translated: true
type: note
---

### Visual Studio Code 1.104 (Agosto de 2025)

Esta versión se centra en gran medida en las mejoras de IA para GitHub Copilot, una seguridad mejorada para las herramientas de IA y mejoras de productividad en el editor y la terminal. Aquí tienes un desglose de las actualizaciones clave:

#### Funciones de IA
- **Selección Automática de Modelo (Vista previa)**: El chat ahora selecciona automáticamente el mejor modelo (por ejemplo, Claude Sonnet 4, variantes de GPT-5) basándose en el rendimiento y los límites de tasa cuando se selecciona "Auto"; incluye un descuento del 10% en las solicitudes para usuarios de pago.
- **Confirmar Ediciones en Archivos Sensibles**: El modo Agente requiere la aprobación del usuario antes de editar archivos del sistema, dotfiles, o cualquier cosa fuera del área de trabajo; personalizable mediante ajustes.
- **Soporte para Archivos AGENTS.md (Experimental)**: Incorpora automáticamente el `AGENTS.md` del área de trabajo como contexto para las solicitudes de chat.
- **Colaboración Mejorada de Agentes de Codificación (Experimental)**: Mejor gestión de sesiones, integración con GitHub y delegación desde comentarios TODO o chat.
- **Aprobación Automática en Terminal**: Opt-in para una ejecución de comandos más segura con advertencias para acciones riesgosas como `curl` o `wget`; nuevas reglas para aprobaciones.
- **Renderizado de Matemáticas**: Las ecuaciones KaTeX ahora se renderizan en línea por defecto en las respuestas del chat.
- **Herramienta #codebase Mejorada**: Utiliza un nuevo modelo de embeddings para una búsqueda semántica de código más rápida y eficiente.
- **Desactivar Funciones de IA**: Nueva configuración para ocultar y desactivar el chat de Copilot, las finalizaciones y las sugerencias de forma global o por área de trabajo.
- **Herramientas de IA Específicas para Python (Experimental/Vista previa)**: Resúmenes con tecnología de IA en hover para símbolos no documentados y una herramienta "Ejecutar Fragmento de Código" para la ejecución en memoria.

#### Seguridad
- **Salvaguardas para Herramientas de IA**: Confirmaciones ampliadas para ediciones sensibles, comandos de terminal y autoaprobaciones globales, con advertencias y reglas configurables para mitigar riesgos.
- **Documentación**: Nueva guía sobre consideraciones de seguridad para el desarrollo potenciado por IA.

#### Productividad
- **Valores Predeterminados de la Vista de Chat**: El chat ahora se abre por defecto en la Barra Lateral Secundaria; visibilidad personalizable.
- **Mejoras en la Terminal**: Mejor IntelliSense (por ejemplo, finalizaciones de git, iconos), desplazamiento fijo y acciones en editores/ventanas de terminal.
- **Entornos Python**: Soporte mejorado para Pipenv, inyección de variables de entorno desde archivos `.env` e IntelliSense completo en todos los documentos Python.
- **Ajustes del Editor**: Retardo configurable de sugerencias en línea, índice de pestañas para navegación por teclado y colores del borde de la ventana en Windows.
- **Solicitudes de Extracción de GitHub**: Barra lateral colapsable, acciones TODO para Copilot y opciones para ignorar submódulos.
- **Soporte para Tareas y Terminal**: Manejo de entrada mejorado, visualización de errores y tiempos de espera para la integración del shell.

#### Otros Cambios Notables
- **Accesibilidad**: Comando de enfoque para confirmaciones en el chat para ayudar a los lectores de pantalla.
- **Lenguajes**: Se eliminó el IntelliSense integrado para Bower.json (herramienta obsoleta; migrar a npm/yarn).
- **Creación de Extensiones**: APIs propuestas para desafíos de autenticación y contribuciones a la barra lateral secundaria.
- **Desuso**: Ajustes como `chat.mcp.enabled` migrados; se eliminó el soporte para Bower.

Para más detalles, consulta las notas de la versión oficial.

[Agosto de 2025 (versión 1.104)](https://code.visualstudio.com/updates/v1_104)