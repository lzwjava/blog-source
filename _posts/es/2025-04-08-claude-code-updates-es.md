---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Actualizaciones Importantes de Claude Code
translated: true
type: note
---

### Actualizaciones Importantes en Claude Code

Claude Code, el asistente de codificación con IA de Anthropic, ha experimentado mejoras significativas recientemente, particularmente en torno a la autonomía, la integración y las características de la interfaz de usuario. Según las últimas noticias (29 de septiembre de 2025), la actualización clave se centra en permitir una operación más autónoma, incluyendo una extensión nativa de VS Code, una interfaz de terminal mejorada (versión 2.0) y una nueva funcionalidad de checkpoint para gestionar tareas de larga duración. Además, características como alternar el modo "thinking" parecen ser parte de los refinamientos en curso, permitiendo a los usuarios activar y desactivar la visualización de los pasos de razonamiento de Claude para interacciones más limpias [1].

#### Autonomía y Capacidades de Agente
- **Extensión Nativa de VS Code**: Permite una integración perfecta con el editor VS Code, permitiendo que Claude Code opere directamente dentro del entorno de desarrollo para una edición y depuración de código más autónoma.
- **Interfaz de Terminal v2.0**: Las mejoras incluyen un manejo mejorado de permisos, gestión de memoria entre tareas y coordinación de subagentes. Esto hace que Claude Code sea mejor equilibrando el control del usuario con las operaciones automatizadas durante flujos de trabajo complejos [1][2].
- **Checkpoints**: Una nueva característica para guardar el progreso en tareas largas, permitiendo pausas y reanudaciones sin perder el contexto. Esto permite ejecutar tareas que abarcan múltiples días o sesiones.

Estos cambios se basan en el Claude Agent SDK de Anthropic, proporcionando a los desarrolladores herramientas para crear agentes de IA personalizados que reflejan la infraestructura interna de Claude Code [2].

#### Otros Cambios Notables
- **Integración de Actualización del Modelo**: Claude Code ahora utiliza Claude Sonnet 4.5 por defecto, ofreciendo un rendimiento mejorado en tareas de codificación sin cambios de precio. Este modelo es recomendado en todos los productos Claude por su mejor alineación y reducción de alucinaciones [2].
- **Ajustes en la Interfaz de Usuario**: La característica "Thinking off (tab to toggle)" parece ser un interruptor para mostrar u ocultar el proceso de razonamiento interno de Claude, lo que puede agilizar la salida. Esto se alinea con los comentarios de los usuarios sobre la transparencia y la usabilidad en las sesiones de codificación [3].
- **Intentos de Corrección de Problemas Conocidos**: Se están abordando los informes de que Claude Code añade "2024" a las búsquedas debido a los límites de los datos de entrenamiento, aunque algunos usuarios notan errores persistentes. Una solución alternativa implica el uso de hooks personalizados para actualizar la conciencia de la fecha [3][4].

Para todos los detalles, instale o verifique la última versión: las actualizaciones se aplican automáticamente para todos los usuarios [1]. Si experimenta problemas, asegúrese de que su cliente esté actualizado. Para cambios históricos, consulte registros de cambios comunitarios como ClaudeLog, aunque pueden no cubrir las funciones más recientes [5].

Citas:
[1] https://anthropic.com/news/enabling-claude-code-to-work-more-autonomously
[2] https://www.anthropic.com/news/claude-sonnet-4-5
[3] https://www.reddit.com/r/ClaudeAI/comments/1mtgjdi/claude_code_thinks_it_is_2024_and_keeps_web/
[4] https://medium.com/@dan.avila7/fixed-claude-codes-2024-tunnel-vision-with-a-simple-hook-cb32cfaf9b27
[5] https://www.claudelog.com/claude-code-changelog/