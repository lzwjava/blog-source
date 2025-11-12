---
audio: false
generated: true
lang: fr
layout: post
title: Pilote JDBC Oracle
translated: true
type: note
---

Les pilotes Oracle JDBC (Java Database Connectivity) permettent aux applications Java de se connecter et d'interagir avec les bases de données Oracle. Laissez-moi vous expliquer les composants clés et leur utilisation.

La classe principale pour les connexions Oracle JDBC est `oracle.jdbc.driver.OracleDriver`, bien que dans les versions plus récentes, vous utiliserez souvent `oracle.jdbc.OracleDriver` (qui est la classe recommandée depuis Oracle 10g).

Voici comment utiliser Oracle JDBC dans une application Java :

1. Tout d'abord, vous devez inclure le pilote JDBC Oracle JAR dans votre projet (généralement ojdbc.jar).

2. Chargez la classe du pilote :
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. Établissez une connexion en utilisant une URL de connexion :
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// Ou pour une connexion basée sur le nom de service
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. Créez et exécutez des instructions :
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // Traiter chaque ligne
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. Fermez toujours les ressources lorsque vous avez terminé :
```java
resultSet.close();
statement.close();
connection.close();
```

Le pilote Oracle JDBC existe en plusieurs types :
- Pilote Thin : Implémentation pure Java qui ne nécessite pas d'installation client Oracle
- Pilote OCI : Utilise Oracle Call Interface et nécessite le logiciel client Oracle
- Pilote Kerberos : Pour l'authentification Kerberos
- Pilote JDBC-OCI : Combinaison de JDBC et OCI

Le pilote Thin est le plus couramment utilisé car il ne nécessite pas de logiciel client Oracle supplémentaire sur la machine cliente.

Souhaitez-vous des informations plus spécifiques sur le pool de connexions, les instructions préparées ou d'autres aspects de l'utilisation d'Oracle JDBC ?