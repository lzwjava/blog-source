---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Algoritmo FlashAttention y sus Beneficios
translated: true
type: note
---

# Explicación profunda de FlashAttention (Tri Dao et al., 2022)

Resumen breve al inicio: FlashAttention elimina la necesidad de asignar la matriz de atención completa \\(N\times N\\) en la DRAM de la GPU (HBM) al calcular la atención **bloque por bloque** dentro de la SRAM en el chip (registros / memoria compartida), fusionando toda la canalización de atención en un solo kernel y utilizando una acumulación softmax correcta numéricamente bloque por bloque. Eso reduce drásticamente el tráfico y la memoria de HBM de \\(O(N^2)\\) a efectivamente \\(O(N)\\), y en la práctica proporciona grandes aceleraciones en tiempo real en GPUs para secuencias largas. citeturn0search0turn0search9

---

## El problema: por qué la atención estándar está limitada por E/S
La autoatención del Transformer (producto escalado) generalmente se implementa en tres pasos:

1. calcular las puntuaciones \\(S = Q K^\top\\) (tamaño \\(N\times N\\));  
2. calcular softmax por filas \\(P = \mathrm{softmax}(S)\\);  
3. calcular la salida \\(O = P V\\).

De manera ingenua, se materializa \\(S\\) (y a menudo \\(P\\)) en la DRAM de la GPU. Para una longitud de secuencia \\(N\\) esto usa memoria \\(O(N^2)\\) y conduce a dos problemas de E/S:
- gran huella de DRAM (a menudo lo primero que agota la memoria de la GPU), y  
- muchas lecturas/escrituras entre la DRAM (HBM) y la SRAM/registros en el chip — y esas transferencias HBM↔SRAM son el cuello de botella real en las GPUs modernas.

FlashAttention reformula la atención como un **problema de E/S**, no solo un problema de FLOPS, y se enfoca en reducir los accesos a HBM. citeturn0search0

---

## Ideas principales (a alto nivel)
1. **Dividir en mosaicos las matrices** \\(Q, K, V\\) en bloques que quepan en la SRAM en el chip (memoria compartida / registros).  
2. **Procesar la atención bloque por bloque**: para un mosaico- \\(Q\\) dado y un conjunto en flujo de mosaicos- \\(K,V\\), calcular las contribuciones parciales a la salida y acumularlas inmediatamente — nunca materializar la matriz de puntuación completa \\(N\times N\\) en DRAM.  
3. **Fusionar todo en un solo kernel**: el kernel carga los mosaicos en SRAM, calcula \\(QK^\top\\) para ese par de mosaicos, aplica la lógica softmax y multiplica por el mosaico- \\(V\\), y escribe salidas parciales — todo sin viajes de ida y vuelta de matrices grandes intermedias a DRAM. La fusión de kernels reduce la sobrecarga de instrucciones y memoria.  
4. **Acumulación softmax numéricamente estable bloque por bloque**: debido a que el softmax a lo largo de toda la fila necesita el máximo y la suma globales, FlashAttention utiliza un máximo en ejecución / suma en ejecución (estilo log-sum-exp) para combinar las contribuciones softmax de múltiples mosaicos- \\(K\\) de manera exacta y estable sin almacenar la fila completa de puntuaciones.  
5. **Hacia atrás mediante recálculo**: en lugar de almacenar grandes intermedios para la pasada hacia atrás, recalcular la atención hacia adelante para cada bloque durante la pasada hacia atrás (intercambiar FLOPS extra por mucho menos E/S de DRAM). La E/S de DRAM ahorrada generalmente produce una aceleración neta ya que la E/S de DRAM domina. citeturn0search2turn0search10

Estas ideas juntas producen tanto una reducción de memoria como mejoras de velocidad en tiempo real. citeturn0search0

---

## Algoritmo bloque por bloque — paso a paso (hacia adelante)
Considere una sola cabeza de atención con longitud de secuencia \\(N\\) y dimensión de cabeza \\(d\\). Elija un tamaño de mosaico \\(B\\) para que un bloque de puntuaciones \\(B\times B\\) y los mosaicos correspondientes de \\(Q\\), \\(K\\), \\(V\\) quepan en SRAM.

Para cada mosaico de consulta \\(Q_{i}\\) (filas \\(iB:(i+1)B\\)):

1. Inicializar un acumulador de salida \\(O_i \leftarrow 0\\).  
2. Inicializar el estado de normalización en ejecución: `row_max` (por fila de consulta) a \\(-\infty\\), `row_sum` a 0. Estos rastrean el denominador numéricamente estable para softmax a través de múltiples mosaicos-K.  
3. Para cada mosaico de clave/valor \\(K_{j}, V_{j}\\) (columnas \\(jB:(j+1)B\\)):
   - Cargar \\(Q_i\\), \\(K_j\\), \\(V_j\\) en SRAM.  
   - Calcular el mosaico de puntuaciones en bruto \\(S_{ij} = Q_i K_j^\top / \sqrt{d}\\) (forma \\(B\times B\\) en forma vectorizada).
   - Para cada fila en \\(S_{ij}\\), calcular el máximo local de la fila \\(m_{ij}\\) y los valores exponenciados \\(\exp(S_{ij} - m_{ij})\\).  
   - Fusionar los exponenciales de este mosaico en la normalización de fila en ejecución usando el truco de log-sum-exp:
     - Sea \\(M = \max(\text{row\_max}, m_{ij})\\).
     - Actualizar `row_sum` := `row_sum` · exp(row_max − M) + local_sum · exp(m_{ij} − M).
     - Establecer `row_max` := \\(M\\).
   - Calcular la contribución del mosaico al acumulador con los exponenciales escalados apropiadamente: acumular \\(O_i \mathrel{+}= \text{(softmax-del-mosaico)} \times V_j\\). (Todo hecho dentro de SRAM.)
4. Después de transmitir todos los mosaicos-K, finalizar la normalización usando row_sum y row_max para producir las salidas softmax correctas; escribir \\(O_i\\) a DRAM.

Punto clave: ninguna matriz \\(N\times N\\) se escribe nunca en DRAM; solo se escriben mosaicos pequeños y salidas finales. La acumulación numéricamente correcta usando el máximo en ejecución + suma es lo que permite que las piezas softmax por mosaico se combinen exactamente en el mismo resultado que un softmax completo sobre la fila. citeturn0search2turn0search10

---

## Por qué la fusión de kernels y el mosaico en SRAM ganan en la práctica
- **Menos accesos a HBM:** La atención estándar lee/escribe \\(O(N^2)\\) elementos a DRAM (puntuaciones, softmax). FlashAttention lee cada elemento \\(Q,K,V\\) un número constante de veces, y todos los valores temporales de puntuación/softmax viven solo en SRAM. El análisis de E/S en el artículo muestra menos accesos a HBM y rangos donde FlashAttention es óptimo en E/S dado el tamaño de SRAM. citeturn0search0  
- **Los límites de latencia y ancho de banda importan más que los FLOPS:** Las GPUs son extremadamente rápidas en multiplicación-acumulación en punto flotante; cuando el tráfico de DRAM domina el tiempo de ejecución, reducir las transferencias de DRAM importa más que reducir los FLOPS. La fusión de kernels elimina el tráfico intermedio de DRAM y reduce la sobrecarga de lanzamiento del kernel. citeturn0search0  
- **Compensación en la pasada hacia atrás:** Recalcular los bloques hacia adelante durante la pasada hacia atrás aumenta los FLOPS pero evita almacenar grandes intermedios en DRAM. Debido a que el recálculo ocurre en SRAM y limita el tráfico de DRAM, es una ganancia neta para el tiempo de ejecución en muchos casos. citeturn0search10

Los resultados empíricos del artículo y trabajos posteriores muestran múltiples× aceleraciones (por ejemplo, 2–7× en sus puntos de referencia reportados dependiendo del modelo y la longitud de secuencia) y grandes reducciones en el uso máximo de memoria. citeturn0search0turn0search10

---

## Detalles de implementación importantes y compensaciones

- **Selección del tamaño del mosaico:** El mosaico \\(B\\) debe elegirse para que el conjunto de trabajo (mosaicos de Q, K, V, búferes de puntuación, acumuladores parciales, más espacio extra) quepa en la SRAM en el chip por bloque de hilos. El \\(B\\) óptimo depende de la dimensión de la cabeza, los tipos de datos (FP16/FP32/FP8) y la arquitectura de la GPU (cantidad de memoria compartida / registros). Demasiado pequeño reduce la eficiencia de cálculo; demasiado grande no cabe en SRAM. citeturn0search2

- **Estabilidad numérica:** El algoritmo utiliza un máximo y una suma en ejecución por fila (fusión log-sum-exp) para garantizar que el softmax final sea igual al softmax de matriz completa. Eso es crucial: FlashAttention es **atención exacta** (no una aproximación) debido a esa acumulación estable. citeturn0search0

- **Enmascaramiento y causalidad:** El enmascaramiento causal (autoregresivo) se maneja simplemente omitiendo o poniendo a cero las contribuciones de las posiciones enmascaradas en los mosaicos transmitidos y actualizando la normalización en ejecución en consecuencia. La lógica bloque por bloque aún funciona pero puede necesitar un ordenamiento cuidadoso de los mosaicos para garantizar que los elementos enmascarados no contaminen los acumuladores. citeturn0search2

- **Pasada hacia atrás y diseño de memoria:** FlashAttention almacena solo metadatos mínimos (por ejemplo, row_max/row_sum por bloque) y recalcula los productos de mosaicos hacia adelante durante la pasada hacia atrás. Las implementaciones reordenan cuidadosamente el trabajo para maximizar la reutilización y minimizar la presión de registros. citeturn0search10

- **Precisión y tipos de datos:** Usar FP16/FP8 afecta las opciones de almacenamiento en búfer y acumulación de mosaicos. Algunos trabajos posteriores (FlashAttention-2 / FlashAttention-3) agregan optimizaciones para precisión mixta y características más nuevas de GPU (Hopper, H100) para impulsar aún más la utilización y el rendimiento en punto flotante. citeturn0search4turn0search11

- **Mapeo de paralelismo:** El kernel asigna warps/bloques CTA a mosaicos de consulta; dentro de un CTA, los warps cooperan cargando mosaicos K/V y calculando el producto matricial de mosaicos y reducciones. Las reducciones eficientes a nivel de warp y el uso de instrucciones de multiplicación-suma fusionadas son importantes para el rendimiento máximo. citeturn0search2

---

## FlashAttention vs. métodos de atención larga aproximada
FlashAttention mantiene la semántica de atención **exacta** (el mismo resultado numérico que la atención completa hasta el redondeo en punto flotante), mientras que muchos métodos de atención larga aproximan la atención (esparcidad, bajo rango, FAVOR+, etc.) y intercambian calidad por memoria/tiempo. FlashAttention en cambio reduce el costo de memoria/E/S mientras preserva el cálculo exacto, por lo que la calidad del modelo no cambia mientras que el rendimiento/la memoria mejoran. Esa es la razón por la que es ampliamente atractivo: sin compensación de precisión, solo un kernel de bajo nivel mejorado. citeturn0search0

---

## Disponibilidad práctica y ecosistema
- Los autores publicaron una implementación (CUDA) y un repositorio mantenido con FlashAttention y posteriormente FlashAttention-2. Muchos frameworks (Hugging Face Transformers, bifurcaciones de XLA/PyTorch, implementaciones basadas en Triton) llaman al operador flash-attn o proporcionan kernels fusionados similares. Puedes usar el operador `flash_attn` o bibliotecas que lo expongan; en PyTorch, las versiones recientes incluyen también primitivas de atención eficiente en memoria, y los paquetes de terceros `flash_attn` dan una mejora de velocidad/memoria inmediata para muchas cargas de trabajo. Consulta el repositorio oficial para instaladores y ejemplos de API. citeturn0search9turn0search4

Advertencia: "No hay necesidad de kernels personalizados" es solo parcialmente cierto — FlashAttention *es* un kernel fusionado personalizado (el trabajo en el repositorio) que los frameworks llaman. Las versiones modernas de PyTorch pueden incluir internamente kernels fusionados comparables o delegar en bibliotecas del proveedor, pero la idea central requiere una implementación de kernel fusionado (ya sea en CUDA, Triton o código del proveedor). La lección importante: tú (como usuario de modelo) no tienes que escribir esos kernels tú mismo — usa el operador proporcionado. citeturn0search9turn0search7

---

## Extensiones y trabajos posteriores
- **FlashAttention-2 (2023):** mejora el paralelismo, la partición del trabajo y el escalado multinúcleo para obtener una utilización y rendimiento de GPU aún mejores. citeturn0search4  
- **FlashAttention-3 y otros trabajos de ingeniería (2024+):** ajustes adicionales para nuevo hardware (Hopper/H100), FP8 y una utilización de TFLOP aún mayor. Estos continúan la tendencia de kernels de atención fusionados conscientes del hardware. citeturn0search11

---

## Cuándo ayuda más FlashAttention (reglas generales)
- **Secuencias largas** (múltiples miles) o tamaños grandes de lote/cabeza — ahorra más memoria y da las mayores aceleraciones.  
- **Cuando el ancho de banda de DRAM es el cuello de botella** — por ejemplo, modelos grandes con \\(N\\) grande donde la atención ingenua saturaría la DRAM.  
- **Entrenamiento con contextos grandes** ya que la pasada hacia atrás favorable al recálculo reduce la memoria máxima (permite lote/contexto más grande). citeturn0search0

---

## Pseudocódigo rápido (conceptual)
```
para cada mosaico de consulta Qi:
    row_max = -inf (por fila)
    row_sum = 0    (por fila)
    out_acc = 0    (B x d_v)
    para cada mosaico de clave/valor Kj, Vj:
        cargar Qi, Kj, Vj en SRAM
        S = Qi @ Kj.T / sqrt(d)
        m = max_fila(S)
        expS = exp(S - m)      # exponenciales locales
        suma_local = suma_fila(expS)
        # fusionar normalizadores de forma estable:
        M = max(row_max, m)
        row_sum = row_sum * exp(row_max - M) + suma_local * exp(m - M)
        row_max = M
        # acumular salida parcial con expS escalado:
        out_acc += (expS / (row_sum después de fusionar)) @ Vj
    escribir out_acc a DRAM
```
(La implementación almacena más metadatos y organiza el escalado exacto cuidadosamente; lo anterior es conceptual.) citeturn0search2

---

## Referencias / dónde leer a continuación
- Artículo original de FlashAttention (Tri Dao et al., 2022) — algoritmo, análisis de E/S, puntos de referencia. citeturn0search0turn0search2  
- GitHub oficial con kernels CUDA y enlaces de PyTorch. citeturn0search9  
- Artículo de FlashAttention-2 (Tri Dao, 2023) y notas de ingeniería sobre versiones posteriores. citeturn0search4turn0search11

---

Si quieres, puedo:
- mostrar una comparación línea por línea de un bucle de atención ingenuo vs. el pseudocódigo de FlashAttention bloque por bloque (sin tablas anchas),  
- esbozar la organización del kernel CUDA/Triton y la planificación de registros/memoria compartida para un ejemplo concreto (por ejemplo, dim de cabeza 64, mosaico 128), o  
- indicarte la llamada exacta a la API de PyTorch y un fragmento de ejemplo para reemplazar `torch.nn.functional.scaled_dot_product_attention` con FlashAttention. ¿Cuál sería más útil a continuación?