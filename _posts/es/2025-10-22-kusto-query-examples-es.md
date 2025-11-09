---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejemplos Avanzados del Lenguaje de Consulta Kusto
translated: true
type: note
---

Kusto Query Language (KQL) es una herramienta poderosa para consultar grandes conjuntos de datos en servicios de Azure como Azure Data Explorer y Azure Monitor. A continuación, se presentan varios ejemplos complejos que combinan múltiples operadores, funciones y características avanzadas como análisis de series de tiempo, detección de anomalías, pivoteo y funciones definidas por el usuario. Estos están extraídos de escenarios del mundo real, como el análisis de eventos de tormentas o datos de ventas. Cada uno incluye la consulta y una breve explicación.

### 1. Detección de Anomalías en Datos de Series de Tiempo
Esta consulta agrega promedios diarios desde una tabla de métricas y usa la descomposición de series para identificar anomalías, ideal para monitorear patrones inusuales en registros o telemetría.

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. Función Definida por el Usuario para Filtrado Parametrizado y Resumen
Aquí, una función reutilizable filtra datos de ventas por región y umbral, luego calcula totales—útil para informes dinámicos en los paneles de Azure Data Explorer.

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. Pivoteo de Datos Agregados para Análisis Cruzado
Esto agrega valores por categoría y región, luego convierte las regiones en columnas para una comparación más fácil, común en consultas de business intelligence.

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. Análisis de Correlación Entre Métricas de Series de Tiempo
Usando datos de eventos de tormentas, esto crea series diarias para dos métricas y calcula su correlación para descubrir relaciones, como entre daños materiales y fatalidades.

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. Filtrado, Selección Superior y Cálculo de Duración para Análisis de Eventos
Esto filtra eventos de inundación en Texas, selecciona los 5 principales por daño y agrega una columna de duración calculada—excelente para respuesta a incidentes en Azure Sentinel.

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. Mapeo de Valores Estáticos con Declaración Let para Transformación de Datos
Define un diccionario para mapear tipos de fuente, filtra eventos y proyecta nombres descriptivos—útil para normalizar datos categóricos en registros.

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

Estos ejemplos se pueden ejecutar directamente en la interfaz web de Azure Data Explorer o en Log Analytics. Para más información, explora la galería de ejemplos oficial.

[Guía Completa de Kusto Query Language (KQL)](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[Tutorial: Aprende operadores comunes de Kusto Query Language](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)