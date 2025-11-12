---
audio: false
generated: true
lang: es
layout: post
title: Controlador JDBC de Oracle
translated: true
type: note
---

Los controladores Oracle JDBC (Java Database Connectivity) permiten que las aplicaciones Java se conecten e interactúen con bases de datos Oracle. Permíteme explicar los componentes clave y cómo usarlos.

La clase principal para las conexiones Oracle JDBC es `oracle.jdbc.driver.OracleDriver`, aunque en versiones más nuevas a menudo se usa `oracle.jdbc.OracleDriver` (que es la clase recomendada desde Oracle 10g).

Así es como se usa Oracle JDBC en una aplicación Java:

1. Primero, necesitas incluir el JAR del controlador Oracle JDBC en tu proyecto (típicamente ojdbc.jar).

2. Cargar la clase del controlador:
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. Establecer una conexión usando una URL de conexión:
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// O para conexión basada en nombre de servicio
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. Crear y ejecutar sentencias:
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // Procesar cada fila
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. Siempre cerrar los recursos cuando termines:
```java
resultSet.close();
statement.close();
connection.close();
```

El controlador Oracle JDBC viene en varios tipos:
- Controlador Thin: Implementación pura en Java que no requiere instalación del cliente Oracle
- Controlador OCI: Usa Oracle Call Interface y requiere software cliente de Oracle
- Controlador Kerberos: Para autenticación Kerberos
- Controlador JDBC-OCI: Combinación de JDBC y OCI

El controlador Thin es el más comúnmente usado ya que no requiere software cliente adicional de Oracle en la máquina cliente.

¿Te gustaría obtener información más específica sobre connection pooling, prepared statements u otros aspectos del uso de Oracle JDBC?