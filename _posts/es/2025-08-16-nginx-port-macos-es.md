---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía para Cambiar el Puerto de Nginx en macOS
translated: true
type: note
---

Quieres que Nginx en macOS escuche en un **puerto diferente** al predeterminado (80 para HTTP, 443 para HTTPS). Aquí tienes una guía clara paso a paso:

---

### 1. Localiza tu archivo de configuración de Nginx

* Si lo instalaste a través de **Homebrew**, la configuración predeterminada suele ser:

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  o, en Apple Silicon:

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* Si lo instalaste manualmente, puede estar en `/usr/local/nginx/conf/nginx.conf`.

---

### 2. Edita la directiva `listen`

1. Abre la configuración en un editor de texto:

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. Encuentra el bloque `server`:

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. Cambia `listen 80;` por el puerto que desees, por ejemplo, 8080:

   ```nginx
   listen 8080;
   ```

---

### 3. Prueba la configuración

Ejecuta:

```bash
nginx -t
```

* Si dice `syntax is ok` y `test is successful`, tu configuración es válida.
* Si hay errores, revisa los números de línea que indica.

---

### 4. Reinicia Nginx

* Si se instaló via Homebrew:

```bash
brew services restart nginx
```

* O manualmente:

```bash
sudo nginx -s reload
```

---

### 5. Accede mediante el nuevo puerto

* En tu navegador o con curl:

```
http://localhost:8080
```

---

**Notas Adicionales:**

* Los puertos **<1024** requieren `sudo` en macOS. Por lo tanto, usar puertos como 80 necesitará permisos de root, pero 8080 o 3000 no.
* Si quieres ejecutar múltiples servidores Nginx simultáneamente, cada uno **debe tener un puerto único**.

---

También puedo darte un **truco rápido para ejecutar Nginx temporalmente en cualquier puerto sin editar nginx.conf** usando un flag de línea de comandos. Es útil para pruebas. ¿Quieres que te lo muestre?