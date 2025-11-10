---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Guía de uso de secuencias de IBM DB2
translated: true
type: note
---

### Uso de Secuencias en IBM DB2 con NEXT VALUE FOR

En IBM DB2, `NEXT VALUE FOR` se utiliza para obtener el siguiente valor de una secuencia, la cual genera números únicos y crecientes. Las secuencias son útiles para generar claves primarias u otros identificadores únicos.

#### Ejemplo: Crear y Usar una Secuencia
1. **Crear la secuencia** (ejecuta esto una vez en tu entorno DB2):
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - Esto crea una secuencia llamada `my_sequence` que comienza en 1 y se incrementa en 1 cada vez.

2. **Usar la secuencia en una sentencia INSERT** para obtener el siguiente valor:
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - Esto inserta una nueva fila con `id` como el siguiente valor de la secuencia (por ejemplo, 1 para el primer uso, 2 para el siguiente, etc.).

#### Notas Clave
- También puedes usarlo en consultas SELECT: `SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- Las secuencias son independientes de las tablas y pueden compartirse entre varias tablas si es necesario.
- Para más detalles, consulta la documentación de IBM DB2 sobre secuencias. ¡Si necesitas ejemplos para otras funciones de secuencias como `PREVIOUS VALUE FOR`, házmelo saber!