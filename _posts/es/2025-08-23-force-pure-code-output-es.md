---
audio: false
generated: true
image: false
lang: es
layout: post
title: Métodos de Código de Salida Pura de Fuerza
translated: true
type: note
---

Entendido—quieres que Claude Code (y tus flujos de trabajo del "router" que lo llaman) genere **solo código**, **sin comentarios en línea, docstrings ni explicaciones**. Aquí tienes tres formas confiables de aplicar esto, de más suave a más fuerte. Sin tablas—solo pasos directos.

---

# 1) Pon la regla en `CLAUDE.md` (global o por proyecto)

Claude Code carga archivos de "memoria" automáticamente y los sigue entre sesiones. Añade una regla corta y explícita:

**Global (todos los proyectos):** `~/.claude/CLAUDE.md`
**Por proyecto (incluido en el control de versiones):** `./CLAUDE.md`

```md
# Reglas de salida
- Al generar código, emite solo código.
- No incluyas comentarios en línea, comentarios de bloque, docstrings o texto explicativo a menos que lo pida explícitamente.
- Mantén los mensajes concisos; si se necesita una explicación, ponla después del bloque de código y solo si lo pido.
```

Consejo: puedes gestionar estas memorias con `/memory` y añadir nuevas rápidamente comenzando un mensaje con `#` en Claude Code. ([Anthropic][1])

---

# 2) Crea un **Estilo de Salida personalizado** que prohíba los comentarios (más fuerte)

Los Estilos de Salida modifican el **prompt del sistema** de Claude Code. Crea uno y cámbiate a él:

**Crear:**

```
/output-style:new Quiero un estilo de salida que siempre genere código sin ningún comentario o docstring, sin explicaciones.
```

Esto crea un archivo bajo `~/.claude/output-styles/…`. Puedes editarlo para asegurarte de que la regla sea inequívoca:

```md
---
name: Solo Código (Sin Comentarios)
description: Siempre emite código sin comentarios/docstrings; sin explicaciones a menos que se pidan.
---
# Instrucciones
- Estás codificando en modo "solo-código".
- Nunca incluyas comentarios en línea, comentarios de bloque o docstrings.
- No añadas texto antes o después del código a menos que se solicite explícitamente.

## Comportamientos Específicos
- Si una tarea implica tests, genera el/los archivo(s) de test solo como código.
- Si se necesita aclaración, pregunta brevemente, sin explicaciones.
```

**Activar:**

```
/output-style "Solo Código (Sin Comentarios)"
```

(Los estilos de salida cambian directamente el prompt del sistema; puedes cambiarlos con `/output-style` en cualquier momento.) ([Anthropic][2])

---

# 3) Añade un prompt del sistema extra en tiempo de ejecución (más fuerte / por sesión)

Si lanzas Claude Code desde CLI o un script, añade:

```bash
claude --append-system-prompt "Siempre genera solo código. Sin comentarios en línea, sin comentarios de bloque, sin docstrings, sin explicaciones a menos que se pidan explícitamente."
```

También puedes configurar esto mediante `/config` si prefieres ajustes de proyecto persistentes. (Anthropic señala que puedes usar `--append-system-prompt` para modificar el comportamiento de Claude Code.) ([Anthropic][3])

---

## Dónde poner reglas para todo el "router"

* Si tu "router de Claude Code" son solo tus sesiones regulares de Claude Code en distintos repositorios, prefiere la **memoria global** (`~/.claude/CLAUDE.md`) o un **Estilo de Salida personalizado** para que la regla se aplique en todas partes. ([Anthropic][1])
* Si lanzas mediante un script, incluye la bandera `--append-system-prompt` para que cada ejecución herede la regla. ([Anthropic][3])

---

## Barreras de protección extra (opcionales pero útiles)

* En la memoria del proyecto, añade una línea de **"Violaciones"** para que el modelo se auto-compruebe: "Si estás a punto de generar comentarios/docstrings, detente y elimínalos."
* Si a veces *quieres* comentarios, añade una anulación de una vez en tu prompt: "Solo esta vez, incluye comentarios breves."

Eso es todo. Si me dices cómo inicias Claude Code (escritorio, VS Code, JetBrains, o terminal), puedo darte un fragmento de código listo para usar para esa configuración.

[1]: https://docs.anthropic.com/en/docs/claude-code/memory "Manage Claude's memory - Anthropic"
[2]: https://docs.anthropic.com/en/docs/claude-code/output-styles "Output styles - Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/settings "Claude Code settings - Anthropic"