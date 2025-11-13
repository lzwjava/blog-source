---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل نشر Gunicورن للإنتاج
translated: true
type: note
---

Gunicorn (Green Unicorn) هو خادم HTTP شائع لتطبيقات Python يستخدم مواصفات WSGI. يُستخدم على نطاق واسع في بيئات الإنتاج لخدمة التطبيقات المبنية بإطار عمل مثل Flask أو Django أو FastAPI أو أي تطبيق متوافق مع WSGI. على عكس خوادم التطوير (مثل الخادم المدمج في Flask)، فإن Gunicorn قوي وفعال ومصمم للنشر في بيئات الإنتاج الحقيقية.

---

## ما هو WSGI؟

**WSGI** (واجهة بوابة خادم الويب) هو معيار في Python (PEP 333) يحدد كيفية تواصل خوادم الويب مع تطبيقات Python على الويب. يعمل Gunicorn كخادم WSGI - حيث يستقبل طلبات HTTP من العملاء (عبر وكيل عكسي مثل Nginx) ويمررها إلى تطبيق Python الخاص بك.

```
العميل → Nginx (الوكيل العكسي) → Gunicorn → تطبيق WSGI الخاص بك (مثل Flask/Django)
```

---

## لماذا نستخدم Gunicorn؟

| الميزة | الفائدة |
|-------|--------|
| **جاهز للإنتاج** | يتعامل مع طلبات متعددة متزامنة بكفاءة |
| **نماذج العمال (Workers)** | يدعم عمال المزامنة (sync)، والغير متزامنة (async)، والخيوط (threading)، و gevent |
| **نموذج Pre-fork** | ينشئ عمليات عاملة (worker processes) للتعامل مع الطلبات بالتوازي |
| **إعادة تحميل بدون توقف (Zero-downtime)** | إعادة تشغيل سلسة باستخدام `SIGHUP` |
| **التكامل** | يعمل بسلاسة مع Nginx و systemd و Docker |

> **ملاحظة**: Gunicorn **لا** يخدم الملفات الثابتة (static files) بكفاءة - استخدم Nginx أو CDN لهذا الغرض.

---

## التثبيت

```bash
pip install gunicorn
```

لدعم الـ async:
```bash
pip install gunicorn[gevent]    # أو [eventlet]، [tornado]
```

---

## الاستخدام الأساسي

### سطر الأوامر

```bash
gunicorn [OPTIONS] MODULE_NAME:VARIABLE_NAME
```

مثال مع Flask:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → ملف `run.py`، `app` هو كائن Flask/FastAPI
- `--workers 3` → 3 عمليات عاملة (worker processes)
- `--bind 0.0.0.0:8000` → الاستماع على جميع الواجهات، المنفذ 8000

---

## أنواع العمال (Workers)

يدعم Gunicorn فئات مختلفة من العمال (workers) اعتمادًا على احتياجات تطبيقك:

| نوع العامل | الأمر | حالة الاستخدام |
|-----------|--------|---------|
| **sync** (الافتراضي) | `gunicorn -k sync` | التطبيقات التي تعتمد على وحدة المعالجة المركزية (CPU-bound) أو التطبيقات البسيطة |
| **gevent** | `gunicorn -k gevent` | التزامن العالي، التطبيقات التي تعتمد على الإدخال/الإخراج (I/O-heavy) (مثل واجهات برمجة التطبيقات APIs، websockets) |
| **eventlet** | `gunicorn -k eventlet` | مشابه لـ gevent، جيد للـ async |
| **tornado** | `gunicorn -k tornado` | التطبيقات في الوقت الفعلي (Real-time) |
| **threads** | `gunicorn -k sync --threads 4` | مزيج من الإدخال/الإخراج ووحدة المعالجة المركزية، لكن احذر من GIL |

> **التوصية**: استخدم `gevent` أو `eventlet` لمعظم واجهات برمجة تطبيقات الويب (web APIs).

---

## خيارات التهيئة الرئيسية

| الخيار | الوصف | مثال |
|------|-------------|--------|
| `--bind` | المضيف والمنفذ | `--bind 0.0.0.0:8000` |
| `--workers` | عدد عمليات العمال (worker processes) | `--workers 4` |
| `--worker-class` | نوع العامل | `-k gevent` |
| `--threads` | عدد الخيوط (threads) لكل عامل مزامنة (sync worker) | `--threads 2` |
| `--timeout` | وقت انتهاء المهلة للعامل (بالثواني) | `--timeout 30` |
| `--keep-alive` | وقت انتهاء مهلة keep-alive | `--keep-alive 2` |
| `--max-requests` | إعادة تشغيل العامل بعد عدد N من الطلبات | `--max-requests 1000` |
| `--max-requests-jitter` | إضافة عشوائية لإعادة التشغيل | `--max-requests-jitter 100` |
| `--preload` | تحميل التطبيق قبل عملية forking | `--preload` (بدء تشغيل أسرع، ذاكرة مشتركة) |
| `--log-level` | مستوى التسجيل (Log level) | `--log-level debug` |

---

## كم عدد العمال (Workers) المطلوب؟

القاعدة العامة:

```text
workers = (2 × عدد أنوية وحدة المعالجة المركزية) + 1
```

لـ gevent/eventlet (غير متزامن - async):
```text
workers = عدد أنوية وحدة المعالجة المركزية
threads = 100–1000 (اعتمادًا على درجة التزامن)
```

مثال:
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> استخدم `nproc` أو `htop` للتحقق من عدد أنوية وحدة المعالجة المركزية.

---

## ملف التهيئة (`gunicorn-cfg.py`)

بدلاً من استخدام وسائط طويلة في سطر الأوامر، استخدم ملف تهيئة (كما في Dockerfile الخاص بك):

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

ثم شغل:
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> يستخدم Dockerfile الخاص بك هذا النمط بالضبط - **ممارسة ممتازة**.

---

## التسجيل (Logging)

يسجل Gunicorn سجلات الوصول (access) والأخطاء (errors):

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

أو التسجيل إلى stdout (ملائم لـ Docker):
```python
accesslog = "-"
errorlog = "-"
```

تنسيق السجل:
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## إعادة التحميل السلسة (Graceful Reload) وبدون توقف (Zero Downtime)

1.  **إعادة تحميل العمال** (كود جديد):
    ```bash
    kill -HUP <gunicorn_pid>
    ```

2.  **إعادة التشغيل السلسة**:
    ```bash
    kill -TERM <gunicorn_pid>
    ```

3.  **مع systemd**:
    ```ini
    [Service]
    ExecReload=/bin/kill -HUP $MAINPID
    ```

---

## التشغيل خلف Nginx (مُوصى به)

### مقتطف تهيئة Nginx

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

## أفضل الممارسات مع Docker (Dockerfile الخاص بك رائع!)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**لماذا هذا جيد**:
- `PYTHONUNBUFFERED=1` → سجلات (logs) في الوقت الفعلي
- `PYTHONDONTWRITEBYTECODE=1` → لا يتم إنشاء ملفات `.pyc`
- `--no-cache-dir` → صورة أصغر حجمًا
- ملف التهيئة → أمر CMD نظيف

**تحسينات اختيارية**:
```dockerfile
# استخدام مستخدم غير root
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# فحص الصحة (Healthcheck)
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## مثال لخدمة Systemd

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

التفعيل:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## المشاكل الشائعة والتdebuggging

| المشكلة | الحل |
|------|----------|
| **انتهت مهلة العامل (Worker timeout)** | زيادة `--timeout` أو تحسين الكود |
| **عدد كبير جدًا من الملفات المفتوحة** | زيادة `ulimit -n` أو استخدام عمال async |
| **تسرب الذاكرة (Memory leaks)** | استخدام `--max-requests` لإعادة تشغيل العمال |
| **502 Bad Gateway** | التحقق من أن Gunicorn يعمل، وربط المنفذ (port binding) |
| **بدء تشغيل بطيء** | استخدام `--preload` إذا كانت الذاكرة تسمح |

---

## المراقبة (Monitoring)

-   **السجلات (Logs)**: تتبع سجلات الوصول والأخطاء
-   **المقاييس (Metrics)**: استخدام `prometheus-client` + أداة تصدير Gunicorn (Gunicorn exporter)
-   **نقطة نهاية الصحة (Health endpoint)**:
    ```python
    @app.route("/health")
    def health():
        return "OK", 200
    ```

---

## متقدم: نماذج غير متزامنة (Async Views) (مثال FastAPI)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

شغل باستخدام:
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

ثبّت:
```bash
pip install "uvicorn[standard]"
```

---

## قائمة مراجعة ملخصة

| المهمة | تم؟ |
|------|-------|
| استخدام ملف تهيئة (`gunicorn-cfg.py`) | Yes |
| ضبط `workers` بناءً على وحدة المعالجة المركزية | Yes |
| استخدام عمال async للتطبيقات التي تعتمد على الإدخال/الإخراج | Yes |
| التشغيل خلف Nginx | Yes |
| التسجيل إلى stdout في Docker | Yes |
| ضبط مهلات الوقت (timeouts) و max-requests | Yes |
| إعادة تحميل سلسة باستخدام `HUP` | Yes |

---

## المراجع

-   [Gunicorn Official Docs](https://docs.gunicorn.org/)
-   [Gunicorn Settings Reference](https://docs.gunicorn.org/en/stable/settings.html)
-   [DigitalOcean Gunicorn Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
-   [Uvicorn + Gunicorn for FastAPI](https://fastapi.tiangolo.com/deployment/server-workers/)