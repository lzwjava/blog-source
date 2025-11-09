---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben des libcurl-Konfigurationsfehlers
translated: true
type: note
---

Dieser Fehler bedeutet, dass das `configure`-Skript versucht, **libcurl** (eine Bibliothek für HTTP/HTTPS-Anfragen) zu finden, es aber `curl-config` – ein Hilfsprogramm, das den Installationsort von libcurl mitteilt – nicht lokalisieren kann.

So beheben Sie das Problem, abhängig von Ihrem System:

---

### 🧩 Für Ubuntu / Debian

Führen Sie aus:

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

Versuchen Sie es dann erneut:

```bash
./configure
```

---

### 🧩 Für Fedora / CentOS / RHEL

Führen Sie aus:

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 Für Arch / Manjaro

Führen Sie aus:

```bash
sudo pacman -S curl
```

---

### 🔍 Zur Überprüfung der Installation

Stellen Sie nach der Installation sicher, dass `curl-config` verfügbar ist:

```bash
which curl-config
```

Wenn ein Pfad wie `/usr/bin/curl-config` zurückgegeben wird, ist alles in Ordnung.

Führen Sie dann erneut aus:

```bash
./configure
make
sudo make install
```

---

Möchten Sie, dass ich erkläre, was `curl-config` eigentlich macht und warum `configure` es benötigt?