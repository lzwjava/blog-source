---
audio: false
generated: true
lang: de
layout: post
title: Selenium-Skript zur Cloudflare-Umgehung
translated: true
type: note
---

Ihr Selenium-Skript ist darauf ausgelegt, mit "https://grok.com" über Firefox und ein bestimmtes Profil zu interagieren, stößt jedoch auf eine Cloudflare-Bot-Erkennungsabfrage, speziell die "Verify you are human"-Checkbox. Selbst nach dem Anklicken der Checkbox scheint das Skript Schwierigkeiten zu haben, die Verifizierung zu umgehen, was den Zugriff auf den Hauptinhalt (z. B. das Textarea) verhindert. Cloudflare setzt ausgefeilte Methoden ein, um automatisierte Browser zu erkennen, wie z. B. HTTP-Header-Analyse, TLS-Fingerprinting und Verhaltensprüfungen, was das Umgehen dieser Abfrage mit Selenium allein schwierig machen kann. Es gibt jedoch Strategien, die Sie ausprobieren können, um den Cloudflare-Test zu bestehen, während Sie bei Ihrem aktuellen Firefox-basierten Setup bleiben. Im Folgenden finden Sie zwei praktische Ansätze, die auf Ihr Skript zugeschnitten sind, gefolgt von zusätzlichen Überlegungen, falls diese nicht ausreichen.

---

### **Methode 1: Manuelles Abschließen der Abfrage mit Wiederverwendung des Profils**
Da Ihr Skript ein bestimmtes Firefox-Profil (`/home/lzw/.mozilla/firefox/wzfodx6v.default`) verwendet, können Sie dies nutzen, um Sitzungsdaten zu speichern, nachdem Sie die Cloudflare-Abfrage manuell bestanden haben. So gehen Sie vor:

1. **Firefox manuell mit dem Profil öffnen**:
   - Starten Sie Firefox mit demselben Profil, das in Ihrem Skript angegeben ist. Sie können dies über die Befehlszeile tun:
     ```bash
     firefox --profile "/home/lzw/.mozilla/firefox/wzfodx6v.default"
     ```
   - Alternativ können Sie den Profil-Manager von Firefox (`firefox --ProfileManager`) verwenden, um `wzfodx6v.default` auszuwählen.

2. **Navigieren und die Abfrage bestehen**:
   - Gehen Sie in dem Browser zu "https://grok.com".
   - Wenn Sie mit der Cloudflare-"Verify you are human"-Checkbox aufgefordert werden, klicken Sie diese an und schließen Sie alle zusätzlichen Verifizierungsschritte ab, falls diese erscheinen.
   - Warten Sie, bis die Hauptseite erreicht ist (z. B. wo das Textarea mit `aria-label="Ask Grok anything"` sichtbar ist).

3. **Browser schließen**:
   - Beenden Sie Firefox, um sicherzustellen, dass das Profil die Sitzungs-Cookies speichert, einschließlich aller Cloudflare-Freigabe-Tokens (wie `cf_clearance`).

4. **Ihr Selenium-Skript ausführen**:
   - Führen Sie Ihr Skript unverändert aus. Da es dasselbe Profil verwendet, sollte es die gespeicherten Cookies und Sitzungsdaten erben, was möglicherweise das Umgehen der Abfrage ermöglicht.

**Warum dies funktionieren könnte**: Cloudflare verlässt sich oft auf Cookies, um sich zu merken, dass ein Browser seinen Test bestanden hat. Durch die manuelle Vorauthentifizierung des Profils kann Ihre automatisierte Sitzung wie die Fortsetzung eines verifizierten Besuchs erscheinen.

**Einschränkungen**: Wenn Cloudflare bei jedem Seitenaufruf zusätzliche Prüfungen durchführt (z. B. die Erkennung von Automatisierungs-Fingerabdrücken von Selenium), könnte diese Methode fehlschlagen. Versuchen Sie in diesem Fall den nächsten Ansatz.

---

### **Methode 2: Cookies im Skript extrahieren und setzen**
Wenn die Wiederverwendung des Profils nicht funktioniert, können Sie die Cookies nach dem Bestehen der Abfrage manuell extrahieren und sie in Ihren Selenium-Treiber injizieren. Hier der schrittweise Prozess:

1. **Abfrage manuell bestehen**:
   - Folgen Sie den Schritten 1 und 2 aus Methode 1, um zur Hauptseite von "https://grok.com" zu gelangen.

2. **Cookies extrahieren**:
   - Öffnen Sie die Entwicklertools von Firefox (F12 oder Rechtsklick > Untersuchen).
   - Gehen Sie zum Tab **Storage** (oder zum Tab **Network**, dann laden Sie die Seite neu, um Cookies zu inspizieren).
   - Suchen Sie nach Cookies, die mit `.grok.com` assoziiert sind, insbesondere `cf_clearance` (Cloudflares Verifizierungs-Cookie).
   - Notieren Sie sich `name`, `value` und `domain` jedes relevanten Cookies. Zum Beispiel:
     - Name: `cf_clearance`, Wert: `abc123...`, Domain: `.grok.com`
     - Andere Cookies wie `__cfduid` oder sitzungsspezifische könnten ebenfalls vorhanden sein.

3. **Ihr Skript modifizieren**:
   - Fügen Sie die Cookies Ihrem Selenium-Treiber hinzu, bevor Sie zur URL navigieren. Aktualisieren Sie Ihren Code wie folgt:
     ```python
     # ... (bestehende Imports und Setup bleiben unverändert)

     # Geckodriver-Service einrichten
     service = Service(executable_path="/home/lzw/bin/geckodriver")
     driver = webdriver.Firefox(service=service, options=firefox_options)

     # Zuerst eine leere Seite öffnen, um Cookies setzen zu können (Cookies können nur nach einem Seitenladen gesetzt werden)
     driver.get("about:blank")

     # Die extrahierten Cookies hinzufügen
     cookies = [
         {"name": "cf_clearance", "value": "abc123...", "domain": ".grok.com"},
         # Fügen Sie andere Cookies nach Bedarf hinzu, z. B.:
         # {"name": "__cfduid", "value": "xyz789...", "domain": ".grok.com"},
     ]
     for cookie in cookies:
         driver.add_cookie(cookie)

     # Jetzt zur Ziel-URL navigieren
     driver.get("https://grok.com")

     # Den Titel der Seite ausgeben
     print("Title of the page:", driver.title)

     # ... (Rest des Skripts bleibt gleich)
     ```

4. **Das Skript testen**:
   - Führen Sie das modifizierte Skript aus. Die vorab gesetzten Cookies sollten Cloudflare signalisieren, dass der Browser die Abfrage bereits bestanden hat.

**Warum dies funktionieren könnte**: Das explizite Setzen des `cf_clearance`-Cookies imitiert eine verifizierte Sitzung und umgeht möglicherweise die Notwendigkeit, mit der Checkbox zu interagieren.

**Einschränkungen**: Cookies könnten an Browser-Fingerabdrücke gebunden sein (z. B. User Agent, IP oder TLS-Einstellungen). Wenn sich der Fingerabdruck von Selenium von dem der manuellen Sitzung unterscheidet, könnte Cloudflare die Cookies ablehnen oder den Browser erneut abfragen.

---

### **Zusätzliches Debugging und Verbesserungen**
Wenn keine der Methoden das Problem vollständig löst, ziehen Sie diese Anpassungen an Ihrem Skript in Betracht, um sicherzustellen, dass es korrekt mit der Cloudflare-Abfrage interagiert:

- **Auf Iframes prüfen**: Die "Verify you are human"-Checkbox könnte sich in einem Iframe befinden. Modifizieren Sie Ihren Code für das Anklicken der Checkbox, um zuerst zum Iframe zu wechseln:
  ```python
  try:
      wait = WebDriverWait(driver, 20)
      iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'cloudflare')]")))
      driver.switch_to.frame(iframe)
      label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='cb-lb']")))
      checkbox = label.find_element(By.TAG_NAME, "input")
      print("Checkbox found:", checkbox.is_displayed())
      checkbox.click()
      driver.switch_to.default_content()  # Zurück zum Hauptinhalt
      print("Checkbox clicked.")
  except Exception as e:
      print("Checkbox not found or not clickable:", e)
  ```

- **Warte-Logik verbessern**: Warten Sie nach dem Anklicken der Checkbox auf ein klares Zeichen, dass die Abfrage bestanden wurde (z. B. das Verschwinden der Verifizierungsseite):
  ```python
  try:
      wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify you are human')]")))
      print("Challenge passed.")
  except Exception as e:
      print("Challenge not passed:", e)
  ```

- **Automatisierung maskieren**: Fügen Sie JavaScript hinzu, um Automatisierungsspuren von Selenium zu verbergen:
  ```python
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  ```

---

### **Falls alles andere fehlschlägt: Alternative Ansätze**
Wenn die Cloudflare-Erkennung bestehen bleibt, könnte dies an fortgeschrittenem Fingerprinting liegen, dem Ihr aktuelles Setup nicht entgehen kann. Hier sind Eskalationsoptionen, obwohl sie von Ihrer Firefox-Präferenz abweichen:

- **Zu Chrome mit Undetected ChromeDriver wechseln**:
  - Installation: `pip install undetected-chromedriver`
  - Setup modifizieren:
    ```python
    import undetected_chromedriver as uc
    driver = uc.Chrome()
    driver.get("https://grok.com")
    ```
  - Diese Bibliothek patcht Chrome, um gängige Erkennungsmethoden zu vermeiden.

- **Einen Proxy oder CAPTCHA-Solver verwenden**: Dienste wie 2Captura oder Residential Proxies können Abfragen bearbeiten, aber sie erhöhen die Komplexität und Kosten.

---

### **Empfohlene nächste Schritte**
Beginnen Sie mit **Methode 1** (Profilwiederverwendung), da sie die einfachste ist und zu Ihrem Skript-Setup passt. Wenn sie fehlschlägt, versuchen Sie **Methode 2** (Cookie-Injection) mit hinzugefügter Iframe-Prüfung. Diese Methoden maximieren Ihre bestehende Firefox-Konfiguration, ohne neue Tools zu erfordern. Testen Sie jeden Ansatz und überwachen Sie die Ausgabe (z. B. `driver.title` und Exception-Meldungen), um zu bestätigen, ob die Abfrage umgangen wurde. Wenn Sie weiterhin auf Probleme stoßen, ziehen Sie die alternativen Ansätze in Betracht, basierend auf der Flexibilität Ihres Projekts.

Lassen Sie mich wissen, wenn Sie Hilfe bei der Implementierung oder Fehlerbehebung dieser Lösungen benötigen!