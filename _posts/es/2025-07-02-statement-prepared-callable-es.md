---
audio: false
generated: true
lang: es
layout: post
title: Tipos de Declaraciones SQL de Java Comparados
translated: true
type: note
---

En el paquete `java.sql` de Java, `Statement`, `PreparedStatement` y `CallableStatement` son interfaces utilizadas para ejecutar consultas SQL, pero tienen propósitos diferentes y características distintas. Aquí tienes una comparación concisa:

1. **Statement**:
   - **Propósito**: Se utiliza para ejecutar consultas SQL estáticas sin parámetros.
   - **Cómo funciona**: Pasas una consulta SQL completa como cadena de texto a los métodos `executeQuery()` o `executeUpdate()`.
   - **Características Clave**:
     - Adecuado para consultas simples y únicas.
     - No tiene enlace de parámetros, por lo que concatenas manualmente los valores en la cadena SQL, lo que puede generar riesgos de inyección SQL.
     - Menos eficiente para consultas repetidas, ya que la base de datos re-analiza el SQL cada vez.
   - **Ejemplo**:
     ```java
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = 1");
     ```

2. **PreparedStatement**:
   - **Propósito**: Se utiliza para consultas SQL precompiladas con entradas parametrizadas.
   - **Cómo funciona**: Defines una consulta con marcadores de posición (`?`) y estableces los valores de los parámetros usando métodos como `setInt()`, `setString()`, etc.
   - **Características Clave**:
     - Previene la inyección SQL al separar la lógica SQL de los datos.
     - Más eficiente para consultas repetidas, ya que el SQL se compila una vez y se reutiliza.
     - Admite el enlace dinámico de parámetros, haciéndolo más seguro y flexible.
   - **Ejemplo**:
     ```java
     PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     pstmt.setInt(1, 1);
     ResultSet rs = pstmt.executeQuery();
     ```

3. **CallableStatement**:
   - **Propósito**: Se utiliza para ejecutar stored procedures en la base de datos.
   - **Cómo funciona**: Extiende `PreparedStatement` para manejar llamadas a stored procedures, admitiendo parámetros de entrada (`IN`), salida (`OUT`) y entrada/salida (`IN OUT`).
   - **Características Clave**:
     - Diseñado específicamente para stored procedures de bases de datos.
     - Permite el registro de parámetros de salida usando métodos como `registerOutParameter()`.
     - Admite el manejo de parámetros complejos para la lógica de los stored procedures.
   - **Ejemplo**:
     ```java
     CallableStatement cstmt = conn.prepareCall("{call getUserName(?, ?)}");
     cstmt.setInt(1, 1);
     cstmt.registerOutParameter(2, Types.VARCHAR);
     cstmt.execute();
     String username = cstmt.getString(2);
     ```

**Diferencias Clave**:
| Característica         | Statement                          | PreparedStatement                  | CallableStatement                 |
|------------------------|------------------------------------|------------------------------------|------------------------------------|
| **Propósito**          | Consultas SQL estáticas           | Consultas SQL parametrizadas      | Ejecución de stored procedures   |
| **Inyección SQL**      | Vulnerable (concatenación manual) | Seguro (enlace de parámetros)     | Seguro (enlace de parámetros)    |
| **Rendimiento**        | Menos eficiente (sin precompilación)| Más eficiente (precompilado)      | Eficiente para stored procedures |
| **Caso de Uso**        | Consultas simples y únicas        | Consultas repetitivas o parametrizadas | Stored procedures con parámetros|
| **Soporte de Parámetros**| Ninguno                          | Solo parámetros de entrada        | Parámetros IN, OUT e IN/OUT      |

**Cuándo Usar**:
- Usa `Statement` para consultas simples y no repetitivas donde la seguridad y el rendimiento son menos críticos.
- Usa `PreparedStatement` para consultas parametrizadas, ejecución repetitiva o cuando la prevención de inyección SQL sea una preocupación.
- Usa `CallableStatement` cuando invoques stored procedures de la base de datos con parámetros de entrada/salida.

Esta explicación se basa en el comportamiento estándar de la API SQL de Java según mi fecha de corte de conocimiento. ¡Si necesitas más detalles o ejemplos, házmelo saber