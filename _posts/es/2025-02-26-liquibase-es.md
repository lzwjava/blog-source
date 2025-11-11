---
audio: false
generated: true
lang: es
layout: post
title: 'Liquibase: Gestión del Esquema de la Base de Datos'
translated: true
type: note
---

Aquí tienes una guía completa sobre **cómo usar Liquibase** en una aplicación Spring Boot para gestionar los cambios en el esquema de tu base de datos de manera efectiva:

---

### 1. Añadir la Dependencia de Liquibase
Para empezar, necesitas incluir la dependencia de Liquibase en tu proyecto. Si usas **Maven**, añade esto a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

Para **Gradle**, añade esto a tu `build.gradle`:

```groovy
implementation 'org.liquibase:liquibase-core'
```

Esto incorpora la librería core de Liquibase a tu proyecto.

---

### 2. Configurar Liquibase
Liquibase utiliza un **archivo changelog** para gestionar los cambios del esquema de la base de datos. Por defecto, Spring Boot busca un archivo llamado `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml`, o `db/changelog/db.changelog-master.sql` en el classpath. Puedes personalizar esta ubicación añadiendo una propiedad a tu `application.properties` (o `application.yml`):

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Esto le indica a Spring Boot dónde encontrar tu archivo changelog.

---

### 3. Crear un Archivo Changelog
El archivo changelog define los cambios que quieres aplicar a tu base de datos. Puedes escribirlo en formatos como XML, YAML o SQL. Aquí hay un ejemplo de un archivo **changelog en XML** ubicado en `src/main/resources/db/changelog/db.changelog-master.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="tu-nombre">
        <createTable tableName="users">
            <column name="id" type="int">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="username" type="varchar(255)"/>
            <column name="email" type="varchar(255)"/>
        </createTable>
    </changeSet>

</databaseChangeLog>
```

Este ejemplo crea una tabla `users` con tres columnas: `id`, `username` y `email`. Cada `<changeSet>` representa un conjunto de cambios a aplicar.

---

### 4. Ejecutar tu Aplicación Spring Boot
Cuando inicias tu aplicación Spring Boot, Liquibase automáticamente:
- Lee el archivo changelog.
- Verifica qué changesets ya han sido aplicados (seguidos en una tabla llamada `DATABASECHANGELOG`).
- Ejecuta cualquier changeset nuevo contra tu base de datos.

No se necesita código adicional—la auto-configuración de Spring Boot se encarga de esto por ti.

---

### 5. Personalizar Liquibase (Opcional)
Puedes ajustar el comportamiento de Liquibase usando propiedades en `application.properties`. Aquí hay algunas opciones comunes:

```properties
spring.liquibase.enabled=true          # Activar o desactivar Liquibase
spring.liquibase.drop-first=false      # Eliminar la base de datos antes de aplicar cambios (usar con precaución)
spring.liquibase.contexts=dev,prod     # Ejecutar changesets solo en contextos específicos
```

Estos ajustes te permiten adaptar Liquibase a tu entorno o flujo de trabajo.

---

### 6. Aprovechar Características Avanzadas
Liquibase ofrece características potentes para mejorar la gestión del esquema:
- **Contextos y Etiquetas**: Controla qué changesets se ejecutan en entornos específicos (ej. `dev` vs. `prod`).
- **Precondiciones**: Asegura que se cumplan ciertas condiciones (ej. que exista una tabla) antes de aplicar un changeset.
- **Rollbacks**: Define cómo deshacer un changeset si es necesario.
- **Refactorización**: Usa soporte incorporado para cambios complejos en la base de datos (ej. renombrar columnas).

Por ejemplo, añadir un contexto a un changeset:

```xml
<changeSet id="2" author="tu-nombre" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

Este changeset solo se ejecuta en el contexto `dev`.

---

### 7. Probar con una Base de Datos en Memoria
Para pruebas, combina Liquibase con una base de datos en memoria como H2. Añade la dependencia de H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

Luego configura tu `application.properties` para pruebas:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase aplicará tus cambios a la base de datos en memoria durante las pruebas.

---

### 8. Control de Versiones de tu Changelog
Almacena tus archivos changelog en un sistema de control de versiones (ej. Git) junto con el código de tu aplicación. Esto asegura que tu esquema de base de datos evolucione al mismo tiempo que tu base de código, haciendo los despliegues y rollbacks más predecibles.

---

### Resumen
Para usar Liquibase en una aplicación Spring Boot:
1. Añade la dependencia de Liquibase.
2. Configura la ubicación del archivo changelog.
3. Crea un archivo changelog con tus cambios de base de datos.
4. Ejecuta tu aplicación—Liquibase se encarga del resto.

Liquibase es una herramienta robusta para gestionar cambios en el esquema de la base de datos de manera estructurada y controlada por versiones, integrada perfectamente con Spring Boot.