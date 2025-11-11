---
audio: false
generated: true
lang: de
layout: post
title: Selenium-Skript
translated: true
type: note
---

Hier folgt ein anspruchvolles Beispiel eines Selenium-Skripts in Python, das fortgeschrittene Funktionen demonstriert, darunter das Page Object Model (POM), explizite FacetGrid für responsive Layouts, explizite Waits, die Handhabung dynamischer Inhalte und Fehlerbehandlung. Das Skript automatisiert ein komplexes Szenario: Das Scraping von Produktdaten von einer E-Commerce-Website, das Navigieren durch mehrere Seiten und das Erstellen eines Zusammenfassungsberichts. Das Beispiel nimmt zu Demonstrationszwecken eine hypothetische E-Commerce-Website an, aber die Konzepte können an echte Websites angepasst werden.

Dieses Beispiel zeigt:
- **Page Object Model (POM)** für organisierten und wartbaren Code.
- **Explizite Waits** für die Handhabung dynamischer Inhalte.
- **FacetGrid** für die Handhabung responsiver Tabellen.
- **Headless-Browser** für eine effiziente Ausführung.
- **Datenverarbeitung** zur Erstellung eines JSON-Berichts.
- **Fehlerbehandlung** für Robustheit.

```python
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

# Page Object für die Produktlistenseite
class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.CLASS_NAME, "product-card")
        self.product_name = (By.CLASS_NAME, "product-name")
        self.product_price = (By.CLASS_NAME, "product-price")
        self.next_page_button = (By.ID, "next-page")
        self.sort_dropdown = (By.ID, "sort-options")

    def sort_by_price(self):
        try:
            sort_select = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sort_dropdown)
            )
            select = Select(sort_select)
            select.select_by_value("price-asc")
            time.sleep(2)  # Zeit zum Anwenden der Sortierung
        except TimeoutException:
            print("Sortier-Dropdown nicht gefunden oder Timeout")

    def get_products(self):
        try:
            cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            products = []
            for card in cards:
                name = card.find_element(*self.product_name).text
                price = card.find_element(*self.product_price).text
                products.append({"name": name, "price": price})
            return products
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Fehler beim Abrufen der Produkte: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # Warten auf Seitenladung
            return True
        except TimeoutException:
            print("Keine 'Nächste Seite'-Schaltfläche gefunden oder Timeout")
            return False

# Page Object für die Suchseite
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search-bar")
        self.search_button = (By.ID, "search-submit")

    def search(self, query):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.search_input)
            )
            search_box.clear()
            search_box.send_keys(query)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            ).click()
            time.sleep(2)  # Warten auf Suchergebnisse
        except TimeoutException as e:
            print(f"Suche fehlgeschlagen: {e}")

# Hauptskript
def scrape_ecommerce_site():
    # Headless Chrome einrichten
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # Zur Website navigieren
        driver.get("https://example.com")
        
        # Page Objects initialisieren
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # Suche durchführen
        search_page.search("laptop")
        
        # Nach Preis sortieren
        product_page.sort_by_price()
        
        # Mehrere Seiten scrapen
        page_count = 0
        max_pages = 3  # Limit für die Demo
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"Seite {page_count + 1} gescraped: {len(products)} Produkte")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # Zusammenfassung erstellen
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Ergebnisse in JSON speichern
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("Ergebnisse in product_data.json gespeichert")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    
    finally:
        driver.quit()

def calculate_average_price(products):
    if not products:
        return 0
    prices = []
    for product in products:
        try:
            price_str = product["price"].replace("$", "").replace(",", "")
            prices.append(float(price_str))
        except (ValueError, AttributeError):
            continue
    return sum(prices) / len(prices) if prices else 0

if __name__ == "__main__":
    scrape_ecommerce_site()
```

### Erklärung des Beispiels
1. **Page Object Model (POM)**:
   - Das Skript verwendet zwei Page-Object-Klassen (`SearchPage` und `ProductListingPage`), um seiten-spezifische Logik zu kapseln, was den Code modular und wartbar macht.
   - Jede Klasse enthält Locators und Methoden für die Interaktion mit spezifischen Seitenelementen.

2. **Headless-Browser**:
   - Das Skript führt Chrome im Headless-Modus für Effizienz aus, geeignet für CI/CD-Pipelines oder Server.

3. **Explizite Waits**:
   - `WebDriverWait` und `expected_conditions` werden verwendet, um dynamische Inhalte zu handhaben und sicherzustellen, dass Elemente vorhanden oder klickbar sind, bevor interagiert wird.

4. **Handhabung responsiver Tabellen**:
   - Das Skript verwendet eine FacetGrid-ähnliche Logik, um eine Produktlistentabelle zu scrapen, und extrahiert Produktnamen und Preise aus jeder Karte.
   - Es handhabt Paginierung, indem es durch mehrere Seiten navigiert (für dieses Beispiel auf maximal 3 begrenzt).

5. **Fehlerbehandlung**:
   - Das Skript fängt `TimeoutException` und `NoSuchElementException` ab, um fehlende Elemente oder Timeouts elegant zu handhaben.
   - Ein `try-finally`-Block stellt sicher, dass der Browser auch bei einem Fehler geschlossen wird.

6. **Datenverarbeitung**:
   - Gescrapte Daten werden in einer Liste von Dictionaries gespeichert und zusammengefasst (z.B. Gesamtprodukte, Durchschnittspreis).
   - Ergebnisse werden in einer JSON-Datei (`product_data.json`) für die weitere Verwendung gespeichert.

7. **Dynamische Sortierung**:
   - Das Skript interagiert mit einem Dropdown, um Produkte nach Preis zu sortieren, und simuliert so echtes Nutzerverhalten.

### Ausgabe
Das Skript erzeugt eine JSON-Datei (`product_data.json`) mit der folgenden Struktur:
```json
{
  "products": [
    {"name": "Laptop Model A", "price": "$999.99"},
    {"name": "Laptop Model B", "price": "$1299.99"},
    ...
  ],
  "summary": {
    "total_products": 30,
    "average_price": 1099.45,
    "timestamp": "2025-05-24 21:33:00"
  }
}
```

### Hinweise
- **Website-Anpassung**: Die Locators (`By.ID`, `By.CLASS_NAME`) und die URL (`https://example.com`) sind Platzhalter. Ersetzen Sie diese durch tatsächliche Werte aus der HTML-Struktur der Zielwebsite, die Sie mit Browser-Entwicklertools inspizieren können.
- **Abhängigkeiten**: Stellen Sie sicher, dass `selenium` installiert ist (`pip install selenium`) und der entsprechende Browser-Treiber (z.B. ChromeDriver) in Ihrem PATH vorhanden ist.
- **Verbesserungen**:
  - Fügen Sie Logging für besseres Debugging hinzu.
  - Implementieren Sie Wiederholungslogik für flaky Netzwerkanfragen.
  - Verwenden Sie eine Konfigurationsdatei für Locators und Einstellungen.
  - Erweitern Sie das Skript, um komplexere Szenarien wie Authentifizierung oder CAPTCHA zu handhaben.

### Ausführen des Skripts
1. Installieren Sie die Abhängigkeiten: `pip install selenium`.
2. Laden Sie ChromeDriver herunter und konfigurieren Sie es.
3. Ersetzen Sie die URL und die Locators durch die einer echten E-Commerce-Website (z.B. Amazon, eBay).
4. Führen Sie das Skript aus: `python advanced_selenium_ecommerce_scraper.py`.

Dieses Beispiel demonstriert ein produktionsreifes Selenium-Skript mit Best Practices. Lassen Sie mich wissen, wenn Sie Hilfe bei der Anpassung an eine bestimmte Website oder beim Hinzufügen von Funktionen wie Authentifizierung oder paralleler Ausführung mit Selenium Grid benötigen!