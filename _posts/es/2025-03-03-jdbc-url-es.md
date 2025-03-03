---
audio: false
generated: true
lang: es
layout: post
title: jdbc:mysql://localhost:3306/mydatabase
translated: true
---

Para construir una URL JDBC para conectarse a una base de datos DB2 basada en el elemento `properties.db2.jcc` en el archivo `server.xml` de un perfil de WebSphere Liberty, necesitas usar los valores proporcionados para ciertos atributos clave, como `databaseName`, `serverName` y `portNumber`. Aquí te explico cómo hacerlo:

### Formato básico de URL JDBC para DB2
El formato estándar para una URL JDBC utilizando el controlador JDBC de tipo 4 de DB2 (que se usa comúnmente en configuraciones de Liberty Profile) es:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - Este es el identificador de protocolo para una base de datos DB2 utilizando el controlador de tipo 4, indicando una conexión de red directa.
- **`<serverName>`** - El nombre de host o la dirección IP del servidor DB2, especificado por el atributo `serverName` en `properties.db2.jcc`.
- **`<portNumber>`** - El puerto en el que la instancia de DB2 está escuchando, especificado por el atributo `portNumber` (el valor predeterminado es generalmente `50000` si no se especifica).
- **`<databaseName>`** - El nombre de la base de datos a la que se va a conectar, especificado por el atributo `databaseName`.

### Pasos para construir la URL
1. **Identificar las propiedades requeridas**: Del elemento `properties.db2.jcc` en `server.xml`, extrae los valores para `serverName`, `portNumber` y `databaseName`. Estos son los componentes esenciales necesarios para la URL.
2. **Montar la URL**: Combina estos valores en el formato anterior, asegurándote de usar los separadores adecuados (`:` entre el servidor y el puerto, `/` antes del nombre de la base de datos).
3. **Manejar propiedades adicionales (si están presentes)**: Si `properties.db2.jcc` incluye otros atributos (por ejemplo, `currentSchema`, `sslConnection`), a veces se pueden adjuntar a la URL, pero esto depende de su naturaleza. Normalmente, propiedades como `user` y `password` se pasan por separado al establecer la conexión, no en la URL, por razones de seguridad.

### Ejemplo
Supongamos que tu `server.xml` contiene la siguiente configuración `properties.db2.jcc`:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

La URL JDBC sería:

```
jdbc:db2://localhost:50000/SAMPLE
```

- El `user` y `password` no se incluyen en la URL; generalmente se proporcionan por separado al obtener una conexión a través del controlador JDBC (por ejemplo, a través de un `DataSource` o `DriverManager`).

### Incluir propiedades adicionales (opcional)
Si se especifican propiedades adicionales en `properties.db2.jcc`, como `currentSchema` o `sslConnection`, y deseas incluirlas en la URL (aunque algunas pueden configurarse mejor en las propiedades de conexión), adjúntalas después del nombre de la base de datos con un dos puntos (`:`) seguido de pares `property=value` separados por punto y coma. Por ejemplo:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

La URL podría ser:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

Sin embargo:
- Propiedades como `sslConnection=true` a menudo se establecen en un objeto `Properties` o en la configuración de la fuente de datos en lugar de en la URL.
- Consulta la documentación del controlador JDBC de DB2 para confirmar qué propiedades son válidas en la URL frente a las que requieren una configuración separada.

### Respuesta final
En el contexto de tu consulta, asumiendo que `properties.db2.jcc` proporciona al menos `databaseName`, `serverName` y `portNumber`, la URL JDBC se construye como:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

Reemplaza `<serverName>`, `<portNumber>` y `<databaseName>` con los valores reales de tu configuración `properties.db2.jcc`. Si hay propiedades adicionales presentes e intencionadas para la URL, adjúntalas como `:property1=value1;property2=value2;`, pero generalmente, propiedades como `user`, `password` y `sslConnection` se manejan por separado en la configuración de la conexión.