---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Clave SSH para la Implementación de JAR con GitHub Actions
translated: true
type: note
---

Para generar una clave SSH para GitHub Actions y desplegar un archivo JAR, sigue estos pasos:

1. **Generar un Par de Claves SSH**:
   - En tu máquina local o en un entorno seguro, ejecuta:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Si tu sistema no soporta Ed25519, usa:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Presiona Enter para aceptar la ubicación predeterminada del archivo y opcionalmente establece una frase de contraseña (recomendado para seguridad). Esto crea dos archivos:
     - `github-actions-deploy` (clave privada)
     - `github-actions-deploy.pub` (clave pública)

2. **Añadir la Clave Pública al Servidor Objetivo**:
   - Copia la clave pública:
     ```bash
     cat github-actions-deploy.pub
     ```
   - Inicia sesión en el servidor donde desplegarás el archivo JAR.
   - Añade la clave pública al archivo `~/.ssh/authorized_keys` en el servidor:
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - Asegúrate de que el archivo `authorized_keys` tenga los permisos correctos:
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **Almacenar la Clave Privada en los Secrets de GitHub**:
   - Ve a tu repositorio de GitHub: `Settings > Secrets and variables > Actions > Secrets`.
   - Haz clic en **New repository secret**.
   - Nombra el secret (por ejemplo, `SSH_PRIVATE_KEY`).
   - Pega el contenido de la clave privada (`github-actions-deploy`):
     ```bash
     cat github-actions-deploy
     ```
   - Guarda el secret.

4. **Configurar el Flujo de Trabajo de GitHub Actions**:
   - Crea o edita un archivo de flujo de trabajo (por ejemplo, `.github/workflows/deploy.yml`).
   - Añade un paso para usar la clave SSH para desplegar el JAR. A continuación, un flujo de trabajo de ejemplo:

     ```yaml
     name: Desplegar JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout del código
           uses: actions/checkout@v4

         - name: Configurar Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # Ajusta a tu versión de Java
             distribution: 'temurin'

         - name: Construir JAR
           run: mvn clean package # Ajusta para tu herramienta de construcción (por ejemplo, Gradle)

         - name: Instalar Clave SSH
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # Ver nota abajo

         - name: Añadir Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # Reemplaza <server-ip-or-hostname> con la IP o hostname de tu servidor

         - name: Desplegar JAR al Servidor
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # Ajusta para tu proceso de despliegue
     ```

   - **Notas**:
     - Reemplaza `target/your-app.jar` con la ruta a tu archivo JAR.
     - Reemplaza `user@<server-ip-or-hostname>` con el usuario SSH y la dirección de tu servidor.
     - Ajusta el comando de despliegue (por ejemplo, `sudo systemctl restart your-service`) para que coincida con cómo inicias o despliegas el JAR en tu servidor.
     - El paso `known_hosts` es crítico para evitar problemas de verificación del host SSH. Si conoces la clave host del servidor, puedes pre-popularla en el paso `shimataro/ssh-key-action`, o usar `ssh-keyscan` como se muestra.

5. **Asegurar el Flujo de Trabajo**:
   - Asegúrate de que la clave privada nunca se exponga en los logs o salidas.
   - Restringe los permisos del repositorio para prevenir acceso no autorizado a los secrets.
   - Si usas una frase de contraseña para la clave SSH, añádela como otro secret e inclúyela en el paso `shimataro/ssh-key-action`:
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **Probar el Flujo de Trabajo**:
   - Haz un push de un cambio a la rama `main` (o la rama especificada en el flujo de trabajo).
   - Monitorea el flujo de trabajo en la pestaña **Actions** de tu repositorio de GitHub para asegurarte de que el JAR se construye y despliega correctamente.

7. **Solución de Problemas**:
   - **Permission denied**: Verifica que la clave SSH esté correctamente añadida al `authorized_keys` del servidor y que el usuario tenga permiso para acceder al directorio objetivo.
   - **Host verification failed**: Asegúrate de que el paso `known_hosts` esté correctamente configurado con la IP o hostname del servidor.
   - **Build issues**: Confirma que la versión de Java y los comandos de construcción coincidan con la configuración de tu proyecto.

Esta configuración integra de forma segura el despliegue basado en SSH en tu flujo de trabajo de GitHub Actions para desplegar un archivo JAR. Si necesitas ajustes específicos (por ejemplo, para una configuración de servidor particular o herramienta de construcción), ¡avísame!