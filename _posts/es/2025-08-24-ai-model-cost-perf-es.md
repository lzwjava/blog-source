---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Costos y Rendimiento de Modelos de IA
translated: true
type: note
---

Aquí tienes un desglose más claro de las **puntuaciones de referencia** y los **precios de la API** para cada modelo: Claude 4 Opus (también indicado como Claude Opus 4), GPT‑5 (estándar/completo), GPT‑5 Mini, GPT‑5 Nano, además de o3 (OpenAI) y Claude 4 Sonnet—sin usar tablas, para mantenerlo ordenado y legible.

---

## Rendimiento en Referencia (SWE-bench)

Esto refleja qué tan bien se desempeñan los modelos en tareas de ingeniería de software:

* **Claude 4 Opus (14 de mayo de 2025)**: 67.60
* **GPT‑5 (7 de agosto de 2025, razonamiento medio)**: 65.00
* **Claude 4 Sonnet (14 de mayo de 2025)**: 64.93 ([SWE-bench][1])

**Conclusión**: Claude 4 Opus lidera ligeramente en el rendimiento de SWE-bench, seguido de cerca por GPT-5 y Claude Sonnet.

---

## Precios de la API (por millón de tokens)

### **Claude 4 Opus**

* Entrada: **\$15**
* Salida: **\$75** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (estándar/completo)**

* Entrada: **\$1.25**
* Entrada en caché (cuando se reutiliza): **\$0.125**
* Salida: **\$10** ([OpenAI][5])

### **GPT-5 Mini**

* Entrada: **\$0.25**
* Salida: **\$2** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

* Entrada: **\$0.05**
* Salida: **\$0.40** ([OpenAI][5], [WIRED][6])

### **o3-mini** (para contexto)

* Precios disponibles a través de la referencia o4‑mini:
* Entrada: **\$1.10**, Salida: **\$4.40** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

* Entrada: **\$3**, Salida: **\$15** ([LaoZhang AI][3])

---

## Aspectos Destacados de la Comparación Rápida

* **Mejor rendimiento**: Claude 4 Opus supera ligeramente a GPT-5 y Claude Sonnet en los benchmarks de codificación.
* **Costo más bajo por token**:

  * **GPT-5 Nano** es, con diferencia, el más económico, perfecto para tareas ligeras como la resumen.
  * **GPT-5 Mini** ofrece un equilibrio entre velocidad y asequibilidad.
  * **GPT-5 estándar** sigue siendo muy rentable, especialmente con cachés baratos.
* **Los modelos Claude**, tanto Opus como Sonnet, son significativamente más caros por token, pero justifican su precio mediante capacidades de razonamiento y agente más sólidas.

---

## Resumen (claro y conciso):

* **Claude 4 Opus**: Máximo rendimiento, alto costo (\$15 entrada / \$75 salida).
* **GPT-5 (completo)**: Gran rendimiento (justo por detrás de Opus), mucho más barato (\$1.25 entrada / \$10 salida).
* **GPT-5 Mini**: Opción de presupuesto medio (\$0.25 entrada / \$2 salida).
* **GPT-5 Nano**: Ideal para tareas ligeras o uso a gran escala de bajo costo (\$0.05 entrada / \$0.40 salida).
* **Claude 4 Sonnet**: Costo/rendimiento intermedio (\$3 entrada / \$15 salida), pero ligeramente por debajo de los demás en el benchmark.

---

¡Avísame si necesitas ayuda para estimar el **costo mensual** para un patrón de uso particular o necesitas comparaciones que tengan en cuenta el almacenamiento en caché de prompts y los descuentos por volumen!

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."