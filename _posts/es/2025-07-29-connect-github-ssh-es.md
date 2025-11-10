---
audio: false
generated: true
image: false
lang: es
layout: post
title: Conectarse a GitHub con SSH
translated: true
type: note
---

Para conectarte a GitHub usando SSH, sigue estos pasos basados en la documentación proporcionada por GitHub. Esta guía asume que estás empezando desde cero e incluye verificar la existencia de claves, generar una nueva clave, agregarla a GitHub y probar la conexión.

### 1. Verificar si existen claves SSH
Antes de crear una nueva clave SSH, verifica si ya tienes una:
- Abre una terminal (en macOS/Linux) o Git Bash (en Windows).
- Ejecuta:
  ```bash
  ls -al ~/.ssh
  ```
- Busca archivos como `id_rsa` e `id_rsa.pub` (o similares, por ejemplo, `id_ed25519`, `id_ed25519.pub`). Si existen, es posible que ya tengas una clave. Si deseas usar una clave existente, salta al paso 3. Si no, procede a generar una nueva clave.

### 2. Generar una nueva clave SSH
Si no tienes una clave SSH o quieres una nueva:
- En tu terminal, genera una nueva clave SSH:
  ```bash
  ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
  ```
  - Reemplaza `tu_email@ejemplo.com` con el correo electrónico asociado a tu cuenta de GitHub.
  - Si tu sistema no soporta `ed25519`, usa:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "tu_email@ejemplo.com"
    ```
- Cuando se te solicite, presiona Enter para guardar la clave en la ubicación predeterminada (`~/.ssh/id_ed25519` o `~/.ssh/id_rsa`).
- Opcionalmente, ingresa una frase de contraseña para mayor seguridad (o presiona Enter para no usar ninguna).

### 3. Agregar la clave SSH al agente SSH
El agente SSH gestiona tus claves para la autenticación:
- Inicia el agente SSH:
  ```bash
  eval "$(ssh-agent -s)"
  ```
- Agrega tu clave privada al agente:
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - Si usaste RSA, reemplaza `id_ed25519` con `id_rsa`.
- Si estableciste una frase de contraseña, se te pedirá que la ingreses.

### 4. Agregar la clave SSH a tu cuenta de GitHub
- Copia tu clave pública al portapapeles:
  - En macOS:
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - En Linux:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    Luego copia manualmente la salida.
  - En Windows (Git Bash):
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - Si usaste RSA, reemplaza `id_ed25519.pub` con `id_rsa.pub`.
- Ve a GitHub:
  - Inicia sesión en [GitHub](https://github.com).
  - Haz clic en tu foto de perfil (parte superior derecha) → **Settings** → **SSH and GPG keys** → **New SSH key** o **Add SSH key**.
  - Pega tu clave pública en el campo "Key", asígnale un título (por ejemplo, "Mi Portátil") y haz clic en **Add SSH key**.

### 5. Probar tu conexión SSH
Verifica que tu clave SSH funcione con GitHub:
- Ejecuta:
  ```bash
  ssh -T git@github.com
  ```
- Si se te solicita, confirma escribiendo `yes`.
- Deberías ver un mensaje como:
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  Esto confirma que tu conexión SSH está funcionando.

### 6. Configurar Git para usar SSH
Asegúrate de que tu repositorio Git use SSH para la autenticación:
- Verifica la URL remota de tu repositorio:
  ```bash
  git remote -v
  ```
- Si la URL comienza con `https://`, cámbiala a SSH:
  ```bash
  git remote set-url origin git@github.com:usuario/repositorio.git
  ```
  - Reemplaza `usuario/repositorio` con tu nombre de usuario y nombre del repositorio en GitHub.

### 7. Opcional: Gestionar frases de contraseña de claves SSH
Si estableciste una frase de contraseña, puedes configurar el agente SSH para evitar tener que ingresarla repetidamente:
- En macOS, agrega tu clave al llavero:
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- En Linux/Windows, el agente SSH normalmente solicita la frase de contraseña solo una vez por sesión.

### 8. Opcional: Usar Reenvío del Agente SSH o Claves de Implementación
- **Reenvío del Agente SSH (SSH Agent Forwarding)**: Si estás desplegando en un servidor, habilita el reenvío del agente para usar tus claves SSH locales de forma segura. Agrega a tu `~/.ssh/config`:
  ```bash
  Host ejemplo.com
      ForwardAgent yes
  ```
  Reemplaza `ejemplo.com` con el nombre de host de tu servidor.
- **Claves de Implementación (Deploy Keys)**: Para scripts automatizados, genera una clave SSH separada para cada servidor y agrégalas como una clave de implementación en la configuración de tu repositorio de GitHub.

### Resolución de problemas
- Si `ssh -T git@github.com` falla, asegúrate de:
  - Que tu clave pública se haya agregado correctamente a GitHub.
  - Que el agente SSH esté ejecutándose y tu clave esté agregada (usa `ssh-add -l` para listar las claves cargadas).
  - Que los permisos de los archivos sean correctos:
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- Para más problemas, consulta la guía de resolución de problemas de GitHub.

Ahora puedes usar SSH para interactuar con GitHub de forma segura sin tener que ingresar credenciales repetidamente.

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)