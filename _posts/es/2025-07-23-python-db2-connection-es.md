---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Conexión de Python a IBM DB2
translated: true
type: note
---

### Resumen
IBM DB2 es un sistema de gestión de bases de datos relacional, y Python puede interactuar con él usando el paquete `ibm_db`, que proporciona una interfaz de bajo nivel, e `ibm_db_dbi`, un wrapper compatible con DB-API 2.0 que se sitúa sobre `ibm_db` para un uso más fácil y más "Pythónico". `ibm_db` es más directo y potente pero requiere un conocimiento más profundo, mientras que `ibm_db_dbi` imita el módulo `sqlite3` de Python, haciéndolo más simple para operaciones estándar de bases de datos. Ambos son parte de los controladores Python de IBM DB2.

### Instalación
Instala los paquetes usando pip:
```
pip install ibm_db
pip install ibm_db_dbi
```
Nota: Estos requieren una librería cliente de DB2. Para Windows/Linux, descarga e instala IBM Data Server Driver Package desde el sitio de IBM. En macOS, podría necesitar configuración adicional. Asegúrate de que tu servidor DB2 sea accesible (ej., ejecutándose en un host con credenciales).

### Usando ibm_db
`ibm_db` proporciona funciones para conectar, ejecutar sentencias y manejar resultados. No es compatible con DB-API pero ofrece más control.

#### Conexión Básica y Consulta
```python
import ibm_db

# Formato de cadena de conexión: DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Conectar
conn = ibm_db.connect(conn_str, "", "")

# Ejecutar una consulta
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# Obtener resultados (uno a la vez)
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # Devuelve un diccionario
    row = ibm_db.fetch_assoc(stmt)

# Cerrar
ibm_db.close(conn)
```
- **Funciones Clave**: `connect()`, `exec_immediate()` para consultas simples, `prepare()` y `execute()` para consultas parametrizadas y prevenir inyecciones.
- **Sentencias Preparadas**: Usa `prepare()` para compilar una consulta y `execute()` con parámetros.

#### Manejo de Errores
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"Error de conexión: {str(e)}")
```

### Usando ibm_db_dbi
`ibm_db_dbi` implementa DB-API 2.0, haciéndolo intercambiable con módulos como `sqlite3` o `psycopg2`.

#### Conexión Básica y Consulta
```python
import ibm_db_dbi

# Cadena de conexión similar a ibm_db
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Conectar
conn = ibm_db_dbi.connect(conn_str)

# Crear cursor
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM MYTABLE")

# Obtener resultados
rows = cursor.fetchall()  # Devuelve una lista de tuplas
for row in rows:
    print(row)

# Cerrar
cursor.close()
conn.close()
```
- **Consultas Parametrizadas**: `cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – usa ? como marcadores de posición.
- **Transacciones**: `conn.commit()` o `conn.rollback()`; el autocommit está desactivado por defecto.

### Diferencias Clave y Cuándo Usar Cada Uno

| Característica       | ibm_db                          | ibm_db_dbi                      |
|----------------------|---------------------------------|---------------------------------|
| Cumplimiento         | No DB-API (bajo nivel)          | Compatible con DB-API 2.0      |
| Facilidad de Uso     | Requiere más código; acceso directo | Sintaxis más simple, similar a Python |
| Rendimiento          | Potencialmente más rápido para operaciones complejas | Sobrecarga del wrapper         |
| Funcionalidad        | Todas las características de DB2 | Subconjunto vía interfaz DB-API |
| Caso de Uso          | Apps personalizadas que necesitan control total | Operaciones CRUD estándar      |

Usa `ibm_db_dbi` por familiaridad si estás acostumbrado a otros controladores DB-API. Cambia a `ibm_db` para características avanzadas específicas de DB2 como procedimientos almacenados u operaciones masivas.

### Mejores Prácticas
- Siempre maneja las excepciones y cierra las conexiones en un bloque `try-finally` o `with` para evitar fugas de recursos.
- Para conjuntos de resultados grandes, usa `fetchmany(size)` en lugar de `fetchall()` para limitar el uso de memoria.
- Verifica la compatibilidad de la versión de DB2; los paquetes soportan DB2 LUW, z/OS, iSeries.
- Consulta la documentación de IBM para temas avanzados como conexiones SSL o integración con CLPPlus.

Para más ejemplos, visita el [repositorio de controladores Python para IBM db2](https://github.com/ibmdb/python-ibmdb). Si encuentras problemas, asegúrate de que tu instancia de DB2 esté ejecutándose y las credenciales sean correctas.