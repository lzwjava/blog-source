---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: गुनिकॉर्न प्रोडक्शन डिप्लॉयमेंट गाइड
translated: true
type: note
---

Gunicorn (Green Unicorn) पायथन वेब एप्लिकेशन के लिए एक लोकप्रिय WSGI HTTP सर्वर है। यह उत्पादन (production) में Flask, Django, FastAPI, या किसी भी WSGI-संगत ऐप से बने एप्लिकेशन को सर्व करने के लिए व्यापक रूप से उपयोग किया जाता है। डेवलपमेंट सर्वरों (जैसे Flask का बिल्ट-इन सर्वर) के विपरीत, Gunicorn मजबूत, कुशल और वास्तविक दुनिया में तैनाती के लिए डिज़ाइन किया गया है।

---

## WSGI क्या है?

**WSGI** (Web Server Gateway Interface) एक पायथन मानक (PEP 333) है जो परिभाषित करता है कि वेब सर्वर पायथन वेब एप्लिकेशन के साथ कैसे संचार करते हैं। Gunicorn एक WSGI सर्वर के रूप में कार्य करता है—यह क्लाइंट्स से HTTP अनुरोध (Nginx जैसे रिवर्स प्रॉक्सी के माध्यम से) प्राप्त करता है और उन्हें आपके पायथन ऐप को पास कर देता है।

```
क्लाइंट → Nginx (रिवर्स प्रॉक्सी) → Gunicorn → आपका WSGI ऐप (जैसे, Flask/Django)
```

---

## Gunicorn का उपयोग क्यों करें?

| सुविधा | लाभ |
|-------|--------|
| **प्रोडक्शन-तैयार** | एक साथ कई अनुरोधों को कुशलतापूर्वक संभालता है |
| **वर्कर मॉडल** | सिंक, एसिंक, थ्रेडिंग, और gevent वर्कर का समर्थन करता है |
| **प्री-फोर्क मॉडल** | अनुरोधों को समानांतर में संभालने के लिए वर्कर प्रक्रियाएं शुरू करता है |
| **जीरो-डाउनटाइम रीलोड** | `SIGHUP` के साथ सहज रीस्टार्ट |
| **एकीकरण** | Nginx, systemd, Docker के साथ निर्बाध रूप से काम करता है |

> **नोट**: Gunicorn स्टैटिक फाइलों को कुशलतापूर्वक **नहीं** परोसता है—उसके लिए Nginx या CDN का उपयोग करें।

---

## इंस्टालेशन

```bash
pip install gunicorn
```

एसिंक सपोर्ट के लिए:
```bash
pip install gunicorn[gevent]    # or [eventlet], [tornado]
```

---

## बेसिक उपयोग

### कमांड लाइन

```bash
gunicorn [OPTIONS] MODULE_NAME:VARIABLE_NAME
```

Flask के साथ उदाहरण:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → `run.py` फाइल, `app` Flask/FastAPI इंस्टेंस है
- `--workers 3` → 3 वर्कर प्रक्रियाएं
- `--bind 0.0.0.0:8000` → सभी इंटरफेस, पोर्ट 8000 पर सुनें

---

## वर्कर प्रकार

Gunicorn आपके ऐप की जरूरतों के आधार पर विभिन्न वर्कर क्लासेस का समर्थन करता है:

| वर्कर प्रकार | कमांड | उपयोग केस |
|-----------|--------|---------|
| **sync** (डिफॉल्ट) | `gunicorn -k sync` | CPU-बाउंड या सरल ऐप्स |
| **gevent** | `gunicorn -k gevent` | उच्च समवर्तिता (concurrency), I/O-हेवी (जैसे, APIs, websockets) |
| **eventlet** | `gunicorn -k eventlet` | gevent के समान, async के लिए अच्छा |
| **tornado** | `gunicorn -k tornado` | रियल-टाइम ऐप्स |
| **threads** | `gunicorn -k sync --threads 4` | मिश्रित I/O + CPU, लेकिन GIL से सावधान |

> **सिफारिश**: अधिकांश वेब APIs के लिए `gevent` या `eventlet` का उपयोग करें।

---

## मुख्य कॉन्फ़िगरेशन विकल्प

| विकल्प | विवरण | उदाहरण |
|------|-------------|--------|
| `--bind` | होस्ट और पोर्ट | `--bind 0.0.0.0:8000` |
| `--workers` | वर्कर प्रक्रियाओं की संख्या | `--workers 4` |
| `--worker-class` | वर्कर प्रकार | `-k gevent` |
| `--threads` | प्रति सिंक वर्कर थ्रेड्स | `--threads 2` |
| `--timeout` | वर्कर टाइमआउट (सेकंड) | `--timeout 30` |
| `--keep-alive` | कीप-अलाइव टाइमआउट | `--keep-alive 2` |
| `--max-requests` | N अनुरोधों के बाद वर्कर रीस्टार्ट करें | `--max-requests 1000` |
| `--max-requests-jitter` | रीस्टार्ट को यादृच्छिक बनाएं | `--max-requests-jitter 100` |
| `--preload` | फोर्किंग से पहले ऐप लोड करें | `--preload` (तेज़ स्टार्टअप, शेयर्ड मेमोरी) |
| `--log-level` | लॉग स्तर | `--log-level debug` |

---

## कितने वर्कर?

सामान्य नियम:

```text
workers = (2 × CPU cores) + 1
```

gevent/eventlet (async) के लिए:
```text
workers = CPU cores की संख्या
threads = 100–1000 (concurrency पर निर्भर करता है)
```

उदाहरण:
```bash
gunicorn -k gevent --workers 2 --threads 200 run:app
```

> CPU cores जांचने के लिए `nproc` या `htop` का उपयोग करें।

---

## कॉन्फ़िगरेशन फ़ाइल (`gunicorn-cfg.py`)

लंबे CLI आर्ग्युमेंट्स के बजाय, एक कॉन्फ़िग फ़ाइल का उपयोग करें (जैसा कि आपके Dockerfile में है):

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

फिर चलाएं:
```bash
gunicorn --config gunicorn-cfg.py run:app
```

> आपके Dockerfile में यही पैटर्न उपयोग किया गया है—**उत्कृष्ट अभ्यास**।

---

## लॉगिंग

Gunicorn एक्सेस और एरर लॉग करता है:

```python
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "warning"
```

या stdout पर लॉग करें (Docker-अनुकूल):
```python
accesslog = "-"
errorlog = "-"
```

लॉग फॉर्मेट:
```python
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
```

---

## सहज रीलोड और जीरो डाउनटाइम

1. **वर्कर रीलोड करें** (नया कोड):
   ```bash
   kill -HUP <gunicorn_pid>
   ```

2. **सहज रूप से रीस्टार्ट करें**:
   ```bash
   kill -TERM <gunicorn_pid>
   ```

3. **systemd के साथ**:
   ```ini
   [Service]
   ExecReload=/bin/kill -HUP $MAINPID
   ```

---

## Nginx के पीछे चलाना (सिफारिश किया गया)

### Nginx कॉन्फ़िग स्निपेट

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

## Docker बेस्ट प्रैक्टिसेज (आपका Dockerfile बढ़िया है!)

```dockerfile
FROM python:3.9
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
```

**यह अच्छा क्यों है**:
- `PYTHONUNBUFFERED=1` → रियल-टाइम लॉग
- `PYTHONDONTWRITEBYTECODE=1` → कोई `.pyc` फाइलें नहीं
- `--no-cache-dir` → छोटी इमेज
- कॉन्फ़िग फ़ाइल → साफ़ CMD

**वैकल्पिक सुधार**:
```dockerfile
# नॉन-रूट यूजर का उपयोग करें
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# हेल्थचेक
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
```

---

## Systemd सर्विस उदाहरण

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

एनेबल करें:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
```

---

## सामान्य समस्याएं और डीबगिंग

| समस्या | समाधान |
|------|----------|
| **वर्कर टाइमआउट** | `--timeout` बढ़ाएं या कोड ऑप्टिमाइज़ करें |
| **बहुत सारी ओपन फाइलें** | `ulimit -n` बढ़ाएं या async वर्कर का उपयोग करें |
| **मेमोरी लीक** | वर्कर को रीस्टार्ट करने के लिए `--max-requests` का उपयोग करें |
| **502 बैड गेटवे** | जांचें कि Gunicorn चल रहा है, पोर्ट बाइंडिंग |
| **धीमा स्टार्टअप** | यदि मेमोरी अनुमति दे तो `--preload` का उपयोग करें |

---

## मॉनिटरिंग

- **लॉग्स**: एक्सेस/एरर लॉग्स टेल करें
- **मेट्रिक्स**: `prometheus-client` + Gunicorn एक्सपोर्टर का उपयोग करें
- **हेल्थ एंडपॉइंट**:
  ```python
  @app.route("/health")
  def health():
      return "OK", 200
  ```

---

## एडवांस्ड: एसिंक व्यूज़ (FastAPI उदाहरण)

```python
# run.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

इसके साथ चलाएं:
```bash
gunicorn -k uvicorn.workers.UvicornWorker run:app
```

इंस्टॉल करें:
```bash
pip install "uvicorn[standard]"
```

---

## सारांश चेकलिस्ट

| कार्य | हो गया? |
|------|-------|
| कॉन्फ़िग फ़ाइल (`gunicorn-cfg.py`) का उपयोग करें | Yes |
| CPU के आधार पर `workers` सेट करें | Yes |
| I/O के लिए async वर्कर का उपयोग करें | Yes |
| Nginx के पीछे चलाएं | Yes |
| Docker में stdout पर लॉग करें | Yes |
| टाइमआउट और max-requests सेट करें | Yes |
| `HUP` के साथ सहज रीलोड | Yes |

---

## संदर्भ

- [Gunicorn ऑफिशियल डॉक्स](https://docs.gunicorn.org/)
- [Gunicorn सेटिंग्स रेफरेंस](https://docs.gunicorn.org/en/stable/settings.html)
- [DigitalOcean Gunicorn ट्यूटोरियल](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [FastAPI के लिए Uvicorn + Gunicorn](https://fastapi.tiangolo.com/deployment/server-workers/)