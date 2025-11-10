---
audio: false
generated: true
image: false
lang: de
layout: post
title: Proxyschema wird nicht unterstützt
translated: true
type: note
---

Der Fehler zeigt an, dass die `httpx`-Bibliothek, die vom `openai`-Client in Ihrem `gitmessageai.py`-Skript verwendet wird, versucht, einen Proxy mit der URL `socks://127.0.0.1:7891/` zu konfigurieren, aber das Schema `socks` nicht unterstützt oder erkannt wird, was zu einem `ValueError: Unknown scheme for proxy URL` führt. Dies deutet darauf hin, dass eine Proxy-Konfiguration aus Ihrer Umgebung oder Ihrem Code übernommen wird und ein nicht unterstütztes SOCKS-Proxy-Schema verwendet.

Lassen Sie uns aufschlüsseln, woher der Proxy kommen könnte und wie Sie das Problem beheben können.

### Woher kommt der Proxy?

Die Proxy-Konfiguration (`socks://127.0.0.1:7891/`) stammt wahrscheinlich aus einer der folgenden Quellen:

1. **Umgebungsvariablen**
   - Die `httpx`-Bibliothek überprüft automatisch die Proxy-Einstellungen in Umgebungsvariablen wie `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY` oder deren Kleinbuchstaben-Varianten (`http_proxy`, `https_proxy`, `all_proxy`).
   - Ein Wert wie `socks://127.0.0.1:7891/` deutet auf einen SOCKS-Proxy hin (üblich für Tools wie Shadowsocks oder VPNs), der in einer dieser Variablen gesetzt wurde.
   - Um zu überprüfen, ob diese Variablen gesetzt sind, führen Sie Folgendes in Ihrem Terminal aus:
     ```bash
     env | grep -i proxy
     ```
     Suchen Sie nach Variablen wie `HTTP_PROXY=socks://127.0.0.1:7891` oder `HTTPS_PROXY=socks://127.0.0.1:7891`.

2. **Systemweite Proxy-Einstellungen**
   - Wenn Sie ein Linux-System verwenden, könnten Proxy-Einstellungen global konfiguriert sein (z. B. in `/etc/environment`, `/etc/profile` oder Ihrer Shell-Konfiguration wie `~/.bashrc`, `~/.zshrc` oder `~/.profile`).
   - Überprüfen Sie diese Dateien auf Zeilen wie:
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - Sie können diese Dateien mit folgenden Befehlen einsehen:
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **Proxy-Konfiguration in einem Proxy-Tool**
   - Die Adresse `127.0.0.1:7891` wird häufig von Proxy- oder VPN-Tools wie Shadowsocks, V2Ray oder Clash verwendet, die oft standardmäßig SOCKS5-Proxys auf Ports wie 7890 oder 7891 verwenden.
   - Wenn Sie ein solches Tool installiert oder konfiguriert haben, könnte es automatisch Umgebungsvariablen oder systemweite Proxy-Einstellungen gesetzt haben.

4. **Expliziter Proxy im Code**
   - Weniger wahrscheinlich, aber Ihr `gitmessageai.py`-Skript oder eine verwendete Bibliothek könnte explizit einen Proxy konfigurieren. Da der Fehler in `httpx` auftritt, überprüfen Sie, ob Ihr Skript einen Proxy an den `OpenAI`-Client oder `httpx`-Client übergibt.
   - Durchsuchen Sie Ihr Skript nach Begriffen wie `proxy`, `proxies` oder `httpx.Client`:
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Python-Bibliothekskonfiguration**
   - Einige Python-Bibliotheken (z. B. `requests` oder `httpx`) könnten Proxy-Einstellungen von einer Konfigurationsdatei oder einem vorherigen Setup übernehmen. `httpx` verläss sich jedoch primär auf Umgebungsvariablen oder expliziten Code.

### Warum verursacht `socks://` ein Problem?

- Die `httpx`-Bibliothek (verwendet von `openai`) unterstützt das `socks`-Schema (SOCKS4/SOCKS5-Proxys) nativ nicht, es sei denn, zusätzliche Abhängigkeiten wie `httpx-socks` sind installiert.
- Der Fehler `Unknown scheme for proxy URL` tritt auf, weil `httpx` Proxys mit Schemata wie `http://` oder `https://` erwartet, nicht `socks://`.

### Wie Sie das Problem beheben

Sie haben zwei Möglichkeiten: **Entfernen oder Umgehen des Proxys**, wenn er nicht benötigt wird, oder **Unterstützung des SOCKS-Proxys**, wenn Sie ihn verwenden möchten.

#### Option 1: Proxy entfernen oder umgehen

Wenn Sie keinen Proxy für die DeepSeek-API benötigen, können Sie die Proxy-Konfiguration deaktivieren oder umgehen.

1. **Umgebungsvariablen zurücksetzen**
   - Wenn der Proxy in Umgebungsvariablen gesetzt ist, setzen Sie sie für Ihre Sitzung zurück:
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - Um dies dauerhaft zu machen, entfernen Sie die entsprechenden `export`-Zeilen aus `~/.bashrc`, `~/.zshrc`, `/etc/environment` oder anderen Shell-Konfigurationsdateien.

2. **Skript ohne Proxy ausführen**
   - Führen Sie Ihr Skript vorübergehend ohne Proxy-Einstellungen aus:
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - Wenn dies funktioniert, war der Proxy das Problem.

3. **Proxy im Code umgehen**
   - Modifizieren Sie Ihr `gitmessageai.py`-Skript, um Proxys im `OpenAI`-Client explizit zu deaktivieren:
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # Proxys deaktivieren
         )
         # Ihre API-Aufruflogik hier
         response = client.chat.completions.create(
             model="deepseek",  # Durch korrektes Modell ersetzen
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Das Setzen von `proxies=None` stellt sicher, dass `httpx` alle Umgebungs-Proxy-Einstellungen ignoriert.

#### Option 2: SOCKS-Proxy unterstützen

Wenn Sie den SOCKS-Proxy verwenden müssen (z. B. für den Zugriff auf die DeepSeek-API über einen VPN- oder Proxy-Server), müssen Sie SOCKS-Unterstützung zu `httpx` hinzufügen.

1. **`httpx-socks` installieren**
   - Installieren Sie das `httpx-socks`-Paket, um SOCKS4/SOCKS5-Proxy-Unterstützung zu aktivieren:
     ```bash
     pip install httpx-socks
     ```
   - Dies erweitert `httpx`, um `socks://` und `socks5://` Schemata zu verarbeiten.

2. **Ihren Code aktualisieren**
   - Modifizieren Sie Ihr Skript, um den SOCKS-Proxy explizit zu verwenden:
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # SOCKS5-Proxy konfigurieren
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # Ihre API-Aufruflogik hier
         response = client.chat.completions.create(
             model="deepseek",  # Durch korrektes Modell ersetzen
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Ersetzen Sie `socks5://` durch `socks4://`, wenn Ihr Proxy SOCKS4 verwendet.

3. **Proxy-Server überprüfen**
   - Stellen Sie sicher, dass der Proxy-Server unter `127.0.0.1:7891` läuft. Wenn Sie ein Tool wie Clash oder Shadowsocks verwenden, überprüfen Sie dessen Status:
     ```bash
     netstat -tuln | grep 7891
     ```
   - Wenn kein Prozess auf Port 7891 lauscht, starten Sie Ihr Proxy-Tool oder korrigieren Sie den Port in der Proxy-URL.

### Zusätzliche Debugging-Schritte

- **Proxy-Tool-Konfiguration überprüfen**
  - Wenn Sie ein Proxy-Tool wie Clash oder Shadowsocks verwenden, verifizieren Sie dessen Konfigurationsdatei (z. B. `~/.config/clash/config.yaml`), um zu bestätigen, dass es `127.0.0.1:7891` für SOCKS5 verwendet.
  - Stellen Sie sicher, dass das Tool läuft und zugänglich ist.

- **Proxy-Konnektivität testen**
  - Testen Sie den Proxy mit einem Tool wie `curl` (erfordert `curl` mit SOCKS-Unterstützung):
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - Wenn dies fehlschlägt, ist der Proxy-Server entweder nicht aktiv oder falsch konfiguriert.

- **Proxy-Nutzung protokollieren**
  - Fügen Sie Ihrem Skript Logging hinzu, um zu bestätigen, welcher Proxy verwendet wird:
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

### Empfohlene Lösung

Wenn Sie den Proxy nicht benötigen, ist die einfachste Lösung, ihn zu deaktivieren, indem Sie die Umgebungsvariablen zurücksetzen und ausführen:
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

Wenn Sie den Proxy benötigen, installieren Sie `httpx-socks` und aktualisieren Sie Ihren Code, um `SyncProxyTransport` wie oben gezeigt zu verwenden.

### Referenzen
- [httpx Dokumentation](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [DeepSeek API Dokumentation](https://platform.deepseek.com/docs)