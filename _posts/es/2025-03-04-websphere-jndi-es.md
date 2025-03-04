---
audio: true
generated: true
lang: es
layout: post
title: Configuración de JNDI Datasource en WebSphere Liberty
translated: true
---

Para determinar si un programa Java EAR utiliza un datasource definido en el archivo `server.xml` en WebSphere Liberty, debe verificar si la aplicación accede a un datasource a través de un nombre JNDI (Java Naming and Directory Interface) que corresponde a un datasource configurado en la configuración del servidor, específicamente en el archivo `server.xml` o en cualquier archivo que incluya. A continuación se presenta una guía paso a paso para ayudarle a confirmar esto:

### Paso 1: Identificar el Nombre JNDI Utilizado por la Aplicación
La primera tarea es averiguar qué nombre JNDI utiliza la aplicación EAR para buscar su datasource. En una aplicación Java EE desplegada como un archivo EAR, esto puede especificarse en varios lugares:

- **Descriptores de Despliegue**: Verifique los descriptores de despliegue de la aplicación, como `web.xml` (para módulos web) o `ejb-jar.xml` (para módulos EJB), para un elemento `<resource-ref>`. Este elemento declara una referencia de recurso que la aplicación utiliza para acceder a un datasource. Por ejemplo:

  ```xml
  <resource-ref>
      <res-ref-name>jdbc/myDataSource</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>
  </resource-ref>
  ```

  Aquí, la aplicación busca el datasource utilizando el nombre JNDI `java:comp/env/jdbc/myDataSource`.

- **Archivos de Vinculación**: En WebSphere Liberty, la referencia de recurso del descriptor de despliegue puede estar vinculada a un nombre JNDI real definido en el servidor a través de archivos de vinculación como `ibm-web-bnd.xml` (para módulos web) o `ibm-ejb-jar-bnd.xml` (para EJBs). Busque una vinculación `<resource-ref>`, como:

  ```xml
  <resource-ref name="jdbc/myDataSource" binding-name="jdbc/actualDataSource"/>
  ```

  En este caso, la referencia de la aplicación `jdbc/myDataSource` se mappa al nombre JNDI del servidor `jdbc/actualDataSource`.

- **Código de la Aplicación**: Si tiene acceso al código fuente, busque búsquedas JNDI o anotaciones:
  - **Búsqueda JNDI**: Busque código como:

    ```java
    Context ctx = new InitialContext();
    DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/myDataSource");
    ```

    Esto indica el nombre JNDI `java:comp/env/jdbc/myDataSource`.

  - **Anotaciones**: En aplicaciones Java EE modernas, puede utilizarse la anotación `@Resource`, como:

    ```java
    @Resource(name = "jdbc/myDataSource")
    private DataSource ds;
    ```

    Esto también apunta a `java:comp/env/jdbc/myDataSource`.

Si no existe un archivo de vinculación, el nombre JNDI en el código o en el descriptor de despliegue (por ejemplo, `jdbc/myDataSource`) puede corresponder directamente al nombre esperado en la configuración del servidor.

### Paso 2: Verificar la Configuración de `server.xml`
Una vez que haya identificado el nombre JNDI que utiliza la aplicación (ya sea directamente o a través de una vinculación), verifique el archivo `server.xml` de WebSphere Liberty (y cualquier archivo de configuración incluido a través de un elemento `<include>`) para una definición de datasource coincidente. Un datasource en `server.xml` generalmente se define con un elemento `<dataSource>`, como esto:

```xml
<dataSource id="myDataSource" jndiName="jdbc/myDataSource">
    <jdbcDriver libraryRef="myDBLib"/>
    <properties url="jdbc:mysql://localhost:3306/mydb" user="user" password="pass"/>
</dataSource>
```

- Busque el atributo `jndiName` (por ejemplo, `jdbc/myDataSource`).
- Compárelo con el nombre JNDI utilizado por la aplicación (por ejemplo, `jdbc/myDataSource` o el nombre vinculado como `jdbc/actualDataSource`).

Si el nombre JNDI coincide, la aplicación está utilizando el datasource definido en `server.xml`.

### Paso 3: Interpretar los Resultados
- **Coincidencia Encontrada**: Si el nombre JNDI utilizado por la aplicación corresponde a un elemento `<dataSource>` en `server.xml` (o en un archivo incluido), entonces el programa Java EAR está utilizando el datasource de `server.xml`.
- **Sin Coincidencia**: Si no hay un nombre JNDI coincidente en `server.xml`, la aplicación podría no estar utilizando un datasource definido por el servidor. Podría estar creando su propio datasource de manera programática (por ejemplo, utilizando un controlador JDBC directamente con una URL, nombre de usuario y contraseña), aunque esto es menos común y no se recomienda en un entorno gestionado como WebSphere Liberty.

### Consideraciones Adicionales
- **Archivos de Configuración Incluidos**: Si `server.xml` utiliza elementos `<include>` (por ejemplo, `<include location="datasources.xml"/>`), verifique esos archivos para definiciones de datasource.
- **Comportamiento Predeterminado**: Si ningún archivo de vinculación anula el nombre JNDI, la aplicación podría asumir que el nombre de referencia de recurso (por ejemplo, `jdbc/myDataSource`) coincide con un datasource en `server.xml`.
- **Registros del Servidor o Herramientas**: Aunque no forma parte de la verificación de configuración, también podría revisar los registros del servidor o utilizar el Centro de Administración de WebSphere Liberty para ver qué datasources están activos y asociados con la aplicación, aunque esto es más una verificación en tiempo de ejecución.

### Conclusión
Para confirmar si un programa Java EAR utiliza el datasource de `server.xml` en WebSphere Liberty:
1. Identifique el nombre JNDI que utiliza la aplicación (a través de descriptores de despliegue, archivos de vinculación o código).
2. Verifique si ese nombre JNDI coincide con un datasource definido en `server.xml` o en sus archivos incluidos.

Si hay una coincidencia, la aplicación depende del datasource de `server.xml`; de lo contrario, probablemente utiliza un enfoque alternativo.