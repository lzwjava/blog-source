---
audio: false
generated: true
image: false
lang: de
layout: post
title: Anleitung zum Ändern des Nginx-Ports unter macOS
translated: true
type: note
---

Sie möchten, dass Nginx auf macOS an einem **anderen Port** als dem Standard (80 für HTTP, 443 für HTTPS) lauscht. Hier ist eine klare Schritt-für-Schritt-Anleitung:

---

### 1. Suchen Sie Ihre Nginx-Konfigurationsdatei

* Wenn Sie es über **Homebrew** installiert haben, ist die Standardkonfiguration normalerweise:

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  oder, auf Apple Silicon:

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* Wenn Sie es manuell installiert haben, könnte sie unter `/usr/local/nginx/conf/nginx.conf` liegen.

---

### 2. Bearbeiten Sie die `listen`-Direktive

1. Öffnen Sie die Konfiguration in einem Texteditor:

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. Suchen Sie den `server`-Block:

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. Ändern Sie `listen 80;` zu Ihrem gewünschten Port, z.B. 8080:

   ```nginx
   listen 8080;
   ```

---

### 3. Testen Sie die Konfiguration

Führen Sie aus:

```bash
nginx -t
```

* Wenn `syntax is ok` und `test is successful` angezeigt wird, ist Ihre Konfiguration gültig.
* Bei Fehlern prüfen Sie die angegebenen Zeilennummern.

---

### 4. Starten Sie Nginx neu

* Wenn es über Homebrew installiert wurde:

```bash
brew services restart nginx
```

* Oder manuell:

```bash
sudo nginx -s reload
```

---

### 5. Zugriff über den neuen Port

* In Ihrem Browser oder mit curl:

```
http://localhost:8080
```

---

**Zusätzliche Hinweise:**

* Ports **<1024** erfordern `sudo` auf macOS. Die Verwendung von Ports wie 80 erfordert also Root-Rechte, Ports wie 8080 oder 3000 jedoch nicht.
* Wenn Sie mehrere Nginx-Server gleichzeitig betreiben möchten, **muss jeder einen eindeutigen Port haben**.

---

Ich kann Ihnen auch einen **schnellen Trick zeigen, um Nginx temporär auf einem beliebigen Port zu starten, ohne die nginx.conf zu bearbeiten**, indem Sie ein Kommandozeilen-Flag verwenden. Das ist praktisch für Tests. Soll ich Ihnen das zeigen?