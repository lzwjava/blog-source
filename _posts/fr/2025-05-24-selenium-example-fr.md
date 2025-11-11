---
audio: false
generated: true
lang: fr
layout: post
title: Script Selenium
translated: true
type: note
---

Voici un exemple sophistiqué de script Selenium en Python qui démontre des fonctionnalités avancées, incluant le Page Object Model (POM), FacetGrid explicite pour les mises en page responsives, les attentes explicites, la gestion de contenu dynamique et la gestion d'erreurs. Le script automatise un scénario complexe : extraire des données produits d'un site e-commerce, naviguer à travers plusieurs pages et générer un rapport récapitulatif. L'exemple suppose un site e-commerce hypothétique à des fins de démonstration, mais les concepts peuvent être adaptés à de vrais sites web.

Cet exemple met en avant :
- **Le Page Object Model (POM)** pour un code organisé et maintenable.
- **Les attentes explicites** pour gérer le contenu dynamique.
- **FacetGrid** pour la gestion de tableaux responsifs.
- **Le navigateur headless** pour une exécution efficace.
- **Le traitement des données** pour générer un rapport JSON.
- **La gestion d'erreurs** pour la robustesse.

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

# Page Object pour la Page de Liste de Produits
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
            time.sleep(2)  # Laisser le temps au tri de s'appliquer
        except TimeoutException:
            print("Liste déroulante de tri non trouvée ou délai d'attente dépassé")

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
            print(f"Erreur lors de la récupération des produits : {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # Attendre le chargement de la page
            return True
        except TimeoutException:
            print("Bouton page suivante non trouvé ou délai d'attente dépassé")
            return False

# Page Object pour la Page de Recherche
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
            time.sleep(2)  # Attendre les résultats de la recherche
        except TimeoutException as e:
            print(f"Échec de la recherche : {e}")

# Script principal
def scrape_ecommerce_site():
    # Configurer Chrome en mode headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # Naviguer vers le site web
        driver.get("https://example.com")
        
        # Initialiser les objets page
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # Effectuer une recherche
        search_page.search("laptop")
        
        # Trier par prix
        product_page.sort_by_price()
        
        # Extraire les données de plusieurs pages
        page_count = 0
        max_pages = 3  # Limite pour la démo
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"Page {page_count + 1 scrapée : {len(products)} produits")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # Générer le résumé
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Sauvegarder les résultats en JSON
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("Résultats sauvegardés dans product_data.json")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    
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

### Explication de l'exemple
1. **Page Object Model (POM)** :
   - Le script utilise deux classes d'objets page (`SearchPage` et `ProductListingPage`) pour encapsuler la logique spécifique à chaque page, rendant le code modulaire et maintenable.
   - Chaque classe contient des localisateurs et des méthodes pour interagir avec des éléments spécifiques de la page.

2. **Navigateur Headless** :
   - Le script exécute Chrome en mode headless pour l'efficacité, adapté aux pipelines CI/CD ou aux serveurs.

3. **Attentes Explicites** :
   - `WebDriverWait` et `expected_conditions` sont utilisés pour gérer le contenu dynamique, en s'assurant que les éléments sont présents ou cliquables avant l'interaction.

4. **Gestion de Tableau Responsif** :
   - Le script utilise une logique similaire à FacetGrid pour extraire les données d'un tableau de liste de produits, extrayant les noms et prix de chaque carte produit.
   - Il gère la pagination en naviguant à travers plusieurs pages (jusqu'à un maximum de 3 pour cet exemple).

5. **Gestion des Erreurs** :
   - Le script intercepte `TimeoutException` et `NoSuchElementException` pour gérer les éléments manquants ou les délais dépassés de manière élégante.
   - Un bloc `try-finally` garantit que le navigateur est fermé même si une erreur se produit.

6. **Traitement des Données** :
   - Les données extraites sont stockées dans une liste de dictionnaires et résumées (ex: total des produits, prix moyen).
   - Les résultats sont sauvegardés dans un fichier JSON (`product_data.json`) pour une utilisation ultérieure.

7. **Tri Dynamique** :
   - Le script interagit avec une liste déroulante pour trier les produits par prix, simulant le comportement d'un utilisateur réel.

### Sortie
Le script produit un fichier JSON (`product_data.json`) avec la structure suivante :
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

### Notes
- **Adaptation au Site Web** : Les localisateurs (`By.ID`, `By.CLASS_NAME`) et l'URL (`https://example.com`) sont des espaces réservés. Remplacez-les par les valeurs réelles provenant de la structure HTML du site web cible, que vous pouvez inspecter en utilisant les outils de développement du navigateur.
- **Dépendances** : Assurez-vous d'avoir `selenium` installé (`pip install selenium`) et le pilote de navigateur approprié (ex: ChromeDriver) dans votre PATH.
- **Améliorations Possibles** :
  - Ajouter des journaux (logs) pour un meilleur débogage.
  - Implémenter une logique de nouvelle tentative pour les requêtes réseau intermittentes.
  - Utiliser un fichier de configuration pour les localisateurs et les paramètres.
  - Étendre pour gérer des scénarios plus complexes comme l'authentification ou les CAPTCHA.

### Exécution du Script
1. Installer les dépendances : `pip install selenium`.
2. Télécharger et configurer ChromeDriver.
3. Remplacer l'URL et les localisateurs par ceux d'un vrai site e-commerce (ex: Amazon, eBay).
4. Exécuter le script : `python advanced_selenium_ecommerce_scraper.py`.

Cet exemple démontre un script Selenium prêt pour la production suivant les bonnes pratiques. Faites-moi savoir si vous avez besoin d'aide pour l'adapter à un site web spécifique ou pour ajouter des fonctionnalités comme l'authentification ou l'exécution parallèle avec Selenium Grid !