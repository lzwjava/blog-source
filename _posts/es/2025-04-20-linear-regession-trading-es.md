---
audio: false
generated: true
lang: es
layout: post
title: Uso de la Regresión Lineal para Operar en los Mercados
translated: true
type: note
---

¡Excelente pregunta! Estás combinando dos tareas aquí:

1.  **Obtener datos históricos de acciones (por ejemplo, Tencent) usando TigerOpen API**
2.  **Usar esos datos con tu código existente de regresión lineal basado en numpy**

---

## ¿Funcionará tal cual?

**No, no directamente.** Tu código actual de ML espera `x_train` e `y_train` como arrays de numpy de valores numéricos que representan características y etiquetas (por ejemplo, población vs. beneficio). Pero la API de TigerOpen devuelve **barras históricas de acciones** (datos OHLCV), que es una serie temporal con múltiples campos por marca de tiempo.

Necesitas:

- Extraer y preprocesar correctamente los datos de la acción en arrays `x_train` e `y_train` adecuados.
- Adaptar tu modelo y código al contexto de los datos de acciones (por ejemplo, predecir el precio de cierre a partir de días anteriores).

---

## ¿Cómo adaptar tus datos de acciones para tu modelo de regresión lineal?

### Paso 1: Obtener datos históricos para Tencent (símbolo `'00700'`)

```python
bars_dict = quote_client.get_bars(
    symbols=['00700'],
    period=BarPeriod.DAY,
    begin_time='2024-01-01',
    end_time=datetime.now().strftime('%Y-%m-%d'),
    limit=100,
    right=QuoteRight.BR
)

bars = bars_dict.get('00700', [])
```

### Paso 2: Extraer características y etiquetas

Un enfoque simple:

- Usar el índice del día como `x_train` (por ejemplo, 0, 1, 2, ...)
- Usar el precio de cierre como `y_train`

```python
import numpy as np

x_train = np.array([i for i in range(len(bars))])
y_train = np.array([bar.close for bar in bars])
```

Alternativamente, puedes usar el cierre del día anterior como característica para predecir el cierre del día siguiente, o características más sofisticadas.

### Paso 3: Usar tu código de regresión lineal

Ahora tus `x_train` e `y_train` son arrays de numpy de números, por lo que tu código debería funcionar bien después de que arregles tus funciones `compute_cost` y `compute_gradient` (que actualmente devuelven cero o gradientes cero).

---

## Ejemplo: Implementar compute_cost y compute_gradient

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    total_cost = 0.5 * np.sum((w * x + b - y) ** 2) / m
    return total_cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    error = w * x + b - y
    dj_dw = np.sum(error * x) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db
```

---

## Resumen

- Obtén datos históricos de acciones con la API de TigerOpen
- Convierte los datos de series temporales en arrays numéricos (`x_train`, `y_train`)
- Implementa o corrige tus funciones de costo y gradiente
- Entonces tu código de descenso de gradiente y graficado funcionará para ajustar un modelo lineal a los datos del precio de la acción

---

## Extra: Graficar precios de acciones

Tu gráfico de dispersión mostrará el precio de cierre a lo largo de los días, y la línea de regresión ajustará una tendencia.

---

Si quieres, ¡puedo ayudarte a escribir un ejemplo completo que integre la obtención de datos de TigerOpen con tu código de regresión lineal en numpy! Solo pídelo.