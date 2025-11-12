---
audio: false
generated: true
lang: es
layout: post
title: Declaraciones SELECT de SQL
translated: true
type: note
---

Para responder a tu consulta sobre cómo usar `SELECT`, `LEFT JOIN`, `RIGHT JOIN`, `SELECT` complejo, `FROM`, `GROUP BY`, `WHERE NOT IN` e `IN` en SQL, explicaré cada componente claramente y proporcionaré ejemplos prácticos. Estas son operaciones fundamentales de SQL utilizadas para recuperar y manipular datos de bases de datos. Desglosémoslas paso a paso, usando un esquema de base de datos simple para mayor consistencia:

- **Tablas:**
  - `employees` (columnas: `employee_id`, `employee_name`, `department_id`, `salary`)
  - `departments` (columnas: `department_id`, `department_name`)
  - `projects` (columnas: `project_id`, `project_name`, `employee_id`)

---

### 1. SELECT
La cláusula `SELECT` se utiliza para especificar las columnas que deseas recuperar de una tabla de la base de datos. Forma la base de cualquier consulta SQL.

- **Propósito:** Elegir qué datos mostrar.
- **Ejemplo:**
  ```sql
  SELECT employee_name, salary
  FROM employees;
  ```
  Esto recupera las columnas `employee_name` y `salary` de la tabla `employees`.

---

### 2. FROM
La cláusula `FROM` identifica la tabla (o tablas) de la que se extraerán los datos. Siempre se usa con `SELECT`.

- **Propósito:** Especificar la fuente de datos.
- **Ejemplo:**
  ```sql
  SELECT employee_name
  FROM employees;
  ```
  Aquí, `employees` es la tabla que se consulta.

---

### 3. LEFT JOIN
Un `LEFT JOIN` (o `LEFT OUTER JOIN`) combina filas de dos tablas. Devuelve todos los registros de la tabla izquierda y los registros coincidentes de la tabla derecha. Si no hay coincidencia, el resultado incluye valores `NULL` para las columnas de la tabla derecha.

- **Propósito:** Incluir todas las filas de la tabla izquierda, independientemente de las coincidencias en la tabla derecha.
- **Ejemplo:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Esto lista todos los empleados y sus nombres de departamento. Si un empleado no está asignado a un departamento, `department_name` será `NULL`.

---

### 4. RIGHT JOIN
Un `RIGHT JOIN` (o `RIGHT OUTER JOIN`) es similar a un `LEFT JOIN`, pero devuelve todos los registros de la tabla derecha y los registros coincidentes de la tabla izquierda. Las filas de la tabla izquierda que no coincidan resultarán en valores `NULL`.

- **Propósito:** Incluir todas las filas de la tabla derecha, independientemente de las coincidencias en la tabla izquierda.
- **Ejemplo:**
  ```sql
  SELECT e.employee_name, d.department_name
  FROM employees e
  RIGHT JOIN departments d
  ON e.department_id = d.department_id;
  ```
  Esto muestra todos los departamentos y sus empleados. Los departamentos sin empleados tendrán `NULL` en `employee_name`.

---

### 5. SELECT Complejo
Un "`SELECT` complejo" no es un término formal de SQL, pero típicamente se refiere a una sentencia `SELECT` que combina múltiples cláusulas, joins, subconsultas o funciones de agregación para realizar una recuperación de datos avanzada.

- **Propósito:** Manejar consultas intrincadas que involucran múltiples operaciones.
- **Ejemplo:**
  ```sql
  SELECT d.department_name, COUNT(e.employee_id) AS employee_count
  FROM departments d
  LEFT JOIN employees e
  ON d.department_id = e.department_id
  GROUP BY d.department_name
  HAVING COUNT(e.employee_id) > 5;
  ```
  Esto encuentra departamentos con más de 5 empleados, contando empleados por departamento y filtrando los resultados.

---

### 6. GROUP BY
La cláusula `GROUP BY` agrupa filas que tienen los mismos valores en columnas especificadas en filas de resumen, a menudo utilizada con funciones de agregación como `COUNT`, `SUM` o `AVG`.

- **Propósito:** Agregar datos basándose en los valores de las columnas.
- **Ejemplo:**
  ```sql
  SELECT department_id, COUNT(employee_id) AS employee_count
  FROM employees
  GROUP BY department_id;
  ```
  Esto cuenta el número de empleados en cada departamento.

---

### 7. WHERE NOT IN
La cláusula `WHERE NOT IN` filtra las filas donde el valor de una columna no está presente en una lista especificada o en el resultado de una subconsulta. Ten cuidado: si la lista/subconsulta incluye `NULL`, es posible que no se devuelva ninguna fila.

- **Propósito:** Excluir filas basándose en un conjunto de valores.
- **Ejemplo:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (1, 2);
  ```
  Esto recupera empleados que no están en los departamentos 1 o 2.

- **Con Subconsulta:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id NOT IN (SELECT department_id FROM departments WHERE department_name = 'Inactive');
  ```
  Esto encuentra empleados que no están en departamentos marcados como 'Inactive'.

---

### 8. IN
La cláusula `IN` filtra las filas donde el valor de una columna coincide con cualquier valor de una lista o subconsulta. Es una forma abreviada de múltiples condiciones `OR`.

- **Propósito:** Incluir filas basándose en un conjunto de valores.
- **Ejemplo:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (3, 4);
  ```
  Esto recupera empleados en los departamentos 3 o 4.

- **Con Subconsulta:**
  ```sql
  SELECT employee_name
  FROM employees
  WHERE department_id IN (
      SELECT department_id
      FROM employees
      GROUP BY department_id
      HAVING COUNT(employee_id) > 5
  );
  ```
  Esto encuentra empleados en departamentos con más de 5 empleados.

---

### Uniendo Todo
Aquí tienes un ejemplo que combina varias de estas operaciones:
```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id NOT IN (1, 2)
GROUP BY d.department_name;
```
- **Explicación:**
  - `FROM departments d`: Comienza con la tabla `departments`.
  - `LEFT JOIN employees e`: Incluye todos los departamentos, incluso aquellos sin empleados.
  - `WHERE NOT IN (1, 2)`: Excluye empleados de los departamentos 1 y 2.
  - `GROUP BY d.department_name`: Agrupa los resultados por nombre de departamento.
  - `SELECT ... COUNT`: Cuenta empleados por departamento.

---

### Consejos Clave
- **Joins:** Elige `LEFT JOIN` o `RIGHT JOIN` basándote en qué filas de la tabla quieres mantener completamente (izquierda o derecha).
- **NULLs con NOT IN:** Si una subconsulta devuelve `NULL`, `NOT IN` puede excluir todas las filas inesperadamente. Considera `NOT EXISTS` como una alternativa.
- **Consultas Complejas:** Divídelas en partes (por ejemplo, prueba los joins por separado) para asegurar la corrección.
- **El Orden Importa:** Coloca `WHERE` antes de `GROUP BY`, y usa `HAVING` después de `GROUP BY` para filtros a nivel de grupo.

Al entender y combinar estos componentes de SQL—`SELECT`, `FROM`, `LEFT JOIN`, `RIGHT JOIN`, `GROUP BY`, `WHERE NOT IN` e `IN`—puedes elaborar consultas para recuperar y analizar datos efectivamente de cualquier base de datos relacional.