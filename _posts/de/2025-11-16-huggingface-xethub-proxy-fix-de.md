---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Behebung des Hugging Face XetHub-Proxy-Problems
translated: true
type: note
---

Ihre Protokolle zeigen etwas sehr Wichtiges:

**Die fehlgeschlagene Verbindung geht *nicht* direkt zu HuggingFace.**
Sie geht zu **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** — dies ist Hugging Faces *XetHub*-Backend (Rust-Client `reqwest`), welches der von Ihnen eingerichtete Proxy **NICHT automatisch abfängt**.

Dies erklärt alles:

* Sie haben bereits `HTTP_PROXY` für Python gesetzt → funktioniert
* Aber XetHub verwendet **rust reqwest**, nicht Python requests
* Rust reqwest **ignoriert System-Proxy-Variablen, es sei denn, Sie setzen die Kleinbuchstaben-Variablen HTTPS_PROXY**, oder verwendet eine explizite Proxy-Konfiguration

Also: **Ihre Python-Umgebung verwendet den Proxy, aber XetHub (der neue HF-Speicheranbieter) tut dies NICHT**.

Deshalb sehen Sie:

```
ConnectError("Connection refused")
```

und Wiederholungsversuche.

---

# Warum das passiert (Kurzversion)

Hugging Face ist kürzlich zu **XetHub** als Speicheranbieter migriert, welcher einen Rust-Client verwendet.
Dieser Client beachtet:

* `https_proxy`
* `http_proxy`

aber **nicht immer** die Großbuchstaben-Versionen, abhängig vom Build.

Sie haben Großbuchstaben gesetzt? → Er könnte sie ignorieren.

---

# Lösung (funktiert zuverlässig in China)

## 1. Setzen Sie SOWOHL Klein- ALS AUCH Großbuchstaben-Proxy-Variablen

In Ihrer Shell **bevor Sie NanoGPT ausführen**:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Rust reqwest bevorzugt Kleinbuchstaben
Python requests bevorzugt Großbuchstaben
Beide zu setzen vermeidet Probleme.

Dann führen Sie aus:

```bash
python data/openwebtext_10k/prepare.py
```

Sie sollten sofort eine ordentliche Download-Geschwindigkeit sehen.

---

# 2. Wichtig, wenn Ihr Proxy SOCKS5 ist

Rust reqwest **unterstützt socks5 nicht**, es sei denn, es wurde mit optionalen Features kompiliert.
Wenn Ihr Proxy also socks5:// ist → wird es fehlschlagen.

Sie müssen zum HTTP-Proxy-Port Ihres Clients wechseln, normalerweise:

* Clash: 7890 (HTTP)
* V2RayN: 10809 (HTTP)

Verwenden Sie HTTP, nicht SOCKS.

---

# 3. So testen Sie, ob der Rust-Teil den Proxy verwendet

Testen Sie via `curl`, **nicht Python**, weil sich curl ähnlich wie Rust in Bezug auf Proxy-Regeln verhält:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Wenn dies funktioniert → werden Rust-Downloads auch funktionieren.

Wenn es fehlschlägt → kann Ihr Proxy die Domain `xethub.hf.co` nicht erreichen.

---

# 4. Wenn Sie Hugging Face zwingen wollen, XetHub zu umgehen

Sie können die Umgebungsvariable setzen:

```bash
export HF_HUB_DISABLE_XETHUB=1
```

Dies erzwingt das alte HuggingFace S3-Backend anstelle von XetHub, das proxy-freundlicher ist.

Dann:

```bash
python data/openwebtext_10k/prepare.py
```

Dies ist die stabilste Lösung.

---

# Empfohlene Lösung (China-freundlich)

Für Zuverlässigkeit:

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

Wenn Sie möchten, kann ich Ihnen geben:

* Ein Bash-Skript mit einem Klick (`hf_proxy_on.sh`)
* Ein permanentes `.bashrc` Proxy-Setup
* Anleitung, um OpenWebText vollständig lokal zu spiegeln und zukünftige Downloads zu vermeiden

Sagen Sie es mir einfach.