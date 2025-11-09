---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Creación de Índices en IBM DB2
translated: true
type: note
---

### Creación de índices en IBM DB2

IBM DB2 admite índices para optimizar el rendimiento de las consultas al permitir una recuperación más rápida de los datos. Los índices se pueden crear en una o más columnas de una tabla. A continuación, se explican los conceptos básicos, incluyendo índices únicos e índices multicolumna (compuestos). Ten en cuenta que "índice de unión" no es un término estándar en la documentación de DB2; podría referirse a un índice compuesto (que abarca múltiples claves) o a un malentendido sobre las operaciones de unión en las consultas. Si te referías a otra cosa, ¡proporciona más detalles!

#### Creación básica de un índice
Utiliza la sentencia `CREATE INDEX` para construir un índice simple en una sola columna. Esto acelera las búsquedas, ordenaciones y combinaciones (joins) en esa columna.

**Sintaxis:**
```sql
CREATE INDEX nombre_indice
ON nombre_tabla (nombre_columna [ASC | DESC]);
```

**Ejemplo:**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` ordena en orden ascendente (por defecto); usa `DESC` para descendente.
- Por defecto, los índices no son únicos, permitiendo valores duplicados.

#### Índice único (Aplicación de claves únicas)
Un índice único garantiza que no haya valores duplicados en la(s) columna(s) indexada(s), similar a una restricción única. DB2 crea automáticamente un índice único cuando defines una clave primaria o una restricción única.

**Sintaxis:**
```sql
CREATE UNIQUE INDEX nombre_indice
ON nombre_tabla (nombre_columna [ASC | DESC]);
```

**Ejemplo:**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- Esto evita la inserción de emails duplicados.
- Para unicidad parcial (ej., ignorar NULLs), añade `WHERE NOT NULL`:  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- Puedes incluir columnas que no son claves para la cobertura de la consulta:  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### Índice compuesto (Múltiples claves, ej., dos o más columnas)
Un índice compuesto (o multicolumna) abarca múltiples claves, útil para consultas que filtran o combinan basándose en combinaciones de columnas. El orden de las columnas es importante—coloca la columna más selectiva primero.

**Sintaxis:**
```sql
CREATE INDEX nombre_indice
ON nombre_tabla (columna1 [ASC | DESC], columna2 [ASC | DESC], ...);
```

**Ejemplo (Dos claves):**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- Esto optimiza consultas como `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;`.
- Para un índice compuesto único: Añade `UNIQUE` (ej., `CREATE UNIQUE INDEX ...`).

#### Consejos adicionales
- **Verificar índice:** Usa `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'TU_ESQUEMA' AND TABNAME = 'TU_TABLA';`.
- **Eliminar índice:** `DROP INDEX nombre_indice;`.
- Los índices consumen almacenamiento y ralentizan inserciones/actualizaciones—úsalos con criterio.
- Para tablas particionadas u opciones avanzadas (ej., clustering), consulta la documentación de DB2.

[Db2 CREATE INDEX Statement](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 Unique Indexes](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 Composite Indexes Example](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 Unique Index Tutorial](https://www.db2tutorial.com/db2-index/db2-unique-index/)