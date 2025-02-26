---
audio: false
lang: es
layout: post
title: 'Liquibase: Gestión de Esquemas de Base de Datos'
translated: true
---

Aquí tienes una guía completa sobre **cómo usar Liquibase** en una aplicación Spring Boot para gestionar los cambios en el esquema de la base de datos de manera efectiva:

---

### 1. Agregar la Dependencia de Liquibase
Para comenzar, necesitas incluir la dependencia de Liquibase en tu proyecto. Si estás usando **Maven**, agrega esto a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
```

Para **Gradle**, agrega esto a tu `build.gradle`:

```groovy
implementation 'org.liquibase:liquibase-core'
```

Esto incorpora la biblioteca principal de Liquibase en tu proyecto.

---

### 2. Configurar Liquibase
Liquibase utiliza un **archivo de registro de cambios** para gestionar los cambios en el esquema de la base de datos. Por defecto, Spring Boot busca un archivo llamado `db/changelog/db.changelog-master.yaml`, `db/changelog/db.changelog-master.xml` o `db/changelog/db.changelog-master.sql` en el classpath. Puedes personalizar esta ubicación agregando una propiedad a tu `application.properties` (o `application.yml`):

```properties
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Esto le indica a Spring Boot dónde encontrar tu archivo de registro de cambios.

---

### 3. Crear un Archivo de Registro de Cambios
El archivo de registro de cambios define los cambios que deseas aplicar a tu base de datos. Puedes escribirlo en formatos como XML, YAML o SQL. Aquí tienes un ejemplo de un **archivo de registro de cambios en XML** ubicado en `src/main/resources/db/changelog/db.changelog-master.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.8.xsd">

    <changeSet id="1" author="your-name">
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

Este ejemplo crea una tabla `users` con tres columnas: `id`, `username` y `email`. Cada `<changeSet>` representa un conjunto de cambios para aplicar.

---

### 4. Ejecutar tu Aplicación Spring Boot
Cuando inicies tu aplicación Spring Boot, Liquibase automáticamente:
- Lee el archivo de registro de cambios.
- Verifica qué conjuntos de cambios ya se han aplicado (seguidos en una tabla llamada `DATABASECHANGELOG`).
- Ejecuta cualquier nuevo conjunto de cambios en tu base de datos.

No se necesita código adicional; la auto-configuración de Spring Boot se encarga de esto.

---

### 5. Personalizar Liquibase (Opcional)
Puedes ajustar el comportamiento de Liquibase utilizando propiedades en `application.properties`. Aquí tienes algunas opciones comunes:

```properties
spring.liquibase.enabled=true          # Habilitar o deshabilitar Liquibase
spring.liquibase.drop-first=false      # Eliminar la base de datos antes de aplicar cambios (usar con precaución)
spring.liquibase.contexts=dev,prod     # Ejecutar conjuntos de cambios solo en contextos específicos
```

Estas configuraciones te permiten adaptar Liquibase a tu entorno o flujo de trabajo.

---

### 6. Aprovechar Funciones Avanzadas
Liquibase ofrece potentes características para mejorar la gestión del esquema:
- **Contextos y Etiquetas**: Controla qué conjuntos de cambios se ejecutan en entornos específicos (por ejemplo, `dev` vs. `prod`).
- **Precondiciones**: Asegúrate de que ciertas condiciones (por ejemplo, que existe una tabla) se cumplan antes de aplicar un conjunto de cambios.
- **Deshacer**: Define cómo deshacer un conjunto de cambios si es necesario.
- **Refactorización**: Utiliza el soporte integrado para cambios complejos en la base de datos (por ejemplo, renombrar columnas).

Por ejemplo, agregar un contexto a un conjunto de cambios:

```xml
<changeSet id="2" author="your-name" context="dev">
    <addColumn tableName="users">
        <column name="created_at" type="timestamp"/>
    </addColumn>
</changeSet>
```

Este conjunto de cambios solo se ejecuta en el contexto `dev`.

---

### 7. Probar con una Base de Datos en Memoria
Para probar, combina Liquibase con una base de datos en memoria como H2. Agrega la dependencia de H2:

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

Luego, configura tu `application.properties` para pruebas:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.liquibase.change-log=classpath:/db/changelog/db.changelog-master.xml
```

Liquibase aplicará tus cambios a la base de datos en memoria durante las pruebas.

---

### 8. Control de Versiones del Registro de Cambios
Almacena tus archivos de registro de cambios en el control de versiones (por ejemplo, Git) junto con el código de tu aplicación. Esto asegura que el esquema de tu base de datos evolucione al mismo tiempo que tu base de código, haciendo que los despliegues y los deshacer sean más predecibles.

---

### Resumen
Para usar Liquibase en una aplicación Spring Boot:
1. Agrega la dependencia de Liquibase.
2. Configura la ubicación del archivo de registro de cambios.
3. Crea un archivo de registro de cambios con tus cambios en la base de datos.
4. Ejecuta tu aplicación; Liquibase se encarga del resto.

Liquibase es una herramienta robusta para gestionar los cambios en el esquema de la base de datos de manera estructurada y controlada por versiones, integrada sin problemas con Spring Boot.