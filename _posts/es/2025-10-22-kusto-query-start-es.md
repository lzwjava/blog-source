---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Introducción al lenguaje de consulta Kusto
translated: true
type: note
---

### Introducción a KQL (KQL) en Azure

KQL es un lenguaje de consulta potente y de solo lectura diseñado para analizar grandes volúmenes de datos estructurados, semiestructurados y no estructurados en servicios de Azure como Azure Data Explorer, Azure Monitor (Log Analytics) y Microsoft Sentinel. Es intuitivo, basado en tuberías (usa `|` para el flujo de datos) y está optimizado para escenarios de big data como análisis de registros, telemetría y detección de amenazas. A continuación, se presenta una guía paso a paso para usarlo.

#### Prerrequisitos
- Una suscripción activa de Azure con acceso a un servicio relevante (por ejemplo, un clúster de Azure Data Explorer, un área de trabajo de Log Analytics o una instancia de Sentinel).
- Permisos apropiados: Como mínimo, acceso de lectura a bases de datos, tablas o áreas de trabajo.
- Familiaridad básica con conceptos de datos (como tablas y filtrado) es útil, pero KQL es apto para principiantes.
- Opcional: Instala la aplicación de Azure Data Explorer o usa la interfaz web para empezar rápidamente; no se necesita un entorno de codificación inicialmente.

#### Paso 1: Elige dónde ejecutar tus consultas
KQL se ejecuta en varios servicios de Azure. Comienza con el que se ajuste a tu fuente de datos:
- **Azure Data Explorer**: Ideal para la exploración de big data. Accede a la interfaz web en [dataexplorer.azure.com](https://dataexplorer.azure.com/). Selecciona un clúster y una base de datos, luego abre el editor de consultas.
- **Azure Monitor / Log Analytics**: Para registros y métricas. En el portal de Azure (portal.azure.com), ve a **Monitor > Registros**, selecciona un área de trabajo y usa el editor de consultas.
- **Microsoft Sentinel**: Para análisis de seguridad. En el portal de Azure, navega a **Microsoft Sentinel > Registros** en tu área de trabajo.
- **Otras opciones**: Microsoft Fabric (a través del editor de consultas KQL) o integra con herramientas como Power BI para visualización.

Los datos se organizan en una jerarquía: bases de datos > tablas > columnas. Las consultas son de solo lectura; usa comandos de gestión (que comienzan con `.`) para cambios de esquema.

#### Paso 2: Comprende la sintaxis básica
Las consultas KQL son declaraciones de texto plano separadas por punto y coma (`;`). Utilizan un modelo de flujo de datos:
- Comienza con un nombre de tabla (por ejemplo, `StormEvents`).
- Canaliza (`|`) los datos a través de operadores para filtrado, agregación, etc.
- Termina con una salida como `count` o `summarize`.
- Distingue entre mayúsculas y minúsculas para nombres/operadores; encierra palabras clave en `['palabra clave']` si es necesario.

Una estructura de consulta simple:
```
NombreDeTabla
| where Condición
| summarize Recuento = count() by ColumnaParaAgrupar
```

Los comandos de gestión (no consultas) comienzan con `.` (por ejemplo, `.show tables` para listar tablas).

#### Paso 3: Escribe y ejecuta tu primera consulta
1. Abre el editor de consultas en el servicio elegido (por ejemplo, la interfaz web de Azure Data Explorer).
2. Ingresa una consulta básica. Ejemplo usando datos de muestra (tabla StormEvents, disponible en la mayoría de los entornos):
   ```
   StormEvents
   | where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
   | where State == "FLORIDA"
   | count
   ```
   - Esto filtra las tormentas en Florida para noviembre de 2007 y devuelve el recuento (por ejemplo, 28).
3. Haz clic en **Ejecutar** para ejecutar. Los resultados aparecen como una tabla; usa la interfaz de usuario para visualizar como gráficos o exportar.
4. Itera: Añade operadores como `project` (seleccionar columnas), `summarize` (agregar) o `extend` (añadir columnas calculadas).

Operadores comunes para aprender primero:
- `where`: Filtrar filas (por ejemplo, `| where Level == "Error"`).
- `summarize`: Agregar (por ejemplo, `| summarize avg(Duration) by User`).
- `join`: Combinar tablas.
- `search`: Búsqueda de texto completo en tablas.

#### Paso 4: Explora características avanzadas y mejores prácticas
- **Series de tiempo y análisis**: Usa funciones como `make-series` para tendencias o `detect-anomalies` para valores atípicos.
- **Visualización**: En el editor, cambia a vistas de cuadrícula/gráficos. Exporta a Power BI para paneles.
- **Consejos de rendimiento**: Ordena los operadores lógicamente (filtra pronto), limita los resultados con `take 100` y prueba en conjuntos de datos pequeños.
- **Casos de uso comunes**:
  - **Análisis de registros**: Consulta errores en aplicaciones (`| where Level == "Error" | take 50`).
  - **Búsqueda de seguridad**: En Sentinel, busca amenazas (`search "inicio de sesión sospechoso"`).
  - **Exploración de datos**: Resume métricas (`| summarize count() by bin(TimeGenerated, 1h)`).

#### Resolución de problemas
- ¿Errores? Revisa la sintaxis en el editor (resalta problemas). Asegúrate de que los nombres de tabla/columna coincidan exactamente.
- ¿Sin datos? Verifica que tu área de trabajo haya ingerido registros o usa conjuntos de datos de muestra.
- Aprende más mediante tutoriales interactivos en el portal de Azure o la documentación.

Para practicar, carga datos de muestra en Azure Data Explorer y experimenta.

[Referencias]  
[Introducción al lenguaje de consulta Kusto (KQL)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)  
[Escribe y ejecuta tu primera consulta KQL](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster)  
[Operadores KQL comunes](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster&tabs=beginner)