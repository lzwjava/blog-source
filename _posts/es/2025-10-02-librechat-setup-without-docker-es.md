---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Configuración De LibreChat Sin Docker Compose
translated: true
type: note
---

Sí, puedes configurar LibreChat sin Docker Compose usando comandos individuales `docker run` o incluso un método sin Docker (instalación manual con Node.js, Yarn, MongoDB y MeiliSearch). Esto evita descargar el binario `docker-compose` en sí (que es pequeño, ~20-30MB, pero supongo que te refieres a las descargas totales de imágenes que suman ~70MB+ para los servicios de LibreChat). Sin embargo, las imágenes principales de Docker (por ejemplo, para la aplicación, MongoDB, MeiliSearch) siguen siendo alrededor de 500MB-1GB en total cuando se descargan—Docker Compose es solo una herramienta de orquestación sobre Docker, no el principal consumidor de ancho de banda. Descargar las imágenes sobre una conexión 4G/5G lenta seguirá siendo el cuello de botella, pero puedes mitigarlo.

A continuación, describiré las opciones, priorizando primero los consejos para ahorrar ancho de banda. Si los datos móviles son muy limitados, considera compartir conexión a una red WiFi temporalmente o usar una configuración pre-descargada en otra máquina (por ejemplo, exportar/importar imágenes via `docker save`/`docker load`).

### Consejos para Ahorrar Ancho de Banda en Cualquier Configuración Basada en Docker
- **Pre-descargar imágenes en una conexión más rápida**: En otro dispositivo con mejor internet, ejecuta `docker pull node:20-alpine` (para la app), `docker pull mongo:7` (base de datos), y `docker pull getmeili/meilisearch:v1.10` (búsqueda). Luego guárdalas en archivos:
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  Transfiere los archivos .tar via USB/unidad (total ~500-800MB comprimidos), luego en tu máquina Ubuntu: `docker load -i librechat-app.tar` etc. No se necesita descarga en línea.
- **Usar alternativas más ligeras**: Para pruebas, omite MeiliSearch inicialmente (es opcional para la búsqueda; desactívalo en la configuración). La imagen de MongoDB es ~400MB—usa una instalación local de MongoDB en su lugar (ver la sección sin Docker a continuación) para ahorrar ~400MB.
- **Monitorear el uso**: Usa `docker pull --quiet` o herramientas como `watch docker images` para rastrear.
- **Proxy o caché**: Si tienes un espejo de Docker Hub o un proxy, configúralo en `/etc/docker/daemon.json` para acelerar las descargas.

### Opción 1: Docker Puro (Sin Compose) – Equivalente a la Configuración con Compose
Puedes replicar el comportamiento de `docker-compose.yml` con `docker run` y `docker network`. Esto descarga las mismas imágenes pero te permite controlar cada paso. La descarga total sigue siendo ~700MB+ (compilación de la app + bases de datos).

1. **Crear una red de Docker** (aísla los servicios):
   ```
   docker network create librechat-network
   ```

2. **Ejecutar MongoDB** (reemplaza `your_mongo_key` con una contraseña fuerte):
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - Crea `./data/mongodb` para persistencia.

3. **Ejecutar MeiliSearch** (reemplaza `your_meili_key`):
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - Omite si el ancho de banda es ajustado; desactívalo en la configuración de la app más tarde.

4. **Clonar y Compilar/Ejecutar la App LibreChat**:
   - Clona el repositorio si no se ha hecho: `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat` (~50MB de descarga para el repo).
   - Compila la imagen (esto descarga la base de Node.js ~200MB y construye las capas de la app):
     ```
     docker build -t librechat-app .
     ```
   - Ejecútala (se enlaza a la BD, usa variables de entorno—crea un archivo `.env` como en mi respuesta anterior):
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - En `.env`, establece `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` y `MEILI_HOST=http://meilisearch:7700` etc.

5. **Acceso**: `http://localhost:3080`. Registros: `docker logs -f librechat`.

- **Detener/Limpieza**: `docker stop mongodb meilisearch librechat && docker rm them`.
- **Pros/Contras**: Igual que con Compose, pero más manual. Sigue siendo pesado en datos para las descargas/compilaciones de imágenes.

### Opción 2: Instalación Sin Docker (Manual, Sin Descargas de Imágenes) – Recomendado para Bajo Ancho de Banda
Instala las dependencias de forma nativa en Ubuntu. Esto evita toda la sobrecarga de Docker (~0MB para contenedores; solo descargas de paquetes via apt/yarn, totalizando ~200-300MB). Usa las configuraciones de Python/Node de tu sistema indirectamente.

#### Prerrequisitos (Instalar Una Vez)
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # Paquete oficial de MongoDB; Binario de MeiliSearch ~50MB
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js: Si no es v20+, instálalo via nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`, luego `nvm install 20`.
- Yarn: `npm install -g yarn`.
- Configuración de MongoDB: Edita `/etc/mongod.conf` para vincular a localhost, reinicia.

#### Pasos de Instalación
1. **Clonar Repositorio**:
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **Instalar Dependencias**:
   ```
   yarn install  # ~100-200MB de descargas para paquetes
   ```

3. **Configurar `.env`** (copia de `.env.example`):
   - `cp .env.example .env && nano .env`
   - Cambios clave:
     - Mongo: `MONGODB_URI=mongodb://localhost:27017/LibreChat` (crear usuario de BD si es necesario via shell `mongo`).
     - Meili: `MEILI_HOST=http://localhost:7700` y `MEILI_MASTER_KEY=your_key`.
     - Desactivar búsqueda si se omite Meili: `SEARCH=false`.
     - Añadir claves de IA según sea necesario.

4. **Compilar y Ejecutar**:
   - En una terminal: `yarn run backend` (inicia la API en el puerto 3090).
   - En otra: `yarn run frontend` (inicia la UI en el puerto 3080).
   - O usar PM2 para producción: `yarn global add pm2 && pm2 start yarn --name backend -- run backend` etc.

5. **Acceso**: `http://localhost:3080`. Crear cuenta y configurar.

- **Datos**: MongoDB almacena en `/var/lib/mongodb`, Meili en `/var/lib/meilisearch`.
- **Solución de Problemas**:
  - Autenticación de Mongo: Ejecutar `mongo` y crear usuario: `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`.
  - Puertos/Firewall: `sudo ufw allow 3080,3090,7700`.
  - Actualizaciones: `git pull && yarn install && restart services`.
- **Pros**: Más ligero en ancho de banda (sin contenedores), usa los recursos del sistema directamente. Contras: Más complicado de configurar, posibles conflictos de dependencias (por ejemplo, con tu Python 3.13, pero Node es separado).

Si los datos móviles son extremadamente limitados, el método sin Docker es el mejor—hazlo por etapas, monitoreando con `du -sh` en los directorios. Para errores, comparte los registros (por ejemplo, de `yarn run backend`). Guía oficial sin Docker: https://docs.librechat.ai/install/installation/manual_install.html. Si necesitas integración con Ollama para IA local (ahorra costos de API), instálalo por separado via su script (~100MB). ¡Avísame si necesitas ajustes!