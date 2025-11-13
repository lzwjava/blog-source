---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de CORS y HTTPS para Nginx
translated: true
type: note
---

```nginx
# Define un mapa para manejar los orígenes permitidos
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### Qué hace
- Crea una variable `$cors_origin` basada en el valor del encabezado `Origin` entrante (`$http_origin`).
- Si la solicitud proviene de `http://localhost:3000`, `https://example.com` o `https://www.example.com`, devuelve ese mismo origen exacto.
- Para cualquier otro origen (o sin origen), utiliza por defecto `https://example.com`.
- Esto se usa después para establecer dinámicamente el encabezado `Access-Control-Allow-Origin`, habilitando CORS solo para los dominios front-end de confianza.

---

```nginx
# Redirigir HTTP a HTTPS
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### Qué hace
- Escucha en el puerto 80 (HTTP).
- Coincide con las solicitudes a `example.com` o `api.example.com`.
- Redirige permanentemente (301) todo el tráfico a la versión HTTPS de la misma URL.
- Fuerza conexiones seguras; no se permite acceso HTTP plano.

---

```nginx
# Configuración principal del sitio para example.com
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### Qué hace
- **Servidor HTTPS** para `example.com` en el puerto 443 con SSL habilitado.
- Utiliza certificados de **Let's Encrypt** (renovables automáticamente, gratuitos).
- Impone versiones TLS modernas (`TLSv1.2`, `TLSv1.3`) y cifrados fuertes para seguridad.
- Sirve archivos estáticos desde `/home/project/project-web`.
- Intenta servir el archivo solicitado → directorio → 404.
- Establece **encabezados de caché**:
  - Imágenes: caché por 30 días.
  - JS/CSS: caché por 12 horas.
- Todos los errores 404 se redirigen a `index.html` → habilita el enrutamiento de **SPA (Single Page App)** (ej. React, Vue).

---

```nginx
# Configuración de API para api.example.com
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # Limpia cualquier encabezado Access-Control preexistente
        more_clear_headers 'Access-Control-Allow-Origin';

        # Maneja solicitudes CORS preflight
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### Qué hace
- **Proxy inverso HTTPS** para `api.example.com`.
- Utiliza un **certificado Let's Encrypt separado** (probablemente debido a múltiples dominios/SANs).
- Todo el tráfico se redirige mediante proxy a un **backend local** ejecutándose en `localhost:5000` (ej. Flask, Node.js, etc.).

#### Manejo de CORS
- Utiliza el mapa `$cors_origin` para **permitir dinámicamente** solo orígenes aprobados.
- **Limpia cualquier** `Access-Control-Allow-Origin` existente para prevenir conflictos.
- Maneja **preflight OPTIONS**:
  - Devuelve inmediatamente `204 No Content`.
  - Permite métodos y encabezados comunes.
  - Almacena en caché la preflight por 1 hora (`Max-Age: 3600`).
- Para las solicitudes reales, agrega encabezados CORS con `always` para que aparezcan incluso en respuestas de error.

#### Configuración del Proxy
- Reenvía la IP real del cliente y la información del protocolo al backend.
- Tiempos de espera altos (10 minutos) → adecuado para operaciones API de larga duración (ej. carga de archivos, cálculos pesados).

---

### Resumen de la Arquitectura

| Componente           | Propósito |
|---------------------|--------|
| `example.com`       | Sirve SPA estático (React/Vue/etc.) |
| `api.example.com`   | Puerta de enlace API segura → backend en puerto 5000 |
| HTTP → HTTPS        | Todo el tráfico forzado sobre TLS |
| CORS                | Restringido a `example.com`, `www` y `localhost:3000` |
| Caché               | Optimizado para rendimiento |
| SSL                 | Let's Encrypt, cifrados modernos |

### Notas de Seguridad
- Configuración TLS fuerte (probablemente A+ en SSL Labs).
- CORS **no es comodín** → previene que sitios no autorizados llamen a la API.
- Preflight manejado eficientemente.
- IP real reenviada → útil para registro/limitación de tasa en el backend.

¡Avísame si quieres un diagrama o una versión Dockerizada!