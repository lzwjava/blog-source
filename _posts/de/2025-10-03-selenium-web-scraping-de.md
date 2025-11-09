---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erklärung von Selenium Web Scraping Code
translated: true
type: note
---

### Erklärung der Verwendung der Selenium-API im bereitgestellten Code

Dieses Python-Skript verwendet die **Selenium WebDriver**-Bibliothek, um einen Webbrowser (insbesondere Chrome) für die Interaktion mit einer Website (wahrscheinlich ein Daten-/Handelsportal unter `https://xxdata.com/index.aspx`) zu automatisieren. Das Ziel scheint Web Scraping zu sein: Anmelden, Suchen nach Handels-/Bestelldaten (unter Verwendung eines HS-Codes wie '8449'), Navigieren durch paginierte Ergebnisse, Anklicken von Details, Extrahieren strukturierter Daten aus HTML-Tabellen und Speichern in einer SQLite-Datenbank (`data.db`).

Selenium wird hier für **Browser-Automatisierung** verwendet, was es dem Skript ermöglicht, menschliche Interaktionen wie Tippen, Klicken, Scrollen und Warten auf Seitenladungen nachzuahmen – etwas, das mit einfachen HTTP-Anfragen (z. B. aufgrund von JavaScript-lastigen Seiten, Iframes oder dynamischen Inhalten) schwierig oder unmöglich ist. Es behandelt dynamische Webelemente, Sitzungen und das Wechseln zwischen mehreren Fenstern/Iframes, was in modernen Web-Apps üblich ist.

Ich werde es **Abschnitt für Abschnitt** aufschlüsseln und dabei die wichtigsten Selenium-APIs, ihren Zweck und ihre Verwendung hervorheben. Hinweis: Einige Methoden im Code (z. B. `find_element_by_css_selector`) stammen aus älteren Selenium-Versionen (vor 4.0) und sind veraltet. Im modernen Selenium (4+) würde man stattdessen `find_element(By.CSS_SELECTOR, ...)` verwenden, aber die Funktionalität ist dieselbe. Das Skript importiert auch die notwendigen Module für Waits, Exceptions und die Elementbehandlung.

#### 1. **Imports und Setup (Selenium-Initialisierung)**
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.webdriver import WebDriver
   from selenium.webdriver.common.keys import Keys
   from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   ```
   - **Zweck**: Diese importieren die Kernkomponenten von Selenium:
     - `webdriver`: Hauptmodul zur Steuerung des Browsers.
     - `WebDriver`: Typ-Hinweis für die Browser-Instanz (stellt Typsicherheit sicher).
     - `Keys`: Zum Simulieren von Tastatureingaben (z. B. Page Up).
     - Exceptions: Behandeln häufige Fehler wie Timeouts oder stale elements (Elemente, die sich nach einem Seitenrefresh ändern).
     - `WebDriverWait` und `EC` (Expected Conditions): Für explizite Waits – Abfragen, bis ein Element eine Bedingung erfüllt (z. B. auf der Seite vorhanden).
     - `By`: Locator-Strategien (z. B. CSS-Selector, ID, Tag-Name), um Elemente zu finden.
     - `WebElement`: Repräsentiert HTML-Elemente für die Interaktion.

   In der `run()`-Funktion:
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # Öffnet den Browser im Vollbildmodus.
   options.add_argument('--log-level=3')      # Unterdrückt Konsolenprotokolle für eine sauberere Ausgabe.
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **Verwendete Selenium-API**: `webdriver.Chrome(options=...)`
     - Initialisiert eine Chrome-Browser-Instanz unter Verwendung einer lokalen `chromedriver`-Executable (muss sich im Skriptverzeichnis befinden).
     - `ChromeOptions`: Passt die Browser-Sitzung an (z. B. könnte der Headless-Modus mit `options.add_argument("--headless")` für Hintergrundbetrieb hinzugefügt werden).
     - Dies erzeugt ein lebendiges, steuerbares Browserfenster. Selenium fungiert als Brücke zwischen Python und dem DevTools-Protokoll des Browsers.

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **Verwendete Selenium-API**: `WebDriver.get(url)`
     - Navigiert zur Start-URL und lädt die Seite, wie ein Benutzer, der sie in die Adressleiste tippt.

#### 2. **Anmeldeprozess**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **Verwendete Selenium-APIs**:
     - `WebDriver.find_element_by_css_selector(css)` (veraltet; modern: `find_element(By.CSS_SELECTOR, css)`): Findet ein einzelnes HTML-Element unter Verwendung eines CSS-Selektors (z. B. nach Attribut wie `name="username"`). Gibt ein `WebElement` zurück.
     - `WebElement.send_keys(text)`: Simuliert die Eingabe in ein Eingabefeld (z. B. Benutzername/Passwort).
     - `WebElement.click()`: Simuliert einen Mausklick auf einen Button oder Link.
   - **Wie Selenium verwendet wird**: Automatisiert das Absenden des Formulars. Ohne Selenium müsste man POST-Anfragen reverse-engineeren, aber dies behandelt JavaScript-Validierung oder dynamische Formulare nahtlos. Anmeldedaten sind hartkodiert (unsicher in der Produktion – Umgebungsvariablen verwenden).

   Nach der Anmeldung:
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - Ruft eine benutzerdefinierte `wait_element`-Funktion auf (siehe unten), um anzuhalten, bis das Dashboard geladen ist.

#### 3. **Navigation und Suche**
   ```python
   trade_div = browser.find_element_by_css_selector('div.dsh_01')
   trade_div.click()
   wait_element(browser, 'a.teq_icon')
   teq = browser.find_element_by_css_selector('a.teq_icon')
   teq.click()
   wait_element(browser, 'div.panel-body')
   iframe = browser.find_element_by_css_selector('div.panel-body > iframe')
   iframe_id = iframe.get_attribute('id')
   browser.switch_to.frame(iframe_id)
   ```
   - **Verwendete Selenium-APIs**:
     - `find_element_by_css_selector`: Findet Navigationselemente (z. B. Dashboard-Div, Icon-Link).
     - `WebElement.click()`: Klickt, um zu navigieren (z. B. zu einem "Handels"-Bereich).
     - `WebElement.get_attribute('id')`: Ruft ein HTML-Attribut ab (hier die ID des Iframes).
     - `WebDriver.switch_to.frame(frame_id)`: Wechselt den Driver-Kontext zu einem `<iframe>` (üblich in Apps zum Einbetten von Inhalten). Ohne dies sind Elemente innerhalb des Iframes unzugänglich.
   - **Wie Selenium verwendet wird**: Behandelt mehrstufige Navigation und eingebettete Inhalte. Iframes isolieren DOMs, daher ist das Wechseln für das Scraping innerer Seiten unerlässlich.

   Suchprozess:
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # Verwendet ID-Locator.
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **Verwendete Selenium-APIs**:
     - `find_element_by_id(id)` (veraltet; modern: `find_element(By.ID, id)`): Findet anhand des HTML-`id`-Attributs.
     - `send_keys`: Tippt die Suchanfrage (HS-Code für Produkte).
     - `time.sleep(10)`: Impliziter Wait (primitiv; besser explizite Waits verwenden).
     - `click()`: Sendet die Suche ab.
   - **Wie Selenium verwendet wird**: Simuliert die Benutzersuche. Das `time.sleep` pausiert, damit AJAX/JavaScript Ergebnisse laden kann.

#### 4. **Paginierung und Verarbeitung der Ergebnisse**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # Berechnet die Gesamtseitenanzahl (20 Ergebnisse/Seite).
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # Mehrere Elemente.
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # JavaScript-Scrollen.
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # Tastatur-Scrollen.
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (mehr unten)
   ```
   - **Verwendete Selenium-APIs**:
     - `find_element_by_css_selector`: Ruft die Ergebnisanzahl aus einem Span-Element ab.
     - `WebElement.text`: Extrahiert sichtbaren Text aus einem Element (z. B. Anzahl wie "100").
     - `find_elements_by_css_selector` (Plural; veraltet: `find_elements(By.CSS_SELECTOR, ...)`): Findet mehrere Elemente (z. B. Zeilenlinks auf einer Seite). Gibt eine Liste von `WebElement`s zurück.
     - `WebDriver.execute_script(js_code, *args)`: Führt benutzerdefiniertes JavaScript im Browser aus (hier scrollt es ein Element ins Blickfeld, um Klickprobleme zu vermeiden).
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`: Simuliert Tastatur-Scrollen (unter Verwendung der `Keys`-Enum).
     - Exceptions: Fängt Klickfehler ab (z. B. Overlay blockiert Klick) oder stale elements (DOM aktualisiert, referenzierte Elemente ungültig – häufig in dynamischen UIs).
   - **Wie Selenium verwendet wird**: Automatisiert die Paginierung durch Eingabe von Seitenzahlen und Klicken auf "Weiter". Für jede Ergebniszeile (`div.rownumber-bt`) scrollt es, um die Sichtbarkeit sicherzustellen, und klickt dann, um Details in einem neuen Fenster zu öffnen. Dies behandelt lazy-loaded oder Infinite-Scroll-ähnliches Verhalten.

#### 5. **Fenster-/Iframe-Wechsel und Datenextraktion**
   Fortsetzung der Schleife:
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # Wechselt zum neuen Tab/Fenster.
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # Schließt das Detailfenster.
   browser.switch_to.window(browser.window_handles[0])  # Zurück zum Hauptfenster.
   browser.switch_to.frame(iframe_id)  # Zurück zum Iframe-Kontext.
   ```
   - **Verwendete Selenium-APIs**:
     - `WebDriver.window_handles`: Liste der geöffneten Fenster-/Tab-IDs.
     - `WebDriver.switch_to.window(handle)`: Wechselt den Fokus zu einem bestimmten Fenster (Index 0 = Hauptfenster, 1 = neuer Tab, geöffnet durch Klick).
     - `WebDriver.close()`: Schließt das aktuelle Fenster.
   - **Wie Selenium verwendet wird**: Klicks öffnen Details in neuen Tabs, daher wechselt es die Kontexte, um diese abzugreifen, und kehrt dann zurück. Dies ist entscheidend für Multi-Tab-Apps.

#### 6. **Datenextraktion in der `save_page(browser: WebDriver)`-Funktion**
   Dies ist die Kern-Logik des Scrapings:
   ```python
   ts = browser.find_elements_by_css_selector('table')  # Alle Tabellen auf der Seite.
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # TD-Zellen in der ersten Tabelle.
   order_number = tds0[2].text  # Extrahiert Text aus bestimmten Zellen.
   # ... (ähnlich für andere Tabellen: t1, t2, etc.)
   ```
   - **Verwendete Selenium-APIs**:
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (veraltet: `By.TAG_NAME` verwenden): Findet alle `<table>`s und ihre `<td>`-Zellen.
     - `WebElement.text`: Holt Textinhalt aus Zellen (z. B. Auftragsnummer, Importeurname).
     - Benutzerdefinierte `tds_to_text(tds: list[WebElement])`: Verkettet Text aus gepaarten `<td>`s (z. B. Label + Wert).
   - **Wie Selenium verwendet wird**: Parst die DOM-Struktur der Seite (Tabellen mit Auftrags-/Importeur-/Exporteur-Details). Es behandelt variable Tabellenanzahlen (z. B. wenn `len(ts) == 8`, existieren zusätzliche Tabellen). Daten werden dann in SQLite eingefügt (Nicht-Selenium-Teil).

   Bedingte Logik extrahiert Felder wie `order_number`, `importer`, `exporter` usw. basierend auf Tabellenindizes – unter der Annahme eines festen Layouts.

#### 7. **Waits und Fehlerbehandlung (`wait_element`-Funktion)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **Verwendete Selenium-APIs**:
     - `expected_conditions.presence_of_element_located(locator)`: Wartet, bis ein Element im DOM existiert (nicht unbedingt sichtbar).
     - `WebDriverWait(driver, timeout).until(condition)`: Fragt alle 0,5 s bis zu 30 s lang die Bedingung ab.
     - `TimeoutException`: Wird ausgelöst, wenn der Wait fehlschlägt.
   - **Wie Selenium verwendet wird**: Verhindert Race Conditions (z. B. Klicken, bevor die Seite geladen ist). Besser als `time.sleep`, da es elementspezifisch und effizient ist.

#### 8. **Bereinigung**
   ```python
   time.sleep(1000)  # Lange Pause (Debugging?).
   browser.quit()    # Schließt den Browser und beendet die Sitzung.
   ```
   - **Verwendete Selenium-API**: `WebDriver.quit()`: Beendet den Treiber, schließt alle Fenster und gibt Ressourcen frei.

#### Gesamteinordnung von Selenium
- **Automatisierungsablauf**: Selenium startet einen echten Browser, lädt Seiten, interagiert über DOM-Abfragen (Locators wie CSS/ID) und behandelt dynamisches Verhalten (JS-Ausführung, Waits, Wechsel). Es ist ideal für SPAs oder geschützte Seiten mit Sitzungen/Cookies.
- **Stärken hier**: Behandelt Anmeldestatus, Iframes, neue Tabs und Scrollen – Scraping-Tools wie BeautifulSoup/Requests könnten dies allein nicht leisten.
- **Einschränkungen/Probleme im Code**:
  - Veraltete Locators: Für Zukunftssicherheit auf `By` aktualisieren.
  - Hartkodierte Sleeps: Mehr durch Waits ersetzen, um Geschwindigkeit zu erhöhen/Fehleranfälligkeit zu reduzieren.
  - Exceptions: Gute Behandlung, aber bei StaleElement könnte ein Retry versucht werden.
  - Ethik/Rechtlichkeit: Scraping könnte Nutzungsbedingungen verletzen; User-Agent-Header oder Proxies hinzufügen, um Menschen nachzuahmen.
  - Leistung: Läuft headful (sichtbarer Browser); für Produktion auf headless umstellen.
- **Ausführung**: Erfordert ChromeDriver (von der Selenium-Website herunterladen, Chrome-Version anpassen). Selenium via `pip install selenium` installieren.

Wenn Sie Fragen zu bestimmten Teilen, zur Modernisierung des Codes oder zum Debugging haben, lassen Sie es mich wissen!