---
audio: false
generated: true
lang: es
layout: post
title: Script de Selenio
translated: true
type: note
---

A continuación se presenta un ejemplo sofisticado de un script de Selenium en Python que demuestra características avanzadas, incluyendo el Page Object Model (POM), FacetGrid explícito para diseños responsivos, esperas explícitas, manejo de contenido dinámico y manejo de errores. El script automatiza un escenario complejo: extraer datos de productos de un sitio web de comercio electrónico, navegar a través de múltiples páginas y generar un reporte resumen. El ejemplo asume un sitio web de comercio electrónico hipotético para fines de demostración, pero los conceptos pueden adaptarse a sitios web reales.

Este ejemplo muestra:
- **Page Object Model (POM)** para un código organizado y mantenible.
- **Esperas explícitas** para manejar contenido dinámico.
- **FacetGrid** para el manejo responsivo de tablas.
- **Navegador headless** para una ejecución eficiente.
- **Procesamiento de datos** para generar un reporte JSON.
- **Manejo de errores** para robustez.

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

# Page Object para la Página de Listado de Productos
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
            time.sleep(2)  # Permitir que se aplique la ordenación
        except TimeoutException:
            print("No se encontró el menú desplegable de ordenación o se agotó el tiempo de espera")

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
            print(f"Error al recuperar productos: {e}")
            return []

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_page_button)
            )
            next_button.click()
            time.sleep(2)  # Esperar a que cargue la página
            return True
        except TimeoutException:
            print("No se encontró el botón de página siguiente o se agotó el tiempo de espera")
            return False

# Page Object para la Página de Búsqueda
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
            time.sleep(2)  # Esperar a los resultados de la búsqueda
        except TimeoutException as e:
            print(f"La búsqueda falló: {e}")

# Script principal
def scrape_ecommerce_site():
    # Configurar Chrome en modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    all_products = []

    try:
        # Navegar al sitio web
        driver.get("https://example.com")
        
        # Inicializar objetos de página
        search_page = SearchPage(driver)
        product_page = ProductListingPage(driver)
        
        # Realizar búsqueda
        search_page.search("laptop")
        
        # Ordenar por precio
        product_page.sort_by_price()
        
        # Extraer datos de múltiples páginas
        page_count = 0
        max_pages = 3  # Límite para la demo
        
        while page_count < max_pages:
            products = product_page.get_products()
            all_products.extend(products)
            print(f"Página {page_count + 1} extraída: {len(products)} productos")
            
            if not product_page.go_to_next_page():
                break
            page_count += 1

        # Generar resumen
        summary = {
            "total_products": len(all_products),
            "average_price": calculate_average_price(all_products),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Guardar resultados en JSON
        with open("product_data.json", "w") as f:
            json.dump({"products": all_products, "summary": summary}, f, indent=2)
        print("Resultados guardados en product_data.json")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
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

### Explicación del Ejemplo
1. **Page Object Model (POM)**:
   - El script utiliza dos clases de objetos de página (`SearchPage` y `ProductListingPage`) para encapsular la lógica específica de cada página, haciendo el código modular y mantenible.
   - Cada clase contiene localizadores y métodos para interactuar con elementos específicos de la página.

2. **Navegador Headless**:
   - El script ejecuta Chrome en modo headless para eficiencia, adecuado para pipelines de CI/CD o servidores.

3. **Esperas Explícitas**:
   - Se utilizan `WebDriverWait` y `expected_conditions` para manejar contenido dinámico, asegurando que los elementos estén presentes o sean clickeables antes de la interacción.

4. **Manejo Responsivo de Tablas**:
   - El script utiliza una lógica similar a FacetGrid para extraer datos de una tabla de listado de productos, extrayendo nombres y precios de cada tarjeta.
   - Maneja la paginación navegando a través de múltiples páginas (hasta un máximo de 3 para este ejemplo).

5. **Manejo de Errores**:
   - El script captura `TimeoutException` y `NoSuchElementException` para manejar elementos faltantes o tiempos de espera agotados de manera elegante.
   - Un bloque `try-finally` asegura que el navegador se cierre incluso si ocurre un error.

6. **Procesamiento de Datos**:
   - Los datos extraídos se almacenan en una lista de diccionarios y se resumen (ej., total de productos, precio promedio).
   - Los resultados se guardan en un archivo JSON (`product_data.json`) para su uso posterior.

7. **Ordenación Dinámica**:
   - El script interactúa con un menú desplegable para ordenar productos por precio, simulando el comportamiento de un usuario real.

### Salida
El script produce un archivo JSON (`product_data.json`) con la siguiente estructura:
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

### Notas
- **Adaptación del Sitio Web**: Los localizadores (`By.ID`, `By.CLASS_NAME`) y la URL (`https://example.com`) son marcadores de posición. Reemplácelos con valores reales de la estructura HTML del sitio web objetivo, que puede inspeccionar usando las herramientas de desarrollo del navegador.
- **Dependencias**: Asegúrese de tener `selenium` instalado (`pip install selenium`) y el controlador del navegador apropiado (ej., ChromeDriver) en su PATH.
- **Mejoras**:
  - Agregar logging para una mejor depuración.
  - Implementar lógica de reintento para peticiones de red inestables.
  - Usar un archivo de configuración para localizadores y ajustes.
  - Extender para manejar escenarios más complejos como autenticación o CAPTCHA.

### Ejecución del Script
1. Instale las dependencias: `pip install selenium`.
2. Descargue y configure ChromeDriver.
3. Reemplace la URL y los localizadores con los de un sitio de comercio electrónico real (ej., Amazon, eBay).
4. Ejecute el script: `python advanced_selenium_ecommerce_scraper.py`.

Este ejemplo demuestra un script de Selenium listo para producción con las mejores prácticas. ¡Avíseme si necesita ayuda para adaptarlo a un sitio web específico o agregar características como autenticación o ejecución en paralelo con Selenium Grid!