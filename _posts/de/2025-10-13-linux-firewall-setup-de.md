---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Linux-Firewall-Einrichtungsleitfaden
translated: true
type: note
---

Gute Frage — die Einrichtung einer Firewall unter Linux (wie **Red Hat** oder **Ubuntu**) erfolgt hauptsächlich mit entweder **`firewalld`** oder **`ufw`**, abhängig von Ihrem System. Nachfolgend finden Sie eine klare Anleitung für beide Familien, sodass Sie die richtige Wahl treffen können.

---

### 🔹 Unter **Red Hat / CentOS / Fedora** (firewalld)

#### 1. Prüfen, ob `firewalld` installiert und aktiv ist

```bash
sudo systemctl status firewalld
```

Wenn es nicht läuft:

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

#### 2. Grundlegende Verwendung

Aktive Zonen prüfen (Zonen gruppieren Schnittstellen und Regeln):

```bash
sudo firewall-cmd --get-active-zones
```

Alle Regeln für die aktuelle Zone auflisten:

```bash
sudo firewall-cmd --list-all
```

#### 3. Ports/Dienste erlauben oder blockieren

Einen Port erlauben (z.B. SSH auf Port 22):

```bash
sudo firewall-cmd --permanent --add-port=22/tcp
```

Einen bekannten Dienst erlauben (z.B. HTTP):

```bash
sudo firewall-cmd --permanent --add-service=http
```

Einen blockieren/entfernen:

```bash
sudo firewall-cmd --permanent --remove-service=http
```

Neu laden, um anzuwenden:

```bash
sudo firewall-cmd --reload
```

#### 4. Regeln überprüfen

```bash
sudo firewall-cmd --list-all
```

---

### 🔹 Unter **Ubuntu / Debian** (ufw)

Ubuntu wird mit **UFW** (Uncomplicated Firewall) ausgeliefert, das einfacher zu verwalten ist.

#### 1. UFW aktivieren

```bash
sudo ufw enable
```

#### 2. Ports oder Dienste erlauben/verweigern

SSH erlauben:

```bash
sudo ufw allow ssh
```

HTTP erlauben (Port 80):

```bash
sudo ufw allow 80/tcp
```

Einen spezifischen Portbereich erlauben:

```bash
sudo ufw allow 1000:2000/tcp
```

Einen Dienst verweigern:

```bash
sudo ufw deny 23/tcp
```

#### 3. Status prüfen

```bash
sudo ufw status verbose
```

#### 4. Regeln bei Bedarf zurücksetzen

```bash
sudo ufw reset
```

---

### 🔹 Für beide Systeme

Um **allen eingehenden Verkehr bis auf wenige Ausnahmen zu blockieren**, können Sie:

1. Standardmäßig alle eingehenden Verbindungen verweigern

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

   *(für `firewalld` verwenden Sie Zonen oder Drop-Zonen für ein ähnliches Verhalten)*

2. Dann selektiv Ports erlauben (z.B. 22, 80, 443).

---

### 🔹 Sicherheitstipp

**Erlauben Sie immer zuerst SSH**, bevor Sie Firewall-Regeln aus der Ferne aktivieren oder ändern — sonst schließen Sie sich selbst aus.

---

Möchten Sie, dass ich ein **Beispiel für eine minimale Firewall-Einrichtung** zeige (z.B. für einen typischen Web-Server, der nur SSH + HTTP + HTTPS erlaubt)?