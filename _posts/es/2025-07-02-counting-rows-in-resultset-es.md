---
audio: false
generated: true
lang: es
layout: post
title: Conteo de Filas en ResultSet Desplazable
translated: true
type: note
---

En Java, cuando trabajas con un `ResultSet` (por ejemplo, a través de `Statement.executeQuery()`), contar las filas puede ser complicado si el `fetchSize` está establecido en `0` (lo que significa que el controlador JDBC recuperará las filas según sea necesario). Además, usar un result set desplazable (usando `ResultSet.TYPE_SCROLL_INSENSITIVE` o `ResultSet.TYPE_SCROLL_SENSITIVE`) te permite navegar a través del result set pero requiere más memoria ya que las filas se cargan en la memoria.

Aquí hay una estrategia que puedes usar para contar filas en un `ResultSet` sin requerir un recorrido completo del result set. Utiliza la característica `scrollable` del `ResultSet` y la capacidad de "ir a la última fila" y "obtener el número de fila".

### Pasos para contar filas usando un `ResultSet` desplazable:

1.  **Crear un ResultSet desplazable**: Asegúrate de usar un `Statement` que pueda generar result sets desplazables estableciendo el tipo de cursor apropiado.
2.  **Mover a la última fila**: El result set desplazable te permite ir a la última fila usando `last()`.
3.  **Obtener el número de fila**: Después de moverte a la última fila, puedes llamar a `getRow()` para determinar el número de filas.
4.  **Opcional**: Si necesitas iterar a través del result set, regresa a la primera fila usando `first()`.

Aquí hay un ejemplo de implementación en Java:

```java
import java.sql.*;

public class RowCountExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/your_database";
        String username = "your_username";
        String password = "your_password";
        
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            conn = DriverManager.getConnection(url, username, password);
            stmt = conn.createStatement(
                    ResultSet.TYPE_SCROLL_INSENSITIVE, 
                    ResultSet.CONCUR_READ_ONLY);
            rs = stmt.executeQuery("SELECT * FROM your_table");
            
            // Mover a la última fila para contar el número total de filas
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // Opcionalmente, regresar a la primera fila
                rs.first();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Puntos Clave:

*   **ResultSet desplazable**: Creamos un `ResultSet` desplazable usando `ResultSet.TYPE_SCROLL_INSENSITIVE`. Este tipo de result set te permite moverte a la última fila y obtener el recuento de filas.
*   **Recuento de filas**: El método `rs.getRow()` devuelve el número de la fila actual cuando el cursor está posicionado en la última fila. Este valor es efectivamente el número total de filas en el result set.
*   **Fetch Size**: Si el `fetchSize` es `0`, el controlador recupera las filas dinámicamente, pero usar un result set desplazable nos permite navegar por las filas de manera eficiente.

### Mejores Prácticas:

*   **Eficiencia de memoria**: Si bien los result sets desplazables son útiles para contar filas, ten en cuenta que pueden consumir más memoria, ya que todas las filas deben cargarse en la memoria. Si estás trabajando con un conjunto de datos grande, considera usar un enfoque diferente (como iterar sobre el result set sin `last()` para contar las filas incrementalmente) si el uso de memoria es una preocupación.
*   **Enfoque alternativo**: Si la memoria es un problema y solo necesitas el recuento de filas, puedes ejecutar una consulta `SELECT COUNT(*)` en lugar de recuperar todo el result set. Esto suele ser más eficiente.

```sql
SELECT COUNT(*) FROM your_table;
```

¡Avísame si necesitas más aclaraciones!