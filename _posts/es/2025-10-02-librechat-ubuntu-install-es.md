---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Instalación de LibreChat en Ubuntu
translated: true
type: note
---

### Instalación de LibreChat en Ubuntu 24.04 LTS

LibreChat es una plataforma de chat de IA de código abierto que admite múltiples modelos de IA (por ejemplo, OpenAI, Gemini, Ollama) a través de una interfaz web. El método de instalación recomendado es usar Docker Compose, ya que es simple, maneja dependencias como MongoDB y MeiliSearch automáticamente y funciona de forma confiable en Ubuntu. Tu sistema (Ubuntu 24.04.2 LTS con Python 3.13.4) cumple con los requisitos, pero necesitarás instalar Docker y Git primero.

#### Prerrequisitos
1.  **Actualiza tu sistema**:
    ```
    sudo apt update && sudo apt upgrade -y
    ```

2.  **Instala Git** (si no está ya instalado):
    ```
    sudo apt install git -y
    ```

3.  **Instala Docker y Docker Compose**:
    - Instala Docker:
      ```
      sudo apt install docker.io -y
      sudo systemctl start docker
      sudo systemctl enable docker
      sudo usermod -aG docker $USER
      ```
      Cierra sesión y vuelve a iniciarla (o ejecuta `newgrp docker`) para que los cambios de grupo surtan efecto.
    - Instala Docker Compose (última versión):
      ```
      sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      sudo chmod +x /usr/local/bin/docker-compose
      ```
      Verifica con `docker-compose --version`.

#### Pasos de Instalación
1.  **Clona el repositorio de LibreChat**:
    ```
    cd ~/projects  # O tu directorio preferido
    git clone https://github.com/danny-avila/LibreChat.git
    cd LibreChat
    ```

2.  **Copia y configura el archivo de entorno**:
    - Copia el archivo de ejemplo:
      ```
      cp .env.example .env
      ```
    - Edita `.env` con un editor de texto (por ejemplo, `nano .env`). Configuraciones clave a actualizar:
      - Establece una clave maestra de MongoDB: Genera una contraseña segura y establece `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` y `MONGODB_MASTER_KEY=tu_clave_generada_aqui`.
      - Para MeiliSearch: Establece `MEILI_MASTER_KEY=tu_clave_generada_aqui` (genera una clave segura).
      - Añade claves API de IA si es necesario (por ejemplo, `OPENAI_API_KEY=tu_clave_openai`). Para modelos locales como Ollama, no se requiere clave inicialmente.
      - Guarda y sal. Para todas las opciones de configuración, consulta la documentación.

3.  **Inicia LibreChat con Docker Compose**:
    ```
    docker-compose up -d
    ```
    - Esto descarga las imágenes, inicia los servicios (aplicación LibreChat, MongoDB, MeiliSearch) y se ejecuta en modo desatendido.
    - Espera a que se inicie completamente (verifica con `docker-compose logs -f`).

4.  **Accede a LibreChat**:
    - Abre tu navegador y ve a `http://localhost:3080`.
    - Crea una cuenta en la página de inicio de sesión.
    - Selecciona un modelo de IA (configura los endpoints en los ajustes) y comienza a chatear.

#### Consejos Post-Instalación
-   **Detener/Actualizar**: Ejecuta `docker-compose down` para detener, luego `git pull` y `docker-compose up -d --build` para actualizar.
-   **Persistencia de Datos**: Los volúmenes se crean automáticamente para los datos de MongoDB (en `./data/mongodb`).
-   **Solución de Problemas**:
    - Si hay conflicto de puertos, edita `docker-compose.yml` para cambiar `3080:3080`.
    - Para acceso sin interfaz gráfica/en servidor, usa la IP de tu servidor (por ejemplo, `http://tu-ip-servidor:3080`) y asegúrate de que el firewall permita el puerto 3080 (`sudo ufw allow 3080`).
    - Si usas LLMs locales, instala Ollama por separado y añádelo como un endpoint en `.env`.
-   **Alternativa: Método NPM** (sin Docker): Si lo prefieres, instala Node.js 18+, Yarn, MongoDB y MeiliSearch manualmente, luego ejecuta `yarn install` y `yarn run frontend` + `yarn run backend`. Pero Docker es muy recomendado por su simplicidad.

Esto debería permitirte tenerlo funcionando rápidamente. Si encuentras errores, comparte la salida para obtener más ayuda.

[Documentación Oficial de LibreChat](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Guía de Docker para Ubuntu](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[Tutorial de It's FOSS](https://itsfoss.com/librechat-linux/)