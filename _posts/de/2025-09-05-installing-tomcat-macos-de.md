---
audio: false
generated: true
image: false
lang: de
layout: post
title: Installation von Apache Tomcat auf macOS
translated: true
type: note
---

Hier ist eine Schritt-für-Schritt-Anleitung zur Installation und Ausführung von **Apache Tomcat auf macOS**:

---

### 1. Java überprüfen

Tomcat benötigt Java. Überprüfen Sie, ob es installiert ist:

```bash
java -version
```

Wenn Sie keine Java-Version sehen (z. B. `1.8` oder `11` oder höher), installieren Sie eine. Unter macOS ist der einfachste Weg über [Homebrew](https://brew.sh):

```bash
brew install openjdk@11
```

Dann verlinken Sie es:

```bash
brew link --force --overwrite openjdk@11
```

---

### 2. Tomcat installieren (Option A: Homebrew – am einfachsten)

Mit Homebrew können Sie Tomcat schnell installieren:

```bash
brew install tomcat
```

Dies installiert in der Regel die neueste Version (z. B. Tomcat 10).

Sie finden es unter:

```
/usr/local/Cellar/tomcat/<version>/libexec
```

Oder bei Verwendung von Apple Silicon:

```
/opt/homebrew/Cellar/tomcat/<version>/libexec
```

Starten Sie es mit:

```bash
catalina run
```

---

### 3. Tomcat installieren (Option B: Manueller Download – offizielle Methode)

1. Gehen Sie zur [Apache Tomcat Website](https://tomcat.apache.org/download-10.cgi) und laden Sie den neuesten stabilen Release herunter (wählen Sie die `.tar.gz`-Datei).

2. Extrahieren Sie sie in ein Verzeichnis, zum Beispiel:

   ```bash
   tar xvf apache-tomcat-10.*.tar.gz
   mv apache-tomcat-10.* ~/tomcat
   ```

3. Starten Sie Tomcat:

   ```bash
   cd ~/tomcat/bin
   ./startup.sh
   ```

4. Um es zu stoppen:

   ```bash
   ./shutdown.sh
   ```

---

### 4. Installation überprüfen

Öffnen Sie Ihren Browser und gehen Sie zu:

```
http://localhost:8080
```

Sie sollten die Tomcat-Begrüßungsseite sehen.

---

### 5. (Optional) Zu PATH hinzufügen

Damit Sie `startup.sh` von überall ausführen können, fügen Sie dies Ihrer `~/.zshrc` oder `~/.bashrc` hinzu:

```bash
export CATALINA_HOME=~/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
```

Neu laden:

```bash
source ~/.zshrc
```

---

👉 Das war's. Sie haben nun Tomcat lokal auf macOS laufen.

Möchten Sie, dass ich Ihnen im Anschluss auch zeige, **wie man eine WAR-Datei auf Tomcat unter macOS deployed**?