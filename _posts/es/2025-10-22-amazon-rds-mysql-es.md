---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Uso de Amazon RDS para MySQL
translated: true
type: note
---

Amazon RDS (Relational Database Service) para MySQL es un servicio de base de datos gestionado que facilita la configuración, operación y escalado de bases de datos MySQL en la nube. Se encarga de tareas rutinarias como copias de seguridad, aplicación de parches y escalado, para que puedas centrarte en tu aplicación. Esta guía te lleva a través de lo básico: crear una instancia de base de datos MySQL, conectarte a ella y realizar operaciones simples. Usaremos la Consola de AWS Management por simplicidad.

**Nota sobre Costos:** El Nivel Gratuito de AWS ofrece uso limitado para cuentas nuevas, pero se aplicarán cargos por recursos que lo excedan. Elimina siempre los recursos cuando termines para evitar facturas inesperadas. Para producción, sigue las mejores prácticas de seguridad como usar VPCs, cifrado y acceso de privilegio mínimo.

## Prerrequisitos
- Una cuenta de AWS (regístrate en [aws.amazon.com](https://aws.amazon.com) si es necesario).
- Familiaridad básica con la consola de AWS y MySQL.
- Para pruebas de conexión segura, crearemos una instancia EC2 en la misma VPC (Virtual Private Cloud). Determina tu dirección IP pública (por ejemplo, mediante [checkip.amazonaws.com](https://checkip.amazonaws.com)) para el acceso SSH.
- Elige una Región de AWS cercana a ti (por ejemplo, US East (N. Virginia)).

**Mejor Práctica:** Usa una instancia de base de datos privada en una VPC para restringir el acceso solo a recursos de confianza. Habilita SSL/TLS para conexiones cifradas.

## Paso 1: Crear una Instancia EC2 para la Conexión
Esto configura un servidor Linux simple para conectarte a tu instancia de base de datos privada.

1. Inicia sesión en la [Consola de AWS Management](https://console.aws.amazon.com) y abre la consola de EC2.
2. Selecciona tu Región.
3. Haz clic en **Launch instance**.
4. Configura:
   - **Name:** `ec2-database-connect`.
   - **AMI:** Amazon Linux 2023 (elegible para nivel gratuito).
   - **Instance type:** t3.micro (elegible para nivel gratuito).
   - **Key pair:** Crea o selecciona una existente para el acceso SSH.
   - **Network settings:** Editar > Permitir tráfico SSH desde **My IP** (o tu IP específica, ej. `192.0.2.1/32`). Evita `0.0.0.0/0` por seguridad.
   - Deja los valores por defecto para almacenamiento y etiquetas.
5. Haz clic en **Launch instance**.
6. Anota el ID de instancia, el DNS IPv4 público y el nombre del par de claves desde los detalles de la instancia.
7. Espera a que el estado muestre **Running** (2-5 minutos).

**Consejo de Seguridad:** Restringe SSH solo a tu IP. Descarga el par de claves (archivo .pem) de forma segura.

## Paso 2: Crear una Instancia de Base de Datos MySQL
Usa "Easy create" para una configuración rápida con valores por defecto.

1. Abre la [consola de RDS](https://console.aws.amazon.com/rds/).
2. Selecciona la misma Región que tu instancia EC2.
3. En el panel de navegación, haz clic en **Databases** > **Create database**.
4. Selecciona **Easy create**.
5. En **Configuration**:
   - Engine type: **MySQL**.
   - Templates: **Free tier** (o **Sandbox** para cuentas de pago).
   - DB instance identifier: `database-test1` (o el que elijas).
   - Master username: `admin` (o personalizado).
   - Master password: Generar automáticamente o establece una contraseña fuerte (guárdala de forma segura).
6. (Opcional) En **Connectivity**, selecciona **Connect to an EC2 compute resource** y elige tu instancia EC2 para una configuración más fácil.
7. Haz clic en **Create database**.
8. Ve la ventana emergente de credenciales (nombre de usuario/contraseña)—guárdalas, ya que la contraseña no se puede recuperar después.
9. Espera a que el estado cambie a **Available** (hasta 10-20 minutos). Anota el **Endpoint** (nombre DNS) y el puerto (por defecto: 3306) desde la pestaña **Connectivity & security**.

**Mejor Práctica:** Para producción, usa "Standard create" para personalizar VPC, copias de seguridad (habilita las automatizadas) y almacenamiento. Habilita la protección contra eliminación y multi-AZ para alta disponibilidad.

## Paso 3: Conectarse a la Instancia de Base de Datos
Conéctate desde tu instancia EC2 usando el cliente MySQL.

1. Conéctate por SSH a tu instancia EC2:
   ```
   ssh -i /ruta/a/tu-par-de-claves.pem ec2-user@tu-dns-publico-ec2
   ```
   (Reemplaza con tus detalles; ej. `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`.)

2. En la instancia EC2, actualiza los paquetes:
   ```
   sudo dnf update -y
   ```

3. Instala el cliente MySQL:
   ```
   sudo dnf install mariadb105 -y
   ```

4. Conéctate a la base de datos:
   ```
   mysql -h tu-db-endpoint -P 3306 -u admin -p
   ```
   Ingresa la contraseña maestra cuando se solicite.

Si es exitoso, verás el prompt de MySQL (`mysql>`).

**Solución de Problemas:** Asegúrate de que los grupos de seguridad permiten tráfico entrante en el puerto 3306 desde la instancia EC2. Para conexiones externas, haz la base de datos pública (no recomendado) o usa hosts bastión/VPN.

**Consejo de Seguridad:** Usa `--ssl-mode=REQUIRED` para conexiones cifradas: `mysql -h endpoint -P 3306 -u admin -p --ssl-mode=REQUIRED`.

## Paso 4: Uso Básico
Una vez conectado, puedes ejecutar comandos SQL. Ejemplos:

- Mostrar bases de datos: `SHOW DATABASES;`
- Crear una base de datos de ejemplo: `CREATE DATABASE myapp;`
- Usarla: `USE myapp;`
- Crear una tabla:
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- Insertar datos: `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- Consultar: `SELECT * FROM users;`
- Salir: `EXIT;`

Desde aplicaciones (ej. Python, Node.js), usa controladores MySQL estándar con el endpoint, puerto, nombre de usuario y contraseña como cadenas de conexión.

**Mejor Práctica:** Monitorea el rendimiento mediante CloudWatch, habilita copias de seguridad automatizadas y escala verticalmente (tamaño de instancia) u horizontalmente (réplicas de lectura) según sea necesario.

## Limpieza: Eliminar Recursos
Para detener los cargos:

1. **Eliminar instancia EC2:** Consola EC2 > Seleccionar instancia > **Instance state** > **Terminate** > Confirmar.
2. **Eliminar instancia de base de datos:** Consola RDS > Seleccionar base de datos > **Actions** > **Delete** > Desmarcar creación de snapshot > Confirmar.

Revisa la consola de Facturación de AWS para verificar cualquier recurso en ejecución.

Para temas más avanzados como migraciones, ajuste de rendimiento o uso de API/CLI, consulta la documentación de AWS.

## Referencias
- [Creating and connecting to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [Getting started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)