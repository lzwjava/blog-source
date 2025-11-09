---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Oracle 12c en Ubuntu
translated: true
type: note
---

### Instalación de Oracle Database 12c Release 1 (12.1.0.2 con parche 12.1.2?) desde Tarball en Ubuntu 22.04 x86_64

El archivo `v12.1.2_linuxx64_server_dec.tar.gz` parece ser un tarball para Oracle Database 12c Release 1 (probablemente versión 12.1.0.2 empaquetada con el parche 12.1.2, edición server, posiblemente "dec" para desconfigurado). Esta es una versión antigua de Oracle Database (de ~2013-2014), y Oracle **no admite oficialmente Ubuntu**. La instalación en Ubuntu 22.04 (que usa bibliotecas modernas como glibc 2.35) puede funcionar pero puede requerir soluciones alternativas para problemas de compatibilidad, como enlaces de bibliotecas o parámetros del kernel. Espere posibles errores con las dependencias—pruebe primero en una máquina virtual.

**Advertencias:**
- Oracle 12c está en fin de vida para soporte extendido (desde 2022), así que úselo para pruebas/producción bajo su propio riesgo. Considere versiones más nuevas como 19c o 23ai para producción.
- Necesitará acceso root/sudo.
- Hardware mínimo: 2 GB de RAM (8 GB recomendados), 2 núcleos de CPU, 10 GB de espacio libre en disco para el software (más para la base de datos).
- Haga una copia de seguridad de su sistema antes de continuar.
- Si este tarball no es de una fuente oficial de Oracle, verifique su integridad (por ejemplo, con checksums) para evitar malware.

#### Paso 1: Preparar el Sistema
1. **Actualizar Ubuntu**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Instalar Dependencias Requeridas**:
   Oracle 12c necesita bibliotecas específicas. Instálelas via apt:
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - Si `oracle-java8-installer` no está disponible (está en repositorios antiguos), agregue el PPA de Java de Oracle o descargue JDK 8 manualmente:
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     Acepte la licencia durante la instalación. Establezca JAVA_HOME:
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Crear Usuario y Grupos de Oracle**:
   Ejecute como root o con sudo:
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # Establezca una contraseña para el usuario oracle
   ```

4. **Configurar Parámetros del Kernel**:
   Edite `/etc/sysctl.conf`:
   ```
   sudo nano /etc/sysctl.conf
   ```
   Agregue estas líneas (ajuste para su RAM/disco; estos son mínimos):
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   Aplique los cambios:
   ```
   sudo sysctl -p
   ```

5. **Establecer Límites de Shell para el Usuario Oracle**:
   Edite `/etc/security/limits.conf`:
   ```
   sudo nano /etc/security/limits.conf
   ```
   Agregue:
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   Edite `/etc/pam.d/login` y agregue:
   ```
   sudo nano /etc/pam.d/login
   ```
   Añada: `session required pam_limits.so`

6. **Crear Directorios**:
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **Espacio de Intercambio (Swap)** (si RAM < 8 GB, agregue swap):
   Para 2 GB de RAM, cree un archivo de swap de 2 GB:
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **Deshabilitar Firewall/SElinux** (si está habilitado):
   ```
   sudo ufw disable  # O configure los puertos 1521, 5500 si es necesario
   sudo apt remove apparmor -y  # Si AppArmor interfiere
   ```

#### Paso 2: Extraer el Tarball
Cambie al usuario oracle:
```
su - oracle
cd ~/Downloads  # O donde esté el archivo
```
Extraiga (esto crea la estructura de directorios del home de la base de datos):
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- Esto debería crear `/u01/app/oracle/product/12.1.0/dbhome_1` con archivos como `runInstaller`.
- Si el tarball se extrae en una estructura diferente, ajuste las rutas en consecuencia (por ejemplo, directorio `database/`).

#### Paso 3: Ejecutar el Instalador
Todavía como usuario oracle:
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- El instalador GUI se iniciará (requiere reenvío X11 si es SSH; use `ssh -X` o habilite X11).
- **Opciones de Instalación**:
  - Seleccione "Create and configure a database software only" o "Single instance database installation" (para la edición server).
  - ORACLE_HOME: `/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventory: `/u01/app/oraInventory`
  - Si es solo software (sin creación de BD), elija "Install database software only".
- Siga el asistente: Acepte los valores predeterminados donde sea posible, pero establezca contraseñas para SYS/SYSTEM.
- Ignore cualquier advertencia de "prereq" inicialmente—arregle después de la instalación si es necesario.

Si falla el GUI (por ejemplo, error DISPLAY), ejecute la instalación silenciosa:
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
Necesitará preparar un archivo de respuesta (ejemplo en el directorio extraído, por ejemplo, `db_install.rsp`). Edítelo con sus configuraciones (ORACLE_HOME, etc.) y ejecute.

#### Paso 4: Post-Instalación
1. **Ejecutar root.sh** (como root):
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **Establecer Variables de Entorno** (para el usuario oracle, agregue a `~/.bash_profile`):
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # Cámbielo a su SID
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **Crear una Base de Datos** (si no se hizo durante la instalación):
   ```
   dbca  # Database Configuration Assistant (GUI/silent)
   ```
   O use SQL*Plus para creación manual.

4. **Iniciar/Detener Servicios**:
   ```
   sqlplus / as sysdba
   STARTUP;  # O shutdown
   ```
   Agregue a systemd para inicio automático (cree `/etc/systemd/system/oracle.service` con exec a `dbstart`).

#### Solución de Problemas Comunes en Ubuntu 22.04
- **Errores de Glibc/Dependencias**: Oracle 12c espera glibc <=2.17. Ubuntu 22.04 tiene 2.35—use `ldd` para verificar, o instale bibliotecas de compatibilidad:
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  Si hay errores del enlazador, establezca `LD_PRELOAD` o use un contenedor Docker con Oracle Linux.
- **Problemas de Java/Display**: Asegúrese de que JDK 8 esté configurado (`java -version` debería mostrar 1.8). Para modo sin cabeza (headless): `export DISPLAY=:0`.
- **Memoria Insuficiente (Out of Memory)**: Aumente ulimit o RAM. Edite los parámetros de `runInstaller` si es necesario.
- **Parche 12.1.2**: Si no está incluido, descárguelo de My Oracle Support y aplíquelo con `opatch` después de la instalación.
- **Registros (Logs)**: Verifique `/u01/app/oraInventory/logs/installActions*.log` para ver errores.
- **Solución de Compatibilidad**: Algunos usuarios crean enlaces simbólicos de bibliotecas (por ejemplo, `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a`—investigue según el error).

#### Verificación
- Ejecute `sqlplus / as sysdba` y ejecute `SELECT * FROM v$version;`.
- Listener: `lsnrctl start`.

Si encuentra errores específicos, proporcione la salida del registro para más ayuda. Para documentación oficial (aunque centrada en RHEL), consulte la guía de instalación de Oracle 12c. Si esto es para un producto diferente (no DB), ¡aclare el contenido del tarball!