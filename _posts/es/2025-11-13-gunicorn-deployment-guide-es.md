---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Implementación de Gunicorn en Producción
translated: true
type: note
---

Gunicorn (Green Unicorn) es un servidor HTTP WSGI popular para aplicaciones web Python. Es ampliamente utilizado en producción para servir aplicaciones construidas con frameworks como Flask, Django, FastAPI, o cualquier aplicación compatible con WSGI. A diferencia de los servidores de desarrollo (por ejemplo, el servidor integrado de Flask), Gunicorn es robusto, eficiente y está diseñado para despliegues en entornos reales.

---

## ¿Qué es WSGI?

**WSGI** (Web Server Gateway Interface) es un estándar de Python (PEP 333) que define cómo los servidores web se comunican con las aplicaciones web Python. Gunicorn actúa como un servidor WSGI: recibe peticiones HTTP de clientes (a través de un proxy inverso como Nginx) y las pasa a tu aplicación Python.

```
Cliente → Nginx (proxy inverso) → Gunicorn → Tu Aplicación WSGI (ej: Flask/Django)
```

---

## ¿Por qué usar Gunicorn?

| Característica | Beneficio |
|-------|--------|
| **Listo para producción** | Maneja múltiples peticiones concurrentes de manera eficiente |
| **Modelos de worker** | Soporta workers síncronos, asíncronos, con hilos y gevent |
| **Modelo pre-fork** | Genera procesos worker para manejar peticiones en paralelo |
| **Recarga sin tiempo de inactividad** | Reinicios elegantes con `SIGHUP` |
| **Integración** | Funciona perfectamente con Nginx, systemd, Docker |

> **Nota**: Gunicorn **no** sirve archivos estáticos de manera eficiente — usa Nginx o una CDN para eso.

---

## Instalación

```bash
pip install gunicorn
```

Para soporte asíncrono:
```bash
pip install gunicorn[gevent]    # o [eventlet], [tornado]
```

---

## Uso Básico

### Línea de Comandos

```bash
gunicorn [OPCIONES] NOMBRE_MODULO:NOMBRE_VARIABLE
```

Ejemplo con Flask:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → archivo `run.py`, `app` es la instancia de Flask/FastAPI
- `--workers 3` → 3 procesos worker
- `--bind 0.0.0.0:8000` → escuchar en todas las interfaces, puerto 8000

---

## Tipos de Worker

Gunicorn soporta diferentes clases de worker dependiendo de las necesidades de tu aplicación:

| Tipo de Worker | Comando | Caso de Uso |
|-----------|--------|---------|
| **sync** (por defecto) | `gunicorn -k sync` | Apps que consumen mucha CPU o apps simples |
| **gevent** | `gunicorn -k gevent` | Alta concurrencia, uso intensivo de E/S (ej: APIs, websockets) |
| **eventlet** | `gunicorn -k eventlet` | Similar a gevent, bueno para async |
| **tornado** | `gunicorn -k tornado` | Apps en tiempo real |
| **threads** | `gunicorn -k sync --threads 4` | E/S + CPU mixto, pero cuidado con el GIL |

> **Recomendación**: Usa `gevent` o `eventlet` para la mayoría de las APIs web.

---

## Opciones de Configuración Clave

| Opción | Descripción | Ejemplo |
|------|-------------|--------|
| `--bind` | Host y puerto | `--bind 0.0.0.0:8000` |
| `--workers` | Número de procesos worker | `--workers 4` |
| `--worker-class` | Tipo de worker | `-k gevent` |
| `--threads` | Hilos por worker síncrono | `--threads 2` |
| `--timeout` | Tiempo de espera del worker (segundos) | `--timeout 30` |
| `--keep-alive` | Tiempo de espera keep-alive | `--keep-alive 2` |
| `--max-requests` | Reiniciar worker después de N peticiones | `--max-requests 1000` |
| `--max-requests-jitter` | Aleatorizar reinicio | `--max-requests-jitter 100` |
| `--preload` | Cargar la aplicación antes de hacer fork | `--preload` (inicio más rápido, memoria compartida) |
| `--log-level` | Nivel de log | `--log-level debug` |

---

## ¿Cuántos Workers?

Regla general:

```text
workers = (2 × núcleos de CPU) + 1
```

Para gevent/eventlet (async):
```text
workers = número de núcleos de CPU
threads = 100–1000 (dependiendo de la concurrencia)
```

Ejemplo:
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> Usa `nproc` o `htop` para verificar los núcleos de CPU.

---

## Archivo de Configuración (`gunicorn-cfg.py`)

En lugar de argumentos largos en la CLI, usa un archivo de configuración (como en tu Dockerfile):

```python
# gunicorn-cfg.py
bind = "0.0.0.0:8000"
workers = 3
worker_class = "gevent"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
loglevel = "info"
accesslog = "-"
errorlog = "-"
preload_app = False
```

Luego ejecuta:
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> Tu Dockerfile usa este patrón exacto — **una práctica excelente**.

---

## Logging

Gunicorn registra accesos y errores:

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

O registrar a stdout (apto para Docker):
```python
accesslog = "-"
errorlog = "-"
```

Formato de log:
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## Recarga Elegante y Sin Tiempo de Inactividad

1. **Recargar workers** (código nuevo):
   ```bash
   kill -HUP <gunicorn_pid>
   ```

2. **Reiniciar elegantemente**:
   ```bash
   kill -TERM <gunicorn_pid>
   ```

3. **Con systemd**:
   ```ini
   [Service]
   ExecReload=/bin/kill -HUP $MAINPID
   ```

---

## Ejecución Detrás de Nginx (Recomendado)

### Fragmento de Configuración de Nginx

```nginx
upstream app_server {
    server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://app_server;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/static/;
    }
}
```

---

## Mejores Prácticas con Docker (¡Tu Dockerfile es Genial!)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**Por qué esto es bueno**:
- `PYTHONUNBUFFERED=1` → logs en tiempo real
- `PYTHONDONTWRITEBYTECODE=1` → sin archivos `.pyc`
- `--no-cache-dir` → imagen más pequeña
- Archivo de configuración → CMD limpio

**Mejoras opcionales**:
```dockerfile
# Usar usuario no root
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## Ejemplo de Servicio Systemd

```ini
# /etc/systemd/system/gunicorn.service
[Unit]
Description=Instancia de Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/project
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn \
          --config gunicorn-cfg.py \
          run:app
ExecReload=/bin/kill -HUP $MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
```

Habilitar:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## Problemas Comunes y Depuración

| Problema | Solución |
|------|----------|
| **Tiempo de espera del worker** | Aumentar `--timeout` u optimizar el código |
| **Demasiados archivos abiertos** | Aumentar `ulimit -n` o usar workers asíncronos |
| **Fugas de memoria** | Usar `--max-requests` para reiniciar workers |
| **502 Bad Gateway** | Verificar que Gunicorn esté ejecutándose, enlace de puerto |
| **Inicio lento** | Usar `--preload` si la memoria lo permite |

---

## Monitoreo

- **Logs**: Seguir logs de acceso/error
- **Métricas**: Usar `prometheus-client` + exportador de Gunicorn
- **Endpoint de salud**:
  ```python
  @app.route("/health")
  def health():
      return "OK", 200
  ```

---

## Avanzado: Vistas Asíncronas (Ejemplo con FastAPI)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

Ejecutar con:
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

Instalar:
```bash
pip install "uvicorn[standard]"
```

---

## Lista de Verificación Resumen

| Tarea | ¿Hecho? |
|------|-------|
| Usar archivo de configuración (`gunicorn-cfg.py`) | Sí |
| Establecer `workers` basado en CPU | Sí |
| Usar workers asíncronos para E/S | Sí |
| Ejecutar detrás de Nginx | Sí |
| Log a stdout en Docker | Sí |
| Establecer timeouts & max-requests | Sí |
| Recarga elegante con `HUP` | Sí |

---

## Referencias

- [Documentación Oficial de Gunicorn](https://docs.gunicorn.org/)
- [Referencia de Configuración de Gunicorn](https://docs.gunicorn.org/en/stable/settings.html)
- [Tutorial de Gunicorn en DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [Uvicorn + Gunicorn para FastAPI](https://fastapi.tiangolo.com/deployment/server-workers/)