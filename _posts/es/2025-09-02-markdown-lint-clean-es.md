---
audio: false
generated: true
image: false
lang: es
layout: post
title: Limpieza de Markdown para Archivos Consistentes y Ordenados
translated: true
type: note
---

Aquí tienes una introducción clara y fácil de leer al proyecto **markdownlint** de David Anson:

---

## ¿Qué es **markdownlint**?

**markdownlint** es una herramienta de análisis estático para archivos Markdown/CommonMark, construida sobre Node.js. Su propósito principal es hacer cumplir reglas de consistencia y estilo en el contenido Markdown, ayudando a los escritores a mantener un formato limpio y uniforme, y a evitar construcciones que podrían romperse o renderizarse de manera inconsistente en diferentes analizadores sintácticos ([GitHub][1]).

Inspirado en markdownlint basado en Ruby (markdownlint/mdl), esta herramienta adopta una amplia biblioteca de reglas de linting. Utiliza el analizador sintáctico micromark para soportar CommonMark y lo extiende con características de GitHub Flavored Markdown (GFM) como tablas, enlaces automáticos, directivas, notas al pie y matemáticas ([GitHub][1]).

## Características Principales e Integraciones

* **Cobertura de Reglas**: Ofrece un conjunto completo de reglas integradas, que van desde estilos de encabezados e indentación de listas hasta espacios finales y longitud de línea (por ejemplo, MD001, MD009, MD013…) ([GitHub][1]).
* **Compatibilidad con el Ecosistema**:

  * **Herramientas de Línea de Comandos**:

    * `markdownlint-cli` – una interfaz de CLI tradicional.
    * `markdownlint-cli2` – una CLI más rápida, basada en configuración, con opciones de formato flexibles y soporte para globs, formatos de salida, autocorrección e integración con flujos de trabajo de CI ([GitHub][2], [GitHub][3]).
  * **Extensión para VS Code**:

    * `vscode‑markdownlint` lleva el linting en tiempo real a tu editor. Las violaciones se marcan en línea (subrayadas), con información contextual al pasar el cursor y sugerencias de corrección rápida ([GitHub][4]).
  * **Acción de GitHub**:

    * `markdownlint‑cli2‑action` te permite integrar markdownlint en tu pipeline de CI, permitiendo verificaciones automáticas (y autocorrección opcional) durante los flujos de trabajo de GitHub ([GitHub][5]).

---

## ¿Por qué usarlo?

* **Consistencia**: Garantiza que los archivos Markdown se adhieran a una guía de estilo definida, reduciendo la deriva de formato en un proyecto.
* **Asistencia en el Editor**: La retroalimentación en línea en VS Code y otras integraciones hacen que escribir sea más limpio y rápido.
* **Automatización**: Úsalo en pipelines de CI con herramientas de linting o GitHub Actions para hacer cumplir los estándares antes de las fusiones.
* **Personalizable**: Puedes personalizar los conjuntos de reglas o incluso desactivar reglas mediante archivos de configuración o comentarios en línea (por ejemplo, desactivar MD013 para líneas largas) ([GitHub][5], [Software Recommendations Stack Exchange][6]).

---

¿Te gustaría una guía de inicio rápido para configurarlo con npm, usar la extensión de VS Code o integrarlo en flujos de trabajo de CI?

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"