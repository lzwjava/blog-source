---
audio: false
generated: true
lang: es
layout: post
title: El Arte de la Guerra
translated: true
type: note
---

Aquí hay ejemplos adicionales para habilitar la salida detallada en varias herramientas y sistemas, ampliando el tema de proporcionar retroalimentación o registro más detallado:

- **PowerShell**: Para habilitar la salida detallada, usa el modificador `-Verbose` con los cmdlets que lo admitan. Por ejemplo:  
  ```powershell
  Get-Process -Verbose
  ```
  Alternativamente, establece la variable `$VerbosePreference` globalmente:  
  ```powershell
  $VerbosePreference = "Continue"
  ```

- **CMake**: Para obtener una salida detallada durante el proceso de compilación, usa la bandera `--verbose` o establece `VERBOSE=1`:  
  ```bash
  cmake --build . --verbose
  ```
  O:  
  ```bash
  make VERBOSE=1
  ```

- **Make**: Para habilitar la salida detallada y ver todos los comandos ejecutados, usa la bandera `-d` para depuración o evita silenciar la salida con `@`:  
  ```bash
  make -d
  ```
  O edita el Makefile para eliminar los prefijos `@` de los comandos.

- **GCC (GNU Compiler Collection)**: Para una salida detallada de compilación, usa la bandera `-v`:  
  ```bash
  gcc -v -o output source.c
  ```

- **GDB (GNU Debugger)**: Para aumentar el nivel de detalle, usa el comando `set verbose on` dentro de GDB:  
  ```gdb
  (gdb) set verbose on
  (gdb) run
  ```

- **Ruby**: Ejecuta scripts Ruby en modo detallado usando la bandera `-v` o `--verbose`:  
  ```bash
  ruby -v script.rb
  ```
  Para advertencias adicionales, usa `-w`:  
  ```bash
  ruby -w script.rb
  ```

- **Perl**: Habilita la salida detallada con la bandera `-v` o usa la pragma `diagnostics` para mensajes de error detallados:  
  ```bash
  perl -v script.pl
  ```
  O en el script:  
  ```perl
  use diagnostics;
  ```

- **PHP**: Ejecuta scripts PHP con reporte de errores detallado estableciendo `error_reporting` y `display_errors` en `php.ini`:  
  ```ini
  error_reporting = E_ALL
  display_errors = On
  ```
  O desde la línea de comandos:  
  ```bash
  php -d error_reporting=E_ALL script.php
  ```

- **R**: Para habilitar la salida detallada en scripts R, usa el argumento `verbose=TRUE` en funciones que lo admitan (ej., `install.packages`):  
  ```R
  install.packages("dplyr", verbose=TRUE)
  ```

- **Go (Golang)**: Para salida detallada durante la compilación o pruebas, usa la bandera `-v`:  
  ```bash
  go build -v
  go test -v
  ```

- **Rust (Cargo)**: Habilita la salida detallada con Cargo usando las banderas `-v` o `-vv`:  
  ```bash
  cargo build -v
  cargo run -vv
  ```

- **Jenkins**: Para habilitar el registro detallado en un pipeline, agrega la opción `verbose` en el script o configura la salida de la consola en los ajustes del trabajo. Por ejemplo, en un Jenkinsfile:  
  ```groovy
  sh 'some_command --verbose'
  ```
  Alternativamente, establece la propiedad del sistema `-Dhudson.model.TaskListener.verbose=true` al iniciar Jenkins.

- **Vagrant**: Obtén salida detallada con la bandera `--debug`:  
  ```bash
  vagrant up --debug
  ```

- **Puppet**: Ejecuta Puppet con mayor nivel de detalle usando las banderas `--verbose` o `--debug`:  
  ```bash
  puppet apply site.pp --verbose
  puppet apply site.pp --debug
  ```

- **Chef**: Habilita la salida detallada con la bandera `-l` (nivel de registro):  
  ```bash
  chef-client -l debug
  ```

- **SaltStack**: Aumenta el nivel de detalle con la bandera `-l` (ej., `debug` o `trace`):  
  ```bash
  salt '*' test.ping -l debug
  ```

- **PostgreSQL (psql)**: Para obtener salida detallada de `psql`, usa la bandera `-e` para mostrar las consultas o `\set VERBOSITY verbose` para mensajes de error detallados:  
  ```bash
  psql -e -f script.sql
  ```
  O en `psql`:  
  ```sql
  \set VERBOSITY verbose
  ```

- **MySQL**: Ejecuta el cliente MySQL con salida detallada usando `--verbose`:  
  ```bash
  mysql --verbose < script.sql
  ```

- **SQLite**: Usa el comando `.explain` para obtener planes de ejecución de consultas detallados:  
  ```sqlite
  sqlite3 database.db
  sqlite> .explain
  sqlite> SELECT * FROM table;
  ```

- **MongoDB**: Habilita el registro detallado iniciando `mongod` con la bandera `-v` (hasta `-vvvvv` para más detalle):  
  ```bash
  mongod -v
  ```

- **Elasticsearch**: Inicia Elasticsearch con registro detallado ajustando el archivo `log4j2.properties`:  
  ```properties
  logger.action.level = debug
  ```
  O pasa `--verbose` al iniciar:  
  ```bash
  elasticsearch --verbose
  ```

- **NGINX**: Prueba la configuración con salida detallada usando `-T`:  
  ```bash
  nginx -T
  ```
  Para mayor detalle en tiempo de ejecución, aumenta el nivel de `error_log` en `nginx.conf`:  
  ```nginx
  error_log /var/log/nginx/error.log debug;
  ```

- **Apache HTTP Server**: Habilita el registro detallado estableciendo la directiva `LogLevel` en `httpd.conf` o `apache2.conf`:  
  ```apache
  LogLevel debug
  ```

- **OpenSSL**: Obtén salida detallada con comandos como `s_client`:  
  ```bash
  openssl s_client -connect example.com:443 -debug
  ```

- **JUnit (Java Testing)**: Ejecuta pruebas JUnit con salida detallada configurando el ejecutor de pruebas (ej., el plugin Maven Surefire):  
  ```xml
  <configuration>
      <argLine>-verbose</argLine>
  </configuration>
  ```

Estos ejemplos cubren una amplia gama de herramientas en lenguajes de programación, sistemas de compilación, bases de datos, servidores y utilidades DevOps. ¡Avísame si deseas más ejemplos específicos o detalles para alguna herramienta en particular!