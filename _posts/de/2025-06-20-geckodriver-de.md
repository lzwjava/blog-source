---
audio: false
generated: true
lang: de
layout: post
title: Selenium GeckoDriver Installation unter Ubuntu
translated: true
type: note
---

Um den Selenium Firefox-Treiber (geckodriver) auf Ubuntu zu installieren, folgen Sie diesen Schritten:

1. **Firefox installieren** (falls noch nicht installiert):
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **geckodriver herunterladen**:
   - Besuchen Sie die [geckodriver releases page](https://github.com/mozilla/geckodriver/releases).
   - Wählen Sie die neueste Version, die mit Ihrer Firefox-Version kompatibel ist. Für Ubuntu laden Sie die Linux 64-bit Version herunter (z.B. `geckodriver-vX.XX.X-linux64.tar.gz`).
   - Beispielbefehl zum Herunterladen (ersetzen Sie `X.XX.X` mit der neuesten Version):
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **Die heruntergeladene Datei entpacken**:
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **geckodriver in einen Systempfad verschieben**:
   - Verschieben Sie den entpackten `geckodriver` nach `/usr/local/bin`, um ihn systemweit zugänglich zu machen:
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - Machen Sie ihn ausführbar:
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **Selenium für Python installieren** (falls Sie Python verwenden):
   ```bash
   pip install selenium
   ```

6. **Installation überprüfen**:
   - Überprüfen Sie die geckodriver-Version:
     ```bash
     geckodriver --version
     ```
   - Testen Sie mit einem einfachen Python-Skript:
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**Hinweise**:
- Stellen Sie sicher, dass Ihre Firefox-Version mit der geckodriver-Version kompatibel ist (überprüfen Sie die Release Notes auf der geckodriver GitHub-Seite).
- Falls Sie auf Probleme stoßen, stellen Sie sicher, dass `python3-pip` installiert ist:
  ```bash
  sudo apt install python3-pip
  ```
- Falls geckodriver nicht gefunden wird, fügen Sie `/usr/local/bin` zu Ihrem `PATH` hinzu:
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

Dies sollte den Selenium Firefox-Treiber auf Ubuntu einrichten. Lassen Sie mich wissen, falls Sie auf Probleme stoßen!

---

Der Unterschied zwischen `geckodriver-v0.36.0-linux-aarch64.tar.gz` und `geckodriver-v0.36.0-linux64.tar.gz` liegt in der Ziel-CPU-Architektur:

- **linux-aarch64**: Dies ist für 64-bit ARM-Architekturen (z.B. ARMv8-A), die häufig in Geräten wie dem Raspberry Pi, einigen Servern oder modernen ARM-basierten Linux-Systemen verwendet werden. "aarch64" steht für 64-bit ARM-Architektur.

- **linux64**: Dies ist für 64-bit x86-Architekturen (auch bekannt als x86_64 oder AMD64), die Standard für die meisten Desktop- und Server-PCs mit Linux sind.

**Wichtige Punkte**:
- Wählen Sie `linux-aarch64`, wenn Ihr System einen 64-bit ARM-Prozessor hat.
- Wählen Sie `linux64`, wenn Ihr System einen 64-bit x86-Prozessor hat.
- Sie können die Architektur Ihres Systems unter Linux mit dem Befehl `uname -m` überprüfen. Wenn die Ausgabe `aarch64` ist, verwenden Sie die ARM-Version; wenn die Ausgabe `x86_64` ist, verwenden Sie die linux64-Version.

Die `.asc`-Dateien sind GPG-Signaturen zur Überprüfung der Integrität und Authentizität der entsprechenden `.tar.gz`-Dateien.