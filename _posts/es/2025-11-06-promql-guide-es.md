---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía del Lenguaje de Consulta PromQL
translated: true
type: note
---

PromQL (Prometheus Query Language) es un lenguaje de consulta funcional utilizado para seleccionar y agregar datos de series temporales en tiempo real desde Prometheus. Admite consultas instantáneas (evaluadas en un único punto en el tiempo) y consultas de rango (evaluadas en múltiples pasos a lo largo de un intervalo de tiempo). Las expresiones de PromQL pueden devolver uno de cuatro tipos de datos: **vector instantáneo**, **vector de rango**, **escalar** o **cadena de texto**.

---

## Introducción

PromQL permite a los usuarios:
- Seleccionar series temporales usando **selectores de vector instantáneo**.
- Recuperar datos a lo largo de un intervalo de tiempo usando **selectores de vector de rango**.
- Aplicar **operadores** (aritméticos, de comparación, lógicos, de agregación).
- Usar **funciones** como `rate()`, `sum()`, `avg()` para el análisis.
- Consultar datos a través de la **API HTTP**.

Las expresiones se evalúan en la interfaz de usuario de Prometheus:
- **Pestaña Table**: Consultas instantáneas.
- **Pestaña Graph**: Consultas de rango.

---

## Selectores de Series Temporales

Los selectores de series temporales definen qué métricas y etiquetas recuperar.

### Selectores de Vector Instantáneo

Selecciona la muestra más reciente para cada serie temporal que coincida.

**Sintaxis**:  
```
<metric_name>{<label_matchers>}
```

**Ejemplos**:
- Todas las series temporales con la métrica `http_requests_total`:
  ```
  http_requests_total
  ```
- Job y grupo específicos:
  ```
  http_requests_total{job="prometheus", group="canary"}
  ```
- Coincidencia por regex en environment y excluir el método GET:
  ```
  http_requests_total{environment=~"staging|testing|development", method!="GET"}
  ```
- Coincidencia en `__name__`:
  ```
  {__name__=~"job:.*"}
  ```

**Comparadores de Etiquetas**:
- `=` : coincidencia exacta
- `!=` : no igual
- `=~` : coincidencia por regex (anclada)
- `!~` : sin coincidencia por regex

> Nota: `{job=~".+"}` es válido; `{}` solo es inválido.

---

### Selectores de Vector de Rango

Selecciona un rango de muestras a lo largo del tiempo.

**Sintaxis**:  
```
<instant_selector>[<duration>]
```

**Ejemplo**:
- Últimos 5 minutos de `http_requests_total` para el job `prometheus`:
  ```
  http_requests_total{job="prometheus"}[5m]
  ```

> El rango es **abierto-izquierda, cerrado-derecha**: excluye el tiempo de inicio, incluye el final.

---

### Modificador Offset

Desplaza el tiempo de evaluación hacia adelante o hacia atrás.

**Sintaxis**:  
```
<selector> offset <duration>
```

**Ejemplos**:
- Valor de `http_requests_total` hace 5 minutos:
  ```
  http_requests_total offset 5m
  ```
- Tasa de incremento desde hace 1 semana:
  ```
  rate(http_requests_total[5m] offset 1w)
  ```
- Mirar hacia adelante (offset negativo):
  ```
  rate(http_requests_total[5m] offset -1w)
  ```

> Debe seguir inmediatamente al selector.

---

### Modificador `@`

Evalúa en una marca de tiempo específica.

**Sintaxis**:  
```
<selector> @ <timestamp>
```

**Ejemplos**:
- Valor en la marca de tiempo Unix `1609746000`:
  ```
  http_requests_total @ 1609746000
  ```
- Tasa en un momento específico:
  ```
  rate(http_requests_total[5m] @ 1609746000)
  ```
- Usar `start()` o `end()`:
  ```
  http_requests_total @ start()
  rate(http_requests_total[5m] @ end())
  ```

> Se puede combinar con `offset`.

---

## Rate y Agregaciones

PromQL admite la función **rate** y **operadores de agregación** para calcular métricas a lo largo del tiempo o entre series.

### Función Rate

Calcula la tasa de incremento promedio por segundo.

**Ejemplo**:
```
rate(http_requests_total[5m])
```

> Se usa en **vectores de rango**.

---

### Operadores de Agregación

Se aplican a vectores instantáneos para combinar series temporales.

**Ejemplos**:
- Suma de todos los `http_requests_total`:
  ```
  sum(http_requests_total)
  ```
- Promedio por instancia:
  ```
  avg by (instance)(http_requests_total)
  ```
- Recuento por job:
  ```
  count by (job)(http_requests_total)
  ```

> La agregación requiere series coincidentes; use cláusulas `by` o `without`.

---

## Operadores

PromQL admite varios tipos de operadores.

### Operadores Aritméticos

| Operador | Descripción       | Ejemplo                          |
|----------|-------------------|----------------------------------|
| `+`      | Suma              | `rate(a[5m]) + rate(b[5m])`      |
| `-`      | Resta             | `rate(a[5m]) - rate(b[5m])`      |
| `*`      | Multiplicación    | `http_requests_total * 60`       |
| `/`      | División          | `rate(a[5m]) / rate(b[5m])`      |
| `%`      | Módulo            | `http_requests_total % 100`      |

> Los operandos deben ser compatibles (mismo tipo y forma).

---

### Operadores de Comparación

Comparan dos vectores instantáneos.

| Operador | Descripción       | Ejemplo                             |
|----------|-------------------|-------------------------------------|
| `==`     | Igual             | `rate(a[5m]) == rate(b[5m])`        |
| `!=`     | No igual          | `rate(a[5m]) != 0`                  |
| `>`      | Mayor que         | `http_requests_total > 100`         |
| `<`      | Menor que         | `http_requests_total < 10`          |
| `>=`     | Mayor o igual     | `rate(a[5m]) >= 2`                  |
| `<=`     | Menor o igual     | `http_requests_total <= 5`          |

> Devuelve un vector instantáneo booleano.

---

### Operadores Lógicos

Combinan expresiones booleanas.

| Operador | Descripción       | Ejemplo                                 |
|----------|-------------------|-----------------------------------------|
| `and`    | AND lógico        | `rate(a[5m]) > 1 and rate(b[5m]) > 1`   |
| `or`     | OR lógico         | `rate(a[5m]) > 1 or rate(b[5m]) > 1`    |
| `unless` | Excepto           | `rate(a[5m]) unless rate(b[5m]) > 0`    |

> Los operandos deben ser vectores booleanos de la misma cardinalidad.

---

## Funciones

PromQL incluye funciones integradas para transformación y análisis.

**Funciones Comunes**:
- `rate(v range-vector)` – tasa por segundo.
- `irate(v range-vector)` – tasa instantánea (últimos dos puntos).
- `avg(v)` – valor promedio.
- `sum(v)` – suma de valores.
- `count(v)` – número de elementos.
- `min(v)`, `max(v)` – mínimo/máximo.
- `quantile(v instant-vector, q)` – percentil.

**Ejemplo**:
```
quantile by (job)(0.95, http_request_duration_seconds_bucket[5m])
```

> Consulte la [Documentación de Funciones de Prometheus](https://prometheus.io/docs/prometheus/latest/querying/functions/) para ver la lista completa.

---

## API HTTP para Consultas

Las consultas PromQL se pueden enviar a través de la API HTTP.

### Consultas Instantáneas

**Endpoint**: `/api/v1/query`

**Método**: `GET`

**Parámetros**:
- `query`: Expresión PromQL
- `time`: Marca de tiempo de evaluación (segundos Unix, opcional)
- `timeout`: Tiempo de espera de la consulta (ej. `30s`)

**Ejemplo**:
```
GET /api/v1/query?query=http_requests_total{job="prometheus"}&time=1609746000
```

**Respuesta**: JSON con `status`, `data.result` (vector instantáneo o escalar).

---

### Consultas de Rango

**Endpoint**: `/api/v1/query_range`

**Parámetros**:
- `query`: Expresión PromQL
- `start`: Tiempo de inicio (segundos Unix)
- `end`: Tiempo de fin (segundos Unix)
- `step`: Paso de resolución (ej. `15s`)

**Ejemplo**:
```
GET /api/v1/query_range?query=rate(http_requests_total[5m])&start=1609746000&end=1609746600&step=10s
```

**Respuesta**: JSON con datos de series temporales en cada paso.

---

## Notas Adicionales

- **Literales**:
  - Cadenas: `"hello"`, `'world'`, `` `raw` ``
  - Flotantes: `3.14`, `-2.5e-3`, `1_000`, `0xFF`
  - Duración: `5m`, `1h30m`, `500ms`

- **Comentarios**: Comienzan con `#`

- **Obsolescencia**: Las series se vuelven obsoletas después de 5 minutos (por defecto) sin actualizaciones.

- **Subconsulta**: Ejecutar consulta instantánea sobre un rango:
  ```
  rate(http_requests_total[10m:5m])[5m]
  ```

---

Esta guía cubre lo esencial de PromQL para usuarios principiantes a intermedios. Para uso avanzado, consulte los [Conceptos Básicos de Consulta de Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/) y las páginas enlazadas.