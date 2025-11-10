---
audio: false
generated: true
lang: es
layout: post
title: Java SQL Para Conectividad De Base De Datos
translated: true
type: note
---

El paquete `java.sql` es una **parte fundamental de la API JDBC de Java (Java Database Connectivity)**, que permite a las aplicaciones Java interactuar con bases de datos relacionales como MySQL, PostgreSQL, Oracle, SQL Server y otras. Proporciona las interfaces y clases necesarias para **conectarse a una base de datos, ejecutar consultas SQL y recuperar resultados**.

---

## 📘 **Descripción general de `java.sql`**

El paquete `java.sql` incluye clases e interfaces para:

* Conectarse a bases de datos (`DriverManager`, `Connection`)
* Ejecutar consultas SQL (`Statement`, `PreparedStatement`, `CallableStatement`)
* Procesar resultados (`ResultSet`)
* Manejar metadatos (`DatabaseMetaData`, `ResultSetMetaData`)
* Gestionar transacciones
* Manejar excepciones SQL (`SQLException`)

---

## 🔧 **Configuración: Lo que necesitas**

### 1. **Controlador JDBC**

* Necesitas un controlador JDBC para tu base de datos objetivo (por ejemplo, MySQL: `mysql-connector-java`, PostgreSQL: `postgresql`).
* Puedes incluirlo vía Maven/Gradle o añadir manualmente el archivo `.jar`.

### 2. **URL de la base de datos**

Cada controlador JDBC tiene un formato de URL de conexión:

```java
jdbc:mysql://localhost:3306/mydatabase
jdbc:postgresql://localhost:5432/mydatabase
```

---

## 🧩 **Clases e interfaces clave**

### 🔌 1. `DriverManager`

Establece una conexión a una base de datos.

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

### 🧵 2. `Connection`

Representa una sesión con una base de datos.

* Crear `Statement` o `PreparedStatement`
* Gestionar transacciones (commit, rollback)
* Cerrar la conexión

```java
Connection conn = DriverManager.getConnection(...);
conn.setAutoCommit(false);  // para control manual de transacciones
```

### 📤 3. `Statement` / `PreparedStatement` / `CallableStatement`

#### `Statement`

Se utiliza para ejecutar consultas SQL estáticas.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

#### `PreparedStatement`

Se utiliza para ejecutar consultas parametrizadas. Evita la inyección SQL.

```java
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, 101);
ResultSet rs = ps.executeQuery();
```

#### `CallableStatement`

Se utiliza para procedimientos almacenados.

```java
CallableStatement cs = conn.prepareCall("{call getUser(?)}");
cs.setInt(1, 5);
ResultSet rs = cs.executeQuery();
```

### 📥 4. `ResultSet`

Contiene el resultado de una consulta.

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}
```

### 📚 5. Metadatos

* `DatabaseMetaData`: Información sobre la base de datos
* `ResultSetMetaData`: Información sobre las columnas del resultado

```java
DatabaseMetaData dbMeta = conn.getMetaData();
ResultSetMetaData rsMeta = rs.getMetaData();
```

---

## 🧪 **Ejemplo básico**

```java
import java.sql.*;

public class JdbcExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            String sql = "SELECT * FROM users WHERE age > ?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setInt(1, 18);

            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " - " + rs.getString("name"));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🔁 **Transacciones**

```java
conn.setAutoCommit(false);  // Deshabilitar auto-commit

try {
    PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    ps1.setDouble(1, 100.0);
    ps1.setInt(2, 1);
    ps1.executeUpdate();

    PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    ps2.setDouble(1, 100.0);
    ps2.setInt(2, 2);
    ps2.executeUpdate();

    conn.commit(); // Confirmar la transacción

} catch (SQLException ex) {
    conn.rollback(); // Revertir en caso de error
}
```

---

## ❗ **Manejo de excepciones**

```java
try {
    // Código de base de datos
} catch (SQLException ex) {
    System.err.println("Código de Error: " + ex.getErrorCode());
    System.err.println("Estado SQL: " + ex.getSQLState());
    ex.printStackTrace();
}
```

---

## 🧰 **Características útiles en `java.sql`**

| Característica         | Interfaz/Clase                      | Propósito                                                              |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------- |
| Metadatos              | `DatabaseMetaData`                  | Versión de la BD, características admitidas, tablas, etc.              |
| Información de columnas| `ResultSetMetaData`                 | Número de columnas, tipo, etiqueta, etc.                               |
| Manejo de BLOB/CLOB    | `Blob`, `Clob`                      | Almacenar/recuperar datos binarios o de texto grandes                  |
| Ejecución por lotes    | `addBatch()`, `executeBatch()`      | Ejecutar muchas sentencias juntas                                      |
| ResultSet desplazable  | `ResultSet.TYPE_SCROLL_INSENSITIVE` | Mover el cursor hacia adelante y hacia atrás                           |
| ResultSet actualizable | `ResultSet.CONCUR_UPDATABLE`        | Modificar filas directamente en el `ResultSet`                         |

---

## 📦 **Ejemplo de dependencia Maven (MySQL)**

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.33</version>
</dependency>
```

---

## 🧠 **Mejores prácticas**

* Siempre cierra `Connection`, `Statement`, `ResultSet` en un bloque `finally` o usa try-with-resources.
* Usa `PreparedStatement` en lugar de `Statement` para prevenir la inyección SQL.
* Usa agrupamiento de conexiones en producción (a través de bibliotecas como HikariCP, Apache DBCP).
* Usa transacciones para consultas múltiples relacionadas.
* No codifiques SQL directamente en la lógica de negocio — considera patrones DAO u ORM (como JPA, Hibernate).

---

## 🧮 **Temas avanzados**

* **RowSet**: Versión desconectada de ResultSet (`javax.sql.rowset`)
* **Agrupamiento de conexiones**: Usa `DataSource` con grupos
* **Características de JDBC 4+**: Carga automática de controladores, soporte para try-with-resources
* **JDBC + Spring**: Integración con Spring JDBC Template
* **JDBC + ORM**: Usa `java.sql` por debajo de Hibernate, JPA, MyBatis

---

## 🧾 **Tabla resumen**

| Tarea                  | Clase/Interfaz                      |
| ---------------------- | ----------------------------------- |
| Conectarse a la BD     | `DriverManager`, `Connection`       |
| Ejecutar SQL           | `Statement`, `PreparedStatement`    |
| Procedimientos almacenados | `CallableStatement`             |
| Leer resultados        | `ResultSet`                         |
| Información de la BD   | `DatabaseMetaData`                  |
| Información de columnas| `ResultSetMetaData`                 |
| Transacciones          | `Connection.commit()`, `rollback()` |
| Manejo de excepciones  | `SQLException`                      |

---

Si lo deseas, también puedo proporcionar:

* Una hoja de referencia rápida
* Una clase wrapper reutilizable estilo DAO
* Ejemplos con una base de datos real (MySQL/PostgreSQL)

¡Avísame!