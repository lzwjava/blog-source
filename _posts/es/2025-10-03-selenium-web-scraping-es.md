---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Explicación del Código de Web Scraping con Selenium
translated: true
type: note
---

### Explicación del Uso de la API de Selenium en el Código Proporcionado

Este script de Python utiliza la biblioteca **Selenium WebDriver** para automatizar un navegador web (específicamente Chrome) e interactuar con un sitio web (probablemente un portal de datos/comercio en `https://xxdata.com/index.aspx`). El objetivo parece ser la extracción web (web scraping): iniciar sesión, buscar datos de comercio/pedidos (usando un código HS como '8449'), navegar por los resultados paginados, hacer clic en los detalles, extraer datos estructurados de tablas HTML y almacenarlos en una base de datos SQLite (`data.db`).

Selenium se utiliza aquí para la **automatización del navegador**, permitiendo que el script imite interacciones humanas como escribir, hacer clic, desplazarse y esperar a que las páginas se carguen, algo que es difícil o imposible con simples solicitudes HTTP (por ejemplo, debido a páginas con mucho JavaScript, iframes o contenido dinámico). Maneja elementos web dinámicos, sesiones y el cambio entre ventanas/iframes, que son comunes en las aplicaciones web modernas.

Lo desglosaré **sección por sección**, destacando las API clave de Selenium, su propósito y cómo se utilizan. Nota: Algunos métodos en el código (por ejemplo, `find_element_by_css_selector`) son de versiones antiguas de Selenium (anteriores a la 4.0) y están obsoletos. En Selenium moderno (4+), se usaría `find_element(By.CSS_SELECTOR, ...)` en su lugar, pero la funcionalidad es la misma. El script también importa los módulos necesarios para las esperas, excepciones y el manejo de elementos.

#### 1. **Importaciones y Configuración (Inicialización de Selenium)**
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
   - **Propósito**: Estas importaciones son componentes principales de Selenium:
     - `webdriver`: Módulo principal para controlar el navegador.
     - `WebDriver`: Sugerencia de tipo para la instancia del navegador (asegura la seguridad de tipos).
     - `Keys`: Para simular entradas del teclado (por ejemplo, Avance de Página).
     - Excepciones: Manejan errores comunes como tiempos de espera agotados o elementos obsoletos (elementos que cambian después de una actualización de página).
     - `WebDriverWait` y `EC` (Condiciones Esperadas): Para esperas explícitas—sondeando hasta que un elemento cumple una condición (por ejemplo, está presente en la página).
     - `By`: Estrategias de localización (por ejemplo, selector CSS, ID, nombre de etiqueta) para encontrar elementos.
     - `WebElement`: Representa elementos HTML para la interacción.

   En la función `run()`:
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # Abre el navegador en pantalla completa.
   options.add_argument('--log-level=3')      # Suprime los registros de la consola para una salida más limpia.
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **API de Selenium Utilizada**: `webdriver.Chrome(options=...)`
     - Inicializa una instancia del navegador Chrome usando un ejecutable local `chromedriver` (debe estar en el directorio del script).
     - `ChromeOptions`: Personaliza la sesión del navegador (por ejemplo, se podría agregar el modo sin cabeza con `options.add_argument("--headless")` para ejecución en segundo plano).
     - Esto crea una ventana de navegador en vivo y controlable. Selenium actúa como un puente entre Python y el protocolo DevTools del navegador.

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **API de Selenium Utilizada**: `WebDriver.get(url)`
     - Navega a la URL de inicio, cargando la página como un usuario que la escribe en la barra de direcciones.

#### 2. **Proceso de Inicio de Sesión**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **APIs de Selenium Utilizadas**:
     - `WebDriver.find_element_by_css_selector(css)` (obsoleto; moderno: `find_element(By.CSS_SELECTOR, css)`): Localiza un único elemento HTML usando un selector CSS (por ejemplo, por atributo como `name="username"`). Retorna un `WebElement`.
     - `WebElement.send_keys(text)`: Simula escribir en un campo de entrada (por ejemplo, nombre de usuario/contraseña).
     - `WebElement.click()`: Simula un clic del ratón en un botón o enlace.
   - **Cómo se Usa Selenium**: Automatiza el envío de formularios. Sin Selenium, necesitarías revertir las solicitudes POST, pero esto maneja la validación JavaScript o los formularios dinámicos sin problemas. Las credenciales están codificadas (inseguro en producción—usar variables de entorno).

   Después del inicio de sesión:
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - Llama a una función personalizada `wait_element` (explicada abajo) para pausar hasta que el panel de control se cargue.

#### 3. **Navegación y Búsqueda**
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
   - **APIs de Selenium Utilizadas**:
     - `find_element_by_css_selector`: Localiza elementos de navegación (por ejemplo, div del panel de control, enlace del icono).
     - `WebElement.click()`: Hace clic para navegar (por ejemplo, a una sección de "comercio").
     - `WebElement.get_attribute('id')`: Recupera un atributo HTML (aquí, el ID del iframe).
     - `WebDriver.switch_to.frame(frame_id)`: Cambia el contexto del controlador a un `<iframe>` (común en aplicaciones para incrustar contenido). Sin esto, los elementos dentro del iframe son inaccesibles.
   - **Cómo se Usa Selenium**: Maneja la navegación de múltiples pasos y el contenido incrustado. Los Iframes aíslan los DOM, por lo que cambiar el contexto es esencial para extraer páginas internas.

   Proceso de búsqueda:
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # Usa el localizador por ID.
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **APIs de Selenium Utilizadas**:
     - `find_element_by_id(id)` (obsoleto; moderno: `find_element(By.ID, id)`): Localiza por el atributo HTML `id`.
     - `send_keys`: Escribe la consulta de búsqueda (código HS para productos).
     - `time.sleep(10)`: Espera implícita (cruda; es mejor usar esperas explícitas).
     - `click()`: Envía la búsqueda.
   - **Cómo se Usa Selenium**: Simula la búsqueda del usuario. El `time.sleep` pausa para que AJAX/JavaScript cargue los resultados.

#### 4. **Paginación y Procesamiento de Resultados**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # Calcula el total de páginas (20 resultados/página).
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # Múltiples elementos.
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # Desplazamiento JavaScript.
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # Desplazamiento con teclado.
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (más abajo)
   ```
   - **APIs de Selenium Utilizadas**:
     - `find_element_by_css_selector`: Obtiene el recuento de resultados de un span.
     - `WebElement.text`: Extrae el texto visible de un elemento (por ejemplo, un recuento como "100").
     - `find_elements_by_css_selector` (plural; obsoleto: `find_elements(By.CSS_SELECTOR, ...)`): Encuentra múltiples elementos (por ejemplo, enlaces de fila en una página). Retorna una lista de `WebElement`s.
     - `WebDriver.execute_script(js_code, *args)`: Ejecuta JavaScript personalizado en el navegador (aquí, desplaza un elemento a la vista para evitar problemas de clic).
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)`: Simula el desplazamiento con el teclado (usando la enumeración `Keys`).
     - Excepciones: Captura fallos de clic (por ejemplo, una superposición bloquea el clic) o elementos obsoletos (el DOM se actualizó, invalidando las referencias—común en UIs dinámicas).
   - **Cómo se Usa Selenium**: Automatiza la paginación escribiendo números de página y haciendo clic en "ir". Para cada fila de resultados (`div.rownumber-bt`), se desplaza para asegurar la visibilidad, luego hace clic para abrir los detalles en una nueva ventana. Esto maneja comportamientos similares a la carga diferida o al desplazamiento infinito.

#### 5. **Cambio de Ventana/Iframe y Extracción de Datos**
   Continuando desde el bucle:
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # Cambiar a la nueva pestaña/ventana.
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # Cierra la ventana de detalles.
   browser.switch_to.window(browser.window_handles[0])  # Vuelve a la ventana principal.
   browser.switch_to.frame(iframe_id)  # Vuelve al contexto del iframe.
   ```
   - **APIs de Selenium Utilizadas**:
     - `WebDriver.window_handles`: Lista de IDs de ventanas/pestañas abiertas.
     - `WebDriver.switch_to.window(handle)`: Cambia el enfoque a una ventana específica (índice 0 = principal, 1 = nueva pestaña abierta por el clic).
     - `WebDriver.close()`: Cierra la ventana actual.
   - **Cómo se Usa Selenium**: Los clics abren detalles en nuevas pestañas, por lo que cambia de contexto para extraerlos, luego regresa. Esto es crucial para aplicaciones de múltiples pestañas.

#### 6. **Extracción de Datos en la Función `save_page(browser: WebDriver)`**
   Esta es la lógica central de extracción:
   ```python
   ts = browser.find_elements_by_css_selector('table')  # Todas las tablas en la página.
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # Celdas TD en la primera tabla.
   order_number = tds0[2].text  # Extrae texto de celdas específicas.
   # ... (similar para otras tablas: t1, t2, etc.)
   ```
   - **APIs de Selenium Utilizadas**:
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (obsoleto: usar `By.TAG_NAME`): Encuentra todas las `<table>`s y sus celdas `<td>`.
     - `WebElement.text`: Extrae el contenido de texto de las celdas (por ejemplo, número de pedido, nombre del importador).
     - Personalizada `tds_to_text(tds: list[WebElement])`: Concatena texto de `<td>`s emparejadas (por ejemplo, etiqueta + valor).
   - **Cómo se Usa Selenium**: Analiza la estructura DOM de la página (tablas con detalles de pedido/importador/exportador). Maneja recuentos variables de tablas (por ejemplo, si `len(ts) == 8`, existen tablas extra). Los datos se insertan luego en SQLite (parte no relacionada con Selenium).

   La lógica condicional extrae campos como `order_number`, `importer`, `exporter`, etc., basándose en índices de tabla—asumiendo un diseño fijo.

#### 7. **Esperas y Manejo de Errores (Función `wait_element`)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **APIs de Selenium Utilizadas**:
     - `expected_conditions.presence_of_element_located(locator)`: Espera a que un elemento exista en el DOM (no necesariamente visible).
     - `WebDriverWait(driver, timeout).until(condition)`: Sondea cada 0.5s hasta 30s para la condición.
     - `TimeoutException`: Se genera si la espera falla.
   - **Cómo se Usa Selenium**: Previene condiciones de carrera (por ejemplo, hacer clic antes de que la página se cargue). Mejor que `time.sleep` ya que es específico para el elemento y eficiente.

#### 8. **Limpieza**
   ```python
   time.sleep(1000)  # Pausa larga (¿depuración?).
   browser.quit()    # Cierra el navegador y termina la sesión.
   ```
   - **API de Selenium Utilizada**: `WebDriver.quit()`: Termina el controlador, cierra todas las ventanas y libera recursos.

#### Cómo se Integra Selenium en General
- **Flujo de Automatización**: Selenium inicia un navegador real, carga páginas, interactúa mediante consultas DOM (localizadores como CSS/ID) y maneja comportamientos dinámicos (ejecución JS, esperas, cambios). Es ideal para SPAs o sitios protegidos con sesiones/cookies.
- **Fortalezas Aquí**: Maneja el estado de inicio de sesión, iframes, nuevas pestañas y desplazamiento—herramientas de scraping como BeautifulSoup/Requests no podrían hacer esto por sí solas.
- **Limitaciones/Problemas en el Código**:
  - Localizadores obsoletos: Actualizar a `By` para ser compatible con el futuro.
  - Esperas codificadas: Reemplazar más con esperas para acelerar/reducir la fragilidad.
  - Excepciones: Buen manejo, pero podría reintentar en StaleElement.
  - Ética/Legalidad: La extracción puede violar los términos; agregar cabeceras de user-agent o proxies para imitar humanos.
  - Rendimiento: Se ejecuta con interfaz visible (navegador con ventana); hacerlo sin cabeza (headless) para producción.
- **Ejecutarlo**: Requiere ChromeDriver (descargar del sitio de Selenium, que coincida con la versión de Chrome). Instalar Selenium via `pip install selenium`.

Si tienes preguntas sobre partes específicas, modernizar el código o depurar, ¡avísame