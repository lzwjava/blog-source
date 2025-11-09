---
audio: false
date: 2025-09-06
generated: true
image: false
lang: es
layout: post
title: Errores y Soluciones en la Implementación de LSTM
translated: true
type: note
---

Entendido—aquí tienes un recorrido claro y completo de lo que hace este script de LSTM desde cero, más los errores sutiles que romperán el entrenamiento y cómo solucionarlos. Lo mantendré lineal y fácil de escanear (sin tablas anchas).

# Qué intenta hacer el código

Estás implementando un modelo de lenguaje LSTM mínimo a nivel de carácter/palabra en NumPy:

1. **Configuración y tamaños**

* Se espera que `hidden_size`, `vocab_size`, conjuntos de datos (`training_set`, `validation_set`, `test_set`), mapas token↔índice y funciones como `sigmoid`, `tanh`, `softmax`, `one_hot_encode_sequence` provengan de `data.py` / `utils.py`.
* La entrada de cada paso de tiempo es un vector one-hot `x ∈ R^{vocab_size×1}`.
* Concatenas el estado oculto anterior y la entrada actual:
  `z = [h_{t-1}; x_t] ∈ R^{(hidden_size+vocab_size)×1}`.
  Por eso `W_f, W_i, W_g, W_o ∈ R^{hidden_size×(hidden_size+vocab_size)}`.

2. **Inicialización de parámetros**

* `init_lstm(...)` asigna pesos para las cuatro puertas (olvido f, entrada i, candidata g, salida o), más la proyección de salida `W_v` al vocabulario.
* `init_orthogonal` hace que cada matriz de pesos sea ortonormal (vía QR). Es una elección decente para RNNs/LSTMs.

3. **Paso hacia adelante (por secuencia)**
   Para cada paso de tiempo:

* Construye `z = [h_prev; x]`.
* Calcula las puertas:

  * `f_t = σ(W_f z + b_f)`
  * `i_t = σ(W_i z + b_i)`
  * `g_t = tanh(W_g z + b_g)`
  * `C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t`
  * `o_t = σ(W_o z + b_o)`
  * `h_t = o_t ⊙ tanh(C_t)`
* Proyecta al vocabulario y aplica softmax:

  * `v_t = W_v h_t + b_v`
  * `ŷ_t = softmax(v_t)`
* El código almacena muchos intermedios (`z_s, f_s, i_s, g_s, C_s, o_s, h_s, v_s, output_s`) para la retropropagación.

4. **Pérdida**

* Entropía cruzada en cada paso con un objetivo one-hot:
  `L_t = − log ŷ_t[target]`
  (El código usa `-mean(log(ŷ)*one_hot)` elemento a elemento, que es equivalente a `-log(ŷ[target])` hasta un factor de escala constante).

5. **Paso hacia atrás (BPTT a través de LSTM)**

* Gradientes clásicos de LSTM, acumulados desde `t = T−1 → 0`.
* Recorta la norma global del gradiente, luego actualiza con SGD.

6. **Bucle de entrenamiento**

* Para cada época: evalúa en el conjunto de validación (solo pérdida), luego entrena en el conjunto de entrenamiento (pérdida + gradientes + actualización). Finalmente, grafica las pérdidas de entrenamiento/validación.

---

# Problemas críticos (estos romperán el aprendizaje silenciosamente)

## 1) Indexación fuera de by-one para `h` y `C` en la retropropagación

En `forward`, introduces los estados *iniciales* primero:

* `h_s[0] = h_init`, luego después del paso 0 añades `h_0` → así que `h_s` tiene longitud `T+1` con `h_s[t+1] = h_t`.
* Lo mismo para `C_s`: `C_s[0] = C_init`, luego `C_s[t+1] = C_t`.

Pero en `backward(...)` usas `h[t]` y `C[t]` como si fueran `h_t` y `C_t`. No lo son; están desplazados por uno.

**Solución (regla simple):**

* Usa `h[t+1]` donde quieras `h_t`.
* Usa `C[t+1]` donde quieras `C_t`.
* Para el "estado de celda anterior" quieres `C_prev = C[t]` (no `C[t-1]`).

Así que dentro del bucle `for t in reversed(range(T)):`:

* Estado actual: `h_t = h[t+1]`, `C_t = C[t+1]`
* Estado anterior: `C_{t-1} = C[t]`

Tu línea actual:

```python
C_prev = C[t - 1]
```

es incorrecta para `t==0` (accede al último elemento) y está desplazada en general. Debe ser:

```python
C_prev = C[t]       # estado de celda anterior
# y usa C_t = C[t+1] como "actual"
```

Y donde uses `h[t]` queriendo el estado oculto actual, cámbialo a `h[t+1]`.

## 2) Derivadas incorrectas para varias puertas

A veces aplicas la no linealidad otra vez en lugar de su derivada, u olvidas el flag de derivada.

* **Ruta del estado de celda:**
  Correcto:
  `dC_t += dh_t ⊙ o_t ⊙ (1 - tanh(C_t)^2)`
  Tu código:

  ```python
  dC += dh * o[t] * tanh(tanh(C[t]), derivative=True)
  ```

  Eso es aplicar `tanh` dos veces. Reemplaza con:

  ```python
  dC += dh * o_t * (1 - np.tanh(C_t)**2)
  ```

* **Puerta de olvido:**
  Correcto: `df = dC_t ⊙ C_{t-1} ⊙ f_t ⊙ (1 - f_t)`
  Tu código:

  ```python
  df = dC * C_prev
  df = sigmoid(f[t]) * df
  ```

  Falta el término de la derivada. Debería ser:

  ```python
  df = dC * C_prev
  df *= f[t] * (1 - f[t])      # si f[t] almacena la salida pre-activación de σ
  ```

* **Puerta de entrada:**
  Hiciste:

  ```python
  di = dC * g[t]
  di = sigmoid(i[t], True) * di
  ```

  Esto está bien **si** `sigmoid(x, True)` devuelve σ'(x) *no* σ(x). Más robusto (coincidiendo con cómo almacenaste `i[t]` como salida de la puerta) es:

  ```python
  di = dC * g[t]
  di *= i[t] * (1 - i[t])
  ```

* **Puerta candidata:**
  Hiciste:

  ```python
  dg = dC * i[t]
  dg = tanh(g[t], derivative=True) * dg
  ```

  Si `g[t]` almacena `tanh(preact)`, entonces `tanh’(preact) = 1 - g[t]^2`. Así que:

  ```python
  dg = dC * i[t]
  dg *= (1 - g[t]**2)
  ```

* **Puerta de salida:**
  Hiciste:

  ```python
  do = dh * tanh(C[t])
  do = sigmoid(o[t], derivative=True) * do
  ```

  Con la corrección de indexación (`C_t = C[t+1]`, `o_t = o[t]`) y la derivada como arriba:

  ```python
  do = dh * np.tanh(C_t)
  do *= o[t] * (1 - o[t])
  ```

* **Gradiente de la siguiente celda:**
  Correcto:

  ```python
  dC_next = dC * f[t]
  ```

## 3) Usar `h[0]` / `C[0]` para dimensionar `dh_next` y `dC_next`

Quieres las formas de h/C **actuales** (fin de secuencia), no los ceros iniciales. Usa:

```python
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])
```

## 4) Estabilidad aritmética de la entropía cruzada

`loss += -np.mean(np.log(outputs[t]) * targets[t])` estará bien si `softmax` ajusta/agrega épsilon internamente. Si no, añade un épsilon pequeño:

```python
eps = 1e-12
loss += -np.sum(targets[t] * np.log(outputs[t] + eps))
```

## 5) Ajustes de estabilidad del entrenamiento

* **Sesgo de la puerta de olvido:** inicializa `b_f` a un valor positivo (ej., `1.0`) para que al principio del entrenamiento la LSTM tienda a mantener la memoria:

  ```python
  b_f = np.ones((hidden_size, 1)) * 1.0
  ```
* **Tasa de aprendizaje:** `lr=1e-1` con SGD puro es agresivo. Empieza con `1e-2` o usa Adam.
* **Recorte de gradiente:** Bien. Considera normas por matriz si es necesario.

---

# Un núcleo corregido para el bucle de retropropagación

Este esquema muestra las correcciones de indexación y derivadas. Asume que `f[t], i[t], g[t], o[t]` son las *salidas* de sus no linealidades (como en tu forward):

```python
T = len(outputs)
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])

for t in reversed(range(T)):
    # Nombres cortos con indexación correcta
    y_hat = outputs[t]                 # salida softmax
    y_true = targets[t]
    h_t   = h[t+1]
    C_t   = C[t+1]
    C_tm1 = C[t]

    # Capa de salida
    dv = y_hat.copy()
    dv[np.argmax(y_true)] -= 1
    W_v_d += dv @ h_t.T
    b_v_d += dv

    # Retropropagar hacia h
    dh = W_v.T @ dv
    dh += dh_next

    # Puerta de salida
    do = dh * np.tanh(C_t)
    do *= o[t] * (1 - o[t])
    W_o_d += do @ z[t].T
    b_o_d += do

    # Estado de celda
    dC = dC_next + dh * o[t] * (1 - np.tanh(C_t)**2)

    # Candidata (g), Entrada (i), Olvido (f)
    dg = dC * i[t]
    dg *= (1 - g[t]**2)               # ya que g[t] = tanh(preact)

    di = dC * g[t]
    di *= i[t] * (1 - i[t])

    df = dC * C_tm1
    df *= f[t] * (1 - f[t])

    # Acumular gradientes de pesos/sesgos de las puertas
    W_g_d += dg @ z[t].T;  b_g_d += dg
    W_i_d += di @ z[t].T;  b_i_d += di
    W_f_d += df @ z[t].T;  b_f_d += df

    # Propagación hacia z y división a la parte h_{t-1}
    dz = (W_f.T @ df) + (W_i.T @ di) + (W_g.T @ dg) + (W_o.T @ do)
    dh_next = dz[:hidden_size, :]
    dC_next = dC * f[t]
```

---

# Detalles más pequeños pero importantes y recomendaciones

* **Inicialización ortogonal:** Buena para pesos recurrentes. Para las partes de entrada, también podrías escalar por `1/√fan_in`. No es crítico aquí.
* **Lotes:** El código entrena con 1 secuencia a la vez (sin lotes). Bien para claridad, pero lento/con ruido. El mini-lote requeriría cambios cuidadosos en las formas.
* **Teacher forcing:** Estás usando el siguiente token de la verdad fundamental como objetivo; todo bien. Si alguna vez haces generación libre, muestrea de las salidas `softmax` y retroaliméntalo al modelo.
* **Reporte de pérdida:** Sumas las pérdidas por paso de tiempo a través de secuencias y luego promedias por la longitud del conjunto de datos; eso mezcla escalas si las secuencias varían en longitud. Considera normalizar por el total de tokens.
* **Graficado:** Funciona localmente. En entornos sin interfaz gráfica, recuerda cambiar backends o usar savefig.

---

# TL;DR de las correcciones que deberías hacer ahora mismo

1. **Indexación**: Reemplaza cada `h[t]` con `h[t+1]`, cada `C[t]` con `C[t+1]`, y establece `C_prev = C[t]` en la retropropagación.
2. **Derivadas**:

   * Usa `(1 - tanh(C_t)**2)` para la ruta del estado de celda.
   * Usa `puerta * (1 - puerta)` para las puertas-σ ya que almacenaste las salidas de las puertas.
   * Usa `(1 - g[t]**2)` para la puerta candidata ya que `g[t]=tanh(preact)`.
3. **Inicialización**: Establece `b_f` a \~`1.0`.
4. **LR**: Bájalo a `1e-2` (o cambia a Adam).
5. **Estabilidad**: Añade `eps` en `log`.

Haz esos cambios y tu pérdida debería empezar a disminuir de una manera mucho más sensata. Si quieres, pega tu `backward(...)` actualizado y lo revisaré.