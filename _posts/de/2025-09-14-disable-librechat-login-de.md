---
audio: false
date: 2025-09-14
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Deaktivierung der LibreChat-Anmeldeauthentifizierung
translated: true
type: note
---

Um **LibreChat** ohne häufige Anmeldungen nutzen zu können (oder die Anmeldung komplett zu deaktivieren), können Sie die Authentifizierungseinstellungen anpassen. Hier sind die Schritte zur Problemlösung:

---

### **1. Authentifizierung deaktivieren (Keine Anmeldung erforderlich)**
Wenn Sie möchten, dass **LibreChat komplett offen** ist (ohne jegliche Anmeldung), passen Sie die Konfiguration wie folgt an:

#### **Option A: Umgebungsvariablen (Empfohlen)**
Setzen Sie Folgendes in Ihrer `.env`-Datei (oder in den Umgebungsvariablen):
```env
# Authentifizierung komplett deaktivieren
AUTHENTICATION=false
```
Starten Sie LibreChat dann neu:
```bash
docker compose down && docker compose up -d  # Bei Verwendung von Docker
# ODER
npm run build && npm run start  # Bei lokaler Ausführung
```

#### **Option B: `config.yaml` modifizieren**
Wenn Sie eine `config.yaml`-Datei verwenden, fügen Sie hinzu:
```yaml
auth:
  enabled: false
```

---

### **2. Problem häufiger Abmeldungen beheben (Falls Sie die Anmeldung beibehalten möchten)**
Wenn Sie **die Authentifizierung beibehalten**, aber das Problem der häufigen Abmeldungen beheben möchten, versuchen Sie diese Lösungen:

#### **A. Sitzungs-/Cookie-Ablaufzeit erhöhen**
Passen Sie die Sitzungseinstellungen in `.env` an:
```env
# Sitzungs-Timeout verlängern (in Sekunden, z.B. 7 Tage = 604800)
SESSION_EXPIRY=604800

# Sicherstellen, dass Cookies sicher sind (bei HTTPS-Verwendung)
COOKIE_SECURE=true  # Für Tests auf HTTP auf 'false' setzen
COOKIE_SAME_SITE=lax
```

#### **B. Einen persistenten Sitzungsspeicher verwenden**
Standardmäßig verwendet LibreChat möglicherweise Sitzungen im Arbeitsspeicher (die bei einem Neustart zurückgesetzt werden). Wechseln Sie zu einem **datenbankbasierten Sitzungsspeicher** (z.B. Redis oder PostgreSQL):

1. **Redis installieren** (falls noch nicht geschehen):
   ```bash
   docker run -d --name redis -p 6379:6379 redis
   ```
2. `.env` aktualisieren:
   ```env
   SESSION_STORE=redis
   REDIS_URL=redis://localhost:6379
   ```

#### **C. Reverse-Proxy-Einstellungen prüfen (Bei Verwendung von Nginx/Apache)**
Wenn Sie hinter einem Proxy (z.B. Nginx) liegen, stellen Sie sicher:
- Dass Cookies korrekt weitergeleitet werden.
- Dass `ProxyPass` `cookie`-Direktiven enthält.

Beispiel-Nginx-Konfiguration:
```nginx
location / {
    proxy_pass http://localhost:3080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_cookie_path / /;  # Sicherstellen, dass Cookies nicht falsch gescoped sind
}
```

#### **D. Browser-Cache leeren & Im Inkognito-Modus testen**
Manchmal verursachen Browser-Cache oder beschädigte Cookies Probleme. Versuchen Sie:
- Cookies für `librechat.example.com` zu löschen.
- Im **Inkognito-Modus** oder einem anderen Browser zu testen.

---

### **3. Cookie-Probleme debuggen**
Wenn Cookies weiterhin nicht persistent sind:
1. **Browser-DevTools prüfen** (`F12` > **Application** > **Cookies**), um zu sehen, ob `connect.sid` (oder ähnliches) gesetzt wird.
2. **Das `SameSite`-Attribut überprüfen** (sollte `Lax` oder `None` bei cross-site sein).
3. **Sicherstellen, dass die `Domain` korrekt ist** (z.B. `.example.com` für Subdomains).

---

### **4. LibreChat aktualisieren**
Wenn Sie eine ältere Version verwenden, könnten Fehler in neueren Releases behoben sein:
```bash
git pull origin main
docker compose down && docker compose up -d --build
```

---

### **Abschließende Hinweise**
- **Sicherheitswarnung**: Das Deaktivieren der Authentifizierung (`AUTHENTICATION=false`) macht LibreChat **öffentlich zugänglich**. Tun Sie dies nur in vertrauenswürdigen/internen Netzwerken.
- **HTTPS erforderlich**: Wenn Sie Cookies verwenden, stellen Sie sicher, dass Ihre Seite **HTTPS** verwendet (oder setzen Sie `COOKIE_SECURE=false` für Tests).