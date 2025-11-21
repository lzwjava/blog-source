---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Características y Actualizaciones de Cursor 2025
translated: true
type: note
---

### Resumen de las nuevas funciones de Cursor

Cursor, el editor de código potenciado por IA construido sobre VS Code, ha experimentado una rápida evolución en 2025, con un enfoque principal en los flujos de trabajo agentes, la compatibilidad con múltiples modelos y las integraciones perfectas. La actualización más importante es **Cursor 2.0** (lanzado el 29 de octubre de 2025), que presenta Composer—un modelo de codificación propio—y una interfaz rediseñada para gestionar múltiples agentes de IA en paralelo. Esto cambia el editor de la codificación tradicional a la orquestación de tareas impulsadas por IA, como construir funciones de forma autónoma o depurar en diferentes bases de código. A continuación, desglosaré las nuevas funciones clave, agrupadas por lanzamiento y categoría, basándome en anuncios oficiales e informes de usuarios hasta el 21 de noviembre de 2025.

### Lanzamientos principales y funciones nuevas clave

#### Cursor 2.0 (29 de octubre de 2025) – Revisión centrada en agentes
Esta versión reinventa Cursor como un "gestor de flotas de agentes", enfatizando la delegación sobre la codificación manual. Adiciones clave:
- **Modelo Composer**: El primer modelo de codificación interno de Cursor, optimizado para velocidad y grandes bases de código. Utiliza búsqueda semántica para ediciones conscientes del contexto, permitiendo la generación/modificación de código con lenguaje natural. Es un 21% más selectivo en las sugerencias pero tiene una tasa de aceptación un 28% mayor que los modelos anteriores.
- **Interfaz Multi-Agente**: Ejecuta hasta 8 agentes simultáneamente en la misma tarea (por ejemplo, uno para planificar, otro para probar). Incluye una barra lateral de "bandeja de entrada" para monitorear el progreso, revisar diferencias (diffs) como pull requests y generar agentes con diferentes modelos (por ejemplo, Claude Sonnet 4.5 vs. GPT-5.1).
- **Controles de Navegador Integrados**: Los agentes ahora pueden controlar una instancia de Chrome integrada—tomando capturas de pantalla, depurando problemas de UI o probando de extremo a extremo. Esto está disponible generalmente (GA) después de la beta, con soporte empresarial para un uso seguro.
- **Modo Plan (Mejorado)**: Los agentes auto-generan planes editables para tareas, con herramientas para investigación de la base de código y ejecuciones de larga duración. Presiona Shift + Tab para comenzar; incluye preguntas aclaratorias para mejores resultados.
- **Modo Voz**: Dicta prompts por voz a texto; palabras clave de envío personalizadas activan las ejecuciones de los agentes. Soporta elicitación MCP para entradas de usuario estructuradas (por ejemplo, esquemas JSON para preferencias).
- **Revisión de Código Automática**: Revisiones de diferencias (diffs) integradas para cada cambio generado por IA, detectando errores antes de la fusión (merge).
- **Agentes en la Nube**: Ejecuta agentes de forma remota (inicio más rápido, fiabilidad mejorada) sin ocupar tu máquina local. Gestiona flotas en el editor, ideal para trabajo sin conexión.

#### Actualización 1.7 (29 de septiembre de 2025) – Impulsores de flujo de trabajo
- **Comandos de Barra (Slash Commands)**: Acciones rápidas como `/summarize` para compresión de contexto bajo demanda (libera límites de tokens sin nuevos chats).
- **Hooks Personalizados**: Automatiza comportamientos de agentes, por ejemplo, scripts pre/post-tarea para linting o testing.
- **Reglas para Todo el Equipo**: Comparte reglas de la base de código (por ejemplo, Bugbot para revisiones automatizadas) entre equipos a través de archivos `.cursorrules`.
- **Soporte para Barra de Menús y Enlaces Profundos**: Navegación más fácil e integraciones externas.

#### Aspectos destacados anteriores de 2025 (Mayo–Agosto)
- **Agentes en Segundo Plano (0.50, 15 de mayo)**: Ejecución de tareas en paralelo (por ejemplo, un agente refactoriza mientras otro prueba). Vista previa en macOS/Linux.
- **Modelo de Pestañas Mejorado (Múltiples Actualizaciones)**: Ediciones multiarchivo, ventanas de contexto de más de 1 millón de tokens, y entrenamiento online RL para autocompletados más inteligentes y rápidos (por ejemplo, React hooks, consultas SQL).
- **@carpetas y Ediciones en Línea**: Hacer referencia a directorios completos en los prompts; CMD+K actualizado para cambios de archivo completo con búsqueda/reemplazo preciso.
- **Modo YOLO (Mejoras del Agente)**: Comandos autónomos de terminal, corrección de linting y auto-depuración hasta la resolución.

### Integraciones de Modelos
Cursor ahora admite modelos de vanguardia para diversas tareas:
- **OpenAI (13 de noviembre de 2025)**: GPT-5.1 (planificación/depuración), GPT-5.1 Codex (codificación ambiciosa), GPT-5.1 Codex Mini (ediciones eficientes).
- **Anthropic**: Sonnet 4 (22 de mayo de 2025) y Sonnet-3.7 (24 de febrero de 2025) para una comprensión superior de la base de código.
- **Google**: Gemini 2.5 Pro (10 de junio de 2025) para un crecimiento rápido en integraciones.
- **Otros**: o3/o4-mini (17 de abril de 2025) para codificación mejorada.

| Categoría | Función Nueva Clave | Beneficio | Lanzamiento |
|----------|------------------|---------|---------|
| **Agentes** | Paralelismo Multi-Agente | Delega tareas a 2–8 agentes; compara resultados | 2.0 (Oct) |
| **Modelos** | Composer + Suite GPT-5.1 | Generación más rápida y consciente del contexto | 2.0/Nov |
| **UI/Flujo de trabajo** | Modo Plan + Navegador Integrado | Planificación automática + pruebas de extremo a extremo | 2.0/Sep |
| **Ediciones** | Pestaña Multiarchivo + Actualización en Línea | Refactorizaciones más inteligentes; precisión de archivo completo | Mayo–Oct |
| **Colaboración** | Reglas de Equipo + Agentes en la Nube | Directrices compartidas; ejecución remota | Sep/Oct |

### Actualizaciones de Precios y Accesibilidad
- **Niveles Simplificados (16 de junio de 2025)**: Pro (línea base de computación de $20/mes, llamadas a herramientas ilimitadas); nuevo Ultra ($200/mes, 20x de uso) para usuarios avanzados.
- **Modo Máx.**: Acceso basado en tokens a las capacidades completas del modelo (por ejemplo, contextos largos) en todos los modelos principales.

Estas funciones hacen de Cursor una opción ideal para el desarrollo impulsado por agentes, reduciendo el trabajo manual hasta en un 39% en fusiones de PR (según un estudio de la Universidad de Chicago). Para el registro de cambios completo, consulta el [sitio oficial de Cursor](https://cursor.com/changelog). Si estás en VS Code, la migración es perfecta—descarga y experimenta con la vista de agentes de la versión 2.0 para una victoria rápida.