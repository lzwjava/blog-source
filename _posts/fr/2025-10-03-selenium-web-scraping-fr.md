---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Explication du Code de Web Scraping avec Selenium
translated: true
type: note
---

### Explication de l'utilisation de l'API Selenium dans le code fourni

Ce script Python utilise la bibliothèque **Selenium WebDriver** pour automatiser un navigateur web (spécifiquement Chrome) afin d'interagir avec un site web (probablement un portail de données/commerce à l'adresse `https://xxdata.com/index.aspx`). L'objectif semble être le web scraping : se connecter, rechercher des données de commerce/commandes (en utilisant un code HS comme '8449'), naviguer dans les résultats paginés, cliquer sur les détails, extraire des données structurées à partir de tableaux HTML et les stocker dans une base de données SQLite (`data.db`).

Selenium est utilisé ici pour **l'automatisation du navigateur**, permettant au script d'imiter les interactions humaines comme la frappe, les clics, le défilement et l'attente du chargement des pages—quelque chose de difficile ou impossible avec de simples requêtes HTTP (par exemple, à cause de pages lourdes en JavaScript, d'iframes ou de contenu dynamique). Il gère les éléments web dynamiques, les sessions et la commutation entre multiples fenêtres/iframes, ce qui est courant dans les applications web modernes.

Je vais le décomposer **section par section**, en mettant en évidence les API clés de Selenium, leur objectif et leur utilisation. Note : Certaines méthodes dans le code (par exemple, `find_element_by_css_selector`) proviennent d'anciennes versions de Selenium (antérieures à la 4.0) et sont obsolètes. Dans Selenium moderne (4+), vous utiliseriez `find_element(By.CSS_SELECTOR, ...)` à la place, mais la fonctionnalité est la même. Le script importe également les modules nécessaires pour les attentes, les exceptions et la gestion des éléments.

#### 1. **Imports et Configuration (Initialisation de Selenium)**
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
   - **Objectif** : Ces imports incluent les composants principaux de Selenium :
     - `webdriver` : Module principal pour contrôler le navigateur.
     - `WebDriver` : Indication de type pour l'instance du navigateur (assure la sécurité de type).
     - `Keys` : Pour simuler les entrées clavier (par exemple, Page Up).
     - Exceptions : Gèrent les erreurs courantes comme les timeouts ou les éléments obsolètes (éléments qui changent après un rafraîchissement de page).
     - `WebDriverWait` et `EC` (Conditions Attendues) : Pour les attentes explicites—interrogation jusqu'à ce qu'un élément remplisse une condition (par exemple, présent sur la page).
     - `By` : Stratégies de localisation (par exemple, sélecteur CSS, ID, nom de balise) pour trouver des éléments.
     - `WebElement` : Représente les éléments HTML pour l'interaction.

   Dans la fonction `run()` :
   ```python
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")  # Ouvre le navigateur en plein écran.
   options.add_argument('--log-level=3')      # Supprime les logs de la console pour une sortie plus propre.
   browser: WebDriver = webdriver.Chrome(executable_path="./chromedriver", options=options)
   ```
   - **API Selenium Utilisée** : `webdriver.Chrome(options=...)`
     - Initialise une instance du navigateur Chrome en utilisant un exécutable `chromedriver` local (doit être dans le répertoire du script).
     - `ChromeOptions` : Personnalise la session du navigateur (par exemple, le mode headless pourrait être ajouté avec `options.add_argument("--headless")` pour une exécution en arrière-plan).
     - Cela crée une fenêtre de navigateur vivante et contrôlable. Selenium agit comme un pont entre Python et le protocole DevTools du navigateur.

   ```python
   browser.get('https://xxdata.com/index.aspx')
   ```
   - **API Selenium Utilisée** : `WebDriver.get(url)`
     - Navigue vers l'URL de départ, chargeant la page comme un utilisateur la tapant dans la barre d'adresse.

#### 2. **Processus de Connexion**
   ```python
   input_username = browser.find_element_by_css_selector('input[name=username]')
   input_username.send_keys('name')
   input_password = browser.find_element_by_css_selector('input[name=password]')
   input_password.send_keys('password')
   btn_login = browser.find_element_by_css_selector('div.login-check')
   btn_login.click()
   ```
   - **API Selenium Utilisées** :
     - `WebDriver.find_element_by_css_selector(css)` (obsolète ; moderne : `find_element(By.CSS_SELECTOR, css)`) : Localise un seul élément HTML en utilisant un sélecteur CSS (par exemple, par attribut comme `name="username"`). Retourne un `WebElement`.
     - `WebElement.send_keys(text)` : Simule la frappe dans un champ de saisie (par exemple, nom d'utilisateur/mot de passe).
     - `WebElement.click()` : Simule un clic de souris sur un bouton ou un lien.
   - **Comment Selenium est Utilisé** : Automatise la soumission de formulaire. Sans Selenium, vous devriez rétro-concevoir les requêtes POST, mais cela gère la validation JavaScript ou les formulaires dynamiques de manière transparente. Les identifiants sont codés en dur (non sécurisé en production—utilisez des variables d'environnement).

   Après la connexion :
   ```python
   wait_element(browser, 'div.dsh_01')
   ```
   - Appelle une fonction personnalisée `wait_element` (expliquée ci-dessous) pour faire une pause jusqu'au chargement du tableau de bord.

#### 3. **Navigation et Recherche**
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
   - **API Selenium Utilisées** :
     - `find_element_by_css_selector` : Localise les éléments de navigation (par exemple, div du tableau de bord, lien d'icône).
     - `WebElement.click()` : Clique pour naviguer (par exemple, vers une section "commerce").
     - `WebElement.get_attribute('id')` : Récupère un attribut HTML (ici, l'ID de l'iframe).
     - `WebDriver.switch_to.frame(frame_id)` : Bascule le contexte du pilote vers une `<iframe>` (courant dans les applications pour intégrer du contenu). Sans cela, les éléments à l'intérieur de l'iframe sont inaccessibles.
   - **Comment Selenium est Utilisé** : Gère la navigation en plusieurs étapes et le contenu intégré. Les iframes isolent les DOM, donc la commutation est essentielle pour le scraping des pages internes.

   Processus de recherche :
   ```python
   input_search = browser.find_element_by_id('_easyui_textbox_input7')  # Utilise le localisateur ID.
   input_search.send_keys('8449')
   time.sleep(10)
   enter = browser.find_element_by_css_selector('a#btnOk > div.enter-bt')
   enter.click()
   ```
   - **API Selenium Utilisées** :
     - `find_element_by_id(id)` (obsolète ; moderne : `find_element(By.ID, id)`) : Localise par l'attribut HTML `id`.
     - `send_keys` : Tape la requête de recherche (code HS pour les produits).
     - `time.sleep(10)` : Attente implicite (rudimentaire ; mieux vaut utiliser des attentes explicites).
     - `click()` : Soumet la recherche.
   - **Comment Selenium est Utilisé** : Simule la recherche utilisateur. Le `time.sleep` fait une pause pour le chargement AJAX/JavaScript des résultats.

#### 4. **Pagination et Traitement des Résultats**
   ```python
   result_count_span = browser.find_element_by_css_selector('span#ResultCount')
   page = math.ceil(int(result_count_span.text) / 20)  # Calcule le nombre total de pages (20 résultats/page).
   skip = 0
   page = page - skip

   for p in range(page):
       input_page = browser.find_element_by_css_selector('input.laypage_skip')
       input_page.send_keys(str(p + skip + 1))
       btn_confirm = browser.find_element_by_css_selector('button.laypage_btn')
       btn_confirm.click()
       time.sleep(2)

       locates = browser.find_elements_by_css_selector('div.rownumber-bt')  # Éléments multiples.
       print('page ' + str(p) + ' size: ' + str(len(locates)))
       for locate in locates:
           browser.execute_script("arguments[0].scrollIntoView();", locate)  # Défilement JavaScript.
           time.sleep(1)
           browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)  # Défilement clavier.
           time.sleep(1)
           try:
               locate.click()
           except ElementClickInterceptedException:
               print('ElementClickInterceptedException')
               continue
           except StaleElementReferenceException:
               print('StaleElementReferenceException')
               continue
           # ... (suite ci-dessous)
   ```
   - **API Selenium Utilisées** :
     - `find_element_by_css_selector` : Obtient le nombre de résultats à partir d'un span.
     - `WebElement.text` : Extrait le texte visible d'un élément (par exemple, le compte comme "100").
     - `find_elements_by_css_selector` (pluriel ; obsolète : `find_elements(By.CSS_SELECTOR, ...)`) : Trouve plusieurs éléments (par exemple, les liens de ligne sur une page). Retourne une liste de `WebElement`s.
     - `WebDriver.execute_script(js_code, *args)` : Exécute du JavaScript personnalisé dans le navigateur (ici, fait défiler un élément dans la vue pour éviter les problèmes de clic).
     - `WebDriver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)` : Simule le défilement au clavier (en utilisant l'énumération `Keys`).
     - Exceptions : Attrape les échecs de clic (par exemple, une superposition bloque le clic) ou les éléments obsolètes (DOM rafraîchi, invalidant les références—courant dans les UI dynamiques).
   - **Comment Selenium est Utilisé** : Automatise la pagination en tapant les numéros de page et en cliquant sur "aller". Pour chaque ligne de résultat (`div.rownumber-bt`), il défile pour assurer la visibilité, puis clique pour ouvrir les détails dans une nouvelle fenêtre. Cela gère le comportement de type chargement paresseux ou défilement infini.

#### 5. **Commutation de Fenêtre/Iframe et Extraction des Données**
   Suite de la boucle :
   ```python
   time.sleep(1)
   browser.switch_to.window(browser.window_handles[1])  # Bascule vers le nouvel onglet/fenêtre.
   wait_element(browser, 'div#content')
   try:
       save_page(browser)
   except IndexError:
       print('IndexError')
       continue
   browser.close()  # Ferme la fenêtre de détail.
   browser.switch_to.window(browser.window_handles[0])  # Retour à la fenêtre principale.
   browser.switch_to.frame(iframe_id)  # Retour au contexte de l'iframe.
   ```
   - **API Selenium Utilisées** :
     - `WebDriver.window_handles` : Liste des ID des fenêtres/onglets ouverts.
     - `WebDriver.switch_to.window(handle)` : Bascule le focus vers une fenêtre spécifique (index 0 = principale, 1 = nouvel onglet ouvert par le clic).
     - `WebDriver.close()` : Ferme la fenêtre courante.
   - **Comment Selenium est Utilisé** : Les clics ouvrent les détails dans de nouveaux onglets, donc il bascule de contexte pour les scraper, puis revient. Ceci est crucial pour les applications multi-onglets.

#### 6. **Extraction des Données dans la Fonction `save_page(browser: WebDriver)`**
   C'est la logique principale du scraping :
   ```python
   ts = browser.find_elements_by_css_selector('table')  # Tous les tableaux de la page.
   t0 = ts[0]
   tds0 = t0.find_elements_by_tag_name('td')  # Cellules TD dans le premier tableau.
   order_number = tds0[2].text  # Extrait le texte de cellules spécifiques.
   # ... (similaire pour les autres tableaux : t1, t2, etc.)
   ```
   - **API Selenium Utilisées** :
     - `find_elements_by_css_selector('table')` / `find_elements_by_tag_name('td')` (obsolète : utilisez `By.TAG_NAME`) : Trouve tous les `<table>`s et leurs cellules `<td>`.
     - `WebElement.text` : Récupère le contenu textuel des cellules (par exemple, numéro de commande, nom de l'importateur).
     - Personnalisée `tds_to_text(tds: list[WebElement])` : Concatène le texte des `<td>`s appariés (par exemple, étiquette + valeur).
   - **Comment Selenium est Utilisé** : Analyse la structure DOM de la page (tableaux avec les détails de commande/importateur/exportateur). Il gère les nombres variables de tableaux (par exemple, si `len(ts) == 8`, des tableaux supplémentaires existent). Les données sont ensuite insérées dans SQLite (partie non-Selenium).

   La logique conditionnelle extrait des champs comme `order_number`, `importer`, `exporter`, etc., basée sur les indices des tableaux—en supposant une mise en page fixe.

#### 7. **Attentes et Gestion des Erreurs (Fonction `wait_element`)**
   ```python
   def wait_element(browser, css):
       timeout = 30
       try:
           element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
           WebDriverWait(browser, timeout).until(element_present)
       except TimeoutException:
           print('Timed out waiting for page to load')
   ```
   - **API Selenium Utilisées** :
     - `expected_conditions.presence_of_element_located(locator)` : Attend qu'un élément existe dans le DOM (pas nécessairement visible).
     - `WebDriverWait(driver, timeout).until(condition)` : Interroge toutes les 0.5s jusqu'à 30s pour la condition.
     - `TimeoutException` : Levée si l'attente échoue.
   - **Comment Selenium est Utilisé** : Empêche les conditions de course (par exemple, cliquer avant le chargement de la page). Mieux que `time.sleep` car c'est spécifique à l'élément et efficace.

#### 8. **Nettoyage**
   ```python
   time.sleep(1000)  # Longue pause (débogage ?).
   browser.quit()    # Ferme le navigateur et termine la session.
   ```
   - **API Selenium Utilisée** : `WebDriver.quit()` : Termine le pilote, ferme toutes les fenêtres et libère les ressources.

#### Comment Selenium S'Intègre Globalement
- **Flux d'Automatisation** : Selenium lance un vrai navigateur, charge les pages, interagit via des requêtes DOM (localisateurs comme CSS/ID) et gère les comportements dynamiques (exécution JS, attentes, commutations). C'est idéal pour les SPA ou les sites protégés avec sessions/cookies.
- **Points Forts Ici** : Gère l'état de connexion, les iframes, les nouveaux onglets et le défilement—les outils de scraping comme BeautifulSoup/Requests ne pourraient pas faire cela seuls.
- **Limitations/Problèmes dans le Code** :
  - Localisateurs obsolètes : Mettre à jour vers `By` pour une pérennité.
  - Pauses codées en dur : Remplacer davantage par des attentes pour accélérer/réduire la fragilité.
  - Exceptions : Bonne gestion, mais pourrait réessayer sur StaleElement.
  - Éthique/Légalité : Le scraping peut violer les conditions d'utilisation ; ajoutez des en-têtes user-agent ou des proxies pour imiter les humains.
  - Performance : Exécution headful (navigateur visible) ; passez en mode headless pour la production.
- **Exécution** : Requiert ChromeDriver (téléchargez depuis le site Selenium, correspondant à la version de Chrome). Installez Selenium via `pip install selenium`.

Si vous avez des questions sur des parties spécifiques, la modernisation du code ou le débogage, faites-le moi savoir !