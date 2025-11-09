---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Azure Database para MySQL Flexible Server
translated: true
type: note
---

Azure Database for MySQL es un servicio de base de datos relacional totalmente administrado que funciona con la edición community de MySQL. Se encarga de tareas rutinarias como copias de seguridad, aplicación de revisiones y supervisión, lo que le permite centrarse en su aplicación. La opción de implementación recomendada es **Flexible Server**, que ofrece más opciones de configuración y mejor rendimiento que el antiguo Single Server (que está en proceso de retirada).

Esta guía cubre la creación de un servidor, la conexión al mismo y la realización de operaciones básicas. Se basa en Azure Portal por simplicidad.

## Requisitos previos
- Una suscripción activa de Azure (cree una en [azure.microsoft.com](https://azure.microsoft.com/free/) si es necesario).
- Acceso a Azure Portal (portal.azure.com).
- Conocimientos básicos de los conceptos de MySQL.
- Acceso de red saliente en el puerto 3306 (valor predeterminado para MySQL).
- MySQL Workbench instalado para la conexión (descárguelo desde [mysql.com](https://dev.mysql.com/downloads/workbench/)).

## Paso 1: Crear un Flexible Server en Azure Portal
Siga estos pasos para aprovisionar su servidor.

1. Inicie sesión en [Azure Portal](https://portal.azure.com).

2. Busque "Azure Database for MySQL Flexible Servers" en la barra de búsqueda superior y selecciónelo.

3. Haga clic en **Crear** para iniciar el asistente.

4. En la pestaña **Aspectos básicos**, configure:
   - **Suscripción**: Seleccione su suscripción.
   - **Grupo de recursos**: Cree uno nuevo (por ejemplo, `myresourcegroup`) o elija uno existente.
   - **Nombre del servidor**: Nombre único (por ejemplo, `mydemoserver`), entre 3 y 63 caracteres, letras minúsculas/números/guiones. El nombre de host completo será `<nombre>.mysql.database.azure.com`.
   - **Región**: Elija la más cercana a sus usuarios.
   - **Versión de MySQL**: 8.0 (última versión principal).
   - **Tipo de carga de trabajo**: Desarrollo (para pruebas; use Pequeña/Mediana para producción).
   - **Proceso + almacenamiento**: Nivel ampliable, Standard_B1ms (1 vCore), 10 GiB de almacenamiento, 100 IOPS, copias de seguridad de 7 días. Ajústelo según las necesidades (por ejemplo, aumente las IOPS para migraciones).
   - **Zona de disponibilidad**: Sin preferencia (o coincida con la zona de su aplicación).
   - **Alta disponibilidad**: Deshabilitada para empezar (habilite la redundancia de zona para producción).
   - **Autenticación**: MySQL y Microsoft Entra (para flexibilidad).
   - **Nombre de usuario del administrador**: por ejemplo, `mydemouser` (no root/admin/etc., máximo 32 caracteres).
   - **Contraseña**: Contraseña segura (8-128 caracteres, combinación de mayúsculas/minúsculas/números/símbolos).

5. Cambie a la pestaña **Redes**:
   - **Método de conectividad**: Acceso público (por simplicidad; use VNet privado para seguridad en producción).
   - **Reglas de firewall**: Agregue la IP del cliente actual (o permita servicios de Azure). No podrá cambiar esto más tarde.

6. Revise la configuración en **Revisar + crear** y haga clic en **Crear**. La implementación tarda entre 5 y 10 minutos. Supervísela mediante las notificaciones.

7. Una vez finalizado, anclelo al panel y vaya a la página **Información general** del recurso. Las bases de datos predeterminadas incluyen `information_schema`, `mysql`, etc.

## Paso 2: Conectarse a su servidor
Utilice MySQL Workbench para una conexión gráfica. (Alternativas: Azure Data Studio, CLI de mysql o Azure Cloud Shell).

1. En el portal, vaya a la **Información general** de su servidor y anote:
   - Nombre del servidor (por ejemplo, `mydemoserver.mysql.database.azure.com`).
   - Nombre de usuario del administrador.
   - Restablezca la contraseña si es necesario.

2. Abra MySQL Workbench.

3. Haga clic en **Nueva conexión** (o edite una existente).

4. En la pestaña **Parámetros**:
   - **Nombre de la conexión**: por ejemplo, `Conexión Demo`.
   - **Método de conexión**: Estándar (TCP/IP).
   - **Nombre del host**: Nombre completo del servidor.
   - **Puerto**: 3306.
   - **Nombre de usuario**: Nombre de usuario del administrador.
   - **Contraseña**: Ingrésela y guárdela en el almacén.

5. Haga clic en **Probar conexión**. Si falla:
   - Verifique los detalles del portal.
   - Asegúrese de que el firewall permita su IP.
   - TLS/SSL es obligatorio (TLS 1.2); descargue el certificado de CA desde [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) y vincúlelo en Workbench si es necesario (en la pestaña SSL: Usar SSL > Requerir y especificar el archivo CA).

6. Haga clic en **Aceptar** para guardar. Haga doble clic en el icono de la conexión para abrir un editor de consultas.

## Paso 3: Crear y administrar bases de datos
Una vez conectado, administre las bases de datos mediante el portal o el cliente.

### Mediante Azure Portal:
1. En la página de su servidor, seleccione **Bases de datos** en el menú izquierdo.
2. Haga clic en **+ Agregar**:
   - **Nombre de la base de datos**: por ejemplo, `testdb`.
   - **Juego de caracteres**: utf8 (predeterminado).
   - **Intercalación**: utf8_general_ci.
3. Haga clic en **Guardar**.

Para eliminar: Seleccione la(s) base(s) de datos, haga clic en **Eliminar**.

### Mediante MySQL Workbench (Consultas SQL):
Ejecute estas consultas en el editor de consultas:

- Crear base de datos: `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- Listar bases de datos: `SHOW DATABASES;`
- Usar base de datos: `USE testdb;`
- Crear tabla: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- Insertar datos: `INSERT INTO users (name) VALUES ('Alice');`
- Consultar: `SELECT * FROM users;`

Confirme los cambios con `COMMIT;` si no está confirmando automáticamente.

## Consejos de uso básico
- **Escalado**: Desde **Información general** > **Proceso + almacenamiento**, ajuste vCores/almacenamiento/IOPS (la mayoría de los cambios no requieren tiempo de inactividad).
- **Copias de seguridad**: Automatizadas diarias; restauración a un momento dado hasta 35 días (configúrelo en la configuración de **Copia de seguridad**).
- **Supervisión**: Utilice **Métricas** para información sobre CPU/almacenamiento; establezca alertas.
- **Seguridad**: Utilice siempre SSL (obligatorio). Para producción, habilite HA, redes privadas y autenticación de Entra ID.
- **Migración**: Utilice mysqldump para bases de datos pequeñas; DMS para las grandes.
- **Costos**: Pague por proceso/almacenamiento; comience con un plan pequeño y escale. Utilice la calculadora en [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/).
- **Limpieza**: Elimine el grupo de recursos para eliminar el servidor y evitar cargos.

Para características avanzadas como réplicas de lectura o parámetros del servidor, explore el menú izquierdo del portal.

## Referencias
- [Inicio rápido: Creación de un servidor flexible mediante Azure Portal](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal)
- [Conexión mediante MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [Creación y administración de bases de datos](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Documentación de Azure Database for MySQL](https://learn.microsoft.com/en-us/azure/mysql/)