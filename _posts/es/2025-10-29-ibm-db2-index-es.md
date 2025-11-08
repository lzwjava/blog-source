---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Estructura de Índices de IBM DB2 Explicada
translated: true
type: note
---

### Cómo funcionan los índices de IBM DB2

IBM DB2 utiliza **árboles B+** como estructura de datos principal para sus índices. Esta es una variante de árbol balanceado optimizada para almacenamiento en disco y consultas de rango, comunes en bases de datos relacionales. Los árboles B+ garantizan búsquedas, inserciones y eliminaciones eficientes con complejidad de tiempo logarítmica (O(log n)), lo que los hace ideales para grandes conjuntos de datos. A continuación, desglosaré la estructura, las operaciones clave y las notas específicas de DB2.

#### Estructura del árbol B+ en DB2
Un árbol B+ en DB2 se organiza en una jerarquía de **páginas** (también llamadas nodos), cada una típicamente de 4KB de tamaño en disco. El árbol es auto-balanceable, lo que significa que todos los nodos hoja están a la misma profundidad, y crece o se reduce dinámicamente a medida que cambian los datos. Aquí está el desglose:

- **Página Raíz**: El punto de entrada en la parte superior del árbol. Contiene valores de clave ordenados y punteros a las páginas hijas debajo de ella. Para índices pequeños, la raíz puede apuntar directamente a las páginas hoja.
  
- **Páginas Internas (No Hoja)**: Estos niveles intermedios actúan como directorios. Cada página contiene:
  - Una lista ordenada de **claves de índice** (los valores de la(s) columna(s) indexada(s), por ejemplo, IDs de empleado).
  - Punteros a páginas hijas (un puntero más que claves, separando rangos).
  - Específicamente, cada entrada es el **valor de clave más alto** en el subárbol debajo de ella, emparejado con un **Identificador de Registro (RID)**—un puntero único a la página y ranura donde vive la fila de datos real en la tabla.
  
  Las páginas no hoja *no* almacenan punteros de datos reales; guían el recorrido.

- **Páginas Hoja**: El nivel inferior, enlazado bidireccionalmente (hacia adelante y hacia atrás) para escaneos de rango eficientes. Cada página hoja contiene:
  - **Valores de clave** completos y ordenados de la(s) columna(s) indexada(s).
  - **RIDs** asociados que apuntan directamente a las filas de la tabla.
  - Punteros a páginas hoja adyacentes, permitiendo acceso secuencial (por ejemplo, para `WHERE columna ENTRE x AND y`).

El árbol comienza con al menos 2 niveles (raíz + hojas) y puede crecer a 3–5+ niveles para tablas masivas (millones de filas). El número de niveles (NLEVELS) se puede consultar mediante `SYSCAT.INDEXES` y afecta el rendimiento—menos niveles significan recorridos más rápidos, pero DB2 lo gestiona automáticamente.

Los índices se almacenan por separado de las tablas en su propio tablespace, consumiendo espacio en disco proporcional a los datos indexados (por ejemplo, un índice único en una tabla de 1M de filas podría ocupar ~10–20% del tamaño de la tabla).

#### Cómo funciona la búsqueda
1. Comienza en la **página raíz** y cárgala en memoria.
2. Compara la clave de búsqueda (por ejemplo, `WHERE id = 123`) con las claves ordenadas en la página actual.
3. Selecciona el puntero hijo apropiado (por ejemplo, si la clave de búsqueda > clave actual, ir a la derecha).
4. Repite hacia abajo en el árbol (típicamente 1–5 operaciones de E/S) hasta llegar a una **página hoja**.
5. En la hoja, escanea las claves ordenadas para encontrar coincidencias, luego usa el RID para obtener la fila exacta de la tabla (una E/S más).

Esta compresión de ruta mantiene los recorridos superficiales. Para consultas de rango, una vez en la hoja de inicio, sigue los enlaces hermanos para escanear secuencialmente sin saltar hacia arriba en el árbol.

#### Inserción y Eliminación
- **Inserción**:
  1. Recorre hasta la hoja correcta (como en la búsqueda).
  2. Inserta la nueva clave + RID en la página hoja ordenada.
  3. Si la página se desborda (excede el máximo de entradas, ~200–500 dependiendo del tamaño de la clave), divídela en dos páginas e inserta una clave separadora en la página padre (interna).
  4. Si el padre se desborda, divide hacia arriba (puede crear una nueva raíz). DB2 bloquea páginas brevemente para concurrencia.

- **Eliminación**:
  1. Recorre hasta la hoja y elimina la clave + RID.
  2. Si la página se subabastece (muy pocas entradas), pide prestado a un hermano o se fusiona con él, eliminando la clave separadora del padre.
  3. Propaga fusiones hacia arriba si es necesario. DB2 puede retrasar la reorganización para agrupar cambios y mejorar la eficiencia.

Estas operaciones mantienen el balance automáticamente, con divisiones/fusiones de página mínimas (~1% de las operaciones).

#### Características específicas de DB2
- **Árboles B+ Optimizados** (en DB2 para z/OS): Mejorados para concurrencia en mainframe, con precarga fractal para predecir y precargar páginas, reduciendo la E/S.
- **Agrupamiento (Clustering)**: Los índices pueden estar "agrupados" (datos ordenados físicamente por orden de índice) para un mejor rendimiento en rangos.
- **Tipos**: Admite índices únicos, compuestos (multi-columna) y de mapa de bits, todos basados en B+. No hay índices hash nativos.
- **Mantenimiento**: Ejecuta `RUNSTATS` después de cambios masivos para actualizar las estadísticas para el optimizador. Herramientas como `INSPECT` verifican problemas.

Los árboles B+ sobresalen en DB2 porque minimizan la E/S aleatoria (clave para sistemas limitados por disco) y admiten acceso ordenado sin escaneos completos de tabla.

[Estructura de índice - IBM](https://www.ibm.com/docs/en/db2/11.1.0?topic=indexes-index-structure)  
[Índices de DB2 LUW: Detalles del Árbol B](https://datageek.blog/2013/09/19/db2-luw-basics-indexes/)  
[Inside Db2 for z/OS: Cómo los árboles B+ optimizados impulsan la indexación de alta velocidad](https://planetmainframe.com/2025/06/inside-db2-for-z-os-how-optimized-b-trees-power-high-speed-indexing/)  
[Cómo entender rápidamente el índice de árbol B de DB2](https://srinimf.com/2021/07/26/db2-how-to-understand-b-tree-structure-of-index/)  
[Descripción general del índice de Db2](https://www.idug.org/news/db2-index-overview)