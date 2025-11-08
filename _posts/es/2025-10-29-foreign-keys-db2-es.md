---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Creación de Claves Foráneas en Db2
translated: true
type: note
---

### Creación de Claves Foráneas en IBM Db2

Las claves foráneas en Db2 hacen cumplir la integridad referencial vinculando una columna (o conjunto de columnas) en una tabla (la tabla hija) con la clave primaria o única en otra tabla (la tabla padre). Esto garantiza que los valores en la tabla hija coincidan con los valores existentes en la tabla padre, evitando registros huérfanos.

Puedes definir claves foráneas durante la creación de la tabla usando `CREATE TABLE` o agregándolas a una tabla existente usando `ALTER TABLE`. La sintaxis es SQL estándar y funciona en todas las plataformas Db2 (por ejemplo, LUW, z/OS).

#### 1. Definir una Clave Foránea Durante la Creación de la Tabla (`CREATE TABLE`)
Utiliza la cláusula `FOREIGN KEY` dentro de las definiciones de columna o al final de la definición de la tabla.

**Sintaxis Básica:**
```
CREATE TABLE tabla_hija (
    columna_hija1 tipo_de_dato,
    columna_clave_foranea tipo_de_dato,
    -- Otras columnas...
    CONSTRAINT nombre_restriccion
    FOREIGN KEY (columna_clave_foranea) 
    REFERENCES tabla_padre (columna_clave_padre)
);
```

**Ejemplo:**
Supongamos que tienes una tabla `departments` con una clave primaria `dept_id`:
```
CREATE TABLE departments (
    dept_id INTEGER NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

Ahora crea una tabla `employees` con una clave foránea que referencia `dept_id`:
```
CREATE TABLE employees (
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INTEGER,
    CONSTRAINT fk_emp_dept 
    FOREIGN KEY (dept_id) 
    REFERENCES departments (dept_id)
);
```

Esto crea una clave foránea llamada `fk_emp_dept` en `dept_id` en la tabla `employees`.

#### 2. Agregar una Clave Foránea a una Tabla Existente (`ALTER TABLE`)
Usa `ALTER TABLE` para agregar la restricción después de que la tabla existe. La clave padre ya debe existir.

**Sintaxis Básica:**
```
ALTER TABLE tabla_hija 
ADD CONSTRAINT nombre_restriccion 
FOREIGN KEY (columna_clave_foranea) 
REFERENCES tabla_padre (columna_clave_padre);
```

**Ejemplo:**
Para agregar la misma clave foránea a una tabla `employees` existente:
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id);
```

#### Opciones Adicionales
Puedes especificar acciones para lo que sucede cuando una fila padre se actualiza o elimina:
- `ON DELETE CASCADE`: Elimina las filas hijas cuando se elimina la padre.
- `ON DELETE SET NULL`: Establece la clave foránea en NULL en las filas hijas.
- `ON UPDATE CASCADE`: Actualiza las claves hijas cuando la clave padre cambia.
- `ON UPDATE SET NULL`: Establece a NULL cuando se actualiza la clave padre.

**Ejemplo con Opciones:**
```
ALTER TABLE employees 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) 
REFERENCES departments (dept_id)
ON DELETE CASCADE
ON UPDATE RESTRICT;
```

#### Reglas y Consideraciones Clave
- Las columnas de la clave foránea deben coincidir con el tipo de dato y la longitud de las columnas de la clave padre.
- La tabla padre debe tener una clave primaria o única definida antes de crear la clave foránea.
- Las claves foráneas pueden hacer referencia a la misma tabla (autorreferencial).
- Múltiples columnas pueden formar una clave foránea compuesta: `FOREIGN KEY (col1, col2) REFERENCES padre (pk1, pk2)`.
- Para eliminar una clave foránea: `ALTER TABLE tabla_hija DROP CONSTRAINT nombre_restriccion;`.
- Se recomienda crear un índice en las columnas de la clave foránea para mejorar el rendimiento.

Prueba en un entorno de desarrollo, ya que agregar restricciones puede fallar si los datos existentes las violan (por ejemplo, filas huérfanas).

#### Referencias
- [Foreign key (referential) constraints - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=constraints-foreign-key-referential)
- [CREATE TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-create-table)
- [ALTER TABLE statement - Db2 11.5](https://www.ibm.com/docs/en/db2/11.5.x?topic=statements-alter-table)
- [Adding a foreign key with Db2 - Stack Overflow](https://stackoverflow.com/questions/59370149/adding-a-foreign-key-with-db2-of-ibm)