---
audio: false
generated: true
lang: fr
layout: post
title: Script Selenium pour le Contournement de Cloudflare
translated: true
type: note
---

Votre script Selenium est conçu pour interagir avec "https://grok.com" en utilisant Firefox et un profil spécifique, mais il rencontre un défi de détection de bot Cloudflare, spécifiquement la case à cocher "Verify you are human". Même après avoir cliqué sur la case à cocher, le script semble avoir du mal à contourner la vérification, ce qui empêche l'accès au contenu principal (par exemple, la zone de texte `textarea`). Cloudflare utilise des méthodes sophistiquées pour détecter les navigateurs automatisés, telles que l'analyse des en-têtes HTTP, l'empreinte TLS et les vérifications comportementales, ce qui peut rendre le contournement de ce défi difficile avec Selenium seul. Cependant, il existe des stratégies que vous pouvez essayer pour passer le test Cloudflare tout en restant dans votre configuration actuelle basée sur Firefox. Ci-dessous se trouvent deux approches pratiques adaptées à votre script, suivies de considérations supplémentaires si celles-ci ne suffisent pas.

---

### **Méthode 1 : Achèvement manuel du défi avec réutilisation du profil**
Étant donné que votre script utilise un profil Firefox spécifique (`/home/lzw/.mozilla/firefox/wzfodx6v.default`), vous pouvez l'utiliser pour stocker les données de session après avoir passé manuellement le défi Cloudflare. Voici comment procéder :

1. **Ouvrir Firefox manuellement avec le profil** :
   - Lancez Firefox en utilisant le même profil spécifié dans votre script. Vous pouvez le faire via la ligne de commande :
     ```bash
     firefox --profile "/home/lzw/.mozilla/firefox/wzfodx6v.default"
     ```
   - Alternativement, utilisez le gestionnaire de profils de Firefox (`firefox --ProfileManager`) pour sélectionner `wzfodx6v.default`.

2. **Naviguer et passer le défi** :
   - Allez sur "https://grok.com" dans le navigateur.
   - Lorsque vous êtes invité à cocher la case "Verify you are human" de Cloudflare, cliquez dessus et terminez toutes les étapes de vérification supplémentaires si elles apparaissent.
   - Attendez d'arriver sur la page principale (par exemple, là où la zone de texte avec `aria-label="Ask Grok anything"` est visible).

3. **Fermer le navigateur** :
   - Quittez Firefox pour vous assurer que le profil enregistre les cookies de session, y compris tous les jetons d'autorisation Cloudflare (comme `cf_clearance`).

4. **Exécuter votre script Selenium** :
   - Exécutez votre script tel quel. Puisqu'il utilise le même profil, il devrait hériter des cookies et des données de session stockés, ce qui pourrait lui permettre de contourner le défi.

**Pourquoi cela pourrait fonctionner** : Cloudflare s'appuie souvent sur les cookies pour se souvenir qu'un navigateur a passé son test. En pré-authentifiant le profil manuellement, votre session automatisée peut apparaître comme une continuation d'une visite vérifiée.

**Limitations** : Si Cloudflare effectue des vérifications supplémentaires à chaque chargement de page (par exemple, en détectant les empreintes d'automatisation de Selenium), cette méthode pourrait échouer. Dans ce cas, essayez l'approche suivante.

---

### **Méthode 2 : Extraire et définir les cookies dans le script**
Si la réutilisation du profil ne fonctionne pas, vous pouvez extraire manuellement les cookies après avoir passé le défi et les injecter dans votre pilote Selenium. Voici le processus étape par étape :

1. **Passer le défi manuellement** :
   - Suivez les étapes 1 et 2 de la Méthode 1 pour atteindre la page principale de "https://grok.com".

2. **Extraire les cookies** :
   - Ouvrez les Outils de Développement de Firefox (F12 ou clic droit > Inspecter).
   - Allez dans l'onglet **Stockage** (ou l'onglet **Réseau**, puis rechargez la page pour inspecter les cookies).
   - Cherchez les cookies associés à `.grok.com`, en particulier `cf_clearance` (le cookie de vérification Cloudflare).
   - Notez le `nom`, la `valeur` et le `domaine` de chaque cookie pertinent. Par exemple :
     - Nom : `cf_clearance`, Valeur : `abc123...`, Domaine : `.grok.com`
     - D'autres cookies comme `__cfduid` ou ceux spécifiques à la session pourraient également être présents.

3. **Modifier votre script** :
   - Ajoutez les cookies à votre pilote Selenium avant de naviguer vers l'URL. Mettez à jour votre code comme ceci :
     ```python
     # ... (les imports et la configuration existants restent inchangés)

     # Configurer le service geckodriver
     service = Service(executable_path="/home/lzw/bin/geckodriver")
     driver = webdriver.Firefox(service=service, options=firefox_options)

     # Ouvrir d'abord une page vierge pour définir les cookies (les cookies ne peuvent être définis qu'après un chargement de page)
     driver.get("about:blank")

     # Ajouter les cookies que vous avez extraits
     cookies = [
         {"name": "cf_clearance", "value": "abc123...", "domain": ".grok.com"},
         # Ajouter d'autres cookies si nécessaire, par exemple :
         # {"name": "__cfduid", "value": "xyz789...", "domain": ".grok.com"},
     ]
     for cookie in cookies:
         driver.add_cookie(cookie)

     # Maintenant, naviguez vers l'URL cible
     driver.get("https://grok.com")

     # Imprimer le titre de la page
     print("Title of the page:", driver.title)

     # ... (le reste de votre script reste le même)
     ```

4. **Tester le script** :
   - Exécutez le script modifié. Les cookies pré-définis devraient signaler à Cloudflare que le navigateur a déjà passé le défi.

**Pourquoi cela pourrait fonctionner** : Définir explicitement le cookie `cf_clearance` imite une session vérifiée, contournant potentiellement le besoin d'interagir avec la case à cocher.

**Limitations** : Les cookies pourraient être liés à des empreintes de navigateur (par exemple, l'agent utilisateur, l'adresse IP, ou les paramètres TLS). Si l'empreinte de Selenium diffère de celle de la session manuelle, Cloudflare pourrait rejeter les cookies ou redemander une vérification.

---

### **Débogage et améliorations supplémentaires**
Si aucune méthode ne résout complètement le problème, envisagez ces ajustements à votre script pour vous assurer qu'il interagit correctement avec le défi Cloudflare :

- **Vérifier la présence d'iframes** : La case à cocher "Verify you are human" pourrait se trouver dans une iframe. Modifiez votre code de clic sur la case à cocher pour d'abord basculer vers l'iframe :
  ```python
  try:
      wait = WebDriverWait(driver, 20)
      iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'cloudflare')]")))
      driver.switch_to.frame(iframe)
      label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='cb-lb']")))
      checkbox = label.find_element(By.TAG_NAME, "input")
      print("Checkbox found:", checkbox.is_displayed())
      checkbox.click()
      driver.switch_to.default_content()  # Revenir au contenu principal
      print("Checkbox clicked.")
  except Exception as e:
      print("Checkbox not found or not clickable:", e)
  ```

- **Améliorer la logique d'attente** : Après avoir cliqué sur la case à cocher, attendez un signe clair que le défi est passé (par exemple, la disparition de la page de vérification) :
  ```python
  try:
      wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify you are human')]")))
      print("Challenge passed.")
  except Exception as e:
      print("Challenge not passed:", e)
  ```

- **Masquer l'automatisation** : Ajoutez du JavaScript pour cacher les traces d'automatisation de Selenium :
  ```python
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  ```

---

### **Si tout échoue : Approches alternatives**
Si la détection de Cloudflare persiste, cela pourrait être dû à une empreinte avancée que votre configuration actuelle ne peut pas éviter. Voici des options d'escalade, bien qu'elles s'écartent de votre préférence pour Firefox :

- **Passer à Chrome avec Undetected ChromeDriver** :
  - Installation : `pip install undetected-chromedriver`
  - Modifiez la configuration :
    ```python
    import undetected_chromedriver as uc
    driver = uc.Chrome()
    driver.get("https://grok.com")
    ```
  - Cette bibliothèque modifie Chrome pour éviter les méthodes de détection courantes.

- **Utiliser un proxy ou un solveur de CAPTCHA** : Des services comme 2Captcha ou des proxies résidentiels peuvent gérer les défis, mais ils ajoutent de la complexité et un coût.

---

### **Prochaines étapes recommandées**
Commencez par la **Méthode 1** (réutilisation du profil) car c'est la plus simple et correspond à la configuration de votre script. Si elle échoue, essayez la **Méthode 2** (injection de cookies) avec la vérification de l'iframe ajoutée. Ces méthodes optimisent votre configuration Firefox existante sans nécessiter de nouveaux outils. Testez chaque approche et surveillez la sortie (par exemple, `driver.title` et les messages d'exception) pour confirmer si le défi est contourné. Si vous rencontrez toujours des problèmes, envisagez les approches alternatives en fonction de la flexibilité de votre projet.

N'hésitez pas à me dire si vous avez besoin d'aide pour mettre en œuvre ou résoudre les problèmes de ces solutions !