---
audio: false
generated: true
image: false
lang: es
layout: post
title: Declaración vs CallableStatement en JDBC
translated: true
type: note
---

En JDBC de Java (y otros frameworks construidos sobre él, como Hibernate o Spring), los conceptos de **`Statement`** y **`CallableStatement`** son ambas interfaces utilizadas para enviar comandos SQL a la base de datos, pero sirven para propósitos diferentes.

---

### 1. `Statement`

* **Propósito**: Se utiliza para ejecutar consultas SQL simples sin parámetros.
* **Uso**: Se crea un objeto `Statement` a partir de una `Connection` y se usa para ejecutar cadenas SQL.
* **Métodos típicos**:

  * `executeQuery(sql)` → para consultas `SELECT`, devuelve un `ResultSet`.
  * `executeUpdate(sql)` → para `INSERT`, `UPDATE`, `DELETE`.
  * `execute(sql)` → genérico, devuelve `true` si el resultado es un `ResultSet`.

**Ejemplo**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM employees");

while (rs.next()) {
    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
}
```

* **Cuándo usarlo**: Para sentencias SQL estáticas sin parámetros.
* **Desventaja**: Puede conducir a inyección SQL si se usa con entrada dinámica del usuario.

---

### 2. `CallableStatement`

* **Propósito**: Se utiliza para ejecutar **procedimientos almacenados** en la base de datos.
* **Uso**: Se crea con `Connection.prepareCall()` y permite llamar a rutinas de la base de datos con parámetros **IN**, **OUT** e **INOUT**.
* **Métodos típicos**:

  * `setInt`, `setString`, etc. → para establecer parámetros de entrada.
  * `registerOutParameter` → para registrar parámetros de salida.
  * `execute()` o `executeQuery()` → para ejecutar el procedimiento almacenado.
  * `getInt`, `getString`, etc. → para recuperar valores de salida.

**Ejemplo**:

```java
Connection conn = DriverManager.getConnection(url, user, pass);
CallableStatement cstmt = conn.prepareCall("{call getEmployeeName(?, ?)}");

// Establecer parámetro IN
cstmt.setInt(1, 101);

// Registrar parámetro OUT
cstmt.registerOutParameter(2, java.sql.Types.VARCHAR);

// Ejecutar
cstmt.execute();

// Obtener parámetro OUT
String empName = cstmt.getString(2);
System.out.println("Employee name: " + empName);
```

* **Cuándo usarlo**: Para procedimientos/funciones almacenados que encapsulan lógica en la base de datos.
* **Ventajas**: Soporta lógica compleja, múltiples resultados, parámetros de entrada/salida.

---

### Diferencias Clave (sin tabla)

* `Statement` es para **SQL estático** (consultas ad-hoc).
* `CallableStatement` es para **procedimientos/funciones almacenados**.
* `Statement` ejecuta SQL directamente, mientras que `CallableStatement` interactúa con rutinas de la base de datos que pueden devolver múltiples conjuntos de resultados y parámetros.
* `Statement` es simple pero menos seguro con entrada dinámica, mientras que `CallableStatement` proporciona una forma estructurada de llamar a lógica reutilizable almacenada en la DB.

---

👉 Si quieres, también puedo explicar cómo **`PreparedStatement`** se sitúa entre estos dos (SQL parametrizado más seguro, pero no para procedimientos almacenados). ¿Te gustaría que añada eso?