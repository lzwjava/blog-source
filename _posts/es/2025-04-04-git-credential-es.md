---
audio: false
generated: true
lang: es
layout: post
title: Administrador de Credenciales de Git
translated: true
type: note
---

Estás usando **Git Credential Manager (GCM) versión 2.6.1** en **macOS** y te has encontrado con un problema donde `git config --global credential.helper manager-core` devuelve un error:

```
warning: credential.helper has multiple values
error: cannot overwrite multiple values with a single value
```

Esto sucede porque ya hay múltiples ayudantes de credenciales configurados en tu configuración de Git. Necesitas **borrar los valores existentes** antes de establecer uno nuevo.

---

### **🛠 Solucionar el Problema: Restablecer el Ayudante de Credenciales**
#### **Paso 1: Verificar los Ayudantes de Credenciales Actuales**
Ejecuta:
```sh
git config --global --get-all credential.helper
```
Esto listará todos los ayudantes de credenciales configurados.

#### **Paso 2: Anular los Ayudantes de Credenciales Anteriores**
Restablece todos los ayudantes de credenciales usando:
```sh
git config --global --unset-all credential.helper
```

#### **Paso 3: Establecer GCM como el Único Ayudante de Credenciales**
Ahora, establece **Git Credential Manager (GCM)** como el ayudante nuevamente:
```sh
git config --global credential.helper manager-core
```

#### **Paso 4: Verificar el Cambio**
Comprueba si está configurado correctamente:
```sh
git config --global --get credential.helper
```
Salida esperada:
```
manager-core
```

---

### **🛠 Alternativa: Usar `--replace-all`**
Si prefieres sobrescribir los valores existentes en lugar de anularlos primero, usa:
```sh
git config --global --replace-all credential.helper manager-core
```

---

### **🧩 Depuración Adicional**
Si sigues teniendo problemas, puedes revisar tu configuración global completa de Git:
```sh
git config --global --list
```
Si el problema persiste, ¡avísame! 🚀

---

Git Credential Manager (GCM) es un ayudante seguro de credenciales de Git que almacena y gestiona las credenciales de autenticación para repositorios Git HTTPS. Funciona con servicios como GitHub, GitLab, Bitbucket y Azure DevOps.

---

## **1. Instalar Git Credential Manager**
GCM está incluido con Git para Windows y las distribuciones oficiales de Git para macOS y Linux. Si no está instalado, descárgalo desde:

🔗 **[Git Credential Manager en GitHub](https://github.com/GitCredentialManager/git-credential-manager)**

### **Comprobar si GCM está instalado**
Ejecuta:
```sh
git credential-manager version
```
Si está instalado, verás un número de versión. Si no, instálalo manualmente.

---

## **2. Configurar Git para Usar GCM**
Ejecuta el siguiente comando:
```sh
git config --global credential.helper manager
```
Para macOS/Linux, usa:
```sh
git config --global credential.helper manager-core
```

Para verificar el ayudante de credenciales actual:
```sh
git config --global credential.helper
```

---

## **3. Autenticarse con un Servidor Git**
Una vez configurado, la primera vez que interactúes con un repositorio remoto a través de HTTPS (ej., `git clone`, `git pull`), GCM te pedirá las credenciales.

- Si usas GitHub, GitLab o Bitbucket, GCM abrirá un navegador para la autenticación OAuth.
- Si usas un token de acceso personal (PAT), introdúcelo en lugar de una contraseña.

---

## **4. Almacenar y Gestionar Credenciales**
GCM almacena las credenciales de forma segura en el almacén de credenciales del sistema operativo:
- **Windows**: Administrador de Credenciales de Windows
- **macOS**: Llavero de macOS
- **Linux**: Archivo cifrado con GPG (`~/.git-credentials` o `~/.gitconfig`)

Para añadir una credencial manualmente:
```sh
git credential approve
```

Para eliminar una credencial almacenada:
```sh
git credential reject https://github.com
```

Para borrar todas las credenciales:
```sh
git credential reject
```

---

## **5. Usar Git Credential Manager con Diferentes Proveedores de Git**
### **GitHub**
Usa un **Token de Acceso Personal (PAT)** en lugar de una contraseña:
```sh
git credential reject https://github.com
git pull
```
Se te pedirá que inicies sesión y introduzcas tu token.

### **GitLab**
Para GitLab, usa OAuth o un **PAT**:
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
Usa un **PAT** o la autenticación de Azure.

---

## **6. Depurar Problemas**
Si las credenciales no se guardan o recuperan correctamente:
1. Comprueba el ayudante de credenciales:
   ```sh
   git config --global credential.helper
   ```
2. Restablece Git Credential Manager:
   ```sh
   git credential reject https://your-git-service.com
   ```
3. Reinstala GCM si es necesario.

¿Necesitas ayuda para configurarlo para un servicio específico? 🚀