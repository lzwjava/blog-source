---
audio: false
generated: true
lang: fr
layout: post
title: Guide Selenium
translated: true
type: note
---

Je vais fournir un guide complet sur Selenium, un outil populaire pour automatiser les navigateurs web. Ce guide couvrira les composants de Selenium, la configuration, l'utilisation de base, les fonctionnalités avancées et les bonnes pratiques, incluant des exemples de code en Python.

Selenium est un framework open-source pour automatiser les navigateurs web, principalement utilisé pour tester des applications web mais aussi pour le web scraping et les tâches d'automation. Il prend en charge plusieurs navigateurs (Chrome, Firefox, Safari, Edge, etc.) et langages de programmation (Python, Java, C#, Ruby, JavaScript, etc.).

---

### Guide Complet sur Selenium

#### 1. **Qu'est-ce que Selenium ?**
Selenium est une suite d'outils conçue pour automatiser les navigateurs web. Il vous permet d'interagir avec des éléments web, de simuler des actions utilisateur (clics, saisie, navigation) et de valider le comportement d'une application web. Les principaux composants de Selenium sont :
- **Selenium WebDriver** : Le composant principal pour l'automatisation des navigateurs, fournissant une API pour contrôler les navigateurs de manière programmatique.
- **Selenium IDE** : Une extension de navigateur pour enregistrer et rejouer les interactions du navigateur (principalement pour les débutants).
- **Selenium Grid** : Un outil pour exécuter des tests en parallèle sur plusieurs machines ou navigateurs.

Ce guide se concentre sur **Selenium WebDriver** avec Python, car c'est le composant le plus largement utilisé.

---

#### 2. **Configuration de Selenium**
Pour utiliser Selenium avec Python, vous devez installer les dépendances requises et configurer les pilotes de navigateur.

##### Prérequis
- Python (3.6 ou ultérieur recommandé)
- Un navigateur web (par exemple, Chrome, Firefox)
- Le pilote de navigateur correspondant (par exemple, ChromeDriver pour Chrome, GeckoDriver pour Firefox)
- Le package Python Selenium

##### Étapes d'installation
1. **Installer Python** : Assurez-vous que Python est installé et ajouté au PATH de votre système.
2. **Installer Selenium** :
   Exécutez la commande suivante dans votre terminal :
   ```bash
   pip install selenium
   ```
3. **Télécharger le pilote du navigateur** :
   - Pour Chrome : Téléchargez ChromeDriver depuis [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads). Assurez-vous que la version correspond à votre navigateur Chrome installé.
   - Pour Firefox : Téléchargez GeckoDriver depuis [github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases).
   - Placez l'exécutable du pilote dans un répertoire inclus dans le PATH de votre système ou spécifiez son chemin dans votre code.
4. **Vérifier l'installation** :
   Créez un script simple pour tester la configuration Selenium.

```python
from selenium import webdriver

# Initialiser le WebDriver Chrome
driver = webdriver.Chrome()
# Ouvrir un site web
driver.get("https://www.example.com")
# Imprimer le titre de la page
print(driver.title)
# Fermer le navigateur
driver.quit()
```

Exécutez le script. Si le navigateur s'ouvre, navigue vers `example.com` et imprime le titre de la page, votre configuration est réussie.

---

#### 3. **Concepts de Base de Selenium WebDriver**
Selenium WebDriver fournit une API pour interagir avec les éléments web. Les concepts clés incluent :

- **WebDriver** : L'interface pour contrôler une instance de navigateur (par exemple, `webdriver.Chrome()` pour Chrome).
- **WebElement** : Représente un élément HTML (par exemple, un bouton, un champ de saisie) sur une page web.
- **Localisateurs** : Méthodes pour trouver des éléments (par exemple, par ID, nom, classe, XPath, sélecteur CSS).
- **Actions** : Méthodes pour interagir avec les éléments (par exemple, cliquer, envoyer des touches, obtenir le texte).

##### Localisateurs Courants
Selenium utilise des localisateurs pour identifier les éléments sur une page web :
- `find_element_by_id("id")` : Trouve un élément par son ID.
- `find_element_by_name("name")` : Trouve un élément par son attribut name.
- `find_element_by_class_name("class")` : Trouve un élément par son nom de classe.
- `find_element_by_tag_name("tag")` : Trouve un élément par sa balise HTML.
- `find_element_by_css_selector("selector")` : Trouve un élément en utilisant un sélecteur CSS.
- `find_element_by_xpath("xpath")` : Trouve un élément en utilisant une expression XPath.
- `find_elements_*` : Retourne une liste de tous les éléments correspondants (par exemple, `find_elements_by_tag_name`).

##### Interactions de Base
- `click()` : Clique sur un élément.
- `send_keys("text")` : Saisit du texte dans un champ de saisie.
- `text` : Récupère le contenu textuel d'un élément.
- `get_attribute("attribute")` : Obtient la valeur d'un attribut d'un élément (par exemple, `value`, `href`).
- `is_displayed()`, `is_enabled()`, `is_selected()` : Vérifie l'état de l'élément.

---

#### 4. **Écrire un Script Selenium de Base**
Voici un exemple de script qui automatise la connexion à un site web (en utilisant une page de connexion hypothétique pour la démonstration).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialiser le WebDriver Chrome
driver = webdriver.Chrome()

try:
    # Naviguer vers la page de connexion
    driver.get("https://example.com/login")
    
    # Trouver les champs nom d'utilisateur et mot de passe
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    # Saisir les identifiants
    username.send_keys("testuser")
    password.send_keys("testpassword")
    
    # Soumettre le formulaire
    password.send_keys(Keys.RETURN)
    
    # Attendre le chargement de la page
    time.sleep(2)
    
    # Vérifier le succès de la connexion (vérifier un message de bienvenue)
    welcome_message = driver.find_element(By.CLASS_NAME, "welcome").text
    print(f"Connexion réussie ! Message de bienvenue : {welcome_message}")
    
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    
finally:
    # Fermer le navigateur
    driver.quit()
```

**Notes** :
- Remplacez `"https://example.com/login"` par l'URL réelle du site web cible.
- Ajustez les localisateurs d'éléments (`By.ID`, `By.CLASS_NAME`) en fonction de la structure HTML du site web.
- Le `time.sleep(2)` est une attente simple ; pour la production, utilisez des attentes explicites (abordées plus tard).

---

#### 5. **Fonctionnalités Avancées**
Selenium offre des fonctionnalités avancées pour une automatisation robuste.

##### a. **Mécanismes d'Attente**
Selenium fournit deux types d'attentes pour gérer les pages web dynamiques :
- **Attente Implicite** : Définit un temps d'attente par défaut pour toutes les recherches d'éléments.
  ```python
  driver.implicitly_wait(10)  # Attendre jusqu'à 10 secondes que les éléments apparaissent
  ```
- **Attente Explicite** : Attend une condition spécifique (par exemple, un élément est cliquable).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le WebDriver Chrome
driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    
    # Attendre qu'un élément soit cliquable (jusqu'à 10 secondes)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    button.click()
    
    print("Bouton cliqué avec succès !")
    
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    
finally:
    driver.quit()
```

##### b. **Gestion des Alertes**
Selenium peut interagir avec les alertes JavaScript, les confirmations et les invites :
```python
alert = driver.switch_to.alert
alert.accept()  # Cliquer sur OK
alert.dismiss()  # Cliquer sur Annuler
alert.send_keys("text")  # Saisir dans une invite
```

##### c. **Navigation dans les Cadres et Fenêtres**
- **Cadres/Iframes** : Basculer vers un cadre pour interagir avec ses éléments.
  ```python
  driver.switch_to.frame("frame-id")
  driver.switch_to.default_content()  # Revenir au contenu principal
  ```
- **Fenêtres/Onglets** : Gérer plusieurs fenêtres de navigateur.
  ```python
  original_window = driver.current_window_handle
  for window_handle in driver.window_handles:
      driver.switch_to.window(window_handle)
  ```

##### d. **Exécution de JavaScript**
Exécuter du code JavaScript directement dans le navigateur :
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Faire défiler jusqu'en bas
```

##### e. **Captures d'Écran**
Capturer des captures d'écran pour le débogage ou la documentation :
```python
driver.save_screenshot("screenshot.png")
```

---

#### 6. **Selenium avec Navigateurs Headless**
Les navigateurs headless s'exécutent sans interface graphique, idéaux pour les pipelines CI/CD ou les serveurs.
Exemple avec Chrome en mode headless :

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurer les options Chrome pour le mode headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialiser le WebDriver Chrome en mode headless
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.example.com")
    print(f"Titre de la page : {driver.title}")
    
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    
finally:
    driver.quit()
```

---

#### 7. **Bonnes Pratiques**
- **Utiliser les Attentes Explicites** : Évitez `time.sleep()` pour les pages dynamiques ; utilisez `WebDriverWait` avec `expected_conditions`.
- **Gérer les Exceptions** : Encapsulez le code dans des blocs `try-except` pour gérer les erreurs gracieusement.
- **Fermer le WebDriver** : Appelez toujours `driver.quit()` pour fermer le navigateur et libérer les ressources.
- **Organiser les Localisateurs** : Stockez les localisateurs dans un fichier ou une classe séparé pour la maintenabilité.
- **Utiliser le Modèle d'Objet de Page (Page Object Model - POM)** : Encapsulez les interactions de page dans des classes pour améliorer la réutilisabilité du code.

Exemple de Modèle d'Objet de Page :

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit-button")
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

# Utilisation
from selenium import webdriver

driver = webdriver.Chrome()
login_page = LoginPage(driver)
try:
    driver.get("https://example.com/login")
    login_page.login("testuser", "testpassword")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
finally:
    driver.quit()
```

---

#### 8. **Selenium Grid**
Selenium Grid permet d'exécuter des tests sur plusieurs navigateurs, systèmes d'exploitation ou machines en parallèle. Il consiste en un **hub** (serveur central) et des **nodes** (machines exécutant les navigateurs).
- **Configuration** : Configurez un hub et des nodes en utilisant le fichier JAR de Selenium Grid ou Docker.
- **Cas d'Usage** : Tester la compatibilité multi-navigateurs (par exemple, Chrome sur Windows, Firefox sur Linux).
- **Exemple** : Se connecter à un WebDriver distant :
  ```python
  from selenium.webdriver.remote.webdriver import WebDriver
  driver = WebDriver(command_executor="http://hub-ip:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
  ```

---

#### 9. **Défis Courants et Solutions**
- **Élément Non Trouvé** : Utilisez des attentes explicites ou vérifiez les localisateurs avec les outils de développement du navigateur.
- **Référence d'Élément Obsolète (Stale Element Reference)** : Re-localisez les éléments après les actualisations de page ou les changements du DOM.
- **Lenteur des Performances** : Optimisez les localisateurs (préférez ID/CSS à XPath) et utilisez le mode headless.
- **Contenu Dynamique** : Utilisez l'exécution JavaScript ou des attentes pour gérer le contenu chargé en AJAX.

---

#### 10. **Ressources**
- Documentation Officielle : [selenium.dev](https://www.selenium.dev/documentation/)
- Bindings Python Selenium : [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- Pilotes de Navigateurs : ChromeDriver, GeckoDriver
- Communauté : Stack Overflow, publications X (recherchez #Selenium ou #WebDriver)

---

Ce guide couvre les éléments essentiels de Selenium WebDriver, de la configuration à l'utilisation avancée. Faites-moi savoir si vous avez besoin d'aide pour une tâche Selenium spécifique ou des exemples plus avancés !