---
audio: false
generated: true
image: false
lang: de
layout: post
title: Python Certifi SSL-Zertifikat Leitfaden
translated: true
type: note
---

Das **`certifi`**-Paket auf PyPI ist eine kleine Bibliothek, die **Mozillas vertrauenswürdige Stammzertifikate** in einem Bundle bereitstellt. Es wird häufig von Python-Bibliotheken wie `requests`, `urllib3` oder jedem HTTPS-Client verwendet, der SSL/TLS-Zertifikate validieren muss.

So verwenden Sie es:

---

### 1. `certifi` installieren

```bash
pip install certifi
```

---

### 2. Den Pfad zum CA-Bundle abrufen

In Python:

```python
import certifi

print(certifi.where())
```

Dies gibt den vollständigen Pfad zum CA-Zertifikatsbundle (eine `.pem`-Datei) aus. Zum Beispiel:

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. Verwendung mit `requests` oder `urllib3`

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

Standardmäßig verwendet `requests` bereits intern `certifi`, aber das explizite Übergeben von `verify=certifi.where()` stellt sicher, dass das aktualisierte Bundle verwendet wird.

---

### 4. Verwendung in anderen HTTPS-Bibliotheken

Wenn Sie direkt mit `urllib3` arbeiten:

```python
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

response = http.request("GET", "https://example.com")
print(response.status)
```

---

### 5. Systemweite Verwendung (optional)

Manchmal möchten Sie möglicherweise eine Anwendung so konfigurieren, dass sie das CA-Bundle von certifi verwendet:

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 Kurz gesagt:

* Installieren mit `pip install certifi`
* Verwenden Sie `certifi.where()`, um den Pfad zum Zertifikatsbundle zu erhalten
* Übergeben Sie es an Bibliotheken, die eine Zertifikatsvalidierung benötigen

---

Möchten Sie, dass ich Ihnen auch zeige, **wie Sie Ihre gesamte Python-Umgebung standardmäßig die Zertifikate von certifi verwenden lassen**, damit Sie nicht jede Bibliothek einzeln konfigurieren müssen?