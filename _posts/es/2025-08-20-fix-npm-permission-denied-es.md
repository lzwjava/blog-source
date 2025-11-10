---
audio: false
generated: true
image: false
lang: es
layout: post
title: Cómo Solucionar el Error de Permiso Denegado de NPM
translated: true
type: note
---

El error que estás experimentando, `EACCES: permission denied`, significa que tu usuario actual **no tiene permisos de escritura** en el directorio `/usr/local/lib/node_modules`. Este es un problema común al instalar paquetes npm globales en Linux o macOS.

### **Cómo solucionar este problema**

#### **Opción 1: Usar `sudo` (No recomendado para uso regular)**
Puedes usar `sudo` para ejecutar el comando como usuario root, pero esto **no es recomendable** para uso regular, ya que puede causar problemas de permisos con los paquetes npm más adelante.

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **Opción 2: Cambiar el directorio por defecto de npm (Recomendado)**
La mejor práctica es configurar npm para usar un directorio en tu carpeta personal donde tengas permisos de escritura.

1. **Crear un directorio global para npm en tu carpeta personal:**
   ```bash
   mkdir ~/.npm-global
   ```
2. **Configurar npm para usar este directorio:**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **Agregar el nuevo directorio a tu `PATH`:**
   Abre tu archivo de configuración del shell (por ejemplo, `~/.bashrc`, `~/.zshrc`, o `~/.profile`) y agrega esta línea:
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   Luego, recarga tu shell:
   ```bash
   source ~/.bashrc  # o ~/.zshrc, ~/.profile
   ```
4. **Reintentar la instalación:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **Opción 3: Corregir los permisos de `/usr/local` (Avanzado)**
Si deseas seguir usando `/usr/local`, puedes cambiar su propiedad a tu usuario:
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
Luego reintenta la instalación.

---

**Recomendación:** Usa la **Opción 2** para evitar problemas de permisos en el futuro.