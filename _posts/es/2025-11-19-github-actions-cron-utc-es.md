---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Programación Cron de GitHub Actions Usa Hora UTC
translated: true
type: note
---

**Los flujos de trabajo programados de GitHub Actions (que utilizan el activador `on: schedule:` con sintaxis cron) siempre interpretan los tiempos cron en UTC (Tiempo Universal Coordinado).**

No existe soporte incorporado para especificar una zona horaria diferente directamente en el YAML del flujo de trabajo. Si deseas que un trabajo se ejecute a una hora local específica (por ejemplo, 9:00 AM PST), debes convertirla a la hora UTC equivalente y escribir la expresión cron en consecuencia.

### Puntos clave de la documentación oficial:
- Los flujos de trabajo programados utilizan la sintaxis cron de POSIX y se ejecutan a **horas UTC** específicas.
- Ejemplo: `cron: '0 5 * * *'` se ejecuta diariamente a las 5:00 AM UTC (no a tu hora local).

Esto ha sido consistente durante años y sigue siendo el caso hasta finales de 2025: no existe un parámetro de zona horaria nativo para el evento `schedule` (a diferencia de otras funciones de GitHub como Dependabot).

[Eventos que activan flujos de trabajo - GitHub Docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[Sintaxis de flujo de trabajo para GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)