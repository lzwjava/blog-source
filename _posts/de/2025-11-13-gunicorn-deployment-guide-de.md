---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Gunicorn Produktionsleitfaden
translated: true
type: note
---

Gunicorn (Green Unicorn) ist ein beliebter WSGI-HTTP-Server für Python-Webanwendungen. Er wird häufig im Produktivbetrieb eingesetzt, um Anwendungen zu bedienen, die mit Frameworks wie Flask, Django, FastAPI oder jeder WSGI-konformen App erstellt wurden. Im Gegensatz zu Entwicklungsservern (z. B. dem eingebauten Server von Flask) ist Gunicorn robust, effizient und für den realen Einsatz konzipiert.

---

## Was ist WSGI?

**WSGI** (Web Server Gateway Interface) ist ein Python-Standard (PEP 333), der definiert, wie Webserver mit Python-Webanwendungen kommunizieren. Gunicorn fungiert als ein WSGI-Server – er empfängt HTTP-Anfragen von Clients (über einen Reverse-Proxy wie Nginx) und leitet sie an Ihre Python-App weiter.

```
Client → Nginx (Reverse-Proxy) → Gunicorn → Ihre WSGI-App (z.B. Flask/Django)
```

---

## Warum Gunicorn verwenden?

| Funktion | Vorteil |
|-------|--------|
| **Produktionsreif** | Verarbeitet mehrere gleichzeitige Anfragen effizient |
| **Worker-Modelle** | Unterstützt synchrone, asynchrone, Thread- und Gevent-Worker |
| **Pre-Fork-Modell** | Erzeugt Worker-Prozesse, um Anfragen parallel zu bearbeiten |
| **Zero-Downtime-Reload** | Elegante Neustarts mit `SIGHUP` |
| **Integration** | Funktioniert nahtlos mit Nginx, systemd, Docker |

> **Hinweis**: Gunicorn bedient **keine** statischen Dateien effizient – verwenden Sie dafür Nginx oder ein CDN.

---

## Installation

```bash
pip install gunicorn
```

Für Async-Unterstützung:
```bash
pip install gunicorn[gevent]    # oder [eventlet], [tornado]
```

---

## Grundlegende Verwendung

### Kommandozeile

```bash
gunicorn [OPTIONEN] MODULNAME:VARIABLENNAME
```

Beispiel mit Flask:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → `run.py` Datei, `app` ist die Flask/FastAPI-Instanz
- `--workers 3` → 3 Worker-Prozesse
- `--bind 0.0.0.0:8000` → Lausche auf allen Netzwerkschnittstellen, Port 8000

---

## Worker-Typen

Gunicorn unterstützt verschiedene Worker-Klassen, je nach den Anforderungen Ihrer App:

| Worker-Typ | Befehl | Anwendungsfall |
|-----------|--------|---------|
| **sync** (Standard) | `gunicorn -k sync` | CPU-intensive oder einfache Apps |
| **gevent** | `gunicorn -k gevent` | Hohe Nebenläufigkeit, I/O-lastig (z.B. APIs, Websockets) |
| **eventlet** | `gunicorn -k eventlet` | Ähnlich wie gevent, gut für Async |
| **tornado** | `gunicorn -k tornado` | Echtzeit-Apps |
| **threads** | `gunicorn -k sync --threads 4` | Gemischte I/O + CPU, aber Vorsicht vor dem GIL |

> **Empfehlung**: Verwenden Sie `gevent` oder `eventlet` für die meisten Web-APIs.

---

## Wichtige Konfigurationsoptionen

| Option | Beschreibung | Beispiel |
|------|-------------|--------|
| `--bind` | Host und Port | `--bind 0.0.0.0:8000` |
| `--workers` | Anzahl der Worker-Prozesse | `--workers 4` |
| `--worker-class` | Worker-Typ | `-k gevent` |
| `--threads` | Threads pro Sync-Worker | `--threads 2` |
| `--timeout` | Worker-Timeout (Sekunden) | `--timeout 30` |
| `--keep-alive` | Keep-Alive-Timeout | `--keep-alive 2` |
| `--max-requests` | Worker nach N Anfragen neu starten | `--max-requests 1000` |
| `--max-requests-jitter` | Neustart-Zeitpunkt randomisieren | `--max-requests-jitter 100` |
| `--preload` | App vor dem Forking laden | `--preload` (schnellerer Start, gemeinsamer Speicher) |
| `--log-level` | Log-Level | `--log-level debug` |

---

## Wie viele Worker?

Allgemeine Faustregel:

```text
workers = (2 × CPU-Kerne) + 1
```

Für gevent/eventlet (async):
```text
workers = Anzahl der CPU-Kerne
threads = 100–1000 (abhängig von der Nebenläufigkeit)
```

Beispiel:
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> Verwenden Sie `nproc` oder `htop`, um die CPU-Kerne zu überprüfen.

---

## Konfigurationsdatei (`gunicorn-cfg.py`)

Anstatt langer CLI-Argumente können Sie eine Konfigurationsdatei verwenden (wie in Ihrem Dockerfile):

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

Dann ausführen mit:
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> Ihr Dockerfile verwendet genau dieses Muster – **ausgezeichnete Praxis**.

---

## Logging

Gunicorn protokolliert Zugriffe und Fehler:

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

Oder Logging nach stdout (Docker-freundlich):
```python
accesslog = "-"
errorlog = "-"
```

Log-Format:
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## Elegantes Neuladen & Zero Downtime

1. **Worker neu laden** (neuer Code):
   ```bash
   kill -HUP <gunicorn_pid>
   ```

2. **Elegant neu starten**:
   ```bash
   kill -TERM <gunicorn_pid>
   ```

3. **Mit systemd**:
   ```ini
   [Service]
   ExecReload=/bin/kill -HUP $MAINPID
   ```

---

## Betrieb hinter Nginx (Empfohlen)

### Nginx-Konfigurationsausschnitt

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

## Docker Best Practices (Ihr Dockerfile ist großartig!)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**Warum das gut ist**:
- `PYTHONUNBUFFERED=1` → Echtzeit-Logs
- `PYTHONDONTWRITEBYTECODE=1` → Keine `.pyc`-Dateien
- `--no-cache-dir` → Kleineres Image
- Konfigurationsdatei → Sauberer CMD

**Optionale Verbesserungen**:
```dockerfile
# Nicht-Root-Benutzer verwenden
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## Systemd Service Beispiel

```ini
# /etc/systemd/system/gunicorn.service
[Unit]
Description=Gunicorn instance
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

Aktivieren:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## Häufige Probleme & Debugging

| Problem | Lösung |
|------|----------|
| **Worker-Timeout** | `--timeout` erhöhen oder Code optimieren |
| **Zu viele geöffnete Dateien** | `ulimit -n` erhöhen oder Async-Worker verwenden |
| **Speicherlecks** | `--max-requests` verwenden, um Worker neu zu starten |
| **502 Bad Gateway** | Prüfen, ob Gunicorn läuft, Port-Binding prüfen |
| **Langsamer Start** | `--preload` verwenden, falls Speicher es erlaubt |

---

## Monitoring

- **Logs**: Access-/Error-Logs mit `tail` verfolgen
- **Metriken**: `prometheus-client` + Gunicorn Exporter verwenden
- **Health-Endpoint**:
  ```python
  @app.route("/health")
  def health():
      return "OK", 200
  ```

---

## Fortgeschritten: Async Views (FastAPI Beispiel)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

Ausführen mit:
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

Installation:
```bash
pip install "uvicorn[standard]"
```

---

## Zusammenfassende Checkliste

| Aufgabe | Erledigt? |
|------|-------|
| Konfigurationsdatei verwenden (`gunicorn-cfg.py`) | Ja |
| `workers` basierend auf CPU festlegen | Ja |
| Async-Worker für I/O verwenden | Ja |
| Hinter Nginx betreiben | Ja |
| In Docker nach stdout loggen | Ja |
| Timeouts & max-requests setzen | Ja |
| Elegantes Neuladen mit `HUP` | Ja |

---

## Referenzen

- [Gunicorn Offizielle Dokumentation](https://docs.gunicorn.org/)
- [Gunicorn Einstellungsreferenz](https://docs.gunicorn.org/en/stable/settings.html)
- [DigitalOcean Gunicorn Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [Uvicorn + Gunicorn für FastAPI](https://fastapi.tiangolo.com/deployment/server-workers/)