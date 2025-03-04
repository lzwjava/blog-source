---
audio: false
generated: true
lang: en
layout: post
title: JNDI Datasource Configuration in WebSphere Liberty
translated: false
---

To determine whether an EAR Java program uses a datasource defined in the `server.xml` file in WebSphere Liberty, you need to verify if the application is accessing a datasource via a JNDI (Java Naming and Directory Interface) name that corresponds to a datasource configured in the server's configuration, specifically the `server.xml` file or any files it includes. Below is a step-by-step guide to help you confirm this:

### Step 1: Identify the JNDI Name Used by the Application
The first task is to find out which JNDI name the EAR application uses to look up its datasource. In a Java EE application deployed as an EAR file, this can be specified in several places:

- **Deployment Descriptors**: Check the application's deployment descriptors, such as `web.xml` (for web modules) or `ejb-jar.xml` (for EJB modules), for a `<resource-ref>` element. This element declares a resource reference that the application uses to access a datasource. For example:

  ```xml
  <resource-ref>
      <res-ref-name>jdbc/myDataSource</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>
  </resource-ref>
  ```

  Here, the application looks up the datasource using the JNDI name `java:comp/env/jdbc/myDataSource`.

- **Binding Files**: In WebSphere Liberty, the resource reference from the deployment descriptor might be bound to an actual JNDI name defined in the server through binding files like `ibm-web-bnd.xml` (for web modules) or `ibm-ejb-jar-bnd.xml` (for EJBs). Look for a `<resource-ref>` binding, such as:

  ```xml
  <resource-ref name="jdbc/myDataSource" binding-name="jdbc/actualDataSource"/>
  ```

  In this case, the application’s reference `jdbc/myDataSource` is mapped to the server’s JNDI name `jdbc/actualDataSource`.

- **Application Code**: If you have access to the source code, search for JNDI lookups or annotations:
  - **JNDI Lookup**: Look for code like:

    ```java
    Context ctx = new InitialContext();
    DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/myDataSource");
    ```

    This indicates the JNDI name `java:comp/env/jdbc/myDataSource`.

  - **Annotations**: In modern Java EE applications, the `@Resource` annotation might be used, such as:

    ```java
    @Resource(name = "jdbc/myDataSource")
    private DataSource ds;
    ```

    This also points to `java:comp/env/jdbc/myDataSource`.

If no binding file exists, the JNDI name in the code or deployment descriptor (e.g., `jdbc/myDataSource`) may directly correspond to the name expected in the server configuration.

### Step 2: Check the `server.xml` Configuration
Once you’ve identified the JNDI name the application uses (either directly or via a binding), check the WebSphere Liberty `server.xml` file (and any configuration files included via an `<include>` element) for a matching datasource definition. A datasource in `server.xml` is typically defined with a `<dataSource>` element, like this:

```xml
<dataSource id="myDataSource" jndiName="jdbc/myDataSource">
    <jdbcDriver libraryRef="myDBLib"/>
    <properties url="jdbc:mysql://localhost:3306/mydb" user="user" password="pass"/>
</dataSource>
```

- Look for the `jndiName` attribute (e.g., `jdbc/myDataSource`).
- Compare it to the JNDI name used by the application (e.g., `jdbc/myDataSource` or the bound name like `jdbc/actualDataSource`).

If the JNDI name matches, the application is using the datasource defined in `server.xml`.

### Step 3: Interpret the Results
- **Match Found**: If the JNDI name used by the application corresponds to a `<dataSource>` element in `server.xml` (or an included file), then the EAR Java program is using the `server.xml` datasource.
- **No Match**: If there’s no matching JNDI name in `server.xml`, the application might not be using a server-defined datasource. It could be creating its own datasource programmatically (e.g., using a JDBC driver directly with a URL, username, and password), though this is less common and not recommended in a managed environment like WebSphere Liberty.

### Additional Considerations
- **Included Configuration Files**: If `server.xml` uses `<include>` elements (e.g., `<include location="datasources.xml"/>`), check those files for datasource definitions.
- **Default Behavior**: If no binding file overrides the JNDI name, the application might assume the resource reference name (e.g., `jdbc/myDataSource`) matches a datasource in `server.xml`.
- **Server Logs or Tools**: While not directly part of the configuration check, you could also review server logs or use the WebSphere Liberty Admin Center to see which datasources are active and associated with the application, though this is more of a runtime verification.

### Conclusion
To confirm whether an EAR Java program uses the `server.xml` datasource in WebSphere Liberty:
1. Identify the JNDI name the application uses (via deployment descriptors, binding files, or code).
2. Verify if that JNDI name matches a datasource defined in `server.xml` or its included files.

If there’s a match, the application relies on the `server.xml` datasource; otherwise, it likely uses an alternative approach.