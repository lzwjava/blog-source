---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Integración de Liquibase con Spring Boot
translated: true
type: note
---

## Integración de Liquibase con Spring Boot

Liquibase es una herramienta de código abierto popular para gestionar cambios de esquema de base de datos (migraciones) de manera controlada por versiones. Spring Boot proporciona un excelente soporte de auto-configuración para Liquibase, facilitando su integración. Esta guía asume que estás usando Spring Boot 3.x (la última versión hasta 2025) con Maven, pero los conceptos también aplican para Gradle. Cubriremos lo básico paso a paso.

### Prerrequisitos
- Un proyecto Spring Boot configurado (por ejemplo, mediante Spring Initializr).
- Una base de datos (por ejemplo, H2 para pruebas, PostgreSQL/MySQL para producción) configurada en `application.properties`.

### Paso 1: Añadir la Dependencia de Liquibase
Incluye el starter de Liquibase Spring Boot en tu `pom.xml`. Esto incluye Liquibase y lo integra sin problemas.

```xml
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId> <!-- Para conectividad con la base de datos -->
</dependency>
```

Para Gradle, añade en `build.gradle`:
```groovy
implementation 'org.liquibase:liquibase-core'
implementation 'org.springframework.boot:spring-boot-starter-jdbc'
```

Ejecuta `mvn clean install` (o `./gradlew build`) para obtener las dependencias.

### Paso 2: Configurar Liquibase
Spring Boot detecta automáticamente Liquibase si colocas los archivos de changelog en la ubicación por defecto. Personaliza mediante `application.properties` (o el equivalente `.yml`).

Ejemplo `application.properties`:
```properties
# Configuración de la base de datos (ajusta para tu BD)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Configuración de Liquibase
spring.liquibase.change-log=classpath:db/changelog/db.changelog-master.xml
spring.liquibase.enabled=true  # El valor por defecto es true
spring.liquibase.drop-first=false  # Establecer a true en desarrollo para eliminar el esquema al iniciar
```

- `change-log`: Ruta a tu archivo maestro de changelog (por defecto: `db/changelog/db.changelog-master.xml`).
- Activar/desactivar con `spring.liquibase.enabled`.
- Para contextos/perfiles, usa `spring.liquibase.contexts=dev` para ejecutar cambios específicos.

### Paso 3: Crear Archivos de Changelog
Liquibase utiliza "changelogs" para definir cambios de esquema. Crea una estructura de directorios bajo `src/main/resources`:
```
src/main/resources/
└── db/
    └── changelog/
        ├── db.changelog-master.xml  # Archivo maestro que incluye otros
        └── changes/
            ├── 001-create-users-table.xml  # Cambios individuales
            └── 002-add-email-column.xml
```

#### Changelog Maestro (`db.changelog-master.xml`)
Este incluye otros changelogs:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                        http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <include file="changes/001-create-users-table.xml"/>
    <include file="changes/002-add-email-column.xml"/>
</databaseChangeLog>
```

#### Cambio de Ejemplo (`001-create-users-table.xml`)
Define la creación de una tabla:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                                       http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.24.xsd">

    <changeSet id="001" author="yourname">
        <createTable tableName="users">
            <column name="id" type="bigint">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="name" type="varchar(255)">
                <constraints nullable="false"/>
            </column>
        </createTable>
    </changeSet>
</databaseChangeLog>
```

- Usa formatos XML, YAML, JSON o SQL para los changelogs.
- Cada `<changeSet>` es una migración con un ID (para seguimiento).
- Ejecuta `java -jar target/your-app.jar` para iniciar la aplicación—Liquibase aplica los cambios automáticamente durante el arranque.

### Paso 4: Ejecución y Pruebas
- **Al Iniciar**: Spring Boot ejecuta Liquibase antes de que tu aplicación arranque completamente.
- **Reversión (Rollback)**: Usa `spring.liquibase.rollback-file` o la CLI para pruebas.
- **Integración CLI**: Para ejecuciones manuales, añade el plugin de Maven de Liquibase:
  ```xml
  <plugin>
      <groupId>org.liquibase</groupId>
      <artifactId>liquibase-maven-plugin</artifactId>
      <version>4.24.0</version>
      <configuration>
          <changeLogFile>src/main/resources/db/changelog/db.changelog-master.xml</changeLogFile>
          <url>jdbc:h2:mem:testdb</url>
          <username>sa</username>
          <password></password>
      </configuration>
  </plugin>
  ```
  Luego ejecuta `mvn liquibase:update`.

- **Validación**: Activa `spring.liquibase.validate-on-migrate=true` para verificar los changelogs.

### Consejos Comunes
- **Perfiles**: Usa `@Profile("dev")` en beans si es necesario, pero Liquibase se ejecuta globalmente a menos que se filtre.
- **Precondiciones**: Añade `<preConditions>` en los changesets para verificar el estado de la BD.
- **Formato SQL**: Para SQL directo, crea archivos `.sql` e inclúyelos: `<sqlFile path="changes/create-users.sql" relativeToChangelogFile="true"/>`.
- **Solución de Problemas**: Revisa los logs en busca de errores (por ejemplo, los prefijados con `liquibase`). Asegúrate de que la URL de la BD es correcta.
- **Producción**: Usa Flyway si lo prefieres, pero Liquibase sobresale con cambios complejos y soporte multi-BD.

Para características avanzadas como reversiones etiquetadas o extensiones personalizadas, consulta la documentación.

### Referencias
- [Auto-Configuración de Spring Boot para Liquibase](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#io.liquibase)
- [Documentación Oficial de Liquibase](https://docs.liquibase.com/start/home.html)
- [Tutorial de Baeldung: Spring Boot + Liquibase](https://www.baeldung.com/liquibase-refactor-schema-of-jpa-entity-in-spring-boot)