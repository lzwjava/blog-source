---
audio: false
generated: true
lang: es
layout: post
title: Construcción e Implementación de una Imagen de Docker
translated: true
type: note
---

Aquí tienes una guía paso a paso para construir una aplicación Spring Boot en una imagen Docker y desplegarla en un servidor:

### Prerrequisitos
1. **Java** (por ejemplo, JDK 17 o una versión compatible) instalado localmente.
2. **Maven** o **Gradle** (dependiendo de la configuración de tu proyecto Spring Boot).
3. **Docker** instalado en tu máquina local y en el servidor.
4. **Un proyecto Spring Boot** listo para containerizar.
5. **Acceso al servidor** (por ejemplo, vía SSH) con Docker instalado.

---

### Paso 1: Prepara tu aplicación Spring Boot
Asegúrate de que tu aplicación Spring Boot funcione localmente. Pruébala con:
```bash
mvn spring-boot:run  # Si usas Maven
# O
gradle bootRun       # Si usas Gradle
```

Asegúrate de que la aplicación se construye correctamente:
```bash
mvn clean package    # Maven
# O
gradle build         # Gradle
```
Esto genera un archivo `.jar` (por ejemplo, `target/myapp-1.0.0.jar`).

---

### Paso 2: Crea un Dockerfile
En el directorio raíz de tu proyecto (donde se encuentra el archivo `.jar`), crea un archivo llamado `Dockerfile` con el siguiente contenido:

```dockerfile
# Usa una imagen base oficial de OpenJDK
FROM openjdk:17-jdk-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo JAR de Spring Boot al contenedor
COPY target/myapp-1.0.0.jar app.jar

# Expone el puerto en el que corre tu app Spring Boot (por defecto es 8080)
EXPOSE 8080

# Ejecuta el archivo JAR
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Notas:**
- Reemplaza `myapp-1.0.0.jar` con el nombre real de tu archivo JAR.
- Ajusta la versión de Java (`openjdk:17-jdk-slim`) si tu aplicación usa una versión diferente.

---

### Paso 3: Construye la imagen Docker
Desde el directorio que contiene el `Dockerfile`, ejecuta:
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` etiqueta la imagen como `myapp` con la versión `latest`.
- El `.` le dice a Docker que use el directorio actual como contexto de construcción.

Verifica que la imagen fue creada:
```bash
docker images
```

---

### Paso 4: Prueba la imagen Docker localmente
Ejecuta el contenedor localmente para asegurarte de que funciona:
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` mapea el puerto 8080 de tu máquina al puerto 8080 en el contenedor.
- Abre un navegador o usa `curl` para probar (por ejemplo, `curl http://localhost:8080`).

Detén el contenedor con `Ctrl+C` o encuentra su ID con `docker ps` y detenlo:
```bash
docker stop <container-id>
```

---

### Paso 5: Sube la imagen a un registro de Docker (Opcional)
Para desplegar en un servidor, necesitarás subir la imagen a un registro como Docker Hub (o un registro privado). Si omites esto, transferirás la imagen manualmente.

1. Inicia sesión en Docker Hub:
   ```bash
   docker login
   ```
2. Etiqueta tu imagen:
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. Sube la imagen:
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### Paso 6: Despliega en el servidor
#### Opción 1: Usando un registro
1. Conéctate por SSH a tu servidor:
   ```bash
   ssh user@server-ip
   ```
2. Descarga la imagen:
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. Ejecuta el contenedor:
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` ejecuta el contenedor en modo desatendido (en segundo plano).

#### Opción 2: Transferencia manual
Si no usaste un registro:
1. Guarda la imagen localmente como un archivo `.tar`:
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. Transfiérelo al servidor (por ejemplo, vía SCP):
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. Conéctate por SSH al servidor:
   ```bash
   ssh user@server-ip
   ```
4. Carga la imagen:
   ```bash
   docker load -i myapp.tar
   ```
5. Ejecuta el contenedor:
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### Paso 7: Verifica el despliegue
Comprueba si el contenedor se está ejecutando:
```bash
docker ps
```

Prueba la aplicación desde el servidor o externamente:
- Si estás en el servidor: `curl http://localhost:8080`
- Si es externo: Usa la IP del servidor (por ejemplo, `http://server-ip:8080`), asegurándote de que el puerto esté abierto en el firewall del servidor.

---

### Opcional: Mejoras
- **Variables de Entorno**: Pasa configuraciones a tu aplicación:
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: Para configuraciones multi-contenedor, usa un archivo `docker-compose.yml`.
- **Política de Reinicio**: Añade `--restart unless-stopped` para asegurar que el contenedor se reinicie al reiniciar el servidor.

¡Avísame si necesitas ayuda con alguna parte específica!

---

Por la salida de error que proporcionaste, hay algunos problemas que impiden que tu comando `docker build` tenga éxito. Vamos a desglosarlos y resolverlos paso a paso.

---

### Problemas Identificados
1. **Falta el plugin `docker-buildx`**  
   Error: `fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`  
   Esto sugiere que Docker está intentando usar el plugin `buildx` (una herramienta de construcción moderna), pero no está instalado o configurado correctamente.

2. **Advertencia de desuso del constructor heredado**  
   Advertencia: `DEPRECATED: The legacy builder is deprecated...`  
   Docker recomienda cambiar a BuildKit (`buildx`), pero está recurriendo al constructor heredado, el cual está fallando.

3. **Docker Daemon no se está ejecutando**  
   Error: `Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`  
   El daemon de Docker (el servicio en segundo plano que gestiona los contenedores) no se está ejecutando en tu sistema.

4. **Errores de acceso a archivos**  
   Errores: `Can't add file ... to tar: io: read/write on closed pipe` y `Can't close tar writer...`  
   Estos son problemas secundarios causados por el fallo del proceso de construcción debido a que el daemon no se está ejecutando.

5. **Configuración de Proxy Detectada**  
   Tu sistema está usando proxies (`HTTP_PROXY` y `HTTPS_PROXY`). Esto podría interferir con Docker si no está configurado correctamente.

---

### Solución Paso a Paso

#### 1. Verifica que el Docker Daemon se esté ejecutando
El problema principal es que el daemon de Docker no se está ejecutando. Así es como solucionarlo:

- **En macOS** (asumiendo que usas Docker Desktop):
  1. Abre Docker Desktop desde tu carpeta de Aplicaciones o Spotlight.
  2. Asegúrate de que se esté ejecutando (verás que el icono de la ballena de Docker en la barra de menú se vuelve verde).
  3. Si no inicia:
     - Cierra Docker Desktop y reinícialo.
     - Busca actualizaciones: Docker Desktop > Check for Updates.
     - Si sigue fallando, reinstala Docker Desktop desde [docker.com](https://www.docker.com/products/docker-desktop/).

- **Verificar vía Terminal**:
  Ejecuta:
  ```bash
  docker info
  ```
  Si el daemon se está ejecutando, verás información del sistema. Si no, obtendrás el mismo error "Cannot connect".

- **Reiniciar el Daemon Manualmente** (si es necesario):
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

Una vez que el daemon se esté ejecutando, procede a los siguientes pasos.

---

#### 2. Instala el plugin `buildx` (Opcional pero Recomendado)
Dado que el constructor heredado está en desuso, configuremos `buildx`:

1. **Instalar `buildx`**:
   - Descarga el binario manualmente o usa las instrucciones de Docker:
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     (Comprueba la [última versión](https://github.com/docker/buildx/releases) para tu SO/arquitectura, por ejemplo, `darwin-arm64` para Macs M1/M2).

2. **Verificar la Instalación**:
   ```bash
   docker buildx version
   ```

3. **Establecer BuildKit como Predeterminado** (opcional):
   Añade esto a `~/.docker/config.json`:
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

Alternativamente, puedes omitir esto y usar el constructor heredado por ahora (ver Paso 4).

---

#### 3. Maneja la Configuración del Proxy
Tu configuración de proxy (`http://127.0.0.1:7890`) podría interferir con la capacidad de Docker para obtener imágenes. Configura Docker para usarlos:

1. **Vía Docker Desktop**:
   - Abre Docker Desktop > Settings > Resources > Proxies.
   - Habilita "Manual proxy configuration" e ingresa:
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - Aplica y Reinicia.

2. **Vía CLI** (si no usas Desktop):
   Crea o edita `~/.docker/config.json`:
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   Reinicia Docker después de editar.

---

#### 4. Reintenta la Construcción
Ahora que el daemon se está ejecutando y los proxies están configurados, intenta construir de nuevo:

```bash
docker build -t myapp:latest .
```

- Si instalaste `buildx`, usará BuildKit por defecto.
- Si omitiste `buildx`, añade `--progress=plain` para forzar el constructor heredado:
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. Soluciona el Error de `.git/hooks` (Si Persiste)
El error `.git/hooks/pre-rebase.sample` sugiere que Docker está intentando incluir archivos innecesarios en el contexto de construcción. Exclúyelos con un archivo `.dockerignore`:

1. Crea `.dockerignore` en el mismo directorio que tu `Dockerfile`:
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. Esto le dice a Docker que ignore la carpeta `.git` y todo en `target/` excepto tu archivo JAR.

3. Reintenta la construcción:
   ```bash
   docker build -t myapp:latest .
   ```

---

### Verificación Final
- Comprueba la imagen:
  ```bash
  docker images
  ```
- Ejecútala localmente:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- Prueba con `curl http://localhost:8080`.

---

### Próximos Pasos
Una vez que la imagen se construya con éxito, sigue los pasos de despliegue de mi respuesta anterior (por ejemplo, subir a un registro o transferir a un servidor). ¡Avísame si tienes más problemas!