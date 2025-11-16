---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Behebung langsamer Hugging Face Downloads
translated: true
type: note
---

Dies ist ein häufiges Problem beim Herunterladen großer HF-Datasets über einen Proxy. Die Kombination aus:

* Vielen Dateien mit mehreren hundert MB
* Python `requests` / `huggingface_hub`
* Einem lokalen HTTP-Proxy (insbesondere Clash, V2Ray oder tun2socks)

führt oft zu extrem langsamen Durchsatzraten oder Verbindungsabbrüchen.

Nachfolgend sind die nützlichsten Lösungen aufgeführt.

---

## 1. **Beste Lösung: `hf_transfer` verwenden**

Hugging Face hat einen beschleunigten Downloader, der **10–50 mal schneller** ist und stabiler läuft.

Installation:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Führen Sie Ihren Befehl erneut aus.

Dies allein behebt normalerweise langsame Downloads über Proxies.

---

## 2. `aria2c` mit Hugging Face CLI verwenden (am schnellsten für sehr große Dateien)

Falls Sie manuell herunterladen:

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

Dann herunterladen:

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

Die HF CLI verwendet automatisch aria2, das folgendes besser handhabt als `requests`:

* Parallele Verbindungen
* Fortsetzen von Downloads
* Instabile Proxies

---

## 3. Lösung für langsame lokale Proxies: Systemweiten SOCKS anstelle von HTTP verwenden

Wenn Sie so etwas verwenden wie:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

Wechseln Sie zu SOCKS5, falls Ihr Proxy dies unterstützt:

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

SOCKS ist für das Streamen großer Dateien **viel stabiler**.

---

## 4. Proxy für große Dateien deaktivieren

Falls Ihr Rohtnetzwerk in Ordnung ist, aber der Proxy verlangsamt:

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

Dann versuchen Sie es erneut. Einige HF-Server sind je nach Region auch ohne Proxy schnell.

---

## 5. HF-Spiegelserver verwenden (chinesisches Festland / TW manchmal langsam)

Sie können den CDN erzwingen:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

Führen Sie den Befehl dann erneut aus.
Dies verbessert die Geschwindigkeit in einigen Regionen erheblich.

---

## 6. Unterbrochene Downloads fortsetzen

HF-Datasets werden hier zwischengespeichert:

```
~/.cache/huggingface/datasets/
```

Falls eine Datei teilweise heruntergeladen wurde, setzt HF den Download automatisch fort — kein Neustart bei Null erforderlich.

---

## 7. Falls es immer noch langsam ist: Vermeiden Sie das vollständige Dataset, verwenden Sie einen kleinen Ausschnitt

OpenWebText ist >40 GB.
Sie können nur einen kleinen Teil laden:

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## Schnelle Empfehlung

Am schnellsten + einfachsten:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

Sie sollten sofort einen Sprung bei den Download-Geschwindigkeiten bemerken.

---

Falls Sie möchten, kann ich Ihnen zeigen, wie Sie Ihr `prepare.py` so ändern können, dass es einen komplett benutzerdefinierten Downloader mit Wiederholungsversuchen/Backoff und parallelem Abruf verwendet, sodass Ihre Pipeline immer schnell herunterlädt und nie hängen bleibt.