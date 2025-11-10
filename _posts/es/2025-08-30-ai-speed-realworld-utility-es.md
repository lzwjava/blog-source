---
audio: false
generated: true
image: false
lang: es
layout: post
title: La Velocidad de la IA Encuentra la Utilidad del Mundo Real
translated: true
type: note
---

Aquí están los **puntos clave** del artículo:

---

### Concepto Central

* Los **benchmarks de IA tradicionales** se centran principalmente en la precisión/calidad, pero descuidan la **velocidad de procesamiento**, que es crucial en aplicaciones del mundo real sensibles al tiempo (por ejemplo, conducción autónoma, servicio al cliente).
* Las métricas de velocidad existentes (TTFT, TPS) son **centradas en tokens** e inadecuadas para un futuro de IA multimodal.
* **Nueva métrica propuesta**: **Ancho de Banda de Inteligencia** — la cantidad de información útil que una IA puede producir por unidad de tiempo.

---

### Aproximaciones al Ancho de Banda de Inteligencia

1. **Puntuación de benchmark por tiempo**

   * Utilizar el rendimiento normalizado del benchmark dividido por el tiempo empleado.
   * Más informativo que tokens/segundo para tareas prácticas.

2. **Enfoque de teoría de la información**

   * Medir el contenido de información de la salida mediante distribuciones de probabilidad.
   * Limitado porque información ≠ utilidad y requiere acceso a vectores de probabilidad.

3. **Bits de salida en bruto por segundo**

   * El más simple, agnóstico a la modalidad.
   * Mide bits/segundo de la salida de IA (texto, imagen, video).
   * No mide directamente la utilidad, pero funciona si se aplica solo a los modelos de mejor rendimiento.

---

### Contexto Histórico

* La velocidad se ignoraba anteriormente porque:

  1. La IA no era lo suficientemente avanzada para necesitarla.
  2. Las aplicaciones eran estrechas y específicas de la tarea.
* Con los **LLM** y la **IA multimodal**, se ha vuelto necesaria una **métrica de velocidad unificada**.

---

### Implicaciones para la Interacción Humano-IA

* Similar a la **Ley de Moore** y la **Ley de Nielsen**, esta métrica puede revelar tendencias de crecimiento.
* **Concepto de umbral**: una vez que la velocidad de salida de la IA supera la velocidad perceptual humana (por ejemplo, lectura o escucha), la interacción en tiempo real se vuelve posible.
* La IA ya supera las velocidades humanas de lectura y escucha; la siguiente frontera es la **integración de imagen y video en tiempo real**.
* Futuro: La IA podría soportar **razonamiento visual en tiempo real, diseño estilo pizarra y entornos virtuales inmersivos**.

---

### Experimentos y Datos

* Medición a través de LLM históricos, generadores de imagen y video utilizando **bits de salida en bruto/seg**.
* **Observaciones**:

  * LLM: 0–3 KB/s.
  * Generadores de imagen: crecimiento exponencial.
  * Generadores de video: actualmente rezagados pero se espera que aceleren.
  * **Gemini 2.5 Flash** es un caso atípico (optimizado para baja latencia).

---

### Ley de Jin

* **Formulación**: *El ancho de banda de inteligencia del mejor modelo de IA alojado disponible públicamente se duplica cada año.*
* Actualmente liderado por **generadores de imagen**; se espera que el video tome la delantera a medida que mejore el servicio.
* **Predicciones**:

  1. La **integración de imágenes en el chat de IA** se volverá estándar dentro de 1 año.
  2. La **interacción con video en tiempo real** será factible dentro de ~3 años (requiere una aceleración de ~8×).

---

### Limitaciones

* Definir la **"información útil"** sigue sin resolverse.
* Los datos actuales son escasos, por lo que la estimación de duplicación anual es incierta.
* El crecimiento puede estar limitado por la energía/economía, no solo por el progreso tecnológico.

---

### Conclusión

* La evaluación de la IA debe tener en cuenta **tanto la corrección como la velocidad**, reflejando la evaluación de la inteligencia humana.
* El **Ancho de Banda de Inteligencia** ofrece un marco predictivo para el futuro de la IA, especialmente para la **interacción multimodal en tiempo real**.

---

¿Quieres que también cree una **línea de tiempo de estilo visual** de las predicciones de la Ley de Jin (texto → imágenes → video → entornos inmersivos) para que sea más fácil de entender de un vistazo?