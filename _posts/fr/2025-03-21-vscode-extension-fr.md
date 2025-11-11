---
audio: false
generated: true
lang: fr
layout: post
title: Dépannage de l'Installation d'Extension VSCode avec Problèmes de Proxy
translated: true
type: note
---

Pour consulter le journal d'installation des extensions dans Visual Studio Code (VSCode) ou utiliser la ligne de commande pour installer une extension avec `code --install-extension` et visualiser le journal—en particulier si vous suspectez un problème de proxy—voici comment procéder :

---

### Utilisation de la ligne de commande avec `code --install-extension`
Vous pouvez installer des extensions via la ligne de commande et obtenir une certaine visibilité sur le processus, ce qui peut aider à diagnostiquer les problèmes de proxy.

1. **Installer avec une sortie verbeuse**
   Exécutez la commande suivante pour installer une extension et voir une sortie plus détaillée :
   ```bash
   code --install-extension <extension-id> --verbose
   ```
   - Remplacez `<extension-id>` par l'identifiant de l'extension (par exemple, `vscodevim.vim`).
   - Le drapeau `--verbose` augmente le niveau de détail de la sortie, affichant la progression et les erreurs potentielles, telles que les problèmes de proxy ou de réseau.

2. **Gérer les problèmes de proxy**
   Si vous êtes derrière un proxy, celui-ci pourrait interférer avec l'installation. Essayez ces approches :
   - **Définir les variables d'environnement du proxy** :
     Avant d'exécuter la commande, configurez les paramètres du proxy :
     ```bash
     export HTTP_PROXY=http://votre-serveur-proxy:port
     export HTTPS_PROXY=http://votre-serveur-proxy:port
     code --install-extension <extension-id>
     ```
     - Sur Windows, utilisez `set` au lieu de `export` :
       ```cmd
       set HTTP_PROXY=http://votre-serveur-proxy:port
       set HTTPS_PROXY=http://votre-serveur-proxy:port
       code --install-extension <extension-id>
       ```
   - **Spécifier le proxy directement** :
     Utilisez le drapeau `--proxy-server` :
     ```bash
     code --install-extension <extension-id> --proxy-server=http://votre-serveur-proxy:port
     ```

3. **Vérifier la sortie**
   - La sortie console du drapeau `--verbose` montrera la progression de l'installation et toute erreur (par exemple, des timeouts de connexion ou des échecs d'authentification proxy).
   - Note : L'interface en ligne de commande (`code`) a un support proxy limité par rapport à l'interface graphique de VSCode, donc les journaux pourraient ne pas être aussi détaillés que prévu.

---

### Consultation des journaux dans VSCode
Pour des journaux plus détaillés—en particulier après une tentative d'installation—utilisez les fonctionnalités de journalisation intégrées à VSCode :

1. **Ouvrir le dossier des journaux**
   - Ouvrez VSCode et accédez à la Palette de commandes :
     - Appuyez sur `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur macOS).
     - Tapez et sélectionnez **Developer: Open Logs Folder**.
   - Cela ouvre un dossier contenant divers fichiers journaux. Cherchez :
     - **`exthost.log`** : Journaux liés aux processus de l'hôte des extensions, y compris les tentatives d'installation.
     - **`sharedprocess.log`** : Journaux pour les processus partagés qui peuvent inclure des événements liés aux extensions.
   - Ouvrez ces fichiers dans un éditeur de texte et recherchez les erreurs mentionnant l'ID d'extension, les problèmes de réseau ou les problèmes de proxy.

2. **Afficher le panneau Output**
   - Dans VSCode, allez dans `View > Output` pour ouvrir le panneau **Output**.
   - Dans le menu déroulant à droite, sélectionnez **Extensions**.
   - Cela affiche les journaux en temps réel pour les activités des extensions lors d'une installation depuis l'interface VSCode (pas directement via CLI). Si vous réessayez l'installation via l'interface utilisateur de VSCode, vous pourriez voir les erreurs liées au proxy ici.

---

### Étapes supplémentaires pour le dépannage du proxy
Puisque vous suspectez un problème de proxy, voici des conseils supplémentaires pour assurer une configuration correcte :

- **Configurer le proxy dans VSCode**
  - Ouvrez les paramètres de VSCode (`File > Preferences > Settings` ou `Ctrl+,`).
  - Cherchez `proxy` et définissez :
    ```json
    "http.proxy": "http://votre-serveur-proxy:port"
    ```
  - Optionnellement, ajustez `"http.proxyStrictSSL"` (définissez sur `false` si nécessaire) ou `"http.proxyAuthorization"` (pour les proxies authentifiés).
  - Ces paramètres s'appliquent aux installations dans VSCode, pas nécessairement à la CLI.

- **Tester l'accès réseau**
  - Testez manuellement si le proxy autorise l'accès au VSCode Marketplace :
    - Trouvez l'URL du fichier VSIX de l'extension (par exemple, sur le site du Marketplace).
    - Utilisez un outil comme `curl` :
      ```bash
      curl -x http://votre-serveur-proxy:port <vsix-url>
      ```
    - Si cela échoue, votre proxy pourrait bloquer la connexion.

---

### Approche recommandée
- **Pour l'installation en CLI** : Utilisez `code --install-extension <extension-id> --verbose` avec les variables d'environnement de proxy ou `--proxy-server` pour voir la sortie immédiate. Vérifiez les erreurs dans le terminal.
- **Pour des journaux détaillés** : Installez l'extension via l'interface utilisateur de VSCode (Marketplace) et vérifiez le panneau **Output > Extensions** ou le dossier des journaux (`exthost.log`).
- **Vérification du proxy** : Assurez-vous que les paramètres de proxy sont corrects à la fois dans votre système et dans VSCode.

Cette combinaison vous permet de surveiller la progression et de diagnostiquer efficacement les problèmes de proxy. Si la sortie CLI n'est pas suffisante, les journaux de VSCode fourniront un aperçu plus profond de ce qui ne fonctionne pas.