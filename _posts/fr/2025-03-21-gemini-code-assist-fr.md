---
audio: false
generated: true
lang: fr
layout: post
title: Gemini Code Assist
translated: true
type: note
---

Pour utiliser **Gemini Code Assist**, un assistant de codage alimenté par l'IA développé par Google, vous pouvez l'intégrer à votre environnement de développement, tel que Visual Studio Code (VSCode), pour améliorer votre expérience de codage. Gemini Code Assist aide à la complétion de code, à la génération de code, aux explications, au débogage, et plus encore. Voici un guide étape par étape pour le configurer et l'utiliser dans VSCode.

---

### Étape 1 : Installer l'extension Gemini Code Assist
- Ouvrez **VSCode**.
- Accédez à la vue **Extensions** en cliquant sur l'icône Extensions dans la barre d'activité ou en appuyant sur `Ctrl+Shift+X` (Windows/Linux) ou `Cmd+Shift+X` (macOS).
- Dans la barre de recherche, tapez **"Gemini Code Assist"**.
- Trouvez l'extension officielle dans le marketplace, cliquez sur **Installer**, et redémarrez VSCode si vous y êtes invité.

---

### Étape 2 : Se connecter avec votre compte Google
- Après l'installation, localisez **l'icône Gemini Code Assist** dans la barre d'activité (sur le côté gauche de VSCode).
- Cliquez sur l'icône pour ouvrir le volet Gemini.
- Sélectionnez **"Se connecter avec Google"** et suivez les invites d'authentification en utilisant votre compte Google.
  - Pour la **version gratuite** (Gemini Code Assist pour les particuliers), un compte Gmail personnel est suffisant.
  - Pour les **versions Standard ou Entreprise**, vous devrez peut-être le lier à un projet Google Cloud avec les API nécessaires activées.

---

### Étape 3 : Commencer à utiliser Gemini Code Assist
Une fois connecté, vous pouvez tirer parti de ses fonctionnalités de plusieurs manières :

#### a. Complétion de code
- Pendant que vous tapez dans l'éditeur, Gemini suggère automatiquement des complétions de code.
- Acceptez ces suggestions en appuyant sur `Tab` (ou une autre touche configurée).

#### b. Génération de code et explications via le chat
- Ouvrez le **volet Gemini** en cliquant sur son icône dans la barre d'activité.
- Tapez une invite en langage naturel, telle que :
  - "Explique ce code"
  - "Génère une fonction pour trier un tableau"
  - "Aide-moi à déboguer cette erreur"
- Pour référencer un code spécifique, surlignez-le dans l'éditeur avant de saisir votre invite.
- Gemini répondra dans le volet de discussion, et vous pourrez insérer tout code généré dans votre fichier si vous le souhaitez.

#### c. Transformation de code
- Accédez au menu Quick Pick en appuyant sur `Ctrl+I` (Windows/Linux) ou `Cmd+I` (macOS).
- Entrez une commande comme `/generate function to create a Cloud Storage bucket`.
- Examinez les modifications suggérées dans une vue diff et appliquez-les si nécessaire.

#### d. Suggestions inline
- Pendant le codage, Gemini peut offrir des suggestions inline pour compléter des lignes ou des blocs de code.
- Celles-ci apparaissent au fur et à mesure que vous tapez et peuvent être acceptées par une pression sur une touche.

---

### Conseils supplémentaires
- **Visite guidée** : Lors de la première utilisation, vous pourriez voir une option pour lancer une visite guidée dans VSCode. Ce guide interactif présente les fonctionnalités de l'extension.
- **Langages pris en charge** : Gemini Code Assist fonctionne avec tous les langages de programmation du domaine public, tels que Python, JavaScript et Java.
- **Valider les suggestions** : Reveuez toujours le code généré par l'IA, car il peut parfois être plausible mais incorrect.
- **Confidentialité** : Vous pouvez ajuster les paramètres d'utilisation des données dans l'extension pour qu'ils correspondent à vos préférences.

---

### Considérations potentielles
- **Réseau** : Si vous êtes derrière un proxy, configurez les paramètres réseau de VSCode en conséquence.
- **Limites d'utilisation** : La version gratuite fournit jusqu'à 6 000 requêtes liées au code et 240 requêtes de chat par jour, ce qui est amplement suffisant pour la plupart des utilisateurs.
- **Intégration GitHub** : Pour les revues de code alimentées par l'IA sur GitHub, une configuration supplémentaire est requise, mais celle-ci est distincte de la fonctionnalité principale de l'IDE.

---

En suivant ces étapes, vous pouvez utiliser efficacement Gemini Code Assist pour rationaliser vos tâches de codage dans VSCode. Pour plus de détails, consultez la documentation officielle de Google.