---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Konfiguration des Hugging Face XetHub-Proxys
translated: true
type: note
---

Ja — **Rust reqwest unterstützt absolut eine explizite Proxy-Konfiguration**, und Hugging Faces XetHub-Client (geschrieben in Rust) erlaubt dies ebenfalls.
ABER: Hugging Face stellt **keine Python-API** bereit, um Proxy-Einstellungen direkt zu übergeben.
Stattdessen verlässt sich XetHub auf **Umgebungsvariablen**, die reqwest automatisch ausliest.

Die explizite Proxy-Konfiguration für reqwest sieht also so aus:

---

# ✔ Wie reqwest Proxys erkennt (offiziell)

Reqwest verwendet automatisch die folgenden **Umgebungsvariablen**:

* `https_proxy`
* `http_proxy`
* `all_proxy`

Kleinbuchstaben sind der wichtige Teil.
Reqwest **ignoriert** Großbuchstaben-Variablen (`HTTPS_PROXY`), es sei denn, ein bestimmtes Feature-Flag wurde zur Kompilierzeit aktiviert.

**Hugging Face XetHub verwendet das Standard-reqwest → nur Kleinbuchstaben.**

Das bedeutet:

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

ist die einzige garantiert funktionierende explizite Proxy-Konfiguration für XetHub.

---

# ✔ Wie HuggingFace XetHub die Proxy-Konfiguration lädt

Wenn Python `load_dataset` ausführt, wird ein Rust-Binary ausgelöst, das:

1. Nach Proxy-Umgebungsvariablen in Kleinbuchstaben sucht
2. URLs umschreibt
3. Verbindungen über reqwest öffnet
4. Datei-Chunks von `https://transfer.xethub.hf.co` herunterlädt

Wenn diese Umgebungsvariablen nicht gesetzt oder erreichbar sind → Verbindung abgelehnt.

---

# ✔ Manuelles Erzwingen der Proxy-Nutzung in reqwest (Referenzcode)

Nur um zu zeigen, was reqwest intern tun würde:

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

Hugging Faces XetHub-Client *macht etwas Gleichwertiges*, aber ausgelöst durch Umgebungsvariablen.

---

# ✔ Vollständige explizite Proxy-Konfiguration, die immer mit reqwest funktioniert (HF-kompatibel)

Führe **alle** diese Befehle aus:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

Verwende `http` Proxy, nicht `socks5`, weil:

* Die SOCKS-Unterstützung von reqwest optional ist
* Das XetHub-Client-Binary für HF nicht damit kompiliert wurde

Daher kann SOCKS stillschweigend fehlschlagen.

---

# ✔ Überprüfen, ob dein Proxy verwendet wird

Versuche:

```bash
env | grep proxy
```

Wenn du Kleinbuchstaben siehst → gut.

Dann:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Wenn curl erfolgreich ist → wird reqwest erfolgreich sein.

---

# Zusammenfassung

* Hugging Face Datasets laden manchmal über **XetHub** (Rust reqwest Client)
* Reqwest respektiert standardmäßig nur **Kleinbuchstaben** Proxy-Variablen
* Du musst sie explizit setzen
* Verwende **HTTP** Proxy, nicht SOCKS
* `HF_HUB_DISABLE_XETHUB=1` kann reqwest komplett umgehen, falls nötig

---

Falls du möchtest, kann ich vorbereiten:

* Ein "HF Proxy Fix"-Skript mit einem Befehl
* Eine persistente Konfiguration für deine `.bashrc`
* Eine Auto-Erkennung, um zu bestätigen, ob reqwest den Proxy verwendet

Sag mir einfach Bescheid.