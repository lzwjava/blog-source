---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Migración de Base de Datos Flyway
translated: true
type: note
---

### Introducción a Flyway
Flyway es una herramienta de código abierto popular para gestionar migraciones de esquemas de base de datos de manera controlada por versiones. Te permite aplicar cambios incrementales a tu base de datos (como crear tablas, alterar columnas o insertar datos) de forma repetible y segura. En aplicaciones Java, Flyway se puede integrar a través de su API, y a menudo se ejecuta al inicio de la aplicación para garantizar que el esquema de la base de datos esté actualizado antes de que tu código interactúe con ella. Funciona con la mayoría de las bases de datos a través de JDBC (por ejemplo, PostgreSQL, MySQL, Oracle).

### Paso 1: Añadir la Dependencia de Flyway
Añade Flyway a tu archivo de compilación. Usa la edición de código abierto a menos que necesites funciones empresariales.

**Maven (`pom.xml`)**:
```xml
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
        <version>11.14.1</version> <!-- Comprueba la versión más reciente -->
    </dependency>
    <!-- Añade tu controlador JDBC de base de datos, por ejemplo, para PostgreSQL -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.7.3</version>
    </dependency>
</dependencies>
```

**Gradle (`build.gradle`)**:
```groovy
dependencies {
    implementation 'org.flywaydb:flyway-core:11.14.1'
    // Añade tu controlador JDBC de base de datos
    implementation 'org.postgresql:postgresql:42.7.3'
}
```

También necesitarás el controlador JDBC para tu base de datos objetivo.

### Paso 2: Configurar Flyway
Flyway utiliza una API fluida para la configuración. Los ajustes clave incluyen los detalles de conexión a la base de datos, las ubicaciones para los scripts de migración y callbacks opcionales.

En tu código Java, crea una instancia de `Flyway`:
```java
import org.flywaydb.core.Flyway;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")  // Carpeta para los scripts SQL (por defecto: db/migration)
                .load();
    }
}
```
- `locations`: Apunta a donde se almacenan tus archivos de migración (por ejemplo, `src/main/resources/db/migration` para classpath).
- Otras configuraciones comunes: `.baselineOnMigrate(true)` para establecer una base para esquemas existentes, o `.table("flyway_schema_history")` para personalizar la tabla de historial.

### Paso 3: Escribir Scripts de Migración
Los scripts de migración son archivos SQL ubicados en la ubicación configurada (por ejemplo, `src/main/resources/db/migration`). Flyway los aplica en orden.

#### Convenciones de Nomenclatura
- **Migraciones versionadas** (para cambios de esquema únicos): `V<versión>__<descripción>.sql` (por ejemplo, `V1__Create_person_table.sql`, `V2__Add_age_column.sql`).
  - Formato de versión: Usa guiones bajos para los segmentos (por ejemplo, `V1_1__Initial.sql`).
- **Migraciones repetibles** (para tareas continuas como vistas): `R__<descripción>.sql` (por ejemplo, `R__Update_view.sql`). Estas se ejecutan cada vez que cambian.
- Los archivos se aplican en orden lexicográfico.

#### Scripts de Ejemplo
Crea estos archivos en `src/main/resources/db/migration`.

**V1__Create_person_table.sql**:
```sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO person (id, name) VALUES (1, 'John Doe');
```

**V2__Add_age_column.sql**:
```sql
ALTER TABLE person ADD COLUMN age INT;
```

**R__Populate_names.sql** (repetible):
```sql
UPDATE person SET name = CONCAT(name, ' (Updated)') WHERE id = 1;
```

Flyway rastrea las migraciones aplicadas en una tabla `flyway_schema_history`.

Para lógica compleja no apta para SQL, usa migraciones basadas en Java (implementa `org.flywaydb.core.api.migration.java.JavaMigration`).

### Paso 4: Ejecutar Migraciones Programáticamente
Llama a `migrate()` para aplicar las migraciones pendientes. Integra esto en el inicio de tu aplicación (por ejemplo, en `main()` o en un `@PostConstruct` de Spring).

```java
import org.flywaydb.core.Flyway;
import org.flywaydb.core.api.FlywayException;

public class DatabaseMigration {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/mydb";
        String user = "username";
        String password = "password";

        Flyway flyway = Flyway.configure()
                .dataSource(url, user, password)
                .locations("classpath:db/migration")
                .load();

        try {
            flyway.migrate();  // Aplica todas las migraciones pendientes
            System.out.println("¡Migración de la base de datos exitosa!");
        } catch (FlywayException e) {
            System.err.println("Error en la migración: " + e.getMessage());
            // Maneja el error (por ejemplo, salir o hacer rollback)
        }

        // Ahora inicia el resto de tu aplicación
    }
}
```

- `migrate()`: Aplica las migraciones versionadas en orden, luego las repetibles.
- Otros comandos: `flyway.info()` para el estado, `flyway.repair()` para corregir problemas, `flyway.validate()` para verificar la consistencia.
- Ejecuta esto antes de cualquier operación de base de datos para garantizar la compatibilidad del esquema.

### Mejores Prácticas
- Mantén las migraciones idempotentes (seguras para re-ejecutar).
- Prueba las migraciones en una copia de los datos de producción.
- Usa control de versiones para los archivos de migración.
- Para Spring Boot, añade `spring-boot-starter-jdbc` y establece `spring.flyway.enabled=true` en `application.properties` para la auto-configuración.

### Referencias
- [Documentación de la API de Flyway (Java)](https://documentation.red-gate.com/fd/api-java-277579358.html)
- [Documentación de Migraciones de Flyway](https://documentation.red-gate.com/fd/migrations-271585107.html)
- [Flyway Getting Started](https://documentation.red-gate.com/fd/getting-started-with-flyway-184127223.html)