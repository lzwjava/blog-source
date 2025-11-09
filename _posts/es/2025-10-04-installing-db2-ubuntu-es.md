---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de IBM Db2 en Ubuntu
translated: true
type: note
---

### Instalación de IBM Db2 12.1.2 en Ubuntu 22.04 o 24.04 desde `ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz`

IBM Db2 versión 12.1.2 (Fix Pack 2) es compatible con versiones recientes de Ubuntu, incluyendo 22.04 (Jammy) y 24.04 (Noble), siempre que su sistema cumpla con los requisitos previos de hardware y software. Esta instalación utiliza el instalador gráfico o silencioso desde el archivo tar.gz. Se recomienda revisar la documentación oficial de IBM para Db2 12.1 (por ejemplo, en el IBM Knowledge Center o la página de Descargas de Db2) para obtener los detalles más recientes, ya que los requisitos pueden variar según la edición (aquí, Server Edition).

**Notas Importantes Antes de Comenzar:**
- **Requisitos del Sistema**:
  - Arquitectura x86_64 de 64 bits (Intel/AMD).
  - Al menos 4 GB de RAM (8 GB recomendados) y 2 GB de espacio de intercambio (swap).
  - 10 GB de espacio libre en disco para la instalación base (más para los datos).
  - Acceso root o sudo.
  - Versión del kernel: Ubuntu 22.04/24.04 debería funcionar, pero asegúrese de que su kernel sea al menos 3.10 (verifique con `uname -r`).
  - Firewall: Desactive temporalmente o abra los puertos (puerto predeterminado de Db2: 50000 para TCP/IP).
- **Problemas Potenciales en Ubuntu**:
  - Db2 se prueba principalmente en RHEL/SUSE, pero Ubuntu es compatible a través de paquetes Debian. Es posible que necesite resolver dependencias de bibliotecas.
  - Si está en Ubuntu 24.04, es muy nuevo—pruebe primero en una máquina virtual, ya que la certificación completa podría retrasarse.
  - Esto instala la Server Edition. Para otras ediciones (por ejemplo, Express-C), descargue el archivo tar.gz apropiado.
- **Copia de Seguridad**: Haga una copia de seguridad de su sistema antes de proceder.
- Descargue el archivo desde el sitio oficial de IBM Passport Advantage o de Descargas de Db2 (requiere una IBM ID).

#### Paso 1: Instalar los Prerrequisitos
Actualice su sistema e instale las bibliotecas requeridas. Db2 necesita E/S asíncrona, PAM y otras bibliotecas de tiempo de ejecución.

```bash
sudo apt update
sudo apt upgrade -y

# Instalar paquetes esenciales (comunes para Db2 en Ubuntu/Debian)
sudo apt install -y libaio1 libpam0g:i386 libncurses5 libstdc++6:i386 \
    unixodbc unixodbc-dev libxml2 libxslt1.1 wget curl

# Para Ubuntu 24.04, posiblemente necesite también:
sudo apt install -y libc6:i386 libgcc-s1:i386

# Verificar compatibilidad de glibc (Db2 12.1 requiere glibc 2.17+)
ldd --version  # Debería mostrar glibc 2.35+ en Ubuntu 22.04/24.04
```

Si encuentra bibliotecas de 32 bits faltantes (por ejemplo, para componentes de Java), habilite multiarquitectura:
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

#### Paso 2: Preparar los Archivos de Instalación
1. Cree un directorio temporal para la extracción (por ejemplo, `/tmp/db2_install`):
   ```bash
   sudo mkdir -p /tmp/db2_install
   cd /tmp/db2_install
   ```

2. Copie el archivo tar.gz a este directorio (asumiendo que lo tiene descargado, por ejemplo, en `~/Downloads`):
   ```bash
   cp ~/Downloads/ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz .
   ```

3. Extraiga el archivo:
   ```bash
   tar -xzf ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz
   ```
   - Esto crea un directorio como `db2` o `sqllib` que contiene los archivos del instalador (por ejemplo, `db2setup`).

4. Cambie al directorio extraído:
   ```bash
   cd db2  # O cualquiera que sea el directorio principal—verifique con `ls`
   ```

#### Paso 3: Ejecutar el Instalador
Db2 proporciona un instalador gráfico (`db2setup`) o un archivo de respuesta para instalaciones silenciosas. Ejecute como root/sudo.

**Opción A: Instalador Gráfico (Recomendado para la Primera Vez)**
1. Asegúrese de tener una pantalla (si está en un servidor sin GUI, use reenvío X con SSH: `ssh -X usuario@host`).
2. Ejecute el instalador:
   ```bash
   sudo ./db2setup
   ```
   - El asistente lo guiará:
     - Acepte la licencia.
     - Elija la instalación "Típica" para Server Edition.
     - Seleccione la ruta de instalación (predeterminada: `/opt/ibm/db2/V12.1`—asegúrese de que `/opt/ibm` exista y sea escribible; créelo con `sudo mkdir -p /opt/ibm` si es necesario).
     - Cree una instancia de Db2 (por ejemplo, "db2inst1")—esto configura el usuario administrador de la base de datos.
     - Establezca la autenticación (por ejemplo, local o LDAP).
     - Habilite características como SQL Procedural Language si es necesario.
   - El instalador compilará y configurará la instancia.

**Opción B: Instalación Silenciosa (No Interactiva)**
Si prefiere usar scripts:
1. Genere un archivo de respuesta durante una prueba:
   ```bash
   sudo ./db2setup -g  # Genera `db2setup.rsp` en el directorio actual
   ```
   Edite `db2setup.rsp` (por ejemplo, establezca `LIC_AGREEMENT=ACCEPT`, `INSTALL_TYPE=TYPICAL`, `CREATE_DB2_INSTANCE=YES`, etc.).

2. Ejecute la instalación silenciosa:
   ```bash
   sudo ./db2setup -u db2setup.rsp
   ```

- La instalación toma de 10 a 30 minutos. Observe si hay errores en `/tmp/db2setup.log`.

#### Paso 4: Configuración Posterior a la Instalación
1. **Verificar la Instalación**:
   - Inicie sesión como el propietario de la instancia (por ejemplo, `db2inst1`—creado durante la instalación):
     ```bash
     su - db2inst1
     ```
   - Verifique la versión de Db2:
     ```bash
     db2level
     ```
   - Inicie la instancia:
     ```bash
     db2start
     ```
   - Pruebe la conexión:
     ```bash
     db2 connect to sample  # Crea una base de datos de ejemplo si no existe
     db2 "select * from sysibm.sysdummy1"
     db2 disconnect all
     db2stop  # Cuando termine
     ```

2. **Crear una Base de Datos (Si No Se Hizo Durante la Instalación)**:
   ```bash
   su - db2inst1
   db2sampl  # Opcional: Crea la base de datos de ejemplo
   # O crear una base de datos personalizada:
   db2 "create database MYDB"
   db2 connect to MYDB
   ```

3. **Configuración del Entorno**:
   - Agregue Db2 al PATH para el usuario de la instancia (agregue a `~/.bashrc`):
     ```bash
     export PATH=/opt/ibm/db2/V12.1/bin:$PATH
     export DB2INSTANCE=db2inst1
     ```
   - Recargue: `source ~/.bashrc`.

4. **Habilitar Acceso Remoto (Opcional)**:
   - Actualice los servicios:
     ```bash
     su - db2inst1
     db2 update dbm cfg using SVCENAME db2i  # O su puerto
     db2set DB2COMM=TCPIP
     db2start
     ```
   - Edite `/etc/services` (como root) para agregar:
     ```
     db2i          50000/tcp
     ```
   - Reinicie la instancia.

5. **Configuración del Firewall**:
   ```bash
   sudo ufw allow 50000/tcp  # Para el puerto predeterminado de Db2
   sudo ufw reload
   ```

#### Paso 5: Aplicar Actualizaciones (Recomendado)
- Descargue y aplique el último Fix Pack si es necesario (12.1.2 es FP2; verifique si hay FP3+):
  - Use la herramienta `db2iupdt` o el instalador de actualizaciones de IBM.
- Monitoree los registros: `/tmp/db2` o `/opt/ibm/db2/V12.1/instance/db2inst1/sqllib/db2dump`.

#### Solución de Problemas Comunes
- **"No suitable Java runtime"**: Instale OpenJDK: `sudo apt install openjdk-11-jre-headless`.
- **Errores de Bibliotecas (por ejemplo, libaio.so)**: Asegúrese de que `libaio1` esté instalado y ejecute `sudo ldconfig`.
- **Permiso Denegado**: Ejecute el instalador como root; asegure la propiedad de `/opt/ibm`: `sudo chown -R db2inst1:db2iadm1 /opt/ibm/db2`.
- **Incompatibilidad de Glibc**: Poco probable en Ubuntu 22.04/24.04, pero si surgen problemas, considere una instalación en contenedor (Docker).
- **Falla la Instalación Silenciosa**: Revise `db2setup.log` para encontrar pistas.
- **Específico de Ubuntu 24.04**: Si fallan las dependencias de bibliotecas, posiblemente necesite agregar PPAs o compilar bibliotecas faltantes. Pruebe primero en 22.04.
- ¿Errores? Busque en los foros de soporte de IBM o ejecute `db2diag` como el usuario de la instancia.

Si encuentra errores específicos, proporcione detalles para una ayuda más dirigida. Para uso en producción, considere los entornos certificados por IBM o consultar al soporte. ¡Éxito! Su instancia de Db2 ahora debería estar lista para la creación y uso de bases de datos.