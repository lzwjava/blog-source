---
audio: false
date: 2025-09-14
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Deshabilitar la Autenticación de Inicio de Sesión de LibreChat
translated: true
type: note
---

Para que **LibreChat** funcione sin requerir inicios de sesión frecuentes (o deshabilitar el inicio de sesión por completo), puedes ajustar la configuración de autenticación. Aquí están los pasos para resolver el problema:

---

### **1. Deshabilitar la Autenticación (No se Requiere Inicio de Sesión)**
Si quieres que **LibreChat esté completamente abierto** (sin inicio de sesión), modifica la configuración:

#### **Opción A: Variables de Entorno (Recomendado)**
Establece lo siguiente en tu archivo `.env` (o en las variables de entorno):
```env
# Deshabilitar la autenticación por completo
AUTHENTICATION=false
```
Luego, reinicia LibreChat:
```bash
docker compose down && docker compose up -d  # Si usas Docker
# O
npm run build && npm run start  # Si lo ejecutas localmente
```

#### **Opción B: Modificar `config.yaml`**
Si estás usando un archivo `config.yaml`, añade:
```yaml
auth:
  enabled: false
```

---

### **2. Solucionar Problemas de Cierre de Sesión Frecuente (Si Aún Quieres Inicio de Sesión)**
Si **quieres mantener la autenticación** pero solucionar el problema de cierre de sesión frecuente, prueba estas soluciones:

#### **A. Aumentar el Tiempo de Expiración de la Sesión/Cookie**
Modifica la configuración de sesión en `.env`:
```env
# Extiende el tiempo de espera de la sesión (en segundos, ej., 7 días = 604800)
SESSION_EXPIRY=604800

# Asegúrate de que las cookies sean seguras (si usas HTTPS)
COOKIE_SECURE=true  # Establécelo en false si pruebas en HTTP
COOKIE_SAME_SITE=lax
```

#### **B. Usar un Almacén de Sesiones Persistente**
Por defecto, LibreChat puede usar sesiones en memoria (que se reinician al reiniciar). Cambia a un **almacén de sesiones respaldado por base de datos** (ej., Redis o PostgreSQL):

1. **Instala Redis** (si aún no está instalado):
   ```bash
   docker run -d --name redis -p 6379:6379 redis
   ```
2. Actualiza `.env`:
   ```env
   SESSION_STORE=redis
   REDIS_URL=redis://localhost:6379
   ```

#### **C. Verificar la Configuración del Proxy Inverso (Si Usas Nginx/Apache)**
Si estás detrás de un proxy (ej., Nginx), asegúrate de que:
- Las cookies se reenvían correctamente.
- `ProxyPass` incluye directivas de `cookie`.

Ejemplo de configuración de Nginx:
```nginx
location / {
    proxy_pass http://localhost:3080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_cookie_path / /;  # Asegura que las cookies no tengan un ámbito incorrecto
}
```

#### **D. Limpiar la Caché del Navegador y Probar en Modo Incógnito**
A veces, la caché del navegador o las cookies corruptas causan problemas. Prueba:
- Borrar las cookies para `librechat.ejemplo.com`.
- Probar en **Modo Incógnito** o en un navegador diferente.

---

### **3. Depurar Problemas de Cookies**
Si las cookies aún no persisten:
1. **Revisa las DevTools del navegador** (`F12` > **Application** > **Cookies**) para ver si `connect.sid` (o similar) se está estableciendo.
2. **Verifica el atributo `SameSite`** (debería ser `Lax` o `None` si es cross-site).
3. **Asegúrate de que el `Domain` es correcto** (ej., `.ejemplo.com` para subdominios).

---

### **4. Actualizar LibreChat**
Si estás en una versión antigua, los errores podrían estar solucionados en versiones más recientes:
```bash
git pull origin main
docker compose down && docker compose up -d --build
```

---

### **Notas Finales**
- **Advertencia de Seguridad**: Deshabilitar la autenticación (`AUTHENTICATION=false`) hace que LibreChat sea **accesible públicamente**. Solo haz esto para redes internas o de confianza.
- **HTTPS Requerido**: Si usas cookies, asegúrate de que tu sitio use **HTTPS** (o establece `COOKIE_SECURE=false` para pruebas).