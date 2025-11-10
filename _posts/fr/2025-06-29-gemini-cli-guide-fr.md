---
audio: false
generated: true
lang: fr
layout: post
title: Installer et utiliser Gemini CLI
translated: true
type: note
---

Voici un guide concis pour installer, configurer et utiliser la **Google Gemini CLI**, un agent IA open-source qui intègre les capacités de Gemini dans votre terminal pour le codage, l'automatisation des tâches et plus encore. Ce guide est basé sur les dernières informations disponibles au 29 juin 2025.

---

## **Guide Google Gemini CLI**

### **Qu'est-ce que Gemini CLI ?**
Gemini CLI est un outil en ligne de commande open-source développé par Google qui apporte la puissance du modèle Gemini 2.5 Pro (avec une fenêtre de contexte d'1 million de tokens) dans votre terminal. Il prend en charge le codage, le débogage, la génération de contenu, l'automatisation des tâches et les tâches multimodales comme la génération d'images et de vidéos. Il est gratuit à utiliser avec un compte Google et s'intègre à des outils comme Google Search et les serveurs Model Context Protocol (MCP).

---

### **Prérequis**
- **Node.js** : Version 18 ou supérieure. Vérifiez avec `node -v`. Installez-le depuis [nodejs.org](https://nodejs.org) si nécessaire.
- **Compte Google** : Requis pour un accès gratuit à Gemini 2.5 Pro (60 requêtes/minute, 1 000 requêtes/jour).
- (Optionnel) **Clé API** : Pour des limites plus élevées ou des modèles spécifiques, générez-en une depuis [Google AI Studio](https://aistudio.google.com).
- (Optionnel) **Docker** : Pour l'intégration de serveurs MCP (par exemple, outils GitHub).

---

### **Installation**
Il existe deux façons de commencer avec Gemini CLI :

1. **Installation Globale** :
   ```bash
   npm install -g @google/gemini-cli
   gemini
   ```
   Cela installe la CLI globalement et l'exécute avec la commande `gemini`.

2. **Exécution Sans Installation** :
   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```
   Cela exécute la CLI directement sans installation, idéal pour les tests.

---

### **Configuration**
1. **Lancez la CLI** :
   - Exécutez `gemini` dans votre terminal.
   - Lors du premier lancement, sélectionnez un thème (par exemple, ASCII, sombre, clair) et appuyez sur Entrée.

2. **Authentification** :
   - Choisissez **Login with Google** pour un accès gratuit (recommandé pour la plupart des utilisateurs).
   - Une fenêtre de navigateur s'ouvrira ; connectez-vous avec votre compte Google.
   - Alternativement, utilisez une clé API :
     - Générez une clé depuis [Google AI Studio](https://aistudio.google.com).
     - Définissez-la comme variable d'environnement :
       ```bash
       export GEMINI_API_KEY=VOTRE_CLE_API
       ```
     - Ceci est utile pour des limites plus élevées ou un usage professionnel.

3. **Naviguez vers votre projet** :
   - Exécutez `gemini` dans le répertoire racine de votre projet pour fournir un contexte pour les tâches liées au code.

---

### **Utilisation de Base**
Gemini CLI fonctionne dans un environnement interactif de type Read-Eval-Print Loop (REPL). Tapez des commandes ou des invites en langage naturel pour interagir avec le modèle Gemini. Voici quelques tâches courantes :

1. **Explication de Code** :
   - Naviguez vers un dossier de projet et exécutez :
     ```bash
     gemini
     ```
   - Invite : `Explain the architecture of this project` ou `Describe the main function in main.py`.
   - La CLI lit les fichiers et fournit une explication structurée.

2. **Génération de Code** :
   - Invite : `Create a simple to-do app in HTML, CSS, and JavaScript`.
   - La CLI génère le code et peut le sauvegarder dans des fichiers si demandé.

3. **Débogage** :
   - Collez un message d'erreur ou une stack trace et demandez : `What’s causing this error?`.
   - La CLI analyse l'erreur et suggère des correctifs, utilisant potentiellement Google Search pour un contexte supplémentaire.

4. **Gestion de Fichiers** :
   - Invite : `Organize my PDF invoices by month of expenditure`.
   - La CLI peut manipuler les fichiers ou convertir les formats (par exemple, images en PNG).

5. **Intégration GitHub** :
   - Utilisez les serveurs MCP pour les tâches GitHub (par exemple, lister les issues) :
     - Configurez un serveur MCP GitHub dans `.gemini/settings.json` avec un Personal Access Token (PAT).
     - Invite : `Get all open issues assigned to me in the foo/bar repo`.
   - Exécutez `/mcp` pour lister les serveurs et outils MCP configurés.

6. **Tâches Multimodales** :
   - Générez des médias avec des outils comme Imagen ou Veo :
     - Invite : `Create a short video of a cat’s adventures in Australia using Veo`.

---

### **Fonctionnalités Clés**
- **Fichiers de Contexte (GEMINI.md)** : Ajoutez un fichier `GEMINI.md` dans la racine de votre projet pour définir les styles de codage, les règles du projet ou les préférences (par exemple, "Use async/await for JavaScript"). La CLI l'utilise pour des réponses sur mesure.
- **Outils Intégrés** :
   - `/tools` : Liste les outils disponibles (par exemple, Google Search, opérations sur fichiers).
   - `/compress` : Résume le contexte du chat pour économiser des tokens.
   - `/bug` : Signalez directement des problèmes sur le dépôt GitHub de Gemini CLI.
- **Mode Non Interactif** : Pour le scriptage, redirigez les commandes :
   ```bash
   echo "Write a Python script" | gemini
   ```
- **Mémoire de Conversation** : Sauvegardez l'historique de session avec `/save <tag>` et reprenez avec `/restore <tag>`.
- **Configuration Personnalisée** :
   - Modifiez `~/.gemini/settings.json` pour les paramètres globaux ou `.gemini/settings.json` dans un projet pour les paramètres locaux.
   - Exemple : Définissez des serveurs MCP ou des thèmes personnalisés.

---

### **Astuces et Conseils**
- **Commencez par des Plans** : Pour les tâches complexes, demandez d'abord un plan : `Create a detailed implementation plan for a login system`. Cela garantit une sortie structurée.
- **Utilisez le Contexte Local** : Encodez les détails spécifiques au projet dans `GEMINI.md` au lieu de compter sur les serveurs MCP pour des réponses plus rapides et fiables.
- **Débogage** : Activez la journalisation verbeuse avec `DEBUG=true gemini` pour des informations détaillées des requêtes/réponses.
- **Revoyez les Changements** : Revevez toujours les modifications de fichiers ou les commandes avant de les approuver (tapez `y` pour confirmer).
- **Explorez les Outils** : Exécutez `/tools` pour découvrir les capacités intégrées comme la recherche web ou la sauvegarde de mémoire.

---

### **Dépannage**
- **Problèmes d'Authentification** : Assurez-vous que votre compte Google ou votre clé API est valide. Utilisez `/auth` pour changer de méthode.
- **Limites de Taux** : Le niveau gratuit permet 60 requêtes/minute et 1 000/jour. Pour des limites plus élevées, utilisez une clé API ou Vertex AI.
- **Erreurs** : Consultez le [Guide de Dépannage](https://github.com/google-gemini/gemini-cli/docs/troubleshooting.md) sur GitHub.
- **Réponses Lentes** : La CLI est en version préliminaire et peut être lente avec les appels API. Signalez vos retours sur GitHub.

---

### **Utilisation Avancée**
- **Intégration de Serveurs MCP** :
  - Configurez un serveur MCP GitHub pour les interactions avec le dépôt :
    - Créez un PAT GitHub avec les portées nécessaires.
    - Ajoutez-le dans `.gemini/settings.json` :
      ```json
      {
        "mcpServers": [
          {
            "name": "github",
            "url": "http://localhost:8080",
            "type": "github"
          }
        ]
      }
      ```
    - Exécutez un conteneur Docker pour le serveur MCP (voir la documentation GitHub).
- **Scriptage** : Automatisez les tâches en intégrant Gemini CLI dans des scripts :
  ```bash
  gemini --non-interactive "Generate a bash script to backup my files"
  ```
- **Invites Multimodales** :
  - Exemple : `Describe this image: path/to/image.jpg` (nécessite un modèle compatible avec la vision comme `gemini-pro-vision`).

---

### **Limitations**
- **Stade Préliminaire** : Gemini CLI est en pré-GA, avec un support potentiellement limité ou des bugs.
- **Pas Entièrement Open-Source** : Seule l'interface CLI est sous licence Apache 2.0 ; le modèle Gemini est propriétaire.
- **Partage des Quotas** : Les limites sont partagées avec Gemini Code Assist si utilisé.
- **Tarification Future** : La tarification post-préversion n'est pas claire ; les fonctionnalités avancées pourraient nécessiter un paiement.

---

### **Ressources**
- **GitHub Officiel** : [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Documentation** : [gemini-cli.click](https://gemini-cli.click) ou la documentation GitHub
- **Annonce sur le Blog** : [blog.google](https://blog.google)
- **Retours** : Signalez des bugs ou des suggestions sur GitHub.

---

### **Exemple de Flux de Travail**
1. Installation : `npm install -g @google/gemini-cli`
2. Exécution : `cd my-project && gemini`
3. Authentification : Connectez-vous avec Google.
4. Invite : `Write a Python script for a REST API with FastAPI`.
5. Revoyez et sauvegardez le code généré.
6. Utilisez `/tools` pour explorer les fonctionnalités supplémentaires comme l'intégration GitHub.

---

Gemini CLI est un outil puissant pour les développeurs, offrant une intégration IA transparente dans le terminal. Commencez simplement, tirez parti de `GEMINI.md` pour le contexte, et explorez ses capacités multimodales pour booster votre productivité. Pour plus d'exemples, consultez les [tutoriels GitHub](https://github.com/google-gemini/gemini-cli/docs/cli/tutorials.md).

Si vous avez besoin d'exemples spécifiques ou avez des questions sur une fonctionnalité particulière, faites-le moi savoir !