---
audio: false
generated: true
lang: es
layout: post
title: Crear una base de datos de PostgreSQL
translated: true
type: note
---

Ya estás en la terminal interactiva de PostgreSQL (`psql`) como usuario `postgres`, ¡lo cual es excelente! Para crear una base de datos en PostgreSQL, puedes usar el comando `CREATE DATABASE`. Aquí tienes una guía paso a paso:

1. **Asegúrate de estar en `psql`**:
   Ya lo estás, como lo muestra el indicador `postgres=#`.

2. **Crear una base de datos**:
   Usa el siguiente comando para crear una nueva base de datos. Reemplaza `mydatabase` con el nombre que desees para tu base de datos:

   ```sql
   CREATE DATABASE mydatabase;
   ```

   Esto crea una base de datos llamada `mydatabase`.

3. **Verificar que la base de datos fue creada**:
   Lista todas las bases de datos para confirmar:

   ```sql
   \l
   ```

   Esto mostrará una tabla con todas las bases de datos, incluyendo `mydatabase`.

4. **Conectarse a la nueva base de datos**:
   Para empezar a trabajar en la nueva base de datos, conéctate a ella con:

   ```sql
   \c mydatabase
   ```

   Esto cambia tu sesión a `mydatabase`.

5. **Opcional: Crear un usuario y otorgar permisos**:
   Si deseas que un usuario específico gestione esta base de datos, créalo y otórgale privilegios:

   ```sql
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

   Reemplaza `myuser` y `mypassword` con el nombre de usuario y la contraseña que desees.

6. **Salir de `psql`**:
   Cuando hayas terminado, sal con:

   ```sql
   \q
   ```

### Notas:
- El error `Permission denied` que viste (`could not change directory to "/home/lzw/projects/lzwjava.github.io"`) se debe a que el usuario `postgres` no tiene acceso a tu directorio personal. Esto no afecta la creación de la base de datos, pero puede aparecer cuando ejecutas `psql` desde un directorio restringido. Puedes evitar esto ejecutando `psql` desde un directorio al que el usuario `postgres` sí tenga acceso o sin cambiar de directorio (por ejemplo, ejecuta `sudo -u postgres psql` desde `/tmp`).
- El comando `ls` que intentaste en `psql` no es válido. Usa `\l` para listar bases de datos o `\dt` para listar tablas dentro de una base de datos.
- Asegúrate de que el servicio de PostgreSQL esté en ejecución (`sudo systemctl start postgresql.service`), lo cual ya hiciste.

### Ejemplo de Sesión:
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 mydatabase  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# \q
```

Si necesitas más ayuda (por ejemplo, configurar tablas, usuarios o conectar desde una aplicación), ¡avísame!