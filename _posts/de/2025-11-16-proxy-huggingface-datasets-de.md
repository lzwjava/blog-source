---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verwendung eines Proxys mit Hugging Face Datasets
translated: true
type: note
---

Ja — `datasets` befolgt deine **System-/Umgebungs-Proxy-Einstellungen**, hat jedoch **keine** eigene Proxy-Konfiguration.
Du kannst Hugging Face also absolut über einen Proxy Datensätze herunterladen lassen, wenn du in China bist.

So geht's.

---

# Wie man `load_dataset` dazu bringt, einen Proxy zu verwenden (China-freundlich)

## 1. Umgebungsvariablen für HTTP/HTTPS-Proxy setzen

`datasets` verwendet intern die `requests`-Bibliothek von Python.
`requests` verwendet automatisch die standardmäßigen Proxy-Umgebungsvariablen:

### Linux / macOS

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Wenn dein Proxy SOCKS5 verwendet:

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

### Windows (PowerShell)

```powershell
setx HTTP_PROXY "http://127.0.0.1:7890"
setx HTTPS_PROXY "http://127.0.0.1:7890"
```

Anschließend Terminal neu öffnen.

---

## 2. Wenn du Python innerhalb von Code ausführst (wie Jupyter), setze es innerhalb von Python

```python
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
```

Das funktioniert zuverlässig.

---

## 3. Bestätigen, dass der Proxy funktioniert

Du kannst es testen mit:

```python
import requests
print(requests.get("https://api.ipify.org?format=json").text)
```

Wenn die IP der Ausgangsknoten deines Proxys ist, dann werden auch die Hugging Face-Datensatz-Downloads über diesen Proxy laufen.

---

## 4. Hugging Faces `huggingface_hub` respektiert diese Variablen ebenfalls

`datasets` verwendet intern `huggingface_hub`, und dies befolgt **ebenfalls**:

* `HTTP_PROXY`
* `HTTPS_PROXY`
* `http_proxy`
* `https_proxy`

Sobald die Umgebungsvariablen gesetzt sind, werden sowohl Modell- als auch Datensatz-Downloads automatisch deinen Proxy verwenden.

---

# Hinweise zur Verwendung in China

* Hugging Face-Rohdownloads erfordern oft einen Proxy, da sie auf US-/Europa-Endpunkten gehostet werden.
* Wenn du Timeouts bei `.zst`-Datensatzdateien siehst, ist das normal ohne Proxy.
* Ein globaler Proxy (Clash, V2Ray, Qv2ray, etc.) macht alles reibungsloser.

---

# Wenn du möchtest, kann ich zeigen:

* Wie du sicherstellst, dass NanoGPT Datensätze über deinen Proxy herunterlädt
* Wie du den Datensatz lokal zwischenspeicherst, um zukünftige Downloads zu vermeiden
* Wie du Hugging Face-Datensätze lokal in China spiegelst (z.B. Tsinghua Mirror Workaround)

Sag mir einfach, was du brauchst.