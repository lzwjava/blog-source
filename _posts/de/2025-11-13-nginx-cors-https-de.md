---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Nginx CORS und HTTPS Konfiguration
translated: true
type: note
---

```nginx
# Definiert eine Map zur Handhabung der erlaubten Origins
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### Funktionsweise
- Erstellt eine Variable `$cors_origin` basierend auf dem Wert des eingehenden `Origin`-Headers (`$http_origin`).
- Wenn die Anfrage von `http://localhost:3000`, `https://example.com` oder `https://www.example.com` kommt, wird genau dieser Origin zurückgegeben.
- Für jeden anderen Origin (oder keinen Origin) wird standardmäßig `https://example.com` verwendet.
- Dies wird später verwendet, um den `Access-Control-Allow-Origin`-Header dynamisch zu setzen und CORS nur für vertrauenswürdige Frontend-Domains zu aktivieren.

---

```nginx
# HTTP zu HTTPS Weiterleitung
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### Funktionsweise
- Lauscht auf Port 80 (HTTP).
- Matcht Anfragen an `example.com` oder `api.example.com`.
- Leitet alle Anfragen permanent (301) zur HTTPS-Version derselben URL weiter.
- Erzwingt sichere Verbindungen; kein Zugriff per Plain-HTTP ist erlaubt.

---

```nginx
# Hauptseiten-Konfiguration für example.com
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### Funktionsweise
- **HTTPS-Server** für `example.com` auf Port 443 mit aktiviertem SSL.
- Verwendet **Let's Encrypt**-Zertifikate (automatisch erneuerbar, kostenlos).
- Erzwingt moderne TLS-Versionen (`TLSv1.2`, `TLSv1.3`) und starke Cipher für Sicherheit.
- Serviert statische Dateien aus `/home/project/project-web`.
- Versucht, angeforderte Datei → Verzeichnis → 404 zu servieren.
- Setzt **Cache-Header**:
  - Bilder: Cache für 30 Tage.
  - JS/CSS: Cache für 12 Stunden.
- Alle 404-Fehler werden zu `index.html` geleitet → ermöglicht **SPA (Single Page App)**-Routing (z.B. React, Vue).

---

```nginx
# API-Konfiguration für api.example.com
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # Löscht alle vorhandenen Access-Control-Header
        more_clear_headers 'Access-Control-Allow-Origin';

        # Behandelt CORS-Preflight-Anfragen
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### Funktionsweise
- **HTTPS-Reverse-Proxy** für `api.example.com`.
- Verwendet ein **separates Let's Encrypt-Zertifikat** (wahrscheinlich aufgrund mehrerer Domains/SANs).
- Der gesamte Traffic wird zu einem **lokalen Backend** auf `localhost:5000` weitergeleitet (z.B. Flask, Node.js, etc.).

#### CORS-Behandlung
- Verwendet die `$cors_origin`-Map, um **dynamisch nur genehmigte Origins zu erlauben**.
- **Löscht vorhandene** `Access-Control-Allow-Origin`-Header, um Konflikte zu vermeiden.
- Behandelt **OPTIONS-Preflight**:
  - Gibt sofort `204 No Content` zurück.
  - Erlaubt gängige Methoden und Header.
  - Cached Preflight für 1 Stunde (`Max-Age: 3600`).
- Für tatsächliche Anfragen werden CORS-Header mit `always` hinzugefügt, sodass sie auch bei Fehlerantworten erscheinen.

#### Proxy-Einstellungen
- Leitet echte Client-IP und Protokollinformationen an das Backend weiter.
- Hohe Timeouts (10 Minuten) → geeignet für langlaufende API-Operationen (z.B. Datei-Uploads, aufwändige Berechnungen).

---

### Zusammenfassung der Architektur

| Komponente          | Zweck |
|---------------------|-------|
| `example.com`       | Serviert statische SPA (React/Vue/etc.) |
| `api.example.com`   | Sichere API-Gateway → Backend auf Port 5000 |
| HTTP → HTTPS        | Gesamter Traffic wird über TLS erzwungen |
| CORS                | Eingeschränkt auf `example.com`, `www` und `localhost:3000` |
| Caching             | Für Performance optimiert |
| SSL                 | Let's Encrypt, moderne Cipher |

### Sicherheitshinweise
- Starke TLS-Konfiguration (wahrscheinlich A+ bei SSL Labs).
- CORS ist **kein Wildcard** → verhindert unbefugte API-Aufrufe von anderen Websites.
- Preflight wird effizient behandelt.
- Echte IP wird weitergeleitet → nützlich für Logging/Rate-Limiting im Backend.

Sag Bescheid, wenn du eine Diagramm- oder Dockerisierte Version möchtest!