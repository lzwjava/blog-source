---
audio: false
generated: true
lang: es
layout: post
title: Actualización de la CLI de Código Claude
translated: true
type: note
---

¡Hola! Parece que estás trabajando con la herramienta Claude Code CLI de Anthropic. Según la salida que pegaste, parece que ya intentó una actualización automática a la versión 1.0.61, pero si eso no funciona o necesitas actualizar manualmente, aquí te explicamos cómo:

Para actualizar Claude Code CLI:
- Abre tu terminal.
- Ejecuta el comando: `claude update`
Este comando integrado debería buscar e instalar la última versión.

Si la actualización falla (por ejemplo, debido a problemas de permisos o de red), puedes intentar reinstalarlo mediante npm (asumiendo que tienes Node.js y npm instalados):
- Ejecuta: `npm install -g @anthropic-ai/claude-code`

Después de actualizar, es posible que necesites iniciar sesión nuevamente ejecutando `claude /login` (o a veces `claude login`, dependiendo de la versión). Si aún ves errores, verifica tu conexión a internet, asegúrate de que tu clave API sea válida o consulta la documentación oficial de solución de problemas.

Para más detalles sobre los comandos, puedes ejecutar `claude --help` como hiciste, lo que debería mostrar las opciones en la versión actualizada.

[Referencia de CLI - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[Cómo configurar y usar la herramienta Claude CLI como un profesional](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Resumen de Claude Code - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)