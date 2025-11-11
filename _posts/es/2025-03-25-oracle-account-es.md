---
audio: false
generated: true
lang: es
layout: post
title: Base de Datos Oracle - Cuenta de Usuario
translated: true
type: note
---

El error `ORA-28000: The account is locked` se produce al intentar conectarse a una base de datos Oracle (por ejemplo, mediante un controlador JDBC thin) y la cuenta de usuario que intentas utilizar está bloqueada. Esto suele ocurrir debido a demasiados intentos de inicio de sesión fallidos, un bloqueo manual por parte de un administrador o una política de caducidad de la cuenta. Para resolverlo, necesitas desbloquear la cuenta y, si es necesario, restablecer la contraseña o verificar el estado de la cuenta. A continuación, se detallan los pasos para solucionar este problema al conectarse a una base de datos Oracle.

---

### Pasos para solucionar ORA-28000

#### 1. **Verificar el error**
   Cuando encuentres este error en una conexión JDBC, podría verse así:
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   Esto confirma que el problema está con la cuenta de la base de datos, no con la configuración JDBC en sí (por ejemplo, la URL, el controlador o la configuración del origen de datos de WebSphere).

#### 2. **Iniciar sesión como usuario con privilegios**
   Para desbloquear la cuenta, necesitas acceso a un usuario de la base de datos con privilegios administrativos (por ejemplo, `SYS`, `SYSTEM` o un usuario con el rol `DBA`). Conéctate a la base de datos usando una herramienta como SQL*Plus, SQL Developer o un cliente JDBC:
   ```bash
   sqlplus / as sysdba
   ```
   O
   ```bash
   sqlplus system/<contraseña>@<nombre_servicio>
   ```
   Reemplaza `<contraseña>` y `<nombre_servicio>` con tus credenciales reales y el nombre del servicio de la base de datos (por ejemplo, `ORCL`).

#### 3. **Verificar el estado de la cuenta**
   Ejecuta la siguiente consulta SQL para verificar el estado de la cuenta bloqueada:
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'TU_NOMBRE_DE_USUARIO';
   ```
   - Reemplaza `TU_NOMBRE_DE_USUARIO` con el nombre de usuario con el que intentas conectarte (por ejemplo, `miusuario`).
   - Observa la columna `ACCOUNT_STATUS`. Si dice `LOCKED` o `LOCKED(TIMED)`, la cuenta está bloqueada.

   Salida de ejemplo:
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MIUSUARIO  LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **Desbloquear la cuenta**
   Para desbloquear la cuenta, ejecuta este comando SQL como el usuario con privilegios:
   ```sql
   ALTER USER tu_nombre_de_usuario ACCOUNT UNLOCK;
   ```
   Ejemplo:
   ```sql
   ALTER USER miusuario ACCOUNT UNLOCK;
   ```

#### 5. **(Opcional) Restablecer la contraseña**
   Si la contraseña podría haber caducado o sospechas que es incorrecta, restablécela mientras lo haces:
   ```sql
   ALTER USER tu_nombre_de_usuario IDENTIFIED BY nueva_contraseña;
   ```
   Ejemplo:
   ```sql
   ALTER USER miusuario IDENTIFIED BY minuevacontraseña123;
   ```
   - Después de restablecerla, actualiza la contraseña en tu `server.xml` de WebSphere (o donde esté configurado el origen de datos JDBC) y vuelve a cifrarla si es necesario (consulta tu pregunta anterior para los pasos de codificación AES).

#### 6. **Confirmar los cambios (si es necesario)**
   En la mayoría de los casos, los comandos `ALTER USER` surten efecto inmediatamente y no requieren un `COMMIT`. Sin embargo, si estás en un entorno con muchas transacciones, asegúrate de que no ocurra una reversión reiniciando la sesión o la base de datos si es necesario.

#### 7. **Probar la conexión**
   Intenta conectarte nuevamente usando tu aplicación JDBC o una prueba simple:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "miusuario";
           String password = "minuevacontraseña123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("¡Conexión exitosa!");
           conn.close();
       }
   }
   ```
   - Actualiza la `url`, `user` y `password` para que coincidan con tu entorno.
   - Si esto funciona, actualiza la configuración de tu origen de datos de WebSphere en consecuencia.

#### 8. **Verificar las políticas del perfil (evitar bloqueos futuros)**
   La cuenta podría haberse bloqueado debido a una política de seguridad en el perfil del usuario (por ejemplo, `FAILED_LOGIN_ATTEMPTS` o `PASSWORD_LOCK_TIME`). Verifica el perfil asignado al usuario:
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'TU_NOMBRE_DE_USUARIO';
   ```
   Luego, inspecciona los límites del perfil:
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'TU_NOMBRE_DE_PERFIL';
   ```
   Busca:
   - `FAILED_LOGIN_ATTEMPTS`: Número de intentos fallidos antes del bloqueo (por ejemplo, `10`).
   - `PASSWORD_LOCK_TIME`: Duración del bloqueo (por ejemplo, `1` día).

   Para relajar estas configuraciones (si es apropiado), modifica el perfil:
   ```sql
   ALTER PROFILE tu_nombre_de_perfil LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   Ejemplo:
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **Reiniciar WebSphere (si es necesario)**
   Si estás usando WebSphere y actualizaste la contraseña del origen de datos, reinicia el servidor de aplicaciones para asegurarte de que los cambios surtan efecto:
   - Para Liberty: `./bin/server stop` y `./bin/server start`.
   - Para WebSphere tradicional: Usa la Consola de Administración o `stopServer.sh`/`startServer.sh`.

---

### Causas comunes de ORA-28000
- **Demasiados intentos de inicio de sesión fallidos**: Revisa los registros de la aplicación o los registros de WebSphere (por ejemplo, `SystemOut.log`) en busca de errores de conexión previos.
- **Bloqueo manual**: Un administrador podría haber bloqueado la cuenta intencionadamente (`ALTER USER miusuario ACCOUNT LOCK`).
- **Cuenta caducada**: Algunos entornos bloquean las cuentas cuando las contraseñas caducan. Verifica `EXPIRY_DATE` en `dba_users`.

---

### Consejos para la resolución de problemas
- Si no tienes acceso `SYS` o `SYSTEM`, contacta con tu administrador de base de datos para que desbloquee la cuenta.
- Asegúrate de que la URL JDBC, el nombre de usuario y la contraseña en `server.xml` sean correctos antes de reintentar.
- Si el problema persiste, verifica que el listener de Oracle esté en ejecución:
  ```bash
  lsnrctl status
  ```

¡Avísame si encuentras errores adicionales o necesitas ayuda con un paso específico!