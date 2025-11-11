---
audio: false
generated: true
lang: fr
layout: post
title: Débuter avec GitHub Copilot dans VS Code
translated: true
type: note
---

Utiliser GitHub Copilot dans Visual Studio Code (VS Code) est simple une fois qu'il est configuré. Voici un guide étape par étape pour commencer, en date du 20 mars 2025 :

---

### Étape 1 : Installer VS Code
- Assurez-vous d'avoir Visual Studio Code d'installé. Téléchargez-le sur [code.visualstudio.com](https://code.visualstudio.com/) si ce n'est pas déjà fait.
- Mettez VS Code à jour vers la dernière version pour une compatibilité optimale (allez dans `Aide > Vérifier les mises à jour`).

---

### Étape 2 : Installer l'extension GitHub Copilot
1. **Ouvrez VS Code**.
2. **Accédez au Marketplace des Extensions** :
   - Cliquez sur l'icône Extensions dans la Barre d'activité sur la gauche (ou appuyez sur `Ctrl+Shift+X` / `Cmd+Shift+X` sur Mac).
3. **Recherchez "GitHub Copilot"** :
   - Tapez "GitHub Copilot" dans la barre de recherche.
   - Cherchez l'extension officielle de GitHub (elle aura un badge vérifié).
4. **Installez l'Extension** :
   - Cliquez sur le bouton `Installer` à côté de "GitHub Copilot".
5. **Optionnel : Installez Copilot Chat (Recommandé)** :
   - Recherchez "GitHub Copilot Chat" et installez-la également. Cela ajoute des fonctionnalités d'IA conversationnelle comme poser des questions ou générer du code via le chat.

---

### Étape 3 : Se connecter à GitHub Copilot
1. **Authentifiez-vous avec GitHub** :
   - Après l'installation, une invite vous demandant de vous connecter apparaîtra.
   - Cliquez sur `Sign in to GitHub` dans la fenêtre contextuelle ou allez à l'icône d'état Copilot (dans le coin inférieur droit de VS Code) et sélectionnez "Sign in".
2. **Autorisez dans le Navigateur** :
   - Une fenêtre de navigateur s'ouvrira pour vous demander de vous connecter à votre compte GitHub.
   - Approuvez la demande d'autorisation en cliquant sur `Authorize Git hypoxia`.
3. **Copiez le Code** :
   - GitHub fournira un code à usage unique. Copiez-le et collez-le dans VS Code lorsque vous y êtes invité.
4. **Vérifiez l'Activation** :
   - Une fois connecté, l'icône Copilot dans la barre d'état devrait devenir verte, indiquant qu'elle est active. Vous verrez également une notification confirmant votre accès.

---

### Étape 4 : Configurer Copilot (Optionnel)
- **Activer/Désactiver les Suggestions** :
  - Allez dans `Fichier > Préférences > Paramètres` (ou `Ctrl+,` / `Cmd+,`).
  - Recherchez "Copilot" pour ajuster les paramètres, comme activer les suggestions inline ou le désactiver pour des langages spécifiques.
- **Vérifier l'Abonnement** :
  - Copilot nécessite un abonnement (10 $/mois ou 100 $/an) après un essai de 30 jours. Les étudiants, enseignants et mainteneurs de projets open source peuvent demander un accès gratuit via [GitHub Education](https://education.github.com/) ou les paramètres de Copilot.

---

### Étape 5 : Commencer à utiliser Copilot
Voici comment tirer parti de Copilot dans votre flux de travail de codage :

#### 1. **Suggestions de Code**
- **Auto-complétion Inline** :
  - Commencez à taper dans un fichier (par exemple, `def calculate_sum(` en Python), et Copilot suggérera des complétions en texte gris.
  - Appuyez sur `Tab` pour accepter la suggestion ou continuez à taper pour l'ignorer.
- **Suggestions Multi-lignes** :
  - Écrivez un commentaire comme `// Function to sort an array` et appuyez sur Entrée. Copilot pourrait suggérer une implémentation entière (par exemple, un algorithme de tri).
  - Utilisez `Alt+]` (ou `Option+]` sur Mac) pour parcourir les suggestions multiples.

#### 2. **Génération de Code à partir de Commentaires**
- Tapez un commentaire descriptif comme :
  ```javascript
  // Fetch data from an API and handle errors
  ```
  Appuyez sur Entrée, et Copilot peut générer :
  ```javascript
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  ```
- Acceptez avec `Tab` ou modifiez si nécessaire.

#### 3. **Copilot Chat (Si Installé)**
- **Ouvrir le Chat** :
  - Cliquez sur l'icône de chat dans la barre latérale ou utilisez `Ctrl+Alt+C` (personnalisable).
- **Posez des Questions** :
  - Tapez quelque chose comme "Explain how Promises work in JavaScript" ou "Write a Python script to read a CSV file."
  - Copilot répondra dans le panneau de chat et pourra insérer du code directement dans votre éditeur.
- **Aide Contextuelle** :
  - Surlignez du code, faites un clic droit et sélectionnez "Ask Copilot" pour l'expliquer ou le refactoriser.

#### 4. **Débogage et Tests**
- Écrivez un commentaire comme `// Write unit tests for this function`, et Copilot peut générer des cas de test en utilisant des frameworks comme Jest ou PyTest.

---

### Conseils pour une Utilisation Efficace
- **Soyez Spécifique** : Plus vous fournissez de contexte (par exemple, des commentaires, des noms de variables), meilleures sont les suggestions de Copilot.
- **Vérifiez les Suggestions** : Copilot n'est pas parfait — vérifiez toujours son code pour l'exactitude et la sécurité.
- **Support des Langages** : Il fonctionne mieux avec les langages populaires (Python, JavaScript, Java, etc.) mais en supporte des dizaines d'autres.
- **Raccourcis Clavier** :
  - `Alt+\` (ou `Option+\` sur Mac) : Afficher manuellement toutes les suggestions.
  - `Ctrl+Entrée` : Ouvrir le panneau de suggestions.

---

### Dépannage
- **Cela ne fonctionne pas ?** :
  - Assurez-vous d'être connecté (vérifiez la barre d'état).
  - Vérifiez que votre abonnement est actif dans les paramètres de votre compte GitHub.
  - Redémarrez VS Code ou réinstallez l'extension si les problèmes persistent.
- **Aucune Suggestion ?** :
  - Vérifiez si Copilot est activé pour le langage actuel (`editor.inlineSuggest.enabled` doit être vrai dans les paramètres).

---

C'est tout ! Vous êtes maintenant prêt à utiliser GitHub Copilot dans VS Code. Commencez par ouvrir un fichier, tapez du code ou un commentaire, et laissez Copilot vous assister. Bon codage !